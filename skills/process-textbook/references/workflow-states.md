# Workflow State Management

This document describes the state machine for the textbook processing workflow.

---

## State File Location

Workflow state is persisted in:
```
.claude/workflow-textbook-processing.local.md
```

**Note**: This file is gitignored (`.local.md` pattern) to prevent committing workflow state to version control.

---

## State Machine Diagram

```
                START
                  │
                  ▼
            INITIALIZED ──────────────┐
                  │                   │
                  │ (validate PDF)    │ (error)
                  ▼                   │
              VALIDATED               │
                  │                   │
                  │ (begin)           │
                  ▼                   ▼
            IN_PROGRESS ──────────▶ ERROR
                  │   ▲               │
                  │   │               │
                  │   │ (retry)       │
                  │   └───────────────┘
                  │
                  │ (all steps done)
                  ▼
             COMPLETED
```

---

## State Definitions

### INITIALIZED
**Description**: Workflow created, PDF path recorded, not yet validated.

**Transitions:**
- → VALIDATED: PDF validation successful
- → ERROR: PDF validation failed

**Actions:**
- Record PDF path
- Record chapter name (parsed from filename)
- Set timestamp

### VALIDATED
**Description**: PDF exists and is valid, ready to start processing.

**Transitions:**
- → IN_PROGRESS: User confirms to start workflow
- → ERROR: User cancels or unexpected error

**Actions:**
- Mark all steps as PENDING
- Prepare output directory

### IN_PROGRESS
**Description**: Workflow is actively processing steps.

**Transitions:**
- → COMPLETED: All 5 steps completed successfully
- → ERROR: Unrecoverable error encountered
- → IN_PROGRESS: (stays in this state while processing)

**Actions:**
- Execute steps sequentially
- Update step status as each completes
- Save state after each step
- Track output paths

**Sub-states:**
```
IN_PROGRESS
  ├─ Step 1: PENDING → IN_PROGRESS → COMPLETED
  ├─ Step 2d: PENDING → IN_PROGRESS → COMPLETED
  ├─ Step 2a: PENDING → IN_PROGRESS → COMPLETED
  ├─ Step 2b: PENDING → IN_PROGRESS → COMPLETED
  └─ Step 2c: PENDING → IN_PROGRESS → COMPLETED
```

### COMPLETED
**Description**: All 5 outputs generated successfully.

**Transitions:**
- (Terminal state - no transitions)

**Actions:**
- Display final summary
- List all output paths
- Mark workflow complete in state file

### ERROR
**Description**: Workflow encountered an error and cannot proceed.

**Transitions:**
- → IN_PROGRESS: User chooses to retry from last successful step
- → INITIALIZED: User chooses to restart from beginning
- (Can also stay in ERROR if user abandons)

**Actions:**
- Record error details
- Save error timestamp
- Determine which step failed
- Offer retry options

---

## State File Format

### Template
```markdown
# Textbook Processing Workflow State

**Status**: [INITIALIZED|VALIDATED|IN_PROGRESS|COMPLETED|ERROR]
**PDF Path**: /absolute/path/to/source.pdf
**Chapter Name**: [Extracted from filename]
**Started**: YYYY-MM-DD HH:MM:SS
**Last Updated**: YYYY-MM-DD HH:MM:SS

## Step Completion Status
- [x] Step 1: Notes (Completed @ HH:MM:SS)
- [x] Step 2d: Script (Completed @ HH:MM:SS)
- [x] Step 2a: Problems (Completed @ HH:MM:SS)
- [ ] Step 2b: Quick Answers (In Progress)
- [ ] Step 2c: Explanations (Pending)

## Artifacts Generated
- `/full/path/to/[Notes] chapter-name.pdf` (439 KB)
- `/full/path/to/[Script] chapter-name.pdf` (312 KB)
- `/full/path/to/[Problems] chapter-name.pdf` (255 KB)

## Current Step Details
**Step**: 2b (Quick Answers)
**Status**: IN_PROGRESS
**Started**: YYYY-MM-DD HH:MM:SS
**Attempts**: 1 of 3

## Error Log
(Empty if no errors)

## Notes
User interrupted workflow with Ctrl+C after Step 2a.
Resuming from Step 2b.
```

### Example: Fresh Start
```markdown
# Textbook Processing Workflow State

**Status**: INITIALIZED
**PDF Path**: /Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_source/1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf
**Chapter Name**: 1.1 Dedeuctive Reasoning and Logical Connectives
**Started**: 2026-02-13 14:30:00
**Last Updated**: 2026-02-13 14:30:00

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
**Status**: Awaiting user confirmation to begin

## Error Log
(Empty)

## Notes
Workflow initialized. PDF validation successful (439.8 KB).
Waiting for user to confirm chapter name.
```

