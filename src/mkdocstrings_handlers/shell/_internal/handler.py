# This module implements a handler for shell scripts and shell libraries.

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar

from mkdocs.exceptions import PluginError
from mkdocstrings import BaseHandler, CollectionError, CollectorItem, get_logger
from shellman import FILTERS, DocFile

from mkdocstrings_handlers.shell._internal.config import ShellConfig, ShellOptions

if TYPE_CHECKING:
    from collections.abc import Mapping, MutableMapping

    from mkdocs.config.defaults import MkDocsConfig
    from mkdocstrings import HandlerOptions


_logger = get_logger(__name__)


class ShellHandler(BaseHandler):
    """The Shell handler class."""

    name: ClassVar[str] = "shell"
    """The handler's name."""

    domain: ClassVar[str] = "shell"
    """The cross-documentation domain/language for this handler."""

    enable_inventory: ClassVar[bool] = False
    """Whether this handler is interested in enabling the creation of the `objects.inv` Sphinx inventory file."""

    fallback_theme: ClassVar[str] = "material"
    """The theme to fallback to."""

    def __init__(self, config: ShellConfig, base_dir: Path, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.config = config
        """The handler configuration."""
        self.base_dir = base_dir
        """The base directory for the handler."""
        self.global_options = config.options
        """The global options for the handler."""

    def get_options(self, local_options: Mapping[str, Any]) -> HandlerOptions:
        """Get the combined (global and local) options."""
        extra = {**self.global_options.get("extra", {}), **local_options.get("extra", {})}
        options = {**self.global_options, **local_options, "extra": extra}
        try:
            return ShellOptions.from_data(**options)
        except Exception as error:
            raise PluginError(f"Invalid options: {error}") from error

    def collect(self, identifier: str, options: ShellOptions) -> CollectorItem:  # noqa: ARG002
        """Collect data from a shell script/library."""
        script_path = self.base_dir / identifier
        try:
            return DocFile(str(script_path))
        except FileNotFoundError as error:
            raise CollectionError(f"Could not find script '{script_path}'") from error

    def render(self, data: CollectorItem, options: ShellOptions) -> str:
        """Render the collected data."""
        heading_level = options.heading_level
        template = self.env.get_template("script.html.jinja")
        return template.render(
            config=options,
            filename=data.filename,
            script=data.sections,
            heading_level=heading_level,
        )

    def update_env(self, config: MkDocsConfig) -> None:  # noqa: ARG002
        """Update the Jinja environment."""
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.keep_trailing_newline = False
        self.env.filters.update(FILTERS)


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
