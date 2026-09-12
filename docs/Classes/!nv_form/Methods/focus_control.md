# focus_control
Set a particular control to have the keyboard focus, and notify the user.

`bool focus_control(nv_form_control@ctrl, bool quiet = false, bool interupt_previous_speech = true);`

## Arguments:
- `nv_form_control@ctrl`: The control to focus.
- `bool quiet = false`: Should this be silently focused?
- `bool interupt_previous_speech = true`: Should previous speech be interrupted when focused.

## Returns:
`bool`: `true` if the control was successfully focused, `false` otherwise.
