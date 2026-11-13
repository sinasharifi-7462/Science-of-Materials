# generator/build_site.py
# ==============================================================================
# SCIENCE OF MATERIALS — MASTER SITE BUILDER & PACKAGER
# Department of Mechanical Engineering | University of Tehran
# Preparer: Sina Sharifi (TA) | Instructor: Prof. A. Sadeghi
# ==============================================================================

import os
import sys
import shutil
import zipfile

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
    1: (svg_assets.svg_tetrahedron(), "Figure 1.1: The MSE Paradigm Tetrahedron & Life-Cycle Octahedron"),
    2: (svg_assets.svg_potential_well(), "Figure 2.1: Interatomic Potential Energy Well, Bonding Energy & Thermal Expansion"),
    3: (svg_assets.svg_crystal_unit_cells(), "Figure 3.1: 3D Metallic Unit Cells (BCC, FCC, HCP) & Atomic Packing Factors"),
    4: (svg_assets.svg_point_defects(), "Figure 4.1: Atlas of Point Defects (Vacancies, Solutes, Interstitials) & Hume-Rothery Rules"),
    5: (svg_assets.svg_diffusion_profiles(), "Figure 5.1: Fick's Second Law Carburization Concentration Depth Profiles C(x,t)"),
    6: (svg_assets.svg_stress_strain_curve(), "Figure 6.1: Engineering vs True Stress-Strain Curve, Yield Offset & Toughness"),
    7: (svg_assets.svg_hall_petch(), "Figure 7.1: Hall-Petch Grain Boundary Dislocation Pile-Up & Strengthening Law"),
    8: (svg_assets.svg_charpy_dbtt(), "Figure 8.1: Charpy V-Notch Impact DBTT Transition for BCC vs FCC Alloys"),
}

def get_mathjax_header(is_subfolder=False):
    prefix = "../" if is_subfolder else ""
    return f"""
  <!-- MathJax 3 Configuration for High-Fidelity Technical Rendering (100% Offline + CDN Fallback) -->
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        processEnvironments: true
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }},
      startup: {{
        pageReady: () => {{
          return MathJax.startup.defaultPageReady().then(() => {{
            console.log('MathJax initial technical typesetting ready');
          }});
        }}
      }}
    }};
  </script>
  <script src="{prefix}js/mathjax.js" onerror="this.onerror=null;this.src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js';"></script>
"""

