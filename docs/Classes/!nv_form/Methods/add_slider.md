# add_slider
Creates a new slider and adds it to the form.

`nv_form_slider@ add_slider(const string &in caption, const string &in id = "", double min = 0, double max = 100, double step = 1, double initial = 0, double page = 0, int position = -1, dictionary@ text = null);`

## Arguments:
- `const string &in caption`: The label to associate.
- `const string &in id = ""`: The ID.
- `double min = 0`: The minimum value.
- `double max = 100`: The maximum value.
- `double step = 1`: Step size when pressing arrow keys.
- `double initial = 0`: The initial value.
- `double page = 0`: Page size, the number of values that will be increased or decreased when you press PageUp and PageDown. If this is set to 0, the page size will be the step size value multiplied by 10.
- `int position = -1`: The position to insert at.
- `dictionary@ text = null`: Text values.

## Returns:
`nv_form_slider@`: A handle to the control on success, null otherwise.
