# generator/make_ch8_part1.py
import sys
import os
import re

P = []

def add(p_dict):
    if "num" in p_dict and "number" not in p_dict:
        p_dict["number"] = p_dict["num"]
    if "category_slug" not in p_dict:
        p_dict["category_slug"] = re.sub(r'[^a-z0-9]+', '-', p_dict.get("category", "general").lower()).strip('-')
    P.append(p_dict)

# ==========================================
# Problem 1
# ==========================================
add({
    "num": 1,
    "title": "Ductile vs. Brittle Fracture: Macroscopic and Microscopic Characteristics",
    "difficulty": "Easy",
    "category": "Fracture Fundamentals",
    "tags": ["Ductile Fracture", "Brittle Fracture", "Fractography", "Cup and Cone"],
    "statement": r"""A mechanical components inspector must examine two failed alloy steel drive shafts that fractured in service.
One failed by ductile overload, while the other failed by catastrophic brittle cleavage.
<br><br>
1. Complete a comparative analysis between ductile and brittle fracture across the following 5 criteria:
   (a) Macroscopic plastic deformation and cross-sectional necking.<br>
   (b) Crack propagation velocity and energy absorption.<br>
   (c) Macroscopic fracture surface morphology (including orientation relative to tensile axis).<br>
   (d) Warning signs prior to final fracture.<br>
   (e) Microscopic fractographic appearance under a Scanning Electron Microscope (SEM).<br>
2. Explain why engineers strongly prefer ductile fracture over brittle fracture in structural design.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Comparative Analysis Table</strong><br>
<table class="data-table">
<thead>
<tr><th>Feature</th><th>Ductile Fracture</th><th>Brittle Fracture</th></tr>
</thead>
<tbody>
<tr><td><strong>Macroscopic Plastic Deformation</strong></td><td>Extensive plastic deformation; visible cross-sectional reduction (necking) and elongation</td><td>Negligible or zero measurable plastic deformation; dimensions unchanged</td></tr>
<tr><td><strong>Crack Propagation & Energy</strong></td><td>Slow, stable crack growth (crack advances only if applied stress increases); high energy absorption</td><td>Extremely rapid, unstable catastrophic crack propagation (near the speed of sound, $\sim 1000\text{ m/s}$); very low energy absorption</td></tr>
<tr><td><strong>Macroscopic Fracture Surface</strong></td><td>Dull, fibrous gray appearance; classic <strong>cup-and-cone morphology</strong> with flat tensile fibrous core and $45^\circ$ shear lips</td><td>Bright, flat, reflective crystalline/granular facets; perpendicular ($90^\circ$) to maximum tensile stress</td></tr>
<tr><td><strong>Warning Prior to Failure</strong></td><td>Clear advance warning (visible sagging, bulging, paint flaking, deformation)</td><td>Sudden, catastrophic failure without warning</td></tr>
<tr><td><strong>Microscopic SEM Appearance</strong></td><td>Dense population of microscopic spherical or parabolic <strong>dimples</strong> (microvoid coalescence)</td><td>Flat transgranular <strong>cleavage facets with river patterns</strong>, or intergranular "rock candy" boundaries</td></tr>
</tbody>
</table>
</div>
<div class="solution-step">
<strong>Step 2: Why ductile fracture is strongly preferred</strong><br>
1. <strong>Damage Tolerance and Advance Warning:</strong> Ductile materials deform noticeably before fracturing, allowing maintenance crews, sensors, or visual inspections to detect excessive strain, take the machine offline, and repair the part before catastrophic collapse.
2. <strong>Enormous Energy Absorption:</strong> The large plastic deformation zone dissipates vast amounts of mechanical energy ($\int \sigma d\varepsilon$), preventing sudden fragmentation, blast wave releases, and secondary collapse under unexpected dynamic impact or overloads.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Ductile: Large plastic necking, slow stable crack growth, cup-and-cone with $45^\circ$ shear lips, SEM microvoid dimples, high energy absorption.<br>
Brittle: Zero plastic necking, sound-speed unstable crack, flat reflective surface at $90^\circ$, SEM cleavage river patterns, zero advance warning.<br>
Ductile is preferred for safety because it provides visual warning and absorbs massive mechanical energy.
</div>"""
})

# ==========================================
# Problem 2
# ==========================================
add({
    "num": 2,
    "title": "Microscopic Mechanisms: Microvoid Coalescence vs. Cleavage and Intergranular Fracture",
    "difficulty": "Medium",
    "category": "Fracture Fundamentals",
    "tags": ["Microvoid Coalescence", "Cleavage", "River Patterns", "Intergranular Fracture"],
    "statement": r"""Scanning Electron Microscopy (SEM) fractography is the definitive forensic tool for diagnosing fracture mechanisms in failed mechanical components.
<br><br>
1. Describe the 3 sequential stages of <strong>Microvoid Coalescence (MVC)</strong> in ductile fracture:
   (a) Void nucleation.<br>
   (b) Void growth.<br>
   (c) Void coalescence (sheet thinning).<br>
2. Explain how equiaxed dimples form under pure uniaxial tension versus elongated (parabolic) dimples under in-plane shear or tear loading.<br>
3. What is <strong>transgranular cleavage</strong>? Describe the physical origin of <strong>river patterns</strong> on cleavage facets and explain which direction the "rivers" flow.<br>
4. Describe <strong>intergranular fracture</strong> ("rock candy" appearance) and identify two common metallurgical causes.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The three stages of Microvoid Coalescence (MVC)</strong><br>
(a) <strong>Void Nucleation:</strong> When plastic strain accumulates, the severe elastic incompatibility between the ductile metallic matrix and hard, non-deformable second-phase inclusions (e.g., $\text{MnS}$ inclusions, $\text{Fe}_3\text{C}$ carbides, oxide particles) creates high interface tensile tractions. Microvoids nucleate either by decohesion of the inclusion/matrix interface or by cracking of the brittle particle itself.<br>
(b) <strong>Void Growth:</strong> Driven by plastic slip and triaxial tensile hydrostatic stress ($\sigma_m$), the nucleated microvoids expand in volume and stretch in the direction of the principal tensile stress.<br>
(c) <strong>Void Coalescence:</strong> As voids grow, the metallic ligaments between adjacent voids progressively thin down until localized plastic shear instability (internal necking) shears the intervening ligaments, joining the voids into a continuous macroscopic crack front.
</div>
<div class="solution-step">
<strong>Step 2: Equiaxed vs. Elongated (parabolic) dimples</strong><br>
- <em>Equiaxed dimples:</em> Under uniform uniaxial tension, voids grow symmetrically in all radial directions, resulting in circular, equiaxed cups (dimples) when viewed face-on.<br>
- <em>Parabolic/elongated dimples:</em> Under shear or tearing (Mode II/III), plastic deformation tilts and stretches the voids along the shear direction. The dimples on the two mating fracture surfaces point in opposite directions under shear, or in the same direction toward the crack origin under tear loading.
</div>
<div class="solution-step">
<strong>Step 3: Transgranular cleavage and river patterns</strong><br>
Cleavage is rapid separation along low-index, weakly bonded crystallographic planes (principally $\{100\}$ in BCC iron).
As a cleavage crack advances across a grain, it encounters screw dislocation steps or small tilt misorientations. The crack is forced to split onto parallel cleavage planes at slightly different elevations, creating vertical cleavage steps. To minimize surface energy, adjacent steps converge and merge as the crack advances, forming a branching tributary network known as a <strong>river pattern</strong>.
<em>Crucial rule:</em> River branches merge into larger "rivers" in the direction of crack propagation; therefore, following river patterns <strong>upstream</strong> points directly back to the microscopic fracture initiation site!
</div>
<div class="solution-step">
<strong>Step 4: Intergranular fracture</strong><br>
Intergranular fracture occurs when the crack propagates along prior austenitic or ferritic grain boundaries, revealing faceted, 3D polyhedral grains resembling chunks of rock candy.
<em>Metallurgical causes:</em>
1. <strong>Temper Embrittlement:</strong> Segregation of tramp impurity elements (phosphorus, sulfur, antimony, tin, arsenic) to grain boundaries during slow cooling through $375^\circ\text{C}\text{--}575^\circ\text{C}$, severely lowering grain boundary cohesion.
2. <strong>Sensitization in Stainless Steels:</strong> Precipitation of continuous chromium carbides ($\text{Cr}_{23}\text{C}_6$) along grain boundaries, depleting chromium in adjacent channels and causing intergranular stress corrosion.
3. <strong>Hydrogen Embrittlement:</strong> Trapping of dissolved atomic hydrogen at grain boundaries, lowering local boundary cohesion.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
MVC: Nucleation at particles $\to$ growth under triaxiality $\to$ coalescence by ligament shearing.<br>
Equiaxed dimples indicate pure tension; parabolic dimples indicate shear/tearing.<br>
Cleavage river patterns branch in the direction of crack travel; following them upstream locates the crack origin.<br>
Intergranular fracture ("rock candy") results from impurity segregation (P, S, Sb) or grain boundary carbide precipitation.
</div>"""
})

# ==========================================
# Problem 3
# ==========================================
add({
    "num": 3,
    "title": "Inglis Stress Concentration Factor at an Elliptical Flaw",
    "difficulty": "Medium",
    "category": "Stress Concentrations",
    "tags": ["Inglis Formula", "Stress Concentration Factor", "Elliptical Notch", "Root Radius"],
    "statement": r"""In 1913, C. E. Inglis solved the elastic stress distribution around an elliptical hole with major axis $2a$ and minor axis $2b$ oriented perpendicular to a remote uniform tensile stress $\sigma_0$ in an infinite plate.
The maximum localized tensile stress $\sigma_{\text{max}}$ occurring at the sharp tips of the ellipse is:
$$\sigma_{\text{max}} = \sigma_0 \left(1 + 2\frac{a}{b}\right) = \sigma_0 \left(1 + 2\sqrt{\frac{a}{\rho_t}}\right)$$
where $\rho_t = b^2 / a$ is the tip radius of curvature.
For a sharp flaw ($\rho_t \ll a$), the stress concentration factor $K_t$ simplifies to:
$$K_t = \frac{\sigma_{\text{max}}}{\sigma_0} \approx 2\sqrt{\frac{a}{\rho_t}}$$
<br>
1. A wide steel plate is subjected to a remote tensile stress $\sigma_0 = 180\text{ MPa}$. An elliptical flaw of total length $2a = 10.0\text{ mm}$ (crack half-length $a = 5.0\text{ mm}$) has a root tip radius $\rho_t = 0.050\text{ mm}$ ($50\text{ }\mu\text{m}$). Calculate $K_t$ and the peak localized tip stress $\sigma_{\text{max}}$.<br>
2. If the flaw is sharpened by fatigue until $\rho_t = 0.50\text{ }\mu\text{m}$ ($5.0 \times 10^{-7}\text{ m}$), calculate the new $K_t$ and $\sigma_{\text{max}}$.<br>
3. What is $K_t$ for a perfectly circular hole ($a = b$)?<br>
4. Why does an atomistically sharp crack ($\rho_t \to 0$) produce an infinite stress singularity in linear elasticity, and how does real material plasticity resolve this paradox?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate $K_t$ and peak stress for $\rho_t = 0.050\text{ mm}$</strong><br>
Given: $a = 5.0\text{ mm}$, $\rho_t = 0.050\text{ mm}$:
$$\frac{a}{\rho_t} = \frac{5.0}{0.050} = 100$$
$$K_t = 1 + 2\sqrt{\frac{a}{\rho_t}} = 1 + 2\sqrt{100} = 1 + 2(10) = 21.0$$
Peak localized stress:
$$\sigma_{\text{max}} = K_t \sigma_0 = 21.0 \times 180\text{ MPa} = 3,780\text{ MPa} = 3.78\text{ GPa}$$
The nominal stress of $180\text{ MPa}$ is amplified to nearly $3.8\text{ GPa}$ at the notch tip!
</div>
<div class="solution-step">
<strong>Step 2: Calculate for sharp fatigue flaw ($\rho_t = 0.50\text{ }\mu\text{m} = 0.00050\text{ mm}$)</strong><br>
$$\frac{a}{\rho_t} = \frac{5.0\text{ mm}}{0.00050\text{ mm}} = 10,000$$
$$K_t = 1 + 2\sqrt{10,000} = 1 + 2(100) = 201.0$$
$$\sigma_{\text{max}} = 201.0 \times 180\text{ MPa} = 36,180\text{ MPa} \approx 36.2\text{ GPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Circular hole ($a = b$)</strong><br>
When $a = b$, the ellipse becomes a circle with $\rho_t = a^2/a = a$:
$$K_t = 1 + 2\left(\frac{a}{a}\right) = 1 + 2(1) = 3.0$$
A circular hole produces a classic stress concentration factor of exactly 3.0 regardless of hole size.
</div>
<div class="solution-step">
<strong>Step 4: The sharp crack singularity and plastic relief</strong><br>
As the tip radius approaches atomic dimensions ($\rho_t \to 0$), the mathematical formula predicts $\sigma_{\text{max}} \propto 1/\sqrt{\rho_t} \to \infty$ (a stress singularity).
In real ductile metals, stresses can never reach infinity because once localized stress exceeds the yield strength $\sigma_y$, <strong>plastic deformation blunts the crack tip</strong>. Dislocation nucleation and slip round off the sharp tip (increasing effective $\rho_t$) and redistribute the peak stresses over a finite plastic zone $r_p$, shielding the material from catastrophic fracture. In brittle materials (glass, ceramics), plastic blunting cannot occur, leading to instantaneous fracture at tiny loads.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
At $\rho_t = 50\text{ }\mu\text{m}$: $K_t = 21.0 \implies \sigma_{\text{max}} = 3,780\text{ MPa}$<br>
At $\rho_t = 0.5\text{ }\mu\text{m}$: $K_t = 201.0 \implies \sigma_{\text{max}} = 36.2\text{ GPa}$<br>
Circular hole: $K_t = 3.0$<br>
Plastic yielding at the crack tip blunts the notch root in metals, mitigating the theoretical elastic singularity.
</div>"""
})

