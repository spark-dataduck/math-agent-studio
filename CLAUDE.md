# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Math Agent Studio** is a Claude Code plugin that transforms math textbook chapter PDFs into 5 comprehensive study materials: Notes, Problems, Quick Answers, Explanations, and YouTube Scripts. All outputs are in English with rich visual formatting (colored boxes, tables, LaTeX).

**Target Use Case**: Students studying from math textbooks (e.g., "How To Prove It") who want comprehensive, exam-ready materials plus YouTube scripts for educational content.

## Commands & Testing

### Running the Plugin

```bash
# Test the full workflow with example PDF
/process-textbook "reference_source/1.1 Deductive Reasoning [How To Prove It].pdf"

# Or just describe the task
"Process this math textbook: reference_source/1.1 Deductive Reasoning [How To Prove It].pdf"
```

### Validation Scripts

```bash
# Validate a PDF file exists and is readable
python3 scripts/validate_pdf.py "path/to/file.pdf"

# Generate standardized output path
python3 scripts/generate_output_path.py "Notes" "reference_source/chapter.pdf"
```

**Important**: `validate_pdf.py` and `generate_output_path.py` use only standard library. `generate_pdf.py` requires **Playwright** (auto-installed on first run via `pip install playwright && playwright install chromium`).

## Architecture & Workflow

### Component Hierarchy

```
/process-textbook skill (entry point)
    ↓
workflow-orchestrator agent (coordinator)
    ↓ (sequential execution)
    ├─ Step 1: notes-generator
    ├─ Step 2d: script-generator (depends on notes)
    ├─ Step 2a: problems-generator (depends on notes)
    ├─ Step 2b: answers-generator (depends on problems)
    └─ Step 2c: explanations-generator (depends on problems)
```

### Critical Design Decision: Sequential Execution

**Why not parallel?** The workflow executes generators **sequentially**, not in parallel:
- More reliable (easier debugging, clearer progress)
- Avoids API rate limiting
- Predictable resource usage
- Allows proper dependency management

Even though Step 2d and Step 2a only depend on Step 1, they still run sequentially. This is intentional.

### State Persistence

Workflow state is saved in `.claude/workflow-textbook-processing.local.md` (git-ignored via `*.local.md` pattern).

**State File Format**:
```markdown
# Textbook Processing Workflow State

**Status**: IN_PROGRESS | COMPLETED | ERROR
**PDF Path**: /full/path/to/source.pdf
**Chapter Name**: 1.1 Deductive Reasoning
**Started**: 2026-02-13 14:30:00
**Last Updated**: 2026-02-13 14:35:23

## Step Completion Status
- [x] Step 1: Notes (Completed @ 14:35:23)
- [ ] Step 2d: Script (Pending)
...

## Artifacts Generated
- `/path/to/[Notes] chapter.pdf` (1.2 MB)
```

**Resumption**: If interrupted (Ctrl+C, error), re-run `/process-textbook` to resume from the last completed step.

### Dependencies Between Steps

```
notes-generator (Step 1)
    ├─> script-generator (uses notes as reference)
    └─> problems-generator (uses source PDF + notes)
            ├─> answers-generator (extracts answers from problems)
            └─> explanations-generator (writes solutions for problems)
```

**Key Insight**:
- Steps 2b and 2c depend on Step 2a (problems must exist before answers/explanations)
- Step 2d depends on Step 1 (script uses notes for content)
- Step 2a depends on Step 1 (problems based on notes concepts)

## Reference Materials

All reference materials are in `skills/process-textbook/references/`:

1. **prompts.md** - AI prompts for all 5 output types
   - Contains detailed instructions for content generation
   - Defines tone, structure, and formatting requirements
   - **Critical for output quality** - edit here to change content style

2. **output-formats.md** - Visual formatting specifications
   - Color schemes (blue for definitions, purple for examples, etc.)
   - Page layouts and typography
   - Box styles and table formats

3. **workflow-states.md** - State machine documentation
   - Valid states: INITIALIZED, VALIDATED, IN_PROGRESS, COMPLETED, ERROR
   - Transition rules and error recovery

## File Naming Convention

All outputs follow this pattern:
```
[Output Type] [Chapter Name] [Source Book].pdf
```

Examples:
```
[Notes] 1.1 Deductive Reasoning [How To Prove It].pdf
[Problems] 1.1 Deductive Reasoning [How To Prove It].pdf
[Quick Answers] 1.1 Deductive Reasoning [How To Prove It].pdf
[Explanations] 1.1 Deductive Reasoning [How To Prove It].pdf
[Script] 1.1 Deductive Reasoning [How To Prove It].pdf
```

