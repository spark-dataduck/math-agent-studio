# Math Textbook Processing Prompts

This file contains all AI prompt templates for generating the 5 output types from math textbook PDFs.
All prompts are in Korean as specified by the user.

---

## 1. Notes Generation (내용 요약정리)

**Purpose:** Generate comprehensive study notes (8-11 pages) with concepts, mnemonics, examples, and common traps.

**Target Audience:** Students preparing for exams who need structured, visual study materials.

**Output Format:** PDF with colored boxes, tables, icons, and visual hierarchy.

### Korean Prompt:

```
중요한 개념, 공식 키워드 눈에 잘 띄게 정리 해줘. 한 개념 또는 공식 배운 다음에 바로 쉬운 예제를 넣어줘.

내가 공부할 때 시험볼 때 자주 틀리고 헷갈렸던 부분들도 꼭 언급해주고, 개념을 이해하는 데 도움이 될 만한 비유나 시각적 연상법도 추가해줘.

**포함할 요소:**
- THE BIG IDEA (navy 박스): 챕터의 핵심 개념
- Visual Mnemonics: 개념을 쉽게 기억할 수 있는 비유/은유
- Definition Tables: 정의를 표 형식으로 정리
- Common Traps (빨간 경고): 자주 틀리는 실수들
- Useful Tips (주황 박스): 문제 풀 때 유용한 팁
- "Try These" 예제: 각 개념마다 3-4개의 연습 문제

**형식 가이드:**
- 8-11 페이지 분량
- 색상 구분 (navy = 핵심, red = 주의, orange = 팁)
- 표와 다이어그램 적극 활용
- 수식은 명확하게 표기
```

### Expected Output Structure:

```
[Notes] Chapter Title.pdf

Page 1: THE BIG IDEA (navy box)
  - Core concept overview
  - Why this matters
  - Key vocabulary

Page 2-3: Concept 1
  - Definition (table format)
  - Visual mnemonic
  - Examples (2-3)
  - Try These (3-4 problems)

Page 4-5: Concept 2
  - Common Trap (red warning box)
  - Useful Tip (orange box)
  - Worked examples
  - Try These

Page 6-8: Advanced Concepts
  - Building on basics
  - Edge cases
  - Complex examples

Page 9-10: Review Section
  - Summary table
  - Key formulas
  - Common mistakes recap

Page 11: Quick Reference
  - Formula sheet
  - Checklist
```

---

## 2. Problems Generation (문제 생성)

**Purpose:** Generate 10 practice problems (6 standard exam + 4 competition level).

**Target Audience:** Students who want to test understanding and prepare for competitions.

**Output Format:** PDF with clearly numbered problems, progressive difficulty.

### Korean Prompt:

```
최대한 Putnam Math Competition 스타일로 만들어줘.

**문제 구성:**
- Section A (1-6번): 표준 시험 문제 (난이도: 쉬움 → 중간)
- Section B (7-10번): 경시대회 스타일 문제 (난이도: 어려움)

**요구사항:**
- 각 문제는 챕터의 핵심 개념을 테스트해야 함
- 문제는 단계적으로 어려워져야 함 (progressive difficulty)
- 일부 문제는 다단계 (multi-part)로 구성
- 문제 사이에 충분한 공간 제공 (학생들이 풀 수 있도록)
- 명확한 번호 매기기와 구분

**스타일:**
- 간결하고 명확한 문제 진술
- 필요한 경우 다이어그램 포함
- 계산 문제와 증명 문제를 적절히 섞음
```

### Expected Output Structure:

```
[Problems] Chapter Title.pdf

Section A: Standard Problems (표준 문제)

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

Section B: Competition Problems (경시 문제)

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

## 3. Quick Answers Generation (답지 생성)

**Purpose:** Generate concise answer key in table format for quick checking.

**Target Audience:** Students who want to quickly verify their answers.

**Output Format:** 1-page PDF with compact table layout.

### Korean Prompt:

```
빠르게 답만 일단 먼저 체크할 수 있게 답만 정리해서 답지 만들어줘.

**형식:**
- 표 형식 (Table format)
- 문제 번호 | 답안 컬럼 구조
- 교차 행 색상 (Alternating row colors)
- 간단한 설명 (예: "x = 3" 또는 "증명 필요")

**요구사항:**
- 1페이지에 모든 답안 포함
- 명확하고 간결한 답안
- 다단계 문제는 각 파트 별로 답안 표시 (예: 1a, 1b)
- 증명 문제는 "증명 참조" 표시
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

## 4. Explanations Generation (해설지 생성)

**Purpose:** Generate detailed step-by-step solutions with multiple approaches.

**Target Audience:** Students who got wrong answers or want to learn different solution methods.

**Output Format:** 2-3 page PDF with detailed explanations.

### Korean Prompt:

