# Math Textbook Processing Prompts

This file contains all AI prompt templates for generating the 5 output types from math textbook PDFs.
All prompts and outputs are in **English**.

---

## 1. Notes Generation (Comprehensive Study Notes)

**Purpose:** Generate comprehensive study notes (8-11 pages) with concepts, mnemonics, examples, and common traps.

**Target Audience:** Students preparing for exams who need structured, visual study materials.

**Output Format:** PDF with colored boxes, tables, icons, and visual hierarchy.

### Prompt:

```
Organize key concepts, formulas, and keywords so they stand out clearly. After each concept or formula, immediately include easy examples.

Mention common mistakes and confusing points that students frequently get wrong on exams, and add analogies or visual mnemonics that help with understanding.

**Required Elements:**
- THE BIG IDEA (navy box): Core concept of the chapter
- Visual Mnemonics: Analogies/metaphors to remember concepts easily
- Definition Tables: Definitions organized in table format
- Common Traps (red warning): Frequently made mistakes
- Useful Tips (orange box): Helpful tips for problem-solving
- "Try These" examples: 3-4 practice problems per concept
- Practice Problems: Exam Level (final 2 pages, problems only — NO answer key)
  - Section A: Standard Exam Problems (6 problems, progressive difficulty)
  - Section B: Competition-Style Problems 🏆 (4-5 problems)
    - Diverse types: Knights & Knaves, Liar Puzzles, Number Theory, Chain Arguments, AMC-style
  - Problems test ALL concepts from the notes
  - Header: "Work through each problem, then check the [Quick Answers] document for solutions."

**Format Guide:**
- **8-11 pages total** (STRICT target — not 12, not 15, not 17)
- **Total content: ~2,200-2,800 words** (NOT 3,200+). If over 2,800 words, cut content.
- **Each concept section: ~500-650 words** including all boxes and Try These
- Page 1: Title page (dedicated full page, no content boxes)
- Pages 2-9: Concepts with inline Try These (3-4 major concepts, each spanning 2-3 pages)
- Pages 10-11: Practice Problems: Exam Level — **problems only, NO answer key** (answers go in Quick Answers output)
- Color coding: pastel tints with accent-color borders (navy = core concepts, red = warnings, orange = tips)
- Use tables and diagrams extensively
- Notation must be clear and precise
- **Information density:** Each concept page should have ~60-80% text/content coverage (not 30-40%). Allow reasonable whitespace between sections, but don't waste half-pages unnecessarily.
- **Box titles MUST include emojis:** THE BIG IDEA 💡, Common Trap ⚠️, Useful Tip 💡, Try These! 📝, mnemonics can use 🧠 or 🎯
- **Per-element word limits:** Big Idea box 80-120 words (prose, no bullet lists), Mnemonic 40-60 words, Common Trap 40-60 words, Useful Tip 40-60 words, Try These ≤3 problems with 20-40 word answers each, Definition table 4-6 rows with "In Plain Terms" column
- **Per-concept MINIMUM: 450 words** — each concept section must have enough substance to fill ~2 pages. If thin, add richer table rows, longer mnemonic, or more detailed Try These solutions.
- **Concept limit:** 3-4 major concepts get full box treatment. If 5+ concepts, give minor ones just a heading + paragraph (no Big Idea box).
```

### Expected Output Structure:

```
[Notes] Chapter Title.pdf

Page 1: TITLE PAGE (dedicated, full page)
  - Book title (large, centered)
  - "Chapter N [Topic]"
  - Author name
  - Horizontal rule
  - "Section X.X: [Section Title]"
  - "Core Concepts • Mnemonics • Inline Examples • Competition Problems"
  - NO content boxes on this page

Pages 2-3 (or 2-4): Concept 1
  - THE BIG IDEA 💡 (pastel navy box)
  - Definition table
  - Visual mnemonic 🎯 or 🧠 (metaphor/analogy)
  - Key properties with inline examples
  - Common Trap ⚠️ (pastel pink box)
  - Useful Tip 💡 (pastel orange box)
  - Try These! 📝 (3-4 problems with solutions)
  - **ALL flow together in one concept section** without internal page breaks

Pages 4-5 (or 5-7): Concept 2
  - Same inline structure as Concept 1
  - Start with `.page-break` but then all elements flow together

Pages 6-9: Additional Concepts (if needed)
  - Each major concept gets its own `.page-break` to start
  - Aim for ~2-3 pages per concept including all boxes/tables/examples
  - **Target density: 60-80% of page filled with content** (not 30-40% with massive whitespace)

Pages 10-11: Practice Problems: Exam Level (problems only, NO answer key)
  - Section A: Standard Exam Problems (6 problems)
  - Section B: Competition-Style Problems 🏆 (4-5 problems)
  - NO Answer Key — answers go in the separate [Quick Answers] output
```

