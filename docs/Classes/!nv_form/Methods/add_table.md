# add_table
Creates a new table and adds it to the form.

`nv_form_table@add_table(const string &in caption, const string &in id = "", int position = -1, bool speak_position = false);`

## Arguments:
- `const string &in caption`: The label to associate with the table.
- `const string &in id = ""`: The ID.
- `int position = -1`: The position to insert at.
- `bool speak_position = false`: Should the row and column numbers be spoken along with each cell?

## Returns:
`nv_form_table@`: The table on success, null otherwise.

## Remarks:
The table starts empty. Call `set_headers` on the returned handle before adding rows, because the number of headers is what decides how many columns the user can reach.

This method is specific to this fork.