### Example: Mid-Workflow Interruption
```markdown
# Textbook Processing Workflow State

**Status**: IN_PROGRESS
**PDF Path**: /Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_source/1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf
**Chapter Name**: 1.1 Dedeuctive Reasoning and Logical Connectives
**Started**: 2026-02-13 14:30:00
**Last Updated**: 2026-02-13 14:45:23

## Step Completion Status
- [x] Step 1: Notes (Completed @ 14:38:12)
- [x] Step 2d: Script (Completed @ 14:42:45)
- [x] Step 2a: Problems (Completed @ 14:45:23)
- [ ] Step 2b: Quick Answers (Pending)
- [ ] Step 2c: Explanations (Pending)

## Artifacts Generated
- `/Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_outputs/[Notes] 1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf` (1.2 MB)
- `/Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_outputs/[Script] 1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf` (523 KB)
- `/Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_outputs/[Problems] 1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf` (387 KB)

## Current Step Details
**Step**: 2a (Problems)
**Status**: COMPLETED
**Started**: 2026-02-13 14:43:30
**Completed**: 2026-02-13 14:45:23
**Duration**: 1m 53s

## Error Log
(Empty)

## Notes
User interrupted workflow after Step 2a completed.
Ready to resume from Step 2b when restarted.
```

### Example: Error State
```markdown
# Textbook Processing Workflow State

**Status**: ERROR
**PDF Path**: /Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_source/1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf
**Chapter Name**: 1.1 Dedeuctive Reasoning and Logical Connectives
**Started**: 2026-02-13 14:30:00
**Last Updated**: 2026-02-13 14:52:10

## Step Completion Status
- [x] Step 1: Notes (Completed @ 14:38:12)
- [x] Step 2d: Script (Completed @ 14:42:45)
- [x] Step 2a: Problems (Completed @ 14:45:23)
- [x] Step 2b: Quick Answers (Completed @ 14:48:30)
- [!] Step 2c: Explanations (ERROR @ 14:52:10)

## Artifacts Generated
- `/Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_outputs/[Notes] 1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf` (1.2 MB)
- `/Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_outputs/[Script] 1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf` (523 KB)
- `/Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_outputs/[Problems] 1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf` (387 KB)
- `/Users/sundoopark/Documents/personal_projects/math-agent-studio/reference_outputs/[Quick Answers] 1.1 Dedeuctive Reasoning and Logical Connectives [How To Prove It].pdf` (156 KB)

## Current Step Details
**Step**: 2c (Explanations)
**Status**: ERROR
**Started**: 2026-02-13 14:49:00
**Failed**: 2026-02-13 14:52:10
**Attempts**: 3 of 3 (max retries reached)

## Error Log
[2026-02-13 14:49:45] Attempt 1 failed: API timeout after 120s
[2026-02-13 14:50:30] Attempt 2 failed: API timeout after 120s
[2026-02-13 14:52:10] Attempt 3 failed: API timeout after 120s
ERROR: Max retry attempts (3) exceeded for Step 2c.

## Notes
Repeated API timeouts suggest network issue or overloaded service.
User can retry Step 2c specifically, or check API status.
All other steps completed successfully.
```

---

## State Transitions in Detail

### 1. Fresh Start Flow

```
User: /process-textbook path/to/chapter.pdf

SKILL:
  1. Check if .local.md exists
     - No: Create new workflow state (INITIALIZED)
     - Yes: Load existing state, offer resume

  2. Validate PDF
     - scripts/validate_pdf.py
     - Success: → VALIDATED
     - Failure: → ERROR, re-prompt user

  3. Parse chapter name from filename
     - "1.1 Deductive Reasoning [Book].pdf"
     - → Chapter: "1.1 Deductive Reasoning"

  4. Confirm with user
     - "Process chapter '1.1 Deductive Reasoning'?"
     - Yes: → IN_PROGRESS
     - No: → Stay in VALIDATED, await new input

  5. Invoke workflow-orchestrator agent
```

### 2. Resume Flow

```
User: /process-textbook

SKILL:
  1. Check .local.md exists
     - Yes: Load state
     - No: Prompt for PDF path

  2. Determine current state
     - COMPLETED: Inform user, offer restart
     - ERROR: Show error, offer retry options
     - IN_PROGRESS: Offer resume from last step

  3. If resuming IN_PROGRESS:
     - Find last completed step
     - Determine next pending step
     - Confirm with user: "Resume from Step 2b?"

  4. Invoke workflow-orchestrator with resume flag
```

### 3. Error Recovery Flow

```
State: ERROR (Step 2c failed)

SKILL:
  1. Display error summary
     - Which step failed
     - How many attempts made
     - Error messages

  2. Offer options:
     A. Retry Step 2c only (keeps previous outputs)
     B. Restart from Step 1 (regenerate all)
     C. Skip Step 2c (continue without)
     D. Cancel workflow

  3. Based on user choice:
     A: → IN_PROGRESS (resume at 2c)
     B: → INITIALIZED (reset state)
     C: → COMPLETED (mark as done, but incomplete)
     D: Keep ERROR state
```

