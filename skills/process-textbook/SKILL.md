---
name: process-textbook
description: Process a math textbook chapter PDF into 5 comprehensive study materials (Notes, Problems, Quick Answers, Explanations, Script). Invoke with "process this math textbook" or "/process-textbook [path]".
trigger_phrases:
  - "process math textbook"
  - "convert math pdf"
  - "generate study materials"
  - "process textbook chapter"
version: 1.0.0
allowed-tools:
  - Read
  - Write(reference_outputs/**)
  - Write(/tmp/generate_*)
  - Bash(python3 scripts/*)
  - Bash(python3 /tmp/generate_*)
  - Bash(pip install reportlab)
  - Bash(pip3 install reportlab)
  - Bash(stat *)
  - Bash(file *)
  - Bash(wc *)
  - Bash(mkdir *)
  - Bash(ls *)
---

# Process Math Textbook Skill

Transform a math textbook chapter PDF into 5 comprehensive study materials:
1. **[Notes]** - Comprehensive study notes (8-11 pages)
2. **[Problems]** - 10 practice problems (6 standard + 4 competition)
3. **[Quick Answers]** - Concise answer key (1 page)
4. **[Explanations]** - Detailed step-by-step solutions (2-3 pages)
5. **[Script]** - 10-minute YouTube educational video script (6 pages)

## Usage

```bash
/process-textbook [path-to-pdf]
```

**Example:**
```bash
/process-textbook "reference_source/1.1 Deductive Reasoning [How To Prove It].pdf"
```

**Or simply say:**
- "Process this math textbook" (will prompt for path)
- "Convert the PDF at [path] to study materials"
- "Generate study materials from [path]"

## How It Works

This skill orchestrates 5 specialized AI agents in sequence:
1. **notes-generator** → Creates comprehensive notes
2. **script-generator** → Creates YouTube script (depends on notes)
3. **problems-generator** → Creates practice problems (depends on notes)
4. **answers-generator** → Creates answer key (depends on problems)
5. **explanations-generator** → Creates detailed solutions (depends on problems)

Typical execution time: **15-25 minutes** for a full chapter.

## Execution Instructions

When invoked, follow this workflow:

### Phase 1: Input Validation & State Check

```markdown
1. Check for PDF path
   - If provided in invocation: Use it
   - If in conversation context: Extract it
   - If neither: Prompt user for path

2. Check for existing workflow state
   - Look for: .claude/workflow-textbook-processing.local.md
   - If exists: Load state and check status
   - If not: This is a fresh start

3. Handle existing workflow state
   - If COMPLETED: Inform user, offer to restart
   - If ERROR: Show error, offer retry options
   - If IN_PROGRESS: Offer to resume from last step
   - If none: Continue to validation
```

### Phase 2: PDF Validation

```markdown
1. Validate PDF path format
   - Must be absolute or relative path
   - Must end in .pdf extension

2. Validate PDF exists and is readable
   Bash: python3 scripts/validate_pdf.py "$pdf_path"

   If validation fails:
   - Display error message
   - Re-prompt user for correct path
   - Do NOT proceed to orchestration

3. Parse chapter name from filename
   Example:
     Input: "1.1 Deductive Reasoning [How To Prove It].pdf"
     Parsed: "1.1 Deductive Reasoning"

   Remove file extension (.pdf)
   Keep everything up to (and including) first bracket [...]
```

### Phase 3: User Confirmation

```markdown
Display summary and confirm:

┌─────────────────────────────────────────────────────┐
│  Math Textbook Processing                           │
├─────────────────────────────────────────────────────┤
│  Source PDF: [filename]                             │
│  Chapter: [parsed chapter name]                     │
│  Location: [full path]                              │
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

If No: Exit gracefully
If Yes: Continue to initialization
```

### Phase 4: Workflow Initialization

```markdown
1. Create or update state file
   Location: .claude/workflow-textbook-processing.local.md

   Initial state:
   ```
   # Textbook Processing Workflow State

   **Status**: INITIALIZED
   **PDF Path**: [full path]
   **Chapter Name**: [parsed name]
   **Started**: [timestamp]
   **Last Updated**: [timestamp]

   ## Step Completion Status
   - [ ] Step 1: Notes (Pending)
   - [ ] Step 2d: Script (Pending)
   - [ ] Step 2a: Problems (Pending)
   - [ ] Step 2b: Quick Answers (Pending)
   - [ ] Step 2c: Explanations (Pending)

   ## Artifacts Generated
   (None yet)

   ## Current Step Details
   **Step**: None
   **Status**: Awaiting orchestration start

   ## Error Log
   (Empty)

   ## Notes
   Workflow initialized successfully.
   ```

2. Update state to VALIDATED
   After PDF validation passes, mark status as VALIDATED

3. Prepare to invoke orchestrator
```

### Phase 5: Orchestration

```markdown
1. Invoke workflow-orchestrator agent
   Task: workflow-orchestrator
   Inputs:
     - pdf_path: [validated PDF path]
     - chapter_name: [parsed chapter name]
     - resume: false (for fresh start) or true (for resumption)

2. Display progress messages
   The orchestrator will execute 5 steps sequentially.

   Show user-friendly progress:

   🔄 Starting workflow...

   ┌─────────────────────────────────────────────────────┐
   │ Step 1/5: Generating comprehensive notes            │
   │ Status: In Progress...                              │
   │ Time elapsed: 2m 30s                                │
   └─────────────────────────────────────────────────────┘

   ✅ Step 1 complete! (5m 23s)
      Output: [Notes] chapter-name.pdf (1.2 MB)

   🔄 Step 2/5: Generating YouTube script...
   ✅ Step 2 complete! (3m 15s)

   🔄 Step 3/5: Generating practice problems...
   ✅ Step 3 complete! (4m 08s)

   🔄 Step 4/5: Generating answer key...
   ✅ Step 4 complete! (1m 42s)

   🔄 Step 5/5: Generating detailed explanations...
   ✅ Step 5 complete! (3m 56s)

3. Handle interruptions
   If user presses Ctrl+C or process is interrupted:
   - State is already saved by orchestrator
   - Inform user: "Workflow paused. Run /process-textbook again to resume."
   - Exit gracefully

4. Handle errors
   If orchestrator returns error:
   - Display error details
   - Show which step failed
   - Offer options:
     A. Retry failed step
     B. Restart from beginning
     C. Skip failed step (if non-critical)
     D. Cancel workflow
```

### Phase 6: Completion & Summary

```markdown
1. Verify all outputs generated
   Check that all 5 files exist in reference_outputs/

2. Update final state
   Mark workflow status as COMPLETED in .local.md

3. Display completion summary

   ═══════════════════════════════════════════════════════
                ✅ Processing Complete!
   ═══════════════════════════════════════════════════════

   Chapter: [Chapter Name]
   Total Time: [duration]
   Output Location: reference_outputs/

   Generated Files:
   ─────────────────────────────────────────────────────

   1. 📄 [Notes] [chapter].pdf
      Comprehensive study notes
      Size: 1.2 MB | Pages: 9
      Path: reference_outputs/[Notes] [chapter].pdf

   2. 🎬 [Script] [chapter].pdf
      10-minute YouTube script
      Size: 523 KB | Pages: 6
      Path: reference_outputs/[Script] [chapter].pdf

   3. 📝 [Problems] [chapter].pdf
      10 practice problems (6 standard + 4 competition)
      Size: 387 KB | Pages: 5
      Path: reference_outputs/[Problems] [chapter].pdf

   4. ✅ [Quick Answers] [chapter].pdf
      Quick answer key
      Size: 156 KB | Pages: 1
      Path: reference_outputs/[Quick Answers] [chapter].pdf

   5. 📖 [Explanations] [chapter].pdf
      Detailed step-by-step solutions
      Size: 445 KB | Pages: 3
      Path: reference_outputs/[Explanations] [chapter].pdf

   ═══════════════════════════════════════════════════════

   Next Steps:
   • Study the [Notes] to learn key concepts
   • Test yourself with [Problems]
   • Check your work with [Quick Answers]
   • Review [Explanations] for detailed solutions
   • Use [Script] to create educational video content

   Tip: All files are ready to use immediately!
   ═══════════════════════════════════════════════════════

4. Archive state file (optional)
   Move .local.md to .completed.[timestamp].md
   Or keep for reference
```

## Resumption Logic

When user runs `/process-textbook` and an incomplete workflow exists:

```markdown
1. Detect existing workflow state
   Read: .claude/workflow-textbook-processing.local.md

2. Determine workflow status
   - INITIALIZED/VALIDATED: Ask if user wants to continue
   - IN_PROGRESS: Offer to resume from last completed step
   - ERROR: Show error and offer retry
   - COMPLETED: Inform user and offer restart

3. Display resumption prompt

   ┌─────────────────────────────────────────────────────┐
   │  Found Incomplete Workflow                          │
   ├─────────────────────────────────────────────────────┤
   │  Chapter: [Chapter Name]                            │
   │  Started: [timestamp]                               │
   │                                                     │
   │  Progress:                                          │
   │    ✅ Step 1: Notes (Completed)                     │
   │    ✅ Step 2: Script (Completed)                    │
   │    ✅ Step 3: Problems (Completed)                  │
   │    ⏸️  Step 4: Quick Answers (Paused)               │
   │    ⏳ Step 5: Explanations (Pending)                │
   │                                                     │
   │  Options:                                           │
   │    A. Resume from Step 4 (Quick Answers)            │
   │    B. Restart from beginning                        │
   │    C. Cancel and keep current progress              │
   └─────────────────────────────────────────────────────┘

   What would you like to do? [A/B/C]

4. Handle user choice
   A: Resume → Invoke orchestrator with resume=true
   B: Restart → Archive old state, start fresh
   C: Cancel → Exit, keep state file
```

## Error Handling

### Common Errors & Solutions

**Error: PDF Not Found**
```
❌ Error: PDF file not found

The file path you provided doesn't exist:
  [provided path]

Please check:
  • Is the path correct?
  • Does the file exist at this location?
  • Do you have permission to read it?

Try again with: /process-textbook [correct-path]
```

**Error: Invalid PDF**
```
❌ Error: Invalid PDF file

The file exists but is not a valid PDF:
  [provided path]
  File type: [detected type]

Please provide a valid PDF file.
```

**Error: Workflow Step Failed**
```
❌ Error: Step [N] failed

Step: [Step Name]
Reason: [Error message]
Attempts: 3/3 (max retries exceeded)

The workflow has been paused.

Options:
  A. Retry Step [N] only
  B. Restart entire workflow
  C. View error details
  D. Cancel and exit

What would you like to do? [A/B/C/D]
```

**Error: Disk Space**
```
❌ Error: Insufficient disk space

Unable to write output file. Free up disk space and try again.

Current disk usage: [percentage]%
Estimated space needed: ~5 MB

After freeing space, run: /process-textbook
(Your progress has been saved and can be resumed)
```

## State File Management

### State File Location
```
.claude/workflow-textbook-processing.local.md
```

This file is:
- Created when workflow starts
- Updated after each step completion
- Preserved on interruption
- Archived on completion (optional)
- Git-ignored (*.local.md pattern)

### Reading State
```bash
# Check if state exists
if [ -f ".claude/workflow-textbook-processing.local.md" ]; then
    # Load state
    STATE_CONTENT=$(cat .claude/workflow-textbook-processing.local.md)
    # Parse status, steps, etc.
fi
```

Use Read tool to load state content.

### Writing State
Use Write tool to update state file with new content.

### Archiving State
On completion, optionally move to completed archive:
```bash
mv .claude/workflow-textbook-processing.local.md \
   .claude/workflow-textbook-processing.completed.$(date +%Y%m%d_%H%M%S).md
```

## Integration with Other Tools

### Utility Scripts

**PDF Validation:**
```bash
python3 scripts/validate_pdf.py "$pdf_path"
# Exit code 0 = success, 1 = failure
```

**Output Path Generation:**
```bash
output_path=$(python3 scripts/generate_output_path.py "Notes" "$pdf_path")
# Prints standardized output path
```

### Agent Invocation

Invoke the workflow orchestrator using Task tool:
```markdown
Task: workflow-orchestrator
Description: Orchestrate generation of 5 study materials
Inputs:
  - pdf_path: [validated path]
  - chapter_name: [parsed name]
  - resume: [true/false]
```

## Performance Expectations

### Timing
- **Step 1 (Notes)**: 3-8 minutes (longest step)
- **Step 2 (Script)**: 2-4 minutes
- **Step 3 (Problems)**: 3-5 minutes
- **Step 4 (Answers)**: 1-2 minutes
- **Step 5 (Explanations)**: 3-5 minutes
- **Total**: 15-25 minutes typical

### File Sizes
- **[Notes]**: 1-2 MB (8-11 pages)
- **[Script]**: 400-600 KB (6 pages)
- **[Problems]**: 300-500 KB (4-6 pages)
- **[Quick Answers]**: 150-200 KB (1 page)
- **[Explanations]**: 400-600 KB (2-3 pages)
- **Total**: ~3-4 MB for all outputs

## Best Practices

1. **Always validate PDF first**
   - Check file exists before starting workflow
   - Saves time if path is wrong

2. **Inform user of time commitment**
   - Let them know it takes 15-25 minutes
   - They can interrupt and resume later

3. **Save progress frequently**
   - State is updated after each step
   - No work is lost on interruption

4. **Provide clear error messages**
   - Don't just say "error occurred"
   - Explain what went wrong and how to fix

5. **Make resumption easy**
   - Auto-detect incomplete workflows
   - Offer clear resume options

6. **Display progress clearly**
   - Show which step is running
   - Show elapsed time
   - Show completed vs remaining

7. **Verify outputs exist**
   - Before marking complete, check all files
   - Validate file sizes are reasonable

## Troubleshooting

### Workflow is stuck
- Check if orchestrator agent is still running
- Look at state file for last update time
- If no progress for >10 minutes, might be hung

### Output quality is poor
- Text not rendering: Check UTF-8 encoding
- Math notation broken: Check LaTeX rendering
- Missing sections: Regenerate that step

### Can't resume workflow
- State file might be corrupted
- Try starting fresh workflow
- Archive old state file first

## Files Created by This Skill

During execution, this skill creates/updates:
- `.claude/workflow-textbook-processing.local.md` (state file)
- `reference_outputs/[Notes] [chapter].pdf`
- `reference_outputs/[Script] [chapter].pdf`
- `reference_outputs/[Problems] [chapter].pdf`
- `reference_outputs/[Quick Answers] [chapter].pdf`
- `reference_outputs/[Explanations] [chapter].pdf`

All output files are placed in the `reference_outputs/` directory
parallel to the source PDF's `reference_source/` directory.

## Dependencies

This skill requires:
- Python 3.9+ (for utility scripts)
- Claude Code 2.1+ (for plugin runtime)
- Workflow orchestrator agent
- 5 generator agents (notes, script, problems, answers, explanations)

## Notes

- All AI prompts are specified in prompts.md
- Output PDFs are UTF-8 encoded
- Visual formatting (colored boxes, tables) is essential
- Sequential execution is more reliable than parallel
- State file enables resumption from any interruption
- Each run processes exactly ONE chapter
- To process multiple chapters, run the skill multiple times

## Version History

- v1.0.0 (2026-02-13): Initial release with 5-output workflow
