import pathlib
print("Examples included in the repo:")
for f in pathlib.Path("examples").iterdir():
    print("-", f.name)
print("Check PROMPT.md and REASONING.md for main content.")