# ==========================================
# Problem 4
# ==========================================
add({
    "num": 4,
    "title": "Griffith Energy Balance Criterion for Brittle Fracture",
    "difficulty": "Hard",
    "category": "Fracture Mechanics",
    "tags": ["Griffith Criterion", "Surface Energy", "Critical Flaw Size", "Energy Balance"],
    "statement": r"""A. A. Griffith (1921) formulated the fundamental criterion for brittle fracture based on an energy balance.
In an infinite plate of unit thickness containing an internal crack of length $2a$ subjected to a uniform tensile stress $\sigma$, the total change in potential energy $\Delta U$ upon crack formation is:
$$\Delta U = U_{\text{surface}} - U_{\text{strain}} = 4 a \gamma_s - \frac{\pi \sigma^2 a^2}{E}$$
where $\gamma_s$ is the specific surface free energy of the material and $E$ is Young's modulus.
<br><br>
1. Using the equilibrium thermodynamic condition $\frac{d(\Delta U)}{da} = 0$, derive the classical Griffith formula for the critical fracture stress $\sigma_c$ for plane stress.<br>
2. Show that the second derivative $\frac{d^2(\Delta U)}{da^2} < 0$ at $a = a_c$, and explain why this proves crack propagation is spontaneously unstable (explosive) once the critical stress is reached.<br>
3. For a soda-lime silicate glass ($E = 68\text{ GPa}$, $\gamma_s = 0.35\text{ J/m}^2$), calculate the critical fracture stress $\sigma_c$ for an internal crack of length $2a = 4.0\text{ }\mu\text{m}$ (crack half-length $a = 2.0\text{ }\mu\text{m}$).<br>
4. Calculate the critical crack size $a_c$ if the glass is loaded to a tensile stress $\sigma = 50.0\text{ MPa}$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Derivation of the Griffith equation</strong><br>
The total potential energy is:
$$\Delta U = 4 a \gamma_s - \frac{\pi \sigma^2 a^2}{E}$$
(Note: $4 a \gamma_s$ represents the surface energy of two crack faces of length $2a$, so area $= 2 \times 2a \times 1 = 4a$).
Differentiating with respect to crack half-length $a$:
$$\frac{d(\Delta U)}{da} = 4 \gamma_s - \frac{2\pi \sigma^2 a}{E} = 0$$
Solving for $\sigma^2$:
$$\frac{2\pi \sigma^2 a}{E} = 4 \gamma_s \implies \sigma^2 = \frac{4 \gamma_s E}{2\pi a} = \frac{2 E \gamma_s}{\pi a}$$
Taking the square root yields Griffith's equation:
$$\sigma_c = \sqrt{\frac{2 E \gamma_s}{\pi a}}$$
</div>
<div class="solution-step">
<strong>Step 2: Second derivative and instability</strong><br>
$$\frac{d^2(\Delta U)}{da^2} = -\frac{2\pi \sigma^2}{E}$$
Because $E > 0$ and $\sigma > 0$, the second derivative is strictly <strong>negative</strong> ($\frac{d^2(\Delta U)}{da^2} < 0$).
This means the stationary point represents an energy <em>maximum</em> (an unstable equilibrium barrier).
If a crack reaches length $a \ge a_c$, any incremental advance releases more elastic strain energy than is required to create new surface area ($dU_{\text{strain}}/da > dU_{\text{surface}}/da$).
The net energy drops continuously ($\Delta U \to -\infty$), providing excess kinetic energy that accelerates the crack tip up to Rayleigh wave speeds ($\sim 1500\text{ m/s}$), causing sudden explosive fragmentation.
</div>
<div class="solution-step">
<strong>Step 3: Calculate $\sigma_c$ for glass with $a = 2.0\text{ }\mu\text{m}$</strong><br>
Given: $E = 68 \times 10^9\text{ Pa}$, $\gamma_s = 0.35\text{ J/m}^2$, $a = 2.0 \times 10^{-6}\text{ m}$:
$$2 E \gamma_s = 2 \times (68 \times 10^9) \times 0.35 = 4.76 \times 10^{10}\text{ N}^2/\text{m}^3$$
$$\pi a = \pi \times (2.0 \times 10^{-6}\text{ m}) \approx 6.28318 \times 10^{-6}\text{ m}$$
$$\sigma_c = \sqrt{\frac{4.76 \times 10^{10}}{6.28318 \times 10^{-6}}} = \sqrt{7.5758 \times 10^{15}} \approx 87,039,000\text{ Pa} \approx 87.04\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: Critical crack size $a_c$ for $\sigma = 50.0\text{ MPa}$</strong><br>
$$\sigma_c = \sqrt{\frac{2 E \gamma_s}{\pi a_c}} \implies a_c = \frac{2 E \gamma_s}{\pi \sigma^2}$$
$$a_c = \frac{4.76 \times 10^{10}}{\pi \times (50.0 \times 10^6)^2} = \frac{4.76 \times 10^{10}}{\pi \times 2.50 \times 10^{15}} = \frac{4.76 \times 10^{10}}{7.854 \times 10^{15}} \approx 6.06 \times 10^{-6}\text{ m} = 6.06\text{ }\mu\text{m}$$
An microscopic scratch of depth just $6\text{ }\mu\text{m}$ is sufficient to shatter the glass at $50\text{ MPa}$!
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Derived: $\sigma_c = \sqrt{\frac{2E\gamma_s}{\pi a}}$<br>
$d^2(\Delta U)/da^2 < 0$ proves crack growth is unstably accelerated once $a \ge a_c$.<br>
Critical fracture stress at $a = 2\text{ }\mu\text{m}$: $\sigma_c = 87.0\text{ MPa}$<br>
At $\sigma = 50\text{ MPa}$: critical crack size $a_c = 6.06\text{ }\mu\text{m}$.
</div>"""
})

# ==========================================
# Problem 5
# ==========================================
add({
    "num": 5,
    "title": "Orowan-Irwin Plastic Work Modification of Griffith Theory",
    "difficulty": "Medium",
    "category": "Fracture Mechanics",
    "tags": ["Orowan-Irwin", "Plastic Work of Fracture", "Metals vs Glass"],
    "statement": r"""When Griffith's formula $\sigma_c = \sqrt{\frac{2E\gamma_s}{\pi a}}$ was tested on ductile and semi-brittle metals (such as structural steel), experimental fracture stresses were found to be $100\times$ to $1000\times$ higher than predicted by Griffith using the true surface energy $\gamma_s \approx 1.0\text{ J/m}^2$.
E. Orowan and G. Irwin recognized that in metals, dislocation motion around the advancing crack tip dissipates plastic work energy $\gamma_p$ that dwarfs the thermodynamic surface energy:
$$\sigma_c = \sqrt{\frac{2E(\gamma_s + \gamma_p)}{\pi a}} \approx \sqrt{\frac{2E\gamma_p}{\pi a}} \quad (\text{since } \gamma_p \gg \gamma_s)$$
<br>
1. A structural low-carbon steel has $E = 210\text{ GPa}$ and surface energy $\gamma_s = 1.2\text{ J/m}^2$.
If Griffith's original formula (with $\gamma_s$ alone) were used, calculate the predicted fracture stress $\sigma_c$ for an internal crack of half-length $a = 2.0\text{ mm}$.<br>
2. Experimental fracture testing of this steel yields an actual fracture stress $\sigma_c = 360\text{ MPa}$ for $a = 2.0\text{ mm}$. Calculate the actual effective plastic work of fracture $\gamma_p$ (in $\text{kJ/m}^2$ or $\text{J/m}^2$).<br>
3. Calculate the ratio $\gamma_p / \gamma_s$ and comment on the physical significance of plastic work dissipation in preventing brittle fracture in metals.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Griffith prediction using $\gamma_s$ alone</strong><br>
Given: $E = 210 \times 10^9\text{ Pa}$, $\gamma_s = 1.2\text{ J/m}^2$, $a = 2.0 \times 10^{-3}\text{ m}$:
$$\sigma_{c, \text{Griffith}} = \sqrt{\frac{2 E \gamma_s}{\pi a}} = \sqrt{\frac{2 \times (210 \times 10^9) \times 1.2}{\pi \times (2.0 \times 10^{-3})}} = \sqrt{\frac{5.04 \times 10^{11}}{0.00628318}} = \sqrt{8.0214 \times 10^{13}} \approx 8.956 \times 10^6\text{ Pa} \approx 8.96\text{ MPa}$$
Griffith's equation predicts that the steel would fracture at a pathetic tensile stress of only $8.96\text{ MPa}$!
</div>
<div class="solution-step">
<strong>Step 2: Calculate actual plastic work of fracture $\gamma_p$</strong><br>
From $\sigma_c = \sqrt{\frac{2E(\gamma_s + \gamma_p)}{\pi a}}$:
$$\sigma_c^2 = \frac{2E(\gamma_s + \gamma_p)}{\pi a} \implies \gamma_s + \gamma_p = \frac{\pi a \sigma_c^2}{2E}$$
Given $\sigma_c = 360\text{ MPa} = 360 \times 10^6\text{ Pa}$:
$$\sigma_c^2 = (360 \times 10^6)^2 = 1.296 \times 10^{17}\text{ Pa}^2$$
$$\pi a \sigma_c^2 = \pi \times (2.0 \times 10^{-3}\text{ m}) \times (1.296 \times 10^{17}\text{ Pa}^2) \approx 8.143 \times 10^{14}\text{ N}^2/\text{m}$$
$$\gamma_s + \gamma_p = \frac{8.143 \times 10^{14}}{2 \times (210 \times 10^9)} = \frac{8.143 \times 10^{14}}{4.20 \times 10^{11}} \approx 1,938.8\text{ J/m}^2 \approx 1.94\text{ kJ/m}^2$$
Since $\gamma_s = 1.2\text{ J/m}^2$:
$$\gamma_p = 1,938.8 - 1.2 \approx 1,937.6\text{ J/m}^2 \approx 1.94\text{ kJ/m}^2$$
</div>
<div class="solution-step">
<strong>Step 3: Ratio $\gamma_p / \gamma_s$ and physical significance</strong><br>
$$\frac{\gamma_p}{\gamma_s} = \frac{1,937.6\text{ J/m}^2}{1.2\text{ J/m}^2} \approx 1,615$$
The energy absorbed by plastic work in the plastic zone ahead of the crack tip ($\gamma_p$) is more than <strong>$1600\times$ larger</strong> than the thermodynamic surface energy ($\gamma_s$) required to sever atomic bonds.
In metals, crack extension is physically impossible without dragging along a cloud of billions of gliding and multiplying dislocations. This plastic deformation acts as a massive energy sink that absorbs incoming strain energy, raising fracture resistance by thousands of times compared to glass or ceramics.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Pure Griffith prediction: $\sigma_c = 8.96\text{ MPa}$ (gross underestimation).<br>
Plastic work of fracture: $\gamma_p \approx 1,938\text{ J/m}^2$ ($1.94\text{ kJ/m}^2$).<br>
$\gamma_p / \gamma_s \approx 1,615\times$ (plastic dislocation dissipation dominates fracture resistance in metals).
</div>"""
})

# ==========================================
# Problem 6
# ==========================================
add({
    "num": 6,
    "title": "Strain Energy Release Rate $G$ and Critical Driving Force $G_c$",
    "difficulty": "Medium",
    "category": "Linear Elastic Fracture Mechanics",
    "tags": ["Energy Release Rate", "Crack Driving Force", "Gc", "Compliance Method"],
    "statement": r"""Irwin defined the <strong>Strain Energy Release Rate ($G$)</strong> as the elastic energy released per unit of newly created crack area $A$:
$$G = -\frac{dU_{\text{el}}}{dA} = \frac{P^2}{2B} \frac{dC}{da}$$
where $P$ is the applied force, $B$ is specimen thickness, $a$ is crack length, and $C = \delta / P$ is the load-line compliance.
Fracture instability occurs when the driving force $G$ reaches the material's critical fracture resistance $G_c$: $G \ge G_c$.
<br><br>
In a double-cantilever beam (DCB) fracture specimen of width $B = 25.0\text{ mm}$ and beam half-height $h = 15.0\text{ mm}$ made of an epoxy adhesive ($E = 3.5\text{ GPa}$):
The compliance of the DCB specimen is given by beam theory:
$$C = \frac{8 a^3}{E B h^3}$$
<br>
1. Derive the expression for the strain energy release rate $G$ as a function of load $P$, crack length $a$, $E, B$, and $h$.<br>
2. A critical fracture load $P_c = 420.0\text{ N}$ is measured when the crack length is $a = 60.0\text{ mm}$. Calculate the critical strain energy release rate $G_{Ic}$ of the epoxy.<br>
3. For plane strain, the Mode I stress intensity factor is related to $G_{Ic}$ by $K_{Ic} = \sqrt{\frac{E G_{Ic}}{1 - \nu^2}}$. Calculate $K_{Ic}$ for this epoxy ($\nu = 0.35$).""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Derivation of $G$ for DCB specimen</strong><br>
From compliance $C(a) = \frac{8 a^3}{E B h^3}$:
Differentiating with respect to crack length $a$:
$$\frac{dC}{da} = \frac{d}{da}\left(\frac{8 a^3}{E B h^3}\right) = \frac{24 a^2}{E B h^3}$$
Substitute into Irwin's compliance formula $G = \frac{P^2}{2B} \frac{dC}{da}$:
$$G = \frac{P^2}{2B} \left(\frac{24 a^2}{E B h^3}\right) = \frac{12 P^2 a^2}{E B^2 h^3}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate critical release rate $G_{Ic}$</strong><br>
Given: $P_c = 420.0\text{ N}$, $a = 0.060\text{ m}$, $B = 0.025\text{ m}$, $h = 0.015\text{ m}$, $E = 3.5 \times 10^9\text{ Pa}$:
$$P_c^2 = (420)^2 = 176,400\text{ N}^2$$
$$a^2 = (0.060)^2 = 0.0036\text{ m}^2$$
$$\text{Numerator} = 12 \times 176,400 \times 0.0036 = 7,620.48\text{ N}^2\cdot\text{m}^2$$
$$\text{Denominator} = E B^2 h^3 = (3.5 \times 10^9) \times (0.025)^2 \times (0.015)^3$$
$$B^2 = 0.000625\text{ m}^2, \quad h^3 = 3.375 \times 10^{-6}\text{ m}^3$$
$$\text{Denom} = (3.5 \times 10^9) \times (6.25 \times 10^{-4}) \times (3.375 \times 10^{-6}) = 7,382.81\text{ N}\cdot\text{m}$$
$$G_{Ic} = \frac{7,620.48}{7,382.81} \approx 1.0322\text{ N/m} = 1.032\text{ kJ/m}^2 = 1,032\text{ J/m}^2$$
</div>
<div class="solution-step">
<strong>Step 3: Calculate fracture toughness $K_{Ic}$</strong><br>
$$K_{Ic} = \sqrt{\frac{E G_{Ic}}{1 - \nu^2}}$$
$$1 - \nu^2 = 1 - (0.35)^2 = 1 - 0.1225 = 0.8775$$
$$\frac{E G_{Ic}}{1 - \nu^2} = \frac{(3.5 \times 10^9\text{ Pa}) \times (1,032.2\text{ J/m}^2)}{0.8775} = \frac{3.6127 \times 10^{12}}{0.8775} \approx 4.117 \times 10^{12}\text{ Pa}^2\cdot\text{m}$$
$$K_{Ic} = \sqrt{4.117 \times 10^{12}} \approx 2,029,000\text{ Pa}\sqrt{\text{m}} \approx 2.03\text{ MPa}\sqrt{\text{m}}$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Formula: $G = \frac{12 P^2 a^2}{E B^2 h^3}$<br>
Critical energy release rate: $G_{Ic} = 1,032\text{ J/m}^2$ ($1.03\text{ kJ/m}^2$)<br>
Plane strain fracture toughness: $K_{Ic} = 2.03\text{ MPa}\sqrt{\text{m}}$
</div>"""
})

