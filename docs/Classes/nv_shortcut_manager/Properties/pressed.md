# pressed
Returns a handle to `nv_shortcut` class with the shortcut that is currently pressed.

`nv_shortcut@ pressed;`

## Remarks:
When using this property, necessary actions are automatically executed, i.e. clearing active unnecessary shortcuts.

To modify this function, implement the following syntax:
```NVGT
nv_shortcut@ get_pressed() property {
	return null;
}
```