---

## 2. Problems Generation (Practice Problems)

**Purpose:** Generate 10 practice problems (6 standard exam + 4 competition level).

**Target Audience:** Students who want to test understanding and prepare for competitions.

**Output Format:** PDF with clearly numbered problems, progressive difficulty.

### Prompt:

```
Create problems in the style of the Putnam Math Competition as much as possible.

**Problem Structure:**
- Section A (Problems 1-6): Standard exam problems (difficulty: easy → medium)
- Section B (Problems 7-10): Competition-style problems (difficulty: hard)

**Requirements:**
- Each problem must test core concepts from the chapter
- Problems must have progressive difficulty
- Some problems should be multi-part
- Provide sufficient space between problems (for students to work)
- Clear numbering and separation

**Style:**
- Concise and clear problem statements
- Include diagrams where necessary
- Mix computational problems and proof problems appropriately
```

### Expected Output Structure:

```
[Problems] Chapter Title.pdf

Section A: Standard Problems

Problem 1. [Easy - Basic concept application]
  (a) ...
  (b) ...

Problem 2. [Easy-Medium - Single concept]
  ...

Problem 3. [Medium - Multiple concepts]
  ...

Problem 4. [Medium - Requires deeper thinking]
  ...

Problem 5. [Medium-Hard - Multi-step]
  ...

Problem 6. [Hard - Complex application]
  ...

Section B: Competition Problems

Problem 7. [Putnam-style - Creative approach needed]
  ...

Problem 8. [Putnam-style - Proof required]
  ...

Problem 9. [Putnam-style - Multiple approaches possible]
  ...

Problem 10. [Putnam-style - Very challenging]
  ...
```

---

## 3. Quick Answers Generation (Answer Key)

**Purpose:** Generate concise answer key in table format for quick checking.

**Target Audience:** Students who want to quickly verify their answers.

**Output Format:** 1-page PDF with compact table layout.

### Prompt:

```
Create a quick answer key so students can check answers at a glance.

**Format:**
- Table format
- Problem number | Answer column structure
- Alternating row colors
- Brief descriptions (e.g., "x = 3" or "See detailed solution")

**Requirements:**
- All answers on 1 page
- Clear and concise answers
- Multi-part problems show answers per part (e.g., 1a, 1b)
- Proof problems marked as "See detailed solution"
```

### Expected Output Structure:

```
[Quick Answers] Chapter Title.pdf

┌─────────┬─────────────────────────────────────┐
│ Problem │ Answer                              │
├─────────┼─────────────────────────────────────┤
│ 1(a)    │ x = 5                               │
│ 1(b)    │ y = -2                              │
├─────────┼─────────────────────────────────────┤
│ 2       │ True                                │
├─────────┼─────────────────────────────────────┤
│ 3       │ See detailed solution               │
├─────────┼─────────────────────────────────────┤
│ 4(a)    │ n ≥ 3                               │
│ 4(b)    │ Proof required                      │
├─────────┼─────────────────────────────────────┤
│ ...     │ ...                                 │
└─────────┴─────────────────────────────────────┘

Note: For proof problems, refer to [Explanations] document.
```

---

## 4. Explanations Generation (Detailed Solutions)

**Purpose:** Generate detailed step-by-step solutions with multiple approaches.

**Target Audience:** Students who got wrong answers or want to learn different solution methods.

**Output Format:** 2-3 page PDF with detailed explanations.

### Prompt:

```
Include both solutions and answers together. If there are multiple approaches to solving a problem, explain all of them.

**Required Elements:**
- Answers (bold emphasis)
- Step-by-step reasoning
- Case analysis when applicable
- Common errors highlighted
- Alternative solution methods

**Style:**
- Clear and logical explanations
- Explain the reasoning behind each step
- Mix formulas and text appropriately
- Highlight important insights
```

### Expected Output Structure:

```
[Explanations] Chapter Title.pdf

Problem 1.
Answer: (a) x = 5, (b) y = -2

Solution:
(a) Step 1: Start with the given equation...
    Step 2: Apply [concept name]...
    Step 3: Simplify to get x = 5.

(b) Step 1: From part (a), we know x = 5...
    Step 2: Substitute into the second equation...
    Step 3: Solve for y = -2.

Common Mistake: Students often forget to check...

Alternative Method: We could also approach this by...

---

Problem 2.
Answer: True

Solution:
Method 1 (Direct Proof):
  Let's prove this statement directly...
  [Step-by-step proof]

Method 2 (Contradiction):
  Alternatively, assume the negation...
  [Proof by contradiction]

Key Insight: This problem tests understanding of...

---

[Continue for all 10 problems]
```

---

## 5. Script Generation (YouTube Script)

