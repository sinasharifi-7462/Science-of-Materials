# generator/make_ch7_part2.py
import sys
import os
import re

import make_ch7_part1

P = list(make_ch7_part1.P)

def add(p_dict):
    if "num" in p_dict and "number" not in p_dict:
        p_dict["number"] = p_dict["num"]
    if "category_slug" not in p_dict:
        p_dict["category_slug"] = re.sub(r'[^a-z0-9]+', '-', p_dict.get("category", "general").lower()).strip('-')
    P.append(p_dict)

# ==========================================
# Problem 26
# ==========================================
add({
    "num": 26,
    "title": "Static and Dynamic Strain Aging: Portevin-Le Chatelier Effect",
    "difficulty": "Medium",
    "category": "Strain Aging",
    "tags": ["Strain Aging", "Portevin-Le Chatelier", "Serrated Flow", "Blue Brittleness"],
    "statement": r"""When a mild steel specimen is pulled past its yield point to a plastic strain of $\varepsilon_p = 4\%$, unloaded, and immediately retested in tension, yielding resumes smoothly without any yield point.
However, if the pre-strained specimen is aged at room temperature for several days (or at $100^\circ\text{C}\text{ to }150^\circ\text{C}$ for 30 minutes) before retesting:
- The yield drop reappears with an even higher yield point ($\sigma_{\text{UYP}}' > \sigma_{\text{unloaded}}$).
- The tensile strength increases, while ductility (%EL) drops.
This is <strong>static strain aging</strong>.
<br><br>
1. Explain the atomic diffusion mechanism driving static strain aging.<br>
2. In tensile tests conducted at intermediate temperatures ($150^\circ\text{C}\text{ to }300^\circ\text{C}$) or specific strain rates, the stress-strain curve exhibits serrated, jerky flow with repeating load drops. What is this phenomenon called (Portevin-Le Chatelier effect)?<br>
3. Explain the microscopic competition between dislocation glide velocity $v_d$ and solute diffusion velocity $v_s$ that creates PLC serrations.<br>
4. Why is the temperature regime around $200^\circ\text{C}\text{--}300^\circ\text{C}$ in steels known as the "blue brittleness" range?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Mechanism of static strain aging</strong><br>
During the initial pre-straining, dislocations break free from their Cottrell atmospheres and multiply.
When the specimen is unloaded and aged, the unlocked mobile dislocations remain arrested in the lattice.
Carbon and nitrogen interstitial solute atoms possess significant diffusion rates even near room temperature (activation energy for interstitial migration $\sim 0.8\text{ eV}$). Driven by the elastic interaction gradient ($U \propto 1/r$), carbon and nitrogen atoms diffuse toward the freshly created mobile dislocations, reforming dense Cottrell atmospheres and pinning them firmly again. Subsequent reloading requires an elevated stress to re-unlock these pinned dislocations, causing the return of the yield drop at a higher strength.
</div>
<div class="solution-step">
<strong>Step 2: Dynamic Strain Aging (Portevin-Le Chatelier Effect)</strong><br>
When strain aging occurs <em>simultaneously during ongoing plastic deformation</em>, it is known as <strong>Dynamic Strain Aging (DSA)</strong> or the <strong>Portevin-Le Chatelier (PLC) effect</strong>. It manifests as distinctive jerky serrations in the stress-strain curve.
</div>
<div class="solution-step">
<strong>Step 3: Dislocation velocity vs. Solute diffusion velocity</strong><br>
DSA arises from a dynamic synchronization between gliding dislocations and diffusing solute atoms:
1. When a dislocation is momentarily arrested at a forest obstacle (waiting time $t_w$), fast-diffusing carbon atoms catch up and form a solute cloud around it.
2. The applied stress rises until it reaches the breakaway threshold, abruptly tearing the dislocation free.
3. The dislocation surges forward at high velocity $v_d \gg v_s$ (causing an instantaneous drop in load).
4. Upon striking the next obstacle, the dislocation arrests again, and solute atoms catch up once more.
This cyclic pinning and breakaway leads to a negative strain rate sensitivity ($d\sigma/d\dot{\varepsilon} < 0$), triggering plastic instability and propagating deformation bands.
</div>
<div class="solution-step">
<strong>Step 4: Blue brittleness</strong><br>
In steels tested between $200^\circ\text{C}$ and $300^\circ\text{C}$ (temperatures that tint steel a characteristic iridescent blue oxide color), dynamic strain aging is at its maximum intensity. The continuous pinning of dislocations by carbon/nitrogen minimizes mobile dislocation activity, raising hardness and tensile strength while causing a precipitous drop in ductility and impact energy. This embrittlement at elevated working temperatures is called <strong>blue brittleness</strong>.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Static aging: Carbon re-diffuses to unlocked dislocations during holding, restoring the yield drop.<br>
PLC effect (Dynamic Strain Aging): Solute diffusion velocity matches dislocation waiting time, causing cyclic pinning/unpinning serrations.<br>
Blue brittleness ($200\text{--}300^\circ\text{C}$): Intense dynamic strain aging causes high strength but severe embrittlement.
</div>"""
})

# ==========================================
# Problem 27
# ==========================================
add({
    "num": 27,
    "title": "Suzuki Hardening: Chemical Segregation to Stacking Faults",
    "difficulty": "Medium",
    "category": "Solid Solution Strengthening",
    "tags": ["Suzuki Hardening", "Stacking Fault", "Chemical Strengthening", "Low-SFE"],
    "statement": r"""In FCC alloys with low stacking fault energy (such as $\alpha$-brass Cu-30Zn, bronze Cu-Sn, or austenitic stainless steel), full dislocations split into widely separated Shockley partials bounding a wide strip of stacking fault ribbon.
The crystal structure inside the stacking fault ribbon is two atomic layers of Hexagonal Close-Packed (HCP) packing ($\dots ABCABABCA \dots$).
<br><br>
1. Define <strong>Suzuki segregation</strong> and explain how the difference in chemical free energy between FCC and HCP phases causes solute redistribution.<br>
2. A copper alloy containing zinc has a free energy difference per unit area $\Delta G_{\text{chem}} = \gamma_{\text{SF}}(c) - \gamma_{\text{SF}}(c_0) = 8.0\text{ mJ/m}^2$ when zinc segregates to the fault ribbon. If the equilibrium ribbon width is $d = 4.5\text{ nm}$ and Burgers vector $b = 0.256\text{ nm}$, calculate the critical shear stress $\Delta\tau_{\text{Suzuki}}$ required to pull the trailing partial away from the enriched stacking fault.<br>
3. Why is Suzuki hardening completely absent in pure metals and negligible in high-SFE metals like aluminum?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Definition and thermodynamic origin</strong><br>
An intrinsic stacking fault in an FCC crystal has local atomic stacking $\dots ABC\mathbf{AB}ABC\dots$, creating a thin two-layer slab of HCP crystal structure within the FCC matrix.<br>
If a solute element has higher thermodynamic solubility or lower chemical free energy in the HCP phase than in the FCC phase (e.g., Zn or Sn in Cu), solute atoms preferentially diffuse into the stacking fault ribbon to minimize total free energy. This chemical segregation to the fault plane is called <strong>Suzuki segregation</strong> (or chemical interaction hardening).
</div>
<div class="solution-step">
<strong>Step 2: Calculate Suzuki shear stress $\Delta\tau_{\text{Suzuki}}$</strong><br>
When an applied stress attempts to move the extended dislocation, the leading partial must advance onto fresh FCC lattice, while the trailing partial must destroy the solute-enriched HCP fault. The chemical concentration difference creates a retarding force per unit length:
$$F_{\text{chem}} = \Delta \gamma = 8.0\text{ mJ/m}^2 = 8.0 \times 10^{-3}\text{ N/m}$$
The shear stress required to force dislocation glide against this chemical pinning force is:
$$\Delta\tau_{\text{Suzuki}} = \frac{F_{\text{chem}}}{b}$$
Given $b = 0.256 \times 10^{-9}\text{ m}$:
$$\Delta\tau_{\text{Suzuki}} = \frac{8.0 \times 10^{-3}\text{ N/m}}{0.256 \times 10^{-9}\text{ m}} = 3.125 \times 10^7\text{ Pa} \approx 31.25\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Why Suzuki hardening is absent in pure metals and Al</strong><br>
1. <em>Pure metals:</em> In pure copper or pure silver, there are no solute atoms to segregate; hence, $\Delta \gamma = 0$ and Suzuki hardening cannot exist.<br>
2. <em>High-SFE metals (Aluminum):</em> In aluminum, the stacking fault energy is extremely high ($\gamma_{\text{SF}} \approx 160\text{ mJ/m}^2$), which compresses the Shockley partial separation distance to less than $1\text{ nm}$ ($d \approx 1\text{--}2$ atomic spacings). With virtually no stacking fault area to accommodate solute segregation, Suzuki chemical hardening is completely negligible.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Suzuki effect: Solute segregates to the 2-layer HCP stacking fault ribbon to lower chemical free energy.<br>
Pinning shear stress: $\Delta\tau_{\text{Suzuki}} = \Delta \gamma / b = 31.3\text{ MPa}$<br>
Absent in pure metals (no solute) and negligible in Al (extremely narrow stacking fault ribbon).
</div>"""
})

# ==========================================
# Problem 28
# ==========================================
add({
    "num": 28,
    "title": "Cold Working and Percent Cold Work (%CW) Calculation",
    "difficulty": "Easy",
    "category": "Strain Hardening",
    "tags": ["Cold Work", "%CW", "Rolling", "Wire Drawing"],
    "statement": r"""Strain hardening (work hardening) is quantified by the percentage of cold work (%CW), defined by the fractional reduction in cross-sectional area:
$$\%CW = \left(\frac{A_0 - A_d}{A_0}\right) \times 100\%$$
where $A_0$ is the original cross-sectional area and $A_d$ is the deformed cross-sectional area.
<br><br>
1. A flat strip of brass with initial width $w_0 = 100.0\text{ mm}$ and initial thickness $t_0 = 6.0\text{ mm}$ is cold rolled in several passes to a final thickness $t_f = 2.4\text{ mm}$. Assuming negligible lateral spreading of the strip ($w_f \approx w_0$), calculate the %CW.<br>
2. A cylindrical rod of pure copper with initial diameter $d_0 = 12.0\text{ mm}$ is drawn through a series of conical dies to a final wire diameter $d_f = 4.8\text{ mm}$. Calculate the %CW.<br>
3. Express the true plastic strain $\varepsilon_{\text{true}} = \ln(A_0 / A_d)$ as a function of %CW, and calculate the true strain for both operations.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate %CW for flat sheet rolling</strong><br>
Since width is constant ($w_f = w_0$):
$$A_0 = w_0 t_0, \quad A_d = w_0 t_f$$
$$\%CW_{\text{rolling}} = \left(\frac{w_0 t_0 - w_0 t_f}{w_0 t_0}\right) \times 100\% = \left(\frac{t_0 - t_f}{t_0}\right) \times 100\%$$
$$\%CW_{\text{rolling}} = \left(\frac{6.0 - 2.4}{6.0}\right) \times 100\% = \left(\frac{3.6}{6.0}\right) \times 100\% = 60.0\%$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate %CW for cylindrical wire drawing</strong><br>
For circular cross-sections ($A = \frac{\pi}{4} d^2$):
$$\%CW_{\text{wire}} = \left(\frac{\frac{\pi}{4}d_0^2 - \frac{\pi}{4}d_f^2}{\frac{\pi}{4}d_0^2}\right) \times 100\% = \left(1 - \frac{d_f^2}{d_0^2}\right) \times 100\%$$
$$\frac{d_f^2}{d_0^2} = \left(\frac{4.8}{12.0}\right)^2 = (0.40)^2 = 0.160$$
$$\%CW_{\text{wire}} = (1 - 0.160) \times 100\% = 84.0\%$$
</div>
<div class="solution-step">
<strong>Step 3: Relationship between true strain and %CW</strong><br>
$$\frac{A_0 - A_d}{A_0} = \frac{\%CW}{100} \implies 1 - \frac{A_d}{A_0} = \frac{\%CW}{100} \implies \frac{A_0}{A_d} = \frac{1}{1 - (\%CW / 100)}$$
$$\varepsilon_{\text{true}} = \ln\left(\frac{A_0}{A_d}\right) = -\ln\left(1 - \frac{\%CW}{100}\right)$$
- <em>For rolling (%CW = 60.0%):</em>
$$\varepsilon_{\text{true}} = -\ln(1 - 0.60) = -\ln(0.40) \approx 0.9163$$
- <em>For wire drawing (%CW = 84.0%):</em>
$$\varepsilon_{\text{true}} = -\ln(1 - 0.84) = -\ln(0.16) \approx 1.8326$$
Notice that doubling the true strain from $0.92$ to $1.83$ corresponds to increasing %CW from $60\%$ to $84\%$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Sheet rolling: $\%CW = 60.0\%$, true strain $\varepsilon = 0.916$<br>
Wire drawing: $\%CW = 84.0\%$, true strain $\varepsilon = 1.833$<br>
Formula: $\varepsilon_{\text{true}} = -\ln(1 - \%CW/100)$
</div>"""
})

