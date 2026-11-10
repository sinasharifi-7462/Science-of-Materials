# ==============================================================================
# SCRIPT TO BUILD CHAPTER 1 DATA: 50 COMPREHENSIVE PROBLEMS & STEP-BY-STEP SOLUTIONS
# Topic: Introduction to Materials Science & Engineering
# ==============================================================================

import json

problems = []

def add_p(num, title, cat, cat_slug, diff, stmt, sol):
    problems.append({
        "number": num,
        "title": title,
        "category": cat,
        "category_slug": cat_slug,
        "difficulty": diff,
        "statement": stmt,
        "solution": sol
    })

# P1
add_p(1, "The Fundamental Distinction: Materials Science vs. Materials Engineering",
      "Conceptual & Paradigmatic", "concept", "Fundamental",
      """<p>In academic curricula and industrial research, the fields of <strong>Materials Science</strong> and <strong>Materials Engineering</strong> are closely intertwined yet represent distinct epistemological viewpoints.</p>
      <ol type="a">
        <li>Provide a rigorous definition of <em>Materials Science</em> and state its primary scientific objective.</li>
        <li>Provide a rigorous definition of <em>Materials Engineering</em> and state how it builds upon materials science.</li>
        <li>Illustrate this distinction using a concrete engineering example: the development and manufacturing of a heat-treated aerospace aluminum wing spar.</li>
      </ol>""",
      """<div class="solution-step">
        <div class="solution-step-title">Part (a): Definition and Core Objective of Materials Science</div>
        <p><strong>Materials Science</strong> is the scientific discipline focused on investigating the fundamental relationships that exist between the internal structure of materials (encompassing subatomic arrangements, atomic bonding, crystal lattice geometries, point/line/planar defects, and multi-phase microstructures) and their macroscopic chemical, physical, and mechanical properties. Its primary objective is to discover fundamental physical principles, quantify mechanisms, and formulate predictive models explaining <em>why</em> materials behave the way they do.</p>
      </div>
      <div class="solution-step">
        <div class="solution-step-title">Part (b): Definition and Core Objective of Materials Engineering</div>
        <p><strong>Materials Engineering</strong> is the applied engineering discipline that utilizes established structure-property correlations to design, synthesize, optimize, and manufacture materials into predetermined macroscopic shapes and functional components that satisfy specific, rigorous performance and economic criteria. Its primary objective is applied problem-solving: producing reliable, cost-effective components that withstand intended service environments.</p>
      </div>
      <div class="solution-step">
        <div class="solution-step-title">Part (c): Illustrative Case Study (Aerospace Wing Spar)</div>
        <p>Consider an Al-Zn-Mg-Cu alloy (AA 7075) used for a high-performance commercial aircraft wing spar:</p>
        <ul>
          <li><strong>The Materials Scientist</strong> investigates the thermodynamics and kinetics of solid solution decomposition during artificial aging. Using transmission electron microscopy (TEM) and small-angle X-ray scattering, the scientist characterizes the precipitation sequence (supersaturated solid solution &rarr; GP zones &rarr; metastable &eta;&prime; phase &rarr; equilibrium &eta;-$\text{MgZn}_2$), measuring how coherent stress fields around &eta;&prime; platelets interact with gliding dislocations to increase yield strength.</li>
          <li><strong>The Materials Engineer</strong> takes these fundamental scientific findings to specify the industrial processing route: selecting a two-step aging heat treatment (T73 temper) that balances peak tensile strength (over 500 MPa) against stress-corrosion cracking resistance and fracture toughness ($K_{Ic}$), while designing the extrusion dies, machining tolerances, and non-destructive inspection protocols for mass production.</li>
        </ul>
      </div>
      <div class="final-answer-box">
        <strong>Summary Takeaway:</strong> Materials Science investigates <em>structure-property relationships</em> (understanding fundamentals); Materials Engineering applies these relationships to <em>design processing routes and components</em> that meet engineering performance requirements.
      </div>""")