**Location**: All outputs go to `outputs/` directory.

## Generator Agents

Each generator agent is a specialized Task that:
1. Reads input files (source PDF, previous outputs)
2. Applies prompt from `prompts.md`
3. Generates formatted PDF output
4. Returns output path to orchestrator

**Agent Files**:
- `agents/notes-generator.md` - Comprehensive notes (8-11 pages: HTML→Playwright PDF pipeline with KaTeX math, `notes-base.css`)
- `agents/script-generator.md` - 10-minute YouTube script (HTML→Playwright pipeline, `content-base.css`, English only)
- `agents/problems-generator.md` - 10 problems (HTML→Playwright pipeline, `content-base.css`, 4-6 pages)
- `agents/answers-generator.md` - Compact answer key (HTML→Playwright pipeline, `content-base.css`, 1-page table)
- `agents/explanations-generator.md` - Step-by-step solutions (HTML→Playwright pipeline, `content-base.css`, 2-3 pages)

**Important**: Agents do NOT communicate with each other directly. All coordination happens through the workflow-orchestrator.

## Error Handling

### Retry Logic

Each step has 3 retry attempts with exponential backoff:
- Attempt 1: Immediate
- Attempt 2: 5 seconds delay
- Attempt 3: 10 seconds delay
- After 3 failures: Mark as ERROR, offer manual retry

### Common Failures

1. **PDF Not Found**: Caught during validation (before workflow starts)
2. **API Timeout**: Automatically retried up to 3 times
3. **Invalid Output** (corrupted PDF, <100KB): Regenerated automatically
4. **Disk Full**: Cannot auto-retry, user must free space
5. **User Interruption** (Ctrl+C): State saved, resumable on next invocation

## Plugin Configuration

### plugin.json (metadata only)

`.claude-plugin/plugin.json` contains **only metadata**: name, version, description, author, repository, keywords.

**Skills and agents are NOT declared in plugin.json** - they are auto-discovered from the `skills/` and `agents/` directories.

**Common plugin.json mistakes** (will cause install validation errors):
- `repository` must be a plain string URL, NOT an object like `{"type": "git", "url": "..."}`
- Do NOT include `skills` or `agents` arrays
- Do NOT include a `claudeCode` key (unrecognized)

### marketplace.json (for distribution)

`.claude-plugin/marketplace.json` is required for marketplace distribution (when users install via `/plugin` → Add Marketplace).

**Schema** (based on official Notion plugin pattern):
```json
{
  "name": "kebab-case-marketplace-name",
  "owner": { "name": "Owner Name" },
  "plugins": [
    {
      "name": "plugin-name",
      "description": "...",
      "source": { "source": "github", "repo": "owner/repo" }
    }
  ]
}
```

**Key rules**:
- `name` must be kebab-case (no spaces)
- `owner` is required (object with `name`)
- Each plugin needs a `source` object with `"source": "github"` and `"repo": "owner/repo"`
- `$schema` field is optional (the URL returns 404 anyway)

**Reference examples**:
- Notion plugin: `~/.claude/plugins/cache/claude-plugins-official/Notion/0.1.0/`
- Anthropic official: `https://github.com/anthropics/claude-code/blob/main/.claude-plugin/marketplace.json`

**Repository**: This plugin is published under `spark-dataduck` org (not `sundoopark` personal account).

## Development Workflow

### Adding a New Output Type

To add a 6th output (e.g., flashcards):

1. Create prompt in `skills/process-textbook/references/prompts.md`
2. Create agent file: `agents/flashcards-generator.md` (auto-discovered, no registration needed)
3. Update `workflow-orchestrator.md` to include new step
4. Update `SKILL.md` execution order
5. Update README.md to document new output

### Modifying Output Content

**To change what gets generated** (e.g., longer scripts, different problem types):
- Edit `skills/process-textbook/references/prompts.md` (prompts)
- Edit specific agent file (e.g., `agents/script-generator.md`)

**To change visual formatting** (e.g., colors, layouts):
- Edit `skills/process-textbook/references/output-formats.md`

### Testing Changes

Always test with the reference example:
```bash
/process-textbook "reference_source/1.1 Deductive Reasoning [How To Prove It].pdf"
```

Compare outputs with existing files in `reference_outputs/` to verify quality.

## Performance Characteristics

**Typical Execution Times** (per step):
- Step 1 (Notes): 3-8 minutes (longest, most content)
- Step 2d (Script): 2-4 minutes
- Step 2a (Problems): 3-5 minutes
- Step 2b (Answers): 1-2 minutes (shortest, extraction only)
- Step 2c (Explanations): 3-5 minutes
- **Total**: 15-25 minutes per chapter