# ==========================================
# Problem 29
# ==========================================
add({
    "num": 29,
    "title": "Dislocation Multiplication: Frank-Read Source Mechanism",
    "difficulty": "Hard",
    "category": "Dislocation Mechanics",
    "tags": ["Frank-Read Source", "Dislocation Multiplication", "Bowing Stress"],
    "statement": r"""A Frank-Read source consists of a segment of dislocation line of length $L$ pinned at both ends by precipitates, solute clusters, or sessile nodes.
Under an applied shear stress $\tau$, the dislocation bows out into a circular arc with radius of curvature $R$:
$$\tau = \frac{G b}{2 R}$$
The critical condition occurs when the segment bows into a semicircle of radius $R_{\text{crit}} = L / 2$.
<br><br>
1. Derive the formula for the critical activation shear stress $\tau_{\text{FR}}$ of a Frank-Read source.<br>
2. For an iron crystal ($G = 80\text{ GPa}$, $b = 0.248\text{ nm}$), calculate the operating stress $\tau_{\text{FR}}$ for a pinning length $L = 0.50\text{ }\mu\text{m}$.<br>
3. Describe the 4 sequential steps in the emission cycle of a Frank-Read source that allows it to generate hundreds of concentric dislocation loops without consuming itself.<br>
4. Calculate the back stress $\tau_{\text{back}}$ exerted on the source by a concentric ring of 20 emitted loops piled up at distance $D = 10\text{ }\mu\text{m}$, and explain why Frank-Read sources eventually shut down.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Derivation of Frank-Read activation stress</strong><br>
A dislocation has line tension $T \approx \frac{1}{2} G b^2$.
Balancing the Peach-Koehler forward force per unit length $f = \tau b$ with the restoring force from line tension curvature $T/R$:
$$\tau b = \frac{T}{R} \approx \frac{G b^2}{2 R} \implies \tau = \frac{G b}{2 R}$$
As the applied stress increases, $R$ decreases. The minimum possible radius of curvature occurs when the dislocation bows into a semicircle with diameter equal to the pinned length $L$:
$$R_{\text{min}} = \frac{L}{2}$$
Beyond this semicircular configuration, further expansion causes $R$ to increase, allowing spontaneous, unstable growth. Thus:
$$\tau_{\text{FR}} = \frac{G b}{2 (L/2)} = \frac{G b}{L} \quad (\text{or with rigorous line tension: } \tau_{\text{FR}} \approx \frac{2Gb}{L})$$
Using $\tau_{\text{FR}} = \frac{G b}{L}$:
</div>
<div class="solution-step">
<strong>Step 2: Calculate $\tau_{\text{FR}}$ for iron</strong><br>
Given: $G = 80 \times 10^9\text{ Pa}$, $b = 0.248 \times 10^{-9}\text{ m}$, $L = 0.50 \times 10^{-6}\text{ m}$:
$$\tau_{\text{FR}} = \frac{(80 \times 10^9) \times (0.248 \times 10^{-9})}{0.50 \times 10^{-6}} = \frac{19.84}{0.50 \times 10^{-6}} = 3.968 \times 10^7\text{ Pa} \approx 39.68\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Frank-Read source cycle sequence</strong><br>
1. <em>Initial bowing:</em> The straight segment pinned at points A and B bows out into a circular arc under applied shear stress $\tau$.
2. <em>Semicircular instability:</em> When stress reaches $\tau_{\text{FR}}$, the segment achieves the semicircular shape ($R = L/2$) and begins expanding unstably around the pinning points.
3. <em>Kidney-shaped wrap-around:</em> The two sides of the loop sweep backwards and curve towards each other behind the pinning points.
4. <em>Annihilation and pinch-off:</em> Where the two advancing segments meet, they have opposite Burgers vector orientations ($\mathbf{b}$ and $-\mathbf{b}$). They attract and annihilate, pinching off a complete, closed expanding dislocation loop while regenerating the original straight segment A-B, ready to repeat the cycle.
</div>
<div class="solution-step">
<strong>Step 4: Source shutdown by back stress</strong><br>
Each expanding dislocation loop moves out until it is arrested by a grain boundary or hard precipitate. The emitted loops form a coaxial pile-up that exerts an elastic repulsive <strong>back stress</strong> ($\tau_{\text{back}}$) opposing the applied stress:
$$\tau_{\text{net}} = \tau_{\text{applied}} - \tau_{\text{back}}$$
Once a sufficient number of loops accumulate (typically $n \sim 20\text{--}50$), $\tau_{\text{back}}$ increases until $\tau_{\text{net}} < \tau_{\text{FR}}$. At this point, the source can no longer reach the semicircular configuration and shuts down permanently unless the applied stress is raised or dislocations cross-slip away.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Critical activation stress: $\tau_{\text{FR}} = \frac{Gb}{L} = 39.7\text{ MPa}$<br>
Mechanism: Bowing $\to$ semicircular instability $\to$ wrap-around $\to$ pinch-off $\to$ loop emission.<br>
Accumulation of emitted loops generates elastic back stress that shuts down the source.
</div>"""
})

