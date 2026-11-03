# AI USE LOG

- Course: SECB3203
- Assessment: Lab 2
- Student name: Moayed Mohamed Saleh
- Matric no: A24CS0017
- Group ID: n/a
- AI level: 1
- Tools cited: OpenAI (2026). ChatGPT (GPT-6). Accessed 3 November 2026 from https://chatgpt.com/c/6ae95061-3894-83ed-9bc7-be409335ee14

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 3 November 2026
- Tool: OpenAI ChatGPT (GPT-6), accessed 3 November 2026, https://chatgpt.com/c/6ae95061-3894-83ed-9bc7-be409335ee14
- Purpose: explain
- Prompt: "give me an example to test this function in terminal? def clean_sequence(raw: str) -> str: ..."
- Output: AI explained how to test the `clean_sequence()` function using the Python terminal and provided examples involving lowercase letters, spaces, digits and newlines.
- Verified by: Ran the examples in the Python terminal and checked the expected outputs.
- My change: Used the examples to understand how the function processes different inputs.
- Used in: `src/lab02_sequences.py`, `clean_sequence()`.

## Entry 2

- Date: 3 November 2026
- Tool: OpenAI ChatGPT (GPT-6), accessed 3 November 2026, https://chatgpt.com/c/6ae95061-3894-83ed-9bc7-be409335ee14
- Purpose: explain
- Prompt: "i didnt understand what exactly im suppossed to do in this function"
- Output: AI explained how `find_motif()` searches for a smaller sequence inside a larger sequence, including 0-based positions, overlapping matches, case-insensitive matching and empty motif handling.
- Verified by: Compared the examples with the assessment requirements and checked the expected positions.
- My change: Used the explanation to understand the requirements and implemented the function myself.
- Used in: `src/lab02_sequences.py`, `find_motif()`.

## Entry 3

- Date: 3 November 2026
- Tool: OpenAI ChatGPT (GPT-6), accessed 3 November 2026, https://chatgpt.com/c/6ae95061-3894-83ed-9bc7-be409335ee14- 
Purpose: tests-plan
- Prompt: "what type of tests i can do for Add three tests for find_motif, make python -m pytest pass, and make ruff check src report no issues. Complete your AI use log. dont write the code i will"
- Output: AI suggested three test scenarios: normal motif matching, overlapping matches and case-insensitive matching. It also explained additional edge cases.
- Verified by: Ran `python -m pytest` and checked the test results.
- My change: Selected the suggested test scenarios and wrote the tests myself without asking AI to generate the test code.
- Used in: `tests/`, tests for `find_motif()`.

## Entry 4

- Date: 3 November 2026
- Tool: OpenAI ChatGPT (GPT-6), accessed 3 November 2026, https://chatgpt.com/c/6ae95061-3894-83ed-9bc7-be409335ee14
- Purpose: debug
- Prompt: "what is the error?" (Provided my Python implementation and the pytest output.)
- Output: AI identified two problems: incorrect indentation in `gc_content()` caused only the last character to be counted, and `transcribe()` used an uninitialised variable and had an incorrectly indented return statement.
- Verified by: Ran `python -m pytest` to identify the failing tests and reviewed the suggested corrections.
- My change: Used the debugging explanation to understand the mistakes and planned to correct the indentation and variable usage myself.
- Used in: `src/lab02_sequences.py`, `gc_content()` and `transcribe()`.