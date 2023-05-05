import dearpygui.dearpygui as dpg
import timer

with open("labels.txt", "r") as f:
    LABELS = [line for line in f.readlines()]

NUM_LABELS = len(LABELS)
PAUSE_RESUME_TAG = "pause_resume"
DISPLAY_TAG = "elapsed_time"
TIME_TYPE_TAG = "time_type"

# Initialize a timer object
program_timer = timer.Timer(PAUSE_RESUME_TAG, DISPLAY_TAG, TIME_TYPE_TAG)


def get_num_checked() -> int:
    """Returns the number of checkboxes that are checked."""
    num_checked = [label for label in LABELS if dpg.get_value(label)]
    return num_checked


def reset_checkboxes() -> None:
    """Resets all checkboxes to unchecked."""
    first_item_checked = dpg.get_value(LABELS[0])
    for label in LABELS:
        if first_item_checked:
            val = False
        else:
            val = True
        dpg.set_value(label, val)


dpg.create_context()
FONT = r"fonts\f2.ttf"

with dpg.font_registry():
    default_font = dpg.add_font(FONT, 18)

with dpg.handler_registry():
    dpg.add_key_press_handler(dpg.mvKey_Spacebar, callback=reset_checkboxes)

with dpg.value_registry():
    dpg.add_bool_value(default_value=True, tag="bool_value")
    dpg.add_string_value(default_value="Default string", tag="string_value")

with dpg.window(
    label="Checkbox",
    width=400,
    height=760,
    no_move=True,
    no_close=True,
    no_title_bar=True,
    no_resize=True,
):
    with dpg.group(horizontal=True):
        dpg.add_text("File Number:")
        dpg.add_input_text(width=65)
        dpg.add_spacer(width=50)
        dpg.add_text("5", tag="completion_percentage")
    for label in LABELS:
        formatted_label = label.strip("\n")
        while len(formatted_label) < 90:
            formatted_label = f"{formatted_label} "
        dpg.add_checkbox(label=formatted_label, tag=label)
    with dpg.group(horizontal=True):
        btn_height = 30
        btn_width = 70
        dpg.add_button(
            label="Start",
            height=btn_height,
            width=btn_width,
            callback=program_timer.start_timer,
        )
        dpg.add_button(
            label="Pause",
            height=btn_height,
            width=btn_width,
            callback=program_timer.pause_resume_timer,
            tag=PAUSE_RESUME_TAG,
        )
        dpg.add_button(
            label="Stop",
            height=btn_height,
            width=btn_width,
            callback=program_timer.stop_timer,
        )
    with dpg.group(horizontal=True):
        dpg.add_text("Elapsed Time: ")
        dpg.add_text("0", tag=DISPLAY_TAG)
        dpg.add_text("Seconds", tag=TIME_TYPE_TAG)

dpg.bind_font(default_font)

dpg.create_viewport(
    title="Custom Title", width=400, height=760, resizable=False
)
dpg.setup_dearpygui()
dpg.show_viewport()

while dpg.is_dearpygui_running():
    program_timer.advance_time()

    num_checked = get_num_checked()
    num_checked = len(num_checked)
    dpg.set_value(
        "elapsed_time", f"{program_timer.display_time(TIME_TYPE_TAG)}"
    )
    dpg.set_value(
        "completion_percentage",
        f"{num_checked}/{NUM_LABELS}\
    {round((num_checked/NUM_LABELS)*100, 2)}% Complete.",
    )
    dpg.render_dearpygui_frame()

dpg.destroy_context()
