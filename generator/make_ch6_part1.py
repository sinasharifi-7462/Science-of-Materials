# generator/make_ch6_part1.py
# ==============================================================================
# CHAPTER 6: MECHANICAL PROPERTIES OF METALS - PART 1 (PROBLEMS 1 TO 25)
# Course: Science of Materials | University of Tehran | Prof. Sadeghi
# Prepared by TA Sina Sharifi
# ==============================================================================

P = []

def add(num, title, cat, slug, diff, stmt, sol):
    P.append({
        "number": num,
        "title": title,
        "category": cat,
        "category_slug": slug,
        "difficulty": diff,
        "statement": stmt.strip(),
        "solution": sol.strip()
    })

# P1: Engineering Stress and Strain Definitions
add(1, "Engineering Stress and Strain: Uniaxial Tension Definitions and Units",
    "Elastic Deformation & Moduli", "elastic_moduli", "Fundamental",
    r"""<p>The standard uniaxial tensile test is the primary mechanical characterization method utilized to assess the structural load-bearing capacity of engineering materials.</p>
    <ol type="a">
      <li>State the definitions and mathematical formulas for:
        <ul>
          <li><strong>Engineering Stress</strong> ($\sigma$).</li>
          <li><strong>Engineering Strain</strong> ($\varepsilon$).</li>
        </ul>
        Define original cross-sectional area $A_0$, instantaneous applied tensile load $F$, original gauge length $l_0$, and instantaneous gauge length $l$. State standard SI and Imperial units.</li>
      <li>A cylindrical tensile specimen of AISI 1045 steel has an initial gauge diameter $d_0 = 12.80 \text{ mm}$ and initial gauge length $l_0 = 50.00 \text{ mm}$. Under a tensile load of $F = 45.0 \text{ kN}$, the gauge length elongates to $l = 50.085 \text{ mm}$. Calculate the engineering stress $\sigma$ in megapascals ($\text{MPa}$) and the engineering strain $\varepsilon$ (dimensionless and in percent).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Definitions and Units</div>
      <ul>
        <li><strong>Engineering Stress ($\sigma$):</strong> The instantaneous tensile load $F$ divided by the <em>original, undeformed cross-sectional area</em> $A_0$:
        $$\sigma = \frac{F}{A_0} \quad \left[\frac{\text{N}}{\text{m}^2} = \text{Pa}, \text{ commonly reported in MPa } (1 \text{ MPa} = 10^6 \text{ N/m}^2 = 1 \text{ N/mm}^2) \text{ or psi / ksi}\right]$$</li>
        <li><strong>Engineering Strain ($\varepsilon$):</strong> The change in gauge length $\Delta l = l - l_0$ divided by the <em>original gauge length</em> $l_0$:
        $$\varepsilon = \frac{\Delta l}{l_0} = \frac{l - l_0}{l_0} \quad [\text{dimensionless, or m/m, in/in, or percentage } \varepsilon \times 100\%]$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculations for AISI 1045 Steel Specimen</div>
      <p>Initial cross-sectional area ($d_0 = 12.80 \text{ mm} = 12.80 \times 10^{-3} \text{ m}$):</p>
      $$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi (12.80 \text{ mm})^2}{4} = \frac{\pi \times 163.84}{4} = 128.68 \text{ mm}^2 = 1.2868 \times 10^{-4} \text{ m}^2$$
      <p>Engineering stress ($F = 45.0 \text{ kN} = 45,000 \text{ N}$):</p>
      $$\sigma = \frac{F}{A_0} = \frac{45,000 \text{ N}}{1.2868 \times 10^{-4} \text{ m}^2} = 3.497 \times 10^8 \text{ Pa} = \mathbf{349.7 \text{ MPa}}$$
      <p>Engineering strain ($l_0 = 50.00 \text{ mm}, l = 50.085 \text{ mm}$):</p>
      $$\Delta l = 50.085 - 50.000 = 0.085 \text{ mm}$$
      $$\varepsilon = \frac{\Delta l}{l_0} = \frac{0.085 \text{ mm}}{50.00 \text{ mm}} = \mathbf{1.70 \times 10^{-3} = 0.170\%}$$
    </div>
    <div class="final-answer-box">
      <strong>Engineering Stress:</strong> $\sigma = \frac{F}{A_0} = \mathbf{349.7 \text{ MPa}}$.<br>
      <strong>Engineering Strain:</strong> $\varepsilon = \frac{\Delta l}{l_0} = \mathbf{1.70 \times 10^{-3}} = \mathbf{0.170\%}$.
    </div>""")

# P2: Hooke's Law and Modulus of Elasticity
add(2, "Hooke's Law in Tension: Young's Modulus of Elasticity and Atomic Bonding",
    "Elastic Deformation & Moduli", "elastic_moduli", "Fundamental",
    r"""<p>For most engineering metals subjected to low stresses, deformation is linear and completely reversible (elastic).</p>
    <ol type="a">
      <li>State <strong>Hooke's Law</strong> in 1D tension:
      $$\sigma = E \varepsilon$$
      Define the <strong>Modulus of Elasticity (Young's Modulus $E$)</strong> and state its standard units.</li>
      <li>Explain the microscopic physical origin of Young's modulus in terms of the interatomic potential energy well $E_N(r)$ and interatomic force curve $F(r)$. Show that $E \propto \left.\frac{d^2 E_N}{dr^2}\right|_{r_0}$.</li>
      <li>Rank metals, ceramics, and polymers in order of decreasing Young's modulus, and explain why heating a metal causes its modulus of elasticity to decrease.</li>
      <li>Using the data from Problem 1 ($\sigma = 349.7 \text{ MPa}$ at $\varepsilon = 1.70 \times 10^{-3}$ in the linear elastic regime), calculate Young's modulus $E$ for the steel specimen in gigapascals ($\text{GPa}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Hooke's Law and Young's Modulus</div>
      $$\sigma = E \varepsilon \implies E = \frac{\sigma}{\varepsilon}$$
      <p>Young's Modulus $E$ represents the mechanical stiffness of a material—its resistance to elastic elongation under applied tensile stress. Standard units: $\text{Pa}$ or $\mathbf{\text{GPa}}$ ($1 \text{ GPa} = 10^9 \text{ Pa} = 10^3 \text{ MPa}$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Atomic Origin of Elastic Modulus</div>
      <p>Under small elastic tensile strains, external stress slightly displaces atoms from their equilibrium separation distance $r_0$ against attractive and repulsive interatomic forces. The restoring force per unit displacement is the interatomic force constant $k_0$:</p>
      $$k_0 = \left.\frac{dF}{dr}\right|_{r_0} = \left.\frac{d^2 E_N}{dr^2}\right|_{r_0}$$
      <p>Because macroscopic stress scales as force per atomic area ($\sigma \sim F/r_0^2$) and strain scales as fractional displacement ($\varepsilon \sim \Delta r / r_0$):</p>
      $$E = \frac{\sigma}{\varepsilon} \sim \frac{F / r_0^2}{\Delta r / r_0} = \frac{1}{r_0} \left(\frac{F}{\Delta r}\right) = \frac{k_0}{r_0} = \frac{1}{r_0} \left.\frac{d^2 E_N}{dr^2}\right|_{r_0}$$
      <p>Thus, Young's modulus is directly proportional to the <strong>curvature (steepness) of the interatomic potential energy well</strong> at the equilibrium separation $r_0$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Materials Ranking and Temperature Effect</div>
      <ul>
        <li><strong>Ranking:</strong> $\mathbf{\text{Ceramics} > \text{Metals} > \text{Polymers}}$
          <ul>
            <li><em>Ceramics (e.g., Diamond $1000\text{ GPa}$, SiC $450\text{ GPa}$, Alumina $380\text{ GPa}$):</em> Ultra-strong directional covalent and ionic bonds produce extremely steep, deep potential wells.</li>
            <li><em>Metals (e.g., Tungsten $410\text{ GPa}$, Steel $207\text{ GPa}$, Copper $110\text{ GPa}$, Aluminum $70\text{ GPa}$):</em> Strong non-directional metallic bonds.</li>
            <li><em>Polymers (e.g., Nylon $2\text{--}4\text{ GPa}$, Polyethylene $0.2\text{--}1.0\text{ GPa}$):</em> Intermolecular bonding is governed by weak secondary van der Waals forces, yielding shallow potential wells.</li>
          </ul>
        </li>
        <li><strong>Temperature Dependence:</strong> As temperature rises, increased thermal vibration amplitudes expand the average interatomic separation ($r > r_0$). At larger separation, the curvature of the potential energy well $\frac{d^2 E_N}{dr^2}$ decreases, causing Young's modulus to decline monotonically with temperature ($dE/dT < 0$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Calculation for Steel Specimen</div>
      $$E = \frac{\sigma}{\varepsilon} = \frac{349.7 \times 10^6 \text{ Pa}}{1.70 \times 10^{-3}} = 2.057 \times 10^{11} \text{ Pa} = \mathbf{205.7 \text{ GPa}}$$
      <p>This matches the standard canonical textbook value for structural carbon steels ($E \approx 207 \text{ GPa}$).</p>
    </div>
    <div class="final-answer-box">
      <strong>Hooke's Law:</strong> $\sigma = E \varepsilon \implies E = \frac{1}{r_0}\left.\frac{d^2E_N}{dr^2}\right|_{r_0}$.<br>
      <strong>Stiffness Ranking:</strong> $\text{Ceramics} > \text{Metals} \gg \text{Polymers}$.<br>
      <strong>Steel Modulus:</strong> $E = \mathbf{205.7 \text{ GPa}}$.
    </div>""")

# P3: Poisson's Ratio
add(3, "Lateral Elastic Contraction and Poisson's Ratio: Theoretical Bounds and Values",
    "Elastic Deformation & Moduli", "elastic_moduli", "Fundamental",
    r"""<p>When a solid rod is pulled in tension, its longitudinal elongation is accompanied by a simultaneous lateral contraction.</p>
    <ol type="a">
      <li>Define <strong>Poisson's Ratio ($\nu$)</strong> mathematically for uniaxial loading along the $z$-axis:
      $$\nu = -\frac{\varepsilon_{\text{lateral}}}{\varepsilon_{\text{axial}}} = -\frac{\varepsilon_x}{\varepsilon_z} = -\frac{\varepsilon_y}{\varepsilon_z}$$
      Why is the negative sign included in the definition?</li>
      <li>State the theoretical thermodynamic bounds for Poisson's ratio in isotropic solids ($-1 \le \nu \le 0.5$). Explain the physical significance of $\nu = 0.5$ (incompressibility) and $\nu = 0$ (cork).</li>
      <li>What are <strong>auxetic materials</strong> ($\nu < 0$), and what unusual geometric behavior do they exhibit when pulled in tension?</li>
      <li>A cylindrical copper bar ($E = 110 \text{ GPa}, \nu = 0.34$) with initial diameter $d_0 = 10.000 \text{ mm}$ is loaded in tension by $F = 15.0 \text{ kN}$ within its elastic limit. Calculate the change in diameter $\Delta d$ in micrometers.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition of Poisson's Ratio $\nu$</div>
      $$\nu = -\frac{\varepsilon_{\text{lateral}}}{\varepsilon_{\text{axial}}}$$
      <p>Under uniaxial tension, the axial strain is positive ($\varepsilon_{\text{axial}} > 0$), while the lateral dimensions contract, making lateral strain negative ($\varepsilon_{\text{lateral}} < 0$). The negative sign is explicitly inserted so that Poisson's ratio is a <strong>positive dimensionless number</strong> for conventional engineering materials.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Theoretical Bounds for Isotropic Solids ($-1 \le \nu \le 0.5$)</div>
      <p>From continuum elasticity, positive strain energy requires that both shear modulus $G = \frac{E}{2(1+\nu)} > 0$ and bulk modulus $K = \frac{E}{3(1-2\nu)} > 0$. This imposes the strict mathematical bounds:</p>
      $$-1.0 \le \nu \le 0.5$$
      <ul>
        <li><strong>$\nu = 0.5$ (Perfect Incompressibility):</strong> The material deforms with zero change in volume ($\Delta V / V = 0$). Typical of rubber, elastomers, and plastically deforming metals.</li>
        <li><strong>$\nu = 0$ (Zero Lateral Strain):</strong> Uniaxial tension causes elongation with zero lateral contraction. Typical of cellular cork (allowing wine corks to be pushed into bottles without expanding radially).</li>
        <li><strong>Common Metals:</strong> Most engineering metals exhibit $\nu \approx 0.28\text{ to }0.35$ (e.g., steel $\sim 0.30$, aluminum $\sim 0.33$, copper $\sim 0.34$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Auxetic Materials ($\nu < 0$)</div>
      <p>Auxetic materials possess negative Poisson's ratios ($\nu < 0$). When pulled in longitudinal tension, their lateral dimensions <strong>expand perpendicularly</strong> rather than contracting (due to re-entrant re-folding cellular microstructures). Used in blast-resistant armor, gore-tex vascular stents, and high-energy absorption footwear.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Calculation for Copper Bar ($d_0 = 10.00 \text{ mm}, F = 15.0 \text{ kN}$)</div>
      $$A_0 = \frac{\pi (10.00 \times 10^{-3} \text{ m})^2}{4} = 7.854 \times 10^{-5} \text{ m}^2$$
      $$\sigma_z = \frac{F}{A_0} = \frac{15,000 \text{ N}}{7.854 \times 10^{-5} \text{ m}^2} = 1.9099 \times 10^8 \text{ Pa} = 191.0 \text{ MPa}$$
      <p>Axial strain along $z$:</p>
      $$\varepsilon_z = \frac{\sigma_z}{E} = \frac{1.9099 \times 10^8 \text{ Pa}}{110 \times 10^9 \text{ Pa}} = 1.7363 \times 10^{-3}$$
      <p>Lateral strain along diameter:</p>
      $$\varepsilon_{\text{lat}} = -\nu \varepsilon_z = -(0.34) \times (1.7363 \times 10^{-3}) = -5.903 \times 10^{-4}$$
      <p>Change in diameter $\Delta d$:</p>
      $$\Delta d = d_0 \cdot \varepsilon_{\text{lat}} = (10.00 \text{ mm}) \times (-5.903 \times 10^{-4}) = -5.903 \times 10^{-3} \text{ mm} = \mathbf{-5.90 \mu\text{m}}$$
      <p>The diameter contracts by $5.90$ micrometers.</p>
    </div>
    <div class="final-answer-box">
      <strong>Poisson's Ratio:</strong> $\nu = -\frac{\varepsilon_{\text{lat}}}{\varepsilon_{\text{axial}}}$ (Bounds: $-1.0 \le \nu \le 0.5$).<br>
      <strong>Physical Limits:</strong> $\nu = 0.5$ (incompressible rubber) &bull; $\nu = 0$ (cork) &bull; $\nu < 0$ (auxetic expansion).<br>
      <strong>Lateral Contraction:</strong> $\Delta d = \mathbf{-5.90 \mu\text{m}}$.
    </div>""")

