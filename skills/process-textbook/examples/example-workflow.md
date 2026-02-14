# Example Workflow Execution

This document shows a complete example of processing a textbook chapter from start to finish.

## Input

**Source PDF:**
```
reference_source/1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
```

**Chapter:** 1.1 Deductive Reasoning and Logical Connectives
**Textbook:** How To Prove It by Daniel J. Velleman
**File Size:** 439.8 KB

## Invocation

### Command Line
```bash
/process-textbook "reference_source/1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf"
```

### Natural Language
```
"Process the math textbook at reference_source/1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf"
```

## Execution Flow

### Step 1: Validation

```
🔍 Validating PDF...

✅ PDF validated successfully
   Path: reference_source/1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Size: 439.8 KB (450,352 bytes)
   Chapter: 1.1 Deductive Reasoning and Logical Connectives
```

### Step 2: User Confirmation

```
┌─────────────────────────────────────────────────────┐
│  Math Textbook Processing                           │
├─────────────────────────────────────────────────────┤
│  Source PDF: 1.1 Deductive Reasoning and Logical    │
│              Connectives [How To Prove It].pdf      │
│  Chapter: 1.1 Deductive Reasoning and Logical       │
│           Connectives                               │
│                                                     │
│  Will generate 5 outputs:                           │
│    1. [Notes] - Comprehensive study notes           │
│    2. [Script] - YouTube video script               │
│    3. [Problems] - 10 practice problems             │
│    4. [Quick Answers] - Answer key                  │
│    5. [Explanations] - Detailed solutions           │
│                                                     │
│  Output directory: reference_outputs/               │
│  Estimated time: 15-25 minutes                      │
└─────────────────────────────────────────────────────┘

Proceed with processing? [Yes/No]
```

**User Response:** Yes

### Step 3: Workflow Initialization

```
📝 Creating workflow state...
✅ State file created: .claude/workflow-textbook-processing.local.md

🚀 Starting workflow orchestration...
```

### Step 4: Sequential Execution

#### Step 1: Notes Generation

```
┌─────────────────────────────────────────────────────┐
│ Step 1/5: Generating Comprehensive Notes            │
│ Status: In Progress...                              │
│ Agent: notes-generator (opus model)                 │
│ Time elapsed: 0m 00s                                │
└─────────────────────────────────────────────────────┘

🔄 Reading source PDF...
🔄 Loading prompt template...
🔄 Analyzing content structure...
🔄 Generating THE BIG IDEA section...
🔄 Creating definition tables...
🔄 Adding visual mnemonics...
🔄 Inserting "Try These" examples...
🔄 Formatting PDF output...
🔄 Writing to reference_outputs/[Notes] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf...

✅ Step 1 complete! (5m 23s)
   Output: [Notes] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Size: 1.2 MB
   Pages: 9
```

#### Step 2d: Script Generation

```
┌─────────────────────────────────────────────────────┐
│ Step 2/5: Generating YouTube Script                 │
│ Status: In Progress...                              │
│ Agent: script-generator                             │
│ Time elapsed: 0m 00s                                │
└─────────────────────────────────────────────────────┘

🔄 Reading notes from Step 1...
🔄 Loading prompt template...
🔄 Creating script structure...
🔄 Writing opening (30s)...
🔄 Writing BIG IDEA section (2min)...
🔄 Adding Common Trap warning (1min)...
🔄 Adding Quick Tip (1min)...
🔄 Writing example walkthroughs (4min)...
🔄 Writing review & closing (1.5min)...
🔄 Formatting with timing markers...

✅ Step 2 complete! (3m 15s)
   Output: [Script] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Size: 523 KB
   Pages: 6
   Estimated duration: 10:15
```

#### Step 3: Problems Generation

```
┌─────────────────────────────────────────────────────┐
│ Step 3/5: Generating Practice Problems              │
│ Status: In Progress...                              │
│ Agent: problems-generator                           │
│ Time elapsed: 0m 00s                                │
└─────────────────────────────────────────────────────┘

🔄 Reading source PDF and notes...
🔄 Loading prompt template...
🔄 Generating Section A problems (1-6)...
   Problem 1: Basic truth tables (⭐ easy)
   Problem 2: Logical equivalences (⭐⭐ easy-medium)
   Problem 3: Compound statements (⭐⭐⭐ medium)
   Problem 4: Conditional reasoning (⭐⭐⭐ medium)
   Problem 5: Multi-step proof (⭐⭐⭐⭐ medium-hard)
   Problem 6: Complex application (⭐⭐⭐⭐⭐ hard)
🔄 Generating Section B problems (7-10)...
   Problem 7: Putnam-style (🏆 creative)
   Problem 8: Proof required (🏆🏆 rigorous)
   Problem 9: Multiple approaches (🏆🏆🏆 strategic)
   Problem 10: Most challenging (🏆🏆🏆🏆 advanced)
🔄 Formatting with adequate spacing...

✅ Step 3 complete! (4m 08s)
   Output: [Problems] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Size: 387 KB
   Pages: 5
   Problem count: 10
```

#### Step 4: Quick Answers Generation