**File Sizes**:
- Notes: 200-600 KB (8-11 pages, HTML→Playwright pipeline)
- Script: 400-600 KB (6 pages)
- Problems: 300-500 KB (4-6 pages)
- Quick Answers: 150-200 KB (1 page)
- Explanations: 400-600 KB (2-3 pages)
- **Total**: ~3-4 MB per chapter

## Important Conventions

### Language

- All prompts and generated content are in English
- UTF-8 encoding throughout
- Math notation uses LaTeX (language-agnostic)

### Git Ignore Patterns

```gitignore
*.local.md          # Workflow state files (session-specific)
__pycache__/        # Python cache
.DS_Store          # macOS metadata
.idea/             # JetBrains IDE
```

### Output Validation

Before marking a step complete, verify:
1. File exists
2. File size > 100 KB
3. File is valid PDF (using `file` command)

### State Transitions

```
(start) → INITIALIZED → VALIDATED → IN_PROGRESS → COMPLETED
                                   ↓
                                 ERROR (with retry options)
```

## Working with This Codebase

### Key Files to Understand

**Start here**:
1. `README.md` - User-facing documentation
2. `skills/process-textbook/SKILL.md` - Entry point logic
3. `agents/workflow-orchestrator.md` - Core workflow coordination

**Deep dive**:
4. `skills/process-textbook/references/prompts.md` - Prompts (critical for output quality)
5. Individual agent files in `agents/` - Understand each output type

**Utilities**:
6. `scripts/validate_pdf.py` - PDF validation
7. `scripts/generate_output_path.py` - Path generation
8. `scripts/generate_pdf.py` - HTML→PDF via Playwright (with KaTeX math rendering)

### Making Changes Safely

1. **Never break resumption**: State file format changes must be backward-compatible
2. **Maintain sequential execution**: Don't parallelize without considering rate limits
3. **Preserve prompts carefully**: Content generation depends on exact prompt phrasing
4. **Test with reference PDF**: Always verify against example before committing

### Reading Agent Files

Agent `.md` files are Claude Code agent definitions with:
- **Frontmatter** (YAML): Name, description, model, tools, color
- **Markdown body**: Execution instructions, logic, prompts

These are NOT regular markdown docs - they're executable agent definitions.

## Plugin Structure

```
math-agent-studio/
├── .claude-plugin/
│   ├── plugin.json           # Plugin metadata (name, version, author)
│   └── marketplace.json      # Marketplace distribution config
├── skills/
│   └── process-textbook/
│       ├── SKILL.md          # Entry point (user-invocable)
│       ├── assets/
│       │   ├── notes-base.css    # CSS classes for notes HTML
│       │   ├── content-base.css  # CSS classes for problems/answers/explanations/script
│       │   └── katex/            # Bundled KaTeX (CSS + JS + fonts)
│       └── references/
│           ├── prompts.md    # AI prompts ⭐
│           ├── output-formats.md
│           └── workflow-states.md
├── agents/
│   ├── workflow-orchestrator.md  # Coordinator ⭐
│   ├── notes-generator.md
│   ├── script-generator.md
│   ├── problems-generator.md
│   ├── answers-generator.md
│   └── explanations-generator.md
├── scripts/
│   ├── validate_pdf.py       # Validation utility
│   ├── generate_output_path.py
│   └── generate_pdf.py       # HTML→PDF via Playwright
├── reference_source/         # Example input PDFs
├── reference_outputs/        # Example output PDFs (for testing)
└── outputs/                  # Generated output PDFs (runtime)
```

⭐ = Most frequently modified files

## Troubleshooting

**"Workflow stuck on a step"**
- Check state file: `.claude/workflow-textbook-processing.local.md`
- If no updates for >10 minutes, likely hung
- Safe to Ctrl+C and resume

**"Text displays as garbage"**
- PDF viewer doesn't support UTF-8
- Try different viewer (Preview on macOS, Adobe Reader)

**"Output quality is poor"**
- Edit prompts in `prompts.md`
- Regenerate by restarting workflow (archive old state first)

**"Can't resume workflow"**
- State file might be corrupted
- Archive: `mv .claude/workflow-textbook-processing.local.md .claude/backup-$(date +%s).md`
- Start fresh workflow

## Version Information

- **Current Version**: 1.0.0
- **Last Updated**: 2026-02-17
- **Claude Code Minimum**: 2.1.0
- **Python Requirement**: 3.9+
