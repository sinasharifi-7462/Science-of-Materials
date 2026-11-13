# generator/common.py
# ==============================================================================
# SCIENCE OF MATERIALS — MIDTERM STUDY SUITE GENERATOR
# University of Tehran | Department of Mechanical Engineering
# Author: Sina Sharifi | Instructor: Prof. A. Sadeghi
# ==============================================================================

CHAPTERS = [
    {
        "id": 1,
        "filename": "chapter1.html",
        "title": "Introduction to Materials Science & Engineering",
        "short_title": "Ch 1: Introduction to MSE",
        "desc": "The Materials Science and Engineering paradigm, the central Processing-Structure-Properties-Performance tetrahedron, broad classification of materials (metals, ceramics, polymers, composites, advanced materials), and Ashby property charts for engineering design.",
        "tags": ["Materials Paradigm", "MSE Tetrahedron", "Material Classes", "Ashby Charts", "Advanced Materials"],
        "count": 50
    },
    {
        "id": 2,
        "filename": "chapter2.html",
        "title": "Atomic Structure & Interatomic Bonding",
        "short_title": "Ch 2: Atomic Structure & Bonding",
        "desc": "Fundamental atomic physics, electronic configurations, quantum numbers, primary bonding (ionic, covalent, metallic), secondary bonding (van der Waals, hydrogen), and physical correlates of the net interatomic potential energy well.",
        "tags": ["Electronic Configuration", "Potential Energy Well", "Ionic & Covalent Bonding", "Metallic Bond", "Thermal Expansion"],
        "count": 50
    },
    {
        "id": 3,
        "filename": "chapter3.html",
        "title": "The Structure of Crystalline Solids",
        "short_title": "Ch 3: Crystalline Solids",
        "desc": "Lattice geometry, 7 crystal systems, 14 Bravais lattices, metallic crystal structures (FCC, BCC, HCP), APF and theoretical density, Miller indices for directions and planes, linear and planar densities, and X-ray diffraction (XRD / Bragg's Law).",
        "tags": ["FCC & BCC & HCP", "Theoretical Density", "Miller Indices", "Planar & Linear Density", "XRD & Bragg's Law"],
        "count": 50
    },
    {
        "id": 4,
        "filename": "chapter4.html",
        "title": "Imperfections in Solids",
        "short_title": "Ch 4: Imperfections in Solids",
        "desc": "Point defects (vacancies, self-interstitials, impurities), Hume-Rothery solubility rules, composition conversions (wt% vs at%), ceramic defect chemistry (Schottky and Frenkel pairs), line defects (edge and screw dislocations, Burgers vectors), interfacial defects, and ASTM grain size.",
        "tags": ["Vacancies & Arrhenius", "Hume-Rothery Rules", "Composition Conversions", "Dislocations & Burgers Vector", "ASTM Grain Size"],
        "count": 50
    },
    {
        "id": 5,
        "filename": "chapter5.html",
        "title": "Diffusion in Solids",
        "short_title": "Ch 5: Diffusion in Solids",
        "desc": "Atomic migration mechanisms (vacancy vs interstitial), steady-state diffusion and Fick's first law, non-steady-state diffusion and Fick's second law error function solutions, Arrhenius temperature dependence of diffusivity, carburization depth calculations, and structural factors.",
        "tags": ["Fick's 1st Law", "Fick's 2nd Law", "Error Function erf(z)", "Arrhenius Diffusivity", "Industrial Carburization"],
        "count": 50
    },
    {
        "id": 6,
        "filename": "chapter6.html",
        "title": "Mechanical Properties of Metals",
        "short_title": "Ch 6: Mechanical Properties",
        "desc": "Engineering stress and strain, Hooke's law, elastic moduli and Poisson's ratio, yielding and the 0.2% offset method, tensile strength, ductility, resilience, toughness, true stress and true strain, Hollomon strain hardening law, Schmid's law for single crystals, and hardness testing.",
        "tags": ["Hooke's Law & Moduli", "0.2% Offset Yielding", "True Stress-Strain", "Hollomon Relation", "Schmid's Law", "Hardness"],
        "count": 50
    },
    {
        "id": 7,
        "filename": "chapter7.html",
        "title": "Dislocations & Strengthening Mechanisms",
        "short_title": "Ch 7: Strengthening Mechanisms",
        "desc": "Principles of plastic deformation, critical shear stresses, the four classical strengthening mechanisms (Hall-Petch grain size refinement, solid solution strengthening, strain hardening/cold work, precipitation hardening/Orowan bowing), and the three stages of annealing (recovery, recrystallization, grain growth).",
        "tags": ["Hall-Petch Equation", "Solid Solution Strengthening", "Cold Work & Taylor Law", "Orowan Precipitation", "Annealing Kinetics"],
        "count": 50
    },
    {
        "id": 8,
        "filename": "chapter8.html",
        "title": "Failure: Fracture, Fatigue & Creep",
        "short_title": "Ch 8: Failure (Fracture, Fatigue, Creep)",
        "desc": "Mechanisms of ductile vs brittle fracture, Griffith criterion, stress concentration factor, Mode I stress intensity and fracture toughness (K_Ic), Charpy impact testing and the ductile-to-brittle transition (DBTT), cyclic fatigue (S-N curves, fatigue limits, mean stress effects), and high-temperature creep power laws.",
        "tags": ["Fracture Toughness K_Ic", "Griffith Criterion", "Charpy Impact & DBTT", "Fatigue S-N & Limits", "Larson-Miller Creep"],
        "count": 50
    }
]

