from pathlib import Path
from typing import Annotated

import copier
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

from scaffoldr.core.constants import Frameworks, console
from scaffoldr.core.utils.helper import Helper


class GenerateCommand:
	"""Handles project generation commands."""

	@staticmethod
	def generate(
		project_name: str,
		framework: str,
		destination: str,
		python_version: str,
		email: str,
		name: str,
		description: str,
		docker: bool,
		use_cloud: bool,
		use_database: bool,
	) -> None:
		"""Generate a new project with the specified framework."""
		# Validate framework
		if framework not in list(Frameworks):
			console.print(
				f"[red]Error:[/red] Framework '{framework}' "
				f"is not supported. Supported frameworks: {', '.join(list(Frameworks))}",
			)
			raise typer.Exit(1)

		cloud_type = "none"
		if use_cloud:
			cloud_type = Helper.cloud_type()

		database_type = None
		if use_database:
			database_type = Helper.database_type()

		project_name = project_name.replace(" ", "-").lower()
		# Check if directory already exists
		if destination == ".":
			project_dir = Path.cwd() / project_name
		else:
			project_dir = Path(destination) / project_name

		if project_dir.exists():
			console.print(f"[red]Error:[/red] Directory '{project_name}' already exists.")
			raise typer.Exit(1)

		# Get template path
		template_path = (
			Path(__file__).parent.parent.parent.parent / "templates" / f"{framework}_template"
		)

		if not template_path.exists():
			console.print(
				f"[red]Error:[/red] Template for framework '{framework}' not found.",
			)
			raise typer.Exit(1)

		# Prepare copier data
		data = {
			"project_name": project_name,
			"project_slug": project_name.replace("-", "_"),
			"author_name": name,
			"author_email": email,
			"description": description,
			"python_version": python_version,
			"use_docker": docker,
			"cloud_type": cloud_type,
			"database": use_database,
			"database_type": database_type,
			"framework": framework,
		}

		try:
			with Progress(
				SpinnerColumn(),
				TextColumn("[progress.description]{task.description}"),
				console=console,
			) as progress:
				task = progress.add_task("Copying template files...", total=None)

				# Run copier
				copier.run_copy(
					src_path=str(template_path),
					dst_path=destination,
					data=data,
					quiet=True,  # Suppress copier output
				)

				progress.update(
					task,
					completed=True,
					description=f"Generating project {project_name} with {framework} framework...",
				)

			Helper.post_hook(str(project_dir))

			console.print(
				f"[green]✅ Project '{project_name}' generated successfully![/green]",
			)
			console.print(
				f"[blue]📁 Change to the project directory:[/blue] cd {project_name}",
			)
			console.print(
				f"[blue]🚀 Run the application:[/blue] uv run {data['project_slug']}",
			)

		except Exception as exception:
			console.print(f"[red]Error:[/red] Failed to generate project: {exception!s}")
			raise typer.Exit(1) from exception


gen = typer.Typer(help="Generate a new project with the specified framework.")


@gen.command()
def generate(
	project_name: Annotated[
		str,
		typer.Option(help="Name of the project to generate", prompt=True),
	],
	framework: Annotated[
		str,
		typer.Option("--framework", "-f", help="Framework to use", prompt=True),
	] = "fastapi",
	destination: Annotated[
		str,
		typer.Option(
			"--destination",
			"-dest",
			help="Destination directory for the new project don't include project name. Please provide full path or '.' for current directory",
			prompt=True,
		),
	] = ".",
	python_version: Annotated[
		str,
		typer.Option(
			"--python-version",
			"-pv",
			help="Python version to use",
			prompt=True,
		),
	] = "3.13",
	email: Annotated[
		str,
		typer.Option(
			"--email",
			"-e",
			help="Author email address",
			prompt=True,
		),
	] = "example@example.com",
	name: Annotated[
		str,
		typer.Option(
			"--name",
			"-n",
			help="Author name",
			prompt=True,
		),
	] = "John Doe",
	description: Annotated[
		str,
		typer.Option(
			"--description",
			"-d",
			help="Project description",
			prompt=True,
		),
	] = "A FastAPI application",
	docker: Annotated[
		bool,
		typer.Option(
			"--docker/--no-docker",
			help="Include Docker support",
			prompt=True,
		),
	] = True,
	use_cloud: Annotated[
		bool,
		typer.Option(
			"--use-cloud/--no-cloud",
			help="Include cloud support (e.g., AWS S3)",
			prompt=True,
		),
	] = True,
	use_database: Annotated[
		bool,
		typer.Option(
			"--use-database/--no-database",
			help="Include database support (e.g., PostgreSQL)",
			prompt=True,
		),
	] = True,
) -> None:
	"""Generate a new project with the specified framework."""
	# Validate framework
	GenerateCommand.generate(
		project_name,
		framework,
		destination,
		python_version,
		email,
		name,
		description,
		docker,
		use_cloud,
		use_database,
	)
