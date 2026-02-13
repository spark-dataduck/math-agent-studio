# Output Format Specifications

This document defines the detailed formatting requirements for all 5 output types.

---

## General Requirements

### File Specifications
- **Format**: PDF (Adobe PDF 1.4 or higher)
- **Encoding**: UTF-8 (for Korean text support)
- **Page Size**: US Letter (8.5" × 11")
- **Orientation**: Portrait
- **Minimum File Size**: 100 KB (to detect generation errors)

### Typography
- **Body Font**: Times New Roman or similar serif (10-12pt)
- **Heading Font**: Arial or Helvetica (14-18pt bold)
- **Math Font**: Computer Modern or STIX (for LaTeX-like rendering)
- **Code Font**: Courier New or Monaco (10pt)

### Margins
- Top: 1.0 inch
- Bottom: 1.0 inch
- Left: 1.0 inch
- Right: 1.0 inch

---

## 1. Notes Format

### Visual Design
```
┌─────────────────────────────────────────┐
│ [Navy Box - THE BIG IDEA]              │
│ Core concept overview                   │
│ Why this matters                        │
└─────────────────────────────────────────┘

Concept Title
─────────────
Definition: [Table with 2 columns]
┌──────────┬──────────────────────────┐
│ Term     │ Definition               │
├──────────┼──────────────────────────┤
│ ...      │ ...                      │
└──────────┴──────────────────────────┘

Visual Mnemonic: 🎯
[Metaphor or analogy]

┌─────────────────────────────────────────┐
│ [Red Box - Common Trap ⚠️]             │
│ Students often confuse...               │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ [Orange Box - Useful Tip 💡]           │
│ Quick way to remember...               │
└─────────────────────────────────────────┘

Try These:
1. [Easy example]
2. [Medium example]
3. [Application example]
```

### Content Structure
1. **Title Page** (optional, if space permits)
2. **THE BIG IDEA** (mandatory first section)
3. **Concepts** (2-4 major concepts)
   - Each with definition, examples, Try These
4. **Advanced Topics** (1-2 sections)
5. **Review Section** (summary tables)
6. **Quick Reference** (formula sheet)

### Color Palette
- Navy: #003366 (RGB: 0, 51, 102)
- Red: #CC0000 (RGB: 204, 0, 0)
- Orange: #FF8800 (RGB: 255, 136, 0)
- Green: #00AA00 (RGB: 0, 170, 0)
- Light Gray: #F5F5F5 (RGB: 245, 245, 245) - for box backgrounds

---

## 2. Problems Format

### Visual Design
```
Section A: Standard Problems (표준 문제)
════════════════════════════════════════

Problem 1. [Brief description if needed]

  [Problem statement with adequate whitespace]

  (a) [Multi-part question]
  (b) [Multi-part question]

  [Space for student work - 2-3 inches]

─────────────────────────────────────────

Problem 2. ...
```

### Content Structure
- **Section A** (Problems 1-6): Standard exam questions
  - Progressive difficulty: Easy (1-2), Medium (3-4), Hard (5-6)
  - Mix of computational and conceptual
- **Section B** (Problems 7-10): Competition-style
  - Putnam-level difficulty
  - Requires creative thinking
  - May involve proofs