# ==============================================================================
# BUILD INDEX.HTML (THE MASTER PORTAL & GRAND ACADEMIC COVER PAGE)
# ==============================================================================
def build_index():
    print("Building root index.html (Master Cover Portal)...")

    chapter_cards_html = ""
    for ch in common.CHAPTERS:
        cid = ch["id"]
        svg_code, svg_caption = CHAPTER_SVGS.get(cid, ("", ""))
        tags_html = "".join([f'<span class="hero-tag">{tag}</span>' for tag in ch["tags"]])
        ch_link = f"chapters/{ch['filename']}"

        chapter_cards_html += f"""
        <article class="chapter-card">
          <div class="card-hero-preview">
            {svg_code}
          </div>
          <div class="card-content">
            <div class="card-meta">
              <span class="chapter-num-badge">CHAPTER {cid:02d}</span>
              <span class="problem-count-badge">50 Problems &bull; 100% Solutions</span>
            </div>
            <h3 class="card-title">
              <a href="{ch_link}">{ch['title']}</a>
            </h3>
            <p class="card-desc">
              {ch['desc']}
            </p>
            <div class="card-tags">
              {tags_html}
            </div>
            <a href="{ch_link}" class="btn-primary" style="width: 100%; justify-content: center;">
              <span>Study Chapter {cid} (50 Problems)</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
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
  <meta name="description" content="Comprehensive 400-problem midterm examination mastery suite for the Science of Materials course at the University of Tehran, Department of Mechanical Engineering. Prepared by Sina Sharifi under Prof. A. Sadeghi.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;500;600;700&family=Vazirmatn:wght@500;700&display=swap" rel="stylesheet">
  {get_mathjax_header(is_subfolder=False)}
</head>
<body data-page-id="index">
  {common.generate_header(active_page="index", title="Science of Materials — University of Tehran", is_subfolder=False)}

  <main class="master-wrapper">
    <!-- Grand Academic Cover Masthead with Ruled Frames -->
    <section class="cover-hero-frame">
      <!-- Classical Corner Flourishes -->
      <div class="corner-flourish corner-tl"></div>
      <div class="corner-flourish corner-tr"></div>
      <div class="corner-flourish corner-bl"></div>
      <div class="corner-flourish corner-br"></div>

      <!-- Institutional Crest & Logo Row -->
      <div class="emblem-row">
        <div class="hero-emblem-badge" title="Department of Mechanical Engineering Emblem">
          <img src="assets/images/ut_mech_emblem.svg" alt="Department of Mechanical Engineering Emblem">
        </div>
        <div class="hero-emblem-badge" title="College of Engineering Official Emblem">
          <img src="assets/images/ut_engineering_logo.svg" alt="College of Engineering Official Emblem">
        </div>
      </div>

      <p class="institution-header-persian">دانشگاه تهران &bull; پردیس دانشکده‌های فنی &bull; دانشکده مهندسی مکانیک</p>
      <p class="cover-pretitle">UNIVERSITY OF TEHRAN &bull; DEPARTMENT OF MECHANICAL ENGINEERING</p>

      <h1 class="cover-main-title">SCIENCE OF MATERIALS</h1>
      <p class="cover-persian-subtitle">مبانی علم و مهندسی مواد — دوره کارشناسی مهندسی مکانیک</p>

      <div class="gold-hairline"></div>

      <p class="cover-subtitle">
        Comprehensive 400-Problem Midterm Examination Study &amp; Mastery Suite
      </p>

      <!-- Formal Academic Attribution Plaque -->
      <div class="attribution-box-formal">
        <div class="attribution-item">
          Prepared &amp; Formulated with Meticulous Technical Rigor by Teaching Assistant <strong>Sina Sharifi</strong>
        </div>
        <div class="attribution-item">
          Under the Academic Supervision of <strong>Prof. A. Sadeghi</strong>
        </div>
        <div class="attribution-scope">
          Complete Curricular Coverage: Chapters 1 through 8 (Up to Phase Diagrams) &bull; 100% Fully Worked Solutions &bull; Technical Vector Compendium
        </div>
      </div>

      <!-- Quick Action Buttons -->
      <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2rem;">
        <a href="#chapters-directory" class="btn-primary" style="padding: 0.85rem 1.75rem; font-size: 1rem;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          Explore All 8 Chapters (400 Solved Problems)
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
          <div class="stat-lbl">Solved Practice Problems</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">50</div>
          <div class="stat-lbl">Problems Per Chapter</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">100%</div>
          <div class="stat-lbl">Step-by-Step Solutions</div>
        </div>
      </div>
    </section>

    <!-- Study Guide & Examination Protocol -->
    <section class="instructions-card">
      <h2>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#facc15" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        Examination Preparation Protocol &bull; How to Maximize Midterm Performance
      </h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; color: #cbd5e1; font-size: 0.98rem; line-height: 1.7;">
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">1. Active Recall Self-Testing:</strong>
          Every problem has its full derivation and boxed final answer hidden by default. Always attempt the derivation independently on paper before revealing the solution.
        </div>
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">2. Categorized Topic Targeting:</strong>
          Filter problems by category (e.g. Miller Indices, Fick's Laws, Schmid's Law, Hall-Petch, LEFM) to target specific areas of the Callister textbook.
        </div>
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">3. Local Progress Tracking:</strong>
          Click <em>"Mark Mastered"</em> on any problem you conquer. Your progress is saved in your browser and tallies in the navigation header.
        </div>
        <div>
          <strong style="color: #ffffff; display: block; margin-bottom: 0.35rem;">4. Formula Sheet Modal:</strong>
          Click <em>"Formula Sheet"</em> at any time to consult the master compendium of governing equations, physical constants, and unit definitions.
        </div>
      </div>
    </section>

    <div class="double-academic-line"></div>

    <!-- Master Chapters Directory -->
    <section id="chapters-directory">
      <div style="text-align: center; margin-bottom: 2.75rem;">
        <p style="font-family: var(--font-mono); color: var(--accent-gold-bright); font-size: 0.88rem; letter-spacing: 0.15em; text-transform: uppercase;">Midterm Examination Syllabus</p>
        <h2 style="font-family: var(--font-serif); font-size: 2.25rem; color: #ffffff; margin-top: 0.25rem;">The Eight Curricular Chapters</h2>
        <div class="gold-hairline"></div>
      </div>

      <div class="chapters-grid">
        {chapter_cards_html}
      </div>
    </section>
  </main>

  {common.generate_formula_modal()}
  {common.generate_footer(is_subfolder=False)}

  <script src="js/main.js"></script>
</body>
</html>
"""
    out_file = os.path.join(BASE_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully generated root {out_file} (size: {len(html)} bytes)")

# ==============================================================================
# BUILD CHAPTER HTML PAGES INSIDE CHAPTERS/ DIRECTORY
# ==============================================================================
def build_chapter(ch_info):
    cid = ch_info["id"]
    filename = ch_info["filename"]
    title = ch_info["title"]
    short_title = ch_info["short_title"]
    desc = ch_info["desc"]
    problems = DATASETS.get(cid, [])

    chapters_dir = os.path.join(BASE_DIR, "chapters")
    os.makedirs(chapters_dir, exist_ok=True)
    out_file = os.path.join(chapters_dir, filename)

    print(f"Building chapters/{filename} (Chapter {cid} - {len(problems)} problems)...")

    # Categories for filter
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

    # Jump options
    jump_options_html = '<option value="">Jump to Problem...</option>\n'
    for p in problems:
        pnum = p["number"]
        ptitle = p["title"]
        short_p = ptitle[:45] + "..." if len(ptitle) > 45 else ptitle
        jump_options_html += f'          <option value="p{pnum}">Problem {pnum:02d}: {short_p}</option>\n'

    # Render problem cards
    problem_cards_html = ""
    for p in problems:
        problem_cards_html += common.render_problem_card(p)

    # Technical SVG
    svg_code, svg_caption = CHAPTER_SVGS.get(cid, ("", ""))

    # Sibling navigation
    prev_link = f'chapter{cid - 1}.html' if cid > 1 else '../index.html'
    prev_label = f'Ch {cid - 1}: {common.CHAPTERS[cid - 2]["short_title"]}' if cid > 1 else 'Home (Cover Portal)'
    next_link = f'chapter{cid + 1}.html' if cid < 8 else '../index.html'
    next_label = f'Ch {cid + 1}: {common.CHAPTERS[cid]["short_title"]}' if cid < 8 else 'Final Review (Home)'

    tags_html = "".join([f'<span class="hero-tag">{tag}</span>' for tag in ch_info["tags"]])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{short_title} — Science of Materials | University of Tehran</title>
  <meta name="description" content="50 comprehensive practice problems with detailed step-by-step solutions for {title}. Science of Materials, University of Tehran. Prepared by Sina Sharifi.">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;500;600;700&family=Vazirmatn:wght@500;700&display=swap" rel="stylesheet">
  {get_mathjax_header(is_subfolder=True)}
</head>
<body data-page-id="chapter{cid}">
  {common.generate_header(active_page=f"chapter{cid}", title=short_title, is_subfolder=True)}

  <main class="master-wrapper">
    <!-- Chapter Breadcrumbs -->
    <div style="font-family: var(--font-mono); font-size: 0.85rem; color: #94a3b8; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
      <a href="../index.html" style="color: var(--accent-gold-bright); text-decoration: none; font-weight: 600;">Home (Cover Portal)</a>
      <span style="color: #64748b;">&rsaquo;</span>
      <span style="color: #64748b;">Chapters</span>
      <span style="color: #64748b;">&rsaquo;</span>
      <span style="color: #ffffff; font-weight: 600;">Chapter {cid:02d}</span>
    </div>

    <!-- Chapter Hero Section -->
    <section class="chapter-hero">
      <div class="hero-header-row">
        <div>
          <span class="chapter-num-badge">CHAPTER {cid:02d} OF 08</span>
          <h1 class="chapter-title" style="margin-top: 0.65rem;">{title}</h1>
        </div>
      </div>

      <p class="chapter-desc">
        {desc}
      </p>

      <div class="card-tags" style="border: none; padding: 0; margin-bottom: 1.75rem;">
        {tags_html}
      </div>

      <!-- High-Resolution Technical Vector Graphic Showcase -->
      <div class="chapter-diagram-showcase">
        <div class="diagram-header-strip">
          <span>{svg_caption}</span>
          <span style="color: var(--accent-cyan-light);">Engineering Vector Schematic</span>
        </div>
        <div class="diagram-canvas">
          {svg_code}
        </div>
      </div>
    </section>

    <!-- Interactive Study Toolbar -->
    <section class="controls-bar">
      <div class="search-box-wrapper">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="problem-search-input" placeholder="Search equations, formulas, topics (e.g. Miller, Fick, yield)...">
      </div>

      <div class="filters-group">
        <select id="category-filter">
          {cat_options_html}
        </select>

        <select id="diff-filter">
          <option value="all">All Difficulties</option>
          <option value="fundamental">Fundamental</option>
          <option value="intermediate">Intermediate</option>
          <option value="advanced">Advanced</option>
        </select>

        <select id="jump-to-problem">
          {jump_options_html}
        </select>

        <span id="visible-problem-count" class="chapter-num-badge" style="font-size: 0.8rem;">50 Problems Shown</span>
        <button id="btn-expand-all" class="btn-classic">Expand All</button>
        <button id="btn-collapse-all" class="btn-classic">Collapse All</button>
      </div>
    </section>

    <!-- Problems List Container -->
    <section class="problems-stream" id="problems-list">
      {problem_cards_html}
    </section>

    <!-- Chapter Navigation Footer Strip -->
    <nav style="display: flex; justify-content: space-between; align-items: center; margin: 4rem 0 2rem; padding-top: 1.75rem; border-top: var(--border-double); flex-wrap: wrap; gap: 1rem;">
      <a href="{prev_link}" class="btn-classic" style="padding: 0.75rem 1.35rem;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
        <span>Previous: {prev_label}</span>
      </a>

      <a href="../index.html" class="btn-classic" style="padding: 0.75rem 1.35rem;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
        <span>Main Portal (Cover)</span>
      </a>

      <a href="{next_link}" class="btn-primary" style="padding: 0.75rem 1.35rem;">
        <span>Next: {next_label}</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </a>
    </nav>
  </main>

  {common.generate_formula_modal()}
  {common.generate_footer(is_subfolder=True)}

  <script src="../js/main.js"></script>
</body>
</html>
"""
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully generated {out_file} (size: {len(html)} bytes)")

# ==============================================================================
# SYNC AND PACKAGE FOR CLOUDFLARE DEPLOYMENT
# ==============================================================================
def sync_cloudflare():
    print("Synchronizing website_for_cloudflare deployment directory...")
    cf_dir = os.path.join(BASE_DIR, "website_for_cloudflare")
    cf_chapters = os.path.join(cf_dir, "chapters")
    cf_css = os.path.join(cf_dir, "css")
    cf_js = os.path.join(cf_dir, "js")
    cf_assets = os.path.join(cf_dir, "assets", "images")

    os.makedirs(cf_chapters, exist_ok=True)
    os.makedirs(cf_css, exist_ok=True)
    os.makedirs(cf_js, exist_ok=True)
    os.makedirs(cf_assets, exist_ok=True)

    # 1. Copy root index.html
    shutil.copy2(os.path.join(BASE_DIR, "index.html"), os.path.join(cf_dir, "index.html"))

    # 2. Copy chapters/*.html
    for i in range(1, 9):
        src_ch = os.path.join(BASE_DIR, "chapters", f"chapter{i}.html")
        dst_ch = os.path.join(cf_chapters, f"chapter{i}.html")
        shutil.copy2(src_ch, dst_ch)

    # 3. Copy CSS and JS
    shutil.copy2(os.path.join(BASE_DIR, "css", "style.css"), os.path.join(cf_css, "style.css"))
    shutil.copy2(os.path.join(BASE_DIR, "js", "main.js"), os.path.join(cf_js, "main.js"))
    shutil.copy2(os.path.join(BASE_DIR, "js", "mathjax.js"), os.path.join(cf_js, "mathjax.js"))

    # 4. Copy Assets/images
    src_assets = os.path.join(BASE_DIR, "assets", "images")
    if os.path.exists(src_assets):
        for f in os.listdir(src_assets):
            sf = os.path.join(src_assets, f)
            if os.path.isfile(sf):
                shutil.copy2(sf, os.path.join(cf_assets, f))

    # 5. Remove any old root chapter files inside website_for_cloudflare if present
    for i in range(1, 9):
        old_cf_ch = os.path.join(cf_dir, f"chapter{i}.html")
        if os.path.exists(old_cf_ch):
            os.remove(old_cf_ch)

    # 6. Recreate zip archive
    zip_path = os.path.join(BASE_DIR, "website_for_cloudflare.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(cf_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, cf_dir)
                zipf.write(file_path, arcname)

    print(f"Successfully packaged {zip_path} (size: {os.path.getsize(zip_path):,} bytes)")

# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================
def main():
    print("=================================================================")
    print("STARTING COMPLETE MASTER SITE REBUILD (CLASSICAL ACADEMIC EDITION)")
    print("University of Tehran | Department of Mechanical Engineering")
    print("Preparer: Sina Sharifi | Course: Science of Materials")
    print("=================================================================")

    # 1. Export all standalone SVGs
    svg_assets.export_all_svgs(os.path.join(BASE_DIR, "assets", "images"))

    # 2. Build root index.html
    build_index()

    # 3. Build chapters/chapter1.html to chapters/chapter8.html
    for ch_info in common.CHAPTERS:
        build_chapter(ch_info)

    # 4. Remove obsolete old root chapter files if they exist in BASE_DIR
    for i in range(1, 9):
        old_root_ch = os.path.join(BASE_DIR, f"chapter{i}.html")
        if os.path.exists(old_root_ch):
            os.remove(old_root_ch)
            print(f"Removed legacy root file: {old_root_ch}")

    # 5. Sync and package Cloudflare assets
    sync_cloudflare()

    print("=================================================================")
    print("SITE GENERATION & PACKAGING COMPLETED WITH 100% SUCCESS!")
    print("=================================================================")

if __name__ == "__main__":
    main()
