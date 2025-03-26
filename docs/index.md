---
title: Overview
hide:
- feedback
---

--8<-- "README.md"

## Example

Let say we have a script called `drag` in a scripts folder,
enabling a drag-drop feature on the command-line.

<details class="info" markdown=1><summary>View the script's contents:</summary>

```sh
--8<-- "docs/examples/drag"
```

</details>

*The documentation syntax used in this script
is documented here: https://pawamoy.github.io/shellman/usage/syntax/.*

We can inject documentation for our script using this markup:

```md
::: scripts/drag
    handler: shell
```

...which would render the following documentation:

::: docs/examples/drag
    handler: shell
    options:
      heading_level: 2
