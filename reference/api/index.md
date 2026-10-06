# shell

Shell handler for mkdocstrings.

Modules:

- **`config`** – Deprecated. Import from mkdocstrings_handlers.shell directly.
- **`handler`** – Deprecated. Import from mkdocstrings_handlers.shell directly.

Classes:

- **`ShellConfig`** – Shell handler configuration.
- **`ShellHandler`** – The Shell handler class.
- **`ShellInputConfig`** – Shell handler configuration.
- **`ShellInputOptions`** – Accepted input options.
- **`ShellOptions`** – Final options passed as template context.

Functions:

- **`get_handler`** – Simply return an instance of ShellHandler.

## ShellConfig

```
ShellConfig(*, options: dict[str, Any] = dict())
```

Bases: `ShellInputConfig`

Shell handler configuration.

Methods:

- **`coerce`** – Coerce data.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`options`** (`dict[str, Any]`) – Global options in mkdocs.yml.

### options

```
options: dict[str, Any] = field(default_factory=dict)
```

Global options in mkdocs.yml.

### coerce

```
coerce(**data: Any) -> MutableMapping[str, Any]
```

Coerce data.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def coerce(cls, **data: Any) -> MutableMapping[str, Any]:
    """Coerce data."""
    return super().coerce(**data)
```

### from_data

```
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def from_data(cls, **data: Any) -> Self:
    """Create an instance from a dictionary."""
    return cls(**cls.coerce(**data))
```

## ShellHandler

```
ShellHandler(
    config: ShellConfig, base_dir: Path, **kwargs: Any
)
```

Bases: `BaseHandler`

The Shell handler class.

Methods:

- **`collect`** – Collect data from a shell script/library.
- **`do_convert_markdown`** – Render Markdown text; for use inside templates.
- **`do_heading`** – Render an HTML heading and register it for the table of contents. For use inside templates.
- **`get_aliases`** – Return the possible aliases for a given identifier.
- **`get_extended_templates_dirs`** – Load template extensions for the given handler, return their templates directories.
- **`get_headings`** – Return and clear the headings gathered so far.
- **`get_inventory_urls`** – Return the URLs (and configuration options) of the inventory files to download.
- **`get_options`** – Get the combined (global and local) options.
- **`get_templates_dir`** – Return the path to the handler's templates directory.
- **`load_inventory`** – Yield items and their URLs from an inventory file streamed from in_file.
- **`render`** – Render the collected data.
- **`render_backlinks`** – Render backlinks.
- **`teardown`** – Teardown the handler.
- **`update_env`** – Update the Jinja environment.

Attributes:

- **`base_dir`** – The base directory for the handler.
- **`config`** – The handler configuration.
- **`custom_templates`** – The path to custom templates.
- **`domain`** (`str`) – The cross-documentation domain/language for this handler.
- **`enable_inventory`** (`bool`) – Whether this handler is interested in enabling the creation of the objects.inv Sphinx inventory file.
- **`env`** – The Jinja environment.
- **`extra_css`** (`str`) – Extra CSS.
- **`fallback_theme`** (`str`) – The theme to fallback to.
- **`global_options`** – The global options for the handler.
- **`md`** (`Markdown`) – The Markdown instance.
- **`mdx`** – The Markdown extensions to use.
- **`mdx_config`** – The configuration for the Markdown extensions.
- **`name`** (`str`) – The handler's name.
- **`outer_layer`** (`bool`) – Whether we're in the outer Markdown conversion layer.
- **`theme`** – The selected theme.

Source code in `src/mkdocstrings_handlers/shell/_internal/handler.py`

```
def __init__(self, config: ShellConfig, base_dir: Path, **kwargs: Any) -> None:
    super().__init__(**kwargs)
    self.config = config
    """The handler configuration."""
    self.base_dir = base_dir
    """The base directory for the handler."""
    self.global_options = config.options
    """The global options for the handler."""