### Formatting Rules
- Clear problem numbers (bold, larger font)
- Adequate spacing between problems (at least 1 inch)
- Horizontal dividers between problems
- Space for student work (don't crowd)
- Diagrams/figures where needed

---

## 3. Quick Answers Format

### Visual Design
```
Quick Answer Key
[Chapter Title]
═════════════════════════════════════════

┌─────────┬─────────────────────────────┐
│ Problem │ Answer                      │
╞═════════╪═════════════════════════════╡
│ 1(a)    │ x = 5                       │
│ 1(b)    │ y = -2                      │
├─────────┼─────────────────────────────┤
│ 2       │ True (see proof)            │
├─────────┼─────────────────────────────┤
│ 3       │ n = 12                      │
├─────────┼─────────────────────────────┤
│ ...     │ ...                         │
└─────────┴─────────────────────────────┘

Note: For detailed solutions, see [Explanations] document.
```

### Content Structure
- **Header**: Title and chapter name
- **Table**: 2-column format (Problem | Answer)
- **Footer**: Reference to explanations document

### Formatting Rules
- **Must fit on 1 page** (critical requirement)
- Alternating row colors (white/light gray)
- Bold problem numbers
- Concise answers (no explanations)
- Multi-part answers on separate rows (1a, 1b, etc.)
- For proofs: "See detailed solution" or "Proof required"

---

## 4. Explanations Format

### Visual Design
```
Detailed Solutions
[Chapter Title]
═════════════════════════════════════════

Problem 1.
Answer: (a) x = 5, (b) y = -2

Solution:
(a) Given: [restate given information]

    Step 1: Apply [concept/theorem name]
            [Mathematical work]

    Step 2: Simplify
            [Show work]

    Step 3: Verify
            [Check answer]

    Therefore, x = 5. ✓

(b) [Similar structure]

┌─────────────────────────────────────────┐
│ Common Mistake ⚠️                       │
│ Students often forget to...             │
└─────────────────────────────────────────┘

Alternative Method:
[Different approach to same problem]
[Show that it yields same answer]

Key Insight:
This problem tests [concept]. The critical
step is recognizing [pattern/strategy].

─────────────────────────────────────────
```

### Content Structure
- Each problem gets its own section
- Answer stated upfront (bold)
- Step-by-step solution with justifications
- Common mistakes highlighted (red box)
- Alternative methods when applicable
- Key insights/takeaways

### Formatting Rules
- Clear problem headers (bold, larger font)
- Numbered steps for clarity
- Mathematical work properly aligned
- Boxes for warnings/tips
- Adequate spacing between problems
- Horizontal dividers

---

## 5. Script Format

### Visual Design
```
═════════════════════════════════════════
    Just Watch Math
    [Chapter Title]
    10-Minute Educational Video Script
═════════════════════════════════════════

[00:00 - 00:30] Opening
─────────────────────────────────────────
[Dialogue in natural Korean]

[화면 지시: Show channel logo]

─────────────────────────────────────────

[00:30 - 02:30] THE BIG IDEA
─────────────────────────────────────────
[Dialogue explaining core concept]

[화면 지시: Display diagram of...]

[Stop for question: "여러분 이해되시나요?"]

─────────────────────────────────────────
```

### Content Structure
1. **Opening** (30 seconds)
   - Greeting
   - Topic introduction
   - Preview
2. **THE BIG IDEA** (2 minutes)
   - Core concept explanation
3. **Common Trap** (1 minute)
   - Warning about mistakes
4. **Quick Tip** (1 minute)
   - Helpful strategy
5. **Examples** (4 minutes)
   - 2-3 worked problems
6. **Review & Closing** (1.5 minutes)
   - Summary
   - Next steps
   - Call to action

### Formatting Rules
- **Timing markers** at every section [MM:SS]
- **Screen directions** in brackets [화면 지시: ...]
- **Natural dialogue** (conversational, not formal)
- **Pauses for engagement** [Stop for question]
- **Visual cues** for transitions
- **Clear section dividers**

### Timing Budget
| Section | Time | Cumulative |
|---------|------|------------|
| Opening | 0:30 | 0:30 |
| Big Idea | 2:00 | 2:30 |
| Common Trap | 1:00 | 3:30 |
| Quick Tip | 1:00 | 4:30 |
| Examples | 4:00 | 8:30 |
| Review/Closing | 1:30 | 10:00 |

---

## Validation Checklist

### For All Outputs
- [ ] File is valid PDF format
- [ ] File size > 100 KB
- [ ] UTF-8 encoding for Korean text
- [ ] All mathematical notation renders correctly
- [ ] Margins are consistent (1 inch all sides)
- [ ] Page numbers present (except Quick Answers)

### Output-Specific
**Notes:**
- [ ] 8-11 pages
- [ ] THE BIG IDEA box present
- [ ] At least 2 colored boxes (trap/tip)
- [ ] Try These examples included

**Problems:**
- [ ] Exactly 10 problems
- [ ] Section A (1-6) and Section B (7-10) clearly marked
- [ ] Adequate space between problems

**Quick Answers:**
- [ ] Fits on 1 page
- [ ] All 10 answers present
- [ ] Table format used
- [ ] Multi-part answers on separate rows

**Explanations:**
- [ ] All 10 problems explained
- [ ] Step-by-step solutions
- [ ] At least 1 alternative method shown
- [ ] Common mistakes highlighted

**Script:**
- [ ] Timing markers throughout
- [ ] Total time ≈ 10 minutes
- [ ] Natural, conversational Korean
- [ ] Screen directions included

---

## Error Handling

### Common Issues

**Issue**: Korean text displays as garbage characters
**Solution**: Ensure UTF-8 encoding, use proper Korean fonts

**Issue**: Mathematical symbols don't render
**Solution**: Use LaTeX rendering or Unicode math symbols

**Issue**: PDF file is too small (<100KB)
**Solution**: Content likely didn't generate properly, retry

**Issue**: Layout is cramped/cluttered
**Solution**: Increase spacing, use better page breaks

**Issue**: Colors don't show in boxes
**Solution**: Use RGB color values, check PDF viewer settings

---

## References

- Adobe PDF Specification 1.4: https://www.adobe.com/devnet/pdf/
- Korean Typography Best Practices: [internal reference]
- LaTeX Math Symbols: https://www.ctan.org/
- WCAG Color Contrast Guidelines: https://www.w3.org/WAI/WCAG21/