```
┌─────────────────────────────────────────────────────┐
│ Step 4/5: Generating Quick Answer Key               │
│ Status: In Progress...                              │
│ Agent: answers-generator                            │
│ Time elapsed: 0m 00s                                │
└─────────────────────────────────────────────────────┘

🔄 Reading problems from Step 3...
🔄 Loading prompt template...
🔄 Solving all 10 problems...
🔄 Creating compact table format...
🔄 Ensuring fits on 1 page...
🔄 Adding references to [Explanations]...

✅ Step 4 complete! (1m 42s)
   Output: [Quick Answers] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Size: 156 KB
   Pages: 1
   Answer count: 10
```

#### Step 5: Explanations Generation

```
┌─────────────────────────────────────────────────────┐
│ Step 5/5: Generating Detailed Explanations          │
│ Status: In Progress...                              │
│ Agent: explanations-generator                       │
│ Time elapsed: 0m 00s                                │
└─────────────────────────────────────────────────────┘

🔄 Reading problems from Step 3...
🔄 Loading prompt template...
🔄 Writing step-by-step solutions...
   Problem 1: Direct application (2 methods)
   Problem 2: Logical equivalence (2 methods)
   Problem 3: Compound statements (case analysis)
   Problem 4: Conditional reasoning (truth table + direct proof)
   Problem 5: Multi-step (detailed breakdown)
   Problem 6: Complex (strategic approach)
   Problem 7: Putnam-style (creative insight)
   Problem 8: Proof (rigorous derivation)
   Problem 9: Multiple approaches (3 methods compared)
   Problem 10: Most challenging (advanced techniques)
🔄 Adding Common Mistake warnings...
🔄 Adding Key Insight sections...
🔄 Formatting with clear sections...

✅ Step 5 complete! (3m 56s)
   Output: [Explanations] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Size: 445 KB
   Pages: 3
```

### Step 5: Completion Summary

```
═══════════════════════════════════════════════════════
            ✅ Processing Complete!
═══════════════════════════════════════════════════════

Chapter: 1.1 Deductive Reasoning and Logical Connectives
Total Time: 18m 24s
Output Location: reference_outputs/

Generated Files:
─────────────────────────────────────────────────────

1. 📄 [Notes] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Comprehensive study notes
   Size: 1.2 MB | Pages: 9
   Path: reference_outputs/[Notes] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf

2. 🎬 [Script] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   10-minute YouTube script
   Size: 523 KB | Pages: 6
   Path: reference_outputs/[Script] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf

3. 📝 [Problems] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   10 practice problems (6 standard + 4 competition)
   Size: 387 KB | Pages: 5
   Path: reference_outputs/[Problems] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf

4. ✅ [Quick Answers] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Quick answer key
   Size: 156 KB | Pages: 1
   Path: reference_outputs/[Quick Answers] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf

5. 📖 [Explanations] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
   Detailed step-by-step solutions
   Size: 445 KB | Pages: 3
   Path: reference_outputs/[Explanations] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf

═══════════════════════════════════════════════════════

Next Steps:
• Study the [Notes] to learn key concepts
• Test yourself with [Problems]
• Check your work with [Quick Answers]
• Review [Explanations] for detailed solutions
• Use [Script] to create educational video content

Tip: All files are ready to use immediately!
═══════════════════════════════════════════════════════
```

## Output Files

All 5 files are generated in `reference_outputs/`:

```
reference_outputs/
├── [Notes] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
├── [Script] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
├── [Problems] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
├── [Quick Answers] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
└── [Explanations] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
```

## State File

During execution, state is tracked in:
```
.claude/workflow-textbook-processing.local.md
```

Final state:
```markdown
# Textbook Processing Workflow State

**Status**: COMPLETED
**PDF Path**: reference_source/1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
**Chapter Name**: 1.1 Deductive Reasoning and Logical Connectives
**Started**: 2026-02-13 14:30:00
**Completed**: 2026-02-13 14:48:24
**Total Duration**: 18m 24s

## Step Completion Status
- [x] Step 1: Notes (Completed @ 14:35:23) - 5m 23s
- [x] Step 2d: Script (Completed @ 14:38:38) - 3m 15s
- [x] Step 2a: Problems (Completed @ 14:42:46) - 4m 08s
- [x] Step 2b: Quick Answers (Completed @ 14:44:28) - 1m 42s
- [x] Step 2c: Explanations (Completed @ 14:48:24) - 3m 56s

## Artifacts Generated
- reference_outputs/[Notes] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf (1.2 MB)
- reference_outputs/[Script] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf (523 KB)
- reference_outputs/[Problems] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf (387 KB)
- reference_outputs/[Quick Answers] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf (156 KB)
- reference_outputs/[Explanations] 1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf (445 KB)

## Error Log
(Empty - no errors)

## Notes
Workflow completed successfully. All 5 outputs generated.
```

## Performance Metrics

| Metric | Value |
|--------|-------|
| Total Time | 18m 24s |
| Total Output Size | 2.7 MB |
| Total Pages | 24 pages |
| Success Rate | 100% (5/5 outputs) |
| Retries | 0 |

## Next Steps

After processing, the user can:

1. **Study** - Read the [Notes] to learn concepts
2. **Practice** - Solve the [Problems]
3. **Check** - Use [Quick Answers] to verify
4. **Learn** - Study [Explanations] for mistakes
5. **Create** - Use [Script] to make educational videos

All files are ready to use immediately!