# P4: Shear Modulus and Bulk Modulus Relationships
add(4, "Elastic Constants: Shear Modulus $G$, Bulk Modulus $K$, and Volumetric Strain",
    "Elastic Deformation & Moduli", "elastic_moduli", "Intermediate",
    r"""<p>For an isotropic linear elastic solid, all elastic behaviors are completely defined by any two independent elastic constants.</p>
    <ol type="a">
      <li>State the mathematical definitions of:
        <ul>
          <li><strong>Shear Modulus ($G$)</strong> relating shear stress $\tau$ to shear strain $\gamma$.</li>
          <li><strong>Bulk Modulus ($K$)</strong> relating hydrostatic pressure $P$ to fractional volume change $\Delta V / V_0$.</li>
        </ul>
      </li>
      <li>State the isotropic elasticity relationships linking $G$ and $K$ to Young's modulus $E$ and Poisson's ratio $\nu$:
      $$G = \frac{E}{2(1 + \nu)}, \quad K = \frac{E}{3(1 - 2\nu)}$$</li>
      <li>Prove that the volumetric strain (dilatation $e = \Delta V / V_0$) under uniaxial tensile stress $\sigma_z$ is given by:
      $$e = \frac{\Delta V}{V_0} = \varepsilon_z (1 - 2\nu) = \frac{\sigma_z}{E}(1 - 2\nu)$$
      Confirm that for $\nu = 0.5$, volumetric strain is identically zero.</li>
      <li>Titanium has $E = 107 \text{ GPa}$ and $\nu = 0.34$. Calculate its Shear Modulus $G$ and Bulk Modulus $K$ in gigapascals.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definitions of $G$ and $K$</div>
      <ul>
        <li><strong>Shear Modulus ($G$):</strong> The ratio of shear stress $\tau$ to engineering shear strain $\gamma$:
        $$\tau = G \gamma \implies G = \frac{\tau}{\gamma} \quad [\text{GPa}]$$</li>
        <li><strong>Bulk Modulus ($K$):</strong> The ratio of uniform hydrostatic pressure $P = -\sigma_h$ to the resulting fractional volumetric compression:
        $$P = -K \left(\frac{\Delta V}{V_0}\right) \implies K = -\frac{P}{\Delta V / V_0} \quad [\text{GPa}]$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Interrelationships in Isotropic Elasticity</div>
      $$G = \frac{E}{2(1 + \nu)}, \quad K = \frac{E}{3(1 - 2\nu)}, \quad E = \frac{9KG}{3K + G}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Proof of Volumetric Strain Equation</div>
      <p>Consider an infinitesimal cube of dimensions $L_0 \times L_0 \times L_0$ subjected to uniaxial tensile stress along $z$. The principal strains are:</p>
      $$\varepsilon_z = \frac{\sigma_z}{E}, \quad \varepsilon_x = -\nu\varepsilon_z, \quad \varepsilon_y = -\nu\varepsilon_z$$
      <p>The deformed volume is:</p>
      $$V = L_0(1 + \varepsilon_x) \cdot L_0(1 + \varepsilon_y) \cdot L_0(1 + \varepsilon_z) = V_0 (1 - \nu\varepsilon_z)(1 - \nu\varepsilon_z)(1 + \varepsilon_z)$$
      <p>Expanding and neglecting higher-order strain products ($\varepsilon^2 \approx 0$ for small elastic deformations):</p>
      $$\frac{V}{V_0} \approx 1 + \varepsilon_x + \varepsilon_y + \varepsilon_z = 1 - \nu\varepsilon_z - \nu\varepsilon_z + \varepsilon_z = 1 + \varepsilon_z(1 - 2\nu)$$
      $$\frac{\Delta V}{V_0} = \frac{V - V_0}{V_0} = \mathbf{\varepsilon_z (1 - 2\nu) = \frac{\sigma_z}{E}(1 - 2\nu)}$$
      <p>If $\nu = 0.5$, then $(1 - 2\nu) = 1 - 2(0.5) = 0 \implies \Delta V / V_0 \equiv 0$ (perfectly constant volume).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Calculations for Titanium ($E = 107 \text{ GPa}, \nu = 0.34$)</div>
      <ul>
        <li><strong>Shear Modulus ($G$):</strong>
        $$G = \frac{E}{2(1 + \nu)} = \frac{107 \text{ GPa}}{2(1 + 0.34)} = \frac{107}{2.68} = \mathbf{39.93 \text{ GPa}}$$</li>
        <li><strong>Bulk Modulus ($K$):</strong>
        $$K = \frac{E}{3(1 - 2\nu)} = \frac{107 \text{ GPa}}{3(1 - 2 \times 0.34)} = \frac{107}{3(1 - 0.68)} = \frac{107}{3(0.32)} = \frac{107}{0.96} = \mathbf{111.46 \text{ GPa}}$$</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Isotropic Relations:</strong> $G = \frac{E}{2(1+\nu)}$, $K = \frac{E}{3(1-2\nu)}$, $\frac{\Delta V}{V_0} = \varepsilon_z(1-2\nu)$.<br>
      <strong>Titanium Moduli:</strong> $G = \mathbf{39.9 \text{ GPa}}$, $K = \mathbf{111.5 \text{ GPa}}$.
    </div>""")

# P5: Plastic Yielding 0.2% Offset Method
add(5, "Plastic Yielding: The 0.2% Strain Offset Yield Strength Construction",
    "Yielding & Tensile Parameters", "tensile_parameters", "Fundamental",
    r"""<p>Because most engineering metals exhibit a gradual transition from elastic to plastic deformation without an abrupt kink, yield strength is standardized using the 0.2% offset method.</p>
    <ol type="a">
      <li>Explain the detailed geometric procedure for determining the <strong>0.2% Offset Yield Strength ($\sigma_y$ or $\sigma_{0.2}$)</strong> from an engineering stress-strain curve according to ASTM E8.</li>
      <li>Why is a plastic offset of $\varepsilon_{\text{offset}} = 0.002$ ($0.2\%$) chosen rather than $0.000$ or $0.05$?</li>
      <li>The linear elastic portion of a tensile curve for an aluminum alloy ($E = 70.0 \text{ GPa}$) passes through the origin. Plastic yielding begins gradually. The measured total engineering strain at a stress of $\sigma = 310 \text{ MPa}$ is $\varepsilon_{\text{total}} = 0.00643$. Determine whether the material has reached, exceeded, or not yet reached its 0.2% offset yield point at this stress.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Geometric Construction of the 0.2% Offset Yield Strength</div>
      <ol>
        <li>Plot the experimental engineering stress-strain curve ($\sigma$ vs. $\varepsilon$).</li>
        <li>Determine the slope of the initial linear elastic region, which defines Young's modulus $E$.</li>
        <li>On the strain axis ($\sigma = 0$), locate the point corresponding to a permanent offset strain of $\varepsilon = 0.002$ ($0.2\%$).</li>
        <li>Draw a straight construction line starting from $(0.002, 0)$ directed parallel to the linear elastic line (slope $= E$).</li>
        <li>The intersection point where this parallel offset line crosses the stress-strain curve defines the <strong>0.2% offset yield strength ($\sigma_y$ or $\sigma_{0.2}$)</strong>.</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Why $\varepsilon_{\text{offset}} = 0.002$ ($0.2\%$) Was Chosen</div>
      <p>True microscopic plastic deformation begins at the proportional limit ($\sigma_{pl}$), where the curve first deviates from linearity. However, measuring $\sigma_{pl}$ is highly subjective and depends strongly on extensometer sensitivity and noise. A small offset of $0.002$ ($0.2\%$) represents a tiny, acceptable permanent plastic deformation that can be reproduced with high precision across different laboratories and testing machines, providing an unambiguous engineering design criterion.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Evaluation for Aluminum Alloy ($\sigma = 310 \text{ MPa}, \varepsilon_{\text{total}} = 0.00643$)</div>
      <p>Total strain is the sum of recoverable elastic strain and permanent plastic strain:</p>
      $$\varepsilon_{\text{total}} = \varepsilon_{\text{elastic}} + \varepsilon_{\text{plastic}}$$
      <p>By Hooke's law, the elastic strain at $\sigma = 310 \text{ MPa}$ ($E = 70.0 \text{ GPa} = 70,000 \text{ MPa}$) is:</p>
      $$\varepsilon_{\text{elastic}} = \frac{\sigma}{E} = \frac{310 \text{ MPa}}{70,000 \text{ MPa}} = 0.004429$$
      <p>Calculate the plastic strain:</p>
      $$\varepsilon_{\text{plastic}} = \varepsilon_{\text{total}} - \varepsilon_{\text{elastic}} = 0.00643 - 0.004429 = \mathbf{0.002001 \approx 0.00200}$$
      <p>Because the plastic strain is precisely $\varepsilon_{\text{plastic}} = 0.00200$ ($0.200\%$), this stress point lies exactly on the offset line! Therefore, the 0.2% offset yield strength of this alloy is precisely $\mathbf{\sigma_y = 310 \text{ MPa}}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>0.2% Offset Method:</strong> Construct line from $\varepsilon = 0.002$ parallel to elastic slope $E$; intersection defines $\sigma_y$.<br>
      <strong>Aluminum Specimen:</strong> $\varepsilon_{\text{plastic}} = 0.00643 - 0.00443 = \mathbf{0.00200} \implies \sigma_y = \mathbf{310 \text{ MPa}}$.
    </div>""")

# Save checkpoint for part 1 (1 to 5)
print("Ch 6 Part 1: P1-P5 written.")
# P6: Upper and Lower Yield Point Phenomenon
add(6, "The Yield Point Phenomenon: Upper/Lower Yield Points, Lüders Bands, and Cottrell Pinning",
    "Yielding & Tensile Parameters", "tensile_parameters", "Intermediate",
    r"""<p>Certain structural alloys, most notably low-carbon mild steels, exhibit an anomalous yield point phenomenon with distinct upper and lower yield points.</p>
    <ol type="a">
      <li>Differentiate between:
        <ul>
          <li><strong>Upper Yield Point ($\sigma_{\text{uy}}$)</strong></li>
          <li><strong>Lower Yield Point ($\sigma_{\text{ly}}$)</strong></li>
          <li><strong>Yield Point Elongation (YPE)</strong></li>
        </ul>
      </li>
      <li>Explain the microscopic mechanism responsible for the upper yield point using Cottrell atmosphere dislocation pinning by interstitial carbon and nitrogen atoms.</li>
      <li>Describe what happens microstructurally during the flat yield point elongation region. What are <strong>Lüders bands (stretcher strains)</strong>?</li>
      <li>In design engineering, which yield point ($\sigma_{\text{uy}}$ or $\sigma_{\text{ly}}$) is used as the design parameter, and why?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Yield Point Phenomenon Definitions</div>
      <ul>
        <li><strong>Upper Yield Point ($\sigma_{\text{uy}}$):</strong> The temporary peak stress where plastic deformation first initiates. After this peak, the stress drops abruptly without increasing load. Highly sensitive to testing machine stiffness and specimen alignment.</li>
        <li><strong>Lower Yield Point ($\sigma_{\text{ly}}$):</strong> The stable, relatively constant plateau stress at which plastic deformation propagates across the specimen gauge length.</li>
        <li><strong>Yield Point Elongation (YPE):</strong> The heterogeneous plastic strain that accumulates at constant lower yield stress before continuous strain hardening commences (typically $1\text{--}4\%$ strain).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Dislocation Pinning Mechanism (Cottrell Atmospheres)</div>
      <p>In low-carbon steel, interstitial carbon and nitrogen atoms segregate to the dilated tensile regions beneath edge dislocation cores, forming dense solute clouds known as <strong>Cottrell atmospheres</strong>. These solute atmospheres anchor (pin) dislocations firmly in place. To initiate plastic flow, an exceptionally high stress ($\sigma_{\text{uy}}$) must be applied to tear dislocations away from their pinning solute atmospheres. Once torn free, these unpinned dislocations multiply catastrophically and glide with extreme ease at a much lower glide resistance, causing the stress to drop abruptly to the lower yield point ($\sigma_{\text{ly}}$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Lüders Bands Propagation (Yield Point Elongation)</div>
      <p>During the yield point elongation, deformation does not occur uniformly throughout the specimen. Instead, one or more localized bands of plastic shear (oriented at approximately $45^\circ\text{--}50^\circ$ to the tensile axis) nucleate at stress concentrators (such as specimen shoulders) and propagate steadily along the gauge section at constant lower yield stress. These visible surface markings are termed <strong>Lüders bands</strong> or <strong>stretcher-strain marks</strong>. Once the entire gauge length has been swept by Lüders bands, uniform strain hardening begins.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Design Engineering Practice</div>
      <p>Structural engineering design codes universally specify the <strong>lower yield strength ($\sigma_{\text{ly}}$)</strong> as the design allowable. The upper yield point is unreliable because minor vibrations, slight specimen misalignment, or tiny surface scratches can prematurely trigger dislocation unpinning, dropping the load-bearing capacity immediately to the lower yield stress.</p>
    </div>
    <div class="final-answer-box">
      <strong>Upper Yield:</strong> Dislocation breakout from Cottrell atmospheres &bull; <strong>Lower Yield:</strong> Mobile dislocation glide.<br>
      <strong>Lüders Bands:</strong> Heterogeneous shear bands propagating along gauge section during yield point elongation.<br>
      <strong>Design Standard:</strong> Lower yield strength $\sigma_{\text{ly}}$ is strictly used for engineering design safety.
    </div>""")

# P7: Skin-Pass Rolling and Strain Aging
add(7, "Elimination of Stretcher Strains: Skin-Pass Temper Rolling and Dynamic Strain Aging",
    "Yielding & Tensile Parameters", "tensile_parameters", "Intermediate",
    r"""<p>In the automotive stamping of outer body panels (hoods, fenders, doors), the formation of visible Lüders bands during deep drawing results in unacceptable surface roughness (orange-peel effect).</p>
    <ol type="a">
      <li>Explain how <strong>skin-pass (temper) rolling</strong> (a light cold rolling pass of $0.5\text{--}1.5\%$ reduction) eliminates the yield point phenomenon and suppresses stretcher strains in deep-drawing steels.</li>
      <li>What is <strong>strain aging (static strain aging)</strong>, and why must temper-rolled steel sheets be stamped into automotive body panels within a few weeks of rolling?</li>
      <li>How does the addition of small amounts of Titanium or Aluminum (Interstitial-Free / IF steels) prevent strain aging permanently?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mechanism of Skin-Pass (Temper) Rolling</div>
      <p>Skin-pass rolling applies a tiny cold reduction of $0.5\text{--}1.5\%$ between smooth steel rolls. This slight plastic deformation breaks all pinned dislocations free from their Cottrell atmospheres throughout the sheet and introduces a small population of fresh, mobile dislocations ($\sim 10^9 \text{ cm}^{-2}$). When the temper-rolled sheet is subsequently stamped in a press, these pre-existing mobile dislocations immediately glide uniformly across the entire part. The stress-strain curve shows a smooth, continuous elastic-to-plastic transition with <strong>zero yield point drop and zero Lüders bands</strong>, producing flawless, mirror-smooth automotive outer panels.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Static Strain Aging During Storage</div>
      <p>If temper-rolled steel coils sit in a warehouse at room temperature ($25^\circ\text{C}$) for several weeks or months, dissolved interstitial carbon and nitrogen atoms diffuse slowly through the ferrite lattice ($D_{\text{N}} \sim 10^{-20} \text{ m}^2/\text{s}$). Driven by elastic strain relief, they migrate to the newly created dislocations and re-form Cottrell atmospheres, pinning them once again. As a consequence, the <strong>sharp yield point and yield point elongation spontaneously return</strong>, accompanied by an increase in yield strength and a loss of ductility. If stamped after aging, the sheet develops severe stretcher-strain wrinkles and may tear during deep drawing.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Interstitial-Free (IF) Steels</div>
      <p>In modern Interstitial-Free (IF) steels, tiny microalloying additions of Titanium and Niobium (e.g., $0.02\text{ wt}\%\text{ Ti/Nb}$) are added during vacuum degassing. Titanium and Niobium have an immense chemical affinity for carbon and nitrogen, precipitating all interstitial solutes as ultra-stable microscopic carbo-nitrides ($\text{TiN}, \text{TiC}, \text{NbC}$). This purges the ferrite matrix of free interstitial carbon and nitrogen ($C_{\text{free}} < 0.001\text{ wt}\%$). Without dissolved interstitials, Cottrell atmospheres cannot form, rendering the steel <strong>completely immune to strain aging indefinitely</strong>.</p>
    </div>
    <div class="final-answer-box">
      <strong>Skin-Pass Rolling ($0.5\text{--}1.5\%$):</strong> Unpins dislocations, eliminating yield drop and stretcher strains.<br>
      <strong>Strain Aging:</strong> Interstitial diffusion re-pins dislocations after weeks of storage, restoring Lüders bands.<br>
      <strong>IF Steels:</strong> Microalloying with $\text{Ti/Nb}$ precipitates all free interstitials, preventing strain aging permanently.
    </div>""")

