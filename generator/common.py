# ==============================================================================
# SCIENCE OF MATERIALS — MIDTERM STUDY SUITE GENERATOR
# University of Tehran | Department of Mechanical Engineering
# Common Templates, SVG Generators, and Component Builders
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

# University of Tehran stylized vector seal
SVG_UT_SEAL = """
<svg width="68" height="68" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="47" stroke="#d4af37" stroke-width="2" stroke-dasharray="2 2" opacity="0.8"/>
  <circle cx="50" cy="50" r="43" stroke="#d4af37" stroke-width="1.5"/>
  <circle cx="50" cy="50" r="38" fill="#0d1b3e" stroke="rgba(212, 175, 55, 0.4)" stroke-width="1"/>
  <!-- Central Traditional Emblem Motif -->
  <path d="M50 16 L56 32 L72 32 L59 42 L64 58 L50 48 L36 58 L41 42 L28 32 L44 32 Z" fill="rgba(212, 175, 55, 0.15)" stroke="#d4af37" stroke-width="1"/>
  <!-- Open Book of Knowledge / Engineering -->
  <path d="M50 48 L38 42 C34 40 30 43 30 48 L30 68 C34 65 42 65 50 69 C58 65 66 65 70 68 L70 48 C70 43 66 40 62 42 Z" fill="#14244d" stroke="#d4af37" stroke-width="1.5"/>
  <path d="M50 48 L50 69" stroke="#d4af37" stroke-width="1.5"/>
  <!-- Mechanical Gear Accents -->
  <circle cx="50" cy="50" r="4" fill="#d4af37"/>
  <!-- Laurel Wreath Curves -->
  <path d="M22 56 C20 40 28 26 42 20" stroke="#d4af37" stroke-width="1.2" stroke-linecap="round"/>
  <path d="M78 56 C80 40 72 26 58 20" stroke="#d4af37" stroke-width="1.2" stroke-linecap="round"/>
</svg>
"""

