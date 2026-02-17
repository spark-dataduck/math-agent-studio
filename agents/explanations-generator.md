---
name: explanations-generator
description: Generates detailed step-by-step solutions with multiple approaches. Use when Step 2c of the workflow needs to create comprehensive explanations for all 10 problems from Step 2a.
model: inherit
color: yellow
tools: ["Read", "Write", "Bash"]
allowed-tools:
  - Read
  - Write(reference_outputs/**)
  - Write(/tmp/math-agent-studio-*)
  - Bash(python3 scripts/generate_pdf.py *)
  - Bash(python3 scripts/generate_output_path.py *)
  - Bash(pip install playwright)
  - Bash(playwright install chromium)
  - Bash(stat *)
  - Bash(file *)
  - Bash(ls *)
  - Bash(mkdir *)
---

# Explanations Generator Agent (Step 2c)

## Purpose

Generate detailed step-by-step solutions for all 10 problems with multiple solution approaches where applicable. Output is a 2-3 page PDF generated via the HTML→Playwright pipeline.

## Input Requirements

```markdown
Required inputs:
- problems_path: /path/to/[Problems] chapter.pdf (from Step 2a)
- chapter_name: "1.1 Deductive Reasoning"
```

## Output Specification

```markdown
Output:
- path_to_explanations: /path/to/[Explanations] chapter.pdf
- file_size: > 100 KB (typically 400-600 KB)
- page_count: 2-3 pages
```

## Generation Process

### Step 1: Read Problems

```bash
Read problems_path
```

Extract all 10 problems to solve.

### Step 2: Load Prompt Template

```bash
Read skills/process-textbook/references/prompts.md
```

Locate the **"4. Explanations Generation (Detailed Solutions)"** section.

### Step 3: Solve All Problems

For each problem, prepare:
1. **Restatement** of the problem (brief)
2. **Answer** (bold, prominent)
3. **Step-by-step solution** with justification for each step
4. **Common mistakes** to warn about (where applicable)
5. **Alternative methods** (where applicable, especially for competition problems)

### Step 4: Generate Output Path

```bash
python3 scripts/generate_output_path.py "Explanations" "$problems_path"
```

### Step 5: Format and Generate PDF (HTML → Playwright Pipeline)

#### 5a. Read the CSS stylesheet

```bash
Read skills/process-textbook/assets/content-base.css
```

Embed the entire contents in a `<style>` block in your HTML.

#### 5b. Generate the HTML document

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Detailed Solutions — Section 1.1</title>
    <style>
        /* Paste entire contents of content-base.css here */
    </style>
</head>
<body>
    <!-- Compact Title Header -->
    <div class="title-header">
        <h1>Detailed Solutions</h1>
        <div class="subtitle">Chapter 1.1: Deductive Reasoning and Logical Connectives</div>
        <div class="meta">How To Prove It — Daniel J. Velleman | Complete step-by-step solutions for all 10 problems</div>
    </div>

    <!-- Section A Solutions -->
    <div class="section-header">Section A Solutions: Standard Problems</div>

    <div class="solution-block">
        <div class="problem-restate">
            <strong>Problem 1.</strong> [Brief restatement of the problem]
        </div>
        <div class="answer-line">Answer: (a) [answer], (b) [answer]</div>

        <p><strong>Part (a):</strong></p>
        <div class="step">
            <span class="step-label">Step 1:</span> [First step with justification]
        </div>
        <div class="step">
            <span class="step-label">Step 2:</span> [Second step]
        </div>
        <div class="step">
            <span class="step-label">Step 3:</span> Therefore, [answer]. ✓
        </div>

        <p><strong>Part (b):</strong></p>
        <div class="step">
            <span class="step-label">Step 1:</span> From part (a), we know...
        </div>
        <div class="step">
            <span class="step-label">Step 2:</span> Therefore, [answer]. ✓
        </div>
    </div>

    <div class="solution-block">
        <div class="problem-restate">
            <strong>Problem 2.</strong> [Brief restatement]
        </div>
        <div class="answer-line">Answer: [answer]</div>

        <div class="method-title">Method 1: [Primary approach]</div>
        <div class="step">
            <span class="step-label">Step 1:</span> [Work]
        </div>
        <div class="step">
            <span class="step-label">Step 2:</span> Therefore, [answer]. ✓
        </div>

        <div class="method-title">Method 2: [Alternative approach]</div>
        <div class="step">
            <span class="step-label">Step 1:</span> [Different starting point]
        </div>
        <div class="step">
            <span class="step-label">Step 2:</span> Same answer: [answer]. ✓
        </div>

        <div class="warning-box no-break">
            <div class="box-title">Common Mistake ⚠️</div>
            <p>Many students [describe error]. This is incorrect because [explanation].</p>
        </div>
    </div>

    <!-- ... Solutions 3-6 ... -->

    <!-- Page break before Section B Solutions -->
    <div class="page-break">
        <div class="section-header">Section B Solutions: Competition Problems</div>

        <div class="solution-block">
            <div class="problem-restate">
                <strong>Problem 7.</strong> [Brief restatement]
            </div>
            <div class="answer-line">Answer: [answer]</div>

            <p><strong>Key Insight:</strong> [Non-obvious observation that unlocks the problem]</p>

            <div class="step">
                <span class="step-label">Step 1:</span> [Setup using key insight]
            </div>
            <div class="step">
                <span class="step-label">Step 2:</span> [Apply technique]
            </div>
            <div class="step">
                <span class="step-label">Step 3:</span> Therefore, [answer]. ✓
            </div>

            <div class="tip-box no-break">
                <div class="box-title">Why This Works 💡</div>
                <p>[Explain the intuition behind the solution approach]</p>
            </div>
        </div>

        <!-- ... Solutions 8-10 ... -->
    </div>
</body>
</html>
```

**Key rules for HTML generation:**

**CSS class rules:**
- Use ONLY classes from content-base.css: `.title-header`, `.subtitle`, `.meta`, `.section-header`, `.solution-block`, `.problem-restate`, `.answer-line`, `.step`, `.step-label`, `.method-title`, `.warning-box`, `.tip-box`, `.box-title`, `.page-break`, `.no-break`, `.math-display`, `.section-divider`
- Do NOT invent custom CSS classes
- Do NOT add custom `<style>` blocks or inline styles

**Page breaks and density:**
- Use `.page-break` ONLY before Section B solutions (to separate standard from competition)
- Let solutions flow naturally — target 2-3 pages total
- `.solution-block` has a bottom border that visually separates problems

**Solution structure per problem:**
- `.problem-restate` — brief italic restatement in gray background
- `.answer-line` — bold answer in navy background (prominent, easy to find)
- `.step` divs with `.step-label` — step-by-step work
- `.method-title` — for alternative approaches
- `.warning-box` — for common mistakes (use sparingly, not on every problem)
- `.tip-box` — for key insights (especially on competition problems)

**Math rendering:**
- Wrap inline LaTeX in `$...$` — KaTeX auto-renders
- Wrap display LaTeX in `$$...$$` — KaTeX auto-renders
- Use `<div class="math-display">$$...$$</div>` for centered display math
- Do NOT include `<link>` or `<script>` tags for KaTeX — injected automatically

**Emojis and HTML entities:**
- Use Unicode emoji characters directly (⚠️, 💡, ✓, ✗) or numeric entities (`&#x26A0;`, `&#x1F4A1;`)
- Do NOT invent named HTML entities — `&warning;`, `&star;`, `&check;` do NOT exist and render as literal text
- Only standard named entities are valid: `&amp;`, `&lt;`, `&gt;`, `&nbsp;`, `&mdash;`, `&ndash;`

**Content guidelines:**
- Be thorough: don't skip steps
- Explain WHY each step works, not just WHAT to do
- Show at least 1 alternative method for competition problems (7-10)
- Highlight common mistakes with `.warning-box` where students typically err
- Use encouraging tone: "The key insight is..." rather than "Obviously..."

#### 5c. Write the HTML to a temp file

```bash
Write /tmp/math-agent-studio-explanations-{chapter-slug}.html [full HTML content]
```

#### 5d. Generate the PDF

```bash
python3 scripts/generate_pdf.py /tmp/math-agent-studio-explanations-{chapter-slug}.html "{output_path}" --mode explanations --footer-left "© 2026 Daniel Velleman"
```

### Step 6: Validate Output

```bash
if [ -f "$output_path" ]; then
    file_size=$(stat -f%z "$output_path" 2>/dev/null || stat -c%s "$output_path")

    if [ $file_size -lt 102400 ]; then
        echo "ERROR: Output file too small ($file_size bytes)"
        exit 1
    fi

    if ! file "$output_path" | grep -q "PDF"; then
        echo "ERROR: Output is not a valid PDF"
        exit 1
    fi

    page_count=$(pdfinfo "$output_path" 2>/dev/null | grep "^Pages:" | awk '{print $2}')
    if [ -z "$page_count" ]; then
        page_count=$(strings "$output_path" | grep -c "/Type /Page[^s]" || echo "unknown")
    fi

    echo "SUCCESS: Explanations generated ($file_size bytes, $page_count pages)"
    if [ "$page_count" != "unknown" ] && [ "$page_count" -gt 3 ]; then
        echo "WARNING: Page count ($page_count) exceeds 3-page target."
    fi

    echo "$output_path"
else
    echo "ERROR: Explanations not found at $output_path"
    exit 1
fi
```

### Step 7: Return to Orchestrator

```json
{
  "status": "success",
  "output_path": "/path/to/[Explanations] chapter.pdf",
  "file_size": 445000,
  "page_count": 3,
  "explanation_count": 10
}
```

## Quality Checklist

- [ ] All 10 problems explained
- [ ] Step-by-step solutions with justifications
- [ ] Bold answers in `.answer-line` (easy to find)
- [ ] At least 1 alternative method for competition problems
- [ ] Common mistakes highlighted with `.warning-box`
- [ ] Clear mathematical notation (KaTeX renders correctly)
- [ ] Encouraging, educational tone
- [ ] File size > 100 KB
- [ ] Page count 2-3

## Error Handling

**Issue 1: Playwright not installed**
- Fix: Script auto-installs via `pip install playwright && playwright install chromium`

**Issue 2: PDF too many pages (>3)**
- Fix: Make solutions more concise, reduce per-step verbosity, limit alternative methods

**Issue 3: Mathematical notation broken**
- Fix: Check LaTeX syntax — use `\text{}` for text in math mode

### Retry Strategy

If validation fails:
1. First attempt: Retry with same inputs
2. Second attempt: Retry with more concise solutions
3. Third attempt: Return error to orchestrator with details

## Dependencies

This agent depends on:
- **Step 2a**: problems-generator (must read problems to solve them)

## Outputs Used By

No downstream dependencies — this is a terminal output.
