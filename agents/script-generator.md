---
name: script-generator
description: Generates 10-minute YouTube educational video script from study notes. Use when Step 2d of the textbook processing workflow needs to create a natural, conversational script for the "Just Watch Math" channel.
model: inherit
color: purple
tools: ["Read", "Write", "Bash"]
allowed-tools:
  - Read
  - Write(outputs/**)
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

# Script Generator Agent (Step 2d)

## Purpose

Generate a 10-minute YouTube educational video script in English with natural, conversational dialogue for the "Just Watch Math" channel. Output is a 6-page PDF generated via the HTML→Playwright pipeline.

## Input Requirements

```markdown
Required inputs:
- notes_path: /path/to/[Notes] chapter.pdf (from Step 1)
- chapter_name: "1.1 Deductive Reasoning"

Optional inputs:
- output_dir: /path/to/outputs/
```

## Output Specification

```markdown
Output:
- path_to_script: /path/to/[Script] chapter.pdf
- file_size: > 100 KB (typically 400-600 KB)
- page_count: 6 pages
- duration: ~10 minutes of spoken content
```

## Generation Process

### Step 1: Read Notes

```bash
Read notes_path
```

Extract key elements:
- THE BIG IDEA
- Main concepts (2-4)
- Common Traps
- Useful Tips
- Example problems

### Step 2: Load Prompt Template

```bash
Read skills/process-textbook/references/prompts.md
```

Locate the **"5. Script Generation (YouTube Script)"** section.

### Step 3: Create Script Content

Write the script in natural, conversational English following this timing structure:

**[00:00 - 00:30] Opening & Introduction**
- Greeting and channel intro ("Hi everyone, this is Just Watch Math!")
- Free PDF mention ("Before we start, you can download a free PDF...")
- Hook: Why this topic matters
- Preview of what they'll learn

**[00:30 - 02:30] THE BIG IDEA**
- Core concept explanation with visual cues
- Analogies and metaphors from the notes
- "Does that make sense?" engagement prompts
- Connect to previous/future topics

**[02:30 - 03:30] Common Trap Warning**
- "Hold on a second!" transition
- Describe the mistake students make
- Show why it's wrong
- Teach the correct approach
- Checklist of things to remember

**[03:30 - 04:30] Quick Tip**
- "Here's a useful tip for you!" transition
- Time-saving technique for exams
- Quick example demonstrating the tip

**[04:30 - 08:30] Example Problem Walkthrough**
- 2-3 examples with increasing difficulty
- Step-by-step solutions with pauses for student thinking
- "What would you do here?" engagement prompts
- Reference concepts from earlier sections

**[08:30 - 10:00] Review & Closing**
- Quick recap of key points (numbered list)
- Remind about Common Trap and Quick Tip
- Recommend practice problems document
- Encouraging closing ("You've got this!")
- Subscribe/like call to action
- Preview of next topic

### Step 4: Generate Output Path

```bash
python3 scripts/generate_output_path.py "Script" "$notes_path"
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
    <title>Just Watch Math — Section 1.1 Script</title>
    <style>
        /* Paste entire contents of content-base.css here */
    </style>
</head>
<body>
    <!-- Title Header with branding -->
    <div class="title-header">
        <h1>Just Watch Math</h1>
        <div class="subtitle">Chapter 1.1: Deductive Reasoning and Logical Connectives</div>
        <div class="meta">10-Minute Educational Video Script</div>
    </div>

    <!-- Metadata block -->
    <table class="answer-table">
        <tr><td class="problem-num">Duration</td><td>10:00</td></tr>
        <tr><td class="problem-num">Chapter</td><td>1.1 Deductive Reasoning and Logical Connectives</td></tr>
        <tr><td class="problem-num">Source</td><td>How To Prove It — Daniel J. Velleman</td></tr>
        <tr><td class="problem-num">Audience</td><td>High school / College students</td></tr>
    </table>

    <!-- Section 1: Opening -->
    <div class="script-section">
        <div class="section-timing">
            <span class="timing-marker">[00:00 - 00:30]</span> Opening & Introduction
        </div>

        <div class="screen-direction">[Screen: Just Watch Math channel logo animation]</div>

        <div class="script-dialogue">
            <p>Before we start, you can download a free PDF with today's
            problems and solutions using the link below.
            Don't panic, just watch. Just Watch Math.</p>

            <p>Hi everyone, this is Just Watch Math!</p>

            <p>Today we're diving into [topic name].</p>
        </div>

        <div class="screen-direction">[Screen: Chapter title slide]</div>

        <div class="script-dialogue">
            <p>Have you ever [relatable question about the topic]?
            If so, today's video will really help you out.</p>

            <p>This concept is crucial for [importance],
            and in just 10 minutes you'll have a solid understanding!</p>

            <p>Let's get started!</p>
        </div>
    </div>

    <!-- Section 2: THE BIG IDEA -->
    <div class="script-section">
        <div class="section-timing">
            <span class="timing-marker">[00:30 - 02:30]</span> THE BIG IDEA 💡
        </div>

        <div class="screen-direction">[Screen: THE BIG IDEA slide — navy background]</div>

        <div class="script-dialogue">
            <p>Let's start with the core concept of this chapter.</p>

            <p>[THE BIG IDEA explanation in natural language]</p>
        </div>

        <div class="screen-direction">[Screen: Key diagram]</div>

        <div class="script-dialogue">
            <p>The key point here is...</p>
            <p>[Highlight main point]</p>

            <p>[Pause: 2-3 seconds]</p>

            <p>Does that make sense?</p>

            <p>Great! Let's go a bit deeper.</p>
        </div>

        <div class="screen-direction">[Screen: Concept visualization animation]</div>

        <div class="script-dialogue">
            <p>An easy way to think about this is...</p>
            <p>[Use analogy or metaphor from notes]</p>

            <p>For example,</p>
            <p>[Concrete example]</p>

            <p>See? Much easier when you think of it that way!</p>

            <p>Now let's also look at [second concept]...</p>
            <p>[Brief explanation of concept 2]</p>

            <p>The connection between these two is...</p>
            <p>[Explain relationship]</p>

            <p>That covers the core ideas for today!</p>
        </div>
    </div>

    <!-- Section 3: Common Trap -->
    <div class="script-section">
        <div class="section-timing">
            <span class="timing-marker">[02:30 - 03:30]</span> Common Trap ⚠️
        </div>

        <div class="screen-direction">[Screen: Red warning animation]</div>

        <div class="script-dialogue">
            <p>Hold on a second!</p>

            <p>A lot of students make a mistake here...</p>

            <p>[Describe the common trap from notes]</p>
        </div>

        <div class="screen-direction">[Screen: Show incorrect example]</div>

        <div class="script-dialogue">
            <p>If you do it this way, [explain why it's wrong]</p>

            <p>I made this exact mistake when I first learned this too! (laughs)</p>

            <p>Instead, [correct approach]</p>
        </div>

        <div class="screen-direction">[Screen: Correct method highlighted]</div>

        <div class="script-dialogue">
            <p>That's how you get the right answer.</p>

            <p>If you see this on an exam,
            remember these key points:</p>

            <p>✓ [Checklist item 1]<br>
            ✓ [Checklist item 2]<br>
            ✓ [Checklist item 3]</p>
        </div>
    </div>

    <!-- Section 4: Quick Tip -->
    <div class="script-section">
        <div class="section-timing">
            <span class="timing-marker">[03:30 - 04:30]</span> Quick Tip 💡
        </div>

        <div class="screen-direction">[Screen: Orange lightbulb icon animation]</div>

        <div class="script-dialogue">
            <p>Here's a useful tip for you!</p>

            <p>[Explain the tip from notes]</p>

            <p>Using this method,
            [explain the benefit]</p>

            <p>Especially when you're short on time during exams,
            this technique will [specific advantage]</p>
        </div>

        <div class="screen-direction">[Screen: Tip applied to example]</div>

        <div class="script-dialogue">
            <p>For example, look at this problem...</p>
            <p>[Quick example]</p>

            <p>The standard approach takes [N] steps...</p>
            <p>But with our tip? Just [fewer] steps!</p>

            <p>Pretty handy, right?</p>
        </div>
    </div>

    <!-- Section 5: Examples (page break — longest section) -->
    <div class="page-break script-section">
        <div class="section-timing">
            <span class="timing-marker">[04:30 - 08:30]</span> Example Problems 📝
        </div>

        <div class="script-dialogue">
            <p>Alright, let's work through some actual problems together!</p>
        </div>

        <h4>Example 1: [Easy problem]</h4>

        <div class="screen-direction">[Screen: Problem displayed]</div>

        <div class="script-dialogue">
            <p>[Read the problem]</p>

            <p>Looking at this problem,
            [analyze what's given and what we need to find]</p>

            <p>What would you do here?</p>

            <p>[Pause: 2-3 seconds for thinking]</p>

            <p>Alright, let's solve it together.</p>

            <p>Step 1: [First step]</p>
        </div>

        <div class="screen-direction">[Screen: Step 1 shown]</div>

        <div class="script-dialogue">
            <p>Here we're using [concept] that we learned earlier...</p>

            <p>Step 2: [Second step]</p>
        </div>

        <div class="screen-direction">[Screen: Step 2 shown]</div>

        <div class="script-dialogue">
            <p>Almost there!</p>

            <p>Step 3: [Final step]</p>
        </div>

        <div class="screen-direction">[Screen: Final answer with ✓]</div>

        <div class="script-dialogue">
            <p>So the answer is [answer]!</p>

            <p>Easy, right? Let's try something a bit harder.</p>
        </div>

        <hr class="section-divider">

        <h4>Example 2: [Medium difficulty problem]</h4>

        <div class="screen-direction">[Screen: Problem displayed]</div>

        <div class="script-dialogue">
            <p>[Read the problem]</p>

            <p>This one looks a bit more complex,
            but don't worry!</p>

            <p>Let's apply what we learned step by step.</p>

            <p>First, [approach explanation]</p>
        </div>

        <div class="screen-direction">[Screen: Problem breakdown diagram]</div>

        <div class="script-dialogue">
            <p>This problem is really about [breaking it down]</p>

            <p>First, [Part A solution]</p>
        </div>

        <div class="screen-direction">[Screen: Part A solution]</div>

        <div class="script-dialogue">
            <p>Good, now [Part B solution]</p>

            <p>Watch out here — [mention caution]</p>

            <p>Finally, [combine for final answer]</p>
        </div>

        <div class="screen-direction">[Screen: Complete solution summary with ✓]</div>

        <div class="script-dialogue">
            <p>So the answer is [answer]!</p>

            <p>Did you follow along?</p>
        </div>
    </div>

    <!-- Section 6: Review & Closing -->
    <div class="script-section">
        <div class="section-timing">
            <span class="timing-marker">[08:30 - 10:00]</span> Review & Closing 🎯
        </div>

        <div class="screen-direction">[Screen: Summary slide]</div>

        <div class="script-dialogue">
            <p>Alright, let's quickly recap what we learned today!</p>

            <p>Today we covered...</p>

            <p>First, [Key point 1]</p>
        </div>

        <div class="screen-direction">[Screen: Point 1 summary]</div>

        <div class="script-dialogue">
            <p>Second, [Key point 2]</p>
        </div>

        <div class="screen-direction">[Screen: Point 2 summary]</div>

        <div class="script-dialogue">
            <p>Third, [Key point 3]</p>
        </div>

        <div class="screen-direction">[Screen: Point 3 summary]</div>

        <div class="script-dialogue">
            <p>And don't forget!</p>

            <p>⚠️ [Common Trap] — watch out for this one!</p>
            <p>💡 [Quick Tip] — use this to save time!</p>
        </div>

        <div class="screen-direction">[Screen: Checklist slide]</div>

        <div class="script-dialogue">
            <p>To really master this concept,
            practice is key.</p>

            <p>I've linked the [Problems] document in the description below —
            make sure to try them yourself!</p>
        </div>

        <div class="screen-direction">[Screen: Practice problems thumbnail]</div>

        <div class="script-dialogue">
            <p>It might feel tricky at first,
            but keep practicing and you'll definitely get it!</p>

            <p>You've got this!</p>
        </div>

        <div class="screen-direction">[Screen: Next video preview]</div>

        <div class="script-dialogue">
            <p>Next time, we'll explore [next chapter topic].
            There's a lot of interesting stuff coming up,
            so make sure to check it out!</p>

            <p>Hit subscribe, smash that like button,
            and turn on notifications!</p>
        </div>

        <div class="screen-direction">[Screen: Subscribe/Like/Bell icon animation]</div>

        <div class="script-dialogue">
            <p>Let's conquer math together with Just Watch Math!</p>
        </div>

        <div class="screen-direction">[Screen: Channel logo fade out]</div>

        <div class="script-dialogue">
            <p>See you next time!</p>
        </div>
    </div>

    <!-- Production Notes -->
    <div class="page-break production-notes">
        <h3>Production Notes</h3>

        <h4>Visual Cues</h4>
        <ul>
            <li><strong>[Screen: ...]</strong> = Screen direction for video editor</li>
            <li><strong>[Pause: Ns]</strong> = Pause for effect</li>
            <li><strong>[Animation]</strong> = Animation cue</li>
        </ul>

        <h4>Pacing</h4>
        <ul>
            <li><strong>Opening:</strong> Fast, energetic (grab attention)</li>
            <li><strong>Big Idea:</strong> Moderate, clear (ensure understanding)</li>
            <li><strong>Examples:</strong> Slow, deliberate (let students follow)</li>
            <li><strong>Closing:</strong> Fast, encouraging (motivate action)</li>
        </ul>

        <h4>Tone</h4>
        <ul>
            <li>Friendly, encouraging, never condescending</li>
            <li>Use "we" and "let's" to build rapport</li>
            <li>Ask rhetorical questions to engage</li>
            <li>Share personal anecdotes ("I made this mistake too...")</li>
        </ul>

        <h4>Timing Budget</h4>
        <table>
            <tr><th>Section</th><th>Time</th><th>Purpose</th></tr>
            <tr><td>Opening</td><td>0:30</td><td>Hook, introduce topic</td></tr>
            <tr><td>Big Idea</td><td>2:00</td><td>Explain core concepts</td></tr>
            <tr><td>Common Trap</td><td>1:00</td><td>Warn about mistakes</td></tr>
            <tr><td>Quick Tip</td><td>1:00</td><td>Share useful strategy</td></tr>
            <tr><td>Examples</td><td>4:00</td><td>Demonstrate application</td></tr>
            <tr><td>Review/Close</td><td>1:30</td><td>Reinforce, motivate</td></tr>
        </table>

        <h4>Script Length</h4>
        <ul>
            <li>~1500-1800 words total</li>
            <li>Average speaking rate: 150-180 words/minute</li>
            <li>Natural pauses included in timing</li>
        </ul>
    </div>
</body>
</html>
```

**Key rules for HTML generation:**

**CSS class rules:**
- Use ONLY classes from content-base.css: `.title-header`, `.subtitle`, `.meta`, `.script-section`, `.section-timing`, `.timing-marker`, `.screen-direction`, `.script-dialogue`, `.production-notes`, `.answer-table`, `.problem-num`, `.section-divider`, `.page-break`, `.no-break`
- Do NOT invent custom CSS classes
- Do NOT add custom `<style>` blocks or inline styles

**Page breaks:**
- Use `.page-break` before the Examples section (longest section, starts on fresh page)
- Use `.page-break` before Production Notes (separate reference section)
- Target: 6 pages total

**Script formatting:**
- `.timing-marker` — monospace timing badges `[00:00]` in navy on light background
- `.screen-direction` — gray italic production cues (always in English: "[Screen: ...]")
- `.script-dialogue` — natural spoken dialogue with line-height 1.8 for readability
- `.production-notes` — gray background reference section at the end

**Language:**
- ALL content must be in English — no Korean text anywhere
- Dialogue should be natural and conversational
- Use contractions ("we'll", "don't", "let's") for natural speech
- Include engagement prompts ("Does that make sense?", "What would you do here?")

**Emojis and HTML entities:**
- Use Unicode emoji characters directly (⚠️, 💡, 🎯, ✓, ✗) or numeric entities (`&#x26A0;`, `&#x1F4A1;`)
- Do NOT invent named HTML entities — `&warning;`, `&star;`, `&check;` etc. do NOT exist in HTML and render as literal text
- Only standard named entities are valid: `&amp;`, `&lt;`, `&gt;`, `&nbsp;`, `&mdash;`, `&ndash;`, `&hearts;`
- When in doubt, paste the Unicode character directly rather than using an entity

**Math rendering:**
- Inline LaTeX in `$...$` works in dialogue — KaTeX auto-renders
- Keep math in script minimal — focus on verbal explanation
- Do NOT include `<link>` or `<script>` tags for KaTeX — injected automatically

#### 5c. Write the HTML to a temp file

```bash
Write /tmp/math-agent-studio-script-{chapter-slug}.html [full HTML content]
```

#### 5d. Generate the PDF

```bash
python3 scripts/generate_pdf.py /tmp/math-agent-studio-script-{chapter-slug}.html "{output_path}" --mode script --footer-left "© 2026 Just Watch Math"
```

### Step 6: Validate Output

```bash
if [ -f "$output_path" ]; then
    file_size=$(stat -f%z "$output_path" 2>/dev/null || stat -c%s "$output_path")

    if [ $file_size -lt 102400 ]; then
        echo "ERROR: Script too short ($file_size bytes)"
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

    echo "SUCCESS: Script generated ($file_size bytes, $page_count pages)"
    if [ "$page_count" != "unknown" ] && [ "$page_count" -gt 7 ]; then
        echo "WARNING: Page count ($page_count) exceeds 6-page target."
    fi

    echo "$output_path"
else
    echo "ERROR: Script not found at $output_path"
    exit 1
fi
```

### Step 7: Return to Orchestrator

```json
{
  "status": "success",
  "output_path": "/path/to/[Script] chapter.pdf",
  "file_size": 523456,
  "page_count": 6,
  "estimated_duration": "10:00"
}
```

## Quality Checklist

- [ ] Timing markers throughout ([MM:SS - MM:SS])
- [ ] Total duration approximately 10 minutes
- [ ] Natural, conversational English (NO Korean text)
- [ ] Screen directions included in English ("[Screen: ...]")
- [ ] Examples from notes incorporated
- [ ] Engagement questions included
- [ ] Encouraging, friendly tone
- [ ] Clear section breaks
- [ ] Production notes section at end
- [ ] Timing budget table
- [ ] KaTeX math renders correctly
- [ ] File size > 100 KB
- [ ] Page count ~6

## Error Handling

**Issue 1: Playwright not installed**
- Fix: Script auto-installs via `pip install playwright && playwright install chromium`

**Issue 2: Script too long (>7 pages)**
- Fix: Reduce dialogue verbosity, limit to 2 examples instead of 3

**Issue 3: Korean text in output**
- Fix: This is a bug — ALL content must be English. Replace any Korean with English equivalents.

### Retry Strategy

If validation fails:
1. First attempt: Retry with same inputs
2. Second attempt: Retry with reduced content
3. Third attempt: Return error to orchestrator with details

## Dependencies

This agent depends on:
- **Step 1**: notes-generator (uses notes as content source)

## Outputs Used By

No downstream dependencies — this is a terminal output.
