### Approach

The approach was pointed out pretty clear in the course. 

The purpose of an HTTP Router is to take a URL path like `/`, `/about`, or `/blog/2019-01-15/my-awesome-blog-post` and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node `/`

A sensible way to split things would be on the parts of the path that are separated by slashes (`/`). A Trie with a single path entry of: "/about/me" would look like:
> (root, None) -> ("about", None) -> ("me", "About Me handler")

### Efficiency
- Time complexity: add_handler and lookup need `O(L)`, 
where `L` = number of parts in the path.
- Space complexity: `O(R*L)`, where `R` = number of routes, 
`L` = number of parts in a path