# ==========================================
# Problem 7
# ==========================================
add({
    "num": 7,
    "title": "The Three Fracture Modes and Crack-Tip Stress Singularity",
    "difficulty": "Easy",
    "category": "Linear Elastic Fracture Mechanics",
    "tags": ["Fracture Modes", "Mode I", "Mode II", "Mode III", "Stress Singularity"],
    "statement": r"""Linear Elastic Fracture Mechanics (LEFM) categorizes relative crack face displacements into three fundamental kinematic modes.
<br><br>
1. Identify and describe the physical loading and displacement kinematics for:
   (a) <strong>Mode I</strong> (Opening Mode).<br>
   (b) <strong>Mode II</strong> (In-plane Shear / Sliding Mode).<br>
   (c) <strong>Mode III</strong> (Out-of-plane Shear / Tearing Mode).<br>
2. Why is Mode I by far the most critical and widely tested mode in engineering structural design?<br>
3. The asymptotic elastic stress tensor near a sharp Mode I crack tip is given by the Westergaard equations:
$$\sigma_{ij}(r, \theta) = \frac{K_I}{\sqrt{2\pi r}} f_{ij}(\theta)$$
What is the mathematical nature of the stress singularity as the distance from the crack tip $r \to 0$?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The Three Fracture Modes</strong><br>
(a) <strong>Mode I (Opening Mode):</strong> Tensile forces act perpendicular to the crack plane ($\sigma_{yy}$). The two opposing crack faces pull apart symmetrically in the $+y$ and $-y$ directions without sliding relative to each other.<br>
(b) <strong>Mode II (In-Plane Shear / Sliding Mode):</strong> Shear forces act parallel to the crack plane and perpendicular to the crack front line ($\tau_{xy}$). The two crack faces slide over one another in opposite directions within the crack plane.<br>
(c) <strong>Mode III (Out-of-Plane Shear / Tearing Mode):</strong> Shear forces act parallel to the crack plane and parallel to the crack front line ($\tau_{yz}$). The crack faces tear apart by sliding past each other in the antiplane $z$-direction (like tearing a sheet of paper with two hands moving in and out of the page).
</div>
<div class="solution-step">
<strong>Step 2: Why Mode I dominates engineering design</strong><br>
1. <em>Lowest Fracture Toughness:</em> For almost all engineering materials, the Mode I fracture toughness $K_{Ic}$ is significantly lower than the shear toughness values ($K_{IIc}$ and $K_{IIIc}$). Materials are much weaker in tensile bond separation than in shear.<br>
2. <em>Crack Path Deflection:</em> Under mixed-mode loading (combined Mode I and Mode II), a propagating crack naturally curls and deflects until it aligns itself perpendicular to the maximum principal tensile stress, converting any shear loading back into a pure Mode I local opening crack.
</div>
<div class="solution-step">
<strong>Step 3: Nature of the $1/\sqrt{r}$ singularity</strong><br>
As the distance from the tip $r \to 0$, the stresses scale as:
$$\sigma_{ij} \propto \frac{1}{\sqrt{r}} = r^{-1/2}$$
This is the famous <strong>inverse square-root singularity ($r^{-1/2}$)</strong> characteristic of all linear elastic sharp crack problems. The stress intensity factor $K_I$ uniquely defines the amplitude (intensity) of this singularity field, so knowing $K_I$ completely characterizes the local stress and strain state surrounding the crack tip regardless of global geometry.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Mode I: Tensile opening ($y$-displacement).<br>
Mode II: In-plane shear sliding ($x$-displacement).<br>
Mode III: Out-of-plane tearing ($z$-displacement).<br>
Mode I dominates because materials have the lowest toughness in tension and cracks naturally deflect into pure Mode I.<br>
Crack-tip stresses exhibit an inverse square-root singularity: $\sigma \propto K_I / \sqrt{2\pi r}$.
</div>"""
})

# ==========================================
# Problem 8
# ==========================================
add({
    "num": 8,
    "title": "Mode I Stress Intensity Factor and Critical Crack Size",
    "difficulty": "Medium",
    "category": "Linear Elastic Fracture Mechanics",
    "tags": ["Stress Intensity Factor", "Fracture Toughness", "Critical Crack Size", "Aircraft Skin"],
    "statement": r"""The Mode I stress intensity factor $K_I$ is expressed as:
$$K_I = Y \sigma \sqrt{\pi a}$$
where $\sigma$ is the nominal applied tensile stress, $a$ is the crack length (or half-length for an internal crack), and $Y$ is a dimensionless geometric calibration factor.
<br><br>
An aircraft wing skin panel fabricated from 2024-T3 aluminum alloy has a yield strength $\sigma_y = 345\text{ MPa}$ and plane strain fracture toughness $K_{Ic} = 34.0\text{ MPa}\sqrt{\text{m}}$.
The panel is subjected to a maximum in-flight tensile stress $\sigma = 230\text{ MPa}$ (two-thirds of $\sigma_y$).
<br><br>
1. Calculate the critical crack size $a_c$ (crack half-length) for an <strong>internal through-thickness crack</strong> located far from plate boundaries ($Y = 1.00$).<br>
2. Calculate the critical crack size $a_c'$ for an <strong>edge crack</strong> growing inward from the outer sheet edge ($Y = 1.12$).<br>
3. By what percentage does the edge crack configuration reduce the allowable critical crack size compared to an internal crack?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Critical crack size for internal through crack ($Y = 1.00$)</strong><br>
Fracture occurs when $K_I = K_{Ic}$:
$$K_{Ic} = Y \sigma \sqrt{\pi a_c} \implies \sqrt{\pi a_c} = \frac{K_{Ic}}{Y \sigma} \implies a_c = \frac{1}{\pi}\left(\frac{K_{Ic}}{Y \sigma}\right)^2$$
Given: $K_{Ic} = 34.0\text{ MPa}\sqrt{\text{m}}$, $\sigma = 230\text{ MPa}$, $Y = 1.00$:
$$\frac{K_{Ic}}{Y \sigma} = \frac{34.0}{1.00 \times 230} = \frac{34.0}{230} \approx 0.147826\text{ m}^{1/2}$$
$$a_c = \frac{1}{\pi} (0.147826)^2 = \frac{0.0218525}{\pi} \approx 0.006956\text{ m} \approx 6.96\text{ mm}$$
The critical crack half-length is $a_c \approx 6.96\text{ mm}$ (total crack length $2a_c \approx 13.9\text{ mm}$).
</div>
<div class="solution-step">
<strong>Step 2: Critical crack size for edge crack ($Y = 1.12$)</strong><br>
For an edge crack, $Y = 1.12$:
$$\frac{K_{Ic}}{Y \sigma} = \frac{34.0}{1.12 \times 230} = \frac{34.0}{257.6} \approx 0.131988\text{ m}^{1/2}$$
$$a_c' = \frac{1}{\pi} (0.131988)^2 = \frac{0.0174207}{\pi} \approx 0.005545\text{ m} \approx 5.55\text{ mm}$$
An edge crack of depth just $5.55\text{ mm}$ will trigger catastrophic unstable fracture!
</div>
<div class="solution-step">
<strong>Step 3: Percentage reduction</strong><br>
$$\Delta = \frac{a_c - a_c'}{a_c} \times 100\% = \frac{6.96 - 5.55}{6.96} \times 100\% = \left(1 - \frac{1}{1.12^2}\right) \times 100\% = (1 - 0.7972) \times 100\% \approx 20.28\%$$
The lack of structural constraint on the free surface causes an edge crack to be $12\%$ more intense for a given size, reducing the allowable safe crack length by over $20.3\%$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Internal crack critical half-length: $a_c = 6.96\text{ mm}$ (total length $2a_c = 13.9\text{ mm}$)<br>
Edge crack critical depth: $a_c' = 5.55\text{ mm}$<br>
Edge crack configuration reduces allowable crack size by $20.3\%$ due to free-surface relaxation ($Y = 1.12$).
</div>"""
})

# ==========================================
# Problem 9
# ==========================================
add({
    "num": 9,
    "title": "Plane Stress vs. Plane Strain Fracture Toughness ($K_c$ vs. $K_{Ic}$)",
    "difficulty": "Medium",
    "category": "Linear Elastic Fracture Mechanics",
    "tags": ["Plane Strain", "Plane Stress", "Thickness Effect", "KIc Plateau"],
    "statement": r"""When measuring the apparent fracture toughness $K_c$ of a metal plate containing a through-crack as a function of plate thickness $B$:
- Very thin sheets exhibit an elevated apparent toughness $K_c \gg K_{Ic}$ with $100\%$ slanted $45^\circ$ shear lips.
- As thickness $B$ increases, $K_c$ decreases and asymptotically levels off to a lower-bound plateau value $K_{Ic}$ with flat, square fracture surfaces.
<br><br>
1. Explain the stress state transformation: why do thin sheets experience <strong>plane stress</strong> ($\sigma_z = 0$) while thick plates experience <strong>plane strain</strong> ($\varepsilon_z = 0, \sigma_z = \nu(\sigma_x + \sigma_y) > 0$)?<br>
2. Explain how out-of-plane constraint in thick plates suppresses the plastic zone size and lowers apparent fracture toughness.<br>
3. Why is $K_{Ic}$ (plane strain fracture toughness) considered a true, geometry-independent material property, while $K_c$ is not?<br>
4. State the ASTM E399 minimum specimen thickness criterion required to guarantee a valid $K_{Ic}$ measurement.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Stress state transformation</strong><br>
- <em>Thin sheets:</em> Both top and bottom surfaces are traction-free free surfaces ($\sigma_z = 0$). Because the plate is extremely thin, the condition $\sigma_z \approx 0$ extends throughout the entire thickness. The material can contract freely in the thickness direction ($\varepsilon_z = -\frac{\nu}{E}(\sigma_x + \sigma_y)$), creating a <strong>plane stress</strong> condition.<br>
- <em>Thick plates:</em> Near the plate mid-plane, the surrounding bulk elastic material acts as a rigid clamp preventing lateral contraction in the $z$-direction ($\varepsilon_z = 0$). By Hooke's law, this kinematic constraint generates a large out-of-plane tensile stress:
$$\sigma_z = \nu(\sigma_x + \sigma_y) > 0$$
creating a severe triaxial tensile state known as <strong>plane strain</strong>.
</div>
<div class="solution-step">
<strong>Step 2: Suppression of plastic zone and toughness</strong><br>
Plastic yielding is driven by shear stress (von Mises or Tresca).
In plane stress ($\sigma_1 > \sigma_2 > 0, \sigma_3 = 0$), the maximum shear stress is large ($\tau_{\text{max}} = \sigma_1 / 2$). Dislocation slip operates freely on $45^\circ$ planes through the thickness, creating a large plastic zone that absorbs immense plastic work energy.
In plane strain, the tensile constraint $\sigma_3 = \sigma_z \approx 2\nu \sigma_1 \approx 0.6\text{--}0.7\sigma_1$ raises the mean hydrostatic stress and compresses the shear stress difference ($\sigma_1 - \sigma_3$). This shrinks the crack-tip plastic zone volume by a factor of 3 to 6:
$$r_{p,\text{plane strain}} \approx \frac{1}{3} r_{p,\text{plane stress}}$$
With a severely constricted plastic dissipation zone, the material fractures at a much lower energy release rate.
</div>
<div class="solution-step">
<strong>Step 3: Why $K_{Ic}$ is a true material property</strong><br>
Once thickness $B$ is large enough that plane strain prevails across $> 95\%$ of the crack front, further increases in thickness produce zero change in constraint or plastic zone size. The fracture toughness reaches a reproducible, geometry-independent lower-bound plateau ($K_{Ic}$) that depends only on composition and microstructure, functioning as a true material constant (like Young's modulus).
</div>
<div class="solution-step">
<strong>Step 4: ASTM E399 validity criterion</strong><br>
To ensure full plane strain constraint, ASTM E399 mandates:
$$B \ge 2.5 \left(\frac{K_{Ic}}{\sigma_y}\right)^2, \quad a \ge 2.5 \left(\frac{K_{Ic}}{\sigma_y}\right)^2, \quad W - a \ge 2.5 \left(\frac{K_{Ic}}{\sigma_y}\right)^2$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Thin sheets: Plane stress ($\sigma_z = 0$), free lateral contraction, large plastic zone, high $K_c$, $45^\circ$ shear lips.<br>
Thick plates: Plane strain ($\varepsilon_z = 0$), high tensile triaxiality ($\sigma_z > 0$), plastic zone shrinks by $\sim 3\times$, flat cleavage.<br>
$K_{Ic}$ is a lower-bound geometry-independent material property.<br>
ASTM E399 criterion: $B, a, (W-a) \ge 2.5 (K_{Ic}/\sigma_y)^2$.
</div>"""
})

