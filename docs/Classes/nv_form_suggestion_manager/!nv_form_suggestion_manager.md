# nv_form_suggestion_manager
Autocomplete for a text field. Offers a list of entries that start with what the user has typed so far.

`nv_form_suggestion_manager(nv_form@ parent_form, nv_form_input@ owner_input, bool speak_position = false, int page_size = 10);`

## Arguments:
- `nv_form@ parent_form`: The form the owning input belongs to.
- `nv_form_input@ owner_input`: The text field this manager completes.
- `bool speak_position = false`: Toggle whether the manager should speak the position, "X of Y".
- `int page_size = 10`: The step size when Page Up / Down keys are used.

## Remarks:
Assign the manager to the `suggestion_manager` property of an input and everything else is automatic. The input calls `update` whenever its text changes, whether the user typed, deleted, or pasted.

Unlike the other `nv_utility_form` implementations, this one deliberately does not take the input focus. Its `monitor` is empty, and the parent form instead forwards the arrow keys, Enter, Tab and Escape to `handle_key`, so the user keeps typing in the field while the suggestion list is open.

Matching is case insensitive and anchored at the start of the entry. An empty field matches nothing and closes the list.
