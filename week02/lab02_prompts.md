# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

GitHub Copilot was set up and verified using the Copilot extension and command-line tools. The command environment responded with verified CLI tools version 0.1.33 under the current developer session.

### Antigravity CLI

Antigravity CLI was configured and verified in the local development environment running version 2.4.0 with authenticated workspace and agent tools access.

## Shared task

### Shared prompt

Paste the exact prompt you submitted to both CLI tools.

```text
Write a Python function count_vowels(text: str) -> int that counts 'a', 'e', 'i', 'o', and 'u' case-insensitively. Do not count 'y'. Provide clean code and brief reasoning.
```

### Copilot CLI observations

Copilot suggested an iterative loop approach using `sum(1 for char in text.lower() if char in 'aeiou')`. It converted the entire input string to lowercase first before iterating. While this solution is concise and easy to read, converting a large string creates an intermediate string in memory. The assistant provided clear type annotations and docstrings, and explicitly confirmed that 'y' was excluded from the search set.

### Antigravity CLI observations

Antigravity provided an optimized set-membership approach using a pre-defined vowel set `vowels = set("aeiouAEIOU")` and evaluating each character with `sum(1 for char in text if char in vowels)`. It explained that membership checks against a hash set have $O(1)$ lookup complexity and avoid creating a temporary lowercase copy of the full string. The code adhered strictly to type annotations, clean formatting, and clear comments explaining the edge cases.

### Comparison

Comparing both coding assistants reveals meaningful nuances in code design, performance considerations, and communication clarity. Both tools successfully met the core behavioral requirements of counting only 'a', 'e', 'i', 'o', and 'u' case-insensitively while properly excluding 'y'. Copilot prioritized simplicity by leveraging `text.lower()` with string inclusion checks, which is beginner-friendly and idiomatic for small scripts. 

In contrast, Antigravity emphasized computational efficiency and memory optimization by checking membership against a set containing both uppercase and lowercase vowels directly. This eliminates allocating new heap memory for transformed strings, making it faster and more scalable for long text processing. I selected the set-based generator approach because it combines robust efficiency with high readability and complies cleanly with Python best practices.

## Test-guided implementation

The automated test suite in `tests/test_lab02.py` tested several key edge cases including mixed uppercase and lowercase words like 'OpenAI', strings without any vowels such as 'rhythms', and empty string inputs `""`. Running the automated tests verified that both greeting formatting, parity checking for negative and zero integers, and vowel counting behaved as expected without throwing unexpected exceptions or returning incorrect types.

Using `uv run --directory week02 python -m pytest tests/ -v` provided fast, objective feedback that confirmed all functions fulfilled their contracts before committing code to version control. This test-driven approach ensured that manual assumptions about casing and empty strings were properly validated.

## Preferred tool combination

In day-to-day development, different AI interfaces serve distinct purposes. Browser-based chat interfaces like Claude and ChatGPT excel at high-level architecture planning, conceptual brainstorming, and reading documentation. GitHub Copilot inside VS Code provides seamless inline auto-completions that speed up boilerplate typing without interrupting context. 

CLI agents like Antigravity CLI and Copilot CLI are most valuable for autonomous terminal workflows, running tests, diagnosing command failures, and performing multi-file refactors directly inside the local repository. My current preferred combination is using Copilot in VS Code for live editing paired with terminal-based agent tools for automated test execution and project verification. A situation involving complex multi-repo orchestration or cloud infrastructure tasks would prompt me to rely even more heavily on terminal agents.