# P8: Ultimate Tensile Strength (UTS) and Necking Onset
add(8, "Ultimate Tensile Strength (UTS): Maximum Load Capacity and the Onset of Necking",
    "Yielding & Tensile Parameters", "tensile_parameters", "Fundamental",
    r"""<p>The Ultimate Tensile Strength (UTS) represents the peak engineering stress sustained by a material during a uniaxial tensile test.</p>
    <ol type="a">
      <li>Define <strong>Tensile Strength (UTS / $\sigma_u$)</strong> mathematically in terms of maximum applied load $F_{\max}$ and original area $A_0$.</li>
      <li>Explain the physical competition between <strong>strain hardening</strong> and <strong>geometric cross-sectional area reduction</strong> that produces the maximum on the engineering stress-strain curve.</li>
      <li>Prove that the mathematical condition defining the peak of the engineering stress-strain curve is:
      $$\left.\frac{d\sigma}{d\varepsilon}\right|_u = 0 \iff \left.\frac{dF}{dl}\right|_{\max} = 0$$
      and that this point marks the transition from uniform elongation to localized necking.</li>
      <li>A cylindrical aluminum tensile bar ($d_0 = 12.8 \text{ mm}$) sustains a maximum tensile load of $F_{\max} = 54.2 \text{ kN}$ before necking begins. Calculate the Ultimate Tensile Strength in megapascals.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition of Ultimate Tensile Strength</div>
      $$\sigma_{\text{UTS}} = \sigma_u = \frac{F_{\max}}{A_0} \quad [\text{MPa}]$$
      <p>where $F_{\max}$ is the absolute maximum tensile load registered by the load cell, and $A_0$ is the original, undeformed cross-sectional area of the gauge section.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Physical Competition Mechanism</div>
      <p>During plastic deformation, two opposing physical effects govern the load-bearing capacity $F = \sigma_T A$:</p>
      <ol>
        <li><strong>Strain Hardening:</strong> Dislocation multiplication and interaction increase the intrinsic flow stress $\sigma_T$ of the metal, enabling it to support greater load.</li>
        <li><strong>Cross-Sectional Area Reduction:</strong> As the specimen elongates in tension, its instantaneous cross-sectional area $A$ continuously shrinks (Poisson contraction and volume conservation), reducing the physical amount of material carrying the load.</li>
      </ol>
      <p>Prior to UTS, strain hardening outpaces area reduction ($d\sigma_T / \sigma_T > |dA| / A$), so the required load $F$ increases, and deformation remains perfectly uniform along the gauge length. At UTS, the rate of area reduction exactly balances the rate of strain hardening ($dF = 0$). Beyond UTS, geometric area reduction dominates, and deformation concentrates into a localized zone (necking).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Mathematical Condition at Maximum Load</div>
      <p>Since engineering stress is $\sigma = F/A_0$ and original area $A_0$ is constant:</p>
      $$\frac{d\sigma}{d\varepsilon} = \frac{1}{A_0} \frac{dF}{d\varepsilon} = \frac{l_0}{A_0} \frac{dF}{dl}$$
      <p>At the maximum load point $F = F_{\max}$, the load derivative is zero: $\left.\frac{dF}{dl}\right|_{\max} = 0$. Therefore:</p>
      $$\left.\frac{d\sigma}{d\varepsilon}\right|_u = 0$$
      <p>Before this point, plastic deformation is uniformly distributed over the entire gauge length ($l_0$). At and beyond this point, plastic strain localizes within a narrow necking zone; the engineering stress drops because the load cell registers falling load, even though the true local stress in the neck continues to rise until fracture.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Calculation for Aluminum Bar ($d_0 = 12.8 \text{ mm}, F_{\max} = 54.2 \text{ kN}$)</div>
      $$A_0 = \frac{\pi (12.8 \text{ mm})^2}{4} = 128.68 \text{ mm}^2 = 1.2868 \times 10^{-4} \text{ m}^2$$
      $$\sigma_{\text{UTS}} = \frac{54,200 \text{ N}}{1.2868 \times 10^{-4} \text{ m}^2} = 4.212 \times 10^8 \text{ Pa} = \mathbf{421.2 \text{ MPa}}$$
    </div>
    <div class="final-answer-box">
      <strong>UTS Definition:</strong> $\sigma_u = \frac{F_{\max}}{A_0} \implies \left.\frac{d\sigma}{d\varepsilon}\right|_u = 0$.<br>
      <strong>Physical Onset:</strong> Marks the exact transition from uniform plastic elongation to localized necking.<br>
      <strong>Calculated UTS:</strong> $\sigma_{\text{UTS}} = \mathbf{421.2 \text{ MPa}}$.
    </div>""")

# P9: Ductility Parameters (%EL and %RA)
add(9, "Ductility Quantification: Percentage Elongation, Reduction in Area, and Gauge Length Sensitivity",
    "Yielding & Tensile Parameters", "tensile_parameters", "Fundamental",
    r"""<p>Ductility is a measure of the degree of plastic deformation that a material can sustain prior to fracture.</p>
    <ol type="a">
      <li>State the mathematical definitions and formulas for:
        <ul>
          <li><strong>Percentage Elongation (%EL)</strong></li>
          <li><strong>Percentage Reduction in Area (%RA)</strong></li>
        </ul>
        defining original and post-fracture dimensions ($l_0, l_f, A_0, A_f$).</li>
      <li>Why is Percentage Elongation (%EL) heavily dependent on the chosen original gauge length $l_0$ (e.g., $l_0 = 2 \text{ in}$ vs. $l_0 = 8 \text{ in}$), whereas Percentage Reduction in Area (%RA) is virtually independent of gauge length?</li>
      <li>A round tensile specimen with initial diameter $d_0 = 12.80 \text{ mm}$ and gauge length $l_0 = 50.00 \text{ mm}$ is pulled to fracture. The two fractured pieces are fitted together:
      $$l_f = 64.50 \text{ mm}, \quad d_f = 8.60 \text{ mm} \quad (\text{at necked fracture surface})$$
      Calculate %EL and %RA for this alloy. Classify whether the material is ductile or brittle.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Formulas for Ductility</div>
      <ul>
        <li><strong>Percentage Elongation (%EL):</strong>
        $$\% \text{EL} = \frac{l_f - l_0}{l_0} \times 100\%$$
        where $l_0$ is original gauge length and $l_f$ is final gauge length measured across the fitted fracture faces.</li>
        <li><strong>Percentage Reduction in Area (%RA):</strong>
        $$\% \text{RA} = \frac{A_0 - A_f}{A_0} \times 100\%$$
        where $A_0 = \frac{\pi d_0^2}{4}$ is original area and $A_f = \frac{\pi d_f^2}{4}$ is minimum cross-sectional area at the fractured neck.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Gauge Length Sensitivity of %EL vs. %RA</div>
      <p>Total plastic elongation is the sum of uniform elongation ($\Delta l_{\text{uniform}} \propto l_0$) and localized necking elongation ($\Delta l_{\text{neck}}$, which depends only on specimen diameter $d_0$, independent of $l_0$):</p>
      $$\% \text{EL} = \frac{\Delta l_{\text{uniform}} + \Delta l_{\text{neck}}}{l_0} \times 100\% = \varepsilon_{\text{uniform}} + \frac{\Delta l_{\text{neck}}}{l_0}$$
      <p>As original gauge length $l_0$ increases (e.g., from 2 inches to 8 inches), the constant localized necking elongation $\Delta l_{\text{neck}}$ is averaged over a much longer length, causing reported %EL to drop significantly. (Therefore, ASTM standards mandate reporting gauge length, typically $l_0 = 4 d_0$ or $5 d_0$). Conversely, %RA measures true local plastic strain directly at the neck fracture surface, making it an intrinsic local material property independent of gauge length.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for Tensile Specimen</div>
      <ul>
        <li><strong>Percentage Elongation (%EL):</strong>
        $$\% \text{EL} = \frac{64.50 \text{ mm} - 50.00 \text{ mm}}{50.00 \text{ mm}} \times 100\% = \frac{14.50}{50.00} \times 100\% = \mathbf{29.0\%}$$</li>
        <li><strong>Percentage Reduction in Area (%RA):</strong>
        $$A_0 = \frac{\pi (12.80)^2}{4} = 128.68 \text{ mm}^2$$
        $$A_f = \frac{\pi (8.60)^2}{4} = 58.09 \text{ mm}^2$$
        $$\% \text{RA} = \frac{128.68 - 58.09}{128.68} \times 100\% = \frac{70.59}{128.68} \times 100\% = \mathbf{54.86\% \approx 54.9\%}$$</li>
      </ul>
      <p><strong>Classification:</strong> Materials exhibiting fracture elongation greater than $5\%$ are classified as <strong>ductile</strong>. With $\% \text{EL} = 29\%$ and $\% \text{RA} \approx 55\%$, this alloy is highly ductile.</p>
    </div>
    <div class="final-answer-box">
      <strong>Percentage Elongation:</strong> $\% \text{EL} = \mathbf{29.0\%}$.<br>
      <strong>Percentage Reduction in Area:</strong> $\% \text{RA} = \mathbf{54.9\%}$.<br>
      Classified as <strong>highly ductile</strong> (%EL $\gg 5\%$). %RA is an intrinsic local parameter independent of gauge length.
    </div>""")

# P10: Modulus of Resilience
add(10, "Modulus of Resilience: Elastic Energy Absorption and Mechanical Spring Design",
    "Yielding & Tensile Parameters", "tensile_parameters", "Intermediate",
    r"""<p>The modulus of resilience $U_r$ quantifies the capacity of a material to absorb mechanical energy during elastic loading and release it completely upon unloading.</p>
    <ol type="a">
      <li>Derive the mathematical formula for the <strong>Modulus of Resilience ($U_r$)</strong> by integrating the linear elastic stress-strain curve from $\varepsilon = 0$ to the yield strain $\varepsilon_y$:
      $$U_r = \int_0^{\varepsilon_y} \sigma d\varepsilon = \frac{\sigma_y^2}{2E}$$
      State the SI units of $U_r$.</li>
      <li>In mechanical suspension springs and archery bows, the engineering design objective is to maximize elastic energy storage per unit volume. From the derived formula, state the two mechanical property criteria that a spring alloy must possess.</li>
      <li>Calculate $U_r$ for:
        <ul>
          <li>A structural mild steel: $\sigma_y = 250 \text{ MPa}, E = 207 \text{ GPa}$.</li>
          <li>A high-strength spring steel (quenched and tempered 5160): $\sigma_y = 1500 \text{ MPa}, E = 207 \text{ GPa}$.</li>
          <li>A high-strength titanium alloy (Ti-6Al-4V aged): $\sigma_y = 1100 \text{ MPa}, E = 114 \text{ GPa}$.</li>
        </ul>
        Which material stores the most elastic energy per unit volume?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Derivation of $U_r$</div>
      <p>Modulus of resilience is the strain energy density (energy per unit volume) absorbed elastically up to the yield point:</p>
      $$U_r = \int_0^{\varepsilon_y} \sigma d\varepsilon$$
      <p>For a linear elastic material obeying Hooke's law ($\sigma = E\varepsilon \implies \varepsilon_y = \frac{\sigma_y}{E}$):</p>
      $$U_r = \int_0^{\varepsilon_y} (E\varepsilon) d\varepsilon = \frac{1}{2} E \varepsilon_y^2 = \frac{1}{2} \sigma_y \varepsilon_y = \frac{1}{2} \sigma_y \left(\frac{\sigma_y}{E}\right) = \mathbf{\frac{\sigma_y^2}{2E}}$$
      <p><strong>Units:</strong> $\frac{\text{N}\cdot\text{m}}{\text{m}^3} = \frac{\text{Joules}}{\text{m}^3} = \mathbf{\text{J/m}^3} = \text{Pa}$ (or $\text{kJ/m}^3$ or $\text{MJ/m}^3$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Spring Material Selection Criteria</div>
      <p>To maximize $U_r = \frac{\sigma_y^2}{2E}$, a material must possess:</p>
      <ol>
        <li>An extremely <strong>high yield strength ($\sigma_y$)</strong> (since $U_r$ scales quadratically as $\sigma_y^2$).</li>
        <li>A relatively <strong>low modulus of elasticity ($E$)</strong> (allowing large elastic deflections under load).</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Quantitative Resilience Comparison</div>
      <ul>
        <li><strong>Structural Mild Steel:</strong>
        $$U_r = \frac{(250 \times 10^6 \text{ Pa})^2}{2(207 \times 10^9 \text{ Pa})} = \frac{6.25 \times 10^{16}}{4.14 \times 10^{11}} = 1.51 \times 10^5 \text{ J/m}^3 = \mathbf{0.151 \text{ MJ/m}^3}$$</li>
        <li><strong>High-Strength Spring Steel (5160):</strong>
        $$U_r = \frac{(1500 \times 10^6 \text{ Pa})^2}{2(207 \times 10^9 \text{ Pa})} = \frac{2.25 \times 10^{18}}{4.14 \times 10^{11}} = 5.435 \times 10^6 \text{ J/m}^3 = \mathbf{5.44 \text{ MJ/m}^3}$$</li>
        <li><strong>Titanium Alloy (Ti-6Al-4V):</strong>
        $$U_r = \frac{(1100 \times 10^6 \text{ Pa})^2}{2(114 \times 10^9 \text{ Pa})} = \frac{1.21 \times 10^{18}}{2.28 \times 10^{11}} = 5.307 \times 10^6 \text{ J/m}^3 = \mathbf{5.31 \text{ MJ/m}^3}$$</li>
      </ul>
      <p><strong>Comparison:</strong> High-strength spring steel stores <strong>36 times more elastic energy</strong> than mild steel! Titanium is virtually equal to spring steel in volumetric resilience ($5.31 \text{ MJ/m}^3$ vs $5.44 \text{ MJ/m}^3$), but because titanium has nearly half the density of steel ($4.43 \text{ g/cm}^3$ vs $7.85 \text{ g/cm}^3$), titanium stores nearly <strong>double the elastic energy per unit weight</strong> ($U_r / \rho$), making it the premier choice for high-performance aerospace and racing vehicle springs.</p>
    </div>
    <div class="final-answer-box">
      <strong>Modulus of Resilience:</strong> $$U_r = \frac{\sigma_y^2}{2E} \quad [\text{J/m}^3]$$
      Mild Steel: $\mathbf{0.15 \text{ MJ/m}^3}$ &bull; Spring Steel: $\mathbf{5.44 \text{ MJ/m}^3}$ &bull; Titanium: $\mathbf{5.31 \text{ MJ/m}^3}$.<br>
      High $\sigma_y$ and low $E$ maximize spring energy storage.
    </div>""")