---

## Step Dependencies

```
Step 1 (Notes)
  └─ BLOCKS ──→ Step 2d (Script) ─────┐
  └─ BLOCKS ──→ Step 2a (Problems) ───┼─→ All must complete
                  └─ BLOCKS ──→ Step 2b (Quick Answers) ──┤
                  └─ BLOCKS ──→ Step 2c (Explanations) ───┘
```

**Dependency Rules:**
1. Step 1 must complete before any Step 2 can start
2. Step 2d can run in parallel with 2a (both depend only on Step 1)
3. Steps 2b and 2c both depend on 2a completing
4. Steps 2b and 2c can run sequentially after 2a

**Execution Order (Sequential for Reliability):**
```
1 → 2d → 2a → 2b → 2c
```

---

## State Management Functions

### Create State
```python
def create_state(pdf_path: str, chapter_name: str) -> dict:
    return {
        "status": "INITIALIZED",
        "pdf_path": pdf_path,
        "chapter_name": chapter_name,
        "started": datetime.now(),
        "last_updated": datetime.now(),
        "steps": {
            "1": {"name": "Notes", "status": "PENDING"},
            "2d": {"name": "Script", "status": "PENDING"},
            "2a": {"name": "Problems", "status": "PENDING"},
            "2b": {"name": "Quick Answers", "status": "PENDING"},
            "2c": {"name": "Explanations", "status": "PENDING"}
        },
        "artifacts": [],
        "errors": []
    }
```

### Update Step Status
```python
def update_step(state: dict, step_id: str, status: str, output_path: str = None):
    state["steps"][step_id]["status"] = status
    state["last_updated"] = datetime.now()

    if status == "COMPLETED" and output_path:
        state["artifacts"].append({
            "step": step_id,
            "path": output_path,
            "size": os.path.getsize(output_path),
            "completed": datetime.now()
        })

    save_state(state)
```

### Check Completion
```python
def is_workflow_complete(state: dict) -> bool:
    required_steps = ["1", "2d", "2a", "2b", "2c"]
    return all(
        state["steps"][step]["status"] == "COMPLETED"
        for step in required_steps
    )
```

---

## Recovery Scenarios

### Scenario 1: User Interrupts (Ctrl+C)
**When**: User cancels mid-workflow
**State**: IN_PROGRESS (partial completion)
**Recovery**: Resume from next pending step
**Data Loss**: None (completed steps saved)

### Scenario 2: API Timeout
**When**: AI generation takes too long
**State**: IN_PROGRESS (step marked ERROR)
**Recovery**: Retry same step (up to 3 attempts)
**Data Loss**: None (retry same step)

### Scenario 3: Disk Full
**When**: No space to write PDF
**State**: ERROR (cannot write output)
**Recovery**: User frees disk space, retry
**Data Loss**: Current step output

### Scenario 4: Invalid PDF Generated
**When**: Generated PDF < 100KB or corrupted
**State**: IN_PROGRESS (validation failed)
**Recovery**: Retry step with same inputs
**Data Loss**: None (regenerate)

### Scenario 5: Process Crash
**When**: Unexpected termination
**State**: IN_PROGRESS (may be stale)
**Recovery**: Detect stale state on restart, offer resume
**Data Loss**: Current step if not saved

---

## Best Practices

1. **Save state after every step completion**
   - Minimize data loss
   - Enable fine-grained resume

2. **Validate outputs before marking complete**
   - Check file exists
   - Check file size > 100KB
   - Verify PDF can be opened

3. **Record timestamps for debugging**
   - Start time, end time, duration
   - Helps identify slow steps

4. **Keep detailed error logs**
   - Include full error messages
   - Record retry attempts
   - Note user actions

5. **Offer clear recovery options**
   - Don't just say "error occurred"
   - Present specific choices
   - Explain consequences of each

---

## File Operations

### Read State
```bash
# Check if state file exists
if [ -f ".claude/workflow-textbook-processing.local.md" ]; then
    # Load and parse state
    STATE=$(cat .claude/workflow-textbook-processing.local.md)
fi
```

### Write State
```bash
# Save state (atomic write for safety)
cat > .claude/workflow-textbook-processing.local.md.tmp << 'EOF'
[state content]
EOF
mv .claude/workflow-textbook-processing.local.md.tmp .claude/workflow-textbook-processing.local.md
```

### Clear State (after completion)
```bash
# Archive completed workflow state
mv .claude/workflow-textbook-processing.local.md \
   .claude/workflow-textbook-processing.completed.$(date +%Y%m%d_%H%M%S).md
```

---

## Version History

- v1.0.0 (2026-02-13): Initial state machine design with sequential execution
