"""Animated ASCII banner for Scaffoldr CLI."""

import time
import math
from typing import List, Tuple

from rich.console import Console
from rich.text import Text
from rich.color import Color

console = Console()

# ASCII art for "SCAFFOLDR"
BANNER_ART = [
    "   _____ _____          ______ ______ ____  _      _____  _____  ",
    "  / ____/ ____|   /\\   |  ____|  ____/ __ \\| |    |  __ \\|  __ \\ ",
    " | (___| |       /  \\  | |__  | |__ | |  | | |    | |  | | |__) |",
    "  \\___ \\ |      / /\\ \\ |  __| |  __|| |  | | |    | |  | |  _  / ",
    "  ____) | |____ / ____ \\| |    | |   | |__| | |____| |__| | | \\ \\ ",
    " |_____/ \\_____/_/    \\_\\_|    |_|    \\____/|______|_____/|_|  \\_\\",
]

# Tagline
TAGLINE = "Building better Python projects, faster."

def get_rainbow_colors(steps: int) -> List[str]:
    """Generate a list of rainbow colors."""
    colors = []
    for i in range(steps):
        # Create rainbow effect using HSV color space
        hue = (i / steps) * 360
        colors.append(f"hsl({int(hue)},100%,70%)")
    return colors

def apply_wave_effect(text: str, frame: int, wave_speed: float = 0.3, wave_amplitude: float = 0.5) -> Text:
    """Apply a wave effect to text with rainbow colors."""
    result = Text()
    rainbow_colors = get_rainbow_colors(len(text))
    
    for i, char in enumerate(text):
        # Calculate wave offset
        wave_offset = math.sin((frame * wave_speed) + (i * 0.5)) * wave_amplitude
        
        # Get color index with wave effect
        color_index = int((i + frame * 2 + wave_offset * 10) % len(rainbow_colors))
        color = rainbow_colors[color_index]
        
        # Add slight brightness variation for wave effect
        brightness = 70 + int(wave_offset * 20)
        brightness = max(50, min(90, brightness))  # Clamp between 50-90%
        
        # Override color with wave-modified brightness
        hue = (color_index / len(rainbow_colors)) * 360
        wave_color = f"hsl({int(hue)},100%,{brightness}%)"
        
        result.append(char, style=wave_color)
    
    return result

def show_animated_banner(duration: float = 3.0, frame_rate: int = 15) -> None:
    """Display an animated rainbow banner."""
    try:
        # Clear screen and hide cursor
        console.clear()
        console.show_cursor(False)
        
        frames = int(duration * frame_rate)
        
        for frame in range(frames):
            # Clear current display
            console.clear()
            
            # Create animated banner
            console.print()  # Empty line at top
            
            for line in BANNER_ART:
                animated_line = apply_wave_effect(line, frame, wave_speed=0.4, wave_amplitude=0.8)
                console.print(animated_line, justify="center")
            
            # Add some spacing
            console.print()
            
            # Animated tagline with different wave parameters
            animated_tagline = apply_wave_effect(TAGLINE, frame + 10, wave_speed=0.2, wave_amplitude=0.3)
            console.print(animated_tagline, justify="center", style="italic")
            
            console.print()  # Empty line at bottom
            
            # Small delay between frames
            time.sleep(1.0 / frame_rate)
        
        # Final static display with subtle colors
        console.clear()
        console.print()
        
        # Show final static banner with gradient
        for i, line in enumerate(BANNER_ART):
            # Create a subtle gradient from blue to purple
            gradient_text = Text()
            for j, char in enumerate(line):
                progress = j / len(line)
                hue = 240 + (progress * 60)  # Blue (240°) to purple (300°)
                color = f"hsl({int(hue)},80%,75%)"
                gradient_text.append(char, style=color)
            console.print(gradient_text, justify="center")
        
        console.print()
        
        # Static tagline in cyan
        console.print(TAGLINE, justify="center", style="italic cyan")
        console.print()
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        console.clear()
        console.print()
        console.print("🚀 Welcome to Scaffoldr!", justify="center", style="bold cyan")
        console.print(TAGLINE, justify="center", style="italic")
        console.print()
    finally:
        # Always restore cursor
        console.show_cursor(True)

def show_simple_banner() -> None:
    """Show a simple non-animated banner for environments that don't support animations."""
    console.print()
    for line in BANNER_ART:
        console.print(line, justify="center", style="bold blue")
    console.print()
    console.print(TAGLINE, justify="center", style="italic cyan")
    console.print()