```
해설과 답 같이 넣어줘. 문제를 접근하는 방법/푸는 방법이 여러가지가 있다면 여러 가지 방법 다 설명해줘.

**포함할 요소:**
- 답안 (볼드체로 강조)
- 단계별 설명 (Step-by-step reasoning)
- 케이스 분석 (Case analysis when applicable)
- 자주 하는 실수 강조 (Common errors highlighted)
- 대안 풀이법 (Alternative solution methods)

**스타일:**
- 명확하고 논리적인 설명
- 각 단계의 이유 설명
- 수식과 텍스트 적절히 혼합
- 중요한 통찰 강조
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

## 5. Script Generation (유튜브 스크립트 생성)

**Purpose:** Generate 10-minute YouTube educational video script.

**Target Audience:** Visual/auditory learners who prefer video content.

**Output Format:** 6-page PDF with timing markers and natural dialogue.

### Korean Prompt:

```
10분 가량의 친근하고 자연스러운 튜터선생님 톤으로 유튜브 스크립트 작성해줘.

**브랜딩:**
- 채널명: "Just Watch Math"
- 톤: 친근하고 격려적인 선생님
- 스타일: 대화형, 질문을 던지며 설명

**구조:**
1. Opening (30초)
   - 인사와 채널 소개
   - 오늘 배울 내용 미리보기

2. THE BIG IDEA (2분)
   - 핵심 개념 설명
   - 왜 이게 중요한지 설명

3. Common Trap 경고 (1분)
   - 자주 틀리는 실수들
   - 어떻게 피할 수 있는지

4. Quick Tip (1분)
   - 문제 풀 때 유용한 팁
   - 시험에서 시간 절약하는 방법

5. 예제 문제 풀이 (4분)
   - 2-3개 예제를 단계별로 설명
   - 학생들이 따라할 수 있도록 천천히

6. Review & Closing (1분 30초)
   - 핵심 내용 요약
   - 연습 문제 추천
   - 다음 영상 예고

**요구사항:**
- 타이밍 마커 표시 [00:30], [02:00] 등
- 자연스러운 전환 문구
- 시각 자료 힌트 포함 (예: "[화면에 수식 표시]")
- 학생들에게 질문 던지기 (참여 유도)
```

### Expected Output Structure:

```
[Script] Chapter Title.pdf

=== Just Watch Math - [Chapter Title] ===

[00:00 - 00:30] Opening
안녕하세요, Just Watch Math입니다!
오늘은 [주제]에 대해서 알아볼 거예요.
이 개념은 [중요성]에서 정말 중요한데요,
10분만 집중하면 완벽하게 이해할 수 있을 거예요!

[00:30 - 02:30] THE BIG IDEA
자, 그럼 시작해볼까요?
[핵심 개념 설명...]
[화면에 다이어그램 표시]

여러분, 이해되시나요?
이 개념의 핵심은 바로 [...]입니다.

[02:30 - 03:30] Common Trap
자, 여기서 잠깐!
많은 학생들이 이 부분에서 실수를 하는데요...
[일반적인 실수 설명]

이렇게 하면 틀리게 됩니다!
대신 [올바른 방법]...

[03:30 - 04:30] Quick Tip
여기 유용한 팁 하나 알려드릴게요!
[팁 설명...]

이 방법을 쓰면 시험에서 시간을 많이 절약할 수 있어요.

[04:30 - 08:30] Examples
그럼 이제 실제 문제를 한번 풀어볼까요?

Example 1: [문제 설명]
Step 1: ...
Step 2: ...
[상세 풀이]

Example 2: [문제 설명]
이번엔 조금 더 어려운 문제인데요...
[상세 풀이]

[08:30 - 10:00] Review & Closing
자, 오늘 배운 내용을 정리해볼게요.
1. [핵심 포인트 1]
2. [핵심 포인트 2]
3. [핵심 포인트 3]

이 개념을 완벽하게 익히려면
[Problems] 문서에 있는 연습문제를 꼭 풀어보세요!

다음 시간에는 [다음 주제]에 대해 알아볼 거예요.
구독과 좋아요 부탁드리고,
Just Watch Math와 함께 수학 정복해봐요!

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
- [ ] Korean text is properly encoded (UTF-8)
- [ ] Visual elements (boxes, colors) are present
- [ ] Page count is within target range
- [ ] File size > 100KB (not corrupted)
- [ ] Content matches prompt requirements

---

## Usage Notes for Agents

1. **Always load the specific prompt** for your output type from this file
2. **Follow the Korean language exactly** - do not translate or modify
3. **Reference the expected output structure** when generating content
4. **Apply formatting guidelines** consistently across all outputs
5. **Validate against quality checklist** before returning path to orchestrator

---

## Version History

- v1.0.0 (2026-02-13): Initial prompt library with 5 output types
