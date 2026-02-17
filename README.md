# Math Agent Studio

Transform math textbook chapter PDFs into comprehensive study materials with AI. One command generates 5 educational outputs: notes, problems, answers, explanations, and YouTube scripts.

## 🎯 What It Does

Input: A math textbook chapter PDF (e.g., "1.1 Deductive Reasoning.pdf")

Output: 5 comprehensive study materials in **~15-25 minutes**:

1. **[Notes]** - Comprehensive study notes (8-11 pages)
   - THE BIG IDEA sections with core concepts
   - Visual mnemonics and metaphors
   - Definition tables and examples
   - Common traps and useful tips
   - "Try These" practice problems

2. **[Problems]** - 10 practice problems (4-6 pages)
   - Section A: 6 standard exam problems
   - Section B: 4 competition-level problems (Putnam-style)
   - Progressive difficulty (easy → hard)

3. **[Quick Answers]** - Answer key (1 page)
   - Compact table format
   - Quick reference for answer checking
   - References detailed solutions

4. **[Explanations]** - Detailed solutions (2-3 pages)
   - Step-by-step solutions for all 10 problems
   - Multiple solution approaches
   - Common mistakes highlighted
   - Key insights and strategies

5. **[Script]** - YouTube video script (6 pages)
   - 10-minute educational video script
   - "Just Watch Math" channel style
   - Natural, conversational tone
   - Timing markers and screen directions

## 🚀 Quick Start

### Installation

