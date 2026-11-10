# generator/build_site.py
# ==============================================================================
# SCIENCE OF MATERIALS — COMPLETE MASTER SITE ASSEMBLER
# University of Tehran | Department of Mechanical Engineering
# Author: Sina Sharifi | Instructor: Prof. A. Sadeghi
# ==============================================================================

import os
import sys

# Ensure generator directory is in path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, CURRENT_DIR)

import common
import svg_assets

# Import all 8 problem datasets
import ch1_data
import ch2_data
import ch3_data
import ch4_data
import ch5_data
import ch6_data
import ch7_data
import ch8_data

DATASETS = {
    1: ch1_data.PROBLEMS,
    2: ch2_data.PROBLEMS,
    3: ch3_data.PROBLEMS,
    4: ch4_data.PROBLEMS,
    5: ch5_data.PROBLEMS,
    6: ch6_data.PROBLEMS,
    7: ch7_data.PROBLEMS,
    8: ch8_data.PROBLEMS,
}

CHAPTER_SVGS = {
    1: (svg_assets.svg_tetrahedron(), "MSE Processing-Structure-Properties-Performance Tetrahedron"),
    2: (svg_assets.svg_potential_well(), "Interatomic Potential Energy Well & Equilibrium Separation"),
    3: (svg_assets.svg_crystal_unit_cells(), "Unit Cells & Planar Atomic Packing (FCC, BCC, HCP)"),
    4: (svg_assets.svg_point_defects(), "Lattice Imperfections, Vacancies & Edge/Screw Dislocations"),
    5: (svg_assets.svg_diffusion_profiles(), "Fick's Diffusion Concentration Profiles & Error Function Solutions"),
    6: (svg_assets.svg_stress_strain_curve(), "Engineering vs True Stress-Strain & Plastic Work Hardening"),
    7: (svg_assets.svg_hall_petch(), "Hall-Petch Grain Refinement & Precipitation Strengthening"),
    8: (svg_assets.svg_charpy_dbtt(), "Charpy Impact DBTT Transition & Fatigue S-N Wöhler Curves"),
}

MATHJAX_HEADER = """
  <!-- MathJax 3 Configuration for High-Fidelity Technical Rendering -->
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      },
      options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }
    };
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
"""