def generate_header(active_page="index", title="Science of Materials — Study Suite", is_subfolder=False):
    prefix = "../" if is_subfolder else ""
    home_link = f"{prefix}index.html"
    logo_src = f"{prefix}assets/images/ut_mech_emblem.svg"

    nav_links_html = f"""
    <a href="{home_link}" class="nav-link {'active' if active_page == 'index' else ''}">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
      Home
    </a>
    """
    for ch in CHAPTERS:
        is_active = (active_page == f"chapter{ch['id']}")
        ch_link = ch['filename'] if is_subfolder else f"chapters/{ch['filename']}"
        nav_links_html += f"""
        <a href="{ch_link}" class="nav-link {'active' if is_active else ''}" title="{ch['title']}">
          Ch {ch['id']}
        </a>
        """

    return f"""
    <header class="site-header">
      <div class="nav-container">
        <a href="{home_link}" class="nav-brand">
          <div class="nav-logo-badge">
            <img src="{logo_src}" alt="University of Tehran Mechanical Engineering Crest">
          </div>
          <div class="nav-brand-text">
            <span class="nav-persian">دانشگاه تهران &bull; دانشکده مهندسی مکانیک</span>
            <h1>UNIVERSITY OF TEHRAN</h1>
            <p>Department of Mechanical Engineering &bull; Science of Materials</p>
          </div>
        </a>

        <nav class="nav-links">
          {nav_links_html}
        </nav>

        <div class="nav-actions">
          <button id="btn-open-formula-sheet" class="btn-classic" title="Open Master Formula Reference">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            Formula Sheet
          </button>
          <span id="mastered-count-badge" class="chapter-num-badge" style="display:inline-block; font-size:0.75rem;">
            0 Mastered
          </span>
        </div>
      </div>
    </header>
    """

def generate_footer(is_subfolder=False):
    prefix = "../" if is_subfolder else ""
    logo_src = f"{prefix}assets/images/ut_mech_emblem.svg"
    fanni_src = f"{prefix}assets/images/ut_engineering_logo.svg"

    return f"""
    <footer class="site-footer">
      <div class="master-wrapper" style="padding-bottom: 0;">
        <div style="display: flex; justify-content: center; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem;">
          <div class="footer-emblem-badge">
            <img src="{logo_src}" alt="UT Mechanical Engineering Crest">
          </div>
          <div class="footer-emblem-badge" style="padding: 4px;">
            <img src="{fanni_src}" alt="College of Engineering Emblem">
          </div>
        </div>

        <p class="footer-persian">دانشگاه تهران &bull; پردیس دانشکده‌های فنی &bull; دانشکده مهندسی مکانیک</p>
        <p class="footer-gold-text">UNIVERSITY OF TEHRAN &bull; DEPARTMENT OF MECHANICAL ENGINEERING</p>
        
        <div class="gold-hairline" style="margin: 0.85rem auto;"></div>

        <p style="color: #cbd5e1; font-size: 0.95rem;">
          Course: <strong>Science of Materials</strong> (Undergraduate Midterm Mastery Suite) &bull; Instructor: <strong>Prof. A. Sadeghi</strong>
        </p>
        <p style="font-size: 0.88rem; color: #facc15; margin-top: 0.35rem;">
          Meticulously Prepared &amp; Synthesized by Teaching Assistant <strong>Sina Sharifi</strong>
        </p>
        <p style="font-size: 0.78rem; color: #94a3b8; margin-top: 1.25rem;">
          Designed for academic excellence &bull; Formatted with LaTeX Math &bull; High-Contrast Classical Edition
        </p>
      </div>
    </footer>
    <button id="btn-back-top" class="btn-back-top" title="Back to top">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"></polyline></svg>
    </button>
    """

