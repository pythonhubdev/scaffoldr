"""Scaffoldr CLI application."""

import typer
from typing_extensions import Annotated

from scaffoldr.banner import show_animated_banner

typer_app = typer.Typer(
    name="scaffoldr",
    help="Flask/FastAPI Architecture Application Generator",
    add_completion=False,
)


@typer_app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[
        bool, typer.Option("--version", "-v", help="Show version and exit")
    ] = False,
    no_banner: Annotated[
        bool, typer.Option("--no-banner", help="Disable animated banner")
    ] = False,
) -> None:
    """Scaffoldr - Building better Python projects, faster."""
    if version:
        typer.echo("scaffoldr 0.2.1")
        raise typer.Exit()

    # Show animated banner unless disabled
    if not no_banner:
        show_animated_banner()

    # If no subcommand was called, show help
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())


@typer_app.command()
def generate(
    project_name: Annotated[
        str, typer.Argument(help="Name of the project to generate")
    ],
    framework: Annotated[
        str, typer.Option("--framework", "-f", help="Framework to use")
    ] = "fastapi",
) -> None:
    """Generate a new project with the specified framework."""
    typer.echo(f"Generating {project_name} with {framework} framework...")
    typer.echo("🚧 Coming soon! This feature is under development.")


if __name__ == "__main__":
    typer_app()
