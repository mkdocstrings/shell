# Configuration

This page lists the available configuration options and what they achieve.

[](){#setting-options}
## `options`

You can specify a few configuration options under the `options` key:

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      shell:
        options:
          # some configuration
```

[](){#option-extra}
### `extra`

- **:octicons-package-24: Type [`dict`][] :material-equal: `{}`{ title="default value" }**

The `extra` option lets you inject additional variables into the Jinja context used when rendering templates. You can then use this extra context in your [overridden templates](https://mkdocstrings.github.io/usage/theming/#templates).

Local `extra` options will be merged into the global `extra` option:

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      shell:
        options:
          extra:
            hello: world
```

```md title="in docs/some_page.md (local configuration)"
::: your_package.your_module.your_func
    handler: shell
    options:
      extra:
        foo: bar
```

...will inject both `hello` and `foo` into the Jinja context when rendering `your_package.your_module.your_func`.

[](){#option-heading_level}
### `heading_level`

- **:octicons-package-24: Type [`int`][] :material-equal: `2`{ title="default value" }**

The initial heading level to use.

When injecting documentation for an object,
the object itself and its members are rendered.
For each layer of objects, we increase the heading level by 1.

The initial heading level will be used for the first layer.
If you set it to 3, then headings will start with `<h3>`.

If the [heading for the root object][show_root_heading] is not shown,
then the initial heading level is used for its members.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      shell:
        options:
          heading_level: 2
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.module
    handler: shell
    options:
      heading_level: 3
```

/// admonition | Preview
    type: preview

//// tab | With level 3 and root heading
<h3><code>module</code> (3)</h3>
<p>Docstring of the module.</p>
<h4><code>ClassA</code> (4)</h4>
<p>Docstring of class A.</p>
<h4><code>ClassB</code> (4)</h4>
<p>Docstring of class B.</p>
<h5><code>method_1</code> (5)</h5>
<p>Docstring of the method.</p>
////

//// tab | With level 3, without root heading
<p>Docstring of the module.</p>
<h3><code>ClassA</code> (3)</h3>
<p>Docstring of class A.</p>
<h3><code>ClassB</code> (3)</h3>
<p>Docstring of class B.</p>
<h4><code>method_1</code> (4)</h4>
<p>Docstring of the method.</p>
////
///

[](){#option-show_root_heading}
### `show_root_heading`

- **:octicons-package-24: Type [`bool`][] :material-equal: `False`{ title="default value" }**

Show the heading of the object at the root of the documentation tree
(i.e. the object referenced by the identifier after `:::`).

While this option defaults to false for backwards compatibility, we recommend setting it to true. Note that the heading of the root object can be a level 1 heading (the first on the page):

```md
# ::: path.to.object
```

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      shell:
        options:
          show_root_heading: false
```

```md title="or in docs/some_page.md (local configuration)"
::: path.to.Class
    handler: shell
    options:
      show_root_heading: true
```

[](){#option-show_root_toc_entry}
### `show_root_toc_entry`

- **:octicons-package-24: Type [`bool`][] :material-equal: `True`{ title="default value" }**
<!-- - **:octicons-project-template-24: Template :material-null:** (N/A) -->

If the root heading is not shown, at least add a ToC entry for it.

If you inject documentation for an object in the middle of a page,
after long paragraphs, and without showing the [root heading][show_root_heading],
then you will not be able to link to this particular object
as it won't have a permalink and will be "lost" in the middle of text.
In that case, it is useful to add a hidden anchor to the document,
which will also appear in the table of contents.

In other cases, you might want to disable the entry to avoid polluting the ToC.
It is not possible to show the root heading *and* hide the ToC entry.

```yaml title="in mkdocs.yml (global configuration)"
plugins:
- mkdocstrings:
    handlers:
      shell:
        options:
          show_root_heading: false
          show_root_toc_entry: true
```

```md title="or in docs/some_page.md (local configuration)"
## Some heading

Lots of text.

::: path.to.object
    handler: shell
    options:
      show_root_heading: false
      show_root_toc_entry: false

## Other heading.

More text.
```

/// admonition | Preview
    type: preview

//// tab | With ToC entry
**Table of contents**<br>
[Some heading](#permalink-to-some-heading){ title="#permalink-to-some-heading" }<br>
[`object`](#permalink-to-object){ title="#permalink-to-object" }<br>
[Other heading](#permalink-to-other-heading){ title="#permalink-to-other-heading" }
////

//// tab | Without ToC entry
**Table of contents**<br>
[Some heading](#permalink-to-some-heading){ title="#permalink-to-some-heading" }<br>
[Other heading](#permalink-to-other-heading){ title="#permalink-to-other-heading" }
////
///
