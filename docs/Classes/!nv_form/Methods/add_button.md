# add_button
Creates a new button and adds it to the form.

`nv_form_button@add_button(string caption, string id = "", bool primary = false, bool cancel = false, int position = -1, nv_form_control_callback@callback = null);`

## Arguments:
- `string caption`: the label to associate with the button.
- `string id = ""`: The ID.
- `bool primary = false`: Should this button be activated by pressing enter anywhere in the form?
- `bool cancel = false`: Should this button be activated by pressing escape anywhere in the form?
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_button@`: An NV control button type on success, null otherwise.
