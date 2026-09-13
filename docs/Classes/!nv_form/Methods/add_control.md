# add_control
Adds a new control into the form.

`bool add_control(nv_form_control@ctrl, bool primary = false, bool cancel = false, int position = -1, nv_form_control_callback@callback = null);`

## Arguments:
- `nv_form_control@ctrl`: A handle to the control you wish to add.
- `bool primary = false`: Set as primary control.
- `bool cancel = false`: Set as cancel control.
- `int position = -1`: The position to insert at. -1 is append.
- `nv_form_control_callback@callback = null`: Control callback.

## Returns:
`bool`: `true` on success, `false` on failure.

## Remarks:
This method is useful if you make a child class of a control.