# Save checkpoint for part 1 (1 to 10)
print("Ch 6 Part 1: P1-P10 written.")
# P11: Modulus of Toughness
add(11, "Modulus of Toughness: Total Energy Absorbed Prior to Fracture",
    "Yielding & Tensile Parameters", "tensile_parameters", "Intermediate",
    r"""<p>The modulus of toughness $U_t$ represents the total mechanical energy per unit volume that a material absorbs before complete fracture occurs.</p>
    <ol type="a">
      <li>State the mathematical definition of the <strong>Modulus of Toughness ($U_t$)</strong> as the total area under the complete engineering stress-strain curve from $\varepsilon = 0$ to fracture strain $\varepsilon_f$:
      $$U_t = \int_0^{\varepsilon_f} \sigma d\varepsilon$$</li>
      <li>State standard engineering numerical approximations used to estimate $U_t$ when the explicit curve is not integrated:
        <ul>
          <li>Trapezoidal parabolic approximation: $U_t \approx \left(\frac{\sigma_y + \sigma_u}{2}\right) \varepsilon_f$</li>
          <li>Two-thirds parabolic rule for ductile metals: $U_t \approx \frac{2}{3} \sigma_u \varepsilon_f$</li>
        </ul>
      </li>
      <li>Contrast a high-strength brittle ceramic ($\sigma_y = \sigma_u = 2000 \text{ MPa}, \varepsilon_f = 0.005$) with a medium-strength ductile structural steel ($\sigma_y = 350 \text{ MPa}, \sigma_u = 550 \text{ MPa}, \varepsilon_f = 0.25$). Calculate $U_t$ for both and explain why high strength alone does not guarantee toughness.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Definition of Toughness</div>
      $$U_t = \int_0^{\varepsilon_f} \sigma d\varepsilon \quad \left[\frac{\text{Joules}}{\text{m}^3} = \text{J/m}^3 \text{ or MJ/m}^3\right]$$
      <p>Modulus of toughness represents the work of deformation required to fracture the material. It combines both strength (how high the curve reaches) and ductility (how far to the right the curve extends).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Engineering Approximation Formulas</div>
      <ul>
        <li><strong>Trapezoidal Average Rule:</strong> Approximates the plastic flow curve as a trapezoid between $\sigma_y$ and $\sigma_u$:
        $$U_t \approx \left(\frac{\sigma_y + \sigma_u}{2}\right) \varepsilon_f$$</li>
        <li><strong>Ductile Power-Law Rule:</strong> For metals with extensive strain hardening, the area is approximated well by:
        $$U_t \approx \sigma_y \varepsilon_f + \frac{\sigma_u - \sigma_y}{1 + n} \varepsilon_f \approx \frac{2}{3} \sigma_u \varepsilon_f$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): High-Strength Ceramic vs. Ductile Steel Comparison</div>
      <ul>
        <li><strong>High-Strength Brittle Ceramic:</strong>
        <p>Because deformation is purely elastic up to fracture ($\sigma_y = \sigma_u = 2000 \text{ MPa}, \varepsilon_f = 0.005$):</p>
        $$U_t = \frac{1}{2} \sigma_u \varepsilon_f = \frac{1}{2} (2000 \text{ MPa}) \times (0.005) = \mathbf{5.0 \text{ MJ/m}^3}$$
        Despite having an immense strength of $2000 \text{ MPa}$, its infinitesimal fracture strain ($0.5\%$) limits energy absorption severely.</li>
        <li><strong>Medium-Strength Ductile Steel ($\sigma_y = 350 \text{ MPa}, \sigma_u = 550 \text{ MPa}, \varepsilon_f = 0.25$):</strong>
        $$U_t \approx \left(\frac{350 + 550}{2} \text{ MPa}\right) \times 0.25 = (450 \text{ MPa}) \times 0.25 = \mathbf{112.5 \text{ MJ/m}^3}$$
        The ductile steel absorbs <strong>22.5 times more fracture energy</strong> than the ultra-strong ceramic!</li>
      </ul>
      <p><strong>Physical Principle:</strong> High strength alone is useless under impact or shock loading if not accompanied by sufficient ductility. Toughness requires a balanced combination of high yield/tensile strength AND large plastic ductility.</p>
    </div>
    <div class="final-answer-box">
      <strong>Modulus of Toughness:</strong> $$U_t = \int_0^{\varepsilon_f} \sigma d\varepsilon \approx \left(\frac{\sigma_y+\sigma_u}{2}\right)\varepsilon_f$$
      Brittle Ceramic: $U_t = \mathbf{5.0 \text{ MJ/m}^3}$ &bull; Ductile Steel: $U_t = \mathbf{112.5 \text{ MJ/m}^3}$ ($\mathbf{22.5\times}$ higher).<br>
      Toughness requires both high strength and large plastic elongation.
    </div>""")

# P12: Complete Tensile Test Comprehensive Analysis
add(12, "Comprehensive Tensile Test Data Reduction: Complete Property Evaluation",
    "Yielding & Tensile Parameters", "tensile_parameters", "Advanced",
    r"""<p>A standard cylindrical tensile specimen of an experimental titanium-aluminum alloy is tested to destruction according to ASTM E8.</p>
    <div class="highlight-box">
      <strong>Experimental Specimen & Test Data:</strong>
      <ul>
        <li>Initial Dimensions: Gauge diameter $d_0 = 12.80 \text{ mm}$, Gauge length $l_0 = 50.00 \text{ mm}$.</li>
        <li>Elastic Data: At load $F_1 = 30.0 \text{ kN}$, gauge length is $l_1 = 50.106 \text{ mm}$.</li>
        <li>Yielding: 0.2% offset line intersects curve at load $F_y = 95.0 \text{ kN}$.</li>
        <li>Maximum Load: Absolute peak load reached is $F_{\max} = 125.0 \text{ kN}$.</li>
        <li>Fracture: Specimen fractures at load $F_f = 105.0 \text{ kN}$.</li>
        <li>Final Dimensions: Gauge length at fracture $l_f = 58.50 \text{ mm}$, neck diameter $d_f = 10.20 \text{ mm}$.</li>
      </ul>
    </div>
    <ol type="a">
      <li>Calculate Young's modulus of elasticity $E$ in gigapascals.</li>
      <li>Calculate the 0.2% offset yield strength $\sigma_y$ and the ultimate tensile strength $\sigma_u$ in megapascals.</li>
      <li>Calculate the ductility parameters: %EL and %RA.</li>
      <li>Calculate the modulus of resilience $U_r$ in $\text{MJ/m}^3$.</li>
      <li>Estimate the modulus of toughness $U_t$ in $\text{MJ/m}^3$ using the trapezoidal approximation.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Young's Modulus $E$</div>
      <p>Original cross-sectional area:</p>
      $$A_0 = \frac{\pi d_0^2}{4} = \frac{\pi (12.80 \text{ mm})^2}{4} = 128.68 \text{ mm}^2 = 1.2868 \times 10^{-4} \text{ m}^2$$
      <p>Elastic stress at $F_1 = 30.0 \text{ kN}$:</p>
      $$\sigma_1 = \frac{30,000 \text{ N}}{1.2868 \times 10^{-4} \text{ m}^2} = 2.3314 \times 10^8 \text{ Pa} = 233.14 \text{ MPa}$$
      <p>Elastic strain at $l_1 = 50.106 \text{ mm}$:</p>
      $$\varepsilon_1 = \frac{50.106 - 50.000}{50.000} = \frac{0.106}{50.000} = 2.120 \times 10^{-3}$$
      $$E = \frac{\sigma_1}{\varepsilon_1} = \frac{233.14 \times 10^6 \text{ Pa}}{2.120 \times 10^{-3}} = 1.0997 \times 10^{11} \text{ Pa} = \mathbf{110.0 \text{ GPa}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Yield Strength and Ultimate Tensile Strength</div>
      $$\sigma_y = \frac{F_y}{A_0} = \frac{95,000 \text{ N}}{1.2868 \times 10^{-4} \text{ m}^2} = 7.3826 \times 10^8 \text{ Pa} = \mathbf{738.3 \text{ MPa}}$$
      $$\sigma_u = \frac{F_{\max}}{A_0} = \frac{125,000 \text{ N}}{1.2868 \times 10^{-4} \text{ m}^2} = 9.7140 \times 10^8 \text{ Pa} = \mathbf{971.4 \text{ MPa}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Ductility Calculations (%EL and %RA)</div>
      $$\% \text{EL} = \frac{l_f - l_0}{l_0} \times 100\% = \frac{58.50 - 50.00}{50.00} \times 100\% = \frac{8.50}{50.00} \times 100\% = \mathbf{17.0\%}$$
      <p>Final fractured cross-sectional area ($d_f = 10.20 \text{ mm}$):</p>
      $$A_f = \frac{\pi (10.20 \text{ mm})^2}{4} = 81.71 \text{ mm}^2$$
      $$\% \text{RA} = \frac{A_0 - A_f}{A_0} \times 100\% = \frac{128.68 - 81.71}{128.68} \times 100\% = \frac{46.97}{128.68} \times 100\% = \mathbf{36.50\% \approx 36.5\%}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Modulus of Resilience $U_r$</div>
      $$U_r = \frac{\sigma_y^2}{2E} = \frac{(738.3 \times 10^6 \text{ Pa})^2}{2(110.0 \times 10^9 \text{ Pa})} = \frac{5.4509 \times 10^{17}}{2.20 \times 10^{11}} = 2.478 \times 10^6 \text{ J/m}^3 = \mathbf{2.48 \text{ MJ/m}^3}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (e): Modulus of Toughness $U_t$</div>
      <p>Fracture engineering strain: $\varepsilon_f = \frac{8.50}{50.00} = 0.170$.</p>
      $$U_t \approx \left(\frac{\sigma_y + \sigma_u}{2}\right) \varepsilon_f = \left(\frac{738.3 + 971.4}{2} \text{ MPa}\right) \times 0.170 = (854.85 \text{ MPa}) \times 0.170 = \mathbf{145.3 \text{ MJ/m}^3}$$
    </div>
    <div class="final-answer-box">
      <strong>Mechanical Properties Summary:</strong><br>
      $E = \mathbf{110.0 \text{ GPa}}$ &bull; $\sigma_y = \mathbf{738.3 \text{ MPa}}$ &bull; $\sigma_u = \mathbf{971.4 \text{ MPa}}$<br>
      $\% \text{EL} = \mathbf{17.0\%}$ &bull; $\% \text{RA} = \mathbf{36.5\%}$ &bull; $U_r = \mathbf{2.48 \text{ MJ/m}^3}$ &bull; $U_t = \mathbf{145.3 \text{ MJ/m}^3}$.
    </div>""")

# P13: True Stress and True Strain Definitions
add(13, "True Stress and True Strain: Physical Distinction from Engineering Parameters",
    "True Stress-Strain & Plasticity", "true_stress_strain", "Fundamental",
    r"""<p>Engineering stress and strain are based on initial undeformed dimensions, obscuring the true physical state of the metal during large plastic deformation.</p>
    <ol type="a">
      <li>State the mathematical definitions of:
        <ul>
          <li><strong>True Stress ($\sigma_T$)</strong> in terms of instantaneous load $F$ and instantaneous cross-sectional area $A_i$.</li>
          <li><strong>True Strain ($\varepsilon_T$)</strong> defined as the integral of incremental strain increments $dl/l$ from original length $l_0$ to instantaneous length $l_i$:
          $$\varepsilon_T = \int_{l_0}^{l_i} \frac{dl}{l} = \ln\left(\frac{l_i}{l_0}\right)$$</li>
        </ul>
      </li>
      <li>Explain why the engineering stress-strain curve exhibits an artificial downward drop after necking, whereas the true stress-strain curve continues to rise monotonically until fracture.</li>
      <li>Explain why true strains are additive ($\varepsilon_{T, \text{total}} = \varepsilon_{T, 1} + \varepsilon_{T, 2}$), whereas engineering strains are not.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Definitions of True Stress and Strain</div>
      <ul>
        <li><strong>True Stress ($\sigma_T$):</strong> The instantaneous tensile load $F$ divided by the <em>actual instantaneous cross-sectional area</em> $A_i$ carrying that load:
        $$\sigma_T = \frac{F}{A_i} \quad [\text{MPa}]$$</li>
        <li><strong>True Strain ($\varepsilon_T$, Hencky / Logarithmic Strain):</strong> The sum of all incremental strain changes referenced to the instantaneous length $l$ at each step of deformation:
        $$\varepsilon_T = \int_{l_0}^{l_i} \frac{dl}{l} = \left[\ln l\right]_{l_0}^{l_i} = \ln\left(\frac{l_i}{l_0}\right)$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Why Engineering Stress Drops While True Stress Rises</div>
      <p>Engineering stress is calculated as $\sigma = F / A_0$, dividing instantaneous load $F$ by the <em>fixed original area</em> $A_0$. Once localized necking begins at UTS, the cross-sectional area at the neck drops much faster than the rate of strain hardening. Consequently, the total load $F$ required to continue deforming the shrinking neck decreases, causing the engineering stress curve to curve downward.</p>
      <p>True stress $\sigma_T = F / A_{\text{neck}}$ divides by the <em>true local area of the neck</em>, which is shrinking rapidly. Because dislocations continue to multiply and tangle within the neck, the metal continues to work-harden right up to the final microsecond of fracture. Thus, the true stress $\sigma_T$ rises monotonically throughout the entire test.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Additivity of True Strain</div>
      <p>Suppose a metal bar is deformed from length $l_0$ to $l_1$, and then subsequently deformed from $l_1$ to $l_2$:</p>
      $$\varepsilon_{T, \text{step 1}} = \ln\left(\frac{l_1}{l_0}\right), \quad \varepsilon_{T, \text{step 2}} = \ln\left(\frac{l_2}{l_1}\right)$$
      $$\varepsilon_{T, 1} + \varepsilon_{T, 2} = \ln\left(\frac{l_1}{l_0}\right) + \ln\left(\frac{l_2}{l_1}\right) = \ln\left(\frac{l_1}{l_0} \cdot \frac{l_2}{l_1}\right) = \ln\left(\frac{l_2}{l_0}\right) = \mathbf{\varepsilon_{T, \text{total}}}$$
      <p>For engineering strain: $\varepsilon_1 = \frac{l_1 - l_0}{l_0}, \varepsilon_2 = \frac{l_2 - l_1}{l_1}$. The sum $\varepsilon_1 + \varepsilon_2 \neq \frac{l_2 - l_0}{l_0}$ because the reference baseline changes from $l_0$ to $l_1$. The logarithmic nature of true strain makes it mathematically rigorous and additive across multi-step metal forming operations (rolling, drawing, forging).</p>
    </div>
    <div class="final-answer-box">
      <strong>True Stress & Strain:</strong> $$\sigma_T = \frac{F}{A_i}, \quad \varepsilon_T = \ln\left(\frac{l_i}{l_0}\right)$$
      Engineering stress drop after necking is an artifact of dividing by fixed $A_0$; true stress rises continuously.<br>
      True strains are strictly additive: $\varepsilon_{T, \text{total}} = \sum \varepsilon_{T, i}$.
    </div>""")

