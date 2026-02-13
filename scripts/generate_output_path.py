#!/usr/bin/env python3
"""
Output Path Generator
Generates standardized output filenames following the pattern:
    reference_outputs/[Type] Section Title [Textbook].pdf

Example:
    Input: reference_source/1.1 Foo [Book].pdf
    Output: reference_outputs/[Notes] 1.1 Foo [Book].pdf
"""
import sys
from pathlib import Path


def generate_output_path(source_pdf_path: str, output_type: str) -> str:
    """
    Generate output path following naming convention.

    Args:
        source_pdf_path: Path to the source PDF (e.g., "reference_source/1.1 Foo.pdf")
        output_type: Type of output (Notes, Problems, Quick Answers, Explanations, Script)

    Returns:
        Full path to the output file

    Example:
        >>> generate_output_path("reference_source/1.1 Foo [Book].pdf", "Notes")
        'reference_outputs/[Notes] 1.1 Foo [Book].pdf'
    """
    source_path = Path(source_pdf_path)

    # Get the base filename without extension
    basename = source_path.stem

    # Determine output directory (parallel to reference_source)
    source_dir = source_path.parent
    output_dir = source_dir.parent / "reference_outputs"

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate output filename with type prefix
    output_filename = f"[{output_type}] {basename}.pdf"

    return str(output_dir / output_filename)


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) != 3:
        print("Usage: generate_output_path.py <output-type> <source-pdf-path>", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print('  generate_output_path.py "Notes" "reference_source/1.1 Foo.pdf"', file=sys.stderr)
        print("\nValid output types:", file=sys.stderr)
        print("  - Notes", file=sys.stderr)
        print("  - Problems", file=sys.stderr)
        print("  - Quick Answers", file=sys.stderr)
        print("  - Explanations", file=sys.stderr)
        print("  - Script", file=sys.stderr)
        sys.exit(1)

    output_type = sys.argv[1]
    source_pdf = sys.argv[2]

    # Validate output type
    valid_types = ["Notes", "Problems", "Quick Answers", "Explanations", "Script"]
    if output_type not in valid_types:
        print(f"ERROR: Invalid output type '{output_type}'", file=sys.stderr)
        print(f"Valid types: {', '.join(valid_types)}", file=sys.stderr)
        sys.exit(1)

    output_path = generate_output_path(source_pdf, output_type)
    print(output_path)


if __name__ == "__main__":
    main()
