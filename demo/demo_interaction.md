# Demo Interaction with AI Debugging Assistant

**Student Input:**



**Assistant Output:**

Error Summary:
Possible syntax error at line 1 — missing punctuation.

Hint Level 1:
Check the end of the function definition line. Python requires a specific token there.

Hint Level 2:
Look at `def add_numbers(a, b)`. Normally, a colon `:` comes after the parameter list.

Hint Level 3:
Replace the end of the def line with the correct punctuation and ensure the body is indented:



Test Suggestion:
After the fix, run `python example1_syntax_error.py` to verify no SyntaxError appears.
