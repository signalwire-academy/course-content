#!/usr/bin/env python3
"""
Extract Unicode box-drawing diagrams from markdown files.
Generates .txt, .svg, and .png files, then updates markdown to reference PNGs.

Usage:
    python scripts/extract_diagrams.py [options]

Options:
    --extract-only     Only extract .txt files, no SVG/PNG conversion
    --svg-only         Create SVG files but skip PNG conversion
    --no-update-md     Don't modify markdown files
    --dry-run          Show what would be done without making changes
    --dpi N            PNG DPI (default: 72)
    --scale N          PNG scale factor (default: 0.70)
    --color COLOR      SVG line color (default: #333333)
"""

import os
import re
import subprocess
import sys
import shutil
from pathlib import Path
import argparse

# Directories to process
CONTENT_DIRS = [
    "level-1",
    "level-2",
    "level-3",
]

# Unicode box-drawing characters that indicate a diagram
BOX_CHARS = set('┌┐└┘├┤┬┴┼─│╔╗╚╝╠╣╦╩╬═║')


def has_box_drawing(content):
    """Check if content contains Unicode box-drawing characters."""
    return any(char in content for char in BOX_CHARS)


def extract_diagrams_from_file(filepath):
    """Extract all code blocks containing box-drawing characters."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all code blocks (``` ... ```)
    # Match code blocks with optional language specifier
    pattern = r'```(\w*)\n(.*?)```'

    diagrams = []
    for match in re.finditer(pattern, content, re.DOTALL):
        lang = match.group(1)
        block_content = match.group(2)

        # Check if this block contains box-drawing characters
        if has_box_drawing(block_content):
            diagrams.append({
                'content': block_content,
                'start': match.start(),
                'end': match.end(),
                'lang': lang,
                'full_match': match.group(0)
            })

    return diagrams, content


def unicode_to_ascii_diagram(content):
    """Convert Unicode box-drawing characters to ASCII for goat."""
    replacements = {
        # Corners
        '┌': '+', '┐': '+', '└': '+', '┘': '+',
        '╔': '+', '╗': '+', '╚': '+', '╝': '+',
        # T-junctions
        '├': '+', '┤': '+', '┬': '+', '┴': '+',
        '╠': '+', '╣': '+', '╦': '+', '╩': '+',
        # Cross
        '┼': '+', '╬': '+',
        # Horizontal lines
        '─': '-', '═': '=',
        # Vertical lines
        '│': '|', '║': '|',
        # Arrows
        '→': '>', '←': '<', '↑': '^', '↓': 'v',
        '▶': '>', '◀': '<', '▲': '^', '▼': 'v',
        '►': '>', '◄': '<',
        # Double arrows
        '⟶': '->', '⟵': '<-',
        '⟷': '<->',
        # Checkboxes
        '✕': 'x', '✓': 'v', '✗': 'x',
    }

    result = content
    for unicode_char, ascii_char in replacements.items():
        result = result.replace(unicode_char, ascii_char)

    # Escape characters that goat interprets specially
    result = result.replace('/', '∕')  # U+2215 DIVISION SLASH
    result = result.replace('\\', '⧵')  # U+29F5 REVERSE SOLIDUS OPERATOR
    result = result.replace('*', '∗')  # U+2217 ASTERISK OPERATOR

    return result


def extract_diagram_title(content):
    """Try to extract a title/description from the diagram content."""
    lines = content.strip().split('\n')

    # Look for text in the first few lines that might be a title
    for line in lines[:5]:
        # Remove box-drawing characters and whitespace
        text = line.strip()
        for char in BOX_CHARS:
            text = text.replace(char, '')
        text = text.strip('+-|= ')

        # If we have meaningful text, use it
        if text and len(text) > 3 and not text.startswith('[') and not text.startswith('('):
            # Truncate if too long
            if len(text) > 60:
                text = text[:57] + '...'
            return text

    return "Diagram"


def save_diagram_txt(diagram_content, output_path, dry_run=False):
    """Save diagram content to a .txt file, converting Unicode to ASCII."""
    ascii_content = unicode_to_ascii_diagram(diagram_content)

    if dry_run:
        print(f"  Would create: {output_path}")
        return True

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ascii_content.rstrip('\n') + '\n')
    print(f"  Created: {output_path}")
    return True


def find_goat():
    """Find goat executable."""
    goat_in_path = shutil.which('goat')
    if goat_in_path:
        return goat_in_path

    candidates = [
        os.path.expanduser('~/go/bin/goat'),
        '/usr/local/bin/goat',
        '/opt/homebrew/bin/goat',
    ]

    for path in candidates:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path

    return None


def convert_to_svg(txt_path, svg_path, color='#333333', dry_run=False):
    """Convert .txt diagram to SVG using goat."""
    if dry_run:
        print(f"  Would create: {svg_path}")
        return True

    goat_cmd = find_goat()
    if not goat_cmd:
        print("  ERROR: goat not found (install with: go install github.com/blampe/goat@latest)")
        return False

    try:
        result = subprocess.run(
            [goat_cmd, '-i', str(txt_path), '-o', str(svg_path), '-sls', color],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"  Created: {svg_path}")
            return True
        else:
            print(f"  ERROR converting {txt_path}: {result.stderr}")
            return False
    except FileNotFoundError:
        print("  ERROR: goat not found in PATH")
        return False


def get_svg_dimensions(svg_path):
    """Extract width and height from SVG file."""
    import xml.etree.ElementTree as ET

    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()

        width = root.get('width', '').replace('px', '')
        height = root.get('height', '').replace('px', '')

        if width and height:
            return float(width), float(height)

        viewbox = root.get('viewBox')
        if viewbox:
            parts = viewbox.split()
            if len(parts) == 4:
                return float(parts[2]), float(parts[3])
    except Exception as e:
        print(f"  WARNING: Could not parse SVG dimensions: {e}")

    return None, None


def convert_to_png(svg_path, png_path, dpi=72, scale=0.70, dry_run=False):
    """Convert SVG to PNG at specified DPI and scale."""
    if dry_run:
        print(f"  Would create: {png_path} ({dpi} DPI, {int(scale*100)}% scale)")
        return True

    # Calculate zoom factor: (target_dpi / svg_default_dpi) * scale
    # SVG default is 96 DPI
    zoom = (dpi / 96.0) * scale

    # Try rsvg-convert first (best quality)
    rsvg = shutil.which('rsvg-convert')
    if rsvg:
        cmd = [rsvg, '-z', str(zoom), '-o', str(png_path), str(svg_path)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  Created: {png_path} ({dpi} DPI, {int(scale*100)}% scale)")
            return True
        else:
            print(f"  rsvg-convert error: {result.stderr}")

    # Try Inkscape
    inkscape = shutil.which('inkscape')
    if inkscape:
        # Inkscape uses export-dpi, we need to adjust for scale
        effective_dpi = dpi * scale
        cmd = ['inkscape', '--export-type=png', f'--export-dpi={effective_dpi}',
               f'--export-filename={png_path}', str(svg_path)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  Created: {png_path} ({dpi} DPI, {int(scale*100)}% scale)")
            return True

    # ImageMagick as last resort
    convert = shutil.which('convert')
    if convert:
        density = int(dpi * scale / 0.72)  # Approximate
        cmd = ['convert', '-density', str(density), '-background', 'white',
               str(svg_path), '-flatten', str(png_path)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  Created: {png_path} (ImageMagick)")
            return True

    print(f"  WARNING: Could not convert to PNG (install librsvg: brew install librsvg)")
    return False


def update_markdown_file(filepath, diagrams, base_name, dry_run=False):
    """Update markdown file to replace inline diagrams with image references."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process diagrams in reverse order to preserve positions
    for idx, diagram in enumerate(reversed(diagrams), start=1):
        actual_idx = len(diagrams) - idx + 1
        png_name = f"{base_name}.diagram{actual_idx}.png"

        # Extract a title for alt text
        alt_text = extract_diagram_title(diagram['content'])

        # Create image reference
        img_ref = f"![{alt_text}]({png_name})"

        # Replace the code block with the image reference
        content = content[:diagram['start']] + img_ref + content[diagram['end']:]

    if dry_run:
        print(f"  Would update: {filepath}")
        return True

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Updated: {filepath}")
    return True


