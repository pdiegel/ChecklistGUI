# Checklist Application

This is a simple checklist application written in Python using the dearpygui library. It allows users to create a checklist of items and track their progress by checking and unchecking items. It also includes a timer feature that can be used to time events in the GUI.

## Getting Started

To run the application, you'll need to have Python 3 and the dearpygui library installed on your computer. You can install the library using pip:

```
pip install dearpygui
```

Once you have the library installed, you can run the application by executing the `main.py` file:

```
python main.py
```

## Usage

When you run the application, a GUI window will appear with a list of checkboxes for each item in the checklist. You can check and uncheck items as you complete them, and the application will display the percentage of items completed.

You can also use the timer feature to time events in the GUI. Click the "Start" button to start the timer, the "Pause" button to pause the timer, and the "Stop" button to stop and reset the timer. The elapsed time will be displayed in seconds, minutes, or hours depending on the duration.

## Customization

The checklist items are stored in a file called `labels.txt`. You can customize the items by editing this file and adding or removing items.

The font used in the GUI can be customized by replacing the `f2.ttf` file in the `fonts` directory with another font file.

## License

This application is licensed under the MIT License. See the `LICENSE` file for details.