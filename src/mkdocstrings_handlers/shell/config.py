"""Configuration and options dataclasses."""

from __future__ import annotations

import sys
from dataclasses import field
from typing import TYPE_CHECKING, Annotated, Any

# YORE: EOL 3.10: Replace block with line 2.
if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

try:
    # When Pydantic is available, use it to validate options (done automatically).
    # Users can therefore opt into validation by installing Pydantic in development/CI.
    # When building the docs to deploy them, Pydantic is not required anymore.

    # When building our own docs, Pydantic is always installed (see `docs` group in `pyproject.toml`)
    # to allow automatic generation of a JSON Schema. The JSON Schema is then referenced by mkdocstrings,
    # which is itself referenced by mkdocs-material's schema system. For example in VSCode:
    #
    # "yaml.schemas": {
    #     "https://squidfunk.github.io/mkdocs-material/schema.json": "mkdocs.yml"
    # }
    from inspect import cleandoc

    from pydantic import Field as BaseField
    from pydantic.dataclasses import dataclass

    _base_url = "https://mkdocstrings.github.io/shell/configuration"

    def Field(  # noqa: N802, D103
        *args: Any,
        description: str,
        parent: str | None = None,
        **kwargs: Any,
    ) -> None:
        def _add_markdown_description(schema: dict[str, Any]) -> None:
            url = f"{_base_url}/#{parent or schema['title']}"
            schema["markdownDescription"] = f"[DOCUMENTATION]({url})\n\n{schema['description']}"

        return BaseField(
            *args,
            description=cleandoc(description),
            field_title_generator=lambda name, _: name,
            json_schema_extra=_add_markdown_description,
            **kwargs,
        )
except ImportError:
    from dataclasses import dataclass  # type: ignore[no-redef]

    def Field(*args: Any, **kwargs: Any) -> None:  # type: ignore[misc]  # noqa: D103, N802
        pass


if TYPE_CHECKING:
    from collections.abc import MutableMapping


# YORE: EOL 3.9: Remove block.
_dataclass_options = {"frozen": True}
if sys.version_info >= (3, 10):
    _dataclass_options["kw_only"] = True


# YORE: EOL 3.9: Replace `**_dataclass_options` with `frozen=True, kw_only=True` within line.
@dataclass(**_dataclass_options)  # type: ignore[call-overload]
class ShellInputOptions:
    """Accepted input options."""

    extra: Annotated[
        dict[str, Any],
        Field(description="Extra options."),
    ] = field(default_factory=dict)

    heading_level: Annotated[
        int,
        Field(description="The initial heading level to use."),
    ] = 2

    show_root_heading: Annotated[
        bool,
        Field(
            description="""Show the heading of the object at the root of the documentation tree.

            The root object is the object referenced by the identifier after `:::`.
            """,
        ),
    ] = False

    show_root_toc_entry: Annotated[
        bool,
        Field(
            description="If the root heading is not shown, at least add a ToC entry for it.",
        ),
    ] = True

    @classmethod
    def coerce(cls, **data: Any) -> MutableMapping[str, Any]:
        """Coerce data."""
        return data

    @classmethod
    def from_data(cls, **data: Any) -> Self:
        """Create an instance from a dictionary."""
        return cls(**cls.coerce(**data))


# YORE: EOL 3.9: Replace `**_dataclass_options` with `frozen=True, kw_only=True` within line.
@dataclass(**_dataclass_options)  # type: ignore[call-overload]
class ShellOptions(ShellInputOptions):  # type: ignore[override,unused-ignore]
    """Final options passed as template context."""


# YORE: EOL 3.9: Replace `**_dataclass_options` with `frozen=True, kw_only=True` within line.
@dataclass(**_dataclass_options)  # type: ignore[call-overload]
class ShellInputConfig:
    """Python handler configuration."""

    options: Annotated[
        ShellInputOptions,
        Field(description="Configuration options for collecting and rendering objects."),
    ] = field(default_factory=ShellInputOptions)


# YORE: EOL 3.9: Replace `**_dataclass_options` with `frozen=True, kw_only=True` within line.
@dataclass(**_dataclass_options)  # type: ignore[call-overload]
class ShellConfig(ShellInputConfig):  # type: ignore[override,unused-ignore]
    """Shell handler configuration."""

    options: dict[str, Any] = field(default_factory=dict)  # type: ignore[assignment]