```

### base_dir

```
base_dir = base_dir
```

The base directory for the handler.

### config

```
config = config
```

The handler configuration.

### custom_templates

```
custom_templates = custom_templates
```

The path to custom templates.

### domain

```
domain: str = 'shell'
```

The cross-documentation domain/language for this handler.

### enable_inventory

```
enable_inventory: bool = False
```

Whether this handler is interested in enabling the creation of the `objects.inv` Sphinx inventory file.

### env

```
env = Environment(
    autoescape=True,
    loader=FileSystemLoader(paths),
    auto_reload=False,
)
```

The Jinja environment.

### extra_css

```
extra_css: str = ''
```

Extra CSS.

### fallback_theme

```
fallback_theme: str = 'material'
```

The theme to fallback to.

### global_options

```
global_options = config.options
```

The global options for the handler.

### md

```
md: Markdown
```

The Markdown instance.

Raises:

- `RuntimeError` – When the Markdown instance is not set yet.

### mdx

```
mdx = mdx
```

The Markdown extensions to use.

### mdx_config

```
mdx_config = mdx_config
```

The configuration for the Markdown extensions.

### name

```
name: str = 'shell'
```

The handler's name.

### outer_layer

```
outer_layer: bool
```

Whether we're in the outer Markdown conversion layer.

### theme

```
theme = theme
```

The selected theme.

### collect

```
collect(
    identifier: str, options: ShellOptions
) -> CollectorItem
```

Collect data from a shell script/library.

Source code in `src/mkdocstrings_handlers/shell/_internal/handler.py`

```
def collect(self, identifier: str, options: ShellOptions) -> CollectorItem:  # noqa: ARG002
    """Collect data from a shell script/library."""
    script_path = self.base_dir / identifier
    try:
        return DocFile(str(script_path))
    except FileNotFoundError as error:
        raise CollectionError(f"Could not find script '{script_path}'") from error
```

### do_convert_markdown

```
do_convert_markdown(
    text: str,
    heading_level: int,
    html_id: str = "",
    *,
    strip_paragraph: bool = False,
    autoref_hook: AutorefsHookInterface | None = None,
) -> Markup
```

Render Markdown text; for use inside templates.

Parameters:

- **`text`** (`str`) – The text to convert.
- **`heading_level`** (`int`) – The base heading level to start all Markdown headings from.
- **`html_id`** (`str`, default: `''` ) – The HTML id of the element that's considered the parent of this element.
- **`strip_paragraph`** (`bool`, default: `False` ) – Whether to exclude the <p> tag from around the whole output.

Returns:

- `Markup` – An HTML string.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def do_convert_markdown(
    self,
    text: str,
    heading_level: int,
    html_id: str = "",
    *,
    strip_paragraph: bool = False,
    autoref_hook: AutorefsHookInterface | None = None,
) -> Markup:
    """Render Markdown text; for use inside templates.

    Arguments:
        text: The text to convert.
        heading_level: The base heading level to start all Markdown headings from.
        html_id: The HTML id of the element that's considered the parent of this element.
        strip_paragraph: Whether to exclude the `<p>` tag from around the whole output.

    Returns:
        An HTML string.
    """
    global _markdown_conversion_layer  # noqa: PLW0603
    _markdown_conversion_layer += 1
    treeprocessors = self.md.treeprocessors
    treeprocessors[HeadingShiftingTreeprocessor.name].shift_by = heading_level
    treeprocessors[IdPrependingTreeprocessor.name].id_prefix = html_id and html_id + "--"
    treeprocessors[ParagraphStrippingTreeprocessor.name].strip = strip_paragraph
    if BacklinksTreeProcessor.name in treeprocessors:
        treeprocessors[BacklinksTreeProcessor.name].initial_id = html_id
    if autoref_hook and AutorefsInlineProcessor.name in self.md.inlinePatterns:
        self.md.inlinePatterns[AutorefsInlineProcessor.name].hook = autoref_hook  # ty: ignore[unresolved-attribute]

    try:
        return Markup(self.md.convert(text))
    finally:
        treeprocessors[HeadingShiftingTreeprocessor.name].shift_by = 0
        treeprocessors[IdPrependingTreeprocessor.name].id_prefix = ""
        treeprocessors[ParagraphStrippingTreeprocessor.name].strip = False
        if BacklinksTreeProcessor.name in treeprocessors:
            treeprocessors[BacklinksTreeProcessor.name].initial_id = None
        if AutorefsInlineProcessor.name in self.md.inlinePatterns:
            self.md.inlinePatterns[AutorefsInlineProcessor.name].hook = None  # ty: ignore[unresolved-attribute]
        self.md.reset()
        _markdown_conversion_layer -= 1
```

### do_heading

```
do_heading(
    content: Markup,
    heading_level: int,
    *,
    role: str | None = None,
    hidden: bool = False,
    toc_label: str | None = None,
    skip_inventory: bool = False,
    **attributes: str,
) -> Markup
```