**Purpose:** Generate 10-minute YouTube educational video script.

**Target Audience:** Visual/auditory learners who prefer video content.

**Output Format:** 6-page PDF with timing markers and natural dialogue.

### Prompt:

```
Write a YouTube script in a friendly, natural tutor tone for approximately 10 minutes.

**Branding:**
- Channel name: "Just Watch Math"
- Tone: Friendly and encouraging teacher
- Style: Conversational, explains while asking questions

**Structure:**
1. Opening (30 seconds)
   - Greeting and channel intro
   - Preview of today's topic

2. THE BIG IDEA (2 minutes)
   - Core concept explanation
   - Why this matters

3. Common Trap Warning (1 minute)
   - Frequently made mistakes
   - How to avoid them

4. Quick Tip (1 minute)
   - Useful tips for problem-solving
   - Time-saving methods for exams

5. Example Problem Walkthrough (4 minutes)
   - Walk through 2-3 examples step by step
   - Pace slowly so students can follow along

6. Review & Closing (1.5 minutes)
   - Summary of key points
   - Recommend practice problems
   - Preview of next video

**Requirements:**
- Include timing markers [00:30], [02:00], etc.
- Natural transition phrases
- Include visual cue hints (e.g., "[show formula on screen]")
- Ask students questions (engagement prompts)
```

### Expected Output Structure:

```
[Script] Chapter Title.pdf

=== Just Watch Math - [Chapter Title] ===

[00:00 - 00:30] Opening
Before we start, you can download a free PDF with today's
problems and solutions using the link below.
Don't panic, just watch. Just Watch Math.

Hi everyone, this is Just Watch Math.
Today we're diving into [topic].
This concept is crucial for [importance],
and in just 10 minutes you'll have a solid understanding!

[00:30 - 02:30] THE BIG IDEA
Let's get started!
[Core concept explanation...]
[show diagram on screen]

Does that make sense?
The key idea here is [...]

[02:30 - 03:30] Common Trap
Hold on a second!
A lot of students make a mistake here...
[Common mistake explanation]

If you do it this way, you'll get it wrong!
Instead, [correct approach]...

[03:30 - 04:30] Quick Tip
Here's a useful tip for you!
[Tip explanation...]

Using this method will save you a lot of time on exams.

[04:30 - 08:30] Examples
Now let's work through some actual problems!

Example 1: [Problem description]
Step 1: ...
Step 2: ...
[Detailed solution]

Example 2: [Problem description]
This one's a bit trickier...
[Detailed solution]

[08:30 - 10:00] Review & Closing
Let's recap what we learned today.
1. [Key point 1]
2. [Key point 2]
3. [Key point 3]

To really master this concept,
make sure to work through the practice problems in the [Problems] document!

Next time we'll cover [next topic].
Hit subscribe and like,
and let's conquer math together with Just Watch Math!

=== End of Script ===
```

---

## Formatting Guidelines

### Visual Elements

**Color Coding:**
- Navy (#003366): Core concepts, THE BIG IDEA
- Red (#CC0000): Warnings, Common Traps, Errors
- Orange (#FF8800): Tips, Useful Information
- Green (#00AA00): Success, Correct Answers
- Gray (#666666): Notes, Side information

**Typography:**
- **Bold**: Answers, key terms, emphasis
- *Italic*: Variables, book references
- `Monospace`: Code, specific notation
- Regular: Body text, explanations

**Layout:**
- Wide margins (at least 1 inch on all sides)
- Clear section headers with hierarchy (H1 > H2 > H3)
- Adequate spacing between problems/concepts
- Tables with alternating row colors for readability

### Mathematical Notation

- Use LaTeX-style notation where applicable
- Ensure all symbols are clearly rendered
- Number important equations
- Align multi-line equations properly
- Use proper fraction formatting

### Page Count Targets

| Output Type | Target Pages | Priority |
|-------------|--------------|----------|
| Notes | 8-11 pages | High |
| Problems | 4-6 pages | Medium |
| Quick Answers | 1 page | High |
| Explanations | 2-3 pages | Medium |
| Script | 6 pages | Medium |

### Quality Validation

Before finalizing each output, verify:
- [ ] All mathematical notation is correct
- [ ] Text is properly encoded (UTF-8)
- [ ] Visual elements (boxes, colors) are present
- [ ] Page count is within target range
- [ ] File size > 100KB (not corrupted)
- [ ] Content matches prompt requirements

---

## Usage Notes for Agents

1. **Always load the specific prompt** for your output type from this file
2. **Generate all content in English**
3. **Reference the expected output structure** when generating content
4. **Apply formatting guidelines** consistently across all outputs
5. **Validate against quality checklist** before returning path to orchestrator

---

## Version History

- v1.0.0 (2026-02-13): Initial prompt library with 5 output types
