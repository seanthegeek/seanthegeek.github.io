#!/usr/bin/env python3
"""Pad and resize an image to Chirpy's lead/preview image ratio (1.91:1, default 1200x630).

Chirpy auto-crops any lead image that isn't 1200x630 / 1.91:1. This script letterboxes
the source image (adds solid-color bars on the shorter axis) instead of letting Chirpy
crop it, then resizes the padded canvas to the target dimensions.

Usage:
    python3 chirpy_lead_image.py INPUT [-o OUTPUT] [--width 1200] [--height 630]
                                  [--color black|white|#RRGGBB]

Examples:
    python3 chirpy_lead_image.py stokes-doj.webp
    python3 chirpy_lead_image.py photo.png -o photo-lead.webp --color "#1a1a1a"
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

ColorType = tuple[int, int, int]

NAMED_COLORS: dict[str, ColorType] = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}


def parse_color(value: str) -> ColorType:
    """Parse a named color ('black', 'white') or hex string ('#rrggbb') into an RGB tuple."""
    lowered = value.strip().lower()
    if lowered in NAMED_COLORS:
        return NAMED_COLORS[lowered]

    hex_value = lowered.lstrip("#")
    if len(hex_value) != 6:
        raise argparse.ArgumentTypeError(
            f"Invalid color '{value}'. Use 'black', 'white', or a hex code like '#1a1a1a'."
        )
    try:
        r, g, b = (int(hex_value[i : i + 2], 16) for i in (0, 2, 4))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid hex color '{value}'.") from exc
    return (r, g, b)


def make_lead_image(
    input_path: Path,
    output_path: Path,
    target_width: int = 1200,
    target_height: int = 630,
    bg_color: ColorType = (0, 0, 0),
) -> None:
    """Letterbox `input_path` to the target aspect ratio, resize, and save to `output_path`."""
    image = Image.open(input_path).convert("RGB")
    width, height = image.size
    target_ratio = target_width / target_height
    current_ratio = width / height

    if current_ratio < target_ratio:
        # Source is too narrow/tall relative to target -> pad width (left/right bars).
        new_width = round(height * target_ratio)
        canvas = Image.new("RGB", (new_width, height), bg_color)
        offset = (new_width - width) // 2
        canvas.paste(image, (offset, 0))
    elif current_ratio > target_ratio:
        # Source is too wide/short relative to target -> pad height (top/bottom bars).
        new_height = round(width / target_ratio)
        canvas = Image.new("RGB", (width, new_height), bg_color)
        offset = (new_height - height) // 2
        canvas.paste(image, (0, offset))
    else:
        canvas = image

    canvas = canvas.resize((target_width, target_height), Image.LANCZOS)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, quality=90)


def build_arg_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", type=Path, help="Path to the source image.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output path. Defaults to '<input-stem>-lead<input-suffix>' next to the input.",
    )
    parser.add_argument("--width", type=int, default=1200, help="Target width (default: 1200).")
    parser.add_argument("--height", type=int, default=630, help="Target height (default: 630).")
    parser.add_argument(
        "--color",
        type=parse_color,
        default=(0, 0, 0),
        help="Letterbox color: 'black', 'white', or a hex code like '#1a1a1a' (default: black).",
    )
    return parser


def main() -> None:
    """Entry point for CLI usage."""
    parser = build_arg_parser()
    args = parser.parse_args()

    output_path: Path = args.output or args.input.with_name(f"{args.input.stem}-lead{args.input.suffix}")

    make_lead_image(
        input_path=args.input,
        output_path=output_path,
        target_width=args.width,
        target_height=args.height,
        bg_color=args.color,
    )
    print(f"Saved {output_path} ({args.width}x{args.height})")


if __name__ == "__main__":
    main()
