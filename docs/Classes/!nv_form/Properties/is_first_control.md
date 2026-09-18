# is_first_control
Determine if the current control is the first in this form, only non hidden control. Read only.

`bool is_first_control;`

## Remarks:
To modify this function, implement the following syntax:
```NVGT
bool get_is_first_control() const property {
	return false;
}
```
