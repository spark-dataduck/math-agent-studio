#!/usr/bin/env python3
"""
Generate PDF from HTML using Playwright/Chromium with KaTeX math rendering.

Supports multi-page documents with headers, footers, and automatic math
typesetting. Used by all generator agents in the math-agent-studio plugin.

Usage:
    python3 scripts/generate_pdf.py input.html output.pdf
    python3 scripts/generate_pdf.py input.html output.pdf --mode notes
    python3 scripts/generate_pdf.py input.html output.pdf --mode notes --footer-left "© 2026 Author"
"""

import sys
import os
import argparse
from pathlib import Path

# Mode presets: each mode defines PDF generation parameters
MODES = {
    "notes": {
        "scale": 1.0,
        "margin_top": "0.75in",
        "margin_bottom": "0.75in",
        "margin_left": "0",
        "margin_right": "0",
        "display_header_footer": True,
        "print_background": True,
    },
    "problems": {
        "scale": 1.0,
        "margin_top": "0.75in",
        "margin_bottom": "0.75in",
        "margin_left": "0",
        "margin_right": "0",
        "display_header_footer": True,
        "print_background": True,
    },
    "answers": {
        "scale": 0.95,
        "margin_top": "0.5in",
        "margin_bottom": "0.5in",
        "margin_left": "0",
        "margin_right": "0",
        "display_header_footer": False,
        "print_background": True,
    },
    "explanations": {
        "scale": 1.0,
        "margin_top": "0.75in",
        "margin_bottom": "0.75in",
        "margin_left": "0",
        "margin_right": "0",
        "display_header_footer": True,
        "print_background": True,
    },
    "script": {
        "scale": 1.0,
        "margin_top": "0.75in",
        "margin_bottom": "0.75in",
        "margin_left": "0",
        "margin_right": "0",
        "display_header_footer": True,
        "print_background": True,
    },
}

# Resolve the project root (two levels up from this script)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
KATEX_DIR = PROJECT_ROOT / "skills" / "process-textbook" / "assets" / "katex"


def build_header_template(footer_left=""):
    """Build Chromium PDF header template.

    Uses Chromium's built-in .title class which reads from <title> tag.
    The header is rendered as italic text in a smaller font.
    """
    return """
    <div style="font-size:9px; font-family:'Times New Roman',serif; font-style:italic;
                width:100%; padding:0 1in; color:#666;">
        <span class="title"></span>
    </div>
    """


def build_footer_template(footer_left=""):
    """Build Chromium PDF footer template.

    Left side: copyright or custom text. Center: page number in "- N -" format.
    """
    left_text = footer_left if footer_left else ""
    return f"""
    <div style="font-size:9px; font-family:'Times New Roman',serif;
                width:100%; padding:0 1in; display:flex; justify-content:space-between; color:#666;">
        <span>{left_text}</span>
        <span style="flex:1; text-align:center;">- <span class="pageNumber"></span> -</span>
        <span style="width:33%;"></span>
    </div>
    """


def inject_katex(page):
    """Inject KaTeX CSS, JS, and auto-render into the page.

    Loads from local bundled files to avoid network dependency.
    Falls back to CDN if local files are missing.
    """
    katex_css = KATEX_DIR / "katex.min.css"
    katex_js = KATEX_DIR / "katex.min.js"
    auto_render_js = KATEX_DIR / "contrib" / "auto-render.min.js"

    if katex_css.exists() and katex_js.exists() and auto_render_js.exists():
        page.add_style_tag(path=str(katex_css))
        page.add_script_tag(path=str(katex_js))
        page.add_script_tag(path=str(auto_render_js))
    else:
        print("Warning: Local KaTeX not found, using CDN fallback...")
        page.add_style_tag(
            url="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css"
        )
        page.add_script_tag(
            url="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"
        )
        page.add_script_tag(
            url="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
        )

    # Trigger auto-render on the document body
    page.evaluate("""
        if (typeof renderMathInElement !== 'undefined') {
            renderMathInElement(document.body, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                    {left: '\\\\(', right: '\\\\)', display: false},
                    {left: '\\\\[', right: '\\\\]', display: true}
                ],
                throwOnError: false
            });
        }
    """)


def generate_pdf(html_path, pdf_path, mode="notes", footer_left=""):
    """Generate PDF from HTML using Playwright Chromium."""
    from playwright.sync_api import sync_playwright

    html_path = Path(html_path).resolve()
    pdf_path = Path(pdf_path).resolve()

    # Ensure output directory exists
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    preset = MODES.get(mode, MODES["notes"])

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 816, "height": 1056})

        page.goto(f"file://{html_path}")
        page.wait_for_timeout(1000)

        # Inject KaTeX for math rendering
        inject_katex(page)

        # Wait for KaTeX to render all math expressions
        page.wait_for_timeout(2000)

        # Build PDF options
        pdf_options = {
            "path": str(pdf_path),
            "format": "Letter",
            "print_background": preset["print_background"],
            "scale": preset["scale"],
            "margin": {
                "top": preset["margin_top"],
                "bottom": preset["margin_bottom"],
                "left": preset["margin_left"],
                "right": preset["margin_right"],
            },
        }

        if preset["display_header_footer"]:
            pdf_options["display_header_footer"] = True
            pdf_options["header_template"] = build_header_template()
            pdf_options["footer_template"] = build_footer_template(footer_left)

        page.pdf(**pdf_options)
        browser.close()

    file_size = pdf_path.stat().st_size
    print(f"PDF saved: {pdf_path} ({file_size:,} bytes)")
    return str(pdf_path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate PDF from HTML using Playwright"
    )
    parser.add_argument("input", help="Input HTML file path")
    parser.add_argument("output", help="Output PDF file path")
    parser.add_argument(
        "--mode",
        choices=list(MODES.keys()),
        default="notes",
        help="PDF generation mode (default: notes)",
    )
    parser.add_argument(
        "--footer-left", default="", help="Text for footer left side (e.g. copyright)"
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found")
        sys.exit(1)

    # Auto-install playwright if needed
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Installing playwright...")
        os.system("pip install playwright --break-system-packages -q")
        os.system("playwright install chromium")

    generate_pdf(args.input, args.output, mode=args.mode, footer_left=args.footer_left)


if __name__ == "__main__":
    main()
