# create_window
Creates a window to show form controls.

`bool create_window(string window_title, bool change_screen_title = true, bool say_dialog = true, bool silent = false);`

## Arguments:
- `string window_title`: The title of the window.
- `bool change_screen_title = true`: Whether or not the main window's title should be set as well.
- `bool say_dialog = true`: Whether or not the window should be reported as a dialog (in the context of the form).
- `bool silent = false`: Should this window be shown silently?

## Returns:
`bool`: `true` on success, `false` on failure.