Render an HTML heading and register it for the table of contents. For use inside templates.

Parameters:

- **`content`** (`Markup`) – The HTML within the heading.
- **`heading_level`** (`int`) – The level of heading (e.g. 3 -> h3).
- **`role`** (`str | None`, default: `None` ) – An optional role for the object bound to this heading.
- **`hidden`** (`bool`, default: `False` ) – If True, only register it for the table of contents, don't render anything.
- **`toc_label`** (`str | None`, default: `None` ) – The title to use in the table of contents ('data-toc-label' attribute).
- **`skip_inventory`** (`bool`, default: `False` ) – Flag element to not be registered in the inventory (by setting a data-skip-inventory attribute).
- **`**attributes`** (`str`, default: `{}` ) – Any extra HTML attributes of the heading.

Returns:

- `Markup` – An HTML string.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def do_heading(
    self,
    content: Markup,
    heading_level: int,
    *,
    role: str | None = None,
    hidden: bool = False,
    toc_label: str | None = None,
    skip_inventory: bool = False,
    **attributes: str,
) -> Markup:
    """Render an HTML heading and register it for the table of contents. For use inside templates.

    Arguments:
        content: The HTML within the heading.
        heading_level: The level of heading (e.g. 3 -> `h3`).
        role: An optional role for the object bound to this heading.
        hidden: If True, only register it for the table of contents, don't render anything.
        toc_label: The title to use in the table of contents ('data-toc-label' attribute).
        skip_inventory: Flag element to not be registered in the inventory (by setting a `data-skip-inventory` attribute).
        **attributes: Any extra HTML attributes of the heading.

    Returns:
        An HTML string.
    """
    # Produce a heading element that will be used later, in `AutoDocProcessor.run`, to:
    # - register it in the ToC: right now we're in the inner Markdown conversion layer,
    #   so we have to bubble up the information to the outer Markdown conversion layer,
    #   for the ToC extension to pick it up.
    # - register it in autorefs: right now we don't know what page is being rendered,
    #   so we bubble up the information again to where autorefs knows the page,
    #   and can correctly register the heading anchor (id) to its full URL.
    # - register it in the objects inventory: same as for autorefs,
    #   we don't know the page here, or the handler (and its domain),
    #   so we bubble up the information to where the mkdocstrings extension knows that.
    el = Element(f"h{heading_level}", attributes)
    if toc_label is None:
        toc_label = content.unescape() if isinstance(content, Markup) else content
    el.set("data-toc-label", toc_label)
    if skip_inventory:
        el.set("data-skip-inventory", "true")
    if role:
        el.set("data-role", role)
    if content:
        el.text = str(content).strip()
    self._headings.append(el)

    if hidden:
        return Markup('<a id="{0}"></a>').format(attributes["id"])

    # Now produce the actual HTML to be rendered. The goal is to wrap the HTML content into a heading.
    # Start with a heading that has just attributes (no text), and add a placeholder into it.
    el = Element(f"h{heading_level}", attributes)
    el.append(Element("mkdocstrings-placeholder"))
    # Tell the inner 'toc' extension to make its additions if configured so.
    toc = cast("TocTreeprocessor", self.md.treeprocessors["toc"])
    if toc.use_anchors:
        toc.add_anchor(el, attributes["id"])
    if toc.use_permalinks:
        toc.add_permalink(el, attributes["id"])

    # The content we received is HTML, so it can't just be inserted into the tree. We had marked the middle
    # of the heading with a placeholder that can never occur (text can't directly contain angle brackets).
    # Now this HTML wrapper can be "filled" by replacing the placeholder.
    html_with_placeholder = tostring(el, encoding="unicode")
    assert (  # noqa: S101
        html_with_placeholder.count("<mkdocstrings-placeholder />") == 1
    ), f"Bug in mkdocstrings: failed to replace in {html_with_placeholder!r}"
    html = html_with_placeholder.replace("<mkdocstrings-placeholder />", content)
    return Markup(html)
```

### get_aliases

```
get_aliases(identifier: str) -> tuple[str, ...]
```

Return the possible aliases for a given identifier.

Parameters:

- **`identifier`** (`str`) – The identifier to get the aliases of.

Returns:

- `tuple[str, ...]` – A tuple of strings - aliases.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def get_aliases(self, identifier: str) -> tuple[str, ...]:  # noqa: ARG002
    """Return the possible aliases for a given identifier.

    Arguments:
        identifier: The identifier to get the aliases of.

    Returns:
        A tuple of strings - aliases.
    """
    return ()
```