def process_file(md_file, extract_only=False, svg_only=False, no_update_md=False,
                 dry_run=False, dpi=72, scale=0.70, color='#333333'):
    """Process a single markdown file."""
    diagrams, content = extract_diagrams_from_file(md_file)

    if not diagrams:
        return []

    base_name = md_file.stem
    created_files = []

    print(f"\n{md_file.name}: {len(diagrams)} diagram(s)")

    for idx, diagram in enumerate(diagrams, start=1):
        txt_name = f"{base_name}.diagram{idx}.txt"
        svg_name = f"{base_name}.diagram{idx}.svg"
        png_name = f"{base_name}.diagram{idx}.png"

        txt_path = md_file.parent / txt_name
        svg_path = md_file.parent / svg_name
        png_path = md_file.parent / png_name

        # Save .txt
        if save_diagram_txt(diagram['content'], txt_path, dry_run):
            created_files.append(txt_path)

        if not extract_only:
            # Convert to SVG
            if convert_to_svg(txt_path, svg_path, color, dry_run):
                created_files.append(svg_path)

                if not svg_only:
                    # Convert to PNG
                    if convert_to_png(svg_path, png_path, dpi, scale, dry_run):
                        created_files.append(png_path)

    # Update markdown file to reference PNGs
    if not extract_only and not svg_only and not no_update_md:
        update_markdown_file(md_file, diagrams, base_name, dry_run)

    return created_files


