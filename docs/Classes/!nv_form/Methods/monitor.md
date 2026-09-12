# monitor
Processes all keyboard input, and dispatches all events to the form. Should be called in your main loop.

`bool monitor();`

## Returns:
`bool`: `true` on success, `false` on failure.

## Remarks:
If this function returns `false`, it means the form should now be exit and thus the loop should be break. You can also do `while(f.monitor())` instead.