# P14: Derivation of Conversion Formulas
add(14, "Derivation of True vs. Engineering Conversion Equations Under Constant Volume",
    "True Stress-Strain & Plasticity", "true_stress_strain", "Intermediate",
    r"""<p>Prior to the onset of necking, true stress and true strain can be directly converted from engineering stress and engineering strain.</p>
    <ol type="a">
      <li>Assuming constant volume during plastic deformation ($V = A_i l_i = A_0 l_0$), derive the standard conversion relationships:
      $$\varepsilon_T = \ln(1 + \varepsilon)$$
      $$\sigma_T = \sigma (1 + \varepsilon)$$</li>
      <li>At an engineering strain of $\varepsilon = 0.050$ ($5\%$), compare $\varepsilon$ with $\varepsilon_T$, and $\sigma$ with $\sigma_T$.</li>
      <li>At an engineering strain of $\varepsilon = 0.300$ ($30\%$), calculate $\varepsilon_T$, and calculate the percentage discrepancy between engineering and true stress.</li>
      <li>Why are these conversion formulas strictly invalid <strong>after the onset of localized necking</strong>?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Derivation of Conversion Equations</div>
      <p>By definition of engineering strain: $\varepsilon = \frac{l_i - l_0}{l_0} = \frac{l_i}{l_0} - 1 \implies \frac{l_i}{l_0} = 1 + \varepsilon$.</p>
      <p>Substituting into the definition of true strain:</p>
      $$\varepsilon_T = \ln\left(\frac{l_i}{l_0}\right) = \mathbf{\ln(1 + \varepsilon)}$$
      <p>Plastic deformation occurs via dislocation glide without changing crystal density, meaning volume is strictly conserved: $A_i l_i = A_0 l_0 \implies \frac{A_0}{A_i} = \frac{l_i}{l_0} = 1 + \varepsilon$.</p>
      <p>Substituting into the definition of true stress:</p>
      $$\sigma_T = \frac{F}{A_i} = \frac{F}{A_0} \left(\frac{A_0}{A_i}\right) = \sigma \left(\frac{l_i}{l_0}\right) = \mathbf{\sigma (1 + \varepsilon)}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Comparison at $\varepsilon = 0.050$ ($5\%$ strain)</div>
      $$\varepsilon_T = \ln(1 + 0.050) = \ln(1.050) = \mathbf{0.04879}$$
      $$\sigma_T = \sigma(1 + 0.050) = \mathbf{1.050 \sigma} \quad (+5.0\% \text{ higher than }\sigma)$$
      <p>At small strains ($\varepsilon < 0.05$), engineering and true values differ by less than $2.5\%$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Comparison at $\varepsilon = 0.300$ ($30\%$ strain)</div>
      $$\varepsilon_T = \ln(1 + 0.300) = \ln(1.300) = \mathbf{0.2624}$$
      $$\sigma_T = \sigma(1 + 0.300) = \mathbf{1.300 \sigma}$$
      $$\text{Percentage Discrepancy} = \frac{\sigma_T - \sigma}{\sigma} \times 100\% = \mathbf{+30.0\%}$$
      <p>At large strains, true stress is $30\%$ higher than engineering stress, and true strain is $12.5\%$ lower than engineering strain.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Invalidation After Necking Onset</div>
      <p>The derivation relied on the assumption that elongation and area contraction are uniform along the entire gauge length ($l_i / l_0 = A_0 / A_i$). The instant necking begins, deformation concentrates into a tiny localized necking zone. The rest of the gauge section stops deforming (and actually unloads elastically!). Measuring $l_i$ across the overall gauge length no longer reflects the severe localized strain inside the neck. After necking, true stress and true strain can only be obtained by measuring the <strong>actual instantaneous neck diameter $d_i$ directly</strong>:</p>
      $$\sigma_T = \frac{4F}{\pi d_{\text{neck}}^2}, \quad \varepsilon_T = \ln\left(\frac{A_0}{A_{\text{neck}}}\right) = 2\ln\left(\frac{d_0}{d_{\text{neck}}}\right)$$
    </div>
    <div class="final-answer-box">
      <strong>Conversion Laws:</strong> $$\varepsilon_T = \ln(1+\varepsilon), \quad \sigma_T = \sigma(1+\varepsilon)$$
      Valid strictly up to the onset of necking (uniform deformation).<br>
      Beyond necking, true parameters must be measured directly from actual neck diameter $d_{\text{neck}}$.
    </div>""")

# P15: Bridgman Correction Factor for Triaxial Neck Stresses
add(15, "Post-Necking Plasticity: Triaxial Stress States and the Bridgman Correction Factor",
    "True Stress-Strain & Plasticity", "true_stress_strain", "Advanced",
    r"""<p>Once localized necking forms in a cylindrical tensile bar, the geometry of the neck alters the internal stress field from simple uniaxial tension to a complex triaxial state.</p>
    <ol type="a">
      <li>Explain why the geometric curvature of the neck profile induces radial ($\sigma_r$) and circumferential ($\sigma_\theta$) tensile stresses in the interior of the neck, creating a <strong>hydrostatic tensile stress state</strong> ($\sigma_h > 0$) along the specimen centerline.</li>
      <li>Why does the apparent average true stress $\sigma_{T, \text{avg}} = F / A_{\text{neck}}$ overestimate the true equivalent flow stress $\bar{\sigma}$ required for plastic dislocation slip?</li>
      <li>State <strong>Bridgman's Correction Formula</strong> for calculating the true equivalent flow stress $\bar{\sigma}$:
      $$\bar{\sigma} = \frac{\sigma_{T, \text{avg}}}{\left(1 + \frac{2R}{a}\right) \ln\left(1 + \frac{a}{2R}\right)}$$
      defining the neck radius $a$ and profile radius of curvature $R$.</li>
      <li>At fracture, a steel tensile bar has a neck radius $a = 4.0 \text{ mm}$ and neck curvature radius $R = 8.0 \text{ mm}$. The fracture load is $F_f = 60.0 \text{ kN}$. Calculate the uncorrected average true fracture stress $\sigma_{T, \text{avg}}$ and the true Bridgman-corrected flow stress $\bar{\sigma}$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Origin of Triaxial Stresses in the Neck</div>
      <p>Before necking, the specimen surface is straight and parallel; outer surface elements are traction-free, ensuring a strictly 1D uniaxial stress state ($\sigma_z = \sigma, \sigma_r = \sigma_\theta = 0$). When a curved neck forms, the longitudinal stress trajectories bend inward following the concave profile. To satisfy differential equilibrium of forces in cylindrical coordinates ($\frac{\partial\sigma_r}{\partial r} + \frac{\sigma_r - \sigma_\theta}{r} + \frac{\partial\tau_{rz}}{\partial z} = 0$), radial and hoop tensile stresses ($\sigma_r = \sigma_\theta > 0$) must develop inside the neck. These lateral tensile stresses reach their maximum at the center axis ($r = 0$), generating an intense <strong>triaxial hydrostatic tensile stress state</strong> ($\sigma_h = \frac{\sigma_z + 2\sigma_r}{3} > 0$) that drives ductile microvoid cavitation and initiates cup-and-cone fracture at the center.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Overestimation by Average True Stress</div>
      <p>According to the von Mises yield criterion, plastic dislocation glide is driven purely by <strong>deviatoric shear stresses</strong> ($\sigma_{\text{eff}} = \sigma_z - \sigma_r$), completely unaffected by hydrostatic tension $\sigma_h$. Because the lateral stresses $\sigma_r$ and $\sigma_\theta$ are positive (tensile), a higher longitudinal stress $\sigma_z$ is required to achieve the same effective shear stress $(\sigma_z - \sigma_r = \bar{\sigma})$. The simple average $\sigma_{T, \text{avg}} = F / A$ measures total longitudinal load, thus significantly overestimating the true material yield flow stress.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c) & (d): Bridgman Correction Calculation</div>
      <p>Given $a = 4.0 \text{ mm}$ (neck radius), $R = 8.0 \text{ mm}$ (profile radius), $F_f = 60.0 \text{ kN}$:</p>
      <p>Neck cross-sectional area:</p>
      $$A_{\text{neck}} = \pi a^2 = \pi (4.0 \times 10^{-3} \text{ m})^2 = 5.0265 \times 10^{-5} \text{ m}^2$$
      <p>Uncorrected average true stress:</p>
      $$\sigma_{T, \text{avg}} = \frac{60,000 \text{ N}}{5.0265 \times 10^{-5} \text{ m}^2} = 1.1937 \times 10^9 \text{ Pa} = \mathbf{1193.7 \text{ MPa}}$$
      <p>Calculate the Bridgman geometry ratio $\frac{a}{2R}$:</p>
      $$\frac{a}{2R} = \frac{4.0 \text{ mm}}{2 \times 8.0 \text{ mm}} = \frac{4.0}{16.0} = 0.250$$
      $$\frac{2R}{a} = \frac{1}{0.250} = 4.00$$
      <p>Bridgman correction factor $B$:</p>
      $$B = \left(1 + \frac{2R}{a}\right) \ln\left(1 + \frac{a}{2R}\right) = (1 + 4.00) \ln(1 + 0.250) = 5.00 \times \ln(1.250) = 5.00 \times 0.22314 = \mathbf{1.1157}$$
      <p>Bridgman-corrected equivalent flow stress $\bar{\sigma}$:</p>
      $$\bar{\sigma} = \frac{\sigma_{T, \text{avg}}}{B} = \frac{1193.7 \text{ MPa}}{1.1157} = \mathbf{1070.0 \text{ MPa}}$$
      <p>The triaxial stress state in the neck inflated the apparent true stress by $123.7 \text{ MPa}$ ($11.6\%$).</p>
    </div>
    <div class="final-answer-box">
      <strong>Bridgman Formula:</strong> $$\bar{\sigma} = \frac{\sigma_{T, \text{avg}}}{(1 + 2R/a)\ln(1 + a/2R)}$$
      <strong>Uncorrected True Stress:</strong> $\sigma_{T, \text{avg}} = \mathbf{1193.7 \text{ MPa}}$.<br>
      <strong>Bridgman-Corrected Flow Stress:</strong> $\bar{\sigma} = \mathbf{1070.0 \text{ MPa}}$ ($11.6\%$ correction).
    </div>""")

# Save checkpoint for part 1 (1 to 15)
print("Ch 6 Part 1: P1-P15 written.")
# P16: Hollomon Strain Hardening Law
add(16, "The Hollomon Power-Law Equation: Strength Coefficient $K$ and Strain-Hardening Exponent $n$",
    "True Stress-Strain & Plasticity", "true_stress_strain", "Fundamental",
    r"""<p>For most engineering metals subjected to plastic deformation, the true stress-strain curve in the uniform plastic region is described by the Hollomon equation.</p>
    <ol type="a">
      <li>State the <strong>Hollomon equation</strong>:
      $$\sigma_T = K \varepsilon_T^n$$
      Define the <strong>Strength Coefficient $K$</strong> and the <strong>Strain-Hardening Exponent $n$</strong>. State their physical meanings and standard units.</li>
      <li>What is the physical meaning of $n = 0$ (perfectly plastic solid) versus $n = 1$ (perfectly elastic solid)?</li>
      <li>State typical values of $n$ for:
        <ul>
          <li>FCC metals with low stacking fault energy (e.g., 70-30 brass, austenitic stainless steel).</li>
          <li>BCC metals (e.g., low-carbon structural steel).</li>
          <li>Heavily cold-worked metals.</li>
        </ul>
      </li>
      <li>Explain why sheet metal stampings (e.g., automotive deep-drawn panels) require metals with high values of $n$ ($n \ge 0.20\text{--}0.45$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): The Hollomon Power-Law Equation</div>
      $$\sigma_T = K \varepsilon_T^n$$
      <ul>
        <li>$\sigma_T$: True flow stress ($\mathbf{\text{MPa}}$).</li>
        <li>$\varepsilon_T$: True plastic strain (dimensionless).</li>
        <li>$K$: <strong>Strength Coefficient</strong>. Represents the true stress required to sustain a true plastic strain of $\varepsilon_T = 1.0$ (since $1.0^n = 1$). Units: $\mathbf{\text{MPa}}$.</li>
        <li>$n$: <strong>Strain-Hardening Exponent</strong> (dimensionless, typically $0.10 \le n \le 0.50$). It measures the ability of a metal to work-harden and resist strain localization under increasing plastic strain:
        $$n = \frac{d(\ln\sigma_T)}{d(\ln\varepsilon_T)} = \frac{\varepsilon_T}{\sigma_T} \frac{d\sigma_T}{d\varepsilon_T}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Physical Limiting Cases of $n$</div>
      <ul>
        <li><strong>$n = 0$ (Rigid-Perfectly Plastic):</strong> The flow stress is independent of strain ($\sigma_T = K = \text{const}$). The material exhibits zero work hardening; once yield is reached, deformation localizes instantly into a neck without uniform elongation (typical of lead at room temperature or metals undergoing superplastic flow).</li>
        <li><strong>$n = 1$ (Linear Elastic / Hardening):</strong> The flow stress increases linearly with strain ($\sigma_T = K \varepsilon_T$), behaving analogously to Hooke's law.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Typical Magnitudes of $n$</div>
      <ul>
        <li><strong>Low-SFE FCC Metals (Brass, 304 Stainless):</strong> $n \approx 0.40\text{ to }0.55$ (exceptionally high strain-hardening rate due to wide partial dislocation ribbons blocking cross-slip).</li>
        <li><strong>BCC Metals (Low-Carbon Steels):</strong> $n \approx 0.15\text{ to }0.25$ (moderate strain hardening; cross-slip occurs readily).</li>
        <li><strong>High-SFE FCC Metals (Aluminum, Copper):</strong> $n \approx 0.20\text{ to }0.35$.</li>
        <li><strong>Heavily Cold-Worked Metals:</strong> $n \approx 0.02\text{ to }0.05$ (dislocation density is already saturated near $\sim 10^{12} \text{ cm}^{-2}$, leaving virtually zero capacity for further work hardening).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Importance in Sheet Metal Deep Drawing</div>
      <p>In sheet metal press stamping, the punch exerts intense tensile stretching over punch radii. If a local region thins slightly, a high-$n$ material rapidly work-hardens in that thinned area, raising its local flow stress. This forces subsequent deformation to shift to adjacent, thicker unhardened regions of the sheet. Thus, high $n$ spreads plastic deformation uniformly across the entire panel, suppressing necking, preventing tearing, and maximizing the maximum draw depth (Limiting Draw Ratio).</p>
    </div>
    <div class="final-answer-box">
      <strong>Hollomon Law:</strong> $$\sigma_T = K \varepsilon_T^n$$
      $K$: Stress at $\varepsilon_T = 1.0$ &bull; $n$: Strain hardening index ($0 < n < 1$).<br>
      High $n$ ($0.4\text{--}0.5$ in brass/stainless) delays localized necking, maximizing formability.
    </div>""")