1. **Prerequisites**
   - [Claude Code](https://claude.ai/code) 2.1 or higher
   - Python 3.9+

2. **Install Plugin**
   ```bash
   cd ~/.claude/plugins
   git clone https://github.com/sundoopark/math-agent-studio.git
   ```

3. **Verify Installation**
   ```bash
   # Start Claude Code
   claude

   # Check if skill is available
   /help
   # You should see "process-textbook" in the skills list
   ```

### First Run

```bash
# Process a chapter
/process-textbook "path/to/your/chapter.pdf"

# Or just ask
"Process this math textbook: path/to/chapter.pdf"
```

**Example:**
```bash
/process-textbook "reference_source/1.1 Deductive Reasoning [How To Prove It].pdf"
```

## 📖 Usage

### Basic Usage

```bash
/process-textbook <path-to-pdf>
```

### Interactive Usage

Just describe what you want:
```
"Process the PDF at reference_source/1.1 Deductive Reasoning.pdf"
"Convert this math chapter to study materials"
"Generate notes and problems from the textbook"
```

Claude Code will automatically invoke the skill.

### Resuming Interrupted Workflows

If you interrupt the process (Ctrl+C) or it fails:

```bash
# Run the skill again
/process-textbook

# You'll see:
Found Incomplete Workflow
Progress:
  ✅ Step 1: Notes (Completed)
  ✅ Step 2: Script (Completed)
  ⏸️  Step 3: Problems (Paused)
  ⏳ Step 4: Quick Answers (Pending)
  ⏳ Step 5: Explanations (Pending)

Options:
  A. Resume from Step 3
  B. Restart from beginning
  C. Cancel
```

The skill automatically saves progress and can resume from any step.

## 🏗️ Architecture

### 3-Tier Architecture

**Math Agent Studio** uses a 3-tier architecture that separates concerns:

1. **Skill** = User-facing API (entry point, validation, UX)
2. **Orchestrator Agent** = Workflow coordinator (state management, sequencing)
3. **Generator Agents** = Content creators (specialized workers)

This separation allows the skill to focus on user experience while agents focus on execution logic.

### Complete Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│ SKILL: process-textbook                                 │
│ (User-facing entry point)                               │
│                                                         │
│ Responsibilities:                                       │
│ • Parse user input (/process-textbook [path])          │
│ • Validate PDF exists and is readable                  │
│ • Handle user confirmations                            │
│ • Display progress messages to user                    │
│ • Handle resumption logic                              │
│ • Show final summary                                   │
└─────────────────────────────────────────────────────────┘
                           │
                           │ invokes via Task tool
                           ▼
┌─────────────────────────────────────────────────────────┐
│ AGENT: workflow-orchestrator                            │
│ (Workflow coordinator - "the foreman")                  │
│                                                         │
│ Responsibilities:                                       │
│ • Manage workflow state (.local.md)                    │
│ • Execute 5 steps sequentially                         │
│ • Handle errors and retries                            │
│ • Validate outputs between steps                       │
│ • Track dependencies (Step 2b needs Step 2a done)      │
└─────────────────────────────────────────────────────────┘
                           │
                           │ spawns via Task tool
                           ▼
┌─────────────────────────────────────────────────────────┐
│ AGENTS: 5 Generator Agents                              │
│ (Content creators - "the workers")                      │
│                                                         │
│ ├─ notes-generator                                     │
│ ├─ script-generator                                    │
│ ├─ problems-generator                                  │
│ ├─ answers-generator                                   │
│ └─ explanations-generator                              │
│                                                         │
│ Responsibilities:                                       │
│ • Read input files (source PDF, previous outputs)      │
│ • Apply prompt templates                               │
│ • Generate formatted PDF output                        │
│ • Validate output quality                              │
│ • Return output path to orchestrator                   │
└─────────────────────────────────────────────────────────┘
```

### Skill vs Agent: Key Differences

| Aspect | Skill | Agent |
|--------|-------|-------|
| **Invoked by** | User (via `/process-textbook`) | Another agent (via Task tool) or skill |
| **Has access to user** | Yes - can prompt user for input | No - receives inputs from invoker |
| **Purpose** | User experience & validation | Execution logic |
| **Tools** | Not explicitly defined (inherits context) | Explicitly defined in YAML frontmatter |
| **Location** | `skills/process-textbook/SKILL.md` | `agents/*.md` |
| **Can spawn agents?** | Yes (can use Task tool) | Only orchestrator can (others don't have Task tool) |
| **Registered in** | `.claude-plugin/plugin.json` → `skills` | `.claude-plugin/plugin.json` → `agents` |

### Component Overview (Legacy View)

```
User → SKILL (entry point)
         ↓
    Workflow Orchestrator
         ↓
    Sequential Execution:
         ↓
    [1] notes-generator ────┐
         ↓                  │
    [2d] script-generator   │ (depends on notes)
         ↓                  │
    [2a] problems-generator │ (depends on notes)
         ↓                  │
    [2b] answers-generator  │ (depends on problems)
         ↓                  │
    [2c] explanations-gen   │ (depends on problems)
         ↓                  │
    5 PDF Files Generated ──┘
```

### Directory Structure

```
math-agent-studio/
├── .claude-plugin/
│   ├── plugin.json              # Plugin metadata
│   └── marketplace.json         # Marketplace distribution config
│
├── skills/
│   └── process-textbook/
│       ├── SKILL.md             # User-facing entry point
│       ├── assets/
│       │   ├── notes-base.css   # CSS for notes (full-page title, pastel boxes)
│       │   ├── content-base.css # CSS for problems/answers/explanations/script
│       │   └── katex/           # Bundled KaTeX (CSS + JS + fonts)
│       └── references/
│           ├── prompts.md       # AI prompts (5 types)
│           ├── output-formats.md # Format specifications
│           └── workflow-states.md # State machine docs
│
├── agents/
│   ├── workflow-orchestrator.md # Workflow manager
│   ├── notes-generator.md       # Step 1: Notes
│   ├── script-generator.md      # Step 2d: YouTube script
│   ├── problems-generator.md    # Step 2a: Problems
│   ├── answers-generator.md     # Step 2b: Answer key
│   └── explanations-generator.md # Step 2c: Solutions
│
├── scripts/
│   ├── validate_pdf.py          # PDF validation
│   ├── generate_output_path.py  # Filename generator
│   └── generate_pdf.py          # HTML→PDF via Playwright (KaTeX math)
│
├── reference_source/            # Example input PDFs
├── reference_outputs/           # Example output PDFs
│
└── README.md                    # This file
```

## 🔧 Configuration

### AI Prompts

All AI prompts are located in:
```
skills/process-textbook/references/prompts.md
```

To modify how content is generated, edit the prompts in that file.

### Output Format Customization

Visual formatting specifications (colors, layouts, page counts) are in:
```
skills/process-textbook/references/output-formats.md
```

### Agent Behavior

Each agent's behavior can be customized by editing its `.md` file in `agents/`.

For example, to change the script length from 10 minutes to 15 minutes:
```markdown
# Edit agents/script-generator.md
# Change timing budget from 10:00 to 15:00
```

## 🎓 Example Output

See the `reference_outputs/` directory for example outputs generated from:
```
reference_source/1.1 Deductive Reasoning and Logical Connectives [How To Prove It].pdf
```

Example files:
- `[Notes] 1.1 Deductive Reasoning...pdf` - Study notes with visual formatting
- `[Problems] 1.1 Deductive Reasoning...pdf` - 10 practice problems
- `[Quick Answers] 1.1 Deductive Reasoning...pdf` - Answer key
- `[Explanations] 1.1 Deductive Reasoning...pdf` - Detailed solutions
- `[Script] 1.1 Deductive Reasoning...pdf` - YouTube script

## 🔍 How It Works

### Workflow Execution

1. **Skill Invocation** (`/process-textbook`)
   - Validates PDF path
   - Parses chapter name
   - Checks for existing workflow state
   - Confirms with user

2. **Workflow Orchestrator**
   - Creates workflow state file (`.local.md`)
   - Executes 5 agents sequentially
   - Updates state after each step
   - Handles errors and retries

3. **Generator Agents** (HTML→Playwright PDF pipeline)
   - Each agent reads relevant inputs
   - Generates structured HTML with embedded CSS and KaTeX math
   - Converts to PDF via Playwright/Chromium (`scripts/generate_pdf.py`)
   - Validates output quality (file size, page count)
   - Returns path to orchestrator

4. **Completion**
   - Validates all 5 outputs exist
   - Displays final summary
   - Marks workflow as complete

### State Management

The workflow state is persisted in:
```
.claude/workflow-textbook-processing.local.md
```

This enables:
- **Resumption** after interruption (Ctrl+C)
- **Error recovery** with retry logic
- **Progress tracking** across sessions

The state file is git-ignored (`.local.md` pattern).

## 📊 Performance

### Typical Execution Times

| Step | Output | Time |
|------|--------|------|
| 1 | Notes | 3-8 min |
| 2d | Script | 2-4 min |
| 2a | Problems | 3-5 min |
| 2b | Quick Answers | 1-2 min |
| 2c | Explanations | 3-5 min |
| **Total** | **All 5** | **15-25 min** |

### File Sizes

| Output | Size | Pages |
|--------|------|-------|
| Notes | 1-2 MB | 8-11 |
| Script | 400-600 KB | 6 |
| Problems | 300-500 KB | 4-6 |
| Quick Answers | 150-200 KB | 1 |
| Explanations | 400-600 KB | 2-3 |
| **Total** | **~3-4 MB** | **~20-25** |

## 🛠️ Troubleshooting

### Common Issues

**"PDF not found" error**
```
Problem: File path doesn't exist or is incorrect
Solution: Check the path and ensure the file exists
```

**Text displays as garbage**
```
Problem: Encoding issue
Solution: Ensure PDF viewer supports UTF-8
```

**Workflow stuck on a step**
```
Problem: API timeout or network issue
Solution: Wait for retry (automatic, max 3 attempts)
         or Ctrl+C and resume later
```

**Output quality is poor**
```
Problem: AI prompt not optimal for this content
Solution: Edit prompts in references/prompts.md
         and regenerate that output
```

**Can't resume workflow**
```
Problem: State file corrupted or missing
Solution: Start fresh workflow (old progress is lost)
         Archive old state file if it exists
```

### Getting Help

1. Check the skill documentation: `skills/process-textbook/SKILL.md`
2. Review agent docs: `agents/[agent-name].md`
3. Check example outputs: `reference_outputs/`
4. File an issue: https://github.com/sundoopark/math-agent-studio/issues

## 🧪 Development

### Running Tests

```bash
# Test PDF validation
python3 scripts/validate_pdf.py "reference_source/1.1 Deductive Reasoning [How To Prove It].pdf"

# Test output path generation
python3 scripts/generate_output_path.py "Notes" "reference_source/test.pdf"

# Test full workflow with example PDF
/process-textbook "reference_source/1.1 Deductive Reasoning [How To Prove It].pdf"
```

### Adding New Output Types

To add a new output type (e.g., flashcards):

1. Create prompt in `skills/process-textbook/references/prompts.md`
2. Create agent file: `agents/flashcards-generator.md` (auto-discovered)
3. Add CSS classes to `skills/process-textbook/assets/content-base.css`
4. Add mode preset to `scripts/generate_pdf.py`
5. Update orchestrator to include new step
6. Update SKILL.md to document new output

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with example PDFs
5. Submit a pull request

Guidelines:
- Follow existing agent structure
- Add prompts to `prompts.md`
- Document new features in README
- Include example outputs

## 📋 Requirements

### System Requirements

- **OS**: macOS, Linux, or Windows with WSL
- **Python**: 3.9 or higher
- **Claude Code**: 2.1 or higher
- **Disk Space**: 50 MB for plugin + ~5 MB per chapter processed

### Python Packages

- **Playwright** - PDF generation via headless Chromium (auto-installed on first run)
- Standard library only for utility scripts (`validate_pdf.py`, `generate_output_path.py`)

### Claude Code Permissions

The skill requests these permissions:
- `Bash(test:*)` - File existence checks
- `Bash(python:*)` - Script execution
- `Read(*)` - PDF and file reading
- `Write(*)` - Output file creation
- `Task(*)` - Agent invocation

## 🌟 Features

### ✅ Completed

- [x] PDF validation and parsing
- [x] Sequential workflow orchestration
- [x] State persistence and resumption
- [x] Error handling with retry logic
- [x] 5 output types (Notes, Problems, Answers, Explanations, Script)
- [x] UTF-8 encoding support
- [x] Visual formatting (colored boxes, tables)
- [x] Progress tracking and reporting
- [x] Example outputs and documentation

### 🚧 Future Enhancements

- [ ] Batch processing (multiple chapters)
- [ ] Custom output templates
- [ ] Interactive preview mode
- [ ] Export to Anki flashcards
- [ ] LaTeX source output option
- [ ] Web interface for configuration
- [ ] Quality validation checks (automated)
- [ ] Multi-language support

## 🙏 Acknowledgments

- Built for [Claude Code](https://claude.ai/code) plugin marketplace
- Putnam Math Competition problem style

## 🔗 Links

- [Plugin Marketplace](https://claude.ai/plugins)
- [Claude Code Documentation](https://docs.claude.ai/code)

---

**Version**: 1.0.0
**Last Updated**: 2026-02-17
**Status**: Production Ready
