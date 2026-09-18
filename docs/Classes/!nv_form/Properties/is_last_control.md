# is_last_control
Determine if the current control is the last in this form, only non hidden control. Read only.

`bool is_last_control;`

## Remarks:
To modify this function, implement the following syntax:
```NVGT
bool get_is_last_control() const property {
	return false;
}
```
