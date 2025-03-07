"""This module implements a handler for the Shell language."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar

from mkdocstrings.handlers.base import BaseHandler, CollectionError, CollectorItem
from mkdocstrings.loggers import get_logger
from shellman import DocFile
from shellman.templates.filters import FILTERS

if TYPE_CHECKING:
    from collections.abc import Mapping, MutableMapping

    from markdown import Markdown


logger = get_logger(__name__)


class ShellHandler(BaseHandler):
    """The Shell handler class."""

    name: str = "shell"
    """The handler's name."""

    domain: str = "shell"
    """The cross-documentation domain/language for this handler."""

    enable_inventory: bool = False
    """Whether this handler is interested in enabling the creation of the `objects.inv` Sphinx inventory file."""

    fallback_theme = "material"
    """The theme to fallback to."""

    fallback_config: ClassVar[dict] = {"fallback": True}
    """The configuration used to collect item during autorefs fallback."""

    default_config: ClassVar[dict] = {
        "show_root_heading": False,
        "show_root_toc_entry": True,
        "heading_level": 2,
    }
    """The default configuration options.

    Option | Type | Description | Default
    ------ | ---- | ----------- | -------
    **`show_root_heading`** | `bool` | Show the heading of the object at the root of the documentation tree. | `False`
    **`show_root_toc_entry`** | `bool` | If the root heading is not shown, at least add a ToC entry for it. | `True`
    **`heading_level`** | `int` | The initial heading level to use. | `2`
    """

    def __init__(  # noqa: D107
        self,
        handler: str,
        theme: str,
        custom_templates: str | None = None,
        config_file_path: str | None = None,
    ) -> None:
        super().__init__(handler, theme, custom_templates)
        if config_file_path:
            self.base_dir = Path(config_file_path).parent
        else:
            self.base_dir = Path(".")

    def collect(self, identifier: str, config: MutableMapping[str, Any]) -> CollectorItem:  # noqa: ARG002
        """Collect data given an identifier and selection configuration.

        In the implementation, you typically call a subprocess that returns JSON, and load that JSON again into
        a Python dictionary for example, though the implementation is completely free.

        Parameters:
            identifier: An identifier that was found in a markdown document for which to collect data. For example,
                in Python, it would be 'mkdocstrings.handlers' to collect documentation about the handlers module.
                It can be anything that you can feed to the tool of your choice.
            config: All configuration options for this handler either defined globally in `mkdocs.yml` or
                locally overridden in an identifier block by the user.

        Returns:
            Anything you want, as long as you can feed it to the `render` method.
        """
        script_path = self.base_dir / identifier
        try:
            return DocFile(str(script_path))
        except FileNotFoundError as error:
            raise CollectionError(f"Could not find script '{script_path}'") from error

    def render(self, data: CollectorItem, config: Mapping[str, Any]) -> str:
        """Render a template using provided data and configuration options.

        Parameters:
            data: The data to render that was collected above in `collect()`.
            config: All configuration options for this handler either defined globally in `mkdocs.yml` or
                locally overridden in an identifier block by the user.

        Returns:
            The rendered template as HTML.
        """
        final_config = {**self.default_config, **config}
        heading_level = final_config["heading_level"]
        template = self.env.get_template("script.html.jinja")
        return template.render(
            config=final_config,
            filename=data.filename,
            script=data.sections,
            heading_level=heading_level,
        )

    def update_env(self, md: Markdown, config: dict) -> None:
        """Update the Jinja environment with any custom settings/filters/options for this handler.

        Parameters:
            md: The Markdown instance. Useful to add functions able to convert Markdown into the environment filters.
            config: Configuration options for `mkdocs` and `mkdocstrings`, read from `mkdocs.yml`. See the source code
                of [mkdocstrings.plugin.MkdocstringsPlugin.on_config][] to see what's in this dictionary.
        """
        super().update_env(md, config)  # Add some mkdocstrings default filters such as highlight and convert_markdown
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False
        self.env.filters.update(FILTERS)


def get_handler(
    theme: str,
    custom_templates: str | None = None,
    config_file_path: str | None = None,
    **config: Any,  # noqa: ARG001
) -> ShellHandler:
    """Simply return an instance of `ShellHandler`.

    Parameters:
        theme: The theme to use when rendering contents.
        custom_templates: Directory containing custom templates.
        config_file_path: The MkDocs configuration file path.
        **config: Configuration passed to the handler.

    Returns:
        An instance of the handler.
    """
    return ShellHandler(
        handler="shell",
        theme=theme,
        custom_templates=custom_templates,
        config_file_path=config_file_path,
    )
