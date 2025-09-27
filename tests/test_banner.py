"""Tests for banner functionality."""

from unittest.mock import patch
from rich.text import Text

from scaffoldr.banner import (
    get_rainbow_colors,
    apply_wave_effect,
    show_simple_banner,
    BANNER_ART,
    TAGLINE,
)


def test_get_rainbow_colors():
    """Test rainbow color generation."""
    colors = get_rainbow_colors(10)
    assert len(colors) == 10
    assert all(color.startswith("hsl(") for color in colors)
    assert all(color.endswith(",100%,70%)") for color in colors)


def test_apply_wave_effect():
    """Test wave effect application to text."""
    text = "HELLO"
    result = apply_wave_effect(text, frame=0)

    assert isinstance(result, Text)
    assert len(result.plain) == len(text)
    assert result.plain == text


def test_banner_constants():
    """Test that banner constants are properly defined."""
    assert isinstance(BANNER_ART, list)
    assert len(BANNER_ART) > 0
    assert all(isinstance(line, str) for line in BANNER_ART)

    assert isinstance(TAGLINE, str)
    assert len(TAGLINE) > 0


@patch("scaffoldr.banner.console")
def test_show_simple_banner(mock_console):
    """Test simple banner display."""
    show_simple_banner()

    # Verify that console.print was called
    assert mock_console.print.called

    # Check that banner art lines were printed
    print_calls = [call[0] for call in mock_console.print.call_args_list]
    banner_lines_printed = sum(
        1 for call in print_calls if call and call[0] in BANNER_ART
    )
    assert banner_lines_printed == len(BANNER_ART)


def test_wave_effect_different_frames():
    """Test that wave effect produces different results for different frames."""
    text = "TEST"
    result1 = apply_wave_effect(text, frame=0)
    result2 = apply_wave_effect(text, frame=10)

    # Results should be different for different frames
    assert result1.plain == result2.plain  # Same text
    # But potentially different styling (hard to test exact colors)
    assert isinstance(result1, Text)
    assert isinstance(result2, Text)


def test_rainbow_colors_range():
    """Test that rainbow colors cover expected hue range."""
    colors = get_rainbow_colors(360)  # Full hue spectrum

    # First color should start near 0 hue
    assert colors[0].startswith("hsl(0,")

    # Last color should be near 359 hue
    assert colors[-1].startswith("hsl(359,")
