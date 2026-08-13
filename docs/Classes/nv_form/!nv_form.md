# nv_form
This class facilitates the easy creation of user interfaces that convey their usage entirely through audio.

## Notes:
- many of the methods in this class only work on certain types of controls, and will return false if used on invalid types of controls.
- Exceptions are not used here. Instead, we indicate errors through `nv_form::get_last_error()`. Please note that this is only for compatibility with old form, and can be removed anytime. It is better to rely on return values.
- A form object can have unlimited controls by default.