# P17: Determination of Hollomon Parameters
add(17, "Determination of Hollomon Parameters ($n$ and $K$) from Experimental Tensile Data",
    "True Stress-Strain & Plasticity", "true_stress_strain", "Intermediate",
    r"""<p>The strain-hardening exponent $n$ and strength coefficient $K$ are extracted from true stress-strain data using logarithmic linearization.</p>
    <div style="text-align:center; margin: 10px 0;">
      A low-alloy structural steel yields the following true stress-strain data points during uniform plastic deformation:<br>
      Point 1: At $\varepsilon_{T, 1} = 0.050$, $\sigma_{T, 1} = 485.0 \text{ MPa}$<br>
      Point 2: At $\varepsilon_{T, 2} = 0.180$, $\sigma_{T, 2} = 650.0 \text{ MPa}$
    </div>
    <ol type="a">
      <li>Derive the algebraic formulas for $n$ and $K$ by linearizing the Hollomon equation ($\ln\sigma_T = \ln K + n \ln\varepsilon_T$).</li>
      <li>Calculate the strain-hardening exponent $n$ for this steel.</li>
      <li>Calculate the strength coefficient $K$ in megapascals.</li>
      <li>Predict the true stress required to sustain a true plastic strain of $\varepsilon_T = 0.100$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Linearization Derivation</div>
      <p>Taking the natural logarithm of both sides of $\sigma_T = K \varepsilon_T^n$:</p>
      $$\ln\sigma_T = \ln K + n \ln\varepsilon_T$$
      <p>Evaluating at two experimental points $(\varepsilon_{T, 1}, \sigma_{T, 1})$ and $(\varepsilon_{T, 2}, \sigma_{T, 2})$ and subtracting:</p>
      $$\ln\sigma_{T, 2} - \ln\sigma_{T, 1} = n (\ln\varepsilon_{T, 2} - \ln\varepsilon_{T, 1}) \implies n = \frac{\ln(\sigma_{T, 2} / \sigma_{T, 1})}{\ln(\varepsilon_{T, 2} / \varepsilon_{T, 1})}$$
      <p>Once $n$ is known, $K$ is obtained from either point:</p>
      $$K = \frac{\sigma_{T, 1}}{\varepsilon_{T, 1}^n} = \frac{\sigma_{T, 2}}{\varepsilon_{T, 2}^n}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation of Strain-Hardening Exponent $n$</div>
      $$\frac{\sigma_{T, 2}}{\sigma_{T, 1}} = \frac{650.0 \text{ MPa}}{485.0 \text{ MPa}} = 1.3402 \implies \ln(1.3402) = 0.29282$$
      $$\frac{\varepsilon_{T, 2}}{\varepsilon_{T, 1}} = \frac{0.180}{0.050} = 3.600 \implies \ln(3.600) = 1.28093$$
      $$n = \frac{0.29282}{1.28093} = \mathbf{0.2286 \approx 0.23}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation of Strength Coefficient $K$</div>
      $$K = \frac{\sigma_{T, 1}}{\varepsilon_{T, 1}^n} = \frac{485.0 \text{ MPa}}{(0.050)^{0.2286}}$$
      $$\ln(0.050) = -2.9957 \implies (0.050)^{0.2286} = \exp(0.2286 \times -2.9957) = \exp(-0.6848) = 0.50418$$
      $$K = \frac{485.0 \text{ MPa}}{0.50418} = \mathbf{961.96 \text{ MPa} \approx 962 \text{ MPa}}$$
      <p>Verification using Point 2: $K = \frac{650.0}{(0.180)^{0.2286}} = \frac{650.0}{0.6757} = 961.96 \text{ MPa}$ (exact match).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Predicted True Stress at $\varepsilon_T = 0.100$</div>
      $$\sigma_T = K \varepsilon_T^n = (961.96 \text{ MPa}) \times (0.100)^{0.2286}$$
      $$(0.100)^{0.2286} = \exp(0.2286 \times \ln(0.100)) = \exp(0.2286 \times -2.3026) = \exp(-0.52637) = 0.59074$$
      $$\sigma_T = 961.96 \times 0.59074 = \mathbf{568.3 \text{ MPa}}$$
    </div>
    <div class="final-answer-box">
      <strong>Strain-Hardening Exponent:</strong> $n = \mathbf{0.229}$.<br>
      <strong>Strength Coefficient:</strong> $K = \mathbf{962 \text{ MPa}}$.<br>
      <strong>Flow Equation:</strong> $\sigma_T = 962 \varepsilon_T^{0.229} \text{ MPa} \implies \sigma_T(0.10) = \mathbf{568.3 \text{ MPa}}$.
    </div>""")

# P18: Considère's Criterion Proof
add(18, "Considère's Construction: Mathematical Proof that $\\varepsilon_{T, u} = n$ at Maximum Load",
    "True Stress-Strain & Plasticity", "true_stress_strain", "Advanced",
    r"""<p>In 1885, Armand Considère derived the rigorous mathematical condition governing the onset of plastic instability (necking) in uniaxial tension.</p>
    <ol type="a">
      <li>Starting from the condition of maximum tensile load ($dF = 0$), derive <strong>Considère's Criterion</strong> in terms of true stress $\sigma_T$ and true strain $\varepsilon_T$:
      $$\frac{d\sigma_T}{d\varepsilon_T} = \sigma_T$$
      Explain the geometric interpretation of this condition on a plot of $\sigma_T$ versus $\varepsilon_T$.</li>
      <li>Assuming the material follows the Hollomon power law $\sigma_T = K \varepsilon_T^n$, differentiate the equation and substitute into Considère's criterion to prove the famous theorem:
      $$\varepsilon_{T, u} = n$$
      stating that the <strong>true uniform strain at the onset of necking is identically equal to the strain-hardening exponent</strong>.</li>
      <li>Calculate the maximum engineering strain $\varepsilon_u$ at necking for a brass alloy with $n = 0.45$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Considère's Criterion</div>
      <p>The instantaneous tensile load supported by the specimen is $F = \sigma_T A$.</p>
      <p>At the maximum load point (UTS), the differential of load is zero:</p>
      $$dF = 0 \implies d(\sigma_T A) = \sigma_T dA + A d\sigma_T = 0 \implies A d\sigma_T = -\sigma_T dA \implies \frac{d\sigma_T}{\sigma_T} = -\frac{dA}{A}$$
      <p>During plastic deformation, volume is strictly conserved ($V = A l = \text{const}$):</p>
      $$dV = A dl + l dA = 0 \implies -\frac{dA}{A} = \frac{dl}{l} \equiv d\varepsilon_T$$
      <p>Substituting $-\frac{dA}{A} = d\varepsilon_T$ into the load equation:</p>
      $$\frac{d\sigma_T}{\sigma_T} = d\varepsilon_T \implies \mathbf{\frac{d\sigma_T}{d\varepsilon_T} = \sigma_T}$$
      <p><strong>Geometric Interpretation:</strong> Necking begins at the exact point on the true stress-strain curve where the <strong>slope (the rate of strain hardening $\frac{d\sigma_T}{d\varepsilon_T}$) becomes numerically equal to the stress itself ($\sigma_T$)</strong>. In Considère's geometric construction, drawing a tangent from $(-1, 0)$ on the true strain axis to the true stress-strain curve identifies the exact necking point.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Proof that $\varepsilon_{T, u} = n$ for Hollomon Power Law</div>
      <p>Given the Hollomon equation: $\sigma_T = K \varepsilon_T^n$. Differentiating with respect to $\varepsilon_T$:</p>
      $$\frac{d\sigma_T}{d\varepsilon_T} = \frac{d}{d\varepsilon_T}(K \varepsilon_T^n) = n K \varepsilon_T^{n-1} = n \left(\frac{K \varepsilon_T^n}{\varepsilon_T}\right) = \frac{n \sigma_T}{\varepsilon_T}$$
      <p>Equating this derivative to Considère's necking criterion ($\frac{d\sigma_T}{d\varepsilon_T} = \sigma_T$):</p>
      $$\frac{n \sigma_T}{\varepsilon_{T, u}} = \sigma_T \implies \frac{n}{\varepsilon_{T, u}} = 1 \implies \mathbf{\varepsilon_{T, u} = n}$$
      <p>This elegant theorem proves that a material's capacity for uniform elongation prior to necking is dictated strictly by its strain-hardening exponent $n$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Maximum Engineering Strain for Brass ($n = 0.45$)</div>
      <p>From Considère's theorem, true strain at necking is $\varepsilon_{T, u} = n = 0.45$.</p>
      <p>Using the conversion formula $\varepsilon_T = \ln(1 + \varepsilon)$:</p>
      $$\ln(1 + \varepsilon_u) = 0.45 \implies 1 + \varepsilon_u = \exp(0.45) = 1.5683$$
      $$\varepsilon_u = 1.5683 - 1 = \mathbf{0.5683 = 56.8\%}$$
      <p>Cartridge brass can sustain an astonishing <strong>$56.8\%$ engineering strain</strong> uniformly across its entire length before localized necking begins!</p>
    </div>
    <div class="final-answer-box">
      <strong>Considère's Criterion:</strong> $$\frac{d\sigma_T}{d\varepsilon_T} = \sigma_T$$
      <strong>Proof for Hollomon Law:</strong> $\frac{n\sigma_T}{\varepsilon_T} = \sigma_T \implies \mathbf{\varepsilon_{T, u} = n}$.<br>
      <strong>For Brass ($n = 0.45$):</strong> Uniform engineering elongation reaches $\varepsilon_u = \mathbf{56.8\%}$ prior to necking.
    </div>""")

# P19: Plastic Work of Deformation
add(19, "Plastic Work of Deformation: Energy per Unit Volume in Bulk Metal Forming",
    "True Stress-Strain & Plasticity", "true_stress_strain", "Intermediate",
    r"""<p>In industrial bulk metalworking processes (cold rolling, wire drawing, forging), engineers must calculate the total mechanical work required to plastically deform a workpiece.</p>
    <ol type="a">
      <li>Derive the formula for the plastic work done per unit volume $w_p$ (in $\text{J/m}^3$) by integrating the Hollomon true stress-strain curve from $\varepsilon_T = 0$ to final plastic strain $\varepsilon_T$:
      $$w_p = \int_0^{\varepsilon_T} \sigma_T d\varepsilon_T = \frac{K \varepsilon_T^{n+1}}{n + 1}$$</li>
      <li>A cylindrical copper billet ($K = 320 \text{ MPa}, n = 0.35$) of initial diameter $d_0 = 50.0 \text{ mm}$ and length $l_0 = 100.0 \text{ mm}$ is cold-extruded into a rod of diameter $d_1 = 25.0 \text{ mm}$. Calculate:
        <ul>
          <li>The true extrusion strain $\varepsilon_T = 2\ln(d_0 / d_1)$.</li>
          <li>The plastic work done per unit volume $w_p$ in $\text{MJ/m}^3$.</li>
          <li>The total mechanical energy $W_{\text{total}}$ in kilojoules ($\text{kJ}$) required to extrude the billet.</li>
        </ul>
      </li>
      <li>Assuming $90\%$ of this plastic deformation work is converted into heat (Taylor-Quinney factor $\beta = 0.90$) under adiabatic high-speed forming, calculate the temperature rise $\Delta T$ of the extruded copper rod ($\rho = 8940 \text{ kg/m}^3, c_p = 385 \text{ J/(kg}\cdot\text{K)}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Plastic Work Formula</div>
      $$w_p = \int_0^{\varepsilon_T} \sigma_T d\varepsilon_T = \int_0^{\varepsilon_T} (K \varepsilon^{n}) d\varepsilon = K \left[ \frac{\varepsilon^{n+1}}{n + 1} \right]_0^{\varepsilon_T} = \mathbf{\frac{K \varepsilon_T^{n+1}}{n + 1}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Extrusion Strain and Work Calculations</div>
      <ul>
        <li><strong>True Extrusion Strain:</strong>
        $$\varepsilon_T = \ln\left(\frac{A_0}{A_1}\right) = \ln\left(\frac{d_0^2}{d_1^2}\right) = 2 \ln\left(\frac{d_0}{d_1}\right) = 2 \ln\left(\frac{50.0 \text{ mm}}{25.0 \text{ mm}}\right) = 2 \ln(2.0) = 2 \times 0.69315 = \mathbf{1.3863}$$</li>
        <li><strong>Plastic Work per Unit Volume:</strong>
        $$n + 1 = 0.35 + 1 = 1.35$$
        $$\varepsilon_T^{n+1} = (1.3863)^{1.35} = \exp(1.35 \times \ln(1.3863)) = \exp(1.35 \times 0.3266) = \exp(0.4409) = 1.5541$$
        $$w_p = \frac{(320 \times 10^6 \text{ Pa}) \times 1.5541}{1.35} = \frac{4.9731 \times 10^8}{1.35} = 3.6838 \times 10^8 \text{ J/m}^3 = \mathbf{368.4 \text{ MJ/m}^3}$$</li>
        <li><strong>Total Extrusion Energy ($W_{\text{total}}$):</strong>
        <p>Billet volume $V_0 = \frac{\pi d_0^2}{4} l_0 = \frac{\pi (0.050 \text{ m})^2}{4} \times (0.100 \text{ m}) = (1.9635 \times 10^{-3} \text{ m}^2) \times 0.100 \text{ m} = 1.9635 \times 10^{-4} \text{ m}^3$.</p>
        $$W_{\text{total}} = w_p \times V_0 = (3.6838 \times 10^8 \text{ J/m}^3) \times (1.9635 \times 10^{-4} \text{ m}^3) = 72,331 \text{ J} = \mathbf{72.33 \text{ kJ}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Adiabatic Temperature Rise $\Delta T$ ($\beta = 0.90$)</div>
      <p>Thermal energy absorbed per unit volume is $q = \beta w_p = \rho c_p \Delta T$:</p>
      $$\Delta T = \frac{\beta w_p}{\rho c_p} = \frac{0.90 \times (3.6838 \times 10^8 \text{ J/m}^3)}{(8940 \text{ kg/m}^3) \times (385 \text{ J/(kg}\cdot\text{K)})} = \frac{3.3154 \times 10^8}{3.4419 \times 10^6} = \mathbf{96.3^\circ\text{C}}$$
      <p>The plastic deformation work heats the freshly extruded copper rod by nearly $100^\circ\text{C}$!</p>
    </div>
    <div class="final-answer-box">
      <strong>Plastic Work Formula:</strong> $$w_p = \frac{K \varepsilon_T^{n+1}}{n+1} \implies w_p = \mathbf{368.4 \text{ MJ/m}^3}$$
      <strong>True Strain:</strong> $\varepsilon_T = \mathbf{1.386}$ &bull; <strong>Total Extrusion Work:</strong> $W_{\text{total}} = \mathbf{72.3 \text{ kJ}}$.<br>
      <strong>Adiabatic Heating:</strong> $\Delta T = \mathbf{96.3^\circ\text{C}}$ temperature rise.
    </div>""")

