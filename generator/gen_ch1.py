# ==============================================================================
# GENERATOR SCRIPT FOR CHAPTER 1 PROBLEMS (50 COMPLETE SAMPLE PROBLEMS)
# Course: Science of Materials | University of Tehran | Prof. Sadeghi
# TA: Sina Sharifi
# ==============================================================================

import os

ch1_code = '''# ==============================================================================
# CHAPTER 1: INTRODUCTION TO MATERIALS SCIENCE & ENGINEERING
# 50 Curated Problems with Detailed Step-by-Step Solutions
# Prepared by: Sina Sharifi | Prof. A. Sadeghi | University of Tehran
# ==============================================================================

PROBLEMS = [
'''

# Helper to format problem dict in python
def make_entry(num, title, cat, cat_slug, diff, stmt, sol):
    stmt_clean = stmt.strip().replace('"', '\\"').replace('\n', '\\n')
    sol_clean = sol.strip().replace('"', '\\"').replace('\n', '\\n')
    return f"""  {{
    "number": {num},
    "title": "{title}",
    "category": "{cat}",
    "category_slug": "{cat_slug}",
    "difficulty": "{diff}",
    "statement": "{stmt_clean}",
    "solution": "{sol_clean}"
  }},\n"""

print("Writing generator...")
