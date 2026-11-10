# Populate Ch1
import json

problems = []

def add(num, title, cat, slug, diff, stmt, sol):
    problems.append({
        'number': num,
        'title': title,
        'category': cat,
        'category_slug': slug,
        'difficulty': diff,
        'statement': stmt,
        'solution': sol
    })

# We will populate all 50
print('Ready to write populate_ch1')