# P20: Schmid's Law Derivation
add(20, "Schmid's Law: Geometric Derivation of Resolved Shear Stress $\\tau_R$",
    "Single-Crystal Plasticity & Schmid's Law", "schmids_law", "Fundamental",
    r"""<p>Plastic deformation in crystalline solids occurs via shear slip along close-packed planes in close-packed directions.</p>
    <ol type="a">
      <li>Consider a cylindrical single-crystal tensile specimen of cross-sectional area $A_0$ loaded by uniaxial tensile force $F$. Let the slip plane normal vector $\mathbf{n}$ make angle $\phi$ with the tensile axis, and let the slip direction $\mathbf{s}$ make angle $\lambda$ with the tensile axis. Derive <strong>Schmid's Law</strong> for the resolved shear stress $\tau_R$:
      $$\tau_R = \sigma \cos\phi \cos\lambda$$
      where $\sigma = F / A_0$ is the applied engineering tensile stress.</li>
      <li>Define the <strong>Schmid Factor</strong> $m = \cos\phi \cos\lambda$.</li>
      <li>State the geometric restriction between angles $\phi$ and $\lambda$. What is the theoretical maximum value of the Schmid factor ($m_{\max}$), and at what specific angles does it occur?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Geometric Derivation of Schmid's Law</div>
      <p>Consider a slip plane slicing through the cylindrical crystal at angle $\phi$ to the cross-sectional plane:</p>
      <ol>
        <li><strong>Area of the Slip Plane ($A_s$):</strong>
          The normal to the slip plane makes angle $\phi$ with the tensile axis. The projected area on the horizontal plane is $A_0 = A_s \cos\phi$. Therefore, the actual area of the inclined slip plane is:
          $$A_s = \frac{A_0}{\cos\phi}$$
        </li>
        <li><strong>Resolved Force Component along Slip Direction ($F_s$):</strong>
          The tensile force $F$ acts along the specimen cylinder axis. The slip direction vector lies within the slip plane and makes angle $\lambda$ with the tensile force vector. The component of tensile force directed parallel to the slip direction is:
          $$F_s = F \cos\lambda$$
        </li>
        <li><strong>Resolved Shear Stress ($\tau_R$):</strong>
          By definition, shear stress is resolved shear force divided by slip plane area:
          $$\tau_R = \frac{F_s}{A_s} = \frac{F \cos\lambda}{\frac{A_0}{\cos\phi}} = \left(\frac{F}{A_0}\right) \cos\phi \cos\lambda = \mathbf{\sigma \cos\phi \cos\lambda}$$
        </li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): The Schmid Factor $m$</div>
      $$m = \cos\phi \cos\lambda \implies \tau_R = m \cdot \sigma$$
      <p>The Schmid factor $m$ is a purely geometric orientation factor (dimensionless, $0 \le m \le 0.5$) that quantifies the fraction of applied tensile stress converted into shear stress driving dislocation motion on a specific slip system.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Geometric Bounds and Maximum Schmid Factor</div>
      <p>Because the slip direction $\mathbf{s}$ lies entirely within the slip plane, it is strictly perpendicular to the slip plane normal $\mathbf{n}$ ($\mathbf{s} \cdot \mathbf{n} = 0$). By spherical trigonometry, the sum of angles satisfies:</p>
      $$\phi + \lambda \ge 90^\circ$$
      <p>To maximize $m = \cos\phi \cos\lambda$, the tensile axis must lie in the plane containing both $\mathbf{n}$ and $\mathbf{s}$, giving $\phi + \lambda = 90^\circ \implies \lambda = 90^\circ - \phi$.</p>
      $$m = \cos\phi \cos(90^\circ - \phi) = \cos\phi \sin\phi = \frac{1}{2} \sin(2\phi)$$
      <p>The maximum value of $\sin(2\phi)$ is $1.0$, occurring when $2\phi = 90^\circ \implies \phi = 45^\circ$:</p>
      $$\mathbf{m_{\max} = 0.500 \quad \text{at } \phi = 45^\circ \text{ and } \lambda = 45^\circ}$$
    </div>
    <div class="final-answer-box">
      <strong>Schmid's Law:</strong> $$\tau_R = \sigma \cos\phi \cos\lambda = m \cdot \sigma$$
      <strong>Schmid Factor:</strong> $m = \cos\phi \cos\lambda$ &bull; Bounds: $0 \le m \le 0.5$.<br>
      <strong>Maximum Value:</strong> $m_{\max} = \mathbf{0.500}$ when $\phi = \lambda = \mathbf{45^\circ}$.
    </div>""")

# P21: Critical Resolved Shear Stress
add(21, "Critical Resolved Shear Stress (CRSS): Single Crystal Yield Criterion",
    "Single-Crystal Plasticity & Schmid's Law", "schmids_law", "Fundamental",
    r"""<p>Plastic yielding in a single crystal initiates when the resolved shear stress on the most favorably oriented slip system reaches a critical threshold value.</p>
    <ol type="a">
      <li>State the <strong>Critical Resolved Shear Stress ($\tau_{\text{CRSS}}$)</strong> yield criterion. Explain why $\tau_{\text{CRSS}}$ is an intrinsic material property independent of crystal orientation, whereas the macroscopic tensile yield strength $\sigma_y$ varies wildly with orientation:
      $$\sigma_y = \frac{\tau_{\text{CRSS}}}{m_{\max}} = \frac{\tau_{\text{CRSS}}}{(\cos\phi \cos\lambda)_{\max}}$$</li>
      <li>Distinguish between a <strong>"soft orientation"</strong> ($m \approx 0.5$) and a <strong>"hard orientation"</strong> ($m \ll 0.5$).</li>
      <li>What happens to macroscopic yield strength if the tensile axis is aligned precisely perpendicular to the slip plane ($\phi = 0^\circ$) or parallel to the slip plane ($\phi = 90^\circ$)?</li>
      <li>A zinc single crystal (HCP, basal slip on $(0001)\langle 11\bar{2}0\rangle$) has $\tau_{\text{CRSS}} = 0.18 \text{ MPa}$. Calculate the macroscopic tensile yield strength $\sigma_y$ when the tensile axis is oriented such that $\phi = 62.0^\circ$ and $\lambda = 34.0^\circ$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): CRSS Yield Criterion</div>
      <p>Plastic deformation initiates in a single crystal when the resolved shear stress $\tau_R$ on any available slip system first reaches the <strong>Critical Resolved Shear Stress ($\tau_{\text{CRSS}}$)</strong>:</p>
      $$\tau_R = \sigma \cos\phi \cos\lambda \ge \tau_{\text{CRSS}}$$
      <p>$\tau_{\text{CRSS}}$ represents the intrinsic lattice resistance (Peierls-Nabarro friction stress + obstacle resistance) required to move dislocations along close-packed planes. It is a fundamental thermodynamic material property for a given metal and temperature, completely independent of how the tensile specimen is cut. In contrast, the macroscopic tensile yield strength $\sigma_y$ is:</p>
      $$\sigma_y = \frac{\tau_{\text{CRSS}}}{m_{\max}}$$
      <p>Because the Schmid factor $m_{\max}$ depends entirely on specimen loading orientation, $\sigma_y$ is highly anisotropic.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b) & (c): Soft Orientations, Hard Orientations, and Singularities</div>
      <ul>
        <li><strong>Soft Orientation ($m \to 0.5$):</strong> The slip plane and slip direction both make $\approx 45^\circ$ with the tensile axis. The applied tensile stress is maximally converted into resolved shear stress. Macroscopic yield strength reaches its absolute minimum: $\sigma_{y, \min} = \frac{\tau_{\text{CRSS}}}{0.5} = \mathbf{2 \tau_{\text{CRSS}}}$.</li>
        <li><strong>Hard Orientation ($m \to 0$):</strong> The slip system is oriented unfavorably. Extremely high macroscopic tensile stress is required to produce even minimal shear stress.</li>
        <li><strong>Singularities ($\phi = 0^\circ$ or $\phi = 90^\circ$):</strong>
          <ul>
            <li>If $\phi = 0^\circ$ (tension normal to slip plane): $\lambda = 90^\circ \implies \cos\lambda = 0 \implies m = 0$.</li>
            <li>If $\phi = 90^\circ$ (tension in slip plane): $\cos\phi = 0 \implies m = 0$.</li>
            <li>In both cases, $\tau_R \equiv 0$ regardless of how large the applied tensile stress $\sigma$ is! Slip on this system is physically impossible ($\sigma_y \to \infty$). The crystal must either activate a different, higher-order slip system, twin, or undergo brittle cleavage fracture.</li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Calculation for Zinc Single Crystal ($\phi = 62.0^\circ, \lambda = 34.0^\circ$)</div>
      $$\cos\phi = \cos(62.0^\circ) = 0.46947$$
      $$\cos\lambda = \cos(34.0^\circ) = 0.82904$$
      $$m = \cos\phi \cos\lambda = 0.46947 \times 0.82904 = \mathbf{0.3892}$$
      <p>Applying the CRSS yield formula ($\tau_{\text{CRSS}} = 0.18 \text{ MPa}$):</p>
      $$\sigma_y = \frac{\tau_{\text{CRSS}}}{m} = \frac{0.18 \text{ MPa}}{0.3892} = \mathbf{0.4625 \text{ MPa}}$$
    </div>
    <div class="final-answer-box">
      <strong>CRSS Law:</strong> $$\sigma_y = \frac{\tau_{\text{CRSS}}}{m} = \frac{\tau_{\text{CRSS}}}{\cos\phi \cos\lambda}$$
      <strong>Soft Orientation ($m=0.5$):</strong> $\sigma_y = 2\tau_{\text{CRSS}}$ (minimum yield strength).<br>
      <strong>Zinc Crystal Yield Strength:</strong> $\sigma_y = \mathbf{0.463 \text{ MPa}}$ ($m = 0.389$).
    </div>""")

# P22: Active Slip System Determination
add(22, "Schmid Factor Evaluation in FCC Single Crystals: Identifying the Primary Slip System",
    "Single-Crystal Plasticity & Schmid's Law", "schmids_law", "Advanced",
    r"""<p>FCC metals possess 12 equivalent slip systems consisting of $\{111\}$ octahedral planes and $\langle 110\rangle$ close-packed directions.</p>
    <ol type="a">
      <li>State the vector formula for computing the cosine of the angle $\theta$ between tensile direction $[u_1 v_1 w_1]$ and plane normal $[h k l]$ or slip direction $[u_2 v_2 w_2]$ in a cubic crystal:
      $$\cos\theta = \frac{u_1 h + v_1 k + w_1 l}{\sqrt{u_1^2 + v_1^2 + w_1^2}\sqrt{h^2 + k^2 + l^2}}$$</li>
      <li>A single crystal of pure copper is pulled in tension along the $[123]$ direction. For the slip plane $(111)$, evaluate the Schmid factor for the three potential slip directions:
        <ul>
          <li>Direction $\mathbf{s}_1 = [1\bar{1}0]$</li>
          <li>Direction $\mathbf{s}_2 = [01\bar{1}]$</li>
          <li>Direction $\mathbf{s}_3 = [10\bar{1}]$</li>
        </ul>
      </li>
      <li>Which of these three slip directions is the <strong>active primary slip system</strong>, and what is its Schmid factor?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Vector Dot Product Angle Formula</div>
      <p>In cubic lattices, basis vectors are orthogonal and identical in magnitude ($a=b=c$). The angle $\theta$ between direction $\mathbf{d}_1 = [u_1, v_1, w_1]$ and $\mathbf{d}_2 = [u_2, v_2, w_2]$ is:</p>
      $$\cos\theta = \frac{\mathbf{d}_1 \cdot \mathbf{d}_2}{|\mathbf{d}_1| |\mathbf{d}_2|} = \frac{u_1 u_2 + v_1 v_2 + w_1 w_2}{\sqrt{u_1^2 + v_1^2 + w_1^2}\sqrt{u_2^2 + v_2^2 + w_2^2}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculations for Tension along $\mathbf{t} = [123]$ and Plane $\mathbf{n} = (111)$</div>
      <p>Tensile axis magnitude: $|\mathbf{t}| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}$.</p>
      <p>Slip plane normal magnitude: $|\mathbf{n}| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$.</p>
      <p>Angle $\phi$ between tensile axis $[123]$ and plane normal $(111)$:</p>
      $$\cos\phi = \frac{1(1) + 2(1) + 3(1)}{\sqrt{14}\sqrt{3}} = \frac{1 + 2 + 3}{\sqrt{42}} = \frac{6}{\sqrt{42}} \approx \mathbf{0.92582}$$
      <p>Now evaluate $\cos\lambda$ for each candidate slip direction ($|\mathbf{s}| = \sqrt{1^2 + 1^2 + 0} = \sqrt{2}$):</p>
      <ul>
        <li><strong>For $\mathbf{s}_1 = [1\bar{1}0]$:</strong>
        $$\cos\lambda_1 = \frac{1(1) + 2(-1) + 3(0)}{\sqrt{14}\sqrt{2}} = \frac{1 - 2 + 0}{\sqrt{28}} = \frac{-1}{\sqrt{28}} = -0.18898$$
        $$m_1 = |\cos\phi \cos\lambda_1| = 0.92582 \times 0.18898 = \mathbf{0.1750}$$</li>
        <li><strong>For $\mathbf{s}_2 = [01\bar{1}]$:</strong>
        $$\cos\lambda_2 = \frac{1(0) + 2(1) + 3(-1)}{\sqrt{14}\sqrt{2}} = \frac{0 + 2 - 3}{\sqrt{28}} = \frac{-1}{\sqrt{28}} = -0.18898$$
        $$m_2 = |\cos\phi \cos\lambda_2| = 0.92582 \times 0.18898 = \mathbf{0.1750}$$</li>
        <li><strong>For $\mathbf{s}_3 = [10\bar{1}]$:</strong>
        $$\cos\lambda_3 = \frac{1(1) + 2(0) + 3(-1)}{\sqrt{14}\sqrt{2}} = \frac{1 + 0 - 3}{\sqrt{28}} = \frac{-2}{\sqrt{28}} = -0.37796$$
        $$m_3 = |\cos\phi \cos\lambda_3| = 0.92582 \times 0.37796 = \mathbf{0.3500}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Primary Active Slip System</div>
      <p>Dislocations will always activate on that specific slip system that experiences the highest resolved shear stress (largest Schmid factor $m$). Comparing the three values:</p>
      $$m_3 = 0.3500 > m_1 = 0.1750 = m_2 = 0.1750$$
      <p>Therefore, the <strong>active primary slip system is $(111)[10\bar{1}]$ with Schmid factor $m = \mathbf{0.350}$</strong>. Plastic slip initiates on this system at a tensile stress of $\sigma_y = \tau_{\text{CRSS}} / 0.350 = 2.857 \tau_{\text{CRSS}}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Plane Angle:</strong> $\cos\phi = \frac{6}{\sqrt{42}} \approx 0.926$.<br>
      <strong>Schmid Factors on $(111)$:</strong> $[1\bar{1}0] \implies m = 0.175$ &bull; $[01\bar{1}] \implies m = 0.175$ &bull; $[10\bar{1}] \implies m = \mathbf{0.350}$.<br>
      <strong>Active Slip System:</strong> $\mathbf{(111)[10\bar{1}]}$ ($m = \mathbf{0.350}$).
    </div>""")