def generate_header(active_page="index", title="Science of Materials — Study Suite"):
    nav_links_html = f"""
    <a href="index.html" class="nav-link {'active' if active_page == 'index' else ''}">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
      Home
    </a>
    """
    for ch in CHAPTERS:
        is_active = (active_page == f"chapter{ch['id']}")
        nav_links_html += f"""
        <a href="{ch['filename']}" class="nav-link {'active' if is_active else ''}" title="{ch['title']}">
          Ch {ch['id']}
        </a>
        """

    return f"""
    <header class="site-header">
      <div class="nav-container">
        <a href="index.html" class="nav-brand">
          <div class="nav-logo-badge">
            <svg width="28" height="28" viewBox="0 0 100 100" fill="none">
              <circle cx="50" cy="50" r="44" stroke="#d4af37" stroke-width="3"/>
              <path d="M50 20 L60 40 L80 40 L65 52 L70 72 L50 60 L30 72 L35 52 L20 40 L40 40 Z" fill="none" stroke="#d4af37" stroke-width="2"/>
            </svg>
          </div>
          <div class="nav-brand-text">
            <h1>UNIVERSITY OF TEHRAN</h1>
            <p>Faculty of Mechanical Engineering | Science of Materials</p>
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

def generate_footer():
    return """
    <footer class="site-footer">
      <div class="master-wrapper" style="padding-bottom: 0;">
        <div class="university-crest" style="margin-bottom: 1rem;">
          """ + SVG_UT_SEAL + """
        </div>
        <p class="footer-gold-text">UNIVERSITY OF TEHRAN</p>
        <p>Faculty of Mechanical Engineering &bull; Department of Materials & Manufacturing</p>
        <p>Course: <strong>Science of Materials</strong> (Undergraduate Curriculum) &bull; Instructor: <strong>Prof. A. Sadeghi</strong></p>
        <p style="margin-top: 0.75rem; color: #cbd5e1;">Comprehensive 400-Problem Midterm Exam Mastery Suite</p>
        <p style="font-size: 0.8rem; color: #94a3b8;">Authored, Curated & Synthesized by Teaching Assistant <strong>Sina Sharifi</strong></p>
        <p style="font-size: 0.75rem; color: #64748b; margin-top: 1.5rem;">Designed for academic excellence &bull; Formatted with LaTeX Math &bull; Dark Blue Classic Edition</p>
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
          <h3>Master Formula Compendium & Physical Constants (Ch 1 – 8)</h3>
          <button id="btn-close-formula-modal" class="modal-close-btn">&times;</button>
        </div>
        <div class="modal-body">
          <div style="background: rgba(30, 58, 138, 0.25); border: 1px solid rgba(56, 189, 248, 0.3); padding: 0.85rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.85rem; color: #bae6fd;">
            <strong>Fundamental Physical Constants:</strong><br>
            Avogadro's Number: \\(N_A = 6.022 \\times 10^{23} \\text{ atoms/mol}\\) &bull;
            Boltzmann's Constant: \\(k = 1.38 \\times 10^{-23} \\text{ J/atom}\\cdot\\text{K} = 8.62 \\times 10^{-5} \\text{ eV/atom}\\cdot\\text{K}\\)<br>
            Universal Gas Constant: \\(R = 8.314 \\text{ J/mol}\\cdot\\text{K}\\) &bull;
            Elementary Charge: \\(e = 1.602 \\times 10^{-19} \\text{ C}\\) &bull;
            1 eV = \\(1.602 \\times 10^{-19} \\text{ J}\\)
          </div>

          <table class="formula-table">
            <thead>
              <tr>
                <th style="width: 25%;">Domain / Law</th>
                <th style="width: 45%;">Governing Mathematical Equation</th>
                <th style="width: 30%;">Key Variables & Units</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Theoretical Crystal Density</strong></td>
                <td>$$\\rho = \\frac{n \\cdot A}{V_c \\cdot N_A}$$</td>
                <td>\\(n\\): atoms/cell; \\(A\\): g/mol; \\(V_c\\): cell volume (\\(\\text{cm}^3\\)); \\(\\rho\\): \\(\\text{g/cm}^3\\)</td>
              </tr>
              <tr>
                <td><strong>Lattice Constants & APF</strong></td>
                <td>
                  BCC: \\(a = \\frac{4R}{\\sqrt{3}}\\), \\(\\text{APF} = 0.68\\), \\(n=2\\)<br>
                  FCC: \\(a = 2\\sqrt{2}R\\), \\(\\text{APF} = 0.74\\), \\(n=4\\)
                </td>
                <td>\\(R\\): atomic radius; \\(a\\): lattice parameter; \\(\\text{APF} = \\frac{n(4/3\\pi R^3)}{V_c}\\)</td>
              </tr>
              <tr>
                <td><strong>Cubic Interplanar Spacing</strong></td>
                <td>$$d_{hkl} = \\frac{a}{\\sqrt{h^2 + k^2 + l^2}}$$</td>
                <td>\\((hkl)\\): Miller indices; \\(a\\): unit cell lattice parameter</td>
              </tr>
              <tr>
                <td><strong>Bragg's Law (XRD)</strong></td>
                <td>$$n\\lambda = 2 d_{hkl} \\sin\\theta$$</td>
                <td>\\(\\lambda\\): X-ray wavelength; \\(\\theta\\): Bragg diffraction angle; \\(n\\): order (usually 1)</td>
              </tr>
              <tr>
                <td><strong>Equilibrium Vacancies</strong></td>
                <td>$$N_v = N \\exp\\left(-\\frac{Q_v}{kT}\\right)$$</td>
                <td>\\(N\\): total atomic sites; \\(Q_v\\): vacancy activation energy (eV or J/mol); \\(T\\): Kelvin</td>
              </tr>
              <tr>
                <td><strong>ASTM Grain Size Number</strong></td>
                <td>$$N = 2^{n - 1}$$</td>
                <td>\\(N\\): grains per square inch at 100\\(\\times\\); \\(n\\): ASTM grain size number</td>
              </tr>
              <tr>
                <td><strong>Fick's First Law (Steady-State)</strong></td>
                <td>$$J = -D \\frac{dC}{dx} = \\frac{M}{A \\cdot t}$$</td>
                <td>\\(J\\): flux (\\(\\text{kg/m}^2\\cdot\\text{s}\\)); \\(D\\): diffusivity (\\(\\text{m}^2/\\text{s}\\)); \\(dC/dx\\): gradient</td>
              </tr>
              <tr>
                <td><strong>Fick's Second Law (Semi-Infinite)</strong></td>
                <td>$$\\frac{C_x - C_0}{C_s - C_0} = 1 - \\text{erf}\\left(\\frac{x}{2\\sqrt{Dt}}\\right)$$</td>
                <td>\\(C_s\\): surface conc; \\(C_0\\): initial base conc; \\(C_x\\): conc at depth \\(x\\) after time \\(t\\)</td>
              </tr>
              <tr>
                <td><strong>Arrhenius Temperature Law</strong></td>
                <td>$$D = D_0 \\exp\\left(-\\frac{Q_d}{RT}\\right)$$</td>
                <td>\\(D_0\\): pre-exponential (\\(\\text{m}^2/\\text{s}\\)); \\(Q_d\\): activation energy (\\(\\text{J/mol}\\)); \\(R=8.314\\)</td>
              </tr>
              <tr>
                <td><strong>Hooke's Law & Shear Modulus</strong></td>
                <td>$$\\sigma = E\\varepsilon, \\quad \\tau = G\\gamma, \\quad G = \\frac{E}{2(1 + \\nu)}$$</td>
                <td>\\(E\\): Young's modulus; \\(G\\): Shear modulus; \\(\\nu\\): Poisson's ratio (\\(\\sim 0.3\\))</td>
              </tr>
              <tr>
                <td><strong>True Stress & True Strain</strong></td>
                <td>$$\\sigma_T = \\sigma(1+\\varepsilon), \\quad \\varepsilon_T = \\ln(1+\\varepsilon)$$</td>
                <td>Valid up to necking; \\(\\sigma, \\varepsilon\\): engineering stress/strain</td>
              </tr>
              <tr>
                <td><strong>Hollomon Power Law</strong></td>
                <td>$$\\sigma_T = K \\varepsilon_T^n$$</td>
                <td>\\(K\\): strength coefficient; \\(n\\): strain hardening exponent; Necking: \\(\\varepsilon_T = n\\)</td>
              </tr>
              <tr>
                <td><strong>Modulus of Resilience</strong></td>
                <td>$$U_r = \\int_0^{\\varepsilon_y} \\sigma d\\varepsilon \\approx \\frac{\\sigma_y^2}{2E}$$</td>
                <td>\\(U_r\\): elastic energy stored per unit volume (\\(\\text{J/m}^3\\) or \\(\\text{Pa}\\))</td>
              </tr>
              <tr>
                <td><strong>Schmid's Law (Single Crystals)</strong></td>
                <td>$$\\tau_R = \\sigma \\cos\\phi \\cos\\lambda \\le \\tau_{\\text{CRSS}}$$</td>
                <td>\\(\\phi\\): angle to slip plane normal; \\(\\lambda\\): angle to slip direction; \\(m = \\cos\\phi\\cos\\lambda\\)</td>
              </tr>
              <tr>
                <td><strong>Hall-Petch Strengthening</strong></td>
                <td>$$\\sigma_y = \\sigma_0 + k_y d^{-1/2}$$</td>
                <td>\\(\\sigma_0\\): friction stress; \\(k_y\\): locking coefficient (\\(\\text{MPa}\\cdot\\text{mm}^{1/2}\\)); \\(d\\): grain size</td>
              </tr>
              <tr>
                <td><strong>Cold Work & Dislocation Density</strong></td>
                <td>$$\\%\\text{CW} = \\frac{A_0 - A_d}{A_0} \\times 100\\%, \\quad \\tau = \\tau_0 + \\alpha G b \\sqrt{\\rho}$$</td>
                <td>\\(\\rho\\): dislocation density (\\(\\text{m}^{-2}\\)); \\(b\\): Burgers vector; \\(A_0, A_d\\): cross-sections</td>
              </tr>
              <tr>
                <td><strong>Orowan Looping (Precipitation)</strong></td>
                <td>$$\\Delta\\tau = \\frac{G b}{L - 2r} \\approx \\frac{G b}{L}$$</td>
                <td>\\(L\\): inter-particle spacing; \\(r\\): particle radius; \\(G\\): matrix shear modulus</td>
              </tr>
              <tr>
                <td><strong>Stress Concentration (Crack Tip)</strong></td>
                <td>$$K_t = \\frac{\\sigma_m}{\\sigma_0} = 2 \\sqrt{\\frac{a}{\\rho_t}}$$</td>
                <td>\\(a\\): crack length; \\(\\rho_t\\): crack tip radius of curvature; \\(\\sigma_0\\): nominal stress</td>
              </tr>
              <tr>
                <td><strong>Griffith Critical Fracture Stress</strong></td>
                <td>$$\\sigma_c = \\sqrt{\\frac{2E\\gamma_s}{\\pi a}}$$</td>
                <td>\\(\\gamma_s\\): specific surface energy (\\(\\text{J/m}^2\\)); \\(E\\): Young's modulus; \\(a\\): crack size</td>
              </tr>
              <tr>
                <td><strong>Mode I Fracture Toughness</strong></td>
                <td>$$K_I = Y \\sigma \\sqrt{\\pi a} \\le K_{Ic}$$</td>
                <td>\\(K_{Ic}\\): plane strain fracture toughness (\\(\\text{MPa}\\cdot\\sqrt{\\text{m}}\\)); \\(Y\\): geometric factor</td>
              </tr>
              <tr>
                <td><strong>Fatigue Stress Parameters</strong></td>
                <td>$$\\sigma_m = \\frac{\\sigma_{\\max}+\\sigma_{\\min}}{2}, \\quad \\sigma_a = \\frac{\\sigma_{\\max}-\\sigma_{\\min}}{2}, \\quad R = \\frac{\\sigma_{\\min}}{\\sigma_{\\max}}$$</td>
                <td>\\(\\sigma_m\\): mean stress; \\(\\sigma_a\\): amplitude; \\(R\\): stress ratio</td>
              </tr>
              <tr>
                <td><strong>Steady-State Creep Rate</strong></td>
                <td>$$\\dot{\\varepsilon}_s = K_2 \\sigma^n \\exp\\left(-\\frac{Q_c}{RT}\\right)$$</td>
                <td>\\(\\dot{\\varepsilon}_s\\): steady creep rate (\\(\\text{s}^{-1}\\)); \\(n\\): stress exponent; \\(Q_c\\): creep activation energy</td>
              </tr>
              <tr>
                <td><strong>Larson-Miller Parameter</strong></td>
                <td>$$P = T \\left(20 + \\log_{10} t_r\\right)$$</td>
                <td>\\(T\\): absolute temperature in Kelvin; \\(t_r\\): rupture life in hours</td>
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

      <div class="problem-statement">
        <h4 style="font-family: var(--font-serif); font-size: 1.15rem; color: #ffffff; margin-bottom: 0.65rem;">
          {prob['title']}
        </h4>
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
          Step-by-Step Technical Solution & Analysis
        </div>
        
        {prob['solution']}
      </div>
    </article>
    """
