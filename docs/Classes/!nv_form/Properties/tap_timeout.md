# tap_timeout
A defined number of milliseconds that takes between each tap in multitap shortcuts.

`int tap_timeout = 200;`

## Remarks:
To modify this function, implement the following syntax:
```NVGT
int tap_timeout {
	get const {
		return __tap_timeout;
	}
	set {
	}
}
```