### get_extended_templates_dirs

```
get_extended_templates_dirs(handler: str) -> list[Path]
```

Load template extensions for the given handler, return their templates directories.

Parameters:

- **`handler`** (`str`) – The name of the handler to get the extended templates directory of.

Returns:

- `list[Path]` – The extensions templates directories.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def get_extended_templates_dirs(self, handler: str) -> list[Path]:
    """Load template extensions for the given handler, return their templates directories.

    Arguments:
        handler: The name of the handler to get the extended templates directory of.

    Returns:
        The extensions templates directories.
    """
    discovered_extensions = entry_points(group=f"mkdocstrings.{handler}.templates")
    return [extension.load()() for extension in discovered_extensions]
```

### get_headings

```
get_headings() -> Sequence[Element]
```

Return and clear the headings gathered so far.

Returns:

- `Sequence[Element]` – A list of HTML elements.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def get_headings(self) -> Sequence[Element]:
    """Return and clear the headings gathered so far.

    Returns:
        A list of HTML elements.
    """
    result = list(self._headings)
    self._headings.clear()
    return result
```

### get_inventory_urls

```
get_inventory_urls() -> list[tuple[str, dict[str, Any]]]
```

Return the URLs (and configuration options) of the inventory files to download.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def get_inventory_urls(self) -> list[tuple[str, dict[str, Any]]]:
    """Return the URLs (and configuration options) of the inventory files to download."""
    return []
```

### get_options

```
get_options(
    local_options: Mapping[str, Any],
) -> HandlerOptions
```

Get the combined (global and local) options.

Source code in `src/mkdocstrings_handlers/shell/_internal/handler.py`

```
def get_options(self, local_options: Mapping[str, Any]) -> HandlerOptions:
    """Get the combined (global and local) options."""
    extra = {**self.global_options.get("extra", {}), **local_options.get("extra", {})}
    options = {**self.global_options, **local_options, "extra": extra}
    try:
        return ShellOptions.from_data(**options)
    except Exception as error:
        raise PluginError(f"Invalid options: {error}") from error
```

### get_templates_dir

```
get_templates_dir(handler: str | None = None) -> Path
```

Return the path to the handler's templates directory.

Override to customize how the templates directory is found.

Parameters:

- **`handler`** (`str | None`, default: `None` ) – The name of the handler to get the templates directory of.

Raises:

- `ModuleNotFoundError` – When no such handler is installed.
- `FileNotFoundError` – When the templates directory cannot be found.

Returns:

- `Path` – The templates directory path.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def get_templates_dir(self, handler: str | None = None) -> Path:
    """Return the path to the handler's templates directory.

    Override to customize how the templates directory is found.

    Arguments:
        handler: The name of the handler to get the templates directory of.

    Raises:
        ModuleNotFoundError: When no such handler is installed.
        FileNotFoundError: When the templates directory cannot be found.

    Returns:
        The templates directory path.
    """
    handler = handler or self.name
    try:
        import mkdocstrings_handlers  # noqa: PLC0415
    except ModuleNotFoundError as error:
        raise ModuleNotFoundError(f"Handler '{handler}' not found, is it installed?") from error

    for path in mkdocstrings_handlers.__path__:
        theme_path = Path(path, handler, "templates")
        if theme_path.exists():
            return theme_path

    raise FileNotFoundError(f"Can't find 'templates' folder for handler '{handler}'")
```

### load_inventory

```
load_inventory(
    in_file: BinaryIO,
    url: str,
    base_url: str | None = None,
    **kwargs: Any,
) -> Iterator[tuple[str, str]]
```

Yield items and their URLs from an inventory file streamed from `in_file`.

Parameters:

- **`in_file`** (`BinaryIO`) – The binary file-like object to read the inventory from.
- **`url`** (`str`) – The URL that this file is being streamed from (used to guess base_url).
- **`base_url`** (`str | None`, default: `None` ) – The URL that this inventory's sub-paths are relative to.
- **`**kwargs`** (`Any`, default: `{}` ) – Ignore additional arguments passed from the config.

Yields:

- `tuple[str, str]` – Tuples of (item identifier, item URL).

Source code in `mkdocstrings/_internal/handlers/base.py`