# P2
add_p(2, "The Materials Tetrahedron: Processing-Structure-Properties-Performance Feedback",
      "Conceptual & Paradigmatic", "concept", "Fundamental",
      """<p>The central paradigm of Materials Science and Engineering is graphically represented by the <strong>Materials Tetrahedron</strong>, which interconnects four fundamental vertices: <em>Processing</em>, <em>Structure</em>, <em>Properties</em>, and <em>Performance</em>.</p>
      <ol type="a">
        <li>Explain the physical meaning of each of the four vertices and the nature of the feedback loops connecting them.</li>
        <li>Explain why modern materials development places <em>Performance</em> at the top vertex, and how life-cycle sustainability and economics modify the classical paradigm.</li>
        <li>Using copper wire manufacturing as an example, describe the chronological traversal around the four vertices from raw casting to a flexible domestic electrical conductor.</li>
      </ol>""",
      """<div class="solution-step">
        <div class="solution-step-title">Part (a): The Four Vertices & Their Interconnectivity</div>
        <ul>
          <li><strong>Processing:</strong> The physical and chemical synthesis and shaping operations applied to raw materials (e.g., casting, rolling, forging, sintering, additive manufacturing, annealing, quenching).</li>
          <li><strong>Structure:</strong> The internal spatial arrangement of constituents across all length scales: subatomic (electron orbitals), atomic/crystal lattice (FCC/BCC/HCP), defect scale (dislocations, vacancies), and microscopic/mesoscopic (grains, inclusions, second phases).</li>
          <li><strong>Properties:</strong> The intrinsic material response to an applied external stimulus (mechanical load, electric field, magnetic field, temperature gradient, corrosive chemical species), independent of component geometry (e.g., yield strength $\\sigma_y$, electrical conductivity $\\sigma_e$, thermal expansion $\\alpha$).</li>
          <li><strong>Performance:</strong> The functional behavior and reliability of the finished component under actual service operating conditions (e.g., fatigue life of an axle, power loss in a transmission line, oxidation resistance of a turbine blade).</li>
        </ul>
      </div>
      <div class="solution-step">
        <div class="solution-step-title">Part (b): Performance-Driven Design & Modern Constraints</div>
        <p>In modern performance-driven engineering, the design loop operates in reverse: the functional requirements and operating environment dictate the required macroscopic <em>Properties</em>; these required properties specify the optimal micro- and nano-<em>Structure</em>; and the desired structure dictates the tailored <em>Processing</em> route. Contemporary engineering expands the tetrahedron into an octahedron by integrating <strong>Cost/Economics</strong> and <strong>Environmental Impact/Life-Cycle Sustainability</strong>.</p>
      </div>
      <div class="solution-step">
        <div class="solution-step-title">Part (c): Traversal in Copper Wire Production</div>
        <ol>
          <li><strong>Processing:</strong> Continuous casting of oxygen-free high-conductivity (OFHC) copper, followed by multipass cold drawing through progressive diamond dies to reduce diameter from 8 mm to 1.5 mm, followed by batch recrystallization annealing at 450 &deg;C.</li>
          <li><strong>Structure:</strong> Cold drawing creates a high dislocation density ($\\sim 10^{15} \\text{ m}^{-2}$) and textured elongated grains. Subsequent annealing triggers recovery and recrystallization, reducing dislocation density to $\\sim 10^9 \\text{ m}^{-2}$ and forming equiaxed, strain-free grains with twin boundaries.</li>
          <li><strong>Properties:</strong> Low dislocation density minimizes electron and dislocation scattering, resulting in very high electrical conductivity ($> 100\\% \\text{ IACS}$) and high tensile ductility ($> 35\\% \\text{ EL}$) with a modest yield strength ($\\approx 70 \\text{ MPa}$).</li>
          <li><strong>Performance:</strong> In domestic electrical wiring, the wire exhibits minimal Joule heating ($I^2R$ power loss), fits safely inside tight junction boxes without work-hardening to brittle fracture, and maintains fire safety over decades of service.</li>
        </ol>
      </div>
      <div class="final-answer-box">
        <strong>Core Principle:</strong> Processing creates Structure; Structure dictates Properties; Properties determine Performance. Changing any single vertex inevitably alters the entire system.
      </div>""")

# We will write a python script that populates all 50 problems for Chapter 1
with open("generator/ch1_builder_data.py", "w", encoding="utf-8") as f:
    f.write("# Chapter 1 Builder Data\n")
    f.write("import json\n")
    f.write(f"p1 = {json.dumps(problems[0], indent=2)}\n")
    f.write(f"p2 = {json.dumps(problems[1], indent=2)}\n")

print("Test builder data written.")