# ==========================================
# Problem 30
# ==========================================
add({
    "num": 30,
    "title": "Forest Dislocation Intersections: Jogs and Kinks",
    "difficulty": "Hard",
    "category": "Dislocation Mechanics",
    "tags": ["Forest Dislocation", "Jog", "Kink", "Vacancy Generation"],
    "statement": r"""When a primary mobile dislocation glides across a crystal, it must cut through a forest of stationary dislocations intersecting its slip plane.
Cutting creates atomic steps in the dislocation lines:
- A <strong>kink</strong> is a step that lies within the original slip plane.
- A <strong>jog</strong> is a step that extends out of the original slip plane into an adjacent parallel plane.
<br><br>
1. Distinguish between kinks and jogs regarding their ability to glide: which one glides conservatively with no activation energy, and which one is restricted?<br>
2. Consider a screw dislocation with Burgers vector $\mathbf{b} = [001]$ gliding on the $(010)$ plane that is cut by an edge forest dislocation with Burgers vector $\mathbf{b}_f = [100]$. Show that the resulting jog on the screw dislocation has edge character.<br>
3. To move forward with the screw dislocation, this jog must climb non-conservatively. Calculate the mechanical work $W$ required to create a vacancy of formation energy $E_v^f = 1.0\text{ eV}$ over an atomic jump distance $b = 0.25\text{ nm}$.<br>
4. Estimate the threshold shear stress $\tau_{\text{jog}}$ needed to drag a non-conservative jog at $0\text{ K}$ without thermal assistance.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Kink vs. Jog mobility</strong><br>
- <strong>Kink:</strong> The step lies entirely within the primary slip plane ($\mathbf{n} \cdot \mathbf{b} = 0$). It can glide conservatively along the dislocation line with virtually zero lattice friction, requiring no thermal activation.
- <strong>Jog:</strong> The step has a segment length equal to the cutting dislocation's Burgers vector ($b_f$) and points out of the slip plane. For an edge dislocation, the jog can glide conservatively along the Burgers vector direction. However, for a <strong>screw dislocation</strong>, the jog has edge character whose slip plane is orthogonal to the primary slip direction; hence, the screw dislocation cannot move without forcing the jog to <strong>climb non-conservatively</strong>, requiring creation of a trail of vacancies or interstitials.
</div>
<div class="solution-step">
<strong>Step 2: Vector analysis of jog on screw dislocation</strong><br>
Primary screw dislocation: line $\mathbf{u}_1 = [001]$, $\mathbf{b}_1 = [001]$ (parallel, so screw).
Cutting forest dislocation: $\mathbf{b}_f = [100]$.
Upon cutting, the primary dislocation acquires a jog segment vector equal to $\mathbf{b}_f$:
$$\mathbf{j} = \mathbf{b}_f = [100]$$
The jog segment has line direction $\mathbf{u}_{\text{jog}} = [100]$ and Burgers vector $\mathbf{b}_1 = [001]$.
Because $\mathbf{u}_{\text{jog}} \cdot \mathbf{b}_1 = [100] \cdot [001] = 0$, the jog segment is <strong>pure edge character</strong>!
Its glide plane is normal to $\mathbf{u}_{\text{jog}} \times \mathbf{b}_1 = [100] \times [001] = [0, -1, 0] = (010)$.
However, forward motion of the screw dislocation requires the jog to move along $[001]$, perpendicular to its glide plane. Thus, it can only move by climb!
</div>
<div class="solution-step">
<strong>Step 3: Energy required to create a vacancy</strong><br>
Moving forward by distance $b$ creates one point defect (a vacancy).
The energy penalty equals the vacancy formation energy:
$$\Delta E = E_v^f = 1.0\text{ eV} = 1.0 \times 1.602 \times 10^{-19}\text{ J} = 1.602 \times 10^{-19}\text{ J}$$
</div>
<div class="solution-step">
<strong>Step 4: Threshold shear stress to drag the jog</strong><br>
If the spacing between jogs along the dislocation line is $l_{\text{jog}} \approx 100\,b$, the mechanical work done by the applied stress $\tau$ over jump distance $b$ on the segment of length $l_{\text{jog}}$ is:
$$W_{\text{mech}} = \tau b \times l_{\text{jog}} b = \tau b^2 l_{\text{jog}}$$
Equating mechanical work to vacancy formation energy:
$$\tau_{\text{jog}} b^2 l_{\text{jog}} = E_v^f \implies \tau_{\text{jog}} = \frac{E_v^f}{b^2 l_{\text{jog}}}$$
For $b = 0.25 \times 10^{-9}\text{ m}$ and $l_{\text{jog}} = 100\,b = 25 \times 10^{-9}\text{ m}$:
$$\tau_{\text{jog}} = \frac{1.602 \times 10^{-19}\text{ J}}{(0.25 \times 10^{-9}\text{ m})^2 \times (25 \times 10^{-9}\text{ m})} = \frac{1.602 \times 10^{-19}}{1.5625 \times 10^{-27}} \approx 1.025 \times 10^8\text{ Pa} \approx 102.5\text{ MPa}$$
This immense friction force required to drag non-conservative jogs is one of the most powerful physical contributions to work hardening in metals.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Kinks glide conservatively with zero activation energy; jogs on screw dislocations must climb non-conservatively.<br>
A cutting forest creates an edge jog that leaves a trail of point defects (vacancies) as it advances.<br>
Athermal drag stress required: $\tau_{\text{jog}} \approx 102.5\text{ MPa}$.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 7 Part 2: P26-P30 added. Current total: {len(P)}")

# ==========================================
# Problem 31
# ==========================================
add({
    "num": 31,
    "title": "Double Cross-Slip Multiplication: The Koehler Mechanism",
    "difficulty": "Medium",
    "category": "Dislocation Mechanics",
    "tags": ["Double Cross-Slip", "Koehler Mechanism", "Dislocation Multiplication", "Screw Dislocation"],
    "statement": r"""In crystals with high stacking fault energy, a gliding screw dislocation can bypass an obstacle by cross-slipping onto an intersecting cross-slip plane.
In the <strong>Koehler double cross-slip mechanism</strong>, the screw segment glides on the cross-slip plane for a short distance $h$ before cross-slipping back onto a new plane parallel to the primary slip plane.
<br><br>
1. Draw a schematic sequence or describe step-by-step how double cross-slip creates two new dislocation sources.<br>
2. Why is double cross-slip much more effective at spreading plastic deformation throughout the entire volume of a crystal than a fixed Frank-Read source?<br>
3. The minimum separation distance $h_{\text{crit}}$ between the parallel primary planes required for the two newly formed edge segments to pass each other without mutually trapping is:
$$h_{\text{crit}} = \frac{G b}{8\pi (1-\nu) \tau}$$
For an aluminum alloy ($G = 26\text{ GPa}$, $b = 0.286\text{ nm}$, $\nu = 0.34$), calculate $h_{\text{crit}}$ under an applied shear stress $\tau = 50\text{ MPa}$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The 4-step Koehler mechanism sequence</strong><br>
1. A screw dislocation gliding on the primary slip plane $(111)$ encounters an impenetrable precipitate or forest obstacle.
2. The screw dislocation cross-slips onto an intersecting cross-slip plane $(1\bar{1}1)$ (since a screw dislocation has its Burgers vector parallel to its line, it can glide on any plane containing $\mathbf{b}$).
3. After traveling a distance $h$ on the cross-slip plane, the screw segment cross-slips a second time back onto a plane parallel to the original primary slip plane.
4. The two edge segments connecting the primary and parallel planes cannot glide on the primary plane; they act as rigid pinning points! The segment on the new plane now bows out under the applied stress and operates as a brand-new Frank-Read source.
</div>
<div class="solution-step">
<strong>Step 2: Volume dispersion of deformation</strong><br>
A conventional Frank-Read source is pinned at fixed metallurgical obstacles and emits loops exclusively in a single atomic plane. In contrast, double cross-slip allows dislocations to multiply and simultaneously hop across hundreds of parallel planes, nucleating thousands of secondary sources throughout the 3D volume. This prevents catastrophic strain localization and spreads work hardening uniformly through the crystal.
</div>
<div class="solution-step">
<strong>Step 3: Calculate critical passing distance $h_{\text{crit}}$</strong><br>
Given: $G = 26 \times 10^9\text{ Pa}$, $b = 0.286 \times 10^{-9}\text{ m}$, $\nu = 0.34$, $\tau = 50 \times 10^6\text{ Pa}$:
$$8\pi(1-\nu) = 8\pi(1 - 0.34) = 8\pi(0.66) \approx 16.5876$$
$$h_{\text{crit}} = \frac{(26 \times 10^9) \times (0.286 \times 10^{-9})}{16.5876 \times (50 \times 10^6)} = \frac{7.436}{8.2938 \times 10^8} \approx 8.966 \times 10^{-9}\text{ m} \approx 8.97\text{ nm}$$
If the cross-slip jump $h > 8.97\text{ nm}$, the edge dipoles pass each other and expand as independent Frank-Read sources. If $h < 8.97\text{ nm}$, the segments form a trapped edge dislocation dipole.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Mechanism: Cross-slip $\to$ glide by distance $h$ $\to$ second cross-slip $\to$ edge segments pin and act as a new Frank-Read source.<br>
Spreads dislocation multiplication across 3D parallel planes throughout the specimen volume.<br>
Critical passing distance $h_{\text{crit}} \approx 8.97\text{ nm}$.
</div>"""
})

# ==========================================
# Problem 32
# ==========================================
add({
    "num": 32,
    "title": "Taylor Dislocation Hardening: Flow Stress vs. Dislocation Density",
    "difficulty": "Medium",
    "category": "Strain Hardening",
    "tags": ["Taylor Hardening", "Dislocation Density", "Flow Stress"],
    "statement": r"""The classical Taylor work-hardening model states that the shear flow stress $\tau$ is governed by the elastic interaction between dislocations separated by an average spacing $l \approx 1/\sqrt{\rho_d}$:
$$\tau = \tau_0 + \alpha G b \sqrt{\rho_d}$$
where $\tau_0$ is the friction stress, $\alpha$ is an empirical interaction constant ($\approx 0.2\text{ to }0.4$), $G$ is the shear modulus, $b$ is the Burgers vector magnitude, and $\rho_d$ is the total dislocation line density (in $\text{m}^{-2}$ or $\text{cm}^{-2}$).
<br><br>
For polycrystalline nickel ($G = 76\text{ GPa}$, $b = 0.249\text{ nm}$, $\alpha = 0.30$, friction stress $\tau_0 = 15\text{ MPa}$, and Taylor orientation factor $\bar{M} = 3.06$):
<br>
1. Calculate the shear yield strength $\tau$ and macroscopic tensile yield strength $\sigma_y = \bar{M}\tau$ in the fully annealed state where $\rho_{d1} = 1.0 \times 10^{11}\text{ m}^{-2}$ ($10^7\text{ cm}^{-2}$).<br>
2. Calculate $\tau$ and $\sigma_y$ after heavy cold rolling where the dislocation density increases to $\rho_{d2} = 4.0 \times 10^{15}\text{ m}^{-2}$ ($4 \times 10^{11}\text{ cm}^{-2}$).<br>
3. Calculate the ratio $\sigma_{y2} / \sigma_{y1}$ and determine the average distance between dislocations $l = 1/\sqrt{\rho_d}$ in both states.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Yield strength in the annealed state ($\rho_{d1} = 10^{11}\text{ m}^{-2}$)</strong><br>
Pre-factor:
$$\alpha G b = 0.30 \times (76 \times 10^9\text{ Pa}) \times (0.249 \times 10^{-9}\text{ m}) \approx 5.6772\text{ N} = 5.6772\text{ Pa}\cdot\text{m}$$
$$\sqrt{\rho_{d1}} = \sqrt{1.0 \times 10^{11}} \approx 3.1623 \times 10^5\text{ m}^{-1}$$
$$\Delta\tau_1 = \alpha G b \sqrt{\rho_{d1}} = (5.6772) \times (3.1623 \times 10^5) \approx 1.795 \times 10^6\text{ Pa} \approx 1.80\text{ MPa}$$
Total shear flow stress:
$$\tau_1 = \tau_0 + \Delta\tau_1 = 15.0 + 1.80 = 16.80\text{ MPa}$$
Macroscopic tensile yield strength:
$$\sigma_{y1} = \bar{M}\tau_1 = 3.06 \times 16.80\text{ MPa} \approx 51.41\text{ MPa}$$
Dislocation spacing:
$$l_1 = \frac{1}{\sqrt{\rho_{d1}}} = \frac{1}{3.1623 \times 10^5\text{ m}^{-1}} \approx 3.162 \times 10^{-6}\text{ m} = 3.16\text{ }\mu\text{m}$$
</div>
<div class="solution-step">
<strong>Step 2: Yield strength in the cold-rolled state ($\rho_{d2} = 4 \times 10^{15}\text{ m}^{-2}$)</strong><br>
$$\sqrt{\rho_{d2}} = \sqrt{4.0 \times 10^{15}} = 2.0 \times 10^3 \times 10^{4.5} \approx 6.3246 \times 10^7\text{ m}^{-1}$$
$$\Delta\tau_2 = (5.6772) \times (6.3246 \times 10^7) \approx 3.5906 \times 10^8\text{ Pa} \approx 359.06\text{ MPa}$$
Total shear flow stress:
$$\tau_2 = 15.0 + 359.06 = 374.06\text{ MPa}$$
Macroscopic tensile yield strength:
$$\sigma_{y2} = 3.06 \times 374.06\text{ MPa} \approx 1,144.6\text{ MPa} \approx 1.14\text{ GPa}$$
Dislocation spacing:
$$l_2 = \frac{1}{\sqrt{\rho_{d2}}} = \frac{1}{6.3246 \times 10^7\text{ m}^{-1}} \approx 1.581 \times 10^{-8}\text{ m} = 15.8\text{ nm}$$
</div>
<div class="solution-step">
<strong>Step 3: Comparison and ratio</strong><br>
$$\frac{\sigma_{y2}}{\sigma_{y1}} = \frac{1,144.6\text{ MPa}}{51.41\text{ MPa}} \approx 22.26$$
Cold working increases the dislocation density by a factor of 40,000, compressing the average dislocation spacing from $3.16\text{ }\mu\text{m}$ down to just $15.8\text{ nm}$. This massive dislocation tangle boosts the tensile yield strength by more than $22\times$ (from $51\text{ MPa}$ to $1,145\text{ MPa}$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Annealed state: $\rho = 10^{11}\text{ m}^{-2} \implies l = 3.16\text{ }\mu\text{m}, \sigma_y = 51.4\text{ MPa}$<br>
Cold-rolled state: $\rho = 4 \times 10^{15}\text{ m}^{-2} \implies l = 15.8\text{ nm}, \sigma_y = 1,145\text{ MPa}$<br>
Strength increases by $22.3\times$ due to Taylor dislocation forest hardening.
</div>"""
})

# ==========================================
# Problem 33
# ==========================================
add({
    "num": 33,
    "title": "Dislocation Density Characterization: Williamson-Hall XRD Analysis",
    "difficulty": "Hard",
    "category": "Characterization",
    "tags": ["Williamson-Hall", "XRD Peak Broadening", "Microstrain", "Dislocation Density"],
    "statement": r"""X-ray diffraction peak broadening in cold-worked metals arises from two distinct physical sources: finite crystallite/domain size ($D$) and internal microstrain ($\varepsilon$) caused by dislocations.
The Williamson-Hall equation separates these two effects:
$$\beta \cos\theta = \frac{K \lambda}{D} + 4\varepsilon \sin\theta$$
where $\beta$ is the full-width at half-maximum (FWHM) in radians, $\theta$ is the Bragg angle, $\lambda = 0.15406\text{ nm}$ ($\text{Cu-}K\alpha$), and $K \approx 0.90$.
Plotting $\beta \cos\theta$ versus $4\sin\theta$ yields a straight line with slope $\varepsilon$ and $y$-intercept $\frac{K\lambda}{D}$.
<br><br>
For a cold-drawn copper wire, XRD measurements of four diffraction peaks yield:
- Peak 1 (111): $2\theta = 43.30^\circ$, $\beta = 0.00384\text{ rad}$
- Peak 2 (200): $2\theta = 50.45^\circ$, $\beta = 0.00512\text{ rad}$
- Peak 3 (220): $2\theta = 74.13^\circ$, $\beta = 0.00845\text{ rad}$
- Peak 4 (311): $2\theta = 89.93^\circ$, $\beta = 0.01160\text{ rad}$
A linear regression yields slope $\varepsilon = 2.45 \times 10^{-3}$ and intercept $Y_0 = 1.62 \times 10^{-3}$.
<br><br>
1. Calculate the coherently scattering crystallite size $D$ (in nm).<br>
2. Calculate the dislocation density $\rho_d$ using the Williamson-Smallman relation:
$$\rho_d = \frac{2\sqrt{3}\,\varepsilon}{D b}$$
where $b = 0.256\text{ nm}$.<br>
3. Name two other experimental techniques used to quantify dislocation density, and list their limitations.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate crystallite domain size $D$</strong><br>
From the $y$-intercept of the Williamson-Hall plot:
$$Y_0 = \frac{K \lambda}{D} \implies D = \frac{K \lambda}{Y_0}$$
Given $K = 0.90$, $\lambda = 0.15406\text{ nm} = 0.15406 \times 10^{-9}\text{ m}$, $Y_0 = 1.62 \times 10^{-3}$:
$$D = \frac{0.90 \times (0.15406 \times 10^{-9}\text{ m})}{1.62 \times 10^{-3}} = \frac{1.38654 \times 10^{-10}}{1.62 \times 10^{-3}} \approx 8.559 \times 10^{-8}\text{ m} = 85.6\text{ nm}$$
The average dislocation subgrain/cell size is approximately $85.6\text{ nm}$.
</div>
<div class="solution-step">
<strong>Step 2: Calculate dislocation density $\rho_d$</strong><br>
Using the Williamson-Smallman formula:
$$\rho_d = \frac{2\sqrt{3}\,\varepsilon}{D b}$$
Given $\varepsilon = 2.45 \times 10^{-3}$, $D = 85.59 \times 10^{-9}\text{ m}$, $b = 0.256 \times 10^{-9}\text{ m}$:
$$\text{Numerator} = 2\sqrt{3} \times (2.45 \times 10^{-3}) = 3.4641 \times (2.45 \times 10^{-3}) \approx 8.487 \times 10^{-3}$$
$$\text{Denominator} = D \times b = (85.59 \times 10^{-9}) \times (0.256 \times 10^{-9}) \approx 2.191 \times 10^{-17}\text{ m}^2$$
$$\rho_d = \frac{8.487 \times 10^{-3}}{2.191 \times 10^{-17}\text{ m}^2} \approx 3.873 \times 10^{14}\text{ m}^{-2} \approx 3.87 \times 10^{10}\text{ cm}^{-2}$$
</div>
<div class="solution-step">
<strong>Step 3: Alternative characterization techniques and limitations</strong><br>
1. <strong>Transmission Electron Microscopy (TEM):</strong> Direct imaging of individual dislocation lines using diffraction contrast (two-beam condition $\mathbf{g} \cdot \mathbf{b} = 0$).<br>
   <em>Limitation:</em> Extremely small sampling volume (foil thickness $< 100\text{ nm}$); foils undergo surface relaxation where dislocations escape during preparation; cannot resolve individual lines when $\rho > 10^{15}\text{ m}^{-2}$.<br>
2. <strong>Etch Pit Counting (Optical / SEM):</strong> Chemical etching selectively dissolves strained regions around dislocation cores emerging at the surface, creating visible pits.<br>
   <em>Limitation:</em> Only applicable to low dislocation densities ($\rho < 10^8\text{ cm}^{-2}$) because pits overlap and blur at higher densities; only samples surface-intersecting dislocations.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Crystallite domain size $D = 85.6\text{ nm}$<br>
Dislocation density $\rho_d = 3.87 \times 10^{14}\text{ m}^{-2}$ ($3.87 \times 10^{10}\text{ cm}^{-2}$)<br>
Alternatives: TEM (direct line imaging, small sample volume) and Etch Pits (limited to low densities $< 10^8\text{ cm}^{-2}$).
</div>"""
})

# ==========================================
# Problem 34
# ==========================================
add({
    "num": 34,
    "title": "Three Stages of Single-Crystal Work Hardening",
    "difficulty": "Medium",
    "category": "Strain Hardening",
    "tags": ["Stage I Easy Glide", "Stage II Linear Hardening", "Stage III Dynamic Recovery"],
    "statement": r"""When a high-purity FCC single crystal (e.g., copper oriented for single slip) is deformed in tension, its shear stress-shear strain ($\tau\text{--}\gamma$) curve exhibits three distinct stages of work hardening.
<br><br>
1. Define <strong>Stage I (Easy Glide)</strong>: explain why the work hardening rate $\theta_I = d\tau/d\gamma$ is extremely low ($\theta_I \approx 10^{-4} G$), and state the condition that ends Stage I.<br>
2. Define <strong>Stage II (Linear Hardening)</strong>: explain why the work hardening rate jumps to a high, universal value $\theta_{II} \approx G/300$ that is virtually independent of temperature and strain rate. What microstructural obstacles form?<br>
3. Define <strong>Stage III (Dynamic Recovery)</strong>: explain why the curve bends over ($d\tau/d\gamma$ decreases) and why the onset stress $\tau_{III}$ is strongly sensitive to temperature and stacking fault energy.<br>
4. Why do polycrystalline metals rarely show Stage I easy glide?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Stage I (Easy Glide)</strong><br>
- <em>Microstructure:</em> Dislocation glide occurs exclusively on the primary slip system with the highest Schmid factor. Dislocations glide over macroscopic distances and exit the crystal at free surfaces without intersecting other dislocation systems.
- <em>Hardening rate:</em> $\theta_I = d\tau/d\gamma \approx 10^{-4} G$ (very flat).
- <em>End of Stage I:</em> As the crystal deforms, lattice rotation gradually increases the Schmid factor on a secondary slip system until the critical resolved shear stress is reached on that system, activating conjugate slip.
</div>
<div class="solution-step">
<strong>Step 2: Stage II (Linear Rapid Hardening)</strong><br>
- <em>Microstructure:</em> Multiple intersecting slip systems are now active simultaneously. Gliding primary dislocations collide with secondary forest dislocations, forming sessile junctions (such as Lomer-Cottrell locks) and dislocation pile-ups.
- <em>Hardening rate:</em> The hardening rate jumps dramatically to $\theta_{II} = d\tau/d\gamma \approx G/300$.
- <em>Temperature independence:</em> Because forming Lomer-Cottrell locks and cutting forest trees are governed by long-range elastic interactions ($G b$), $\theta_{II}$ is athermal and virtually identical across all FCC metals.
</div>
<div class="solution-step">
<strong>Step 3: Stage III (Dynamic Recovery)</strong><br>
- <em>Microstructure:</em> At high stresses, the local stress concentration at dislocation pile-ups becomes large enough to force screw dislocations to constrict their partials and <strong>cross-slip</strong> out of their blocked primary planes.
- <em>Hardening rate:</em> Cross-slipping allows dislocations of opposite sign to meet and annihilate or rearrange into low-energy cellular walls. This continuous annihilation during deformation is <strong>dynamic recovery</strong>, causing the hardening rate to decrease parabolically.
- <em>Sensitivity:</em> Because constriction requires thermal activation and depends on stacking fault width ($d \propto 1/\gamma_{\text{SF}}$), $\tau_{III}$ decreases with increasing temperature and is much lower in high-SFE metals (Al) than in low-SFE metals (brass).
</div>
<div class="solution-step">
<strong>Step 4: Polycrystals and Stage I</strong><br>
In a polycrystal, individual grains are constrained by their neighbors. To maintain grain boundary compatibility without opening voids, the Taylor criterion requires each grain to activate at least 5 independent slip systems immediately upon yielding. Because multiple slip operates from the very start, polycrystals bypass Stage I entirely and enter directly into high Stage II/III hardening.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Stage I: Single slip, easy glide, $\theta_I \approx 10^{-4} G$.<br>
Stage II: Multiple slip, Lomer-Cottrell locks, universal linear rate $\theta_{II} \approx G/300$.<br>
Stage III: Dynamic recovery via cross-slip, temperature-dependent parabolic softening.<br>
Polycrystals bypass Stage I because multi-slip is enforced from the onset of yield.
</div>"""
})

# ==========================================
# Problem 35
# ==========================================
add({
    "num": 35,
    "title": "Stacking Fault Energy and Dislocation Cell Structures vs. Planar Slip",
    "difficulty": "Medium",
    "category": "Strain Hardening",
    "tags": ["Stacking Fault Energy", "Cellular Structure", "Planar Slip", "Cross-Slip"],
    "statement": r"""The stacking fault energy (SFE, $\gamma_{\text{SF}}$) profoundly dictates the deformed dislocation microstructure of FCC metals and alloys.
Consider two alloys subjected to $20\%$ cold rolling at room temperature:
- Alloy 1: Commercially pure aluminum ($\gamma_{\text{SF}} \approx 160\text{ mJ/m}^2$)
- Alloy 2: Austenitic stainless steel AISI 304 or $\alpha$-brass Cu-30Zn ($\gamma_{\text{SF}} \approx 15\text{ mJ/m}^2$)
<br><br>
1. Under Transmission Electron Microscopy (TEM), one alloy reveals a well-developed 3D <strong>cellular dislocation structure</strong> with dislocation-free cell interiors surrounded by dense dislocation cell walls. The other reveals straight, parallel arrays of <strong>planar slip bands</strong> and stacking fault ribbons. Assign each alloy to its corresponding microstructure.<br>
2. Explain the physical mechanism connecting stacking fault energy to the ability of dislocations to form cell walls.<br>
3. Explain why low-SFE alloys (like 304 stainless steel and brass) exhibit much higher work hardening rates ($n \approx 0.45\text{--}0.50$) than high-SFE metals like aluminum ($n \approx 0.15\text{--}0.20$).""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Microstructure assignment</strong><br>
- <strong>Alloy 1 (Aluminum, $\gamma_{\text{SF}} = 160\text{ mJ/m}^2$):</strong> Forms <strong>cellular dislocation structures</strong>. Cell interiors are nearly dislocation-free, bounded by thick, tangled dislocation sub-boundaries (LEDS).<br>
- <strong>Alloy 2 (304 Stainless Steel / Brass, $\gamma_{\text{SF}} = 15\text{ mJ/m}^2$):</strong> Forms <strong>strictly planar slip bands</strong>, wide stacking faults, and deformation twins, with zero cell structure.
</div>
<div class="solution-step">
<strong>Step 2: Physical mechanism (cross-slip capability)</strong><br>
To form a 3D cellular network, dislocations must be able to escape their initial 2D slip planes, glide in three dimensions, and cross-slip into low-energy wall configurations.<br>
- In high-SFE metals (Al, Ni), partial dislocations are separated by $< 1\text{ nm}$. Thermal energy easily constricts the partials, allowing instantaneous screw dislocation cross-slip in all directions, driving rapid dynamic recovery and cellular patterning.<br>
- In low-SFE alloys (brass, stainless steel), the partial dislocations are widely separated ($d > 5\text{--}10\text{ nm}$). Constricting this wide ribbon requires prohibitive energy. Dislocations are geometrically locked into their original 2D slip plane, forcing them to glide in straight coplanar arrays (planar slip).
</div>
<div class="solution-step">
<strong>Step 3: High work hardening in low-SFE alloys</strong><br>
In low-SFE alloys:
1. <em>Suppression of dynamic recovery:</em> Dislocations cannot cross-slip to annihilate; dislocation density accumulates relentlessly with strain.
2. <em>Planar pile-ups and twin boundaries:</em> Coplanar dislocations form massive pile-ups that generate severe back stresses.
3. <em>Deformation twinning (TWIP effect):</em> At higher strains, mechanical microtwins nucleate. The twin boundaries act as new, impenetrable planar obstacles, progressively reducing the dislocation mean free path (dynamic Hall-Petch effect).
This prevents saturation of flow stress, delivering sustained high strain hardening exponents ($n \approx 0.45\text{--}0.50$) and immense uniform elongation ($> 60\%$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
High SFE (Al): Narrow ribbon $\to$ easy cross-slip $\to$ 3D dislocation cell networks ($n \approx 0.18$).<br>
Low SFE (Brass/SS): Wide ribbon $\to$ cross-slip forbidden $\to$ strictly planar slip and deformation twinning.<br>
Low SFE metals maintain exceptionally high strain hardening ($n \approx 0.45$) due to suppressed dynamic recovery and the dynamic Hall-Petch effect.
</div>"""
})

# ==========================================
# Problem 36
# ==========================================
add({
    "num": 36,
    "title": "Precipitation Hardening: The Three-Step Heat Treatment Process",
    "difficulty": "Easy",
    "category": "Precipitation Hardening",
    "tags": ["Precipitation Hardening", "Solution Treatment", "Aging", "Al-Cu Alloy"],
    "statement": r"""Precipitation hardening (age hardening) is the primary method used to strengthen aerospace aluminum, titanium, and nickel superalloys.
The base requirement is an alloy phase diagram with a terminal solid solution exhibiting decreasing solid solubility with decreasing temperature (sloping solvus line).
<br><br>
Consider an aluminum-copper alloy containing $4.0\text{ wt}\%\text{ Cu}$ (e.g., Al 2024 base).
<br><br>
1. Detail the three sequential processing steps required for precipitation hardening:
   (a) Step 1: Solution Heat Treatment (give typical temperature range).<br>
   (b) Step 2: Quenching (explain why water quenching is necessary).<br>
   (c) Step 3: Aging (distinguish between natural aging and artificial aging).<br>
2. What non-equilibrium phase state is produced immediately after Step 2?<br>
3. Why does the alloy possess low hardness and high ductility immediately after quenching, but reaches maximum strength only after aging?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The three sequential steps</strong><br>
(a) <strong>Solution Heat Treatment:</strong> The alloy is heated into the single-phase $\alpha$ solid solution field (typically $500^\circ\text{C}\text{ to }520^\circ\text{C}$ for Al-4%Cu, above the solvus line at $480^\circ\text{C}$ but safely below the eutectic melting temperature at $548^\circ\text{C}$). The alloy is held until all copper dissolves homogeneously into the FCC aluminum matrix.<br>
(b) <strong>Quenching:</strong> The material is rapidly cooled to room temperature (usually by immersion in agitated water). Rapid quenching prevents diffusion, kinetically trapping all copper solute atoms and excess thermal vacancies in the lattice.<br>
(c) <strong>Aging:</strong>
- <em>Natural Aging:</em> The quenched alloy is held at room temperature ($20^\circ\text{C}\text{--}25^\circ\text{C}$) for several days. Solute clusters (GP zones) form slowly by vacancy-assisted diffusion.
- <em>Artificial Aging:</em> The alloy is reheated to an intermediate temperature ($150^\circ\text{C}\text{ to }190^\circ\text{C}$) for $8\text{ to }24\text{ hours}$. Elevated temperature accelerates solute diffusion, promoting precipitation of fine metastable transition phases ($\theta''$ and $\theta'$).
</div>
<div class="solution-step">
<strong>Step 2: Non-equilibrium state after quenching</strong><br>
Immediately following quenching, the alloy exists as a <strong>Supersaturated Solid Solution (SSSS)</strong>. The aluminum lattice is forced to hold $4.0\text{ wt}\%\text{ Cu}$ in solution, even though the equilibrium thermodynamic solubility at room temperature is less than $0.05\text{ wt}\%\text{ Cu}$ ($> 80\times$ supersaturation). It also contains a high concentration of trapped non-equilibrium vacancies ($C_v \sim 10^{-4}$).
</div>
<div class="solution-step">
<strong>Step 3: Hardness evolution</strong><br>
- <em>Immediately after quenching:</em> Copper atoms are randomly dispersed in solid solution. The lattice strain around isolated individual copper atoms is relatively weak, providing only modest solid solution strengthening. The alloy is soft and highly ductile, ideal for forming, bending, or riveting.<br>
- <em>After aging:</em> Diffusion drives copper atoms to aggregate into billions of dense, coherent nanoscale precipitate particles ($\theta''$ and $\theta'$) spaced only $10\text{ to }30\text{ nm}$ apart. These coherent precipitates create intense localized strain fields and order barriers that severely impede dislocation glide, raising the yield strength by $300\%\text{ to }400\%$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Step 1: Solution treat ($500\text{--}520^\circ\text{C}$) $\to$ Step 2: Water quench $\to$ Step 3: Aging (Natural at $20^\circ\text{C}$ or Artificial at $160\text{--}190^\circ\text{C}$).<br>
Quenched state: Supersaturated Solid Solution (SSSS) with trapped excess vacancies.<br>
Soft immediately after quench (easy forming); reaches peak strength after aging due to billions of coherent nanoscale precipitates.
</div>"""
})

# ==========================================
# Problem 37
# ==========================================
add({
    "num": 37,
    "title": "Precipitation Sequence in Al-Cu Alloys: From GP Zones to Equilibrium Phase",
    "difficulty": "Hard",
    "category": "Precipitation Hardening",
    "tags": ["Precipitation Sequence", "GP Zones", "Theta Prime", "Coherency"],
    "statement": r"""During artificial aging of an Al-4wt%Cu alloy, the equilibrium precipitate phase $\theta\text{ (}\text{CuAl}_2\text{)}$ does not form directly because its complex body-centered tetragonal crystal structure has a large interfacial energy barrier with the FCC matrix.
Instead, decomposition follows a multi-step precipitation sequence:
$$\text{SSSS} \to \text{GP-I zones} \to \text{GP-II zones } (\theta'') \to \text{Metastable } \theta' \to \text{Equilibrium } \theta\text{ (}\text{CuAl}_2\text{)}$$
<br>
1. Describe the structure, morphology, and interface coherency of:
   (a) <strong>GP-I zones</strong> (Guinier-Preston zones).<br>
   (b) <strong>GP-II zones</strong> (also designated $\theta''$).<br>
   (c) <strong>Metastable $\theta'$ phase</strong>.<br>
   (d) <strong>Equilibrium $\theta$ phase</strong> ($\text{CuAl}_2$).<br>
2. Why does the system form metastable intermediate phases that have higher bulk free energy than the equilibrium $\theta$ phase? Refer to the activation energy barrier for nucleation $\Delta G^* \propto \gamma_{\alpha/\beta}^3 / (\Delta G_v)^2$.<br>
3. Which of these precipitate phases corresponds to the <strong>peak-aged hardness</strong> condition in 2000-series aerospace aluminum alloys?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Microstructural characteristics of each phase</strong><br>
(a) <strong>GP-I Zones:</strong> Single-atom-thick disks of pure copper atoms ($1\text{--}2$ atomic layers thick, $3\text{--}10\text{ nm}$ diameter) segregated onto $\{100\}$ planes of the aluminum matrix. They are <strong>fully coherent</strong> with the FCC matrix, causing strong tetragonal elastic coherency strain fields in the surrounding lattice.<br>
(b) <strong>GP-II Zones ($\theta''$):</strong> Multilayer copper-rich platelets ($2\text{--}3\text{ nm}$ thick, $10\text{--}30\text{ nm}$ diameter) separated by aluminum layers. They possess an ordered tetragonal structure and remain <strong>fully coherent</strong> along their broad faces, generating intense long-range coherency strain fields.<br>
(c) <strong>Metastable $\theta'$ Phase:</strong> Plate-like particles with a body-centered tetragonal structure ($\text{Al}_2\text{Cu}$, $a = 0.404\text{ nm}, c = 0.580\text{ nm}$). They are <strong>semi-coherent</strong>: fully coherent with $\{100\}$ matrix planes along their broad faces, but have disordered, incoherent cylindrical rim edges with misfit dislocations.<br>
(d) <strong>Equilibrium $\theta$ Phase ($\text{CuAl}_2$):</strong> Coarse, rounded or lenticular particles with a complex body-centered tetragonal structure ($a = 0.607\text{ nm}, c = 0.487\text{ nm}$). They are completely <strong>incoherent</strong> with the FCC aluminum matrix, exhibiting high interfacial energy ($\gamma \approx 500\text{ mJ/m}^2$) and zero coherency strain.
</div>
<div class="solution-step">
<strong>Step 2: Why metastable phases nucleate first (Ostwald's Step Rule)</strong><br>
Classical nucleation theory states that the activation barrier for nucleation is:
$$\Delta G^* \propto \frac{\gamma_{\alpha/\beta}^3}{(\Delta G_v)^2}$$
Because the interfacial energy $\gamma_{\alpha/\beta}$ enters to the <strong>third power</strong>, it exerts complete control over nucleation kinetics:
- Equilibrium $\theta$ is incoherent with high surface energy ($\gamma \sim 500\text{ mJ/m}^2$), producing a massive nucleation barrier $\Delta G^*$ that cannot be overcome at aging temperatures ($150\text{--}190^\circ\text{C}$).
- GP zones and $\theta''$ are fully coherent with atomic matching across interfaces, yielding an exceptionally tiny interfacial energy ($\gamma \sim 10\text{--}30\text{ mJ/m}^2$).
Because $\Delta G^*$ for coherent GP zones is negligible, they nucleate homogeneously and rapidly throughout the matrix. The system follows Ostwald's rule of stages: nucleating the phase of closest structural similarity first, progressively transforming toward equilibrium.
</div>
<div class="solution-step">
<strong>Step 3: Peak-aged phase</strong><br>
The peak hardness and maximum yield strength (T6 temper) correspond to a dense dispersion of <strong>GP-II zones ($\theta''$) and fine $\theta'$ platelets</strong>. At this microstructural stage, the combination of maximum particle density, optimum particle spacing, and immense elastic coherency strain fields maximizes dislocation resistance.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Sequence: SSSS $\to$ GP-I (coherent Cu monolayers) $\to$ GP-II/$\theta''$ (coherent multilayer platelets) $\to$ $\theta'$ (semi-coherent) $\to$ $\theta$ (incoherent $\text{CuAl}_2$).<br>
Metastable phases form first because their coherent interfaces possess tiny interfacial energy ($\gamma^3$), eliminating the nucleation energy barrier.<br>
Peak strength (T6 temper) is achieved by a dense dispersion of $\theta''$ and fine $\theta'$ platelets.
</div>"""
})

# ==========================================
# Problem 38
# ==========================================
add({
    "num": 38,
    "title": "Dislocation Particle Cutting (Friedel-Fleischer Shearing Mechanism)",
    "difficulty": "Hard",
    "category": "Precipitation Hardening",
    "tags": ["Particle Shearing", "Friedel Cutting", "Order Strengthening", "Coherency Strain"],
    "statement": r"""When a dislocation encounters small, coherent precipitate particles (radius $r < r_c$), it shears (cuts) directly through the particles.
Three physical mechanisms resist particle shearing:
1. <strong>Coherency Strain Strengthening ($\Delta\tau_{\text{coh}}$):</strong> Interaction with lattice mismatch strain $\varepsilon_{\text{coh}}$:
$$\Delta\tau_{\text{coh}} = A_1 G |\varepsilon_{\text{coh}}|^{3/2} \left(\frac{r f}{b}\right)^{1/2}$$
2. <strong>Chemical / Interfacial Strengthening ($\Delta\tau_{\text{chem}}$):</strong> Creation of new precipitate/matrix surface area $\Delta A = 2b r$ per cut:
$$\Delta\tau_{\text{chem}} = A_2 \frac{\gamma_{\text{inter}}^{3/2} f^{1/2}}{G^{1/2} b} \left(\frac{r}{b}\right)^{1/2}$$
3. <strong>Order Strengthening ($\Delta\tau_{\text{order}}$):</strong> Passing through an ordered intermetallic precipitate (e.g., $\text{Ni}_3\text{Al}$ $\gamma'$ in superalloys) creates an Anti-Phase Boundary (APB) with energy $\gamma_{\text{APB}}$:
$$\Delta\tau_{\text{order}} = \frac{\gamma_{\text{APB}}}{2b} \left[ \left(\frac{3\pi^2 \gamma_{\text{APB}} f r}{32 T}\right)^{1/2} - f \right]$$
<br>
1. Show that all three particle-cutting mechanisms share the identical mathematical scaling: $\Delta\tau_{\text{cut}} \propto r^{1/2}$.<br>
2. A nickel-base superalloy contains an ordered $\gamma'$ volume fraction $f = 0.20$. If increasing the average precipitate radius from $r_1 = 3.0\text{ nm}$ to $r_2 = 12.0\text{ nm}$ keeps the alloy in the particle-cutting regime, calculate the ratio $\Delta\tau_{\text{cut}}(r_2) / \Delta\tau_{\text{cut}}(r_1)$.<br>
3. Why does shearing particles lead to <strong>planar slip localization</strong> and strain softening in underaged alloys?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Common scaling law $\Delta\tau \propto r^{1/2}$</strong><br>
Examining the governing equations:
- Coherency strain: $\Delta\tau_{\text{coh}} \propto \left(\frac{r f}{b}\right)^{1/2} \propto r^{1/2}$
- Chemical interface: $\Delta\tau_{\text{chem}} \propto \left(\frac{r}{b}\right)^{1/2} \propto r^{1/2}$
- Order strengthening (Friedel cutting): $\Delta\tau_{\text{order}} \propto (r f)^{1/2} \propto r^{1/2}$
In all shearing mechanisms, the resisting force increases as the cross-sectional area or chord length sheared by the dislocation increases with particle radius ($F_p \propto r$), while Friedel flexible dislocation bowing statistics introduce the square-root dependence $\Delta\tau \propto r^{1/2}$.
</div>
<div class="solution-step">
<strong>Step 2: Ratio of strength increase upon aging</strong><br>
Since $\Delta\tau_{\text{cut}} \propto \sqrt{r}$ at constant volume fraction $f$:
$$\frac{\Delta\tau_{\text{cut}}(r_2)}{\Delta\tau_{\text{cut}}(r_1)} = \sqrt{\frac{r_2}{r_1}} = \sqrt{\frac{12.0\text{ nm}}{3.0\text{ nm}}} = \sqrt{4.0} = 2.00$$
Quadrupling the precipitate radius from $3\text{ nm}$ to $12\text{ nm}$ during underaged aging doubles the strengthening contribution ($+100\%$).
</div>
<div class="solution-step">
<strong>Step 3: Planar slip localization in sheared alloys</strong><br>
When a leading dislocation cuts through a precipitate, it shears the particle by Burgers vector $b$, reducing its effective cross-sectional area and destroying atomic order on that slip plane.
Consequently, trailing dislocations gliding on that exact same slip plane encounter weakened, sheared particles and face lower resistance. This creates localized <strong>work softening on active slip planes</strong>, concentrating all plastic strain into narrow, intense planar slip bands. This localized shearing can trigger premature shear cracking and low fatigue ductility in underaged alloys.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
All particle cutting mechanisms scale as $\Delta\tau_{\text{cut}} \propto r^{1/2}$.<br>
Increasing radius from $3\text{ nm}$ to $12\text{ nm}$ doubles the yield strength increment ($\times 2.00$).<br>
Cutting weakens precipitates on active slip planes, triggering intense planar slip localization.
</div>"""
})

# ==========================================
# Problem 39
# ==========================================
add({
    "num": 39,
    "title": "Orowan Dislocation Looping Bypass Mechanism",
    "difficulty": "Hard",
    "category": "Precipitation Hardening",
    "tags": ["Orowan Looping", "Dislocation Bypass", "Orowan Formula", "Overaging"],
    "statement": r"""When precipitates coarsen beyond a critical radius $r_c$, or when particles are incoherent (such as equilibrium $\theta$ in Al-Cu or oxide dispersoids in ODS alloys), dislocations cannot shear them.
Instead, the dislocation bows between adjacent particles and bypasses them by the <strong>Orowan looping mechanism</strong>, leaving behind a closed dislocation loop around each particle.
The Orowan shear stress $\tau_{\text{Orowan}}$ is:
$$\tau_{\text{Orowan}} = \frac{G b}{2\pi \sqrt{1-\nu}} \frac{1}{\lambda - 2r} \ln\left(\frac{2r}{r_0}\right) \approx \frac{G b}{L_{\text{eff}}}$$
where $L_{\text{eff}} = \lambda - 2r$ is the clear interparticle spacing.
For spherical particles of radius $r$ and volume fraction $f$, the planar center-to-center particle spacing is $\lambda = r \sqrt{\frac{2\pi}{3f}} \approx 1.45\,\frac{r}{\sqrt{f}}$.
<br><br>
In an overaged aluminum alloy ($G = 26\text{ GPa}$, $b = 0.286\text{ nm}$, $\nu = 0.34$, inner cut-off $r_0 \approx b$):
The precipitate volume fraction is $f = 0.04$ ($4\%$).
<br><br>
1. Calculate the center-to-center spacing $\lambda$ and clear spacing $L_{\text{eff}} = \lambda - 2r$ for an average particle radius $r_1 = 15.0\text{ nm}$.<br>
2. Calculate the Orowan bypass shear stress $\tau_{\text{Orowan}}$ for $r_1 = 15.0\text{ nm}$.<br>
3. If excessive overaging coarsens the particles to $r_2 = 60.0\text{ nm}$ at the same volume fraction $f = 0.04$, calculate the new Orowan stress $\tau_{\text{Orowan}}'$.<br>
4. Show that Orowan strengthening scales inversely with particle radius ($\tau_{\text{Orowan}} \propto 1/r$).""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate particle spacings for $r_1 = 15.0\text{ nm}$</strong><br>
$$\lambda_1 = r_1 \sqrt{\frac{2\pi}{3f}} = 15.0 \times \sqrt{\frac{2\pi}{3(0.04)}} = 15.0 \times \sqrt{\frac{6.28318}{0.12}} = 15.0 \times \sqrt{52.3599} = 15.0 \times 7.236 \approx 108.54\text{ nm}$$
The clear spacing between particle surfaces is:
$$L_{\text{eff}, 1} = \lambda_1 - 2r_1 = 108.54 - 2(15.0) = 108.54 - 30.0 = 78.54\text{ nm} = 78.54 \times 10^{-9}\text{ m}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate Orowan shear stress for $r_1 = 15.0\text{ nm}$</strong><br>
$$\text{Pre-factor} = \frac{G b}{2\pi \sqrt{1-\nu}} = \frac{(26 \times 10^9) \times (0.286 \times 10^{-9})}{2\pi \sqrt{1 - 0.34}} = \frac{7.436}{2\pi \sqrt{0.66}} = \frac{7.436}{2\pi(0.8124)} = \frac{7.436}{5.1045} \approx 1.4567\text{ N}$$
Logarithmic factor ($r_0 = b = 0.286\text{ nm}$):
$$\ln\left(\frac{2r_1}{r_0}\right) = \ln\left(\frac{30.0}{0.286}\right) = \ln(104.9) \approx 4.653$$
$$\tau_{\text{Orowan}, 1} = \frac{1.4567\text{ N}}{78.54 \times 10^{-9}\text{ m}} \times 4.653 = (1.8547 \times 10^7) \times 4.653 \approx 8.63 \times 10^7\text{ Pa} \approx 86.30\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Calculate Orowan stress for coarsened particles $r_2 = 60.0\text{ nm}$</strong><br>
$$\lambda_2 = 60.0 \times 7.236 \approx 434.16\text{ nm}$$
$$L_{\text{eff}, 2} = 434.16 - 2(60.0) = 434.16 - 120.0 = 314.16\text{ nm} = 314.16 \times 10^{-9}\text{ m}$$
$$\ln\left(\frac{2r_2}{r_0}\right) = \ln\left(\frac{120.0}{0.286}\right) = \ln(419.6) \approx 6.039$$
$$\tau_{\text{Orowan}, 2} = \frac{1.4567\text{ N}}{314.16 \times 10^{-9}\text{ m}} \times 6.039 = (4.6368 \times 10^6) \times 6.039 \approx 2.80 \times 10^7\text{ Pa} \approx 28.00\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: Inverse scaling with radius $\tau \propto 1/r$</strong><br>
Since $\lambda \propto r / \sqrt{f}$, at constant volume fraction $f$, clear spacing $L_{\text{eff}} = r(C - 2) \propto r$.
Neglecting the weak logarithmic term:
$$\tau_{\text{Orowan}} \approx \frac{G b}{L_{\text{eff}}} \propto \frac{\sqrt{f}}{r}$$
Coarsening the particles by $4\times$ (from $15\text{ nm}$ to $60\text{ nm}$) reduces the Orowan yield resistance by a factor of $86.3 / 28.0 \approx 3.08\times$, explaining why overaged alloys suffer dramatic loss of strength.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
At $r = 15\text{ nm}$: clear spacing $L_{\text{eff}} = 78.5\text{ nm} \implies \tau_{\text{Orowan}} = 86.3\text{ MPa}$<br>
At $r = 60\text{ nm}$: clear spacing $L_{\text{eff}} = 314.2\text{ nm} \implies \tau_{\text{Orowan}} = 28.0\text{ MPa}$<br>
Orowan stress scales inversely with precipitate radius ($\tau \propto 1/r$).
</div>"""
})

# ==========================================
# Problem 40
# ==========================================
add({
    "num": 40,
    "title": "Peak Aging and Critical Precipitate Radius $r_c$",
    "difficulty": "Medium",
    "category": "Precipitation Hardening",
    "tags": ["Peak Aging", "Critical Radius", "Cutting vs Looping", "T6 Temper"],
    "statement": r"""The overall yield strength of a precipitation-hardened alloy is governed by the competition between dislocation particle cutting (active at small radii) and Orowan dislocation looping (active at large radii):
$$\tau_{\text{cutting}} = C_1 \sqrt{r}$$
$$\tau_{\text{looping}} = \frac{C_2}{r}$$
Peak aging (maximum yield strength $\tau_{\text{peak}}$) occurs at the critical transition radius $r_c$ where the two curves intersect: $\tau_{\text{cutting}}(r_c) = \tau_{\text{looping}}(r_c)$.
<br><br>
For an aerospace aluminum alloy, experimental calibrations determine:
$C_1 = 28.0\text{ MPa}\cdot\text{nm}^{-1/2}$ and $C_2 = 700.0\text{ MPa}\cdot\text{nm}$.
<br><br>
1. Calculate the critical precipitate radius $r_c$ (in nm).<br>
2. Calculate the peak shear strength increment $\tau_{\text{peak}}$ at $r = r_c$.<br>
3. Define the three aging regimes: <strong>underaged</strong>, <strong>peak-aged</strong>, and <strong>overaged</strong>, and identify the active dislocation mechanism in each regime.<br>
4. Why do aerospace engineers often specify slightly overaged tempers (e.g., 7075-T73 rather than peak-aged 7075-T6) for safety-critical airframe components?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate critical precipitate radius $r_c$</strong><br>
At the transition point between cutting and looping:
$$C_1 \sqrt{r_c} = \frac{C_2}{r_c}$$
Multiply both sides by $r_c$:
$$C_1 r_c^{3/2} = C_2 \implies r_c^{3/2} = \frac{C_2}{C_1} = \frac{700.0}{28.0} = 25.0$$
Raising both sides to the power of $2/3$:
$$r_c = (25.0)^{2/3} = (25.0)^{0.6667} \approx 8.550\text{ nm}$$
The critical precipitate radius for maximum strength is $r_c \approx 8.55\text{ nm}$ (diameter $\approx 17.1\text{ nm}$).
</div>
<div class="solution-step">
<strong>Step 2: Calculate peak shear strength increment $\tau_{\text{peak}}$</strong><br>
Substitute $r_c = 8.550\text{ nm}$ into either formula:
$$\tau_{\text{peak}} = C_1 \sqrt{r_c} = 28.0 \times \sqrt{8.550} = 28.0 \times 2.9240 \approx 81.87\text{ MPa}$$
Check with looping formula:
$$\tau_{\text{looping}} = \frac{C_2}{r_c} = \frac{700.0}{8.550} \approx 81.87\text{ MPa}$$
Both yield exactly $\tau_{\text{peak}} \approx 81.9\text{ MPa}$.
</div>
<div class="solution-step">
<strong>Step 3: The three aging regimes</strong><br>
1. <strong>Underaged regime ($r < r_c$):</strong> Governed by <em>particle cutting (shearing)</em>. Strength increases with aging time ($\tau \propto \sqrt{r}$). High strength but susceptible to planar slip and strain localization.<br>
2. <strong>Peak-aged regime ($r = r_c$):</strong> Intersection point where shearing resistance equals looping resistance. Maximum achievable yield strength (T6 temper).<br>
3. <strong>Overaged regime ($r > r_c$):</strong> Governed by <em>Orowan dislocation looping</em>. Strength decreases with aging time ($\tau \propto 1/r$) as particles coarsen and spacing increases.
</div>
<div class="solution-step">
<strong>Step 4: Why T73 overaging is preferred over peak-aged T6</strong><br>
Although peak-aged 7075-T6 offers the absolute maximum yield strength ($\sim 505\text{ MPa}$), it is notoriously susceptible to <strong>Stress Corrosion Cracking (SCC)</strong> and has lower fracture toughness ($K_{Ic}$). In the T6 temper, continuous solute-depleted zones (PFZ) and coherent grain boundary precipitates promote intergranular corrosion and rapid cracking under sustained tensile stress in humid/marine environments.<br>
Overaging to the <strong>T73 temper</strong> (two-stage aging at $107^\circ\text{C}$ then $163^\circ\text{C}$) coarsens boundary precipitates into discrete, separated incoherent particles and widens the PFZ. Although yield strength drops by $\sim 12\%\text{ to }15\%$ (to $\sim 435\text{ MPa}$), the material becomes virtually immune to catastrophic stress corrosion cracking and gains significantly higher fracture toughness.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Critical radius: $r_c = 8.55\text{ nm}$<br>
Peak strength increment: $\tau_{\text{peak}} = 81.9\text{ MPa}$<br>
Underaged ($r < r_c$): Particle cutting ($\propto \sqrt{r}$); Overaged ($r > r_c$): Orowan looping ($\propto 1/r$).<br>
T73 overaging sacrifices $15\%$ strength to achieve immunity against stress corrosion cracking (SCC) and maximize toughness.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 7 Part 2: P26-P40 added. Current total: {len(P)}")

# ==========================================
# Problem 41
# ==========================================
add({
    "num": 41,
    "title": "Ostwald Ripening and LSW Precipitate Coarsening Kinetics",
    "difficulty": "Hard",
    "category": "Precipitation Hardening",
    "tags": ["Ostwald Ripening", "LSW Theory", "Gibbs-Thomson", "Coarsening"],
    "statement": r"""During extended service at elevated temperatures, fine precipitate particles dissolve while larger particles grow at their expense to minimize the total interfacial surface free energy. This is <strong>Ostwald ripening</strong>.
Driven by the Gibbs-Thomson effect, the solute concentration $C_r$ in the matrix at the surface of a spherical particle of radius $r$ is:
$$C_r = C_\infty \exp\left(\frac{2\gamma V_m}{R T r}\right) \approx C_\infty \left(1 + \frac{2\gamma V_m}{R T r}\right)$$
According to the Lifshitz-Slyozov-Wagner (LSW) theory, diffusion-controlled coarsening follows:
$$\bar{r}^3 - r_0^3 = K t$$
where the coarsening rate constant is $K = \frac{8 \gamma D C_\infty V_m^2}{9 R T}$.
<br><br>
In a nickel alloy aged at $T = 1000\text{ K}$ ($727^\circ\text{C}$):
$\gamma = 0.050\text{ J/m}^2$, $V_m = 7.0 \times 10^{-6}\text{ m}^3/\text{mol}$, $D = 2.0 \times 10^{-16}\text{ m}^2/\text{s}$, $C_\infty = 0.02\text{ mol/m}^3$, and $R = 8.314\text{ J}/(\text{mol}\cdot\text{K})$.
<br><br>
1. Calculate the LSW coarsening rate constant $K$ (in $\text{m}^3/\text{s}$ and $\text{nm}^3/\text{h}$).<br>
2. If the initial average radius after heat treatment is $r_0 = 10.0\text{ nm}$, calculate the average precipitate radius $\bar{r}$ after holding at $1000\text{ K}$ for $100\text{ hours}$ and $1000\text{ hours}$.<br>
3. By what factor does the Orowan yield strength drop between $t = 100\text{ h}$ and $t = 1000\text{ h}$?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate LSW coarsening rate constant $K$</strong><br>
$$R T = 8.314 \times 1000 = 8,314\text{ J/mol}$$
$$V_m^2 = (7.0 \times 10^{-6})^2 = 4.9 \times 10^{-11}\text{ m}^6/\text{mol}^2$$
$$\text{Numerator} = 8 \times \gamma \times D \times C_\infty \times V_m^2$$
$$\text{Num} = 8 \times (0.050) \times (2.0 \times 10^{-16}) \times (0.02) \times (4.9 \times 10^{-11}) = 8 \times 9.8 \times 10^{-29} = 7.84 \times 10^{-28}$$
$$\text{Denominator} = 9 R T = 9 \times 8,314 = 74,826\text{ J/mol}$$
$$K = \frac{7.84 \times 10^{-28}}{74,826} \approx 1.0478 \times 10^{-32}\text{ m}^3/\text{s}$$
Convert to $\text{nm}^3/\text{h}$:
$$1\text{ m}^3 = 10^{27}\text{ nm}^3, \quad 1\text{ h} = 3,600\text{ s}$$
$$K = (1.0478 \times 10^{-32}\text{ m}^3/\text{s}) \times (10^{27}\text{ nm}^3/\text{m}^3) \times (3,600\text{ s/h}) \approx 37.72\text{ nm}^3/\text{h}$$
</div>
<div class="solution-step">
<strong>Step 2: Precipitate radius after $100\text{ h}$ and $1000\text{ h}$</strong><br>
Initial volume factor: $r_0^3 = (10.0\text{ nm})^3 = 1,000\text{ nm}^3$.
<br>
- <em>At $t_1 = 100\text{ h}$:</em>
$$\bar{r}_1^3 = r_0^3 + K t_1 = 1,000 + (37.72 \times 100) = 1,000 + 3,772 = 4,772\text{ nm}^3$$
$$\bar{r}_1 = (4,772)^{1/3} \approx 16.84\text{ nm}$$
<br>
- <em>At $t_2 = 1000\text{ h}$:</em>
$$\bar{r}_2^3 = r_0^3 + K t_2 = 1,000 + (37.72 \times 1000) = 1,000 + 37,720 = 38,720\text{ nm}^3$$
$$\bar{r}_2 = (38,720)^{1/3} \approx 33.83\text{ nm}$$
</div>
<div class="solution-step">
<strong>Step 3: Drop in Orowan yield strength</strong><br>
Since the alloy is overaged, strength is governed by Orowan looping: $\tau_{\text{Orowan}} \propto 1/\bar{r}$.
$$\frac{\tau_{\text{Orowan}}(1000\text{ h})}{\tau_{\text{Orowan}}(100\text{ h})} = \frac{\bar{r}_1}{\bar{r}_2} = \frac{16.84\text{ nm}}{33.83\text{ nm}} \approx 0.4978 \approx 0.50$$
After $1000\text{ hours}$ of thermal exposure, particle coarsening cuts the Orowan strengthening increment in half (a $50.2\%$ drop in strength).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Rate constant $K = 1.05 \times 10^{-32}\text{ m}^3/\text{s} = 37.7\text{ nm}^3/\text{h}$<br>
At $100\text{ h}$: $\bar{r} = 16.8\text{ nm}$; At $1000\text{ h}$: $\bar{r} = 33.8\text{ nm}$<br>
Orowan yield strength drops by $50\%$ between $100\text{ h}$ and $1000\text{ h}$ due to Ostwald ripening.
</div>"""
})

# ==========================================
# Problem 42
# ==========================================
add({
    "num": 42,
    "title": "Precipitate-Free Zones (PFZs) at Grain Boundaries",
    "difficulty": "Medium",
    "category": "Precipitation Hardening",
    "tags": ["PFZ", "Precipitate-Free Zone", "Vacancy Depletion", "Intergranular Fracture"],
    "statement": r"""In age-hardenable aluminum alloys (e.g., Al-Zn-Mg 7000-series), bright-field transmission electron micrographs often reveal narrow, precipitate-denuded channels running parallel to grain boundaries known as <strong>Precipitate-Free Zones (PFZs)</strong>.
The grain interior contains a dense dispersion of hardening precipitates, but a channel of width $W_{\text{PFZ}} = 50\text{--}200\text{ nm}$ adjacent to the boundary is completely devoid of strengthening particles.
<br><br>
1. Explain the two physical mechanisms responsible for PFZ formation during quenching and aging:
   (a) The <strong>vacancy-depletion model</strong>.<br>
   (b) The <strong>solute-depletion model</strong>.<br>
2. A high-strength aluminum alloy has a matrix yield strength $\sigma_{y,\text{matrix}} = 520\text{ MPa}$, but the soft PFZ has a local yield strength of only $\sigma_{y,\text{PFZ}} = 140\text{ MPa}$. When the alloy is pulled in tension, what happens at the grain boundaries?<br>
3. How do PFZs promote intergranular stress corrosion cracking (SCC) and brittle intergranular ductile rupture?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Two mechanisms of PFZ formation</strong><br>
(a) <strong>Vacancy-Depletion Mechanism:</strong> During solution heat treatment at high temperature, a high equilibrium concentration of vacancies is produced ($C_v \sim 10^{-4}$). Grain boundaries act as ideal, unsaturable sinks for vacancies. During quenching, vacancies near grain boundaries rapidly diffuse into the boundary and are annihilated. In the adjacent vacancy-depleted zone, the vacancy concentration falls below the critical threshold required to catalyze the nucleation of GP zones and $\theta''$/$\eta'$ precipitates, leaving a precipitate-free channel.<br>
(b) <strong>Solute-Depletion Mechanism:</strong> During cooling and subsequent aging, heterogeneous nucleation occurs readily on high-angle grain boundaries because the boundary reduces the interfacial energy barrier. Large, coarse equilibrium precipitates (e.g., $\text{MgZn}_2$ or $\text{CuAl}_2$) grow rapidly along the boundary, draining solute atoms from the adjacent matrix. This leaves a solute-denuded zone where solute concentration drops below the solvus line, preventing any matrix precipitation.
</div>
<div class="solution-step">
<strong>Step 2: Microscopic strain localization in the PFZ</strong><br>
When macroscopic tensile load is applied:
- Once stress reaches $140\text{ MPa}$, the soft, unreinforced PFZ yields plastically, while the surrounding matrix ($\sigma_y = 520\text{ MPa}$) remains purely elastic.
- The entire plastic deformation of the polycrystal is forced to concentrate into the narrow $100\text{ nm}$ PFZ channels.
- Because the PFZ is bounded by rigid elastic grains, immense hydrostatic triaxial tensile stresses develop within the soft boundary layer, causing early microvoid nucleation around grain boundary precipitates at tiny overall macroscopic strains.
</div>
<div class="solution-step">
<strong>Step 3: Degradation of SCC and fracture resistance</strong><br>
1. <em>Intergranular ductile failure:</em> Microvoids nucleating along the boundary coalesce rapidly through the narrow soft PFZ, causing catastrophic intergranular ductile fracture with minimal macroscopic elongation (%EL drops from $15\%$ to $< 3\%$).
2. <em>Stress Corrosion Cracking (SCC):</em> The solute-depleted PFZ and adjacent coarse boundary precipitates create sharp galvanic potential differences ($\Delta V \approx 100\text{--}200\text{ mV}$) in aqueous or saline environments. Combined with concentrated tensile stresses, the PFZ dissolves anodically at an accelerated rate, causing rapid intergranular stress corrosion cracking.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Formed by vacancy annihilation at boundaries during quench and solute draining by coarse boundary precipitates.<br>
Soft PFZ ($\sigma_y = 140\text{ MPa}$) undergoes extreme plastic strain localization while matrix ($520\text{ MPa}$) remains elastic.<br>
Triggers premature intergranular ductile tearing and severe stress corrosion cracking (SCC).
</div>"""
})

# ==========================================
# Problem 43
# ==========================================
add({
    "num": 43,
    "title": "Oxide Dispersion Strengthened (ODS) Alloys vs. Precipitation Hardened Alloys",
    "difficulty": "Medium",
    "category": "Advanced Strengthening",
    "tags": ["ODS Alloys", "Dispersion Strengthening", "Yttria", "High-Temperature Creep"],
    "statement": r"""Precipitation-hardened nickel superalloys derive exceptional strength from coherent $\gamma'$ ($\text{Ni}_3(\text{Al,Ti})$) precipitates. However, above $0.75 T_m$ ($> 900^\circ\text{C}\text{--}1000^\circ\text{C}$), $\gamma'$ precipitates dissolve back into solid solution or coarsen catastrophically, destroying high-temperature strength.
Oxide Dispersion Strengthened (ODS) alloys (e.g., MA754, PM2000) are synthesized via mechanical ball milling to uniformly disperse fine, insoluble oxide particles (such as yttria $\text{Y}_2\text{O}_3$ or $\text{Y-Ti-O}$ nanoclusters) into a metallic matrix.
<br><br>
1. Compare precipitation-hardened alloys and ODS alloys across:
   (a) Chemical nature and solubility of the second phase.<br>
   (b) Interface coherency with the matrix.<br>
   (c) Thermal stability at homologous temperatures $T > 0.8 T_m$.<br>
2. Why can ODS alloys NOT be produced by conventional liquid melting and casting?<br>
3. In ODS alloys at high temperatures, dislocations bypass oxide particles via the <strong>threshold stress mechanism (Arzt-Rösler climb model)</strong>. Explain why an attractive interaction exists between a dislocation and an incoherent oxide particle.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Comparison table</strong><br>
(a) <em>Chemical nature and solubility:</em>
- <em>Precipitation hardening:</em> Second phase is an intermetallic compound ($\text{Ni}_3\text{Al}$, $\text{CuAl}_2$) with significant thermodynamic solubility that dissolves at solution temperatures and coarsens rapidly above $0.6 T_m$.
- <em>ODS alloys:</em> Second phase is a highly refractory ceramic oxide ($\text{Y}_2\text{O}_3$, melting point $\sim 2425^\circ\text{C}$) with virtually zero solubility in solid or liquid metal up to the melting point of the alloy.
(b) <em>Interface coherency:</em>
- <em>Precipitates:</em> Typically coherent or semi-coherent with low interfacial energy.
- <em>Oxide dispersoids:</em> Completely incoherent with high interfacial energy.
(c) <em>Thermal stability:</em>
- <em>Precipitates:</em> Dissolve or coarsen, losing all strength above $850\text{--}950^\circ\text{C}$.
- <em>ODS alloys:</em> Absolutely immune to dissolution and coarsening up to $0.85\text{--}0.90 T_m$ ($> 1150^\circ\text{C}$), providing exceptional creep resistance.
</div>
<div class="solution-step">
<strong>Step 2: Why casting cannot produce ODS alloys</strong><br>
Oxide particles have huge density differences compared to molten metals ($\rho_{\text{Y}_2\text{O}_3} \approx 5.0\text{ g/cm}^3$ vs molten nickel $\approx 8.0\text{ g/cm}^3$) and are not wetted by liquid metal. If mixed into a melt, the ceramic oxide particles immediately agglomerate and float to the surface as slag. ODS alloys must therefore be produced through solid-state <strong>powder metallurgy</strong>: high-energy mechanical attrition milling in ball mills to repeatedly fracture and cold-weld powders, followed by hot isostatic pressing (HIP) and extrusion.
</div>
<div class="solution-step">
<strong>Step 3: Dislocation-particle attractive climb interaction (Arzt model)</strong><br>
Because the oxide/metal interface is incoherent, it cannot sustain localized shear stresses and readily relaxes shear tractions by interfacial diffusion. When a dislocation glides into contact with an oxide particle, the dislocation core partially relaxes its elastic strain energy into the incoherent interface. Consequently, the dislocation is pinned in an attractive potential well at the particle exit side. To detach and continue gliding, a critical <strong>threshold detachment stress</strong> ($\tau_{\text{th}} \approx 0.3\text{--}0.7\,\tau_{\text{Orowan}}$) must be supplied, providing outstanding creep resistance even at very low strain rates.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Precipitates dissolve/coarsen above $0.6 T_m$; ODS oxides ($\text{Y}_2\text{O}_3$) are thermodynamically insoluble and stable up to $0.9 T_m$.<br>
Casting fails due to slag flotation; must be synthesized by solid-state mechanical alloying and HIP.<br>
Threshold creep stress arises from elastic core relaxation at incoherent particle interfaces (Arzt attractive detachment).
</div>"""
})

# ==========================================
# Problem 44
# ==========================================
add({
    "num": 44,
    "title": "Annealing Stages: Recovery, Recrystallization, and Grain Growth",
    "difficulty": "Easy",
    "category": "Annealing Kinetics",
    "tags": ["Annealing", "Recovery", "Recrystallization", "Grain Growth"],
    "statement": r"""A heavily cold-worked metal contains substantial stored mechanical energy ($\approx 1\text{--}5\text{ J/g}$), primarily in the form of elastic strain energy around billions of accumulated dislocations.
Heating the deformed metal (annealing) causes it to revert to an equiaxed, strain-free state through three consecutive stages:
$$\text{Stage 1: Recovery} \longrightarrow \text{Stage 2: Recrystallization} \longrightarrow \text{Stage 3: Grain Growth}$$
<br>
1. Construct a comprehensive table tracking the qualitative change (Increases, Decreases sharply, Remains nearly unchanged) during each of the three stages for:
   (a) Dislocation density $\rho_d$<br>
   (b) Electrical conductivity<br>
   (c) Hardness / Yield strength<br>
   (d) Stored energy release fraction<br>
   (e) Grain shape under optical microscope<br>
2. Which stage releases the majority of the stored deformation energy?<br>
3. In which stage does significant long-range migration of high-angle grain boundaries begin?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Comprehensive Annealing Stage Comparison Table</strong><br>
<table class="data-table">
<thead>
<tr><th>Property / Feature</th><th>Stage 1: Recovery</th><th>Stage 2: Recrystallization</th><th>Stage 3: Grain Growth</th></tr>
</thead>
<tbody>
<tr><td><strong>Dislocation Density ($\rho_d$)</strong></td><td>Decreases slightly ($\sim 10\text{--}30\%$) due to annihilation</td><td><strong>Decreases sharply</strong> ($10^{15} \to 10^{10}\text{ m}^{-2}$, by $10^5\times$)</td><td>Remains very low ($\sim 10^9\text{--}10^{10}\text{ m}^{-2}$)</td></tr>
<tr><td><strong>Electrical Conductivity</strong></td><td><strong>Increases significantly</strong> (point defects annihilated)</td><td>Increases slightly to full annealed baseline</td><td>Remains constant at maximum value</td></tr>
<tr><td><strong>Hardness / Yield Strength</strong></td><td>Remains nearly unchanged (drops $< 10\%$)</td><td><strong>Decreases precipitously</strong> (drops $60\text{--}80\%$)</td><td>Decreases gradually (via Hall-Petch $d^{-1/2}$)</td></tr>
<tr><td><strong>Stored Energy Released</strong></td><td>Releases $5\text{ to }20\%$ of stored energy</td><td><strong>Releases the remaining $80\text{ to }95\%$</strong></td><td>Releases tiny capillary interfacial energy</td></tr>
<tr><td><strong>Grain Structure (Microscope)</strong></td><td>Grains remain elongated/flattened; subgrains form</td><td><strong>New fine, strain-free equiaxed grains</strong> nucleate and consume cold-worked grains</td><td>Equiaxed grains grow larger; mean diameter $d$ increases</td></tr>
</tbody>
</table>
</div>
<div class="solution-step">
<strong>Step 2: Stored energy release</strong><br>
<strong>Stage 2 (Recrystallization)</strong> releases the vast majority ($80\%\text{ to }95\%$) of the stored deformation energy. As new strain-free grains sweep across the deformed matrix, virtually all tangled dislocations and deformation bands are completely wiped out by moving high-angle boundaries.
</div>
<div class="solution-step">
<strong>Step 3: Long-range high-angle grain boundary migration</strong><br>
Long-range migration of high-angle boundaries begins at the onset of <strong>Stage 2 (Recrystallization)</strong>. In Stage 1 (Recovery), only short-range vacancy-assisted dislocation climb and glide occur (polygonization), forming low-angle sub-boundaries without moving original high-angle boundaries. In Stage 2, high-angle boundaries nucleate and migrate over long distances to consume the cold-worked matrix.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Recovery: Annihilates point defects and arranges dislocations into subgrains; restores electrical conductivity without softening.<br>
Recrystallization: New strain-free equiaxed grains form, dropping dislocation density by $10^5\times$, releasing $>85\%$ of stored energy, and restoring ductility.<br>
Grain growth: Driven by grain boundary curvature reduction, coarsening grains and gradually lowering strength.
</div>"""
})

# ==========================================
# Problem 45
# ==========================================
add({
    "num": 45,
    "title": "Recovery Stage: Dislocation Annihilation and Polygonization",
    "difficulty": "Medium",
    "category": "Annealing Kinetics",
    "tags": ["Recovery", "Polygonization", "Dislocation Climb", "Subgrain Boundary"],
    "statement": r"""During the recovery stage of annealing, thermal activation enables stored dislocations to lower their elastic energy without forming new grains.
<br><br>
1. Describe the two primary microscopic dislocation mechanisms operating during recovery:
   (a) Dislocation annihilation.<br>
   (b) Dislocation rearrangement (polygonization).<br>
2. Why is vacancy diffusion essential for the recovery of edge dislocations, while screw dislocations can recover by glide alone?<br>
3. Two parallel edge dislocations of opposite sign ($\mathbf{b}$ and $-\mathbf{b}$) are gliding on slip planes separated by a vertical distance $h = 4.0\text{ nm}$. Under thermal activation at $T = 500\text{ K}$, vacancies diffuse to the extra half-planes. Describe their interaction and state the final result of their mutual climb.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Primary mechanisms during recovery</strong><br>
(a) <strong>Dislocation Annihilation:</strong> Dislocations of opposite sign ($\mathbf{b}$ and $-\mathbf{b}$) gliding on the same slip plane attract each other, meet, and annihilate completely, eliminating their elastic strain fields.<br>
(b) <strong>Polygonization (Subgrain Formation):</strong> When a metal is plastically bent, excess edge dislocations of the same sign accumulate randomly. At recovery temperatures, these edge dislocations climb out of their random slip planes and align themselves into vertical walls. This transforms a continuous crystal curvature into flat, polygon-like crystal blocks separated by planar <strong>low-angle tilt subgrain boundaries</strong>.
</div>
<div class="solution-step">
<strong>Step 2: Role of vacancy diffusion in climb</strong><br>
- <em>Screw dislocations:</em> Screw dislocations have their Burgers vector parallel to their line. They can cross-slip freely from one intersecting slip plane to another by glide alone, without requiring atomic diffusion.<br>
- <em>Edge dislocations:</em> The Burgers vector of an edge dislocation is perpendicular to its line. It cannot change slip planes by glide. Moving out of its slip plane requires <strong>dislocation climb</strong>, which physically requires adding or removing atoms at the edge of the extra half-plane. This process requires the absorption or emission of vacancies, meaning recovery of edge dislocations is strictly rate-controlled by the activation energy of vacancy lattice self-diffusion ($Q_d$).
</div>
<div class="solution-step">
<strong>Step 3: Interaction of opposite-sign edge dislocations separated by $h = 4.0\text{ nm}$</strong><br>
The two opposite edge dislocations exert a mutual elastic attractive force on each other:
- Horizontal glide brings them to a vertical alignment at $x = h = 4.0\text{ nm}$ (a metastable $45^\circ$ configuration).
- At recovery temperatures, vacancy diffusion enables climb: the extra half-plane of the positive dislocation emits vacancies (shrinking downward), while the negative dislocation absorbs vacancies (growing upward).
- As they climb toward each other across distance $h = 4.0\text{ nm}$, they meet and completely <strong>annihilate</strong>, destroying two lattice defects and releasing their combined elastic strain energy ($\Delta E \approx G b^2$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Annihilation destroys opposite dislocations; polygonization aligns like dislocations into vertical low-angle tilt walls.<br>
Edge dislocation climb requires atomic diffusion (vacancy migration), while screw dislocations recover via cross-slip.<br>
Opposite edge dipoles separated by $4\text{ nm}$ climb toward each other and mutually annihilate.
</div>"""
})

# ==========================================
# Problem 46
# ==========================================
add({
    "num": 46,
    "title": "Recrystallization Temperature $T_R$ and Influencing Factors",
    "difficulty": "Easy",
    "category": "Annealing Kinetics",
    "tags": ["Recrystallization Temperature", "Melting Point", "%CW", "Solute Retardation"],
    "statement": r"""The <strong>recrystallization temperature ($T_R$)</strong> is defined as the temperature at which a heavily cold-worked metal complete recrystallizes into strain-free grains within precisely 1 hour.
As an empirical rule of thumb:
$$T_R \approx (0.3\text{ to }0.5)\,T_m \quad (\text{in Kelvin})$$
<br>
1. Calculate the estimated range of $T_R$ (in $^\circ\text{C}$) for:
   (a) Pure lead ($T_m = 327^\circ\text{C}$). Explain why lead cannot be cold worked at room temperature ($20^\circ\text{C}$).<br>
   (b) Pure copper ($T_m = 1085^\circ\text{C}$).<br>
   (c) Pure tungsten ($T_m = 3422^\circ\text{C}$).<br>
2. Explain the effect of the following parameters on $T_R$:
   (a) Increasing the percentage of prior cold work (%CW from $10\%$ to $80\%$).<br>
   (b) Alloy purity (zone-refined high-purity metal vs commercial-purity alloy).<br>
   (c) Annealing heating time (holding for 10 hours instead of 1 hour).<br>
3. What is the minimum critical cold work ($\%CW_{\text{crit}} \approx 2\text{--}5\%$) required for recrystallization to occur?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate $T_R$ ranges in Kelvin and Celsius</strong><br>
(a) <em>Lead:</em> $T_m = 327 + 273.15 = 600.15\text{ K}$.
$$T_R \approx (0.3 \times 600.15) \text{ to } (0.5 \times 600.15) = 180\text{ K to } 300\text{ K} \implies -93^\circ\text{C to } +27^\circ\text{C}$$
For high-purity lead, $T_R \approx 0^\circ\text{C}$. Room temperature ($20^\circ\text{C} = 293\text{ K}$) represents a homologous temperature of $T/T_m = 293/600 \approx 0.49$. Lead recrystallizes spontaneously at room temperature; rolling lead at room temperature is technically <strong>hot working</strong>, so work hardening cannot accumulate!
<br>
(b) <em>Copper:</em> $T_m = 1085 + 273 = 1358\text{ K}$.
$$T_R \approx (0.3 \times 1358) \text{ to } (0.4 \times 1358) = 407\text{ K to } 543\text{ K} \implies 134^\circ\text{C to } 270^\circ\text{C}$$
<br>
(c) <em>Tungsten:</em> $T_m = 3422 + 273 = 3695\text{ K}$.
$$T_R \approx (0.33 \times 3695) \text{ to } (0.45 \times 3695) = 1219\text{ K to } 1663\text{ K} \implies 946^\circ\text{C to } 1390^\circ\text{C}$$
Working tungsten at $800^\circ\text{C}$ is still cold working ($T/T_m \approx 0.29 < T_R$).
</div>
<div class="solution-step">
<strong>Step 2: Influencing parameters</strong><br>
(a) <em>Increasing %CW:</em> <strong>Lowers $T_R$</strong>. Greater cold work stores higher dislocation density, providing a larger thermodynamic driving force ($\Delta G = \rho \frac{1}{2}Gb^2$) for nucleation of new grains.<br>
(b) <em>Alloy purity:</em> <strong>Impurities dramatically raise $T_R$</strong>. Even $0.01\text{ wt}\%$ solute atoms segregate to moving high-angle grain boundaries, exerting a powerful solute drag force that drastically retards boundary mobility.<br>
(c) <em>Annealing time:</em> <strong>Longer time lowers $T_R$</strong>. Recrystallization is a thermally activated kinetic process; extending the holding time allows the same transformation fraction to be achieved at lower temperatures.
</div>
<div class="solution-step">
<strong>Step 3: Critical cold work</strong><br>
Below a critical strain ($\%CW_{\text{crit}} \approx 2\text{--}5\%$), the stored dislocation energy is insufficient to nucleate any new strain-free grains, and recrystallization cannot occur at any temperature. Heating a metal deformed below $\%CW_{\text{crit}}$ produces only recovery or abnormal, monstrous grain growth.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Lead: $T_R \approx 0^\circ\text{C}$ (spontaneously recrystallizes at room temperature; cannot be cold worked).<br>
Copper: $T_R \approx 135\text{--}270^\circ\text{C}$; Tungsten: $T_R \approx 950\text{--}1400^\circ\text{C}$.<br>
$T_R$ decreases with higher %CW and longer time; increases sharply with impurities (solute drag).<br>
Minimum critical deformation: $\%CW_{\text{crit}} \approx 2\text{--}5\%$.
</div>"""
})

# ==========================================
# Problem 47
# ==========================================
add({
    "num": 47,
    "title": "Recrystallization Kinetics: Johnson-Mehl-Avrami-Kolmogorov (JMAK) Equation",
    "difficulty": "Hard",
    "category": "Annealing Kinetics",
    "tags": ["JMAK Equation", "Avrami Kinetics", "Sigmoidal Curve", "Recrystallization Time"],
    "statement": r"""The fraction of recrystallized material $X(t)$ as a function of isothermal annealing time $t$ follows the classical Johnson-Mehl-Avrami-Kolmogorov (JMAK) equation:
$$X(t) = 1 - \exp\left(-k t^n\right)$$
where $k$ is a temperature-dependent rate constant and $n$ is the Avrami exponent.
<br><br>
In an isothermal annealing experiment on cold-rolled brass sheet at $350^\circ\text{C}$:
- The fraction recrystallized is $X_1 = 0.20$ ($20\%$) after $t_1 = 10.0\text{ minutes}$.
- The fraction recrystallized is $X_2 = 0.80$ ($80\%$) after $t_2 = 30.0\text{ minutes}$.
<br>
1. Linearize the JMAK equation into the form $\ln\left(\ln\frac{1}{1 - X}\right) = \ln k + n \ln t$.<br>
2. Calculate the Avrami exponent $n$ and the rate constant $k$ (in $\text{min}^{-n}$).<br>
3. Calculate the time $t_{0.50}$ required to reach $50\%$ recrystallization ($X = 0.50$).<br>
4. Calculate the time $t_{0.99}$ required for virtually complete ($99\%$) recrystallization.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Linearization of JMAK equation</strong><br>
$$1 - X = \exp\left(-k t^n\right)$$
Taking the reciprocal:
$$\frac{1}{1 - X} = \exp\left(k t^n\right)$$
Taking the natural logarithm:
$$\ln\left(\frac{1}{1 - X}\right) = k t^n$$
Taking the natural logarithm a second time:
$$\ln\left[\ln\left(\frac{1}{1 - X}\right)\right] = \ln k + n \ln t$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate Avrami exponent $n$ and rate constant $k$</strong><br>
- <em>For $X_1 = 0.20$ at $t_1 = 10.0\text{ min}$:</em>
$$\ln\left(\frac{1}{1 - 0.20}\right) = \ln\left(\frac{1}{0.80}\right) = \ln(1.25) \approx 0.22314$$
$$Y_1 = \ln(0.22314) \approx -1.49994$$
$$\ln(t_1) = \ln(10.0) \approx 2.30259$$
<br>
- <em>For $X_2 = 0.80$ at $t_2 = 30.0\text{ min}$:</em>
$$\ln\left(\frac{1}{1 - 0.80}\right) = \ln(5.0) \approx 1.60944$$
$$Y_2 = \ln(1.60944) \approx +0.47589$$
$$\ln(t_2) = \ln(30.0) \approx 3.40120$$
<br>
Subtracting the two equations:
$$n = \frac{Y_2 - Y_1}{\ln(t_2) - \ln(t_1)} = \frac{0.47589 - (-1.49994)}{3.40120 - 2.30259} = \frac{1.97583}{1.09861} \approx 1.7985 \approx 1.80$$
Now solve for $k$:
$$\ln k = Y_1 - n \ln(t_1) = -1.49994 - (1.7985 \times 2.30259) = -1.49994 - 4.1412 \approx -5.6411$$
$$k = \exp(-5.6411) \approx 3.549 \times 10^{-3}\text{ min}^{-1.80}$$
</div>
<div class="solution-step">
<strong>Step 3: Time for $50\%$ recrystallization ($t_{0.50}$)</strong><br>
$$\ln\left(\frac{1}{1 - 0.50}\right) = \ln(2.0) \approx 0.69315$$
$$k t_{0.50}^n = 0.69315 \implies t_{0.50}^n = \frac{0.69315}{3.549 \times 10^{-3}} \approx 195.31$$
$$t_{0.50} = (195.31)^{1/1.7985} = (195.31)^{0.5560} \approx 18.78\text{ minutes}$$
</div>
<div class="solution-step">
<strong>Step 4: Time for $99\%$ recrystallization ($t_{0.99}$)</strong><br>
$$\ln\left(\frac{1}{1 - 0.99}\right) = \ln(100) \approx 4.60517$$
$$t_{0.99}^n = \frac{4.60517}{3.549 \times 10^{-3}} \approx 1297.6$$
$$t_{0.99} = (1297.6)^{0.5560} \approx 54.04\text{ minutes}$$
Full recrystallization is accomplished in approximately $54\text{ minutes}$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Avrami exponent $n = 1.80$<br>
Rate constant $k = 3.55 \times 10^{-3}\text{ min}^{-1.80}$<br>
$50\%$ recrystallization time: $t_{0.50} = 18.8\text{ min}$<br>
$99\%$ complete recrystallization time: $t_{0.99} = 54.0\text{ min}$
</div>"""
})

# ==========================================
# Problem 48
# ==========================================
add({
    "num": 48,
    "title": "Normal Grain Growth Kinetics and Temperature Dependence",
    "difficulty": "Medium",
    "category": "Annealing Kinetics",
    "tags": ["Grain Growth", "Kinetics", "Activation Energy", "Grain Boundary Energy"],
    "statement": r"""After primary recrystallization is complete, the grain boundaries continue to migrate slowly to reduce the total grain boundary surface area. This is <strong>normal grain growth</strong>.
The average grain diameter $d$ follows the parabolic growth law:
$$d^n - d_0^n = K t$$
where $d_0$ is the initial grain size at $t = 0$, $n \approx 2$ (ideal theoretical value), and the rate constant is thermally activated:
$$K = K_0 \exp\left(-\frac{Q_{\text{gg}}}{R T}\right)$$
<br>
An annealed brass specimen with initial grain diameter $d_0 = 10.0\text{ }\mu\text{m}$ is held at $600^\circ\text{C}$ ($873\text{ K}$).
Assuming ideal parabolic kinetics ($n = 2$):
- After $t_1 = 15.0\text{ minutes}$, the average grain diameter grows to $d_1 = 28.0\text{ }\mu\text{m}$.
<br>
1. Calculate the rate constant $K$ at $600^\circ\text{C}$ (in $\mu\text{m}^2/\text{min}$ and $\text{m}^2/\text{s}$).<br>
2. Predict the grain size $d_2$ after $t_2 = 120.0\text{ minutes}$ (2 hours) at $600^\circ\text{C}$.<br>
3. The activation energy for grain growth in brass is $Q_{\text{gg}} = 145\text{ kJ/mol}$. Calculate the rate constant $K'$ and the resulting grain size after 2 hours at $700^\circ\text{C}$ ($973\text{ K}$).""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate rate constant $K$ at $600^\circ\text{C}$</strong><br>
From $d^2 - d_0^2 = K t$:
$$d_0^2 = (10.0\text{ }\mu\text{m})^2 = 100.0\text{ }\mu\text{m}^2$$
$$d_1^2 = (28.0\text{ }\mu\text{m})^2 = 784.0\text{ }\mu\text{m}^2$$
$$K = \frac{d_1^2 - d_0^2}{t_1} = \frac{784.0 - 100.0}{15.0\text{ min}} = \frac{684.0}{15.0} = 45.60\text{ }\mu\text{m}^2/\text{min}$$
Convert to $\text{m}^2/\text{s}$:
$$1\text{ }\mu\text{m}^2 = 10^{-12}\text{ m}^2, \quad 1\text{ min} = 60\text{ s}$$
$$K = \frac{45.60 \times 10^{-12}\text{ m}^2}{60\text{ s}} = 7.60 \times 10^{-13}\text{ m}^2/\text{s}$$
</div>
<div class="solution-step">
<strong>Step 2: Grain size after $120\text{ min}$ at $600^\circ\text{C}$</strong><br>
$$d_2^2 = d_0^2 + K t_2 = 100.0 + (45.60 \times 120.0) = 100.0 + 5472.0 = 5572.0\text{ }\mu\text{m}^2$$
$$d_2 = \sqrt{5572.0} \approx 74.65\text{ }\mu\text{m}$$
</div>
<div class="solution-step">
<strong>Step 3: Grain growth at $700^\circ\text{C}$ ($973\text{ K}$)</strong><br>
Using the Arrhenius relation:
$$\frac{K(973)}{K(873)} = \exp\left[-\frac{Q_{\text{gg}}}{R} \left(\frac{1}{973} - \frac{1}{873}\right)\right]$$
$$\frac{1}{973} - \frac{1}{873} = 0.0010277 - 0.0011455 = -0.00011773\text{ K}^{-1}$$
$$-\frac{Q_{\text{gg}}}{R} = -\frac{145,000\text{ J/mol}}{8.314\text{ J}/(\text{mol}\cdot\text{K})} \approx -17,440.46\text{ K}$$
$$\text{Exponent} = (-17,440.46) \times (-0.00011773) \approx +2.0533$$
$$\frac{K(700^\circ\text{C})}{K(600^\circ\text{C})} = \exp(2.0533) \approx 7.7937$$
$$K(700^\circ\text{C}) = 45.60 \times 7.7937 \approx 355.39\text{ }\mu\text{m}^2/\text{min}$$
After $t = 120.0\text{ min}$ at $700^\circ\text{C}$:
$$d^2 = 100.0 + (355.39 \times 120.0) = 100.0 + 42,647 = 42,747\text{ }\mu\text{m}^2$$
$$d = \sqrt{42,747} \approx 206.75\text{ }\mu\text{m}$$
Increasing the temperature by $100^\circ\text{C}$ increases the rate constant by nearly $8\times$, coarsening the grain diameter to nearly $207\text{ }\mu\text{m}$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
At $600^\circ\text{C}$: $K = 45.6\text{ }\mu\text{m}^2/\text{min}$ ($7.60 \times 10^{-13}\text{ m}^2/\text{s}$)<br>
Grain size after 2 h at $600^\circ\text{C}$: $d = 74.7\text{ }\mu\text{m}$<br>
At $700^\circ\text{C}$: $K' = 355.4\text{ }\mu\text{m}^2/\text{min} \implies d = 206.8\text{ }\mu\text{m}$ (massive coarsening).
</div>"""
})

# ==========================================
# Problem 49
# ==========================================
add({
    "num": 49,
    "title": "Abnormal Grain Growth (Secondary Recrystallization) and Goss Texture",
    "difficulty": "Hard",
    "category": "Annealing Kinetics",
    "tags": ["Abnormal Grain Growth", "Secondary Recrystallization", "Goss Texture", "Transformer Steels"],
    "statement": r"""In normal grain growth, all grains grow uniformly with a steady-state monomodal grain size distribution.
Under specific conditions, normal grain growth is completely pinned by fine precipitates (Zener pinning, $d_Z = 4r/3f$).
Upon higher temperature annealing, a few select grains suddenly break free from pinning and consume the entire fine-grained matrix, growing to massive millimeter or centimeter dimensions. This is <strong>abnormal grain growth (secondary recrystallization)</strong>.
<br><br>
1. Contrast normal grain growth and secondary recrystallization regarding driving force, grain size distribution, and kinetics.<br>
2. In grain-oriented electrical steels (Fe-3%Si used in transformer cores), secondary recrystallization is deliberately engineered to produce the <strong>Goss texture $\{110\}\langle 001\rangle$</strong>. Why is the Goss texture of vital technological importance for electrical transformers?<br>
3. How are manganese sulfide ($\text{MnS}$) or aluminum nitride ($\text{AlN}$) inhibitor particles used during hot and cold processing to trigger secondary recrystallization in silicon steel?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Normal grain growth vs. Secondary recrystallization</strong><br>
- <strong>Normal Grain Growth:</strong> Driven by gradual reduction in total grain boundary curvature; grain size distribution remains monomodal and self-similar; kinetics follow continuous parabolic growth ($d \propto t^{1/2}$).
- <strong>Secondary Recrystallization:</strong> Initiates only when normal grain growth is heavily inhibited by second-phase particles (e.g., $\text{MnS}$) or strong texture pinning. When inhibitor particles begin to dissolve or coarsen locally, a tiny fraction of grains with special high-mobility boundaries (often Goss orientation $\{110\}\langle 001\rangle$) break free. Driven by the immense boundary surface energy of the surrounding unrecrystallized fine matrix, these grains grow explosively, creating an extreme bimodal grain size distribution until they consume the entire volume.
</div>
<div class="solution-step">
<strong>Step 2: Technological importance of Goss texture $\{110\}\langle 001\rangle$</strong><br>
BCC iron is magnetically anisotropic: the body edge direction $\langle 100\rangle$ is the <strong>easy magnetization axis</strong> (requiring minimum magnetic field to achieve magnetic saturation and exhibiting minimal magnetic hysteresis loss).
- In electrical transformer cores, alternating AC magnetic flux reverses 50 or 60 times per second.
- The Goss texture aligns the $\{110\}$ plane parallel to the sheet surface and the easy $\langle 001\rangle$ magnetic axis strictly parallel to the rolling direction.
- Stamping transformer laminations along this rolling direction aligns magnetic flux directly with the easy axis, cutting eddy current and hysteresis core losses by up to $70\%$, saving billions of kilowatt-hours of electrical energy worldwide annually.
</div>
<div class="solution-step">
<strong>Step 3: Role of $\text{MnS}$ / $\text{AlN}$ grain growth inhibitors</strong><br>
1. During hot slab reheating at $1400^\circ\text{C}$, $\text{MnS}$ dissolves completely.
2. Controlled hot and cold rolling with intermediate annealing precipitates an ultra-fine, dense dispersion of $\text{MnS}$ or $\text{AlN}$ nanoparticles ($r \approx 10\text{--}20\text{ nm}$).
3. These particles exert strong Zener drag ($F_Z \propto f/r$), completely freezing normal grain growth during primary recrystallization at $800^\circ\text{C}$ and maintaining an ultra-fine matrix ($d \approx 15\text{ }\mu\text{m}$).
4. During final high-temperature box annealing at $1100^\circ\text{C}\text{--}1200^\circ\text{C}$ in pure hydrogen, the inhibitor particles coarsen or dissolve, releasing only the strategically oriented Goss grains to consume the entire matrix, producing gigantic grains ($10\text{--}30\text{ mm}$ across) with $> 95\%$ perfect Goss alignment.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Secondary recrystallization is triggered when Zener pinning halts normal growth, enabling explosive growth of select grains.<br>
Produces $\{110\}\langle 001\rangle$ Goss texture, aligning the easy magnetic axis $\langle 100\rangle$ with the transformer core flux, cutting core energy losses by $70\%$.<br>
$\text{MnS}$/$\text{AlN}$ inhibitors pin normal grain growth until high-temperature annealing triggers abnormal Goss expansion.
</div>"""
})

# ==========================================
# Problem 50
# ==========================================
add({
    "num": 50,
    "title": "Comprehensive Strengthening Mechanism Superposition Design",
    "difficulty": "Hard",
    "category": "Strengthening Superposition",
    "tags": ["Strengthening Superposition", "Alloy Design", "Yield Strength", "Comprehensive"],
    "statement": r"""Modern engineering alloys achieve superior yield strength by simultaneously combining all four fundamental strengthening mechanisms:
1. Lattice friction stress ($\sigma_0$)
2. Solid solution strengthening ($\Delta\sigma_{\text{ss}}$)
3. Grain boundary refinement ($\Delta\sigma_{\text{gb}} = k_y d^{-1/2}$)
4. Dislocation strain hardening ($\Delta\sigma_d = \bar{M}\alpha G b \sqrt{\rho_d}$)
5. Precipitation hardening ($\Delta\sigma_p$)
<br>
When combining mechanisms of differing physical nature, the total yield strength $\sigma_y$ is determined by the linear/Pythagorean superposition law:
$$\sigma_y = \sigma_0 + \Delta\sigma_{\text{ss}} + \Delta\sigma_{\text{gb}} + \sqrt{(\Delta\sigma_d)^2 + (\Delta\sigma_p)^2}$$
where short-range obstacle mechanisms ($\Delta\sigma_d$ and $\Delta\sigma_p$) superimpose root-sum-of-squares, while long-range and friction mechanisms add linearly.
<br><br>
A microalloyed HSLA engineering steel has:
- Base lattice friction: $\sigma_0 = 70.0\text{ MPa}$
- Solid solution contribution from Mn and Si: $\Delta\sigma_{\text{ss}} = 85.0\text{ MPa}$
- Hall-Petch slope $k_y = 0.50\text{ MPa}\cdot\text{m}^{1/2}$ with grain size refined to $d = 4.0\text{ }\mu\text{m}$
- Dislocation density $\rho_d = 1.0 \times 10^{14}\text{ m}^{-2}$ ($G = 80\text{ GPa}$, $b = 0.248\text{ nm}$, $\alpha = 0.30$, $\bar{M} = 3.06$)
- Fine dispersion of coherent $\text{NbC}$ precipitates providing $\Delta\sigma_p = 160.0\text{ MPa}$
<br><br>
1. Calculate the grain boundary strengthening increment $\Delta\sigma_{\text{gb}}$.<br>
2. Calculate the dislocation strain hardening increment $\Delta\sigma_d$.<br>
3. Calculate the combined obstacle strength $\Delta\sigma_{\text{obs}} = \sqrt{(\Delta\sigma_d)^2 + (\Delta\sigma_p)^2}$.<br>
4. Calculate the total yield strength $\sigma_y$ of this engineered alloy.<br>
5. By what factor is the final yield strength higher than the pure iron base friction stress $\sigma_0$?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate grain boundary strengthening increment $\Delta\sigma_{\text{gb}}$</strong><br>
Given: $k_y = 0.50\text{ MPa}\cdot\text{m}^{1/2}$, $d = 4.0 \times 10^{-6}\text{ m}$:
$$d^{-1/2} = (4.0 \times 10^{-6})^{-0.5} = \frac{10^3}{\sqrt{4.0}} = \frac{1000}{2.0} = 500.0\text{ m}^{-1/2}$$
$$\Delta\sigma_{\text{gb}} = k_y d^{-1/2} = (0.50\text{ MPa}\cdot\text{m}^{1/2}) \times (500.0\text{ m}^{-1/2}) = 250.0\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate dislocation strain hardening increment $\Delta\sigma_d$</strong><br>
$$\sqrt{\rho_d} = \sqrt{1.0 \times 10^{14}} = 1.0 \times 10^7\text{ m}^{-1}$$
$$\Delta\tau_d = \alpha G b \sqrt{\rho_d} = 0.30 \times (80 \times 10^9\text{ Pa}) \times (0.248 \times 10^{-9}\text{ m}) \times (1.0 \times 10^7\text{ m}^{-1})$$
$$\Delta\tau_d = (5.952\text{ N}) \times (1.0 \times 10^7\text{ m}^{-1}) = 5.952 \times 10^7\text{ Pa} \approx 59.52\text{ MPa}$$
Macroscopic tensile increment:
$$\Delta\sigma_d = \bar{M} \Delta\tau_d = 3.06 \times 59.52\text{ MPa} \approx 182.13\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Calculate combined obstacle strength $\Delta\sigma_{\text{obs}}$</strong><br>
Given $\Delta\sigma_p = 160.0\text{ MPa}$ and $\Delta\sigma_d = 182.13\text{ MPa}$:
$$\Delta\sigma_{\text{obs}} = \sqrt{(\Delta\sigma_d)^2 + (\Delta\sigma_p)^2} = \sqrt{(182.13)^2 + (160.0)^2}$$
$$(182.13)^2 = 33,171.3\text{ MPa}^2$$
$$(160.0)^2 = 25,600.0\text{ MPa}^2$$
$$\Delta\sigma_{\text{obs}} = \sqrt{33,171.3 + 25,600.0} = \sqrt{58,771.3} \approx 242.43\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: Calculate total alloy yield strength $\sigma_y$</strong><br>
$$\sigma_y = \sigma_0 + \Delta\sigma_{\text{ss}} + \Delta\sigma_{\text{gb}} + \Delta\sigma_{\text{obs}}$$
$$\sigma_y = 70.0 + 85.0 + 250.0 + 242.43 = 647.43\text{ MPa}$$
Rounding to standard engineering precision:
$$\sigma_y \approx 647.4\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 5: Strengthening enhancement factor</strong><br>
$$\frac{\sigma_y}{\sigma_0} = \frac{647.43\text{ MPa}}{70.0\text{ MPa}} \approx 9.25$$
By intelligently combining solid solution ($85\text{ MPa}$), grain refinement ($250\text{ MPa}$), dislocation forest hardening ($182\text{ MPa}$), and $\text{NbC}$ precipitation ($160\text{ MPa}$), the yield strength of the steel is amplified by over <strong>$9.25\times$</strong> above the intrinsic lattice resistance of iron.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\Delta\sigma_{\text{gb}} = 250.0\text{ MPa}$ (Grain refinement)<br>
$\Delta\sigma_d = 182.1\text{ MPa}$ (Work hardening)<br>
Combined obstacle stress $\Delta\sigma_{\text{obs}} = 242.4\text{ MPa}$<br>
Total engineered yield strength: $\sigma_y = 647.4\text{ MPa}$ ($9.25\times$ base iron strength).
</div>"""
})

if __name__ == "__main__":
    print(f"Total problems in P: {len(P)}")
    # Write to ch7_data.py
    out_path = os.path.join(os.path.dirname(__file__), "ch7_data.py")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Chapter 7 Problem Dataset (Dislocations & Strengthening Mechanisms - 50 Problems)\n")
        f.write("PROBLEMS = [\n")
        for p in P:
            f.write("    {\n")
            f.write(f'        "number": {p["number"]},\n')
            f.write(f'        "title": {repr(p["title"])},\n')
            f.write(f'        "category": {repr(p["category"])},\n')
            f.write(f'        "category_slug": {repr(p["category_slug"])},\n')
            f.write(f'        "difficulty": {repr(p["difficulty"])},\n')
            f.write(f'        "statement": {repr(p["statement"])},\n')
            f.write(f'        "solution": {repr(p["solution"])}\n')
            f.write("    },\n")
        f.write("]\n")
    print(f"Successfully generated {out_path} with {len(P)} problems!")