```
@classmethod
def load_inventory(
    cls,
    in_file: BinaryIO,  # noqa: ARG003
    url: str,  # noqa: ARG003
    base_url: str | None = None,  # noqa: ARG003
    **kwargs: Any,  # noqa: ARG003
) -> Iterator[tuple[str, str]]:
    """Yield items and their URLs from an inventory file streamed from `in_file`.

    Arguments:
        in_file: The binary file-like object to read the inventory from.
        url: The URL that this file is being streamed from (used to guess `base_url`).
        base_url: The URL that this inventory's sub-paths are relative to.
        **kwargs: Ignore additional arguments passed from the config.

    Yields:
        Tuples of (item identifier, item URL).
    """
    yield from ()
```

### render

```
render(
    data: CollectorItem,
    options: ShellOptions,
    *,
    locale: str | None = None,
) -> str
```

Render the collected data.

Source code in `src/mkdocstrings_handlers/shell/_internal/handler.py`

```
def render(self, data: CollectorItem, options: ShellOptions, *, locale: str | None = None) -> str:  # noqa: ARG002
    """Render the collected data."""
    heading_level = options.heading_level
    template = self.env.get_template("script.html.jinja")
    return template.render(
        config=options,
        filename=data.filename,
        script=data.sections,
        heading_level=heading_level,
    )
```

### render_backlinks

```
render_backlinks(
    backlinks: Mapping[str, Iterable[Backlink]],
    *,
    locale: str | None = None,
) -> str
```

Render backlinks.

Parameters:

- **`backlinks`** (`Mapping[str, Iterable[Backlink]]`) – A mapping of identifiers to backlinks.
- **`locale`** (`str | None`, default: `None` ) – The locale to use for translations, if any.

Returns:

- `str` – The rendered backlinks as HTML.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def render_backlinks(self, backlinks: Mapping[str, Iterable[Backlink]], *, locale: str | None = None) -> str:  # noqa: ARG002
    """Render backlinks.

    Parameters:
        backlinks: A mapping of identifiers to backlinks.
        locale: The locale to use for translations, if any.

    Returns:
        The rendered backlinks as HTML.
    """
    return ""
```

### teardown

```
teardown() -> None
```

Teardown the handler.

This method should be implemented to, for example, terminate a subprocess that was started when creating the handler instance.

Source code in `mkdocstrings/_internal/handlers/base.py`

```
def teardown(self) -> None:
    """Teardown the handler.

    This method should be implemented to, for example, terminate a subprocess
    that was started when creating the handler instance.
    """
```

### update_env

```
update_env(config: MkDocsConfig) -> None
```

Update the Jinja environment.

Source code in `src/mkdocstrings_handlers/shell/_internal/handler.py`

```
def update_env(self, config: MkDocsConfig) -> None:  # noqa: ARG002
    """Update the Jinja environment."""
    self.env.trim_blocks = True
    self.env.lstrip_blocks = True
    self.env.keep_trailing_newline = False
    self.env.filters.update(FILTERS)
```

## ShellInputConfig

```
ShellInputConfig(
    *,
    options: Annotated[
        ShellInputOptions,
        _Field(
            description="Configuration options for collecting and rendering objects."
        ),
    ] = ShellInputOptions(),
)
```

Shell handler configuration.

Methods:

- **`coerce`** – Coerce data.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`options`** (`Annotated[ShellInputOptions, _Field(description='Configuration options for collecting and rendering objects.')]`) – Configuration options for collecting and rendering objects.

### options

```
options: Annotated[
    ShellInputOptions,
    _Field(
        description="Configuration options for collecting and rendering objects."
    ),
] = field(default_factory=ShellInputOptions)
```

Configuration options for collecting and rendering objects.

### coerce

```
coerce(**data: Any) -> MutableMapping[str, Any]
```

Coerce data.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def coerce(cls, **data: Any) -> MutableMapping[str, Any]:
    """Coerce data."""
    return data
```

### from_data

```
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def from_data(cls, **data: Any) -> Self:
    """Create an instance from a dictionary."""
    return cls(**cls.coerce(**data))
```

## ShellInputOptions

