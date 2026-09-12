# add_checkbox
Creates a new checkbox and adds it to the form.

`nv_form_checkbox@add_checkbox(string caption, string id = "", bool selected = false, int position = -1);`

## Arguments:
- `string caption`: the label to associate with the checkbox.
- `string id = ""`: The ID.
- `bool selected = false`: Should this checkbox be checked by default?
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_checkbox@`: An NV control checkbox type on success, null otherwise.
