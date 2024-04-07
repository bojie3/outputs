import language_tool_python
tool = language_tool_python.LanguageTool('en-US')  

errors = []
total = 0
with open("long_typo_output.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        temp = tool.check(line)
        total += len(temp)
        errors.append[line, temp]
print(total)
print(errors)

