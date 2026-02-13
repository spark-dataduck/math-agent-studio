#!/usr/bin/env python3
"""
PDF Validation Script
Validates that a given path points to a valid, readable PDF file.
Exit code 0 = success, 1 = failure
"""
import sys
from pathlib import Path


def validate_pdf(pdf_path: str) -> bool:
    """
    Validate that the given path is a readable PDF file.

    Args:
        pdf_path: Path to the PDF file to validate

    Returns:
        True if validation passes, False otherwise
    """
    path = Path(pdf_path)

    # Check file exists
    if not path.exists():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return False

    # Check it's a file (not a directory)
    if not path.is_file():
        print(f"ERROR: Path is not a file: {pdf_path}", file=sys.stderr)
        return False

    # Check PDF extension
    if path.suffix.lower() != '.pdf':
        print(f"ERROR: File is not a PDF (extension: {path.suffix}): {pdf_path}", file=sys.stderr)
        return False

    # Check file size (catch corrupted/empty PDFs)
    file_size = path.stat().st_size
    if file_size < 1024:  # Less than 1KB
        print(f"ERROR: PDF file too small ({file_size} bytes, possibly corrupted): {pdf_path}", file=sys.stderr)
        return False

    # All checks passed
    print(f"SUCCESS: PDF validated: {pdf_path}")
    print(f"  - Size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")
    print(f"  - Name: {path.name}")
    return True


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) != 2:
        print("Usage: validate_pdf.py <path-to-pdf>", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    success = validate_pdf(pdf_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
