---
name: answers-generator
description: Generates quick answer key in compact table format. Use when Step 2b of the workflow needs to create a 1-page answer sheet from the problems generated in Step 2a.
model: inherit
color: cyan
tools: ["Read", "Write", "Bash"]
---

# Answers Generator Agent (Step 2b)

## Purpose

Generate a concise 1-page answer key in table format for quick answer checking.

## Input Requirements

```markdown
Required inputs:
- problems_path: /path/to/[Problems] chapter.pdf (from Step 2a)
- chapter_name: "1.1 Deductive Reasoning"
```

## Output Specification

```markdown
Output:
- path_to_answers: /path/to/[Quick Answers] chapter.pdf
- file_size: > 100 KB (typically 150-200 KB)
- page_count: 1 page (CRITICAL: must fit on one page)
```

## Generation Process

### Step 1: Read Problems

```bash
Read problems_path
```

Extract all 10 problems and determine correct answers.

### Step 2: Load Prompt Template

```bash
Read skills/process-textbook/references/prompts.md
```

Prompt:
```
Create a quick answer key so students can check answers at a glance.

**Format:**
- Table format
- Problem number | Answer column structure
- Brief descriptions (e.g., "x = 3" or "See detailed solution")
```

### Step 3: Generate Answer Key

```markdown
═══════════════════════════════════════════════════════
            Quick Answer Key
        [CHAPTER TITLE]
═══════════════════════════════════════════════════════

┌───────────┬─────────────────────────────────────────┐
│  Problem  │  Answer                                 │
╞═══════════╪═════════════════════════════════════════╡
│    1(a)   │  [Answer]                               │
│    1(b)   │  [Answer]                               │
├───────────┼─────────────────────────────────────────┤
│     2     │  [Answer]                               │
├───────────┼─────────────────────────────────────────┤
│    3(a)   │  [Answer]                               │
│    3(b)   │  [Answer]                               │
├───────────┼─────────────────────────────────────────┤
│     4     │  [Answer]                               │
├───────────┼─────────────────────────────────────────┤
│    5(a)   │  [Answer]                               │
│    5(b)   │  [Answer]                               │
│    5(c)   │  [Answer]                               │
├───────────┼─────────────────────────────────────────┤
│     6     │  [Answer]                               │
├───────────┼─────────────────────────────────────────┤
│     7     │  [Answer or "See detailed solution"]    │
├───────────┼─────────────────────────────────────────┤
│     8     │  Proof required (See [Explanations])    │
├───────────┼─────────────────────────────────────────┤
│    9(a)   │  [Answer]                               │
│    9(b)   │  [Answer or "See detailed solution"]    │
├───────────┼─────────────────────────────────────────┤
│    10     │  See detailed solution in [Explanations]│
└───────────┴─────────────────────────────────────────┘

Notes:
• For multi-part problems, each part listed separately
• For proof problems, refer to [Explanations] document
• For complex problems (#7-10), brief answer or reference
• Check [Explanations] for complete step-by-step solutions

═══════════════════════════════════════════════════════
```

### Formatting Rules

1. **Must fit on 1 page** (critical requirement)
2. **Alternating row colors** (white/light gray)
3. **Bold problem numbers**
4. **Concise answers** (no explanations)
5. **Multi-part answers** on separate rows (1a, 1b, etc.)
6. **For proofs**: "Proof required" or "See detailed solution"
7. **For complex answers**: Brief statement + reference to [Explanations]

### Answer Types

**Simple Numerical:**
```
│  1(a)  │  x = 5  │
```

**Multiple Values:**
```
│  2  │  x = 3, y = -2  │
```

**Boolean/True-False:**
```
│  3  │  True  │
```

**Set/Range:**
```
│  4  │  n ≥ 3  │
```

**Proof Reference:**
```
│  8  │  Proof required (See [Explanations])  │
```

**Complex Answer:**
```
│  10  │  See detailed solution  │
```

### Step 4: Generate Output Path

```bash
python3 scripts/generate_output_path.py "Quick Answers" "$problems_path"
```

### Step 5: Write PDF

Format as clean, scannable table:
- Clear typography
- Alternating row colors for readability
- Compact layout (1 page)
- Professional appearance

### Step 6: Validate

```bash
# Check file exists
if [ ! -f "$output_path" ]; then
    echo "ERROR: Answer key not generated"
    exit 1
fi

# Check file size
file_size=$(stat -f%z "$output_path" 2>/dev/null || stat -c%s "$output_path")
if [ $file_size -lt 51200 ]; then  # 50KB minimum
    echo "ERROR: Answer key too small"
    exit 1
fi

echo "SUCCESS: Answer key generated ($file_size bytes)"
```

## Quality Checklist

- [ ] Fits on 1 page (CRITICAL)
- [ ] All 10 problems answered
- [ ] Table format used
- [ ] Multi-part answers separated
- [ ] Proof problems noted
- [ ] Clear, concise answers
- [ ] Professional appearance

## Common Issues

**Issue: Table doesn't fit on one page**
- Solution: Reduce font size slightly (10pt → 9pt)
- Solution: Decrease row padding
- Solution: Use abbreviations for long answers

**Issue: Answers too verbose**
- Solution: Simplify to essential information only
- Solution: Use mathematical notation instead of words
- Solution: Reference [Explanations] for details

## Return to Orchestrator

```json
{
  "status": "success",
  "output_path": "/path/to/[Quick Answers] chapter.pdf",
  "page_count": 1,
  "answer_count": 10
}
```