def generate_formula_modal():
    return """
    <div id="formula-modal" class="modal-overlay">
      <div class="modal-card">
        <div class="modal-header">
          <h3>Master Formula Compendium &amp; Physical Constants (Chapters 1 &ndash; 8)</h3>
          <button id="btn-close-formula-modal" class="modal-close-btn">&times;</button>
        </div>
        <div class="modal-body">
          <div style="background: rgba(30, 58, 138, 0.3); border: 1.5px solid rgba(56, 189, 248, 0.5); padding: 1rem; border-radius: 4px; margin-bottom: 1.25rem; font-size: 0.92rem; color: #bae6fd;">
            <strong style="color: #facc15; font-size: 1rem;">Fundamental Physical Constants:</strong><br>
            Avogadro's Number: \\(N_A = 6.022 \\times 10^{23} \\text{ atoms/mol}\\) &bull;
            Boltzmann's Constant: \\(k_B = 1.381 \\times 10^{-23} \\text{ J/K} = 8.617 \\times 10^{-5} \\text{ eV/K}\\)<br>
            Universal Gas Constant: \\(R = 8.314 \\text{ J/mol}\\cdot\\text{K}\\) &bull;
            Electron Charge: \\(e = 1.602 \\times 10^{-19} \\text{ C}\\) &bull;
            \\(1 \\text{ eV} = 1.602 \\times 10^{-19} \\text{ J}\\)
          </div>

          <table class="formula-table">
            <thead>
              <tr>
                <th style="width: 20%;">Chapter / Topic</th>
                <th style="width: 45%;">Governing Equation &amp; Relation</th>
                <th style="width: 35%;">Parameter Definitions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Ch 1: Ashby Indices</strong></td>
                <td>$$M_1 = \\frac{\\sigma_y}{\\rho}, \\quad M_2 = \\frac{E^{1/2}}{\\rho}, \\quad M_3 = \\frac{\\sigma_y^{2/3}}{\\rho}$$</td>
                <td>Lightweight tension tie-rod (\\(M_1\\)), stiff beam (\\(M_2\\)), strong beam (\\(M_3\\))</td>
              </tr>
              <tr>
                <td><strong>Ch 1: Composite Moduli</strong></td>
                <td>$$E_{cl} = V_f E_f + V_m E_m, \\quad \\frac{1}{E_{ct}} = \\frac{V_f}{E_f} + \\frac{V_m}{E_m}$$</td>
                <td>Voigt isostrain (longitudinal) and Reuss isostress (transverse) Rule of Mixtures</td>
              </tr>
              <tr>
                <td><strong>Ch 2: Potential Energy Well</strong></td>
                <td>$$E_N(r) = -\\frac{A}{r^m} + \\frac{B}{r^n}, \\quad F_N(r) = \\frac{dE_N}{dr}$$</td>
                <td>Attractive vs repulsive potential; equilibrium spacing \\(r_0\\) at \\(F_N(r_0) = 0\\)</td>
              </tr>
              <tr>
                <td><strong>Ch 3: Theoretical Density</strong></td>
                <td>$$\\rho = \\frac{n \\cdot A}{V_c \\cdot N_A}$$</td>
                <td>\\(n\\): atoms/cell; \\(A\\): atomic weight (g/mol); \\(V_c\\): cell volume</td>
              </tr>
              <tr>
                <td><strong>Ch 3: Crystal Geometry</strong></td>
                <td>BCC: \\(a = \\frac{4R}{\\sqrt{3}}\\), \\(\\text{APF} = 0.68\\)<br>FCC: \\(a = 2\\sqrt{2}R\\), \\(\\text{APF} = 0.74\\)</td>
                <td>\\(R\\): atomic radius; \\(a\\): cubic lattice parameter</td>
              </tr>
              <tr>
                <td><strong>Ch 3: Bragg's Law (XRD)</strong></td>
                <td>$$n\\lambda = 2 d_{hkl} \\sin\\theta, \\quad d_{hkl} = \\frac{a}{\\sqrt{h^2+k^2+l^2}}$$</td>
                <td>\\(\\lambda\\): X-ray wavelength; \\(d_{hkl}\\): interplanar spacing; \\(\\theta\\): Bragg angle</td>
              </tr>
              <tr>
                <td><strong>Ch 4: Equilibrium Vacancies</strong></td>
                <td>$$N_v = N \\exp\\left(-\\frac{Q_v}{k_B T}\\right)$$</td>
                <td>\\(N\\): total atomic sites; \\(Q_v\\): vacancy formation energy</td>
              </tr>
              <tr>
                <td><strong>Ch 4: ASTM Grain Size</strong></td>
                <td>$$N = 2^{n - 1}$$</td>
                <td>\\(N\\): grains per square inch at 100\\(\\times\\) magnification; \\(n\\): ASTM number</td>
              </tr>
              <tr>
                <td><strong>Ch 5: Fick's 1st Law</strong></td>
                <td>$$J = -D \\frac{dC}{dx}$$</td>
                <td>\\(J\\): diffusion flux (\\(\\text{kg/m}^2\\cdot\\text{s}\\)); \\(D\\): diffusion coefficient</td>
              </tr>
              <tr>
                <td><strong>Ch 5: Fick's 2nd Law</strong></td>
                <td>$$\\frac{C_x - C_0}{C_s - C_0} = 1 - \\text{erf}\\left(\\frac{x}{2\\sqrt{Dt}}\\right)$$</td>
                <td>Semi-infinite solid constant surface concentration carburization/decarburization</td>
              </tr>
              <tr>
                <td><strong>Ch 5: Arrhenius Diffusivity</strong></td>
                <td>$$D = D_0 \\exp\\left(-\\frac{Q_d}{RT}\\right)$$</td>
                <td>\\(D_0\\): pre-exponential; \\(Q_d\\): activation energy for diffusion</td>
              </tr>
              <tr>
                <td><strong>Ch 6: Hooke's Law &amp; Moduli</strong></td>
                <td>$$\\sigma = E\\varepsilon, \\quad \\tau = G\\gamma, \\quad G = \\frac{E}{2(1 + \\nu)}$$</td>
                <td>\\(E\\): Young's modulus; \\(G\\): shear modulus; \\(\\nu\\): Poisson's ratio</td>
              </tr>
              <tr>
                <td><strong>Ch 6: Modulus of Resilience</strong></td>
                <td>$$U_r = \\frac{\\sigma_y^2}{2E}$$</td>
                <td>Elastic strain energy storage capacity per unit volume up to yielding</td>
              </tr>
              <tr>
                <td><strong>Ch 6: Schmid's Law</strong></td>
                <td>$$\\tau_R = \\sigma \\cos\\phi \\cos\\lambda \\le \\tau_{\\text{CRSS}}$$</td>
                <td>\\(\\phi\\): normal to slip plane; \\(\\lambda\\): slip direction angle</td>
              </tr>
              <tr>
                <td><strong>Ch 7: Hall-Petch Law</strong></td>
                <td>$$\\sigma_y = \\sigma_0 + k_y d^{-1/2}$$</td>
                <td>\\(\\sigma_0\\): friction stress; \\(k_y\\): unpinning coefficient; \\(d\\): average grain diameter</td>
              </tr>
              <tr>
                <td><strong>Ch 7: Cold Work &amp; Orowan</strong></td>
                <td>$$\\%\\text{CW} = \\frac{A_0 - A_d}{A_0} \\times 100\\%, \\quad \\Delta\\tau = \\frac{G b}{L}$$</td>
                <td>Dislocation density multiplication &amp; precipitate bowing resistance</td>
              </tr>
              <tr>
                <td><strong>Ch 8: Fracture Toughness</strong></td>
                <td>$$K = Y \\sigma \\sqrt{\\pi a} \\le K_{Ic}$$</td>
                <td>\\(K_{Ic}\\): plane strain fracture toughness; \\(Y\\): dimensionless crack geometry factor</td>
              </tr>
              <tr>
                <td><strong>Ch 8: Larson-Miller Creep</strong></td>
                <td>$$P = T \\left(20 + \\log_{10} t_r\\right)$$</td>
                <td>\\(T\\): temperature in Kelvin; \\(t_r\\): creep rupture time in hours</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    """

