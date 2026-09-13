# add_progress_bar
Creates a new progress bar and adds it to the form.

`nv_form_progress_bar@ add_progress_bar(const string &in caption, const string &in id = "", double min = 0, double max = 100, double initial = 0.0, int position = -1);`

## Arguments:
- `const string &in caption`: The label to associate.
- `const string &in id = ""`: The ID.
- `double min = 0`: The minimum value.
- `double max = 100`: The maximum value.
- `double initial = 0`: The initial value.
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_progress_bar@`: A handle to the control on success, null otherwise.
