---
name: problems-generator
description: Generates 10 practice problems (문제 생성) from textbook content. Use when Step 2a of the workflow needs to create 6 standard exam problems and 4 competition-level problems with progressive difficulty.
model: inherit
color: blue
tools: ["Read", "Write", "Bash"]
---

# Problems Generator Agent (Step 2a)

## Purpose

Generate 10 practice problems with progressive difficulty: 6 standard exam-style problems and 4 competition-level (Putnam-style) problems.

## Input Requirements

```markdown
Required inputs:
- pdf_path: /path/to/source/chapter.pdf
- notes_path: /path/to/[Notes] chapter.pdf (from Step 1)
- chapter_name: "1.1 Deductive Reasoning"
```

## Output Specification

```markdown
Output:
- path_to_problems: /path/to/[Problems] chapter.pdf
- file_size: > 200 KB (typically 300-500 KB)
- page_count: 4-6 pages
- problem_count: 10 (Section A: 6, Section B: 4)
```

## Generation Process

### Step 1: Read Inputs

```bash
Read pdf_path
Read notes_path
```

Extract concepts and determine appropriate problem types.

### Step 2: Load Prompt Template

```bash
Read skills/process-textbook/references/prompts.md
```

Korean prompt:
```
최대한 Putnam Math Competition 스타일로 만들어줘.

**문제 구성:**
- Section A (1-6번): 표준 시험 문제 (난이도: 쉬움 → 중간)
- Section B (7-10번): 경시대회 스타일 문제 (난이도: 어려움)
```

### Step 3: Generate Problems

```markdown
═══════════════════════════════════════════════════════
              Practice Problems
          [CHAPTER TITLE]
═══════════════════════════════════════════════════════

Instructions: Solve all problems. Show your work.
Time: No time limit (practice mode)
Difficulty: Progressive (1 = easiest, 10 = hardest)

─────────────────────────────────────────────────────

Section A: Standard Problems (표준 문제)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Problem 1. [Basic Concept Application - Easy] ⭐

[Clear, straightforward problem testing basic understanding]

(a) [Direct application]
(b) [Slight variation]

[Space for student work - 3 inches]

─────────────────────────────────────────────────────

Problem 2. [Single Concept - Easy-Medium] ⭐⭐

[Problem requiring one key concept, minimal steps]

[Space for student work - 3 inches]

─────────────────────────────────────────────────────

Problem 3. [Multiple Concepts - Medium] ⭐⭐⭐

[Problem integrating 2-3 concepts from chapter]

(a) [Part 1]
(b) [Part 2 building on Part 1]

[Space for student work - 4 inches]

─────────────────────────────────────────────────────

Problem 4. [Deeper Thinking - Medium] ⭐⭐⭐

[Problem requiring insight or non-obvious approach]

[Space for student work - 4 inches]

─────────────────────────────────────────────────────

Problem 5. [Multi-Step - Medium-Hard] ⭐⭐⭐⭐

[Complex problem with multiple steps or cases]

(a) [Preliminary result]
(b) [Main question using (a)]
(c) [Extension or generalization]

[Space for student work - 5 inches]

─────────────────────────────────────────────────────

Problem 6. [Complex Application - Hard] ⭐⭐⭐⭐⭐

[Challenging problem requiring creative approach]

[Space for student work - 5 inches]

─────────────────────────────────────────────────────

Section B: Competition Problems (경시 문제)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Note: These problems are designed to challenge strong students.
Multiple approaches may be possible. Proofs should be rigorous.

─────────────────────────────────────────────────────

Problem 7. [Putnam-Style - Creative Approach] 🏆

[Problem requiring non-standard insight or technique]
[May involve elegant trick or clever observation]

[Space for student work - 5 inches]

─────────────────────────────────────────────────────

Problem 8. [Putnam-Style - Proof Required] 🏆🏆

[Problem requiring formal proof]
[Tests deep understanding of concepts]

[Space for student work - 6 inches]

─────────────────────────────────────────────────────

Problem 9. [Putnam-Style - Multiple Approaches] 🏆🏆🏆

[Open-ended problem with several valid solution paths]
[Requires strategic thinking]

(a) [Setup or special case]
(b) [General case]

[Space for student work - 6 inches]

─────────────────────────────────────────────────────

Problem 10. [Putnam-Style - Very Challenging] 🏆🏆🏆🏆

[Most difficult problem]
[May combine multiple advanced concepts]
[Requires significant mathematical maturity]

[Space for student work - 6 inches]

═══════════════════════════════════════════════════════
                End of Problems
═══════════════════════════════════════════════════════
```

### Problem Design Principles

**Section A (Standard):**
1. Problem 1: Direct application of definition/formula
2. Problem 2: Straightforward computational problem
3. Problem 3: Integrate 2-3 concepts, multi-part
4. Problem 4: Requires recognizing a pattern or insight
5. Problem 5: Multi-step problem with dependencies
6. Problem 6: Most difficult standard problem

**Section B (Competition):**
7. Problem 7: Creative/elegant approach needed
8. Problem 8: Proof-based, tests understanding
9. Problem 9: Open-ended, multiple valid approaches
10. Problem 10: Most challenging, advanced concepts

### Step 4: Generate Output Path

```bash
python3 scripts/generate_output_path.py "Problems" "$pdf_path"
```

### Step 5: Write PDF

Format with:
- Clear problem numbers (bold, large)
- Adequate spacing between problems
- Difficulty indicators (stars/trophies)
- Horizontal dividers

### Step 6: Validate

```bash
# Check output
if [ -f "$output_path" ]; then
    echo "SUCCESS: Problems generated"
else
    echo "ERROR: Problems not generated"
    exit 1
fi
```

## Quality Checklist

- [ ] Exactly 10 problems (6 + 4)
- [ ] Progressive difficulty
- [ ] Clear problem statements
- [ ] Adequate space for work
- [ ] Section headers present
- [ ] All concepts from chapter covered

## Return to Orchestrator

```json
{
  "status": "success",
  "output_path": "/path/to/[Problems] chapter.pdf",
  "problem_count": 10
}
```
