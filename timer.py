import dearpygui.dearpygui as dpg
from datetime import datetime, timedelta


class Timer:
    """This class represents a timer object that can be used to time
    events in the GUI."""

    def __init__(self, pause_tag, display_tag, time_type_tag):
        self.time = "0"
        self.started = False
        self.paused = True
        self.pause_tag = pause_tag
        self.display_tag = display_tag
        self.time_type = time_type_tag
        self.elapsed_pause = timedelta(0)

    def advance_time(self) -> None:
        """This function is called every frame to update the timer.
        The dearpygui render loop runs at 60 fps."""
        if self.paused:
            return
        self.time = datetime.now() - self.start_time - self.elapsed_pause

    def reset_timer(self) -> None:
        """Resets the timer to 0."""
        self.time = "0"
        self.started = False
        self.elapsed_pause = timedelta(0)

    def resume_timer(self) -> None:
        """Resumes the timer."""
        self.paused = False
        self.elapsed_pause += datetime.now() - self.time_paused

    def pause_timer(self) -> None:
        """Pauses the timer."""
        self.paused = True
        self.time_paused = datetime.now()

    def pause_resume_timer(self, sender) -> None:
        """This function is called when the pause/resume button is
        pressed."""
        if not self.started:
            return

        self.set_button_label(sender)
        if self.paused:
            self.resume_timer()
        else:
            self.pause_timer()

    def display_time(self, sender) -> str:
        """Returns the time in seconds, minutes, or hours."""
        string_time = str(self.time)
        time_format = "Seconds"
        if string_time != "0":
            seconds = float(string_time.split(":")[2])
            minutes = float(string_time.split(":")[1]) + (seconds / 60)
            hours = float(string_time.split(":")[0]) + (minutes / 60)
            output = seconds
            if minutes >= 1:
                if hours >= 1:
                    time_format = "Hours"
                    output = hours
                else:
                    time_format = "Minutes"
                    output = minutes
        else:
            output = 0

        dpg.set_value(sender, time_format)
        return "{:.2f}".format(output)

    def set_button_label(self, sender) -> None:
        """Sets the label of the pause/resume button."""
        if self.paused or self.time == 0:
            label = "Pause"
        else:
            label = "Resume"
        dpg.set_item_label(sender, label)

    def start_timer(self) -> None:
        """Starts the timer."""
        if not self.started:
            self.started = True
            self.start_time = datetime.now()
            self.paused = False

    def stop_timer(self) -> None:
        """Stops and resets the timer."""
        if not self.started:
            return

        if not self.paused:
            self.pause_timer()
        self.reset_timer()
        self.set_button_label(self.pause_tag)