# ==============================================================================
# BUILD INDEX.HTML (THE MASTER PORTAL & DETAILED COVER PAGE)
# ==============================================================================
def build_index():
    print("Building index.html (Master Cover Portal)...")
    
    chapter_cards_html = ""
    for ch in common.CHAPTERS:
        cid = ch["id"]
        svg_code, svg_caption = CHAPTER_SVGS.get(cid, ("", ""))
        tags_html = "".join([f'<span class="hero-tag">{tag}</span>' for tag in ch["tags"]])
        
        chapter_cards_html += f"""
        <article class="chapter-card">
          <div class="card-hero-preview" style="height: 180px; overflow: hidden; background: #060b1a; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid rgba(212, 175, 55, 0.2);">
            {svg_code}
          </div>
          <div class="card-content">
            <div class="card-meta">
              <span class="chapter-num-badge">Chapter {cid:02d}</span>
              <span class="problem-count-badge">50 Problems &bull; 100% Solutions</span>
            </div>
            <h3 class="card-title">
              <a href="{ch['filename']}">{ch['title']}</a>
            </h3>
            <p class="card-desc">
              {ch['desc']}
            </p>
            <div class="card-tags" style="margin-bottom: 1.25rem;">
              {tags_html}
            </div>
            <a href="{ch['filename']}" class="btn-primary" style="width: 100%; justify-content: center;">
              <span>Study Chapter {cid} Problems</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </a>
          </div>
        </article>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Science of Materials — Midterm Exam Problem Suite | University of Tehran</title>
  <meta name="description" content="Comprehensive 400-problem midterm examination mastery suite for the Science of Materials course at the University of Tehran, Department of Mechanical Engineering.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Playfair+Display:ital,wght@0,500;0,700;1,400&family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  {MATHJAX_HEADER}
</head>
<body data-page-id="index">
  {common.generate_header(active_page="index", title="Science of Materials — University of Tehran")}

  <main class="master-wrapper">
    <!-- Academic Formal Cover Banner -->
    <section class="cover-hero">
      <div class="university-crest">
        {common.SVG_UT_SEAL}
      </div>

      <p class="cover-pretitle">UNIVERSITY OF TEHRAN &bull; DEPARTMENT OF MECHANICAL ENGINEERING</p>
      
      <h1 class="cover-main-title">SCIENCE OF MATERIALS</h1>
      
      <div class="gold-hairline"></div>

      <p class="cover-subtitle">
        Comprehensive 400-Problem Midterm Examination Study & Mastery Suite
      </p>

      <p class="cover-attribution" style="max-width: 780px; margin: 0 auto 2rem auto; font-size: 1.05rem; line-height: 1.7; color: #cbd5e1;">
        Prepared with meticulous analytical rigor by Teaching Assistant <strong>Sina Sharifi</strong><br>
        Under the Academic Supervision of <strong>Prof. A. Sadeghi</strong><br>
        <span style="font-size: 0.9rem; color: #94a3b8;">Covering the Complete Undergraduate Curriculum from Chapter 1 through Chapter 8 (up to Phase Diagrams)</span>
      </p>

      <!-- Quick Action Buttons -->
      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2.5rem;">
        <a href="#chapters-directory" class="btn-primary" style="padding: 0.85rem 1.75rem; font-size: 1rem;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          Explore All 8 Chapters (400 Problems)
        </a>
        <button id="btn-hero-formula" class="btn-classic" style="padding: 0.85rem 1.75rem; font-size: 1rem;" onclick="document.getElementById('formula-modal').classList.add('active')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          Master Formula Compendium
        </button>
      </div>

      <!-- Quick Stats Counter Strip -->
      <div class="stats-strip">
        <div class="stat-card">
          <div class="stat-num">8</div>
          <div class="stat-lbl">Curricular Chapters</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">400</div>
          <div class="stat-lbl">Sample Problems</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">50</div>
          <div class="stat-lbl">Problems Per Chapter</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">100%</div>
          <div class="stat-lbl">Step-by-Step Solutions</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">16+</div>
          <div class="stat-lbl">Technical SVG Diagrams</div>
        </div>
      </div>
    </section>

    <!-- Study Guide & Pedagogical Notice -->
    <section class="instructions-card" style="background: rgba(16, 28, 61, 0.7); border: 1px solid rgba(212, 175, 55, 0.35); border-radius: 6px; padding: 2rem; margin-bottom: 3.5rem;">
      <h2 style="font-family: var(--font-serif); color: var(--gold-light); font-size: 1.45rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.75rem;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#d4af37" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        How to Use This Problem Suite for Maximum Midterm Exam Success
      </h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; color: #cbd5e1; font-size: 0.95rem; line-height: 1.65;">
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">1. Self-Testing Active Recall:</strong>
          Every problem has its full derivation and boxed answer hidden by default. Always attempt to solve the question independently on paper before clicking <em>"Show Detailed Solution"</em>.
        </div>
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">2. Categorized Learning:</strong>
          Each chapter is organized into distinct categories (Atomic Structure, Miller Indices, Fick's Laws, Schmid's Law, Hall-Petch, LEFM, Creep). Use the category filters to target specific weak areas.
        </div>
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">3. Progress Tracking & Bookmarking:</strong>
          Click <em>"Mark Mastered"</em> on any problem you have conquered. Your browser will locally save your mastery tally in the header badge.
        </div>
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">4. Formula Sheet Modal:</strong>
          Click the <em>"Formula Sheet"</em> button in the header at any time to consult the master compendium of governing equations, unit definitions, and physical constants.
        </div>
      </div>
    </section>

    <!-- Master Chapters Directory -->
    <section id="chapters-directory">
      <div class="directory-header" style="text-align: center; margin-bottom: 2.5rem;">
        <p style="font-family: var(--font-mono); color: var(--gold); font-size: 0.85rem; letter-spacing: 0.15em; text-transform: uppercase;">Midterm Syllabus Directory</p>
        <h2 style="font-family: var(--font-serif); font-size: 2rem; color: #ffffff;">The Eight Curricular Chapters</h2>
        <div class="gold-hairline" style="margin: 0.75rem auto 0 auto;"></div>
      </div>

      <div class="chapters-grid">
        {chapter_cards_html}
      </div>
    </section>
  </main>

  {common.generate_formula_modal()}
  {common.generate_footer()}

  <script src="js/main.js"></script>
</body>
</html>
"""
    out_file = os.path.join(BASE_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully generated {out_file} (size: {len(html)} bytes)")

# ==============================================================================
# BUILD CHAPTER HTML PAGES (CHAPTER 1 TO 8)
# ==============================================================================
def build_chapter(ch_info):
    cid = ch_info["id"]
    filename = ch_info["filename"]
    title = ch_info["title"]
    short_title = ch_info["short_title"]
    desc = ch_info["desc"]
    problems = DATASETS.get(cid, [])
    
    print(f"Building {filename} (Chapter {cid} - {len(problems)} problems)...")

    # Collect unique categories for filter dropdown
    categories = []
    category_slugs = {}
    for p in problems:
        cat = p.get("category", "General")
        cslug = p.get("category_slug", "general")
        if cat not in categories:
            categories.append(cat)
            category_slugs[cat] = cslug

    cat_options_html = '<option value="all">All Categories</option>\n'
    for cat in categories:
        cat_options_html += f'          <option value="{category_slugs[cat]}">{cat}</option>\n'

    # Quick Jump Selector
    jump_options_html = '<option value="">Jump to Problem...</option>\n'
    for p in problems:
        pnum = p["number"]
        ptitle = p["title"]
        # truncate title if too long
        short_p = ptitle[:45] + "..." if len(ptitle) > 45 else ptitle
        jump_options_html += f'          <option value="p{pnum}">Problem {pnum:02d}: {short_p}</option>\n'

    # Render problem cards
    problem_cards_html = ""
    for p in problems:
        problem_cards_html += common.render_problem_card(p)

    # Technical SVG
    svg_code, svg_caption = CHAPTER_SVGS.get(cid, ("", ""))

    # Previous and Next chapter links
    prev_link = f'chapter{cid - 1}.html' if cid > 1 else 'index.html'
    prev_label = f'Ch {cid - 1}: {common.CHAPTERS[cid - 2]["short_title"]}' if cid > 1 else 'Cover Portal (Index)'
    next_link = f'chapter{cid + 1}.html' if cid < 8 else 'index.html'
    next_label = f'Ch {cid + 1}: {common.CHAPTERS[cid]["short_title"]}' if cid < 8 else 'Complete Review (Index)'

    tags_html = "".join([f'<span class="hero-tag">{tag}</span>' for tag in ch_info["tags"]])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{short_title} — Science of Materials | University of Tehran</title>
  <meta name="description" content="50 comprehensive practice problems with detailed step-by-step solutions for {title}. Science of Materials, University of Tehran.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Playfair+Display:ital,wght@0,500;0,700;1,400&family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  {MATHJAX_HEADER}
</head>
<body data-page-id="chapter{cid}">
  {common.generate_header(active_page=f"chapter{cid}", title=short_title)}

  <main class="master-wrapper">
    <!-- Chapter Breadcrumb -->
    <div style="font-family: var(--font-mono); font-size: 0.8rem; color: #94a3b8; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
      <a href="index.html" style="color: var(--gold); text-decoration: none;">Home (Cover)</a>
      <span>&rsaquo;</span>
      <span style="color: #cbd5e1;">Chapter {cid}</span>
    </div>

    <!-- Chapter Hero Section -->
    <section class="chapter-hero">
      <div class="hero-header-row">
        <div>
          <span class="chapter-num-badge">CHAPTER {cid:02d} OF 08</span>
          <h1 class="chapter-title" style="margin-top: 0.5rem;">{title}</h1>
        </div>
      </div>

      <p class="chapter-desc">
        {desc}
      </p>

      <div class="hero-tags">
        {tags_html}
      </div>

      <!-- High-Resolution Technical Vector Graphic -->
      <div class="hero-svg-container" style="margin-top: 2rem;">
        {svg_code}
        <div style="font-family: var(--font-mono); font-size: 0.78rem; color: #94a3b8; margin-top: 0.5rem; text-align: center;">
          Figure {cid}.1: {svg_caption}
        </div>
      </div>
    </section>

    <!-- Interactive Study Toolbar -->
    <section class="controls-bar">
      <div class="controls-left">
        <div class="search-box">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="problem-search-input" class="search-input" placeholder="Search equations, topics, terms...">
        </div>

        <select id="category-filter" class="filter-select">
          {cat_options_html}
        </select>

        <select id="diff-filter" class="filter-select">
          <option value="all">All Difficulties</option>
          <option value="fundamental">Fundamental</option>
          <option value="intermediate">Intermediate</option>
          <option value="advanced">Advanced</option>
        </select>

        <select id="jump-to-problem" class="filter-select">
          {jump_options_html}
        </select>
      </div>

      <div class="controls-right">
        <span id="visible-problem-count" class="visible-count">50 Problems Shown</span>
        <button id="btn-expand-all" class="btn-classic" title="Reveal all 50 solutions at once">Expand All</button>
        <button id="btn-collapse-all" class="btn-classic" title="Hide all solutions for active self-testing">Collapse All</button>
      </div>
    </section>

    <!-- Problems List Container -->
    <section class="problems-container" id="problems-list">
      {problem_cards_html}
    </section>

    <!-- Chapter Navigation Footer -->
    <nav class="chapter-pagination" style="display: flex; justify-content: space-between; align-items: center; margin: 3.5rem 0; padding-top: 1.5rem; border-top: 1px solid rgba(212, 175, 55, 0.3); flex-wrap: wrap; gap: 1rem;">
      <a href="{prev_link}" class="btn-classic" style="padding: 0.65rem 1.25rem;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        <span>Previous: {prev_label}</span>
      </a>

      <a href="index.html" class="btn-classic" style="padding: 0.65rem 1.25rem;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
        <span>All Chapters (Home)</span>
      </a>

      <a href="{next_link}" class="btn-primary" style="padding: 0.65rem 1.25rem;">
        <span>Next: {next_label}</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </a>
    </nav>
  </main>

  {common.generate_formula_modal()}
  {common.generate_footer()}

  <script src="js/main.js"></script>
</body>
</html>
"""
    out_file = os.path.join(BASE_DIR, filename)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully generated {out_file} (size: {len(html)} bytes)")

# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
def main():
    print("=================================================================")
    print("STARTING COMPLETE MASTER SITE GENERATION")
    print("University of Tehran | Department of Mechanical Engineering")
    print("Preparer: Sina Sharifi | Course: Science of Materials")
    print("=================================================================")

    # 1. Build index.html
    build_index()

    # 2. Build chapter1.html to chapter8.html
    for ch_info in common.CHAPTERS:
        build_chapter(ch_info)

    print("=================================================================")
    print("ALL 9 HTML FILES GENERATED SUCCESSFULLY!")
    print("Total problems compiled: 400 problems (50 problems per chapter)")
    print("=================================================================")

if __name__ == "__main__":
    main()
