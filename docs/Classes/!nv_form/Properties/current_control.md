# current_control
Retrieves the currently focused control.

`nv_form_control@ current_control;`

## Returns:
`nv_form_control@`: A handle to the currently focused control on success, null otherwise.

## Remarks:
To modify this function, implement the following syntax:
```NVGT
nv_form_control@ get_current_control() const property {
	return null;
}
```
