# generator/verify_site.py
import glob
import re
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chapters_dir = os.path.join(base_dir, 'chapters')
files = sorted(glob.glob(os.path.join(chapters_dir, 'chapter*.html')))
print(f"Found {len(files)} chapter files in {chapters_dir}:")

total_cards = 0
total_buttons = 0
total_solutions = 0

for f in files:
    fname = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    cards = len(re.findall(r'<article class="problem-card"', content))
    buttons = len(re.findall(r'btn-toggle-solution', content))
    solutions = len(re.findall(r'class="solution-container"', content))
    total_cards += cards
    total_buttons += buttons
    total_solutions += solutions
    print(f"  {fname}: {cards} problem cards, {buttons} toggle buttons, {solutions} solutions")

print("-" * 65)
print(f"TOTAL: {total_cards} problem cards, {total_buttons} toggle buttons, {total_solutions} solutions")

idx_path = os.path.join(base_dir, 'index.html')
with open(idx_path, 'r', encoding='utf-8') as fp:
    idx = fp.read()

print("-" * 65)
print(f"index.html verification:")
print(f"  File size: {len(idx)} bytes")
print(f"  Attribution 'Sina Sharifi': {'Sina Sharifi' in idx}")
print(f"  Professor 'Prof. A. Sadeghi': {'Prof. A. Sadeghi' in idx}")
print(f"  University 'University of Tehran': {'University of Tehran' in idx}")
print(f"  Department 'Department of Mechanical Engineering': {'Department of Mechanical Engineering' in idx}")
print(f"  Course 'Science of Materials': {'Science of Materials' in idx}")
print(f"  Links to all 8 chapters in chapters/ folder: {all(f'chapters/chapter{i}.html' in idx for i in range(1, 9))}")
