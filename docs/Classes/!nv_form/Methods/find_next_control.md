# find_next_control
Returns the next or previous control relative to the current position. It skips through the hidden controls.

`nv_form_control@find_next_control(bool next = true, bool wrap = true) const`

## Arguments:
- `bool next = true`: Should this method find next or previous control?
- `bool wrap = true`: Will the control position wrap around?

## Returns:
`nv_form_control@`: A handle to the control on success, null otherwise.
