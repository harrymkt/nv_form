# controls_count
The number of controls in this form, except hidden ones. Read only.

`uint controls_count;`

## Remarks:
To modify this function, implement the following syntax:
```NVGT
uint get_controls_count() const property {
	return 0;
}
```