# P23: Orientation Dependence of Yield Strength
add(23, "Crystallographic Anisotropy: Yield Strength Variation Across the Standard Stereographic Triangle",
    "Single-Crystal Plasticity & Schmid's Law", "schmids_law", "Advanced",
    r"""<p>Due to Schmid factor variations across crystallographic directions, the macroscopic yield strength of a single crystal exhibits severe spatial anisotropy.</p>
    <ol type="a">
      <li>Consider an FCC metal single crystal with $\tau_{\text{CRSS}} = 1.20 \text{ MPa}$. Calculate the macroscopic tensile yield strength $\sigma_y$ when the tensile axis is aligned with:
        <ul>
          <li>The $[100]$ cube axis.</li>
          <li>The $[111]$ octahedral axis.</li>
          <li>The $[110]$ axis.</li>
        </ul>
      </li>
      <li>How many slip systems operate simultaneously (multiple slip) when pulled along the $[100]$ axis versus the $[111]$ axis?</li>
      <li>Why do single-crystal gas turbine blades (e.g., CMSX-4) have their growth axis aligned strictly along $[001]$?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Yield Strength Calculations for FCC Symmetry Axes</div>
      <ul>
        <li><strong>Tensile Axis along $[100]$:</strong>
          There are 8 symmetrically equivalent $\{111\}\langle 110\rangle$ slip systems with non-zero shear stress.
          Angle with plane $(111)$: $\cos\phi = \frac{1(1)+0+0}{\sqrt{1}\sqrt{3}} = \frac{1}{\sqrt{3}}$.
          Angle with direction $[011]$: $\cos\lambda = \frac{1(0)+0(1)+0(1)}{\sqrt{1}\sqrt{2}} = 0$.
          Angle with direction $[110]$: $\cos\lambda = \frac{1(1)+0(1)+0(0)}{\sqrt{1}\sqrt{2}} = \frac{1}{\sqrt{2}}$.
          $$m_{[100]} = \cos\phi \cos\lambda = \frac{1}{\sqrt{3}} \cdot \frac{1}{\sqrt{2}} = \frac{1}{\sqrt{6}} \approx \mathbf{0.4082}$$
          $$\sigma_{y, [100]} = \frac{\tau_{\text{CRSS}}}{m} = \frac{1.20 \text{ MPa}}{0.4082} = \mathbf{2.939 \text{ MPa}}$$
        </li>
        <li><strong>Tensile Axis along $[111]$:</strong>
          There are 6 symmetrically equivalent slip systems on the other three $\{111\}$ planes. For plane $(1\bar{1}1)$ and direction $[110]$:
          $$\cos\phi = \frac{1(1)+1(-1)+1(1)}{\sqrt{3}\sqrt{3}} = \frac{1}{3}$$
          $$\cos\lambda = \frac{1(1)+1(1)+1(0)}{\sqrt{3}\sqrt{2}} = \frac{2}{\sqrt{6}}$$
          $$m_{[111]} = \frac{1}{3} \cdot \frac{2}{\sqrt{6}} = \frac{2}{3\sqrt{6}} \approx \mathbf{0.2722}$$
          $$\sigma_{y, [111]} = \frac{\tau_{\text{CRSS}}}{m} = \frac{1.20 \text{ MPa}}{0.2722} = \mathbf{4.409 \text{ MPa}}$$
        </li>
        <li><strong>Tensile Axis along $[110]$:</strong>
          Four active slip systems have Schmid factor $m_{[110]} = \frac{1}{\sqrt{6}} \approx \mathbf{0.4082}$.
          $$\sigma_{y, [110]} = \frac{1.20 \text{ MPa}}{0.4082} = \mathbf{2.939 \text{ MPa}}$$
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Simultaneous Symmetrical Slip Systems</div>
      <ul>
        <li><strong>Along $[100]$:</strong> Exactly <strong>8 slip systems</strong> share the identical maximum Schmid factor $m = 0.4082$ and activate simultaneously! Symmetrical dislocation interpenetration produces rapid work hardening.</li>
        <li><strong>Along $[111]$:</strong> Exactly <strong>6 slip systems</strong> share $m = 0.2722$ and operate simultaneously.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Engineering Selection of $[001]$ for Turbine Blades</div>
      <p>Single-crystal nickel superalloy turbine blades are grown via directional solidification along the $[001]$ crystallographic axis because:</p>
      <ol>
        <li><strong>Lowest Young's Modulus:</strong> In FCC nickel, Young's modulus is highly anisotropic: $E_{[001]} \approx 130 \text{ GPa}$, whereas $E_{[111]} \approx 300 \text{ GPa}$. Under severe rapid thermal transients during jet engine takeoff and landing, thermal strain $\varepsilon_{\text{th}} = \alpha \Delta T$ generates thermal stress $\sigma_{\text{th}} = E \alpha \Delta T$. The low modulus along $[001]$ reduces thermal stresses by more than $50\%$, dramatically extending thermal fatigue life.</li>
        <li><strong>High Creep Resistance:</strong> Symmetrical activation of 8 slip systems promotes dislocation lock formation that suppresses high-temperature creep elongation.</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>Yield Strengths ($\tau_{\text{CRSS}} = 1.20\text{ MPa}$):</strong><br>
      $[100] \implies m = \mathbf{0.408}, \sigma_y = \mathbf{2.94 \text{ MPa}}$ (8 slip systems).<br>
      $[111] \implies m = \mathbf{0.272}, \sigma_y = \mathbf{4.41 \text{ MPa}}$ (6 slip systems).<br>
      $[001]$ orientation minimizes $E$ to maximize thermal fatigue resistance in turbine blades.
    </div>""")

# P24: Hardness Testing: Brinell and Rockwell
add(24, "Macrohardness Testing: Indentation Mechanics of Brinell (HB) and Rockwell (HRC/HRB)",
    "Hardness Testing & Empirical Relations", "hardness_testing", "Fundamental",
    r"""<p>Hardness testing is the most widely utilized non-destructive mechanical inspection technique in industrial manufacturing.</p>
    <ol type="a">
      <li>Define <strong>Hardness</strong> and state three reasons why hardness testing is performed far more frequently than tensile testing.</li>
      <li>Describe the <strong>Brinell Hardness Test (HB)</strong>:
        <ul>
          <li>Indenter geometry and standard test load for steels ($10 \text{ mm}$ ball, $3000 \text{ kgf}$).</li>
          <li>Mathematical formula for Brinell Hardness Number (HBW) in terms of applied load $P$, ball diameter $D$, and indentation impression diameter $d$:
          $$\text{HBW} = \frac{2P}{\pi D \left(D - \sqrt{D^2 - d^2}\right)}$$</li>
        </ul>
      </li>
      <li>Describe the <strong>Rockwell Hardness Test</strong>:
        <ul>
          <li>Difference between Rockwell B (HRB) and Rockwell C (HRC) (indenters and major loads).</li>
          <li>Why Rockwell testing measures <strong>residual depth of penetration ($e$)</strong> rather than surface diameter, and why a preliminary minor load is applied first.</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition and Industrial Advantages of Hardness Testing</div>
      <p>Hardness is a measure of a material's resistance to localized permanent plastic deformation (such as surface indentation, scratching, or abrasion).</p>
      <p><strong>Three Key Advantages over Tensile Testing:</strong></p>
      <ol>
        <li><strong>Simple and Inexpensive:</strong> Requires no specialized machined test coupons; can be performed directly on finished components.</li>
        <li><strong>Non-Destructive:</strong> Leaves only a microscopic surface impression that rarely impairs part function.</li>
        <li><strong>Direct Correlation:</strong> Well-calibrated empirical relationships allow tensile strength and wear resistance to be estimated directly from hardness numbers.</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): The Brinell Hardness Test (HBW)</div>
      <ul>
        <li><strong>Standard Conditions for Steels:</strong> A hardened tungsten carbide spherical ball of diameter $D = 10.0 \text{ mm}$ is pressed into the flat surface under a standard static load of $P = 3000 \text{ kgf}$ ($29,420 \text{ N}$) held for $10\text{--}15 \text{ seconds}$.</li>
        <li><strong>Formula:</strong> HBW is the applied load divided by the curved surface area of the spherical indentation cap:
        $$\text{HBW} = \frac{P}{A_{\text{cap}}} = \frac{2P}{\pi D \left(D - \sqrt{D^2 - d^2}\right)}$$
        where $P$ is load in $\text{kgf}$, $D$ is ball diameter in $\text{mm}$, and $d$ is the mean diameter of the surface impression measured in two perpendicular directions using a calibrated microscope.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): The Rockwell Hardness Test (HR)</div>
      <ul>
        <li><strong>Indenters and Major Loads:</strong>
          <ul>
            <li><strong>Rockwell C (HRC) (Hard metals, e.g., hardened steels, titanium):</strong> Uses a $120^\circ$ spheroconical diamond indenter (Brale) with a minor load of $10 \text{ kgf}$ and major load of $150 \text{ kgf}$.</li>
            <li><strong>Rockwell B (HRB) (Soft metals, e.g., brass, aluminum, mild steel):</strong> Uses a $1/16\text{ in}$ ($1.588 \text{ mm}$) hardened steel ball with minor load of $10 \text{ kgf}$ and major load of $100 \text{ kgf}$.</li>
          </ul>
        </li>
        <li><strong>Residual Depth Principle:</strong> Unlike Brinell (which requires optical measurement of diameter), Rockwell measures the <em>incremental depth of penetration $e$</em> electronically and outputs a direct digital dial reading. A preliminary <strong>minor load ($10 \text{ kgf}$)</strong> is applied first to penetrate through surface oxides, dirt, and minor roughness, establishing a zero reference baseline before the major load is applied.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Brinell:</strong> $10\text{ mm}$ ball, $3000\text{ kgf}$, measures optical impression diameter $d$: $\text{HB} = \frac{2P}{\pi D(D - \sqrt{D^2-d^2})}$.<br>
      <strong>Rockwell:</strong> Measures residual depth $e$ with preliminary minor load (eliminates optical error).<br>
      <strong>HRC:</strong> Diamond cone, $150\text{ kgf}$ &bull; <strong>HRB:</strong> $1/16\text{ in}$ ball, $100\text{ kgf}$.
    </div>""")

# P25: Vickers/Knoop and Tensile Strength Correlation
add(25, "Microhardness Testing and Empirical Hardness-Tensile Strength Correlations",
    "Hardness Testing & Empirical Relations", "hardness_testing", "Intermediate",
    r"""<p>Microhardness testing allows localized hardness measurement of individual microstructural phases, thin films, and carburized case depth gradients.</p>
    <ol type="a">
      <li>Describe the <strong>Vickers Microhardness Test (HV)</strong>:
        <ul>
          <li>Indenter geometry (square-based diamond pyramid with face angle $136^\circ$).</li>
          <li>Mathematical formula:
          $$\text{HV} = \frac{1.8544 P}{d^2}$$
          defining load $P$ ($\text{kgf}$) and average diagonal length $d$ ($\text{mm}$).</li>
        </ul>
      </li>
      <li>Describe the <strong>Knoop Hardness Test (HK)</strong>. Why is its elongated rhombic indenter ($7.11:1$ ratio) preferred for testing ultra-thin brittle ceramic coatings and brittle minerals without cracking?</li>
      <li>State the famous empirical correlation between Brinell Hardness (HB) and Ultimate Tensile Strength ($\sigma_{\text{UTS}}$) for plain carbon and low-alloy structural steels:
      $$\sigma_{\text{UTS}} \text{ (MPa)} \approx 3.45 \times \text{HB}$$
      $$\sigma_{\text{UTS}} \text{ (psi)} \approx 500 \times \text{HB}$$</li>
      <li>A Brinell test on an automotive crankshaft steel using a $10 \text{ mm}$ ball under $3000 \text{ kgf}$ load produces an impression diameter of $d = 3.90 \text{ mm}$.
        <ul>
          <li>Calculate the Brinell Hardness Number (HBW).</li>
          <li>Estimate the Ultimate Tensile Strength in megapascals ($\text{MPa}$).</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): The Vickers Hardness Test (HV)</div>
      <p>The Vickers test uses a square-based diamond pyramid indenter with an apex angle between opposite faces of $\alpha = 136^\circ$.</p>
      <p>The surface area of the four triangular pyramid faces is $A = \frac{d^2}{2\sin(136^\circ/2)} = \frac{d^2}{2\sin(68^\circ)} = \frac{d^2}{1.85437}$.</p>
      $$\text{HV} = \frac{P}{A} = \frac{2P \sin(68^\circ)}{d^2} = \mathbf{\frac{1.8544 P}{d^2}}$$
      <p>where $P$ is applied load in $\text{kgf}$ (typically $10\text{--}1000 \text{ gf}$ for microhardness, up to $50 \text{ kgf}$ for macrohardness) and $d$ is the average length of the two indentation diagonals measured under a microscope in millimeters.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): The Knoop Microhardness Test (HK)</div>
      <p>The Knoop test uses an elongated pyramidal diamond indenter that produces a narrow rhombic impression with a length-to-width ratio of approximately $7.11 : 1$. Because the indentation depth is only about one-third of a Vickers impression for the same load, elastic recovery occurs primarily along the short diagonal while the long diagonal remains unaffected. This ultra-shallow penetration minimizes tensile hoop stresses around the impression, allowing microhardness measurements on brittle ceramics, glass, enamel, and sub-micron coatings without inducing fracture or chipping.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Empirical Hardness-Strength Correlation for Steels</div>
      <p>Because plastic indentation is constrained by surrounding elastic material, slip line field theory (Tabor's rule) proves that indentation pressure is roughly three times the tensile yield stress ($H \approx 3 \sigma_y$). For work-hardening steels, empirical calibration yields:</p>
      $$\sigma_{\text{UTS}} \text{ [MPa]} \approx \mathbf{3.45 \times \text{HB}}$$
      $$\sigma_{\text{UTS}} \text{ [psi]} \approx \mathbf{500 \times \text{HB}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Calculations for Crankshaft Steel ($D = 10.0 \text{ mm}, P = 3000 \text{ kgf}, d = 3.90 \text{ mm}$)</div>
      $$\sqrt{D^2 - d^2} = \sqrt{10.0^2 - 3.90^2} = \sqrt{100.0 - 15.21} = \sqrt{84.79} = 9.20815 \text{ mm}$$
      $$D - \sqrt{D^2 - d^2} = 10.0 - 9.20815 = 0.79185 \text{ mm}$$
      $$\text{HBW} = \frac{2 \times 3000}{\pi \times 10.0 \times 0.79185} = \frac{6000}{24.8767} = \mathbf{241.2 \text{ HBW} \approx 241 \text{ HB}}$$
      <p>Estimate Ultimate Tensile Strength:</p>
      $$\sigma_{\text{UTS}} \approx 3.45 \times 241.2 = \mathbf{832.1 \text{ MPa}}$$
    </div>
    <div class="final-answer-box">
      <strong>Vickers:</strong> $\text{HV} = \frac{1.8544 P}{d^2}$ &bull; <strong>Knoop:</strong> Elongated rhombic indenter ($7.11:1$) for crack-free testing of brittle ceramics.<br>
      <strong>Steel Correlation:</strong> $\sigma_{\text{UTS}} \approx 3.45 \times \text{HB}$.<br>
      <strong>Crankshaft:</strong> Hardness = $\mathbf{241 \text{ HBW}} \implies \sigma_{\text{UTS}} \approx \mathbf{832 \text{ MPa}}$.
    </div>""")

# Save checkpoint for part 1 (1 to 25)
print("Ch 6 Part 1: All P1-P25 written successfully!")