```
ShellInputOptions(
    *,
    extra: Annotated[
        dict[str, Any],
        _Field(
            group="general", description="Extra options."
        ),
    ] = dict(),
    heading: Annotated[
        str,
        _Field(
            group="headings",
            description="A custom string to override the autogenerated heading of the root object.",
        ),
    ] = "",
    heading_level: Annotated[
        int,
        _Field(
            group="headings",
            description="The initial heading level to use.",
        ),
    ] = 2,
    show_symbol_type_heading: Annotated[
        bool,
        _Field(
            group="headings",
            description="Show the symbol type in headings (e.g. mod, class, meth, func and attr).",
        ),
    ] = False,
    show_symbol_type_toc: Annotated[
        bool,
        _Field(
            group="headings",
            description="Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).",
        ),
    ] = False,
    toc_label: Annotated[
        str,
        _Field(
            group="headings",
            description="A custom string to override the autogenerated toc label of the root object.",
        ),
    ] = "",
)
```

Accepted input options.

Methods:

- **`coerce`** – Coerce data.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`extra`** (`Annotated[dict[str, Any], _Field(group='general', description='Extra options.')]`) – Extra options.
- **`heading`** (`Annotated[str, _Field(group='headings', description='A custom string to override the autogenerated heading of the root object.')]`) – A custom string to override the autogenerated heading of the root object.
- **`heading_level`** (`Annotated[int, _Field(group='headings', description='The initial heading level to use.')]`) – The initial heading level to use.
- **`show_symbol_type_heading`** (`Annotated[bool, _Field(group='headings', description='Show the symbol type in headings (e.g. mod, class, meth, func and attr).')]`) – Show the symbol type in headings (e.g. mod, class, meth, func and attr).
- **`show_symbol_type_toc`** (`Annotated[bool, _Field(group='headings', description='Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).')]`) – Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).
- **`toc_label`** (`Annotated[str, _Field(group='headings', description='A custom string to override the autogenerated toc label of the root object.')]`) – A custom string to override the autogenerated toc label of the root object.

### extra

```
extra: Annotated[
    dict[str, Any],
    _Field(group="general", description="Extra options."),
] = field(default_factory=dict)
```

Extra options.

### heading

```
heading: Annotated[
    str,
    _Field(
        group="headings",
        description="A custom string to override the autogenerated heading of the root object.",
    ),
] = ""
```

A custom string to override the autogenerated heading of the root object.

### heading_level

```
heading_level: Annotated[
    int,
    _Field(
        group="headings",
        description="The initial heading level to use.",
    ),
] = 2
```

The initial heading level to use.

### show_symbol_type_heading

```
show_symbol_type_heading: Annotated[
    bool,
    _Field(
        group="headings",
        description="Show the symbol type in headings (e.g. mod, class, meth, func and attr).",
    ),
] = False
```

Show the symbol type in headings (e.g. mod, class, meth, func and attr).

### show_symbol_type_toc

```
show_symbol_type_toc: Annotated[
    bool,
    _Field(
        group="headings",
        description="Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).",
    ),
] = False
```

Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).

### toc_label

```
toc_label: Annotated[
    str,
    _Field(
        group="headings",
        description="A custom string to override the autogenerated toc label of the root object.",
    ),
] = ""
```

A custom string to override the autogenerated toc label of the root object.

### coerce

```
coerce(**data: Any) -> MutableMapping[str, Any]
```

Coerce data.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def coerce(cls, **data: Any) -> MutableMapping[str, Any]:
    """Coerce data."""
    return data
```

### from_data

```
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def from_data(cls, **data: Any) -> Self:
    """Create an instance from a dictionary."""
    return cls(**cls.coerce(**data))
