"""Tests for main app functionality."""

import re
from typer.testing import CliRunner
from unittest.mock import patch

from scaffoldr.app import typer_app


runner = CliRunner()


def strip_ansi(text: str) -> str:
    """Strip ANSI color codes from text."""
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", text)


def test_version_option():
    """Test --version option."""
    result = runner.invoke(typer_app, ["--version"])
    assert result.exit_code == 0
    assert "scaffoldr 0.2.1" in result.stdout


def test_help_option():
    """Test --help option."""
    result = runner.invoke(typer_app, ["--help"])
    assert result.exit_code == 0
    clean_output = strip_ansi(result.stdout)
    assert "Flask/FastAPI Architecture Application Generator" in clean_output
    assert "--no-banner" in clean_output


@patch("scaffoldr.app.show_animated_banner")
def test_no_banner_option(mock_banner):
    """Test --no-banner option disables banner."""
    result = runner.invoke(typer_app, ["--no-banner"])
    assert result.exit_code == 0
    mock_banner.assert_not_called()


@patch("scaffoldr.app.show_animated_banner")
def test_banner_enabled_by_default(mock_banner):
    """Test banner is shown by default when no command given."""
    result = runner.invoke(typer_app, [])
    assert result.exit_code == 0
    mock_banner.assert_called_once()


def test_generate_command():
    """Test generate command."""
    result = runner.invoke(typer_app, ["--no-banner", "generate", "test-project"])
    assert result.exit_code == 0
    assert "Generating test-project with fastapi framework" in result.stdout
    assert "Coming soon" in result.stdout


def test_generate_command_with_framework():
    """Test generate command with framework option."""
    result = runner.invoke(
        typer_app, ["--no-banner", "generate", "test-project", "--framework", "flask"]
    )
    assert result.exit_code == 0
    assert "Generating test-project with flask framework" in result.stdout
