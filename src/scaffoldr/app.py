from scaffoldr.animation.banner import BannerAnimation
import typer
from typing import Annotated
from scaffoldr import __version__
from scaffoldr.core.constants import console

app = typer.Typer(
    name="scaffoldr",
    help="",
    add_completion=False,
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    no_banner: Annotated[
        bool,
        typer.Option("--no-banner", help="Disable animated banner"),
    ] = False,
) -> None:
    """Scaffoldr - Building better Python projects, faster."""
    # Show animated banner unless disabled
    if not no_banner:
        BannerAnimation().run()

    # If no subcommand was called, show help
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())


@app.command(
    name="version",
    help="Get the current version of Scaffoldr CLI",
)
def version() -> None:
    """Display the current version of Scaffoldr CLI."""
    console.print(f"[bold green]Scaffoldr CLI version: {__version__}[/bold green]")


@app.command()
def generate(
    project_name: Annotated[
        str,
        typer.Argument(help="Name of the project to generate"),
    ],
    framework: Annotated[
        str,
        typer.Option("--framework", "-f", help="Framework to use"),
    ] = "fastapi",
) -> None:
    """Generate a new project with the specified framework."""
    typer.echo(f"Generating {project_name} with {framework} framework...")
    typer.echo("🚧 Coming soon! This feature is under development.")


if __name__ == "__main__":
    app()