# ==========================================
# Problem 10
# ==========================================
add({
    "num": 10,
    "title": "ASTM E399 Specimen Size Verification for Valid $K_{Ic}$ Testing",
    "difficulty": "Medium",
    "category": "Linear Elastic Fracture Mechanics",
    "tags": ["ASTM E399", "Validity Criterion", "Compact Tension", "Specimen Sizing"],
    "statement": r"""A fracture mechanics test engineer conducts a standard ASTM E399 fracture toughness test on a Compact Tension C(T) specimen of a high-strength aluminum alloy 7075-T651 ($\sigma_y = 500\text{ MPa}$).
The specimen dimensions are: thickness $B = 12.5\text{ mm}$ ($0.0125\text{ m}$), width $W = 50.0\text{ mm}$, and fatigue pre-crack length $a = 25.0\text{ mm}$ ($a/W = 0.50$).
The test records a provisional fracture toughness value $P_Q = 14.2\text{ kN}$, yielding a provisional toughness $K_Q = 29.5\text{ MPa}\sqrt{\text{m}}$.
<br><br>
1. Calculate the ASTM E399 minimum required thickness $B_{\text{min}} = 2.5\left(\frac{K_Q}{\sigma_y}\right)^2$.<br>
2. Determine whether the test satisfies the thickness validity requirement ($B \ge B_{\text{min}}$). Is $K_Q$ a valid $K_{Ic}$ measurement?<br>
3. The engineer now tests a much tougher structural steel: $\sigma_y = 380\text{ MPa}$, estimated $K_{Ic} \approx 95.0\text{ MPa}\sqrt{\text{m}}$. Calculate the minimum specimen thickness $B_{\text{min}}$ required for a valid test on this steel.<br>
4. Why is valid $K_{Ic}$ testing extremely difficult and expensive for low-strength, high-toughness ductile steels?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate $B_{\text{min}}$ for aluminum 7075-T651</strong><br>
Given: $K_Q = 29.5\text{ MPa}\sqrt{\text{m}}$, $\sigma_y = 500\text{ MPa}$:
$$\frac{K_Q}{\sigma_y} = \frac{29.5}{500} = 0.0590\text{ m}^{1/2}$$
$$\left(\frac{K_Q}{\sigma_y}\right)^2 = (0.0590)^2 = 0.003481\text{ m} = 3.481\text{ mm}$$
$$B_{\text{min}} = 2.5 \times 3.481\text{ mm} \approx 8.70\text{ mm} = 0.00870\text{ m}$$
</div>
<div class="solution-step">
<strong>Step 2: Validity check for aluminum test</strong><br>
Actual specimen thickness: $B = 12.5\text{ mm}$.
Comparing:
$$B = 12.5\text{ mm} > B_{\text{min}} = 8.70\text{ mm}$$
Also check crack length:
$$a = 25.0\text{ mm} > 8.70\text{ mm}$$
Ligament:
$$W - a = 50.0 - 25.0 = 25.0\text{ mm} > 8.70\text{ mm}$$
All ASTM E399 size requirements are completely satisfied. Therefore, <strong>$K_Q = K_{Ic} = 29.5\text{ MPa}\sqrt{\text{m}}$ is a valid plane strain fracture toughness measurement</strong>.
</div>
<div class="solution-step">
<strong>Step 3: Calculate $B_{\text{min}}$ for ductile structural steel</strong><br>
Given: $\sigma_y = 380\text{ MPa}$, $K_Q = 95.0\text{ MPa}\sqrt{\text{m}}$:
$$\frac{K_Q}{\sigma_y} = \frac{95.0}{380} = 0.250\text{ m}^{1/2}$$
$$\left(\frac{K_Q}{\sigma_y}\right)^2 = (0.250)^2 = 0.0625\text{ m} = 62.5\text{ mm}$$
$$B_{\text{min}} = 2.5 \times 62.5\text{ mm} = 156.25\text{ mm} \approx 15.6\text{ cm} \approx 6.15\text{ inches}!$$
</div>
<div class="solution-step">
<strong>Step 4: Why ductile steels are difficult to test with LEFM</strong><br>
Because $B_{\text{min}} \propto (K_{Ic} / \sigma_y)^2$, high toughness combined with modest yield strength causes the required specimen thickness to explode. Testing this steel would require a solid steel block over $15.6\text{ cm}$ ($6.15\text{ inches}$) thick, with width $W = 2B \approx 31\text{ cm}$ and weighing over $150\text{ kg}$, requiring massive multi-meganewton hydraulic test frames. For this reason, ductile metals are evaluated using Elastic-Plastic Fracture Mechanics (EPFM) via the $J$-Integral (ASTM E1820) or Crack Tip Opening Displacement (CTOD), which can test standard thin specimens.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Al 7075-T651: $B_{\text{min}} = 8.70\text{ mm}$; since $B = 12.5\text{ mm} > 8.70\text{ mm}$, the test is <strong>valid</strong> ($K_{Ic} = 29.5\text{ MPa}\sqrt{\text{m}}$).<br>
Structural steel: $B_{\text{min}} = 156.3\text{ mm}$ ($15.6\text{ cm}$).<br>
LEFM requires impractically massive specimens for ductile steels ($B \propto (K_{Ic}/\sigma_y)^2$); EPFM ($J$-integral/CTOD) is used instead.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 8 Part 1: P1-P10 added. Current total: {len(P)}")

# ==========================================
# Problem 11
# ==========================================
add({
    "num": 11,
    "title": "Theoretical Cleavage Strength of Brittle Solids",
    "difficulty": "Medium",
    "category": "Fracture Fundamentals",
    "tags": ["Theoretical Strength", "Cleavage", "Orowan Derivation", "Surface Energy"],
    "statement": r"""In 1949, E. Orowan derived the theoretical cleavage strength $\sigma_{\text{th}}$ required to pull adjacent atomic planes apart simultaneously in a defect-free crystal.
Assuming the cohesive restoring stress $\sigma(x)$ varies sinusoidally with displacement $x$:
$$\sigma(x) = \sigma_{\text{th}} \sin\left(\frac{2\pi x}{\lambda}\right) \approx \sigma_{\text{th}} \left(\frac{2\pi x}{\lambda}\right) \quad (\text{for small } x)$$
where $\lambda$ is the interaction wavelength.
Equating the work of fracture to the surface energy of two newly created cleavage surfaces ($2\gamma_s$):
$$\int_0^{\lambda/2} \sigma(x) dx = 2\gamma_s$$
<br>
1. Using Hooke's law $\sigma = E (x / a_0)$, show that $\lambda = \frac{2\pi a_0 \sigma_{\text{th}}}{E}$, where $a_0$ is the equilibrium lattice plane spacing.<br>
2. Substitute $\lambda$ into the surface energy integral and derive Orowan's formula:
$$\sigma_{\text{th}} = \sqrt{\frac{E \gamma_s}{a_0}} \approx \frac{E}{10}$$
3. For alumina ceramic ($\text{Al}_2\text{O}_3$ sapphire: $E = 380\text{ GPa}$, $\gamma_s = 1.0\text{ J/m}^2$, $a_0 = 0.22\text{ nm}$), calculate $\sigma_{\text{th}}$.<br>
4. The measured tensile fracture strength of bulk polycrystalline alumina is typically only $\sigma_f \approx 300\text{ MPa}$. Calculate the discrepancy ratio $\sigma_{\text{th}} / \sigma_f$ and explain why it exists.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Relate $\lambda$ to Hooke's law</strong><br>
For small displacements ($x \ll \lambda$):
$$\sigma(x) \approx \sigma_{\text{th}} \left(\frac{2\pi x}{\lambda}\right)$$
From Hooke's law with strain $\varepsilon = x / a_0$:
$$\sigma = E \varepsilon = E \left(\frac{x}{a_0}\right)$$
Equating the slopes:
$$\sigma_{\text{th}} \left(\frac{2\pi}{\lambda}\right) = \frac{E}{a_0} \implies \lambda = \frac{2\pi a_0 \sigma_{\text{th}}}{E}$$
</div>
<div class="solution-step">
<strong>Step 2: Integration and derivation of $\sigma_{\text{th}}$</strong><br>
The work required to separate the planes to infinity equals the surface energy of two faces ($2\gamma_s$):
$$\int_0^{\lambda/2} \sigma_{\text{th}} \sin\left(\frac{2\pi x}{\lambda}\right) dx = \sigma_{\text{th}} \left[-\frac{\lambda}{2\pi}\cos\left(\frac{2\pi x}{\lambda}\right)\right]_0^{\lambda/2} = \sigma_{\text{th}} \frac{\lambda}{2\pi} [-\cos\pi + \cos 0] = \sigma_{\text{th}} \frac{\lambda}{\pi} = 2\gamma_s$$
Substitute $\lambda = \frac{2\pi a_0 \sigma_{\text{th}}}{E}$:
$$\sigma_{\text{th}} \frac{1}{\pi} \left(\frac{2\pi a_0 \sigma_{\text{th}}}{E}\right) = 2\gamma_s \implies \frac{2 a_0 \sigma_{\text{th}}^2}{E} = 2\gamma_s \implies \sigma_{\text{th}}^2 = \frac{E \gamma_s}{a_0}$$
$$\sigma_{\text{th}} = \sqrt{\frac{E \gamma_s}{a_0}}$$
Assuming $\gamma_s \approx E a_0 / 100$: $\sigma_{\text{th}} \approx \sqrt{E^2 / 100} = \frac{E}{10}$.
</div>
<div class="solution-step">
<strong>Step 3: Calculate $\sigma_{\text{th}}$ for alumina</strong><br>
Given: $E = 380 \times 10^9\text{ Pa}$, $\gamma_s = 1.0\text{ J/m}^2$, $a_0 = 0.22 \times 10^{-9}\text{ m}$:
$$\sigma_{\text{th}} = \sqrt{\frac{(380 \times 10^9) \times 1.0}{0.22 \times 10^{-9}}} = \sqrt{\frac{3.80 \times 10^{11}}{0.22 \times 10^{-9}}} = \sqrt{1.7273 \times 10^{21}} \approx 4.156 \times 10^{10}\text{ Pa} \approx 41.56\text{ GPa}$$
Using the approximation $E/10$: $\sigma_{\text{th}} \approx 38\text{ GPa}$.
</div>
<div class="solution-step">
<strong>Step 4: Ratio and explanation of discrepancy</strong><br>
$$\frac{\sigma_{\text{th}}}{\sigma_f} = \frac{41,560\text{ MPa}}{300\text{ MPa}} \approx 138.5$$
<em>Physical explanation:</em> Bulk ceramics invariably contain microscopic manufacturing defects: sintering pores, microcracks, grain boundary flaws, and surface scratches ($a \sim 10\text{--}50\text{ }\mu\text{m}$). As proven by Inglis and Griffith, these pre-existing flaws create intense stress concentrations that amplify applied loads by $>100\times$, nucleating cleavage at a macroscopic stress of just $300\text{ MPa}$. When tested as defect-free single-crystal nanoneedles or whiskers, alumina approaches its full theoretical strength ($\sim 40\text{ GPa}$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Derived: $\sigma_{\text{th}} = \sqrt{\frac{E\gamma_s}{a_0}} \approx \frac{E}{10}$<br>
Theoretical cleavage strength of alumina: $\sigma_{\text{th}} \approx 41.6\text{ GPa}$<br>
Discrepancy ratio: $\sigma_{\text{th}}/\sigma_f \approx 139\times$ due to stress-concentrating microflaws and sintering pores.
</div>"""
})

# ==========================================
# Problem 12
# ==========================================
add({
    "num": 12,
    "title": "Thermal Shock Resistance Parameter and Critical Temperature Drop",
    "difficulty": "Medium",
    "category": "Ceramic Fracture",
    "tags": ["Thermal Shock", "Thermal Shock Parameter", "Quenching", "Ceramics"],
    "statement": r"""When a hot brittle component is suddenly quenched into cold water, rapid surface contraction is constrained by the hotter interior, generating intense biaxial tensile surface stresses:
$$\sigma_{\text{thermal}} = \frac{E \alpha_L \Delta T}{1 - \nu}$$
Fracture initiates when $\sigma_{\text{thermal}}$ reaches the fracture strength $\sigma_f$.
The maximum quench temperature drop that the material can survive without cracking is the <strong>Thermal Shock Resistance Parameter ($R$)</strong>:
$$R = \Delta T_{\text{max}} = \frac{\sigma_f (1 - \nu)}{E \alpha_L}$$
<br>
Consider two engineering ceramics:
- Ceramic A: Standard Alumina ($\text{Al}_2\text{O}_3$): $\sigma_f = 350\text{ MPa}$, $E = 380\text{ GPa}$, $\nu = 0.25$, $\alpha_L = 8.5 \times 10^{-6}\text{ K}^{-1}$.
- Ceramic B: Fused Silica Glass ($\text{SiO}_2$): $\sigma_f = 70\text{ MPa}$, $E = 72\text{ GPa}$, $\nu = 0.17$, $\alpha_L = 0.50 \times 10^{-6}\text{ K}^{-1}$.
<br>
1. Calculate the thermal shock resistance parameter $R = \Delta T_{\text{max}}$ for both ceramics.<br>
2. Explain why a red-hot crucible ($1000^\circ\text{C}$) made of fused silica can be dropped directly into ice water without cracking, while alumina shatters instantly.<br>
3. Identify the material property that gives fused silica its legendary thermal shock immunity.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate $R = \Delta T_{\text{max}}$ for both ceramics</strong><br>
- <em>Ceramic A (Alumina):</em>
$$\text{Numerator} = \sigma_f (1 - \nu) = (350 \times 10^6\text{ Pa}) \times (1 - 0.25) = (350 \times 10^6) \times 0.75 = 2.625 \times 10^8\text{ Pa}$$
$$\text{Denominator} = E \alpha_L = (380 \times 10^9\text{ Pa}) \times (8.5 \times 10^{-6}\text{ K}^{-1}) = 3.230 \times 10^6\text{ Pa/K}$$
$$R_{\text{Alumina}} = \frac{2.625 \times 10^8}{3.230 \times 10^6} \approx 81.27\text{ K} \approx 81^\circ\text{C}$$
Alumina cannot survive a temperature quench exceeding $\Delta T \approx 81^\circ\text{C}$!
<br>
- <em>Ceramic B (Fused Silica Glass):</em>
$$\text{Numerator} = \sigma_f (1 - \nu) = (70 \times 10^6\text{ Pa}) \times (1 - 0.17) = (70 \times 10^6) \times 0.83 = 5.810 \times 10^7\text{ Pa}$$
$$\text{Denominator} = E \alpha_L = (72 \times 10^9\text{ Pa}) \times (0.50 \times 10^{-6}\text{ K}^{-1}) = 3.600 \times 10^4\text{ Pa/K}$$
$$R_{\text{Silica}} = \frac{5.810 \times 10^7}{3.600 \times 10^4} \approx 1,613.9\text{ K} \approx 1,614^\circ\text{C}$$
</div>
<div class="solution-step">
<strong>Step 2: Comparison and quenching behavior</strong><br>
Quenching from $1000^\circ\text{C}$ into ice water ($0^\circ\text{C}$) imposes a temperature shock $\Delta T = 1000^\circ\text{C}$.
- For alumina: $\Delta T = 1000^\circ\text{C} \gg R = 81^\circ\text{C}$. The induced thermal stress exceeds $\sigma_f$ by more than $12\times$, causing immediate catastrophic shattering.
- For fused silica: $\Delta T = 1000^\circ\text{C} < R = 1,614^\circ\text{C}$. The thermal stresses remain well below fracture strength, so the silica crucible emerges completely intact without a scratch.
</div>
<div class="solution-step">
<strong>Step 3: Key material property behind silica's immunity</strong><br>
The secret lies entirely in fused silica's <strong>exceptionally low coefficient of thermal expansion ($\alpha_L = 0.50 \times 10^{-6}\text{ K}^{-1}$)</strong>, which is $17\times$ smaller than alumina's. Because the 3D covalent silica network expands and contracts minimally upon temperature change, thermal strains ($\varepsilon_{\text{th}} = \alpha_L \Delta T$) are virtually zero, generating negligible thermal stresses.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Alumina: $R = \Delta T_{\text{max}} \approx 81^\circ\text{C}$<br>
Fused Silica: $R = \Delta T_{\text{max}} \approx 1,614^\circ\text{C}$ ($20\times$ higher resistance)<br>
Fused silica survives extreme thermal shock due to its near-zero thermal expansion coefficient ($\alpha_L = 0.5 \times 10^{-6}\text{ K}^{-1}$).
</div>"""
})

# ==========================================
# Problem 13
# ==========================================
add({
    "num": 13,
    "title": "Crack-Tip Plastic Zone Size: Plane Stress vs. Plane Strain",
    "difficulty": "Medium",
    "category": "Linear Elastic Fracture Mechanics",
    "tags": ["Plastic Zone Size", "Irwin Correction", "Plane Stress", "Plane Strain"],
    "statement": r"""Near the tip of a sharp crack, the elastic stress singularity exceeds the yield strength $\sigma_y$. Irwin showed that plastic yielding redistributes load, creating a circular plastic zone of radius $r_y$:
- For <strong>Plane Stress</strong>:
$$r_y = \frac{1}{2\pi} \left(\frac{K_I}{\sigma_y}\right)^2 \quad (\text{total plastic zone diameter } 2r_y = d_p = \frac{1}{\pi}\left(\frac{K_I}{\sigma_y}\right)^2)$$
- For <strong>Plane Strain</strong> (where triaxial tensile constraint raises effective yield resistance to $\approx 3\sigma_y$):
$$r_y = \frac{1}{6\pi} \left(\frac{K_I}{\sigma_y}\right)^2 \quad (\text{diameter } d_p = \frac{1}{3\pi}\left(\frac{K_I}{\sigma_y}\right)^2)$$
<br>
A structural steel beam with yield strength $\sigma_y = 450\text{ MPa}$ operates at a Mode I stress intensity factor $K_I = 45.0\text{ MPa}\sqrt{\text{m}}$.
<br><br>
1. Calculate the plastic zone radius $r_y$ and diameter $d_p$ under plane stress conditions.<br>
2. Calculate $r_y$ and $d_p$ under plane strain conditions.<br>
3. What is the ratio of plane stress to plane strain plastic zone volume? Explain how this confirms why thin sheets are tougher than thick plates.<br>
4. State Irwin's effective crack length correction: $a_{\text{eff}} = a + r_y$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate plastic zone size for Plane Stress</strong><br>
Given: $K_I = 45.0\text{ MPa}\sqrt{\text{m}}$, $\sigma_y = 450\text{ MPa}$:
$$\frac{K_I}{\sigma_y} = \frac{45.0}{450} = 0.100\text{ m}^{1/2}$$
$$\left(\frac{K_I}{\sigma_y}\right)^2 = (0.100)^2 = 0.0100\text{ m} = 10.0\text{ mm}$$
Radius:
$$r_{y,\text{stress}} = \frac{1}{2\pi} \left(\frac{K_I}{\sigma_y}\right)^2 = \frac{10.0\text{ mm}}{2\pi} \approx 1.5915\text{ mm} \approx 1.59\text{ mm}$$
Diameter:
$$d_{p,\text{stress}} = 2 r_{y,\text{stress}} = \frac{10.0\text{ mm}}{\pi} \approx 3.183\text{ mm} \approx 3.18\text{ mm}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate plastic zone size for Plane Strain</strong><br>
Radius:
$$r_{y,\text{strain}} = \frac{1}{6\pi} \left(\frac{K_I}{\sigma_y}\right)^2 = \frac{10.0\text{ mm}}{6\pi} \approx 0.5305\text{ mm} \approx 0.53\text{ mm}$$
Diameter:
$$d_{p,\text{strain}} = 2 r_{y,\text{strain}} = \frac{10.0\text{ mm}}{3\pi} \approx 1.061\text{ mm} \approx 1.06\text{ mm}$$
</div>
<div class="solution-step">
<strong>Step 3: Ratio and toughness explanation</strong><br>
$$\frac{r_{y,\text{stress}}}{r_{y,\text{strain}}} = \frac{1 / (2\pi)}{1 / (6\pi)} = 3.0$$
The plastic zone radius is $3\times$ larger in plane stress than in plane strain.
Because plastic energy dissipation is proportional to the volume of the plastic zone ($\propto r_y^2 \times B$), the plane stress plastic zone absorbs roughly $3^2 = 9\times$ more energy per unit thickness. This massive energy dissipation explains why thin sheets have vastly higher apparent fracture toughness ($K_c$) than thick plates.
</div>
<div class="solution-step">
<strong>Step 4: Irwin's effective crack length correction</strong><br>
Because the plastic zone yields and cannot carry stresses above $\sigma_y$, load sheds into the surrounding elastic field. The elastic stress field behaves as if it surrounded an imaginary, slightly longer crack extending to the center of the plastic zone:
$$a_{\text{eff}} = a + r_y$$
Using $a_{\text{eff}}$ in $K_I = Y \sigma \sqrt{\pi a_{\text{eff}}}$ accounts for small-scale crack tip yielding within linear elasticity.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Plane stress: $r_y = 1.59\text{ mm}$, diameter $d_p = 3.18\text{ mm}$<br>
Plane strain: $r_y = 0.53\text{ mm}$, diameter $d_p = 1.06\text{ mm}$<br>
Plastic zone shrinks by $3\times$ in radius ($9\times$ in area) under plane strain.<br>
Irwin effective crack length: $a_{\text{eff}} = a + r_y$.
</div>"""
})

# ==========================================
# Problem 14
# ==========================================
add({
    "num": 14,
    "title": "Leak-Before-Break (LBB) Design Criterion for Pressure Vessels",
    "difficulty": "Hard",
    "category": "Design & Safety",
    "tags": ["Leak-Before-Break", "Pressure Vessel", "Critical Crack Depth", "Safe-Life"],
    "statement": r"""The <strong>Leak-Before-Break (LBB)</strong> design philosophy guarantees that if a crack grows through a pressure vessel wall, it will penetrate the full thickness and cause a detectable, non-catastrophic fluid leak rather than triggering an explosive, catastrophic burst.
The LBB condition requires that the critical crack size $a_c$ under operating hoop stress $\sigma_h$ be strictly greater than the wall thickness $t$:
$$a_c \ge t$$
Consider a thin-walled cylindrical pressure vessel of internal radius $r = 600\text{ mm}$ and wall thickness $t = 12.0\text{ mm}$ subjected to internal pressure $p = 4.0\text{ MPa}$.
The hoop stress is $\sigma_h = \frac{p r}{t}$.
For a semi-elliptical surface crack of depth $a$, the stress intensity factor is:
$$K_I = 1.12 \sigma_h \sqrt{\frac{\pi a}{Q}}$$
where the flaw shape parameter is $Q \approx 1.25$.
<br><br>
1. Calculate the operating hoop stress $\sigma_h$.<br>
2. Alloy 1 (High-Strength Low-Alloy Steel): $\sigma_y = 650\text{ MPa}$, $K_{Ic} = 90.0\text{ MPa}\sqrt{\text{m}}$. Calculate the critical crack depth $a_c$ and determine whether Alloy 1 satisfies the LBB criterion.<br>
3. Alloy 2 (Ultra-High-Strength Maraging Steel): $\sigma_y = 1800\text{ MPa}$, $K_{Ic} = 45.0\text{ MPa}\sqrt{\text{m}}$. Calculate $a_c$ for Alloy 2 and determine whether it satisfies LBB.<br>
4. Contrast the failure consequences for both alloys if a flaw grows through the vessel wall in service.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate hoop stress $\sigma_h$</strong><br>
$$\sigma_h = \frac{p r}{t} = \frac{(4.0\text{ MPa}) \times (600\text{ mm})}{12.0\text{ mm}} = \frac{2400}{12.0} = 200.0\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Critical crack depth for Alloy 1 (HSLA Steel)</strong><br>
Set $K_I = K_{Ic}$:
$$K_{Ic} = 1.12 \sigma_h \sqrt{\frac{\pi a_c}{Q}} \implies \sqrt{\frac{\pi a_c}{Q}} = \frac{K_{Ic}}{1.12 \sigma_h}$$
$$\frac{\pi a_c}{Q} = \left(\frac{K_{Ic}}{1.12 \sigma_h}\right)^2 \implies a_c = \frac{Q}{\pi} \left(\frac{K_{Ic}}{1.12 \sigma_h}\right)^2$$
For Alloy 1: $K_{Ic} = 90.0\text{ MPa}\sqrt{\text{m}}$:
$$1.12 \sigma_h = 1.12 \times 200.0 = 224.0\text{ MPa}$$
$$\frac{K_{Ic}}{1.12 \sigma_h} = \frac{90.0}{224.0} \approx 0.401786\text{ m}^{1/2}$$
$$\left(\frac{K_{Ic}}{1.12 \sigma_h}\right)^2 = (0.401786)^2 \approx 0.16143\text{ m} = 161.43\text{ mm}$$
$$a_{c1} = \frac{1.25}{\pi} \times 161.43\text{ mm} \approx 64.23\text{ mm}$$
Comparing with thickness $t = 12.0\text{ mm}$:
$$a_{c1} = 64.2\text{ mm} \gg t = 12.0\text{ mm}$$
Alloy 1 <strong>satisfies the Leak-Before-Break criterion with flying colors</strong>!
</div>
<div class="solution-step">
<strong>Step 3: Critical crack depth for Alloy 2 (Maraging Steel)</strong><br>
For Alloy 2: $K_{Ic} = 45.0\text{ MPa}\sqrt{\text{m}}$:
$$\frac{K_{Ic}}{1.12 \sigma_h} = \frac{45.0}{224.0} \approx 0.20089\text{ m}^{1/2}$$
$$a_{c2} = \frac{1.25}{\pi} \times (0.20089)^2 = \frac{1.25}{\pi} \times 0.040358\text{ m} \approx 0.016058\text{ m} = 16.06\text{ mm}$$
If operating at higher stress or with conservative $Y \approx 1.25$:
At $\sigma_h = 200\text{ MPa}$, $a_{c2} = 16.06\text{ mm} > 12.0\text{ mm}$.
However, if Alloy 2 were operated at its allowable design stress ($\sigma_h = 0.5 \sigma_y = 900\text{ MPa}$):
$$1.12 \sigma_h = 1.12 \times 900 = 1008\text{ MPa}$$
$$a_{c2}' = \frac{1.25}{\pi}\left(\frac{45.0}{1008}\right)^2 = \frac{1.25}{\pi}(0.04464)^2 \approx 0.79\text{ mm} \ll t = 12.0\text{ mm}$$
Operating at high stress, Alloy 2 completely fails LBB!
Even at $200\text{ MPa}$, an edge through-crack of length $2c = 2t = 24\text{ mm}$ gives $K_I = 200\sqrt{\pi(0.012)} \approx 38.8\text{ MPa}\sqrt{\text{m}}$, very close to $K_{Ic} = 45$.
</div>
<div class="solution-step">
<strong>Step 4: Failure consequences</strong><br>
- <strong>Alloy 1:</strong> The crack reaches depth $a = t = 12\text{ mm}$ while still far below its critical instability size ($a_c = 64.2\text{ mm}$). Fluid leaks through the wall harmlessly, dropping pressure and sounding pressure-loss alarms, enabling safe shutdown.
- <strong>Alloy 2:</strong> If operated at high stress, a microscopic flaw of depth $< 1\text{ mm}$ triggers catastrophic fast fracture before wall breakthrough, causing explosive fragmentation and shrapnel without warning.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Hoop stress: $\sigma_h = 200.0\text{ MPa}$<br>
Alloy 1 (HSLA): $a_c = 64.2\text{ mm} \gg t = 12.0\text{ mm} \implies$ <strong>Satisfies LBB</strong> (safe leak).<br>
High-strength brittle alloys fail LBB at high stresses ($a_c \ll t$), leading to catastrophic explosion.
</div>"""
})

# ==========================================
# Problem 15
# ==========================================
add({
    "num": 15,
    "title": "Charpy V-Notch (CVN) Impact Testing and Energy Calculation",
    "difficulty": "Easy",
    "category": "Impact Mechanics",
    "tags": ["Charpy Test", "Impact Energy", "Pendulum", "CVN"],
    "statement": r"""The Charpy V-notch (CVN) impact test (ASTM E23) evaluates the dynamic fracture resistance of materials under high strain rate loading and severe triaxial constraint.
A heavy pendulum hammer of mass $m = 22.0\text{ kg}$ is released from an initial height $h_0 = 1.35\text{ m}$ (initial angle $\beta_0$) and strikes the notched face of a standard $10 \times 10 \times 55\text{ mm}$ specimen supported as a simple beam.
After fracturing the specimen, the pendulum swings upward to a maximum post-impact height $h_f = 0.82\text{ m}$ (angle $\beta_f$).
Acceleration due to gravity is $g = 9.81\text{ m/s}^2$.
<br><br>
1. Derive the formula for the impact energy $K_V$ absorbed by the specimen in terms of $m, g, h_0$, and $h_f$, neglecting friction and windage losses.<br>
2. Calculate the total energy absorbed $K_V$ (in Joules).<br>
3. The cross-sectional ligament area behind the $2.0\text{ mm}$ standard $45^\circ$ V-notch is $A_L = 10\text{ mm} \times (10 - 2)\text{ mm} = 80.0\text{ mm}^2$. Calculate the specific impact toughness $a_K = K_V / A_L$ in $\text{J/cm}^2$.<br>
4. If a second, highly brittle cast iron specimen is tested and the pendulum swings to $h_f' = 1.32\text{ m}$, calculate the absorbed energy $K_V'$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Derivation of absorbed energy formula</strong><br>
By conservation of energy:
$$\text{Initial potential energy: } E_0 = m g h_0$$
$$\text{Final residual potential energy: } E_f = m g h_f$$
The mechanical energy absorbed during specimen fracture equals the loss in potential energy of the pendulum:
$$K_V = E_0 - E_f = m g (h_0 - h_f)$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate absorbed energy $K_V$</strong><br>
Given: $m = 22.0\text{ kg}$, $g = 9.81\text{ m/s}^2$, $h_0 = 1.35\text{ m}$, $h_f = 0.82\text{ m}$:
$$h_0 - h_f = 1.35 - 0.82 = 0.53\text{ m}$$
$$K_V = (22.0\text{ kg}) \times (9.81\text{ m/s}^2) \times (0.53\text{ m}) = 215.82 \times 0.53 \approx 114.38\text{ J}$$
</div>
<div class="solution-step">
<strong>Step 3: Calculate specific impact toughness $a_K$</strong><br>
Ligament area:
$$A_L = 80.0\text{ mm}^2 = 0.80\text{ cm}^2 = 80.0 \times 10^{-6}\text{ m}^2$$
$$a_K = \frac{K_V}{A_L} = \frac{114.38\text{ J}}{0.80\text{ cm}^2} \approx 143.0\text{ J/cm}^2 = 1.43\text{ MJ/m}^2$$
An impact energy of $114\text{ J}$ indicates outstanding ductile toughness (well above the structural steel requirement of $27\text{ J}$).
</div>
<div class="solution-step">
<strong>Step 4: Brittle cast iron test</strong><br>
For $h_f' = 1.32\text{ m}$:
$$h_0 - h_f' = 1.35 - 1.32 = 0.03\text{ m}$$
$$K_V' = (22.0) \times (9.81) \times (0.03) \approx 6.47\text{ J}$$
The brittle cast iron absorbs only $6.5\text{ J}$, shattering with virtually zero resistance.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Formula: $K_V = m g (h_0 - h_f)$<br>
Ductile specimen: $K_V = 114.4\text{ J}$, specific toughness $a_K = 143.0\text{ J/cm}^2$<br>
Brittle cast iron: $K_V' = 6.47\text{ J}$ ($< 6\%$ of ductile specimen).
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 8 Part 1: P1-P15 added. Current total: {len(P)}")

# ==========================================
# Problem 16
# ==========================================
add({
    "num": 16,
    "title": "Crack Tip Opening Displacement (CTOD) and Blunting",
    "difficulty": "Medium",
    "category": "Elastic-Plastic Fracture Mechanics",
    "tags": ["CTOD", "Crack Tip Blunting", "EPFM", "Displacement"],
    "statement": r"""When linear elastic fracture mechanics (LEFM) ceases to be valid due to extensive crack-tip plasticity, the <strong>Crack Tip Opening Displacement (CTOD, $\delta_t$)</strong> serves as a fundamental fracture criterion.
Under small-scale yielding, Irwin's and Wells' relationship connects CTOD to the stress intensity factor $K_I$:
$$\delta_t = \frac{K_I^2}{m \sigma_y E}$$
where $m \approx 1.0$ for plane stress and $m \approx 2.0$ for plane strain.
<br><br>
A pressure vessel steel ($E = 205\text{ GPa}$, $\nu = 0.30$, yield strength $\sigma_y = 480\text{ MPa}$) operates under plane strain conditions ($m = 2.0$).
<br><br>
1. Calculate the critical crack-tip opening displacement $\delta_{tc}$ at the moment of fracture if the plane strain fracture toughness is $K_{Ic} = 85.0\text{ MPa}\sqrt{\text{m}}$.<br>
2. Calculate the corresponding plastic zone diameter $d_p = \frac{1}{3\pi}\left(\frac{K_{Ic}}{\sigma_y}\right)^2$.<br>
3. Compare $\delta_{tc}$ with $d_p$ and explain the physical meaning of crack-tip blunting prior to unstable tearing.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate critical CTOD $\delta_{tc}$</strong><br>
Given: $K_{Ic} = 85.0\text{ MPa}\sqrt{\text{m}} = 85.0 \times 10^6\text{ Pa}\sqrt{\text{m}}$, $\sigma_y = 480 \times 10^6\text{ Pa}$, $E = 205 \times 10^9\text{ Pa}$, $m = 2.0$:
$$K_{Ic}^2 = (85.0 \times 10^6)^2 = 7.225 \times 10^{15}\text{ Pa}^2\cdot\text{m}$$
$$m \sigma_y E = 2.0 \times (480 \times 10^6\text{ Pa}) \times (205 \times 10^9\text{ Pa}) = 1.968 \times 10^{20}\text{ Pa}^2$$
$$\delta_{tc} = \frac{7.225 \times 10^{15}}{1.968 \times 10^{20}} \approx 3.671 \times 10^{-5}\text{ m} \approx 36.71\text{ }\mu\text{m}$$
At the point of fracture instability, the opposing crack faces at the original crack tip have pulled apart by $36.7\text{ }\mu\text{m}$.
</div>
<div class="solution-step">
<strong>Step 2: Calculate plastic zone diameter $d_p$</strong><br>
$$\frac{K_{Ic}}{\sigma_y} = \frac{85.0}{480} \approx 0.17708\text{ m}^{1/2}$$
$$\left(\frac{K_{Ic}}{\sigma_y}\right)^2 = (0.17708)^2 \approx 0.03136\text{ m} = 31.36\text{ mm}$$
$$d_p = \frac{31.36\text{ mm}}{3\pi} = \frac{31.36}{9.4248} \approx 3.327\text{ mm} = 3,327\text{ }\mu\text{m}$$
</div>
<div class="solution-step">
<strong>Step 3: Comparison and physical significance of blunting</strong><br>
$$\frac{d_p}{\delta_{tc}} = \frac{3,327\text{ }\mu\text{m}}{36.71\text{ }\mu\text{m}} \approx 90.6$$
The plastic zone extends over $3.33\text{ mm}$ ($> 90\times$ larger than the CTOD).
<em>Physical meaning:</em> An atomistically sharp fatigue crack begins with an initial tip radius of virtually zero ($\rho_t \to 0$). Under rising tensile load, dislocations nucleate from the tip and glide along slip lines inclined at $\pm 45^\circ$. This localized shear opens the crack faces into a rounded, U-shaped blunted notch. This physical stretching and blunting of the tip relaxes peak stresses and delays crack propagation until $\delta_t$ reaches the critical material-specific separation $\delta_{tc}$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Critical CTOD: $\delta_{tc} = 36.7\text{ }\mu\text{m}$<br>
Plastic zone diameter: $d_p = 3.33\text{ mm}$ ($91\times \delta_{tc}$)<br>
CTOD directly measures the physical plastic blunting of the crack tip before crack tearing commences.
</div>"""
})

# ==========================================
# Problem 17
# ==========================================
add({
    "num": 17,
    "title": "Non-Destructive Inspection (NDI) Resolution and Proof Testing",
    "difficulty": "Hard",
    "category": "Design & Safety",
    "tags": ["NDI Resolution", "Proof Testing", "Flaw Detection", "Safe Operating Stress"],
    "statement": r"""In fracture-critical aerospace structures, the maximum allowable design stress is determined by the minimum flaw size detectable by Non-Destructive Inspection (NDI) techniques (such as ultrasonic testing, eddy current, or X-ray radiography).
A solid rocket motor casing fabricated from D6ac high-strength steel ($\sigma_y = 1500\text{ MPa}$, $K_{Ic} = 65.0\text{ MPa}\sqrt{\text{m}}$) is inspected with an ultrasonic technique that has a certified flaw detection resolution of $a_{\text{NDI}} = 1.80\text{ mm}$ (any flaw larger than $1.80\text{ mm}$ is guaranteed to be detected and rejected).
For a surface crack, $K_I = 1.12 \sigma \sqrt{\pi a}$.
<br><br>
1. Assuming an undetected surface flaw of size $a = a_{\text{NDI}} = 1.80\text{ mm}$ exists in the casing, calculate the maximum safe operating tensile stress $\sigma_{\text{op}}$ with a design safety factor $N = 1.50$ against fracture ($K_I \le K_{Ic} / N$).<br>
2. To guarantee structural integrity without relying entirely on NDI, the casing undergoes a pre-service <strong>hydraulic proof test</strong> at proof stress $\sigma_{\text{proof}} = 1100\text{ MPa}$.
If the vessel survives this proof test without bursting, what is the guaranteed maximum possible flaw size $a_{\text{proof}}$ that could remain in the casing?<br>
3. Compare $a_{\text{proof}}$ with $a_{\text{NDI}}$ and explain the engineering philosophy of proof testing.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate safe operating stress $\sigma_{\text{op}}$</strong><br>
Set $K_I = \frac{K_{Ic}}{N} = \frac{65.0\text{ MPa}\sqrt{\text{m}}}{1.50} \approx 43.33\text{ MPa}\sqrt{\text{m}}$.
From $K_I = 1.12 \sigma_{\text{op}} \sqrt{\pi a_{\text{NDI}}}$:
$$\sigma_{\text{op}} = \frac{K_I}{1.12 \sqrt{\pi a_{\text{NDI}}}}$$
Given $a_{\text{NDI}} = 1.80 \times 10^{-3}\text{ m}$:
$$\sqrt{\pi a_{\text{NDI}}} = \sqrt{\pi \times (1.80 \times 10^{-3})} = \sqrt{0.0056549} \approx 0.075199\text{ m}^{1/2}$$
$$\sigma_{\text{op}} = \frac{43.33\text{ MPa}}{1.12 \times 0.075199} = \frac{43.33}{0.084223} \approx 514.47\text{ MPa}$$
The casing may be safely operated up to $\sigma_{\text{op}} \approx 514.5\text{ MPa}$.
</div>
<div class="solution-step">
<strong>Step 2: Maximum possible flaw size surviving proof test</strong><br>
During the proof test, if a flaw had produced $K_I \ge K_{Ic}$, the vessel would have burst.
Since the vessel survived without bursting at $\sigma_{\text{proof}} = 1100\text{ MPa}$:
$$K_I = 1.12 \sigma_{\text{proof}} \sqrt{\pi a_{\text{proof}}} \le K_{Ic}$$
$$\sqrt{\pi a_{\text{proof}}} \le \frac{K_{Ic}}{1.12 \sigma_{\text{proof}}} = \frac{65.0\text{ MPa}\sqrt{\text{m}}}{1.12 \times 1100\text{ MPa}} = \frac{65.0}{1232.0} \approx 0.05276\text{ m}^{1/2}$$
$$\pi a_{\text{proof}} \le (0.05276)^2 \approx 0.0027836\text{ m}$$
$$a_{\text{proof}} = \frac{0.0027836}{\pi} \approx 8.86 \times 10^{-4}\text{ m} = 0.886\text{ mm} \approx 0.89\text{ mm}$$
</div>
<div class="solution-step">
<strong>Step 3: Comparison and proof testing philosophy</strong><br>
$$\frac{a_{\text{proof}}}{a_{\text{NDI}}} = \frac{0.886\text{ mm}}{1.80\text{ mm}} \approx 0.49$$
Surviving the proof test guarantees that no crack larger than $0.89\text{ mm}$ exists in the casing—a threshold nearly $2\times$ tighter than the best NDI inspection limit ($1.80\text{ mm}$)!
<em>Engineering Philosophy:</em> Proof testing screens out components with lethal defects by subjecting them to a deliberate overload under controlled conditions before deployment. Any component that survives the proof test is physically guaranteed to contain no flaw exceeding $a_{\text{proof}}$, establishing an unambiguous, non-destructive baseline for safe-life fatigue calculations.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Safe operating stress: $\sigma_{\text{op}} = 514.5\text{ MPa}$ ($N = 1.5$ safety factor based on NDI limit $1.8\text{ mm}$).<br>
Surviving $1100\text{ MPa}$ proof test guarantees no crack exceeds $a_{\text{proof}} = 0.89\text{ mm}$.<br>
Proof testing provides $2\times$ tighter flaw size assurance than NDI inspection.
</div>"""
})

# ==========================================
# Problem 18
# ==========================================
add({
    "num": 18,
    "title": "Stress Corrosion Cracking (SCC) Threshold $K_{Iscc}$ and Crack Velocity",
    "difficulty": "Medium",
    "category": "Environmental Fracture",
    "tags": ["Stress Corrosion Cracking", "KISCC", "Subcritical Crack Growth", "Corrosion Fatigue"],
    "statement": r"""Stress Corrosion Cracking (SCC) is the insidious, subcritical growth of cracks caused by the synergistic interaction of sustained static tensile stress and a specific corrosive environment (e.g., high-strength aluminum in saltwater, brass in ammonia, or stainless steel in chlorides).
The crack growth velocity $v = da/dt$ as a function of stress intensity factor $K_I$ displays three characteristic regimes:
- <strong>Stage I:</strong> Exponential increase in velocity starting at a threshold toughness $K_{Iscc}$.
- <strong>Stage II (Plateau):</strong> Stress-independent plateau velocity $(da/dt)_{\text{II}}$ controlled by environmental mass transport.
- <strong>Stage III:</strong> Rapid acceleration as $K_I$ approaches mechanical fracture toughness $K_{Ic}$.
<br><br>
A high-strength alloy bolt with $K_{Ic} = 60.0\text{ MPa}\sqrt{\text{m}}$ has an SCC threshold $K_{Iscc} = 15.0\text{ MPa}\sqrt{\text{m}}$ in marine salt fog.
Its Stage II plateau velocity is $(da/dt)_{\text{II}} = 1.2 \times 10^{-7}\text{ m/s}$ ($0.432\text{ mm/h}$).
The bolt is tightened to a sustained tensile stress $\sigma = 320\text{ MPa}$ ($Y = 1.12$).
<br><br>
1. Calculate the critical crack depth $a_{\text{mech}}$ for fast mechanical fracture ($K_I = K_{Ic}$).<br>
2. Calculate the threshold crack depth $a_{\text{scc}}$ below which SCC crack growth cannot initiate ($K_I < K_{Iscc}$).<br>
3. If a pre-existing machining scratch has depth $a_0 = 0.60\text{ mm}$ ($> a_{\text{scc}}$), estimate the time (in hours) required for the crack to grow through the Stage II plateau to trigger catastrophic fracture at $a_{\text{mech}}$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Critical mechanical crack depth $a_{\text{mech}}$</strong><br>
$$K_{Ic} = 1.12 \sigma \sqrt{\pi a_{\text{mech}}} \implies a_{\text{mech}} = \frac{1}{\pi}\left(\frac{K_{Ic}}{1.12 \sigma}\right)^2$$
$$1.12 \sigma = 1.12 \times 320 = 358.4\text{ MPa}$$
$$\frac{K_{Ic}}{1.12 \sigma} = \frac{60.0}{358.4} \approx 0.16741\text{ m}^{1/2}$$
$$a_{\text{mech}} = \frac{1}{\pi} (0.16741)^2 = \frac{0.028026}{\pi} \approx 0.008921\text{ m} = 8.92\text{ mm}$$
</div>
<div class="solution-step">
<strong>Step 2: SCC initiation threshold crack depth $a_{\text{scc}}$</strong><br>
$$K_{Iscc} = 1.12 \sigma \sqrt{\pi a_{\text{scc}}} \implies a_{\text{scc}} = \frac{1}{\pi}\left(\frac{K_{Iscc}}{1.12 \sigma}\right)^2$$
$$\frac{K_{Iscc}}{1.12 \sigma} = \frac{15.0}{358.4} \approx 0.041853\text{ m}^{1/2}$$
$$a_{\text{scc}} = \frac{1}{\pi} (0.041853)^2 = \frac{0.0017516}{\pi} \approx 0.0005576\text{ m} = 0.558\text{ mm} \approx 0.56\text{ mm}$$
Any surface flaw deeper than $0.56\text{ mm}$ will trigger active stress corrosion cracking under this load!
</div>
<div class="solution-step">
<strong>Step 3: Time to catastrophic fracture</strong><br>
The crack initiates at $a_0 = 0.60\text{ mm}$ and grows to $a_{\text{mech}} = 8.92\text{ mm}$.
Total crack extension distance:
$$\Delta a = a_{\text{mech}} - a_0 = 8.92 - 0.60 = 8.32\text{ mm} = 8.32 \times 10^{-3}\text{ m}$$
Assuming steady growth at the Stage II plateau rate $v_{\text{II}} = 1.2 \times 10^{-7}\text{ m/s}$:
$$t_{\text{fail}} = \frac{\Delta a}{v_{\text{II}}} = \frac{8.32 \times 10^{-3}\text{ m}}{1.2 \times 10^{-7}\text{ m/s}} \approx 69,333\text{ seconds}$$
Convert to hours:
$$t_{\text{fail}} = \frac{69,333}{3,600} \approx 19.26\text{ hours}$$
The bolt will undergo sudden, catastrophic brittle fracture in less than $20\text{ hours}$ in service, despite operating far below its nominal yield strength!
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Critical mechanical crack size: $a_{\text{mech}} = 8.92\text{ mm}$<br>
SCC threshold flaw depth: $a_{\text{scc}} = 0.56\text{ mm}$<br>
Time to catastrophic fracture: $t_{\text{fail}} \approx 19.3\text{ hours}$<br>
SCC causes rapid, unexpected catastrophic failure under static loads far below tensile yield strength.
</div>"""
})

# ==========================================
# Problem 19
# ==========================================
add({
    "num": 19,
    "title": "Hydrogen Embrittlement: Mechanisms and Delayed Catastrophic Failure",
    "difficulty": "Hard",
    "category": "Environmental Fracture",
    "tags": ["Hydrogen Embrittlement", "HEDE", "HELP", "Delayed Fracture"],
    "statement": r"""Hydrogen embrittlement (HE) is one of the most insidious failure mechanisms in ultra-high-strength steels ($\sigma_{\text{UTS}} > 1000\text{ MPa}$), titanium alloys, and nickel superalloys.
Atomic hydrogen ($\text{H}^+$ or $\text{H}$) dissolves interstitials into the lattice from electroplating, pickling, welding, or cathodic protection, and diffuses rapidly to regions of high tensile hydrostatic stress ahead of crack tips.
<br><br>
1. Distinguish between <strong>Internal Hydrogen Embrittlement (IHE)</strong> and <strong>Environmental Hydrogen Embrittlement (EHE)</strong>.<br>
2. Explain the two dominant micromechanical theories of hydrogen embrittlement:
   (a) <strong>Hydrogen-Enhanced Decohesion (HEDE)</strong> model.<br>
   (b) <strong>Hydrogen-Enhanced Localized Plasticity (HELP)</strong> model.<br>
3. Why are high-strength steels dramatically more susceptible to hydrogen embrittlement than low-carbon structural steels?<br>
4. Describe the standard industrial baking heat treatment ($190^\circ\text{C}\text{ to }210^\circ\text{C}$ for $4\text{--}24\text{ hours}$) used immediately following electroplating of high-strength fasteners to prevent delayed fracture.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: IHE vs. EHE</strong><br>
- <strong>Internal Hydrogen Embrittlement (IHE):</strong> Hydrogen is absorbed into the bulk metal during prior manufacturing processes (steelmaking, arc welding with damp flux, acid pickling, or electrolytic cadmium/zinc plating) and remains trapped inside the part during service.<br>
- <strong>Environmental Hydrogen Embrittlement (EHE):</strong> Hydrogen is generated continuously during service from external chemical/electrochemical reactions at the surface (e.g., aqueous corrosion, cathodic protection overpotentials, or exposure to high-pressure hydrogen gas).
</div>
<div class="solution-step">
<strong>Step 2: Two dominant microscopic theories</strong><br>
(a) <strong>Hydrogen-Enhanced Decohesion (HEDE):</strong> High hydrostatic tensile stress ($\sigma_m$) ahead of a crack tip attracts dissolved interstitial hydrogen atoms ($C_H = C_0 \exp(\sigma_m V_H / RT)$). The accumulated hydrogen donates electrons to the conduction band of host metal atoms, lowering the electron density between metal atoms and weakening the cohesive interatomic bond strength. As a result, brittle cleavage or intergranular separation occurs at stresses far below the normal cleavage strength.<br>
(b) <strong>Hydrogen-Enhanced Localized Plasticity (HELP):</strong> Hydrogen atmospheres screen the elastic stress fields of dislocations, reducing the repulsive interaction between approaching dislocations. This dramatically increases dislocation mobility and accelerates localized slip along specific shear planes directly ahead of the crack tip. Macroscopically the fracture looks brittle, but microscopically it is caused by intense sub-micron localized plastic shear.
</div>
<div class="solution-step">
<strong>Step 3: Why high-strength steels are exceptionally vulnerable</strong><br>
In high-strength steels ($\sigma_y > 1200\text{ MPa}$), the peak hydrostatic tensile stress ahead of a crack tip reaches $\sigma_m \approx 3\sigma_y \approx 3600\text{--}4500\text{ MPa}$. Because hydrogen segregation scales exponentially with hydrostatic stress ($\propto \exp(\sigma_m V_H / RT)$), hydrogen concentration amplifies by thousands of times at the tip. Furthermore, high-strength steels have very low fracture toughness ($K_{Ic}$) and minimal crack-tip blunting, meaning even a few parts per million (ppm) of dissolved hydrogen is sufficient to trigger delayed catastrophic cracking.
</div>
<div class="solution-step">
<strong>Step 4: Post-plating baking de-embrittlement</strong><br>
Electroplated fasteners (e.g., Grade 8 / 10.9 bolts) are placed in a furnace at $190^\circ\text{C}\text{ to }210^\circ\text{C}$ within 1 to 4 hours of plating. At $200^\circ\text{C}$, the diffusion coefficient of hydrogen in BCC iron is high enough for mobile hydrogen atoms to diffuse out through the plating into the atmosphere, or diffuse away to deep irreversible metallurgical traps (carbide interfaces), permanently reducing diffusible hydrogen below the critical embrittlement threshold ($< 0.1\text{ ppm}$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
IHE absorbs hydrogen during manufacture; EHE absorbs hydrogen from service environments.<br>
HEDE weakens atomic bond cohesive energy; HELP accelerates localized dislocation slip.<br>
High-strength steels suffer massive hydrogen accumulation due to huge crack-tip hydrostatic stresses ($\sigma_m \approx 3\sigma_y$).<br>
Baking at $200^\circ\text{C}$ for $4\text{--}24\text{ h}$ diffuses mobile hydrogen out of the steel, preventing catastrophic delayed fracture.
</div>"""
})

# ==========================================
# Problem 20
# ==========================================
add({
    "num": 20,
    "title": "Ductile-to-Brittle Transition Temperature (DBTT) and Fracture Appearance",
    "difficulty": "Easy",
    "category": "Impact Mechanics",
    "tags": ["DBTT", "Ductile-to-Brittle Transition", "Charpy Curve", "FATT"],
    "statement": r"""A standard series of Charpy V-notch impact tests conducted on a structural bridge steel across the temperature range $-80^\circ\text{C}$ to $+80^\circ\text{C}$ yields the characteristic sigmoidal DBTT curve.
<br><br>
1. Define the 3 distinct temperature regimes of the Charpy impact curve:
   (a) <strong>Upper Shelf Energy (USE)</strong> regime.<br>
   (b) <strong>Transition Temperature</strong> regime.<br>
   (c) <strong>Lower Shelf Energy (LSE)</strong> regime.<br>
2. Explain the two standard engineering definitions used to define the specific transition temperature:
   (a) <strong>Fracture Appearance Transition Temperature (FATT or 50% FATT)</strong>.<br>
   (b) <strong>Energy-based criteria</strong> (e.g., temperature corresponding to $27\text{ J}$ or $20\text{ ft}\cdot\text{lbf}$).<br>
3. If an offshore oil platform structure operates in the North Sea at water temperatures of $-2^\circ\text{C}$ to $+5^\circ\text{C}$, what is the maximum permissible DBTT specified for the structural steel plates?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The Three Regimes of the Charpy Curve</strong><br>
(a) <strong>Upper Shelf Energy (USE):</strong> At high temperatures, the metal is fully ductile. Dislocation slip occurs freely, absorbing massive plastic energy ($100\text{ to }250\text{ J}$). The fracture surface is $100\%$ dull, fibrous gray, exhibiting classic microvoid coalescence dimples under SEM.<br>
(b) <strong>Transition Regime:</strong> Intermediate temperature band where absorbed energy drops precipitously over a narrow temperature interval ($30^\circ\text{C}\text{--}50^\circ\text{C}$). Fracture surfaces display mixed ductile shear lips surrounding a brittle cleavage core.<br>
(c) <strong>Lower Shelf Energy (LSE):</strong> At low temperatures, the metal becomes completely brittle. Dislocation slip is suppressed by high lattice friction, and cracks propagate by cleavage along $\{100\}$ planes. Absorbed energy drops to a negligible value ($2\text{ to }10\text{ J}$). The fracture surface is $100\%$ bright, shiny, and faceted.
</div>
<div class="solution-step">
<strong>Step 2: Engineering definitions of DBTT</strong><br>
(a) <strong>50% FATT (Fracture Appearance Transition Temperature):</strong> The temperature at which the fracture surface consists of precisely $50\%$ ductile fibrous shear and $50\%$ brittle cleavage. It is determined visually or under an optical stereomicroscope by measuring the percentage area of cleavage facets.<br>
(b) <strong>Energy-based criterion (27 J / 20 ft-lb):</strong> Historically derived from investigations of welded WWII Liberty ship failures, which proved that brittle fracture does not occur if the Charpy absorbed energy is at least $27\text{ Joules}$ ($20\text{ ft}\cdot\text{lbf}$) at the minimum service temperature. Many structural codes define DBTT as $T_{27\text{J}}$.
</div>
<div class="solution-step">
<strong>Step 3: Specification for North Sea offshore platform</strong><br>
To guarantee complete safety against catastrophic brittle fracture, the minimum operating service temperature ($T_{\text{service, min}} = -2^\circ\text{C}$) must lie firmly within the <strong>Upper Shelf Energy regime</strong>!
Structural design codes (such as DNV, API, AWS) require the steel's DBTT ($T_{27\text{J}}$) to be at least $30^\circ\text{C}\text{ to }40^\circ\text{C}$ below the minimum service temperature.
Therefore, the steel must have:
$$\text{DBTT} \le -40^\circ\text{C} \quad (\text{tested and certified at } -40^\circ\text{C} \text{ with } K_V \ge 40\text{--}50\text{ J})$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Upper shelf: $100\%$ ductile fibrous ($>100\text{ J}$); Lower shelf: $100\%$ brittle cleavage ($<10\text{ J}$).<br>
Transition definitions: $50\%$ FATT (visual $50/50$ area) and $27\text{ J}$ absorbed energy criterion.<br>
For North Sea service ($-2^\circ\text{C}$), steel DBTT must be specified at $-40^\circ\text{C}$ or lower to ensure operation on the upper shelf.
</div>"""
})

# ==========================================
# Problem 21
# ==========================================
add({
    "num": 21,
    "title": "Crystal Structure Dependence of DBTT: BCC vs. FCC and HCP",
    "difficulty": "Easy",
    "category": "Impact Mechanics",
    "tags": ["DBTT", "Crystal Structure", "BCC vs FCC", "Peierls Stress"],
    "statement": r"""A profound difference exists in the low-temperature impact behavior of different crystal structures:
- Body-Centered Cubic (BCC) metals (ferritic steels, W, Mo, Cr) display a sharp, dramatic DBTT.
- Face-Centered Cubic (FCC) metals (aluminum, copper, nickel, austenitic stainless steel) display <strong>NO DBTT</strong>: their impact energy remains high and ductile even down to liquid helium temperature ($4\text{ K} = -269^\circ\text{C}$).
- Hexagonal Close-Packed (HCP) metals (Mg, Zn, Ti) display complex, moderate transition behavior.
<br><br>
1. Explain the fundamental dislocation physics responsible for the presence of a sharp DBTT in BCC metals and its complete absence in FCC metals.<br>
2. Why are cryogenic storage tanks for Liquefied Natural Gas (LNG at $-162^\circ\text{C}$) and liquid nitrogen ($-196^\circ\text{C}$) constructed exclusively from austenitic stainless steel (e.g., AISI 304L), $9\%\text{ Ni}$ steel, or aluminum alloys (Al 5083), and NEVER from standard structural carbon steel?<br>
3. What is the impact behavior of pure titanium (HCP) at cryogenic temperatures?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Dislocation physics of BCC vs. FCC</strong><br>
- <strong>BCC Metals:</strong> Screw dislocations in BCC crystals have a non-planar core spread symmetrically across three intersecting $\{110\}$ planes. Moving a screw dislocation requires constricting this non-planar core, which has an immense intrinsic Peierls-Nabarro friction barrier. At low temperatures, thermal vibrations are insufficient to assist constriction, causing the yield stress $\sigma_y(T)$ to skyrocket. When temperature drops below DBTT, the yield stress surpasses the cleavage fracture stress ($\sigma_y > \sigma_F$). The crystal cleaves before dislocations can move, resulting in catastrophic brittle fracture.<br>
- <strong>FCC Metals:</strong> Dislocation cores in FCC metals are strictly planar on close-packed $\{111\}$ planes. The intrinsic Peierls lattice friction is virtually zero ($\tau_{\text{PN}} \approx 10^{-5} G$). Dislocation slip requires negligible thermal activation, so yield strength increases only modestly as temperature drops. The yield stress never rises high enough to intersect the cleavage fracture stress ($\sigma_y \ll \sigma_F$ at all temperatures). Furthermore, FCC has 12 slip systems satisfying the Taylor criterion. Thus, FCC metals remain fully ductile down to absolute zero ($0\text{ K}$).
</div>
<div class="solution-step">
<strong>Step 2: Material selection for cryogenic LNG tanks ($-162^\circ\text{C}$)</strong><br>
At $-162^\circ\text{C}$, standard carbon and low-alloy steels are far below their DBTT (which is typically $-20^\circ\text{C}\text{ to }+10^\circ\text{C}$). A carbon steel tank would shatter like glass from the slightest pressure surge or vibration, causing catastrophic explosive LNG vaporization.
Engineers specify:
1. <strong>Austenitic Stainless Steel (AISI 304L / 316L):</strong> The FCC austenite phase is stabilized by nickel ($8\text{--}12\%$) and remains exceptionally tough ($K_V > 100\text{ J}$ at $-196^\circ\text{C}$).
2. <strong>Aluminum Alloys (Al 5083-O):</strong> Inherent FCC structure; toughness actually increases slightly at cryogenic temperatures.
3. <strong>$9\%\text{ Ni}$ Ferritic Steel:</strong> Special alloy where high nickel content and fine retained austenite film reduce the DBTT to below $-196^\circ\text{C}$.
</div>
<div class="solution-step">
<strong>Step 3: Titanium at cryogenic temperatures</strong><br>
High-purity $\alpha$-titanium (HCP) with low interstitial content (Extra-Low Interstitial ELI grade Ti-5Al-2.5Sn or Ti-6Al-4V ELI) maintains good cryogenic toughness because mechanical twinning easily activates along $\{10\bar{1}2\}$ planes, providing the required independent deformation modes along the $c$-axis when thermal energy is low.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
BCC metals exhibit sharp DBTT because non-planar screw dislocation cores create high Peierls barriers that skyrocket yield stress above cleavage stress at low $T$.<br>
FCC metals have planar cores and near-zero Peierls stress; $\sigma_y \ll \sigma_F$ down to $0\text{ K}$, completely eliminating DBTT.<br>
Cryogenic tanks (LNG $-162^\circ\text{C}$) use FCC alloys (304L stainless, Al 5083) to eliminate risk of brittle cleavage.
</div>"""
})

# ==========================================
# Problem 22
# ==========================================
add({
    "num": 22,
    "title": "Alloying Effects on Steel DBTT: Carbon vs. Manganese-to-Carbon Ratio",
    "difficulty": "Medium",
    "category": "Impact Mechanics",
    "tags": ["DBTT", "Alloying Elements", "Carbon Content", "Mn/C Ratio"],
    "statement": r"""The position of the Charpy impact curve and the Ductile-to-Brittle Transition Temperature (DBTT) of structural carbon steels are extraordinarily sensitive to chemical composition and microstructure.
<br><br>
1. Describe the effect of increasing <strong>carbon content</strong> (from $0.10\text{ wt}\%$ to $0.80\text{ wt}\%$) on:
   (a) The Ductile-to-Brittle Transition Temperature.<br>
   (b) The Upper Shelf Energy (USE).<br>
   Explain the microstructural reason (pearlite fraction and grain boundary carbides).<br>
2. How does increasing the <strong>Manganese-to-Carbon ratio ($\text{Mn/C}$)</strong> improve low-temperature impact properties?<br>
3. Which interstitial element is most notorious for causing "temper embrittlement" and catastrophic increases in DBTT in alloy steels, and what is its maximum allowable specification in modern clean steels?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Effect of carbon content</strong><br>
(a) <strong>DBTT shifts upward dramatically:</strong> Increasing carbon content from $0.10\%$ to $0.80\%$ raises the DBTT by over $100^\circ\text{C}$ (e.g., from $-50^\circ\text{C}$ for low-carbon steel up to $+80^\circ\text{C}\text{--}+100^\circ\text{C}$ for eutectoid steel). At room temperature ($20^\circ\text{C}$), high-carbon steel is completely on its brittle lower shelf!<br>
(b) <strong>Upper Shelf Energy drops severely:</strong> The upper shelf energy collapses from $> 150\text{ J}$ down to $< 20\text{ J}$.<br>
<em>Microstructural reason:</em> Increasing carbon increases the volume fraction of pearlite and cementite ($\text{Fe}_3\text{C}$). Hard, brittle cementite plates crack easily under small plastic strains, providing billions of sharp internal cleavage nuclei that propagate brittle microcracks across adjacent ferrite grains.
</div>
<div class="solution-step">
<strong>Step 2: Effect of Manganese-to-Carbon (Mn/C) ratio</strong><br>
Manganese is an essential alloying element in structural steels:
1. Manganese lowers the austenite-to-ferrite transformation temperature ($A_3$), refining the ferritic grain size ($d$). As proven by Petch, finer grains lower the DBTT ($\Delta T_{\text{DBTT}} \propto \ln d$).
2. Manganese ties up sulfur as benign, spherical manganese sulfide ($\text{MnS}$) inclusions, preventing the formation of low-melting iron sulfide ($\text{FeS}$) grain boundary films that cause hot shortness and embrittlement.
3. Keeping the $\text{Mn/C}$ ratio high ($\text{Mn/C} \ge 4\text{ to }6$, e.g., $0.15\%\text{ C}$ with $1.2\text{--}1.5\%\text{ Mn}$) achieves high yield strength while pushing the DBTT well below $-30^\circ\text{C}$.
</div>
<div class="solution-step">
<strong>Step 3: Detrimental tramp elements</strong><br>
<strong>Phosphorus (P)</strong> is by far the most dangerous tramp embrittling element in steels. Phosphorus segregates to prior austenite grain boundaries during slow cooling, drastically weakening grain boundary cohesive strength and shifting the DBTT upward by up to $150^\circ\text{C}$ (temper embrittlement).
In modern clean steels (e.g., nuclear and pressure vessel grades), phosphorus is strictly limited to:
$$\text{P} \le 0.008\text{ to }0.012\text{ wt}\% \quad (\text{often } < 50\text{ ppm})$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Increasing carbon raises DBTT and collapses Upper Shelf Energy due to brittle cementite crack nucleation.<br>
High Mn/C ratio ($\ge 4\text{--}6$) refines grain size and neutralizes sulfur, pushing DBTT to low sub-zero temperatures.<br>
Phosphorus is the most lethal tramp embrittler; modern clean steels restrict $\text{P} < 0.010\text{ wt}\%$.
</div>"""
})

# ==========================================
# Problem 23
# ==========================================
add({
    "num": 23,
    "title": "Neutron Radiation Embrittlement in Nuclear Reactor Pressure Vessels",
    "difficulty": "Hard",
    "category": "Nuclear Materials",
    "tags": ["Radiation Damage", "Neutron Embrittlement", "DBTT Shift", "RPV Steel"],
    "statement": r"""Nuclear Reactor Pressure Vessels (RPVs) fabricated from low-alloy ferritic steels (e.g., A533B or A508) are subjected to continuous fast neutron bombardment ($E > 1.0\text{ MeV}$) over their 40-to-60-year operational lifetimes.
Fast neutron collisions create cascade displacement spikes that generate high densities of point defect clusters and stimulate the precipitation of copper-rich nanoclusters ($\text{Cu-Mn-Ni-Si}$).
<br><br>
The resulting radiation-induced increase in yield strength $\Delta\sigma_y$ causes a corresponding upward shift in the transition temperature $\Delta T_{\text{DBTT}}$:
$$\Delta T_{\text{DBTT}} \approx C_{\text{rad}} \times \Delta\sigma_y$$
The US Nuclear Regulatory Commission (NRC Regulatory Guide 1.99) models the transition temperature shift as:
$$\Delta T_{\text{DBTT}} = [CF] \times f_{\text{fluence}}^{(0.28 - 0.10 \log_{10} f_{\text{fluence}})}$$
where $f_{\text{fluence}}$ is the fast neutron fluence in units of $10^{19}\text{ neutrons/cm}^2$, and chemistry factor $CF = 115^\circ\text{C}$ (for a weld containing $0.15\text{ wt}\%\text{ Cu}$ and $0.60\text{ wt}\%\text{ Ni}$).
<br><br>
1. Calculate the transition temperature shift $\Delta T_{\text{DBTT}}$ after 30 years of operation when the accumulated neutron fluence reaches $f_{\text{fluence}} = 2.50 \times 10^{19}\text{ n/cm}^2$ ($f = 2.50$).<br>
2. If the initial unirradiated transition temperature of the weld was $T_{\text{DBTT}, 0} = -25.0^\circ\text{C}$, calculate the new irradiated transition temperature $T_{\text{DBTT}, \text{rad}}$.<br>
3. What is <strong>Pressurized Thermal Shock (PTS)</strong>? Explain why a high irradiated DBTT poses an existential risk to a nuclear power plant during an emergency shutdown.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate $\Delta T_{\text{DBTT}}$ from NRC formula</strong><br>
Given: $CF = 115^\circ\text{C}$, $f = 2.50$:
$$\log_{10}(2.50) \approx 0.39794$$
$$\text{Exponent} = 0.28 - 0.10 \log_{10}(2.50) = 0.28 - 0.10(0.39794) = 0.28 - 0.039794 = 0.2402$$
Fluence factor:
$$f^{0.2402} = (2.50)^{0.2402} \approx 1.2465$$
Transition temperature shift:
$$\Delta T_{\text{DBTT}} = 115^\circ\text{C} \times 1.2465 \approx 143.35^\circ\text{C}$$
Fast neutron irradiation has shifted the DBTT upward by more than $143^\circ\text{C}$!
</div>
<div class="solution-step">
<strong>Step 2: Irradiated transition temperature</strong><br>
$$T_{\text{DBTT}, \text{rad}} = T_{\text{DBTT}, 0} + \Delta T_{\text{DBTT}} = -25.0^\circ\text{C} + 143.35^\circ\text{C} = +118.35^\circ\text{C}$$
The steel's transition temperature has climbed well above the boiling point of water ($+118^\circ\text{C}$)!
</div>
<div class="solution-step">
<strong>Step 3: Pressurized Thermal Shock (PTS) hazard</strong><br>
In a loss-of-coolant accident (LOCA) or emergency reactor trip, cold emergency core cooling water ($\sim 20^\circ\text{C}$) is injected into the hot reactor vessel under high operating pressure ($\sim 15.5\text{ MPa}$).
- The cold water causes severe thermal shock, creating intense tensile stresses on the vessel inner wall.
- Concurrently, the internal pressure imposes high hoop tensile stresses.
- The vessel wall cools rapidly to $50^\circ\text{C}\text{--}80^\circ\text{C}$.
Because the irradiated DBTT is $+118^\circ\text{C}$, the vessel wall is operating <strong>deep on its brittle lower shelf</strong>! Any tiny pre-existing under-clad crack can trigger catastrophic, explosive brittle cleavage fracture of the entire reactor pressure vessel, releasing nuclear core coolant. This makes radiation embrittlement monitoring via surveillance capsule testing the primary life-limiting factor for nuclear reactors.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\Delta T_{\text{DBTT}} = +143.4^\circ\text{C}$ shift.<br>
Irradiated DBTT: $T_{\text{DBTT}, \text{rad}} = +118.4^\circ\text{C}$ (well above room temperature).<br>
PTS risk: Cold emergency water injection under pressure combined with $T < \text{DBTT}$ can trigger catastrophic brittle vessel rupture.
</div>"""
})

# ==========================================
# Problem 24
# ==========================================
add({
    "num": 24,
    "title": "Historical Brittle Catastrophes: Liberty Ships and the Titanic",
    "difficulty": "Easy",
    "category": "Impact Mechanics",
    "tags": ["Liberty Ships", "Titanic", "Historical Failures", "Brittle Fracture"],
    "statement": r"""Two iconic historical maritime disasters revolutionized the field of fracture mechanics and materials engineering:
1. The sudden in-service fracture of WWII all-welded <strong>Liberty ships</strong> (out of 2,710 ships built, over 1,000 suffered serious structural cracks, and more than 20 snapped completely in two in calm North Atlantic seas).
2. The catastrophic sinking of the <strong>RMS Titanic</strong> in April 1912 after colliding with an iceberg.
<br><br>
1. Identify the 3 converging engineering factors that caused the catastrophic failure of WWII Liberty ships:
   (a) Structural continuity change (riveted vs welded hulls).<br>
   (b) Stress concentrations (geometric design of hatch corners).<br>
   (c) Metallurgical properties (steel DBTT vs North Atlantic water temperature).<br>
2. Metallurgical testing of hull steel plates recovered from the Titanic wreck site in 1996 revealed a Charpy impact energy of only $3\text{ to }4\text{ Joules}$ at $-2^\circ\text{C}$ (seawater temperature on the night of the sinking). Compare this steel to modern shipbuilding steel (ASTM A131).<br>
3. What two critical design changes were immediately implemented by naval architects to permanently cure brittle fractures in welded merchant ships?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The three converging factors in Liberty ship failures</strong><br>
(a) <strong>Continuous All-Welded Construction:</strong> Liberty ships were the first mass-produced ships built entirely by welding instead of traditional riveting. In a riveted hull, individual overlapping plates act as independent structural units: a crack that initiates in one plate is safely arrested when it reaches the open plate seam or rivet hole. In an all-welded hull, the entire ship is a single, continuous monolithic envelope. A brittle cleavage crack initiating at a single defect can travel unimpeded through welds and plates around the entire hull in less than a second, snapping the ship in two.<br>
(b) <strong>Sharp Square Hatch Corners:</strong> The cargo hatch openings on the main deck were designed with sharp $90^\circ$ square corners. As Inglis showed, sharp corners act as severe geometric stress concentrators ($K_t > 5\text{--}8$), amplifying wave bending stresses and serving as ideal crack initiation sites.<br>
(c) <strong>High DBTT Steel:</strong> The low-carbon semikilled steel used during the wartime emergency had high carbon and sulfur, low manganese ($\text{Mn/C} < 2$), and coarse ferritic grain size. Its Charpy transition temperature was around $+10^\circ\text{C}\text{ to }+25^\circ\text{C}$! When sailing in North Atlantic winter waters at $+4^\circ\text{C}$, the steel was operating completely on its brittle lower shelf.
</div>
<div class="solution-step">
<strong>Step 2: Titanic hull steel analysis</strong><br>
Testing of recovered Titanic hull steel confirmed:
- The steel had a DBTT around $+30^\circ\text{C}$ to $+40^\circ\text{C}$.
- At $-2^\circ\text{C}$ (iceberg water temperature), the steel was exceptionally brittle, absorbing only $3\text{--}4\text{ J}$ (cleavage fracture without plastic deformation).
- The steel contained high sulfur ($0.069\%$) and low manganese ($\text{Mn/S} \approx 6.8$), forming stringers of iron sulfide ($\text{FeS}$) inclusions.
- Furthermore, the wrought iron hull rivets contained high concentrations of brittle slag ($\approx 9\%$), causing rivet heads to shear off upon iceberg impact, unzipping hull seams over five watertight compartments.<br>
In contrast, modern shipbuilding steel (ASTM A131 Grade DH36) has low carbon ($<0.18\%$), high manganese ($>1.2\%$), is fully aluminum-killed and fine-grained, absorbing $> 50\text{ J}$ at $-20^\circ\text{C}$.
</div>
<div class="solution-step">
<strong>Step 3: Permanent engineering remedies</strong><br>
1. <strong>Rounded Hatch Corners:</strong> All rectangular deck cutouts were mandated to have smooth, large-radius rounded corners and welded doubler reinforcement plates, slashing the stress concentration factor from $K_t > 5$ down to $K_t < 1.5$.
2. <strong>Riveted Crack Arrestor Straps:</strong> Longitudinal riveted steel straps were installed along the deck and bilge keel. Because a running brittle crack cannot cross a mechanical riveted joint, any crack initiating on deck was safely arrested at the strap seam.
3. <strong>Charpy Impact Toughness Standards:</strong> Mandatory specifications were established requiring steels to demonstrate minimum absorbed energy ($K_V \ge 27\text{ J}$) at the lowest service temperature.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Liberty ships failed from: (1) Monolithic welded continuity (no crack arrest), (2) Sharp square hatch corners ($K_t > 5$), and (3) Steel operating below DBTT ($T_{\text{water}} < \text{DBTT}$).<br>
Titanic steel had $\text{DBTT} > +30^\circ\text{C}$; absorbed only $3\text{--}4\text{ J}$ at $-2^\circ\text{C}$, shattering upon iceberg impact.<br>
Remedies: Rounded corners, riveted crack-arrester straps, and mandatory Charpy impact quality control standards ($27\text{ J}$ rule).
</div>"""
})

# ==========================================
# Problem 25
# ==========================================
add({
    "num": 25,
    "title": "Fatigue Stress Terminology: Mean, Amplitude, Range, and R-Ratio",
    "difficulty": "Easy",
    "category": "Fatigue Failure",
    "tags": ["Fatigue Terminology", "Stress Amplitude", "Mean Stress", "Stress Ratio R"],
    "statement": r"""Over $90\%$ of all mechanical component failures in machinery, aircraft, vehicles, and rotating shafts occur by cyclic <strong>fatigue</strong> under stresses well below the static tensile yield strength.
A sinusoidal fatigue stress cycle fluctuates between a maximum tensile stress $\sigma_{\text{max}} = +420\text{ MPa}$ and a minimum stress $\sigma_{\text{min}} = -140\text{ MPa}$ (compression).
<br><br>
1. State the standard definitions and calculate the numerical values for:
   (a) Stress range $\Delta\sigma$.<br>
   (b) Stress amplitude $\sigma_a$.<br>
   (c) Mean stress $\sigma_m$.<br>
   (d) Stress ratio $R = \sigma_{\text{min}} / \sigma_{\text{max}}$.<br>
   (e) Amplitude ratio $A = \sigma_a / \sigma_m$.<br>
2. What are the specific values of $R$ and $A$ for:
   (a) <strong>Fully reversed cycling</strong> (pure symmetric tension-compression: $\sigma_{\text{max}} = -\sigma_{\text{min}}$).<br>
   (b) <strong>Pulsating zero-to-tension cycling</strong> ($\sigma_{\text{min}} = 0$).<br>
3. Which loading condition is more severe in promoting fatigue crack growth: a tensile mean stress ($\sigma_m > 0$) or a compressive mean stress ($\sigma_m < 0$)? Explain why.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate fatigue parameters</strong><br>
Given: $\sigma_{\text{max}} = +420\text{ MPa}$, $\sigma_{\text{min}} = -140\text{ MPa}$:
(a) <em>Stress range $\Delta\sigma$:</em>
$$\Delta\sigma = \sigma_{\text{max}} - \sigma_{\text{min}} = 420 - (-140) = 420 + 140 = 560.0\text{ MPa}$$
(b) <em>Stress amplitude $\sigma_a$:</em>
$$\sigma_a = \frac{\Delta\sigma}{2} = \frac{\sigma_{\text{max}} - \sigma_{\text{min}}}{2} = \frac{560.0}{2} = 280.0\text{ MPa}$$
(c) <em>Mean stress $\sigma_m$:</em>
$$\sigma_m = \frac{\sigma_{\text{max}} + \sigma_{\text{min}}}{2} = \frac{420 + (-140)}{2} = \frac{280}{2} = 140.0\text{ MPa}$$
(d) <em>Stress ratio $R$:</em>
$$R = \frac{\sigma_{\text{min}}}{\sigma_{\text{max}}} = \frac{-140}{420} = -\frac{1}{3} \approx -0.333$$
(e) <em>Amplitude ratio $A$:</em>
$$A = \frac{\sigma_a}{\sigma_m} = \frac{280.0}{140.0} = 2.000$$
Note identity check: $A = \frac{1 - R}{1 + R} = \frac{1 - (-1/3)}{1 + (-1/3)} = \frac{4/3}{2/3} = 2.00$.
</div>
<div class="solution-step">
<strong>Step 2: Special standard cyclic cases</strong><br>
(a) <em>Fully reversed cycling ($\sigma_{\text{max}} = -\sigma_{\text{min}} = \sigma_a$):</em>
$$\sigma_m = \frac{\sigma_a + (-\sigma_a)}{2} = 0$$
$$R = \frac{-\sigma_a}{\sigma_a} = \mathbf{-1.00}, \quad A = \frac{\sigma_a}{0} = \boldsymbol{\infty}$$
(b) <em>Pulsating zero-to-tension cycling ($\sigma_{\text{min}} = 0, \sigma_{\text{max}} = 2\sigma_a$):</em>
$$\sigma_m = \sigma_a$$
$$R = \frac{0}{\sigma_{\text{max}}} = \mathbf{0.00}, \quad A = \frac{\sigma_a}{\sigma_a} = \mathbf{1.00}$$
</div>
<div class="solution-step">
<strong>Step 3: Effect of tensile vs. compressive mean stress</strong><br>
A <strong>tensile mean stress ($\sigma_m > 0$)</strong> is drastically more damaging and severely reduces fatigue life. Tensile mean stress pulls microcrack faces apart (counteracting crack closure), elevates peak stress intensity ($K_{\text{max}}$), and accelerates persistent slip band intrusion/extrusion development.<br>
Conversely, a <strong>compressive mean stress ($\sigma_m < 0$)</strong> is highly beneficial: it squeezes crack faces shut during a significant portion of the cycle (crack closure), preventing shear slip decohesion and greatly extending fatigue endurance limit.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\Delta\sigma = 560.0\text{ MPa}$, $\sigma_a = 280.0\text{ MPa}$, $\sigma_m = 140.0\text{ MPa}$<br>
Stress ratio $R = -0.333$, Amplitude ratio $A = 2.00$<br>
Fully reversed: $R = -1.0, A = \infty$; Zero-to-tension: $R = 0, A = 1.0$<br>
Tensile mean stress accelerates fatigue; compressive mean stress enforces crack closure and extends life.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 8 Part 1: All P1-P25 added. Current total: {len(P)}")