def process_directory(base_path, content_dir, **kwargs):
    """Process all markdown files in a content directory."""
    dir_path = base_path / content_dir
    if not dir_path.exists():
        return []

    all_files = []
    md_files = sorted(dir_path.glob("*.md"))

    for md_file in md_files:
        files = process_file(md_file, **kwargs)
        all_files.extend(files)

    return all_files


def main():
    parser = argparse.ArgumentParser(
        description='Extract Unicode diagrams from markdown and convert to PNG'
    )
    parser.add_argument('--extract-only', action='store_true',
                        help='Only extract .txt files, no SVG/PNG conversion')
    parser.add_argument('--svg-only', action='store_true',
                        help='Create SVG files but skip PNG conversion')
    parser.add_argument('--no-update-md', action='store_true',
                        help="Don't modify markdown files")
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be done without making changes')
    parser.add_argument('--dpi', type=int, default=72,
                        help='PNG DPI (default: 72)')
    parser.add_argument('--scale', type=float, default=0.70,
                        help='PNG scale factor (default: 0.70)')
    parser.add_argument('--color', default='#333333',
                        help='SVG line color (default: #333333)')

    args = parser.parse_args()

    # Get base path (script is in scripts/)
    script_path = Path(__file__).resolve()
    base_path = script_path.parent.parent

    print("Extracting Unicode diagrams from markdown files...")
    print(f"Settings: DPI={args.dpi}, Scale={int(args.scale*100)}%, Color={args.color}")
    if args.dry_run:
        print("DRY RUN - no files will be created or modified")
    print("=" * 60)

    all_files = []

    for content_dir in CONTENT_DIRS:
        files = process_directory(
            base_path, content_dir,
            extract_only=args.extract_only,
            svg_only=args.svg_only,
            no_update_md=args.no_update_md,
            dry_run=args.dry_run,
            dpi=args.dpi,
            scale=args.scale,
            color=args.color
        )
        all_files.extend(files)

    print("\n" + "=" * 60)
    print(f"Total files created: {len(all_files)}")

    if args.extract_only:
        print("(Extract only mode - no SVG/PNG conversion)")
    elif args.svg_only:
        print("(SVG only mode - no PNG conversion)")
    elif args.no_update_md:
        print("(Markdown files not modified)")


if __name__ == "__main__":
    main()
