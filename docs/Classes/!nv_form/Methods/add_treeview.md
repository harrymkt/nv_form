# add_treeview
Creates a new tree view and adds it to the form.

`nv_form_treeview@add_treeview(const string &in caption, const string &in id = "", nv_form_tree_node@[] nodes = {}, int position = -1);`

## Arguments:
- `const string &in caption`: The label to associate with the tree.
- `const string &in id = ""`: The ID.
- `nv_form_tree_node@[] nodes = {}`: The initial top level nodes.
- `int position = -1`: The position to insert at.

## Returns:
`nv_form_treeview@`: The tree on success, null otherwise.

## Remarks:
This adds the `nv_form_treeview` control.

Any nodes you pass here are added as they are, the visible list is rebuilt for you afterwards.