def render_problem_card(prob):
    diff_class = {
        "Fundamental": "diff-fundamental",
        "Intermediate": "diff-intermediate",
        "Advanced": "diff-advanced"
    }.get(prob.get("difficulty", "Intermediate"), "diff-intermediate")

    return f"""
    <article class="problem-card" id="p{prob['number']}" data-category="{prob.get('category_slug', 'general')}" data-difficulty="{prob.get('difficulty', 'Intermediate').lower()}">
      <div class="problem-header">
        <div class="problem-num-group">
          <span class="problem-badge">Problem {prob['number']:02d}</span>
          <span class="problem-category">{prob.get('category', 'Theory & Application')}</span>
          <span class="difficulty-badge {diff_class}">{prob.get('difficulty', 'Intermediate')}</span>
        </div>
        <div class="problem-actions-top">
          <button class="btn-bookmark" data-problem-id="p{prob['number']}" title="Mark as Mastered in your local browser session">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
            Mark Mastered
          </button>
        </div>
      </div>

      <h4 class="problem-card-title">
        {prob['title']}
      </h4>

      <div class="problem-statement">
        {prob['statement']}
      </div>

      <div class="solution-toggle-bar">
        <button class="btn-toggle-solution" aria-expanded="false">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          Show Detailed Solution
        </button>
      </div>

      <div class="solution-container">
        <div class="solution-heading">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          Step-by-Step Technical Solution &amp; Analysis
        </div>
        
        {prob['solution']}
      </div>
    </article>
    """
