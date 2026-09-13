# create_window
Creates a window to show form controls.

`bool create_window(const string &in window_title, bool change_screen_title = true, bool say_dialog = true, bool silent = false);`

## Arguments:
- `const string &in window_title`: The title of the window.
- `bool change_screen_title = true`: Whether or not the main window's title should be set as well.
- `bool say_dialog = true`: Whether or not the window should be reported as a dialog (in the context of the form).
- `bool silent = false`: Should this window be shown silently?

## Returns:
`bool`: `true` on success, `false` on failure.

## Remarks:
This method initializes title, and other necessary actions for controls, including the setting up of touch gestures.
