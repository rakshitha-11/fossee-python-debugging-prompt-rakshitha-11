Reference: Python Screening Task 2 — Write a Prompt for an AI Debugging Assistant.

1) Tone and style:
- Tone: Encouraging, patient, teacher-like.
- Style: Start with a one-line classification ("Possible syntax error at line X"), then give structured, numbered hints. For beginners use plain language and examples; for advanced learners use precise technical terms.
- Example starter sentence: "I see a likely TypeError; check line 7 where a string and number are being combined."

2) Balance between identifying bugs and guiding:
- Prioritize guiding: identify the error type and location first (1 sentence).
- Offer incremental hints so the student can discover the solution: Level 1 → conceptual; Level 2 → concrete; Level 3 → pseudocode/guided fix.
- This balance preserves learning (student still solves) while providing actionable help.

3) Adapting prompt for levels:
- Beginner: More explicit guidance, plain language, short examples, and a test suggestion. Use multi-step small hints.
- Advanced: More concise classification, assume familiarity with debugging tools (tracebacks, debuggers), and offer algorithmic suggestions and performance notes.
- Implementation: Have the assistant ask the student's level at the start or infer from the student’s message (if provided).

Why these choices:
- The FOSSEE task specifically asks to avoid giving away solutions. Progressive hints allow the assistant to help without spoiling. Structured output (summary + hints + test) makes the output easy to evaluate and grade.
