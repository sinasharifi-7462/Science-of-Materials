import re

with open("generator/build_ch1_data.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace any triple quote not preceded by r with r"""
fixed = re.sub(r'(?<!r)"""', 'r"""', text)

with open("generator/build_ch1_data.py", "w", encoding="utf-8") as f:
    f.write(fixed)

print("Fixed raw strings in build_ch1_data.py")