```

## ShellOptions

```
ShellOptions(
    *,
    extra: Annotated[
        dict[str, Any],
        _Field(
            group="general", description="Extra options."
        ),
    ] = dict(),
    heading: Annotated[
        str,
        _Field(
            group="headings",
            description="A custom string to override the autogenerated heading of the root object.",
        ),
    ] = "",
    heading_level: Annotated[
        int,
        _Field(
            group="headings",
            description="The initial heading level to use.",
        ),
    ] = 2,
    show_symbol_type_heading: Annotated[
        bool,
        _Field(
            group="headings",
            description="Show the symbol type in headings (e.g. mod, class, meth, func and attr).",
        ),
    ] = False,
    show_symbol_type_toc: Annotated[
        bool,
        _Field(
            group="headings",
            description="Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).",
        ),
    ] = False,
    toc_label: Annotated[
        str,
        _Field(
            group="headings",
            description="A custom string to override the autogenerated toc label of the root object.",
        ),
    ] = "",
)
```

Bases: `ShellInputOptions`

Final options passed as template context.

Methods:

- **`coerce`** – Create an instance from a dictionary.
- **`from_data`** – Create an instance from a dictionary.

Attributes:

- **`extra`** (`Annotated[dict[str, Any], _Field(group='general', description='Extra options.')]`) – Extra options.
- **`heading`** (`Annotated[str, _Field(group='headings', description='A custom string to override the autogenerated heading of the root object.')]`) – A custom string to override the autogenerated heading of the root object.
- **`heading_level`** (`Annotated[int, _Field(group='headings', description='The initial heading level to use.')]`) – The initial heading level to use.
- **`show_symbol_type_heading`** (`Annotated[bool, _Field(group='headings', description='Show the symbol type in headings (e.g. mod, class, meth, func and attr).')]`) – Show the symbol type in headings (e.g. mod, class, meth, func and attr).
- **`show_symbol_type_toc`** (`Annotated[bool, _Field(group='headings', description='Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).')]`) – Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).
- **`toc_label`** (`Annotated[str, _Field(group='headings', description='A custom string to override the autogenerated toc label of the root object.')]`) – A custom string to override the autogenerated toc label of the root object.

### extra

```
extra: Annotated[
    dict[str, Any],
    _Field(group="general", description="Extra options."),
] = field(default_factory=dict)
```

Extra options.

### heading

```
heading: Annotated[
    str,
    _Field(
        group="headings",
        description="A custom string to override the autogenerated heading of the root object.",
    ),
] = ""
```

A custom string to override the autogenerated heading of the root object.

### heading_level

```
heading_level: Annotated[
    int,
    _Field(
        group="headings",
        description="The initial heading level to use.",
    ),
] = 2
```

The initial heading level to use.

### show_symbol_type_heading

```
show_symbol_type_heading: Annotated[
    bool,
    _Field(
        group="headings",
        description="Show the symbol type in headings (e.g. mod, class, meth, func and attr).",
    ),
] = False
```

Show the symbol type in headings (e.g. mod, class, meth, func and attr).

### show_symbol_type_toc

```
show_symbol_type_toc: Annotated[
    bool,
    _Field(
        group="headings",
        description="Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).",
    ),
] = False
```

Show the symbol type in the Table of Contents (e.g. mod, class, methd, func and attr).

### toc_label

```
toc_label: Annotated[
    str,
    _Field(
        group="headings",
        description="A custom string to override the autogenerated toc label of the root object.",
    ),
] = ""
```

A custom string to override the autogenerated toc label of the root object.

### coerce

```
coerce(**data: Any) -> MutableMapping[str, Any]
```

Create an instance from a dictionary.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def coerce(cls, **data: Any) -> MutableMapping[str, Any]:
    """Create an instance from a dictionary."""
    # Coerce any field into its final form.
    return super().coerce(**data)
```

### from_data

```
from_data(**data: Any) -> Self
```

Create an instance from a dictionary.

Source code in `src/mkdocstrings_handlers/shell/_internal/config.py`

```
@classmethod
def from_data(cls, **data: Any) -> Self:
    """Create an instance from a dictionary."""
    return cls(**cls.coerce(**data))
```

## get_handler

```
get_handler(
    *,
    handler_config: MutableMapping[str, Any],
    tool_config: MkDocsConfig,
    **kwargs: Any,
) -> ShellHandler
```

Simply return an instance of `ShellHandler`.

Parameters:

- **`handler_config`** (`MutableMapping[str, Any]`) – The handler configuration.
- **`tool_config`** (`MkDocsConfig`) – The tool (SSG) configuration.
- **`**kwargs`** (`Any`, default: `{}` ) – Keyword arguments for the base handler constructor.

Returns:

- `ShellHandler` – An instance of the handler.

Source code in `src/mkdocstrings_handlers/shell/_internal/handler.py`

```
def get_handler(
    *,
    handler_config: MutableMapping[str, Any],
    tool_config: MkDocsConfig,
    **kwargs: Any,
) -> ShellHandler:
    """Simply return an instance of `ShellHandler`.

    Parameters:
        handler_config: The handler configuration.
        tool_config: The tool (SSG) configuration.
        **kwargs: Keyword arguments for the base handler constructor.

    Returns:
        An instance of the handler.
    """
    base_dir = Path(tool_config.config_file_path or "./mkdocs.yml").parent
    return ShellHandler(config=ShellConfig(**handler_config), base_dir=base_dir, **kwargs)
```
