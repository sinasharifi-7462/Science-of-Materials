# generator/make_ch6_part2.py
import sys
import os
import re

# Import Part 1
import make_ch6_part1

P = list(make_ch6_part1.P)

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
    "title": "Plane Stress Transformation and Principal Planes",
    "difficulty": "Medium",
    "category": "Multiaxial Stress",
    "tags": ["Stress Transformation", "Principal Stress", "Mohr's Circle"],
    "statement": r"""A critical element on the surface of a titanium alloy bracket in an aircraft wing spar is subjected to plane stress conditions with $\sigma_x = 180\text{ MPa}$, $\sigma_y = -60\text{ MPa}$, and $\tau_{xy} = 80\text{ MPa}$.
<br><br>
1. Calculate the orientations of the principal stress planes $\theta_{p1}$ and $\theta_{p2}$.<br>
2. Determine the maximum and minimum in-plane principal stresses $\sigma_1$ and $\sigma_2$.<br>
3. Find the maximum in-plane shear stress $\tau_{\text{max, in-plane}}$ and the orientation of the planes on which it acts.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Orientations of the principal stress planes</strong><br>
The angle of the principal planes $\theta_p$ is given by:
$$\tan(2\theta_p) = \frac{2\tau_{xy}}{\sigma_x - \sigma_y} = \frac{2(80)}{180 - (-60)} = \frac{160}{240} = \frac{2}{3} \approx 0.6667$$
$$2\theta_p = \arctan(0.6667) \approx 33.69^\circ \implies \theta_{p1} = 16.85^\circ$$
The second principal plane is orthogonal:
$$\theta_{p2} = \theta_{p1} + 90^\circ = 106.85^\circ \quad (\text{or } -73.15^\circ)$$
</div>
<div class="solution-step">
<strong>Step 2: Principal stresses $\sigma_1$ and $\sigma_2$</strong><br>
The principal stresses are calculated from:
$$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$
$$\sigma_{\text{avg}} = \frac{180 + (-60)}{2} = 60\text{ MPa}$$
$$R = \sqrt{\left(\frac{180 - (-60)}{2}\right)^2 + 80^2} = \sqrt{120^2 + 80^2} = \sqrt{14400 + 6400} = \sqrt{20800} \approx 144.22\text{ MPa}$$
$$\sigma_1 = 60 + 144.22 = 204.22\text{ MPa}$$
$$\sigma_2 = 60 - 144.22 = -84.22\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Maximum in-plane shear stress</strong><br>
The maximum in-plane shear stress equals the radius of Mohr's circle:
$$\tau_{\text{max, in-plane}} = R = \frac{\sigma_1 - \sigma_2}{2} = \frac{204.22 - (-84.22)}{2} = 144.22\text{ MPa}$$
The planes of maximum shear stress are oriented at $45^\circ$ to the principal planes:
$$\theta_s = \theta_{p1} \pm 45^\circ = 16.85^\circ \pm 45^\circ \implies \theta_{s1} = 61.85^\circ, \quad \theta_{s2} = -28.15^\circ$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\theta_{p1} = 16.85^\circ$, $\theta_{p2} = 106.85^\circ$<br>
$\sigma_1 = 204.2\text{ MPa}$, $\sigma_2 = -84.2\text{ MPa}$<br>
$\tau_{\text{max, in-plane}} = 144.2\text{ MPa}$ at $\theta_s = 61.85^\circ, -28.15^\circ$
</div>"""
})

# ==========================================
# Problem 27
# ==========================================
add({
    "num": 27,
    "title": "Mohr's Circle and Absolute Maximum Shear Stress",
    "difficulty": "Medium",
    "category": "Multiaxial Stress",
    "tags": ["Mohr's Circle", "Absolute Max Shear", "3D Stress State"],
    "statement": r"""A machine component made of ductile structural steel is subjected to biaxial tensile stresses in plane stress ($\sigma_z = 0$): $\sigma_x = 240\text{ MPa}$, $\sigma_y = 100\text{ MPa}$, and $\tau_{xy} = 0\text{ MPa}$.
<br><br>
1. Identify the three principal stresses $\sigma_1, \sigma_2, \sigma_3$.<br>
2. Determine the maximum in-plane shear stress $\tau_{\text{max, in-plane}}$.<br>
3. Construct the 3D Mohr's circle representation and determine the absolute maximum shear stress $\tau_{\text{abs, max}}$. Explain why $\tau_{\text{abs, max}} \neq \tau_{\text{max, in-plane}}$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Identify the three principal stresses</strong><br>
Since the shear stress on the $x\text{-}y$ plane is zero, the normal stresses $\sigma_x$ and $\sigma_y$ are already principal stresses. Including the out-of-plane stress for plane stress ($\sigma_z = 0$):
$$\sigma_1 = 240\text{ MPa}, \quad \sigma_2 = 100\text{ MPa}, \quad \sigma_3 = 0\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Maximum in-plane shear stress</strong><br>
The in-plane shear stress considers only the circle between $\sigma_1$ and $\sigma_2$:
$$\tau_{\text{max, in-plane}} = \frac{\sigma_1 - \sigma_2}{2} = \frac{240 - 100}{2} = 70\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: 3D Mohr's circle and absolute maximum shear stress</strong><br>
The 3D state of stress is represented by three Mohr's circles drawn between the pairs $(\sigma_1, \sigma_2)$, $(\sigma_2, \sigma_3)$, and $(\sigma_1, \sigma_3)$. The largest circle spans between the algebraically greatest stress $\sigma_1$ and smallest stress $\sigma_3$:
$$\tau_{\text{abs, max}} = \frac{\sigma_1 - \sigma_3}{2} = \frac{240 - 0}{2} = 120\text{ MPa}$$
<em>Explanation:</em> When both in-plane principal stresses are of the same sign (both tensile here), the zero out-of-plane principal stress ($\sigma_3 = 0$) lies outside the interval $[\sigma_2, \sigma_1]$. Thus, the critical shear planes are inclined at $45^\circ$ to the $x$ and $z$ axes, making $\tau_{\text{abs, max}}$ significantly larger than the in-plane value ($120\text{ MPa}$ vs $70\text{ MPa}$). Ignoring the third dimension would drastically underestimate the risk of plastic shear yielding.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\sigma_1 = 240\text{ MPa}$, $\sigma_2 = 100\text{ MPa}$, $\sigma_3 = 0\text{ MPa}$<br>
$\tau_{\text{max, in-plane}} = 70\text{ MPa}$<br>
$\tau_{\text{abs, max}} = 120\text{ MPa}$ (acts on planes rotated $45^\circ$ out of the sheet surface)
</div>"""
})

# ==========================================
# Problem 28
# ==========================================
add({
    "num": 28,
    "title": "Tresca Yield Criterion (Maximum Shear Stress Theory)",
    "difficulty": "Medium",
    "category": "Yield Criteria",
    "tags": ["Tresca", "Yield Criterion", "Multiaxial Yielding"],
    "statement": r"""A pressure hull made of high-strength alloy steel with a uniaxial yield strength of $\sigma_y = 650\text{ MPa}$ is subjected to a triaxial stress state: $\sigma_1 = 450\text{ MPa}$, $\sigma_2 = 200\text{ MPa}$, and $\sigma_3 = -280\text{ MPa}$.
<br><br>
1. State the Tresca yield criterion mathematically in terms of principal stresses and uniaxial yield strength $\sigma_y$.<br>
2. Calculate the maximum shear stress $\tau_{\text{max}}$ in the material.<br>
3. Determine whether the component will undergo plastic yielding according to the Tresca criterion. If not, calculate the factor of safety $N_{\text{Tresca}}$ against yielding.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Statement of the Tresca criterion</strong><br>
The Tresca (Maximum Shear Stress) criterion postulates that yielding initiates when the absolute maximum shear stress in a multiaxial stress state reaches the maximum shear stress at yielding in a uniaxial tension test:
$$\tau_{\text{max}} = \frac{\sigma_1 - \sigma_3}{2} \ge \tau_y = \frac{\sigma_y}{2} \iff \sigma_1 - \sigma_3 \ge \sigma_y$$
where $\sigma_1 \ge \sigma_2 \ge \sigma_3$.
</div>
<div class="solution-step">
<strong>Step 2: Maximum shear stress calculation</strong><br>
Given $\sigma_1 = 450\text{ MPa}$, $\sigma_2 = 200\text{ MPa}$, $\sigma_3 = -280\text{ MPa}$:
$$\tau_{\text{max}} = \frac{450 - (-280)}{2} = \frac{730}{2} = 365\text{ MPa}$$
The equivalent Tresca stress is:
$$\sigma_{\text{Tresca}} = \sigma_1 - \sigma_3 = 730\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Yield assessment and factor of safety</strong><br>
Comparing the equivalent stress to the uniaxial yield strength:
$$\sigma_{\text{Tresca}} = 730\text{ MPa} > \sigma_y = 650\text{ MPa}$$
$$\tau_{\text{max}} = 365\text{ MPa} > \tau_y = \frac{650}{2} = 325\text{ MPa}$$
The material <strong>will undergo plastic yielding</strong> because the stress exceeds the yield threshold.<br>
The factor of safety is:
$$N_{\text{Tresca}} = \frac{\sigma_y}{\sigma_1 - \sigma_3} = \frac{650}{730} \approx 0.890 \quad (< 1.0 \implies \text{failed/yielded})$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\tau_{\text{max}} = 365\text{ MPa}$, $\sigma_{\text{Tresca}} = 730\text{ MPa}$<br>
$\sigma_{\text{Tresca}} > \sigma_y$ ($730\text{ MPa} > 650\text{ MPa}$) $\implies$ <strong>Yielding will occur</strong> ($N = 0.89$)
</div>"""
})

# ==========================================
# Problem 29
# ==========================================
add({
    "num": 29,
    "title": "von Mises Yield Criterion (Distortion Energy Theory)",
    "difficulty": "Medium",
    "category": "Yield Criteria",
    "tags": ["von Mises", "Distortion Energy", "Equivalent Stress"],
    "statement": r"""For the same stress state as in the previous problem ($\sigma_1 = 450\text{ MPa}$, $\sigma_2 = 200\text{ MPa}$, $\sigma_3 = -280\text{ MPa}$, and $\sigma_y = 650\text{ MPa}$):
<br><br>
1. Calculate the von Mises equivalent stress $\sigma_{\text{vM}}$ (effective stress).<br>
2. Determine whether yielding is predicted according to the von Mises criterion.<br>
3. Calculate the factor of safety $N_{\text{vM}}$ and compare it with the Tresca factor of safety $N_{\text{Tresca}} = 0.890$. Explain why the von Mises criterion predicts a higher safety margin than Tresca.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate the von Mises equivalent stress</strong><br>
The von Mises equivalent stress is defined as:
$$\sigma_{\text{vM}} = \frac{1}{\sqrt{2}}\sqrt{(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}$$
Substitute the given principal stresses:
$$\sigma_1 - \sigma_2 = 450 - 200 = 250\text{ MPa} \implies (250)^2 = 62,500\text{ MPa}^2$$
$$\sigma_2 - \sigma_3 = 200 - (-280) = 480\text{ MPa} \implies (480)^2 = 230,400\text{ MPa}^2$$
$$\sigma_3 - \sigma_1 = -280 - 450 = -730\text{ MPa} \implies (-730)^2 = 532,900\text{ MPa}^2$$
Sum of squared differences:
$$\sum (\Delta \sigma)^2 = 62,500 + 230,400 + 532,900 = 825,800\text{ MPa}^2$$
$$\sigma_{\text{vM}} = \sqrt{\frac{825,800}{2}} = \sqrt{412,900} \approx 642.57\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Yield assessment</strong><br>
Comparing $\sigma_{\text{vM}}$ to $\sigma_y$:
$$\sigma_{\text{vM}} = 642.6\text{ MPa} < \sigma_y = 650\text{ MPa}$$
Remarkably, according to the von Mises criterion, the material <strong>remains elastic and does NOT yield</strong>!
</div>
<div class="solution-step">
<strong>Step 3: Factor of safety and comparison</strong><br>
$$N_{\text{vM}} = \frac{\sigma_y}{\sigma_{\text{vM}}} = \frac{650}{642.57} \approx 1.012$$
<em>Physical explanation:</em> The Tresca hexagon is entirely inscribed within the smooth von Mises ellipse on the $\pi$-plane (deviatoric plane). Tresca depends solely on the extreme principal stresses $(\sigma_1 - \sigma_3)$ and completely ignores the intermediate principal stress $\sigma_2$. In contrast, von Mises accounts for shear distortions along all octahedral planes, where an intermediate stress $\sigma_2$ between $\sigma_1$ and $\sigma_3$ provides constraint that lowers the distortion energy relative to the maximum shear stress. Thus, Tresca is always more conservative than von Mises by up to $\sim 15.5\%$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\sigma_{\text{vM}} = 642.6\text{ MPa}$<br>
Since $\sigma_{\text{vM}} < \sigma_y$ ($642.6 < 650\text{ MPa}$), <strong>yielding does NOT occur</strong> under von Mises ($N_{\text{vM}} = 1.01$).<br>
Tresca predicts yielding ($N = 0.89$) while von Mises predicts safety ($N = 1.01$).
</div>"""
})

# ==========================================
# Problem 30
# ==========================================
add({
    "num": 30,
    "title": "Pure Shear Yielding: Tresca vs. von Mises",
    "difficulty": "Easy",
    "category": "Yield Criteria",
    "tags": ["Pure Shear", "Torsion", "Tresca vs von Mises"],
    "statement": r"""A solid torsion bar is subjected to pure torsional shear stress $\tau$. The material has a tensile yield strength of $\sigma_y = 300\text{ MPa}$.
<br><br>
1. Express the principal stresses $(\sigma_1, \sigma_2, \sigma_3)$ in terms of the applied shear stress $\tau$.<br>
2. Derive the shear yield strength $k_{\text{Tresca}}$ predicted by the Tresca criterion and calculate its numerical value.<br>
3. Derive the shear yield strength $k_{\text{vM}}$ predicted by the von Mises criterion and calculate its numerical value.<br>
4. Find the percentage difference between the two predictions.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Principal stresses in pure shear</strong><br>
In pure shear on the surface of a torsion bar:
$$\sigma_x = 0, \quad \sigma_y = 0, \quad \tau_{xy} = \tau$$
The principal stresses are:
$$\sigma_1 = \tau, \quad \sigma_2 = 0, \quad \sigma_3 = -\tau$$
</div>
<div class="solution-step">
<strong>Step 2: Tresca shear yield strength</strong><br>
According to Tresca:
$$\sigma_1 - \sigma_3 = \tau - (-\tau) = 2\tau = \sigma_y \implies k_{\text{Tresca}} = \frac{\sigma_y}{2} = 0.500\,\sigma_y$$
Numerical value:
$$k_{\text{Tresca}} = 0.500 \times 300\text{ MPa} = 150.0\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: von Mises shear yield strength</strong><br>
According to von Mises:
$$\sigma_{\text{vM}} = \frac{1}{\sqrt{2}}\sqrt{(\tau - 0)^2 + (0 - (-\tau))^2 + (-\tau - \tau)^2} = \frac{1}{\sqrt{2}}\sqrt{\tau^2 + \tau^2 + 4\tau^2} = \frac{1}{\sqrt{2}}\sqrt{6\tau^2} = \sqrt{3}\,\tau$$
Setting $\sigma_{\text{vM}} = \sigma_y$:
$$\sqrt{3}\,\tau_y = \sigma_y \implies k_{\text{vM}} = \frac{\sigma_y}{\sqrt{3}} \approx 0.5774\,\sigma_y$$
Numerical value:
$$k_{\text{vM}} = \frac{300}{\sqrt{3}} \approx 173.2\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: Percentage difference</strong><br>
$$\Delta = \frac{k_{\text{vM}} - k_{\text{Tresca}}}{k_{\text{Tresca}}} \times 100\% = \frac{173.2 - 150.0}{150.0} \times 100\% = \left(\frac{2}{\sqrt{3}} - 1\right) \times 100\% \approx 15.47\%$$
von Mises predicts a shear yield strength that is $15.5\%$ higher than Tresca's estimate.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$k_{\text{Tresca}} = \sigma_y/2 = 150.0\text{ MPa}$<br>
$k_{\text{vM}} = \sigma_y/\sqrt{3} = 173.2\text{ MPa}$<br>
Difference: von Mises is $15.5\%$ less conservative than Tresca in pure shear.
</div>"""
})

# ==========================================
# Problem 31
# ==========================================
add({
    "num": 31,
    "title": "Yielding of Thin-Walled Cylindrical Pressure Vessel",
    "difficulty": "Hard",
    "category": "Multiaxial Stress",
    "tags": ["Pressure Vessel", "Cylindrical Shell", "von Mises Yield"],
    "statement": r"""A thin-walled cylindrical gas storage cylinder has an internal diameter $d = 500\text{ mm}$ (radius $r = 250\text{ mm}$) and wall thickness $t = 5.0\text{ mm}$. It is fabricated from an aluminum alloy with yield strength $\sigma_y = 280\text{ MPa}$.
<br><br>
1. Express the circumferential (hoop) stress $\sigma_\theta$, axial (longitudinal) stress $\sigma_z$, and radial stress $\sigma_r$ as functions of internal gauge pressure $p$.<br>
2. Determine the maximum permissible internal pressure $p_{\text{max, Tresca}}$ before yielding starts according to the Tresca criterion.<br>
3. Determine the maximum permissible internal pressure $p_{\text{max, vM}}$ according to the von Mises criterion.<br>
4. Calculate the ratio $p_{\text{max, vM}} / p_{\text{max, Tresca}}$. What does this demonstrate about cylindrical geometry?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Stresses in terms of internal pressure $p$</strong><br>
For a thin-walled cylinder ($r/t = 250/5 = 50 \gg 10$):
$$\text{Hoop stress: } \sigma_\theta = \frac{p r}{t} = \frac{250}{5} p = 50 p$$
$$\text{Axial stress: } \sigma_z = \frac{p r}{2t} = \frac{250}{10} p = 25 p = 0.5 \sigma_\theta$$
$$\text{Radial stress: } \sigma_r \approx 0 \text{ (on outer surface; reaches }-p\text{ on inner surface, negligible compared to }50p)$$
Ordering the principal stresses:
$$\sigma_1 = \sigma_\theta = 50p, \quad \sigma_2 = \sigma_z = 25p, \quad \sigma_3 = \sigma_r = 0$$
</div>
<div class="solution-step">
<strong>Step 2: Maximum pressure by Tresca criterion</strong><br>
Tresca yield condition:
$$\sigma_1 - \sigma_3 = \sigma_\theta - 0 = 50p = \sigma_y = 280\text{ MPa}$$
$$p_{\text{max, Tresca}} = \frac{280}{50} = 5.60\text{ MPa} = 56.0\text{ bar}$$
</div>
<div class="solution-step">
<strong>Step 3: Maximum pressure by von Mises criterion</strong><br>
$$\sigma_{\text{vM}} = \frac{1}{\sqrt{2}}\sqrt{(\sigma_\theta - \sigma_z)^2 + (\sigma_z - 0)^2 + (0 - \sigma_\theta)^2}$$
Substitute $\sigma_z = 0.5 \sigma_\theta$:
$$\sigma_{\text{vM}} = \frac{1}{\sqrt{2}}\sqrt{(0.5\sigma_\theta)^2 + (0.5\sigma_\theta)^2 + (-\sigma_\theta)^2} = \frac{1}{\sqrt{2}}\sqrt{0.25 + 0.25 + 1}\,\sigma_\theta = \frac{\sqrt{1.5}}{\sqrt{2}}\,\sigma_\theta = \frac{\sqrt{3}}{2}\,\sigma_\theta$$
Setting $\sigma_{\text{vM}} = \sigma_y$:
$$\frac{\sqrt{3}}{2} (50 p) = 280 \implies 25\sqrt{3}\,p = 280 \implies p_{\text{max, vM}} = \frac{280}{25\sqrt{3}} \approx 6.466\text{ MPa} = 64.66\text{ bar}$$
</div>
<div class="solution-step">
<strong>Step 4: Ratio and geometric implication</strong><br>
$$\frac{p_{\text{max, vM}}}{p_{\text{max, Tresca}}} = \frac{2}{\sqrt{3}} \approx 1.155$$
This demonstrates that under 2:1 biaxial tension (the natural stress state of a closed cylinder), the von Mises yield criterion allows <strong>$15.5\%$ higher operating pressure</strong> than Tresca. This is the exact maximum divergence possible between the two criteria!
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$p_{\text{max, Tresca}} = 5.60\text{ MPa}$ ($56.0\text{ bar}$)<br>
$p_{\text{max, vM}} = 6.47\text{ MPa}$ ($64.7\text{ bar}$)<br>
Ratio $= 2/\sqrt{3} = 1.155$ ($15.5\%$ higher load capacity predicted by von Mises).
</div>"""
})

# ==========================================
# Problem 32
# ==========================================
add({
    "num": 32,
    "title": "Yielding of Spherical Pressure Vessel and Equi-Biaxial Tension",
    "difficulty": "Easy",
    "category": "Multiaxial Stress",
    "tags": ["Spherical Vessel", "Equi-Biaxial", "Hydrostatic"],
    "statement": r"""A spherical titanium alloy pressure vessel has an internal radius $r = 200\text{ mm}$ and wall thickness $t = 4.0\text{ mm}$. The tensile yield strength is $\sigma_y = 900\text{ MPa}$.
<br><br>
1. Determine the membrane stresses $\sigma_1, \sigma_2, \sigma_3$ in terms of internal pressure $p$.<br>
2. Calculate the yield pressure $p_y$ predicted by the Tresca criterion.<br>
3. Calculate the yield pressure $p_y$ predicted by the von Mises criterion.<br>
4. Explain why both criteria give the exact same yield pressure in this specific loading case.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Membrane stresses in a thin spherical shell</strong><br>
Due to spherical symmetry, the membrane stresses in any orthogonal tangential directions are identical:
$$\sigma_1 = \sigma_2 = \sigma = \frac{p r}{2t} = \frac{200}{2(4)} p = 25 p$$
The through-thickness radial stress on the outer surface is $\sigma_3 = 0$.
</div>
<div class="solution-step">
<strong>Step 2: Yield pressure by Tresca</strong><br>
$$\sigma_1 - \sigma_3 = 25p - 0 = 25p = \sigma_y = 900\text{ MPa}$$
$$p_{\text{Tresca}} = \frac{900}{25} = 36.0\text{ MPa} = 360\text{ bar}$$
</div>
<div class="solution-step">
<strong>Step 3: Yield pressure by von Mises</strong><br>
$$\sigma_{\text{vM}} = \frac{1}{\sqrt{2}}\sqrt{(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}$$
Since $\sigma_1 = \sigma_2 = \sigma$:
$$\sigma_{\text{vM}} = \frac{1}{\sqrt{2}}\sqrt{0 + (\sigma - 0)^2 + (0 - \sigma)^2} = \frac{1}{\sqrt{2}}\sqrt{2\sigma^2} = \sigma$$
Setting $\sigma_{\text{vM}} = \sigma = 25p = \sigma_y = 900\text{ MPa}$:
$$p_{\text{vM}} = \frac{900}{25} = 36.0\text{ MPa} = 360\text{ bar}$$
</div>
<div class="solution-step">
<strong>Step 4: Why both criteria coincide</strong><br>
Under equi-biaxial plane stress ($\sigma_1 = \sigma_2 = \sigma$ and $\sigma_3 = 0$), the stress state corresponds to the corner points of the Tresca hexagon where it touches the von Mises ellipse. Because $\sigma_1 - \sigma_2 = 0$, there is no distortion in the tangential plane; yielding is governed entirely by shear on planes inclined at $45^\circ$ through the thickness $(\sigma_1 - \sigma_3)$, for which both criteria yield the identical condition $\sigma = \sigma_y$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$p_{\text{Tresca}} = p_{\text{vM}} = 36.0\text{ MPa}$ ($360\text{ bar}$)<br>
Both criteria predict identical yield pressures because the equi-biaxial stress state lies on the intersection of the Tresca hexagon and von Mises ellipse.
</div>"""
})

# ==========================================
# Problem 33
# ==========================================
add({
    "num": 33,
    "title": "Combined Bending and Torsion in a Drive Shaft",
    "difficulty": "Hard",
    "category": "Multiaxial Stress",
    "tags": ["Drive Shaft", "Combined Loading", "von Mises"],
    "statement": r"""A solid circular power transmission shaft with diameter $d = 60\text{ mm}$ (radius $c = 30\text{ mm}$) transmits a torque $T = 3.5\text{ kN}\cdot\text{m}$ while simultaneously supporting a transverse bending moment $M = 2.4\text{ kN}\cdot\text{m}$. The shaft is forged from 4340 steel with yield strength $\sigma_y = 850\text{ MPa}$.
<br><br>
1. Calculate the maximum bending stress $\sigma_b$ and torsional shear stress $\tau_t$ on the outer surface.<br>
2. Calculate the equivalent von Mises stress $\sigma_{\text{vM}}$ at the most critically loaded surface point.<br>
3. Calculate the factor of safety against yielding according to the von Mises criterion.<br>
4. Calculate the factor of safety according to the Tresca criterion.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate surface bending stress and shear stress</strong><br>
Polar moment of inertia $J$ and bending moment of inertia $I$:
$$I = \frac{\pi d^4}{64} = \frac{\pi (0.060)^4}{64} \approx 6.3617 \times 10^{-7}\text{ m}^4$$
$$J = 2I = \frac{\pi d^4}{32} \approx 1.2723 \times 10^{-6}\text{ m}^4$$
Bending stress at the extreme outer fiber ($y = c = 0.030\text{ m}$):
$$\sigma_b = \frac{M c}{I} = \frac{32 M}{\pi d^3} = \frac{32(2400)}{\pi (0.060)^3} \approx 113.18\text{ MPa}$$
Torsional shear stress at the outer surface:
$$\tau_t = \frac{T c}{J} = \frac{16 T}{\pi d^3} = \frac{16(3500)}{\pi (0.060)^3} \approx 82.52\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate von Mises equivalent stress</strong><br>
For plane stress with normal stress $\sigma_x = \sigma_b$, $\sigma_y = 0$, and $\tau_{xy} = \tau_t$:
$$\sigma_{\text{vM}} = \sqrt{\sigma_x^2 + 3\tau_{xy}^2} = \sqrt{(113.18)^2 + 3(82.52)^2}$$
$$(113.18)^2 = 12,810\text{ MPa}^2$$
$$3 \times (82.52)^2 = 3 \times 6,810 = 20,430\text{ MPa}^2$$
$$\sigma_{\text{vM}} = \sqrt{12,810 + 20,430} = \sqrt{33,240} \approx 182.32\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Factor of safety by von Mises</strong><br>
$$N_{\text{vM}} = \frac{\sigma_y}{\sigma_{\text{vM}}} = \frac{850}{182.32} \approx 4.66$$
</div>
<div class="solution-step">
<strong>Step 4: Factor of safety by Tresca</strong><br>
The maximum shear stress is:
$$\tau_{\text{max}} = \sqrt{\left(\frac{\sigma_b}{2}\right)^2 + \tau_t^2} = \sqrt{(56.59)^2 + (82.52)^2} = \sqrt{3202 + 6810} = \sqrt{10012} \approx 100.06\text{ MPa}$$
$$\sigma_{\text{Tresca}} = 2\tau_{\text{max}} = 200.12\text{ MPa}$$
$$N_{\text{Tresca}} = \frac{\sigma_y}{\sigma_{\text{Tresca}}} = \frac{850}{200.12} \approx 4.25$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\sigma_b = 113.2\text{ MPa}$, $\tau_t = 82.5\text{ MPa}$<br>
$\sigma_{\text{vM}} = 182.3\text{ MPa} \implies N_{\text{vM}} = 4.66$<br>
$\sigma_{\text{Tresca}} = 200.1\text{ MPa} \implies N_{\text{Tresca}} = 4.25$
</div>"""
})

# ==========================================
# Problem 34
# ==========================================
add({
    "num": 34,
    "title": "Hydrostatic vs. Deviatoric Stress Decomposition",
    "difficulty": "Medium",
    "category": "Stress Tensor",
    "tags": ["Deviatoric Stress", "Hydrostatic Pressure", "Plastic Yielding"],
    "statement": r"""A cubic element in a deep underground drilling collar is subjected to the stress tensor (in MPa):
$$[\boldsymbol{\sigma}] = \begin{bmatrix} 500 & 50 & 0 \\ 50 & 400 & 0 \\ 0 & 0 & 300 \end{bmatrix}$$
<br>
1. Calculate the hydrostatic (mean) stress $\sigma_m = \sigma_h$.<br>
2. Decompose the stress tensor into hydrostatic stress $[\boldsymbol{\sigma}^h]$ and deviatoric stress $[\mathbf{s}]$.<br>
3. Calculate the second invariant of the stress deviator $J_2 = \frac{1}{2} s_{ij} s_{ji}$.<br>
4. Calculate the von Mises stress using $\sigma_{\text{vM}} = \sqrt{3 J_2}$ and explain why hydrostatic pressure cannot cause dislocation-mediated plastic deformation in metals.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate hydrostatic (mean) stress</strong><br>
$$\sigma_m = \frac{\sigma_{xx} + \sigma_{yy} + \sigma_{zz}}{3} = \frac{500 + 400 + 300}{3} = \frac{1200}{3} = 400\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Deviatoric stress tensor $[\mathbf{s}]$</strong><br>
The deviatoric tensor is obtained by subtracting hydrostatic stress from the diagonal elements ($s_{ij} = \sigma_{ij} - \sigma_m \delta_{ij}$):
$$s_{xx} = 500 - 400 = 100\text{ MPa}$$
$$s_{yy} = 400 - 400 = 0\text{ MPa}$$
$$s_{zz} = 300 - 400 = -100\text{ MPa}$$
The off-diagonal shear components remain unchanged:
$$[\mathbf{s}] = \begin{bmatrix} 100 & 50 & 0 \\ 50 & 0 & 0 \\ 0 & 0 & -100 \end{bmatrix}\text{ MPa}$$
Notice that $\operatorname{tr}(\mathbf{s}) = 100 + 0 + (-100) = 0$, confirming zero volumetric distortion.
</div>
<div class="solution-step">
<strong>Step 3: Calculate the second invariant $J_2$</strong><br>
$$J_2 = \frac{1}{2}(s_{xx}^2 + s_{yy}^2 + s_{zz}^2) + s_{xy}^2 + s_{yz}^2 + s_{zx}^2$$
$$J_2 = \frac{1}{2}(100^2 + 0^2 + (-100)^2) + 50^2 + 0 + 0 = \frac{1}{2}(10,000 + 10,000) + 2500 = 10,000 + 2500 = 12,500\text{ MPa}^2$$
</div>
<div class="solution-step">
<strong>Step 4: von Mises stress and role of hydrostatic pressure</strong><br>
$$\sigma_{\text{vM}} = \sqrt{3 J_2} = \sqrt{3 \times 12,500} = \sqrt{37,500} \approx 193.65\text{ MPa}$$
<em>Physical explanation:</em> Dislocation movement (slip) occurs by shear stress resolving along specific close-packed slip planes. Pure hydrostatic stress exerts equal normal forces in all directions ($\sigma_1 = \sigma_2 = \sigma_3 = -p$), producing zero resolved shear stress on any plane ($\tau = \frac{\sigma - \sigma}{2} = 0$). Hence, hydrostatic pressure produces only reversible elastic volumetric strain ($\Delta V/V_0$) without activating dislocation motion. Only the deviatoric stress components drive shear deformation and plastic flow.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Hydrostatic stress $\sigma_m = 400\text{ MPa}$<br>
$J_2 = 12,500\text{ MPa}^2$<br>
$\sigma_{\text{vM}} = \sqrt{3J_2} = 193.6\text{ MPa}$<br>
Hydrostatic stress produces zero shear stress, hence cannot activate dislocation slip.
</div>"""
})

# ==========================================
# Problem 35
# ==========================================
add({
    "num": 35,
    "title": "Stress Triaxiality and Ductile Fracture Suppression",
    "difficulty": "Hard",
    "category": "Fracture Mechanics",
    "tags": ["Triaxiality", "Bridgman", "Void Growth", "Hydrostatic Confinement"],
    "statement": r"""Stress triaxiality is defined as $\eta = \frac{\sigma_m}{\sigma_{\text{eq}}}$, where $\sigma_m$ is the mean (hydrostatic) stress and $\sigma_{\text{eq}}$ is the equivalent von Mises stress.
<br><br>
1. Calculate $\eta$ for: (a) uniaxial tension, (b) pure torsion, (c) equi-biaxial plane tension, and (d) a notched round tensile bar where $\sigma_m = 320\text{ MPa}$ and $\sigma_{\text{eq}} = 400\text{ MPa}$.<br>
2. According to Rice and Tracey's void growth model, the plastic strain to fracture $\varepsilon_f$ decreases exponentially with triaxiality: $\varepsilon_f = A \exp\left(-\frac{3}{2}\eta\right)$. If $\varepsilon_f = 0.85$ in uniaxial tension, calculate the predicted fracture strain $\varepsilon_f$ in the notched bar.<br>
3. Explain why marble and normally brittle metals deform plastically with huge ductility when subjected to high hydrostatic pressure in a Bridgman high-pressure chamber.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate stress triaxiality $\eta = \sigma_m / \sigma_{\text{eq}}$</strong><br>
(a) <em>Uniaxial tension:</em> $\sigma_1 = \sigma, \sigma_2 = 0, \sigma_3 = 0$.
$$\sigma_m = \frac{\sigma + 0 + 0}{3} = \frac{\sigma}{3}, \quad \sigma_{\text{eq}} = \sigma \implies \eta = \frac{\sigma/3}{\sigma} = \frac{1}{3} \approx 0.333$$
(b) <em>Pure torsion:</em> $\sigma_1 = \tau, \sigma_2 = 0, \sigma_3 = -\tau$.
$$\sigma_m = \frac{\tau + 0 - \tau}{3} = 0 \implies \eta = \frac{0}{\sqrt{3}\tau} = 0$$
(c) <em>Equi-biaxial tension:</em> $\sigma_1 = \sigma, \sigma_2 = \sigma, \sigma_3 = 0$.
$$\sigma_m = \frac{2\sigma}{3}, \quad \sigma_{\text{eq}} = \sigma \implies \eta = \frac{2}{3} \approx 0.667$$
(d) <em>Notched round bar:</em>
$$\eta = \frac{320\text{ MPa}}{400\text{ MPa}} = 0.800$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate fracture strain in notched bar</strong><br>
Using $\varepsilon_f = A \exp(-1.5\eta)$:
For uniaxial tension ($\eta = 1/3 = 0.3333$):
$$0.85 = A \exp(-1.5 \times 0.3333) = A \exp(-0.5) \approx A \times 0.6065 \implies A = \frac{0.85}{0.6065} \approx 1.401$$
Now for the notched bar ($\eta = 0.80$):
$$\varepsilon_f = 1.401 \exp(-1.5 \times 0.80) = 1.401 \exp(-1.20) = 1.401 \times 0.3012 \approx 0.422$$
The severe triaxial tensile state halves the material's ductility (from $85\%$ down to $42.2\%$) due to accelerated void expansion.
</div>
<div class="solution-step">
<strong>Step 3: High hydrostatic confinement in Bridgman experiments</strong><br>
Under large confining pressure $P_{\text{conf}}$, $\sigma_m = -P_{\text{conf}} < 0$, making $\eta$ deeply negative. Tensile hydrostatic stresses open and expand microvoids and microcracks. Under compressive hydrostatic pressure, void nucleation and cleavage crack opening are mechanically prevented; microcracks are squeezed shut. Consequently, materials deform solely by dislocation slip and shear twinning, allowing brittle rock (marble) and refractory metals (W, Mo) to achieve tremendous plastic strains without fracturing.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Triaxiality: Uniaxial $= 1/3 \approx 0.333$, Pure shear $= 0$, Equi-biaxial $= 2/3 \approx 0.667$, Notched bar $= 0.800$<br>
Fracture strain drops from $\varepsilon_f = 0.85$ (smooth) to $0.42$ (notched).<br>
Hydrostatic compression prevents void nucleation/growth, suppressing fracture and enabling extensive plasticity.
</div>"""
})

# ==========================================
# Problem 36
# ==========================================
add({
    "num": 36,
    "title": "Strain Rate Sensitivity Exponent and High-Rate Yielding",
    "difficulty": "Medium",
    "category": "Strain Rate Effects",
    "tags": ["Strain Rate Sensitivity", "Flow Stress", "Dynamic Testing"],
    "statement": r"""A low-carbon structural steel is tested in tension at room temperature across several decades of strain rate. The flow stress at $5\%$ plastic strain is measured as:
$$\sigma_1 = 340\text{ MPa at } \dot{\varepsilon}_1 = 10^{-4}\text{ s}^{-1}$$
$$\sigma_2 = 415\text{ MPa at } \dot{\varepsilon}_2 = 10^{2}\text{ s}^{-1}$$
<br>
1. Calculate the strain rate sensitivity exponent $m = \frac{\partial \ln \sigma}{\partial \ln \dot{\varepsilon}}$.<br>
2. Predict the flow stress $\sigma_3$ under explosive/ballistic loading conditions where $\dot{\varepsilon}_3 = 5 \times 10^3\text{ s}^{-1}$.<br>
3. Calculate the percentage increase in strength when moving from quasi-static testing ($10^{-4}\text{ s}^{-1}$) to ballistic rates ($5 \times 10^3\text{ s}^{-1}$).""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate the strain rate sensitivity exponent $m$</strong><br>
The power-law relation between flow stress and strain rate is:
$$\sigma = C \dot{\varepsilon}^m \implies \ln \sigma = \ln C + m \ln \dot{\varepsilon}$$
$$m = \frac{\ln(\sigma_2 / \sigma_1)}{\ln(\dot{\varepsilon}_2 / \dot{\varepsilon}_1)} = \frac{\ln(415 / 340)}{\ln(10^2 / 10^{-4})} = \frac{\ln(1.2206)}{\ln(10^6)} = \frac{0.19933}{6 \times 2.302585} = \frac{0.19933}{13.8155} \approx 0.01443$$
</div>
<div class="solution-step">
<strong>Step 2: Predict flow stress at ballistic strain rate</strong><br>
$$\sigma_3 = \sigma_1 \left(\frac{\dot{\varepsilon}_3}{\dot{\varepsilon}_1}\right)^m = 340 \left(\frac{5 \times 10^3}{10^{-4}}\right)^{0.01443} = 340 \left(5 \times 10^7\right)^{0.01443}$$
$$\ln(5 \times 10^7) = \ln 5 + 7 \ln 10 = 1.6094 + 16.1181 = 17.7275$$
$$\left(5 \times 10^7\right)^{0.01443} = \exp(0.01443 \times 17.7275) = \exp(0.2558) \approx 1.2915$$
$$\sigma_3 = 340 \times 1.2915 \approx 439.1\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Percentage increase in strength</strong><br>
$$\Delta = \frac{\sigma_3 - \sigma_1}{\sigma_1} \times 100\% = \frac{439.1 - 340.0}{340.0} \times 100\% \approx 29.15\%$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Strain rate sensitivity exponent $m = 0.0144$<br>
Predicted dynamic flow stress $\sigma_3 = 439.1\text{ MPa}$ at $\dot{\varepsilon} = 5000\text{ s}^{-1}$<br>
Strength enhancement $= +29.2\%$ above quasi-static strength.
</div>"""
})

# ==========================================
# Problem 37
# ==========================================
add({
    "num": 37,
    "title": "Cowper-Symonds Constitutive Model for Crashworthiness",
    "difficulty": "Hard",
    "category": "Dynamic Mechanics",
    "tags": ["Cowper-Symonds", "Automotive Crash", "Dynamic Yielding"],
    "statement": r"""In automotive crash simulations, the dynamic yield strength $\sigma_{yd}$ of high-strength low-alloy (HSLA) steel side-impact beams is modeled using the Cowper-Symonds equation:
$$\sigma_{yd} = \sigma_y \left[1 + \left(\frac{\dot{\varepsilon}}{D}\right)^{1/p}\right]$$
The steel has a quasi-static yield strength $\sigma_y = 350\text{ MPa}$ and Cowper-Symonds parameters $D = 40\text{ s}^{-1}$ and $p = 5$.
<br><br>
1. During a frontal vehicle collision at $64\text{ km/h}$ against a rigid barrier, the deformation zone experiences a localized strain rate of $\dot{\varepsilon} = 180\text{ s}^{-1}$. Calculate the dynamic yield strength $\sigma_{yd}$.<br>
2. Calculate the dynamic yield stress ratio $R_{\text{dyn}} = \sigma_{yd} / \sigma_y$.<br>
3. If an automotive crash beam of cross-sectional area $A = 250\text{ mm}^2$ crushes by $\Delta L = 120\text{ mm}$, estimate the total impact kinetic energy absorbed by plastic deformation under this dynamic rate.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate dynamic yield strength $\sigma_{yd}$</strong><br>
Given: $\sigma_y = 350\text{ MPa}$, $\dot{\varepsilon} = 180\text{ s}^{-1}$, $D = 40\text{ s}^{-1}$, $p = 5$.
$$\frac{\dot{\varepsilon}}{D} = \frac{180}{40} = 4.5$$
$$\left(\frac{\dot{\varepsilon}}{D}\right)^{1/p} = (4.5)^{1/5} = (4.5)^{0.2} \approx 1.3510$$
$$\sigma_{yd} = 350 \times [1 + 1.3510] = 350 \times 2.3510 \approx 822.85\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Dynamic strength enhancement ratio</strong><br>
$$R_{\text{dyn}} = \frac{\sigma_{yd}}{\sigma_y} = 2.351$$
The dynamic yield strength is $135.1\%$ higher than the quasi-static yield strength due to dislocation drag at high deformation velocity.
</div>
<div class="solution-step">
<strong>Step 3: Impact energy absorption calculation</strong><br>
Assuming ideal plastic collapse at dynamic flow stress $\sigma_{yd} \approx 822.85\text{ MPa}$:
$$\text{Crush force: } F_{\text{dyn}} = \sigma_{yd} A = (822.85 \times 10^6\text{ N/m}^2) \times (250 \times 10^{-6}\text{ m}^2) = 205,712.5\text{ N} \approx 205.7\text{ kN}$$
Energy absorbed over crush distance $\Delta L = 0.120\text{ m}$:
$$E_{\text{abs}} = F_{\text{dyn}} \times \Delta L = 205,712.5\text{ N} \times 0.120\text{ m} \approx 24,685.5\text{ J} \approx 24.69\text{ kJ}$$
By comparison, under quasi-static conditions, the absorbed energy would be only:
$$E_{\text{static}} = (350 \times 10^6 \times 250 \times 10^{-6}) \times 0.120 = 10,500\text{ J} = 10.50\text{ kJ}$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\sigma_{yd} = 822.9\text{ MPa}$ ($135.1\%$ dynamic increase)<br>
$R_{\text{dyn}} = 2.35$<br>
Dynamic energy absorbed $= 24.69\text{ kJ}$ (over $2.3\times$ higher than static prediction).
</div>"""
})

# ==========================================
# Problem 38
# ==========================================
add({
    "num": 38,
    "title": "Johnson-Cook Constitutive Model Decomposition",
    "difficulty": "Hard",
    "category": "Constitutive Modeling",
    "tags": ["Johnson-Cook", "Thermal Softening", "Machining"],
    "statement": r"""The Johnson-Cook constitutive equation describes the flow stress of metals subjected to large strains, high strain rates, and elevated temperatures:
$$\sigma = \left(A + B \varepsilon_p^n\right)\left(1 + C \ln \dot{\varepsilon}^*\right)\left(1 - T^{*m}\right)$$
where $\dot{\varepsilon}^* = \dot{\varepsilon} / \dot{\varepsilon}_0$ and homologous temperature $T^* = \frac{T - T_{\text{room}}}{T_m - T_{\text{room}}}$.
<br>
For titanium alloy Ti-6Al-4V:
$A = 862\text{ MPa}$, $B = 331\text{ MPa}$, $n = 0.34$, $C = 0.012$, $m = 0.80$, $\dot{\varepsilon}_0 = 1.0\text{ s}^{-1}$, $T_{\text{room}} = 293\text{ K}$, and $T_m = 1933\text{ K}$.
<br><br>
1. Identify the physical phenomenon represented by each of the three bracketed terms.<br>
2. In a high-speed metal cutting operation, the primary shear zone experiences an effective plastic strain $\varepsilon_p = 0.60$, strain rate $\dot{\varepsilon} = 10^4\text{ s}^{-1}$, and adiabatic heating raises the temperature to $T = 773\text{ K}$ ($500^\circ\text{C}$). Calculate the value of each of the three terms.<br>
3. Calculate the net resulting flow stress $\sigma$ in the cutting zone.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Physical meaning of the three terms</strong><br>
1. <em>Term 1: $\left(A + B \varepsilon_p^n\right)$</em> — <strong>Strain hardening</strong>: reflects dislocation multiplication and interaction at reference temperature and strain rate.<br>
2. <em>Term 2: $\left(1 + C \ln \dot{\varepsilon}^*\right)$</em> — <strong>Strain rate sensitivity</strong>: reflects short-range barrier overcoming and phonon/electron drag at high dislocation velocities.<br>
3. <em>Term 3: $\left(1 - T^{*m}\right)$</em> — <strong>Thermal softening</strong>: reflects enhanced thermal activation, dislocation climb, and cross-slip that decrease lattice resistance as temperature approaches melting.
</div>
<div class="solution-step">
<strong>Step 2: Numerical evaluation of each term</strong><br>
<em>Term 1 (Strain hardening):</em>
$$\varepsilon_p = 0.60 \implies (0.60)^{0.34} \approx 0.8407$$
$$\text{Term 1} = 862 + 331(0.8407) = 862 + 278.27 = 1140.27\text{ MPa}$$
<br>
<em>Term 2 (Strain rate enhancement):</em>
$$\dot{\varepsilon}^* = \frac{10^4}{1.0} = 10^4 \implies \ln(10^4) = 4 \times 2.302585 = 9.2103$$
$$\text{Term 2} = 1 + 0.012 \times 9.2103 = 1 + 0.1105 = 1.1105$$
<br>
<em>Term 3 (Thermal softening):</em>
$$T^* = \frac{773 - 293}{1933 - 293} = \frac{480}{1640} \approx 0.29268$$
$$(T^*)^{0.80} = (0.29268)^{0.80} \approx 0.3734$$
$$\text{Term 3} = 1 - 0.3734 = 0.6266$$
</div>
<div class="solution-step">
<strong>Step 3: Net resulting flow stress $\sigma$</strong><br>
$$\sigma = (1140.27\text{ MPa}) \times (1.1105) \times (0.6266) \approx 1266.3 \times 0.6266 \approx 793.5\text{ MPa}$$
Notice that despite work hardening raising the base stress to $1140\text{ MPa}$ and dynamic rate raising it further to $1266\text{ MPa}$, thermal softening cuts it down by nearly $37\%$ to $793.5\text{ MPa}$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Term 1 (Strain Hardening) $= 1140.3\text{ MPa}$<br>
Term 2 (Rate Enhancement) $= 1.111$ ($+11.1\%$)<br>
Term 3 (Thermal Softening) $= 0.627$ ($-37.3\%$ reduction)<br>
Net flow stress $\sigma = 793.5\text{ MPa}$
</div>"""
})

# ==========================================
# Problem 39
# ==========================================
add({
    "num": 39,
    "title": "Temperature Dependence of Yield Stress: Thermal vs. Athermal Components",
    "difficulty": "Medium",
    "category": "Dislocation Mechanics",
    "tags": ["Peierls Stress", "Thermal Activation", "Athermal Stress"],
    "statement": r"""The flow stress of crystalline metals is decomposed into thermal and athermal components:
$$\sigma_y(T) = \sigma^* + \sigma_\mu$$
where $\sigma^*$ is the short-range thermal component (sensitive to temperature and strain rate) and $\sigma_\mu$ is the long-range athermal component (governed by elastic modulus $\mu$).
<br><br>
For a BCC iron alloy, $\sigma_\mu = 120\text{ MPa}$, and the thermal component follows:
$$\sigma^*(T) = \sigma_0^* \left[1 - \left(\frac{T}{T_0}\right)^{1/2}\right]$$
with $\sigma_0^* = 680\text{ MPa}$ and $T_0 = 360\text{ K}$ (above $T_0$, $\sigma^* = 0$).
<br><br>
1. Calculate the yield strength at cryogenic temperature $T = 77\text{ K}$ (liquid nitrogen).<br>
2. Calculate the yield strength at room temperature $T = 293\text{ K}$.<br>
3. Calculate the yield strength at elevated temperature $T = 450\text{ K}$.<br>
4. Explain why BCC metals exhibit an extraordinarily strong temperature dependence of yield stress compared to FCC metals like aluminum or copper.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Yield strength at $T = 77\text{ K}$</strong><br>
$$\sigma^*(77) = 680 \left[1 - \left(\frac{77}{360}\right)^{1/2}\right] = 680 [1 - \sqrt{0.21389}] = 680 [1 - 0.46248] = 680 \times 0.53752 \approx 365.5\text{ MPa}$$
$$\sigma_y(77) = \sigma^*(77) + \sigma_\mu = 365.5 + 120 = 485.5\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Yield strength at $T = 293\text{ K}$</strong><br>
$$\sigma^*(293) = 680 \left[1 - \left(\frac{293}{360}\right)^{1/2}\right] = 680 [1 - \sqrt{0.81389}] = 680 [1 - 0.90216] = 680 \times 0.09784 \approx 66.5\text{ MPa}$$
$$\sigma_y(293) = 66.5 + 120 = 186.5\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Yield strength at $T = 450\text{ K}$</strong><br>
Since $T = 450\text{ K} > T_0 = 360\text{ K}$, thermal energy completely overcomes the lattice friction barrier ($\sigma^* = 0$):
$$\sigma_y(450) = 0 + \sigma_\mu = 120.0\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: BCC vs FCC lattice friction</strong><br>
In BCC crystals, screw dislocations possess a non-planar core spread over three intersecting $\{110\}$ planes. Constricting this non-planar core so the dislocation can glide requires a substantial activation energy (high Peierls-Nabarro lattice friction barrier). At low temperatures, thermal vibrations are insufficient to assist constriction, causing the yield stress to skyrocket. In contrast, FCC dislocations have planar cores with very low intrinsic Peierls barriers ($\tau_{\text{PN}} \approx 10^{-5} G$ vs $10^{-2} G$ for BCC); thus, FCC yield strength depends only weakly on temperature.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$T = 77\text{ K}: \sigma_y = 485.5\text{ MPa}$<br>
$T = 293\text{ K}: \sigma_y = 186.5\text{ MPa}$<br>
$T = 450\text{ K}: \sigma_y = 120.0\text{ MPa}$ (athermal plateau)<br>
BCC metals exhibit steep temperature dependence due to high Peierls barriers associated with non-planar screw dislocation cores.
</div>"""
})

# ==========================================
# Problem 40
# ==========================================
add({
    "num": 40,
    "title": "Adiabatic Shear Banding and Thermomechanical Instability",
    "difficulty": "Hard",
    "category": "High-Strain-Rate Mechanics",
    "tags": ["Adiabatic Shear Band", "Instability", "Thermal Softening"],
    "statement": r"""In high-speed deformation (e.g., ballistic penetration or high-speed machining), almost all plastic work is converted into heat adiabatically. An instability known as an <strong>adiabatic shear band (ASB)</strong> initiates when thermal softening overtakes work hardening:
$$\frac{d\sigma}{d\varepsilon} = \left(\frac{\partial \sigma}{\partial \varepsilon}\right)_T + \left(\frac{\partial \sigma}{\partial T}\right)_\varepsilon \frac{dT}{d\varepsilon} \le 0$$
Assuming the adiabatic temperature rise is given by $\frac{dT}{d\varepsilon} = \frac{\beta \sigma}{\rho c_p}$, where Taylor-Quinney factor $\beta = 0.90$, density $\rho = 7800\text{ kg/m}^3$, and specific heat capacity $c_p = 460\text{ J}/(\text{kg}\cdot\text{K})$.
<br><br>
For a steel alloy, the constitutive law is $\sigma = K \varepsilon^n [1 - \gamma(T - T_0)]$, with $K = 800\text{ MPa}$, $n = 0.15$, and thermal softening coefficient $\gamma = 0.0012\text{ K}^{-1}$.
<br><br>
1. Calculate the temperature rise per unit plastic strain $dT/d\varepsilon$ at $\sigma = 750\text{ MPa}$.<br>
2. Formulate the instability condition $d\sigma/d\varepsilon = 0$ and estimate the critical true strain $\varepsilon_{\text{crit}}$ at which shear localization triggers.<br>
3. Explain why adiabatic shear bands are catastrophic in armor plates and turbine rotor bursts.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate adiabatic temperature rise per unit strain</strong><br>
$$\rho c_p = 7800\text{ kg/m}^3 \times 460\text{ J}/(\text{kg}\cdot\text{K}) = 3.588 \times 10^6\text{ J}/(\text{m}^3\cdot\text{K}) = 3.588\text{ MPa/K}$$
$$\frac{dT}{d\varepsilon} = \frac{\beta \sigma}{\rho c_p} = \frac{0.90 \times 750\text{ MPa}}{3.588\text{ MPa/K}} \approx 188.13\text{ K/unit strain}$$
Every $10\%$ of plastic strain under adiabatic conditions generates roughly $\sim 18.8\text{ K}$ of localized temperature increase!
</div>
<div class="solution-step">
<strong>Step 2: Formulate instability condition and find $\varepsilon_{\text{crit}}$</strong><br>
From $\sigma = K \varepsilon^n [1 - \gamma(T - T_0)]$:
$$\left(\frac{\partial \sigma}{\partial \varepsilon}\right)_T = n \frac{\sigma}{\varepsilon}$$
$$\left(\frac{\partial \sigma}{\partial T}\right)_\varepsilon = -\gamma K \varepsilon^n \approx -\gamma \sigma$$
The total derivative becomes:
$$\frac{d\sigma}{d\varepsilon} = n \frac{\sigma}{\varepsilon} - \gamma \sigma \frac{dT}{d\varepsilon} = \sigma \left[\frac{n}{\varepsilon} - \gamma \frac{\beta \sigma}{\rho c_p}\right] = 0$$
Setting the bracket to zero:
$$\frac{n}{\varepsilon_{\text{crit}}} = \frac{\gamma \beta \sigma}{\rho c_p} \implies \varepsilon_{\text{crit}} = \frac{n \rho c_p}{\gamma \beta \sigma}$$
Substitute the given values:
$$\varepsilon_{\text{crit}} = \frac{0.15 \times 3.588 \times 10^6}{0.0012 \times 0.90 \times (750 \times 10^6)} = \frac{538,200}{810,000} \approx 0.664$$
</div>
<div class="solution-step">
<strong>Step 3: Catastrophic nature of adiabatic shear bands</strong><br>
Once strain reaches $\varepsilon_{\text{crit}}$, further deformation softens the material locally ($d\sigma/d\varepsilon < 0$). This causes severe strain localization into narrow bands (only $10\text{ to }50\text{ }\mu\text{m}$ wide). Within the band, temperatures can reach $80\%\text{ to }100\%$ of the melting point, destroying the material's shear strength and leading to rapid, catastrophic shear plugging or fragmentation without macroscale warning.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$dT/d\varepsilon = 188.1\text{ K/unit strain}$ at $750\text{ MPa}$<br>
Instability condition: $\frac{n}{\varepsilon} - \frac{\gamma \beta \sigma}{\rho c_p} \le 0$<br>
Critical strain $\varepsilon_{\text{crit}} \approx 0.66$ ($66\%$ local strain)<br>
ASBs cause intense thermal softening concentrated in $10\text{--}50\text{ }\mu\text{m}$ zones, causing sudden shear failure.
</div>"""
})

# ==========================================
# Problem 41
# ==========================================
add({
    "num": 41,
    "title": "Taylor Impact Test: Estimating Dynamic Yield Stress",
    "difficulty": "Hard",
    "category": "Impact Mechanics",
    "tags": ["Taylor Test", "Dynamic Yield", "High-Velocity Impact"],
    "statement": r"""In a Taylor impact test, a flat-ended cylindrical projectile made of copper with initial length $L_0 = 50.0\text{ mm}$ and initial diameter $D_0 = 10.0\text{ mm}$ is fired at velocity $V_0 = 180\text{ m/s}$ against an essentially rigid, unyielding armor plate.
<br>
After impact, the projectile recovers with a deformed mushroomed front, an overall final length $L_f = 41.5\text{ mm}$, and an undeformed rear section of length $X = 26.0\text{ mm}$.
Copper density is $\rho = 8960\text{ kg/m}^3$.
<br><br>
1. State Taylor's classical dynamic yield stress formula relating $Y_{\text{dyn}}$ to $L_0, L_f, X, \rho$, and $V_0$.<br>
2. Calculate the dynamic yield strength $Y_{\text{dyn}}$ of the copper projectile.<br>
3. If the quasi-static yield strength of the copper is $\sigma_{y,\text{static}} = 140\text{ MPa}$, calculate the dynamic enhancement factor $Y_{\text{dyn}} / \sigma_{y,\text{static}}$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Taylor's dynamic yield formula</strong><br>
G. I. Taylor derived an analytical model for the dynamic yield strength based on rigid-plastic wave propagation:
$$Y_{\text{dyn}} = \frac{\rho V_0^2 (L_0 - X)}{2 (L_0 - L_f) \ln(L_0 / X)}$$
where:
- $\rho$ is the projectile mass density
- $V_0$ is the impact velocity
- $L_0$ is the initial length
- $L_f$ is the final total length
- $X$ is the length of the undeformed rear section
</div>
<div class="solution-step">
<strong>Step 2: Calculate dynamic yield strength $Y_{\text{dyn}}$</strong><br>
Given parameters:
$$\rho = 8960\text{ kg/m}^3, \quad V_0 = 180\text{ m/s} \implies V_0^2 = 32,400\text{ m}^2/\text{s}^2$$
$$\rho V_0^2 = 8960 \times 32,400 = 2.90304 \times 10^8\text{ Pa} = 290.304\text{ MPa}$$
Lengths:
$$L_0 - X = 50.0 - 26.0 = 24.0\text{ mm} = 0.024\text{ m}$$
$$L_0 - L_f = 50.0 - 41.5 = 8.5\text{ mm} = 0.0085\text{ m}$$
$$\ln\left(\frac{L_0}{X}\right) = \ln\left(\frac{50.0}{26.0}\right) = \ln(1.92308) \approx 0.65393$$
Denominator:
$$\text{Denom} = 2(L_0 - L_f)\ln(L_0 / X) = 2(0.0085)(0.65393) = 0.011117\text{ m}$$
Numerator:
$$\text{Num} = \rho V_0^2 (L_0 - X) = (290.304\text{ MPa}) \times (0.024\text{ m}) = 6.9673\text{ MPa}\cdot\text{m}$$
Dynamic yield strength:
$$Y_{\text{dyn}} = \frac{6.9673}{0.011117} \approx 626.7\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Dynamic enhancement ratio</strong><br>
$$\frac{Y_{\text{dyn}}}{\sigma_{y,\text{static}}} = \frac{626.7\text{ MPa}}{140.0\text{ MPa}} \approx 4.48$$
Under high-velocity impact ($180\text{ m/s}$), copper exhibits nearly a $4.5\times$ increase in effective resistance due to massive strain rates ($\dot{\varepsilon} \sim 10^4\text{--}10^5\text{ s}^{-1}$) and rapid dislocation forest multiplication.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Taylor formula: $Y_{\text{dyn}} = \frac{\rho V_0^2 (L_0 - X)}{2 (L_0 - L_f) \ln(L_0 / X)}$<br>
$Y_{\text{dyn}} = 626.7\text{ MPa}$<br>
Dynamic enhancement factor $= 4.48\times$ quasi-static strength.
</div>"""
})

# ==========================================
# Problem 42
# ==========================================
add({
    "num": 42,
    "title": "Bauschinger Effect and Kinematic vs. Isotropic Hardening",
    "difficulty": "Medium",
    "category": "Plasticity",
    "tags": ["Bauschinger Effect", "Kinematic Hardening", "Reverse Yield"],
    "statement": r"""A cylindrical bar of austenitic stainless steel is loaded in forward tension beyond its initial yield point ($\sigma_{y0} = 240\text{ MPa}$) up to a maximum forward stress of $\sigma_{\text{fwd}} = 480\text{ MPa}$.
Upon unloading to zero stress and immediately reloading in reverse compression:
<br><br>
1. Define the <strong>Bauschinger effect</strong> and explain its microscopic origin in terms of dislocation pile-ups and back stresses.<br>
2. Predict the compressive reverse yield stress $|\sigma_{y,\text{rev}}|$ assuming:
   (a) Pure isotropic hardening.<br>
   (b) Pure kinematic hardening.<br>
3. If experimental measurement reveals reverse yielding begins at $|\sigma_{y,\text{rev}}| = 160\text{ MPa}$, calculate the Bauschinger stress parameter $\beta_B = \frac{\sigma_{\text{fwd}} - |\sigma_{y,\text{rev}}|}{2 \sigma_{\text{fwd}}}$. What does this value indicate?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Definition and microscopic origin</strong><br>
The <strong>Bauschinger effect</strong> is the phenomenon whereby plastic deformation in one direction (e.g., forward tension) lowers the yield strength upon load reversal in the opposite direction (reverse compression).<br>
<em>Microscopic origin:</em> During forward loading, dislocations glide and pile up against impenetrable obstacles (grain boundaries, precipitates). These pile-ups create a long-range microscopic <strong>back stress</strong> ($\tau_b$) that opposes further forward glide. When the load is reversed, this internal back stress aids dislocation glide in the reverse direction, triggering plastic flow at a significantly reduced reverse external stress.
</div>
<div class="solution-step">
<strong>Step 2: Predictions under hardening models</strong><br>
(a) <em>Pure Isotropic Hardening:</em> The yield surface expands uniformly in all directions while keeping its center fixed at the origin.
$$|\sigma_{y,\text{rev}}| = \sigma_{\text{fwd}} = 480\text{ MPa}$$
<br>
(b) <em>Pure Kinematic Hardening:</em> The yield surface maintains a constant size (elastic range $= 2\sigma_{y0}$) and translates rigidly in stress space by back stress $\alpha$:
$$\alpha = \sigma_{\text{fwd}} - \sigma_{y0} = 480 - 240 = 240\text{ MPa}$$
Reverse yield stress:
$$|\sigma_{y,\text{rev}}| = \sigma_{\text{fwd}} - 2\sigma_{y0} = 480 - 2(240) = 0\text{ MPa}$$
(yielding in reverse begins immediately upon reaching zero stress!)
</div>
<div class="solution-step">
<strong>Step 3: Experimental assessment and Bauschinger parameter</strong><br>
Given measured $|\sigma_{y,\text{rev}}| = 160\text{ MPa}$:
$$\beta_B = \frac{\sigma_{\text{fwd}} - |\sigma_{y,\text{rev}}|}{2\sigma_{\text{fwd}}} = \frac{480 - 160}{2(480)} = \frac{320}{960} = \frac{1}{3} \approx 0.333$$
Alternatively, the ratio of reverse yield to forward stress is:
$$\frac{|\sigma_{y,\text{rev}}|}{\sigma_{\text{fwd}}} = \frac{160}{480} = 0.333$$
This proves real metals exhibit mixed isotropic-kinematic hardening: isotropic hardening expands the elastic range, while kinematic back stresses shift the yield center.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Isotropic model prediction: $|\sigma_{y,\text{rev}}| = 480\text{ MPa}$<br>
Kinematic model prediction: $|\sigma_{y,\text{rev}}| = 0\text{ MPa}$<br>
Measured: $|\sigma_{y,\text{rev}}| = 160\text{ MPa}$ $\implies$ $\beta_B = 0.333$ (mixed hardening behavior).
</div>"""
})

# ==========================================
# Problem 43
# ==========================================
add({
    "num": 43,
    "title": "Sheet Metal Bending: Elastic Recovery and Springback Ratio",
    "difficulty": "Hard",
    "category": "Metal Forming",
    "tags": ["Springback", "Sheet Bending", "Elastic Recovery"],
    "statement": r"""During sheet metal forming, elastic recovery occurs upon releasing the tooling, causing the bent part to open up (springback). The springback ratio $K_s$ relates the initial loaded bend radius $r_i$ to the final unloaded radius $r_f$:
$$K_s = \frac{r_i + t/2}{r_f + t/2} \approx 4\left(\frac{r_i \sigma_y}{E t}\right)^3 - 3\left(\frac{r_i \sigma_y}{E t}\right) + 1$$
where $t$ is sheet thickness, $\sigma_y$ is yield strength, and $E$ is Young's modulus.
<br><br>
A sheet of high-strength steel ($E = 205\text{ GPa}$, $\sigma_y = 600\text{ MPa}$) with thickness $t = 2.0\text{ mm}$ is bent over a punch radius $r_i = 10.0\text{ mm}$.
<br><br>
1. Calculate the dimensionless parameter $\xi = \frac{r_i \sigma_y}{E t}$.<br>
2. Calculate the springback ratio $K_s$.<br>
3. If the desired final bend angle is $\alpha_f = 90.0^\circ$, determine the required tooling bend angle $\alpha_i$ to compensate for springback ($K_s = \alpha_f / \alpha_i$).<br>
4. Repeat the calculation for an aluminum alloy sheet of identical dimensions with $E = 70\text{ GPa}$ and $\sigma_y = 350\text{ MPa}$. Which material exhibits greater springback?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate dimensionless parameter $\xi$ for high-strength steel</strong><br>
$$\xi_{\text{steel}} = \frac{r_i \sigma_y}{E t} = \frac{(10.0 \times 10^{-3}\text{ m}) \times (600 \times 10^6\text{ Pa})}{(205 \times 10^9\text{ Pa}) \times (2.0 \times 10^{-3}\text{ m})} = \frac{6000}{410,000} \approx 0.014634$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate springback ratio $K_s$ for steel</strong><br>
$$K_s \approx 4\xi^3 - 3\xi + 1$$
Since $\xi^3 = (0.014634)^3 \approx 3.13 \times 10^{-6}$ is negligible:
$$K_{s,\text{steel}} \approx 1 - 3(0.014634) = 1 - 0.04390 = 0.9561$$
</div>
<div class="solution-step">
<strong>Step 3: Tooling punch angle $\alpha_i$ for steel</strong><br>
$$K_s = \frac{\alpha_f}{\alpha_i} \implies \alpha_i = \frac{\alpha_f}{K_s} = \frac{90.0^\circ}{0.9561} \approx 94.13^\circ$$
The tool must overbend the part by $\Delta \alpha = 94.13^\circ - 90^\circ = 4.13^\circ$.
</div>
<div class="solution-step">
<strong>Step 4: Aluminum alloy calculation and comparison</strong><br>
$$\xi_{\text{Al}} = \frac{r_i \sigma_y}{E t} = \frac{(10.0 \times 10^{-3}) \times (350 \times 10^6)}{(70 \times 10^9) \times (2.0 \times 10^{-3})} = \frac{3500}{140,000} = 0.0250$$
$$K_{s,\text{Al}} \approx 1 - 3(0.0250) = 1 - 0.0750 = 0.9250$$
$$\alpha_{i,\text{Al}} = \frac{90.0^\circ}{0.9250} \approx 97.30^\circ \implies \Delta \alpha_{\text{Al}} = 7.30^\circ$$
Aluminum exhibits <strong>significantly greater springback</strong> ($7.30^\circ$ vs $4.13^\circ$). Springback is directly proportional to $\sigma_y / E$. Because aluminum has one-third the modulus of steel ($70\text{ GPa}$ vs $205\text{ GPa}$), its ratio $\sigma_y / E = 350 / 70,000 = 0.0050$ is larger than steel's $600 / 205,000 = 0.00293$, resulting in far greater elastic recovery upon die release.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Steel: $K_s = 0.9561$, required tool angle $\alpha_i = 94.13^\circ$ (overbend $= 4.13^\circ$)<br>
Aluminum: $K_s = 0.9250$, required tool angle $\alpha_i = 97.30^\circ$ (overbend $= 7.30^\circ$)<br>
Aluminum undergoes $77\%$ more springback due to its higher $\sigma_y / E$ ratio.
</div>"""
})

# ==========================================
# Problem 44
# ==========================================
add({
    "num": 44,
    "title": "Springback Angle in V-Die Bending: Analytical Formulation",
    "difficulty": "Medium",
    "category": "Metal Forming",
    "tags": ["V-Die Bending", "Springback Angle", "Elastic Recovery"],
    "statement": r"""A flat metal strip of width $w = 50\text{ mm}$ and thickness $t = 1.5\text{ mm}$ is bent in a $90^\circ$ V-die. The bend radius of the punch is $R_p = 4.5\text{ mm}$ ($R_p / t = 3.0$).
<br><br>
The springback angle $\Delta \theta = \theta_i - \theta_f$ can be approximated by:
$$\Delta \theta = \theta_i \left[ \frac{3 \sigma_y R_p}{E t} \right]$$
where $\theta_i = 90^\circ$ is the loaded bend angle.
<br><br>
1. Calculate $\Delta \theta$ for an annealed low-carbon steel ($E = 210\text{ GPa}$, $\sigma_y = 220\text{ MPa}$).<br>
2. Calculate $\Delta \theta$ for a high-strength aluminum alloy 7075-T6 ($E = 72\text{ GPa}$, $\sigma_y = 500\text{ MPa}$).<br>
3. Calculate $\Delta \theta$ for a spring steel ($E = 205\text{ GPa}$, $\sigma_y = 1200\text{ MPa}$).<br>
4. List two manufacturing methods used by tool designers to minimize or eliminate springback in stamping dies.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Low-carbon steel</strong><br>
$$\Delta \theta_{\text{steel}} = 90^\circ \times \left[ \frac{3(220 \times 10^6)(4.5 \times 10^{-3})}{(210 \times 10^9)(1.5 \times 10^{-3})} \right] = 90^\circ \times \left[\frac{2.97 \times 10^6}{3.15 \times 10^8}\right] = 90^\circ \times 0.009429 \approx 0.849^\circ$$
The low-carbon steel opens up by only $\sim 0.85^\circ$.
</div>
<div class="solution-step">
<strong>Step 2: Aluminum 7075-T6</strong><br>
$$\Delta \theta_{\text{7075}} = 90^\circ \times \left[ \frac{3(500 \times 10^6)(4.5 \times 10^{-3})}{(72 \times 10^9)(1.5 \times 10^{-3})} \right] = 90^\circ \times \left[\frac{6.75 \times 10^6}{1.08 \times 10^8}\right] = 90^\circ \times 0.06250 = 5.625^\circ$$
Aluminum 7075-T6 springs back by a massive $5.63^\circ$.
</div>
<div class="solution-step">
<strong>Step 3: High-strength spring steel</strong><br>
$$\Delta \theta_{\text{spring}} = 90^\circ \times \left[ \frac{3(1200 \times 10^6)(4.5 \times 10^{-3})}{(205 \times 10^9)(1.5 \times 10^{-3})} \right] = 90^\circ \times \left[\frac{1.62 \times 10^7}{3.075 \times 10^8}\right] = 90^\circ \times 0.05268 \approx 4.741^\circ$$
</div>
<div class="solution-step">
<strong>Step 4: Tool design methods to eliminate springback</strong><br>
1. <strong>Bottoming / Coining (Ironing):</strong> At the stroke bottom, the punch squeezes the bend zone beyond its yield point through the thickness in pure compression, eliminating elastic tensile/compressive strain gradients across the neutral axis.<br>
2. <strong>Overbending:</strong> Machining the punch angle smaller than $90^\circ$ (e.g., $85^\circ$) so that the part springs open to precisely $90.0^\circ$ upon ejection.<br>
3. <strong>Stretch Bending:</strong> Applying axial tension simultaneously during bending so the entire thickness is in tension, avoiding opposing compressive elastic recovery.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Low-carbon steel: $\Delta \theta = 0.85^\circ$<br>
Al 7075-T6: $\Delta \theta = 5.63^\circ$<br>
Spring steel: $\Delta \theta = 4.74^\circ$<br>
Mitigation methods: Coining/bottoming, overbending punch angle, and stretch bending.
</div>"""
})

# ==========================================
# Problem 45
# ==========================================
add({
    "num": 45,
    "title": "Residual Stress Distribution Induced by Inelastic Bending",
    "difficulty": "Hard",
    "category": "Residual Stresses",
    "tags": ["Residual Stress", "Plastic Bending", "Elastic Unloading"],
    "statement": r"""A rectangular beam of width $b = 20\text{ mm}$ and height $h = 40\text{ mm}$ (half-height $c = 20\text{ mm}$) made of an elastic-perfectly plastic steel with yield strength $\sigma_y = 300\text{ MPa}$ and Young's modulus $E = 200\text{ GPa}$ is bent by an applied bending moment $M$ to produce a plastic penetration depth such that the elastic core has half-height $y_0 = 10\text{ mm}$ ($c/2$).
<br><br>
1. Calculate the applied bending moment $M$ required to maintain this elastoplastic state.<br>
2. Calculate the fictitious elastic stress $\sigma_e$ at the outer surface ($y = c$) that would occur during elastic unloading by moment $M$.<br>
3. Determine the residual stress $\sigma_{\text{res}}(y)$ at the outer surface ($y = c$) and at the elastic-plastic boundary ($y = y_0$) after completely removing the bending moment.<br>
4. Sketch the residual stress profile across the beam thickness and verify self-equilibrium.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate the elastoplastic bending moment $M$</strong><br>
For a rectangular cross-section with elastic core height $2y_0$:
$$M = \sigma_y b \left(c^2 - \frac{y_0^2}{3}\right)$$
Given $b = 0.020\text{ m}$, $c = 0.020\text{ m}$, $y_0 = 0.010\text{ m}$:
$$c^2 - \frac{y_0^2}{3} = (0.020)^2 - \frac{(0.010)^2}{3} = 0.00040 - 0.00003333 = 0.00036667\text{ m}^2$$
$$M = (300 \times 10^6\text{ N/m}^2) \times (0.020\text{ m}) \times (0.00036667\text{ m}^2) = 2200.0\text{ N}\cdot\text{m} = 2.20\text{ kN}\cdot\text{m}$$
</div>
<div class="solution-step">
<strong>Step 2: Fictitious elastic unloading stress at outer surface</strong><br>
Unloading is purely elastic. The section modulus $S$ is:
$$S = \frac{b h^2}{6} = \frac{0.020 \times (0.040)^2}{6} = \frac{0.020 \times 0.0016}{6} = 5.3333 \times 10^{-6}\text{ m}^3$$
$$\sigma_e(c) = \frac{M}{S} = \frac{2200}{5.3333 \times 10^{-6}} = 412.5\text{ MPa}$$
At $y = y_0 = c/2$:
$$\sigma_e(y_0) = \frac{1}{2} \sigma_e(c) = 206.25\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Residual stress calculation</strong><br>
Residual stress is the superposition of the loaded elastoplastic stress $\sigma_{\text{load}}$ and the elastic unloading stress $-\sigma_{\text{unload}}$:
$$\sigma_{\text{res}}(y) = \sigma_{\text{load}}(y) - \sigma_e(y)$$
- <em>At the outer tensile surface ($y = c = 20\text{ mm}$):</em>
$$\sigma_{\text{load}}(c) = +\sigma_y = +300\text{ MPa}$$
$$\sigma_{\text{res}}(c) = 300 - 412.5 = -112.5\text{ MPa} \quad (\textbf{compressive residual stress})$$
- <em>At the elastic-plastic interface ($y = y_0 = 10\text{ mm}$):</em>
$$\sigma_{\text{load}}(y_0) = +\sigma_y = +300\text{ MPa}$$
$$\sigma_{\text{res}}(y_0) = 300 - 206.25 = +93.75\text{ MPa} \quad (\textbf{tensile residual stress})$$
- <em>At the neutral axis ($y = 0$):</em>
$$\sigma_{\text{res}}(0) = 0 - 0 = 0\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: Self-equilibrium verification</strong><br>
The residual stress profile consists of compressive stresses at the outer fiber ($-112.5\text{ MPa}$), transitioning to peak tensile stresses at $y = 10\text{ mm}$ ($+93.75\text{ MPa}$), and passing through zero at $y = 0$. By antisymmetry across $y = 0$, the resultant axial force $\int \sigma_{\text{res}} dA = 0$ and the net residual internal moment $\int \sigma_{\text{res}} y dA = 0$, confirming perfect self-equilibrium.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Applied moment $M = 2.20\text{ kN}\cdot\text{m}$<br>
Fictitious elastic unloading stress $\sigma_e(c) = 412.5\text{ MPa}$<br>
Surface residual stress $\sigma_{\text{res}}(c) = -112.5\text{ MPa}$ (compressive)<br>
Interface residual stress $\sigma_{\text{res}}(y_0) = +93.8\text{ MPa}$ (tensile).
</div>"""
})

# ==========================================
# Problem 46
# ==========================================
add({
    "num": 46,
    "title": "Shot Peening: Residual Stress Induction and Fatigue Enhancement",
    "difficulty": "Medium",
    "category": "Surface Engineering",
    "tags": ["Shot Peening", "Residual Stress", "Fatigue Improvement"],
    "statement": r"""Shot peening is used to improve the fatigue life of landing gear components made of 300M ultra-high-strength steel ($\sigma_y = 1650\text{ MPa}$, $\sigma_{\text{UTS}} = 1950\text{ MPa}$).
<br><br>
1. Describe the mechanical mechanism by which cast steel shot impacts create a near-surface compressive residual stress layer.<br>
2. A shot peened surface exhibits a compressive residual stress of $\sigma_{\text{res}} = -850\text{ MPa}$ extending to a depth of $d_p = 0.25\text{ mm}$. If an in-service cyclic bending load produces a nominal surface stress alternating between $0$ and $+950\text{ MPa}$, calculate the effective peak surface stress experienced by the component.<br>
3. Explain why compressive surface residual stresses drastically delay fatigue crack initiation.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Mechanism of shot peening</strong><br>
High-velocity spherical shot particles impact the metallic surface, with each individual impact creating a micro-indentation. The surface material is driven into biaxial plastic extension. The deeper, unyielded elastic substrate acts as a rigid constraint that prevents the deformed surface layer from expanding laterally. Upon rebounding of the shot, the elastic substrate pulls back, forcing the plastically stretched surface layer into intense biaxial compressive residual stress.
</div>
<div class="solution-step">
<strong>Step 2: Effective surface stress with residual stress superposition</strong><br>
Without shot peening:
$$\sigma_{\text{max}} = +950\text{ MPa}, \quad \sigma_{\text{min}} = 0\text{ MPa}$$
With shot peening, the static residual stress $\sigma_{\text{res}} = -850\text{ MPa}$ superimposes directly:
$$\sigma_{\text{max, eff}} = \sigma_{\text{max}} + \sigma_{\text{res}} = +950 + (-850) = +100\text{ MPa}$$
$$\sigma_{\text{min, eff}} = \sigma_{\text{min}} + \sigma_{\text{res}} = 0 + (-850) = -850\text{ MPa}$$
The effective maximum tensile stress drops from $+950\text{ MPa}$ to just $+100\text{ MPa}$!
</div>
<div class="solution-step">
<strong>Step 3: Why compressive stresses delay fatigue crack initiation</strong><br>
Fatigue crack initiation requires cyclic tensile opening stress to drive dislocation irreversible slip bands (extrusions and intrusions) and to pull microscopic crack faces apart. Under compressive residual stress:
1. The effective local stress cycle is shifted almost entirely into the compressive regime.
2. Microcracks are forced shut (crack closure phenomenon), preventing localized stress concentration at flaws.
3. Fatigue crack initiation is postponed by orders of magnitude, and the fatigue endurance limit can increase by $30\%\text{ to }70\%$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Effective peak tensile surface stress drops from $+950\text{ MPa}$ down to $+100\text{ MPa}$ (an $89.5\%$ reduction).<br>
Compressive residual stress enforces crack closure and eliminates tensile slip band opening, dramatically extending fatigue life.
</div>"""
})

# ==========================================
# Problem 47
# ==========================================
add({
    "num": 47,
    "title": r"Residual Stress Measurement: X-Ray Diffraction $\sin^2\psi$ Technique",
    "difficulty": "Hard",
    "category": "Characterization",
    "tags": ["X-Ray Diffraction", "sin^2 psi", "Residual Stress Measurement"],
    "statement": r"""The non-destructive $\sin^2\psi$ X-ray diffraction technique measures surface residual stresses by measuring the shift in Bragg peak position as the sample is tilted by angle $\psi$ relative to the incident beam.
The lattice strain $\varepsilon_\psi$ is related to the tilt angle $\psi$ by:
$$\varepsilon_\psi = \frac{d_\psi - d_0}{d_0} = \left(\frac{1+\nu}{E}\right) \sigma_{\phi} \sin^2\psi - \frac{\nu}{E}(\sigma_1 + \sigma_2)$$
For an untextured nickel alloy component ($E = 210\text{ GPa}$, $\nu = 0.30$), the (311) lattice plane spacing $d_\psi$ is measured at multiple tilt angles using $\text{Cr-}K\alpha$ radiation:
- At $\psi = 0^\circ$ ($\sin^2\psi = 0$): $d = 1.08240\text{ \AA}$
- At $\psi = 45^\circ$ ($\sin^2\psi = 0.50$): $d = 1.08092\text{ \AA}$
- The unstressed reference spacing is $d_0 = 1.08200\text{ \AA}$.
<br><br>
1. Calculate the lattice strain $\varepsilon_\psi$ at $\psi = 0^\circ$ and $\psi = 45^\circ$.<br>
2. Calculate the slope $M = \frac{\partial \varepsilon_\psi}{\partial (\sin^2\psi)}$.<br>
3. Calculate the surface residual stress $\sigma_\phi$. State whether it is tensile or compressive.<br>
4. Name one alternative destructive technique for measuring residual stresses through the full component depth.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate lattice strains</strong><br>
$$\varepsilon_0 = \frac{d_0(\psi=0) - d_0}{d_0} = \frac{1.08240 - 1.08200}{1.08200} = \frac{0.00040}{1.08200} \approx +3.6969 \times 10^{-4}$$
$$\varepsilon_{45} = \frac{d_{45} - d_0}{d_0} = \frac{1.08092 - 1.08200}{1.08200} = \frac{-0.00108}{1.08200} \approx -9.9815 \times 10^{-4}$$
</div>
<div class="solution-step">
<strong>Step 2: Slope of the $\sin^2\psi$ plot</strong><br>
$$M = \frac{\varepsilon_{45} - \varepsilon_0}{\sin^2(45^\circ) - \sin^2(0^\circ)} = \frac{-9.9815 \times 10^{-4} - 3.6969 \times 10^{-4}}{0.50 - 0.0} = \frac{-13.6784 \times 10^{-4}}{0.50} = -2.7357 \times 10^{-3}$$
</div>
<div class="solution-step">
<strong>Step 3: Calculate surface residual stress $\sigma_\phi$</strong><br>
From the governing equation:
$$M = \left(\frac{1+\nu}{E}\right) \sigma_\phi \implies \sigma_\phi = M \left(\frac{E}{1+\nu}\right)$$
$$\frac{E}{1+\nu} = \frac{210 \times 10^3\text{ MPa}}{1 + 0.30} = \frac{210,000}{1.30} \approx 161,538.5\text{ MPa}$$
$$\sigma_\phi = (-2.7357 \times 10^{-3}) \times (161,538.5\text{ MPa}) \approx -441.9\text{ MPa}$$
The negative sign confirms that the surface possesses a <strong>compressive residual stress of $441.9\text{ MPa}$</strong>.
</div>
<div class="solution-step">
<strong>Step 4: Alternative destructive measurement technique</strong><br>
The <strong>Hole-Drilling Strain Gage Method (ASTM E837)</strong>: A high-speed milling cutter drills a small blind hole ($1.6\text{ to }2.0\text{ mm}$ diameter) in the center of a specialized 3-element strain gage rosette. Removing the stressed material relaxes the surrounding elastic stress field; the relieved strains measured by the rosette are converted into in-plane residual stresses as a function of depth.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Slope $M = -2.736 \times 10^{-3}$<br>
Surface residual stress $\sigma_\phi = -441.9\text{ MPa}$ (compressive)<br>
Destructive alternative: Blind hole-drilling strain gage method (ASTM E837) or contour method.
</div>"""
})

# ==========================================
# Problem 48
# ==========================================
add({
    "num": 48,
    "title": "Plastic Strain Ratio (Lankford R-Value) and Normal Anisotropy",
    "difficulty": "Medium",
    "category": "Sheet Metal Formability",
    "tags": ["Lankford R-Value", "Plastic Anisotropy", "Deep Drawing"],
    "statement": r"""The plastic strain ratio (Lankford $R$-value) characterizes the resistance of sheet metal to thinning during plastic forming:
$$R = \frac{\varepsilon_w}{\varepsilon_t} = \frac{\ln(w / w_0)}{\ln(t / t_0)}$$
Assuming constancy of volume during plastic deformation ($\varepsilon_l + \varepsilon_w + \varepsilon_t = 0$).
<br><br>
Tensile specimens stamped from a cold-rolled IF (interstitial-free) steel sheet are elongated to a uniform longitudinal plastic strain $\varepsilon_l = 0.180$.
The width strains measured at angles to the rolling direction are:
- Longitudinal ($0^\circ$): $\varepsilon_w = -0.120$
- Diagonal ($45^\circ$): $\varepsilon_w = -0.110$
- Transverse ($90^\circ$): $\varepsilon_w = -0.128$
<br>
1. Calculate the thickness strain $\varepsilon_t$ and the $R$-value for each orientation ($R_0, R_{45}, R_{90}$).<br>
2. Calculate the average normal anisotropy parameter $\bar{R} = \frac{R_0 + 2R_{45} + R_{90}}{4}$.<br>
3. Explain why sheets with $\bar{R} > 1.8$ are highly prized in automotive body deep-drawing applications.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate thickness strains and $R$-values</strong><br>
From volume conservation: $\varepsilon_t = -(\varepsilon_l + \varepsilon_w) = -(0.180 + \varepsilon_w)$.
<br>
- <em>For $0^\circ$ (Rolling direction):</em>
$$\varepsilon_{t, 0} = -(0.180 - 0.120) = -0.060$$
$$R_0 = \frac{\varepsilon_w}{\varepsilon_t} = \frac{-0.120}{-0.060} = 2.000$$
<br>
- <em>For $45^\circ$ (Diagonal):</em>
$$\varepsilon_{t, 45} = -(0.180 - 0.110) = -0.070$$
$$R_{45} = \frac{\varepsilon_w}{\varepsilon_t} = \frac{-0.110}{-0.070} \approx 1.571$$
<br>
- <em>For $90^\circ$ (Transverse):</em>
$$\varepsilon_{t, 90} = -(0.180 - 0.128) = -0.052$$
$$R_{90} = \frac{\varepsilon_w}{\varepsilon_t} = \frac{-0.128}{-0.052} \approx 2.462$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate average normal anisotropy $\bar{R}$</strong><br>
$$\bar{R} = \frac{R_0 + 2R_{45} + R_{90}}{4} = \frac{2.000 + 2(1.571) + 2.462}{4} = \frac{2.000 + 3.142 + 2.462}{4} = \frac{7.604}{4} \approx 1.901$$
</div>
<div class="solution-step">
<strong>Step 3: Importance of high $\bar{R}$ in deep drawing</strong><br>
The $R$-value is the ratio of width contraction to thickness thinning. When $R > 1$, the sheet resists thinning in the thickness direction far more than it resists contraction in the width direction. In a deep-drawing process (e.g., drawing a beverage can or car fender), the material drawn over the die radius undergoes high tensile drawing stresses. A high $\bar{R}$ value ($\bar{R} \approx 1.9$) prevents localized necking and premature tearing in the cup wall, allowing much higher <strong>Limiting Drawing Ratios (LDR)</strong> and enabling deeper, defect-free stampings.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$R_0 = 2.00$, $R_{45} = 1.57$, $R_{90} = 2.46$<br>
Average normal anisotropy $\bar{R} = 1.90$<br>
High $\bar{R}$ prevents wall thinning and premature tearing during deep drawing.
</div>"""
})

# ==========================================
# Problem 49
# ==========================================
add({
    "num": 49,
    "title": "Planar Anisotropy and Earing Behavior in Deep Drawing",
    "difficulty": "Medium",
    "category": "Sheet Metal Formability",
    "tags": ["Planar Anisotropy", "Earing", "Crystallographic Texture"],
    "statement": r"""Planar anisotropy $\Delta R$ quantifies the variation of plastic properties within the sheet plane:
$$\Delta R = \frac{R_0 - 2R_{45} + R_{90}}{2}$$
During deep drawing of a circular blank into a cylindrical cup, non-zero planar anisotropy causes non-uniform cup rim heights, forming wave-like projections called <strong>ears</strong>.
<br><br>
Using the data from Problem 48 ($R_0 = 2.000$, $R_{45} = 1.571$, $R_{90} = 2.462$):
<br>
1. Calculate the planar anisotropy parameter $\Delta R$.<br>
2. Predict the number and angular positions of the ears formed along the rim of a deep-drawn cup.<br>
3. If another alloy has $\Delta R < 0$ (e.g., cold-rolled and annealed aluminum), predict where the ears will form.<br>
4. Explain how crystallographic preferred orientation (texture) generated during cold rolling creates planar anisotropy.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate planar anisotropy $\Delta R$</strong><br>
$$\Delta R = \frac{R_0 - 2R_{45} + R_{90}}{2} = \frac{2.000 - 2(1.571) + 2.462}{2} = \frac{2.000 - 3.142 + 2.462}{2} = \frac{1.320}{2} = +0.660$$
</div>
<div class="solution-step">
<strong>Step 2: Predict ear locations for $\Delta R > 0$</strong><br>
When $\Delta R > 0$, the $R$-values along $0^\circ$ and $90^\circ$ are significantly higher than along $45^\circ$. Because higher $R$ resists thinning and promotes material flow into the rim height:
- Four ears will form located at <strong>$0^\circ, 90^\circ, 180^\circ,$ and $270^\circ$</strong> relative to the rolling direction (coinciding with the rolling and transverse directions).
- Troughs (depressions) will occur at $45^\circ, 135^\circ, 225^\circ,$ and $315^\circ$.
</div>
<div class="solution-step">
<strong>Step 3: Ear locations for $\Delta R < 0$</strong><br>
When $\Delta R < 0$, $R_{45} > \frac{R_0 + R_{90}}{2}$.
Consequently, the four ears will shift by $45^\circ$ and form at <strong>$45^\circ, 135^\circ, 225^\circ,$ and $315^\circ$</strong>, while troughs form at $0^\circ$ and $90^\circ$.
</div>
<div class="solution-step">
<strong>Step 4: Physical origin in crystallographic texture</strong><br>
During cold rolling, individual crystal grains rotate toward specific crystallographic orientations (e.g., $\{111\}\langle 112\rangle$ or $\{001\}\langle 110\rangle$ textures). Because close-packed slip planes $(\{111\}$ in FCC, $\{110\}$ in BCC) and slip directions are non-randomly oriented relative to the sheet axes, the Schmid factors and yield resistance vary systematically with in-plane testing direction. This directional bias directly causes anisotropic yielding and ear formation.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\Delta R = +0.660$<br>
Since $\Delta R > 0$, 4 ears form at $0^\circ, 90^\circ, 180^\circ,$ and $270^\circ$.<br>
For $\Delta R < 0$, ears form at $45^\circ, 135^\circ, 225^\circ,$ and $315^\circ$.<br>
Earing is caused by crystallographic deformation texture aligning slip systems anisotropically.
</div>"""
})

# ==========================================
# Problem 50
# ==========================================
add({
    "num": 50,
    "title": "Comprehensive Material Selection: Aerospace Pressure Cylinder",
    "difficulty": "Hard",
    "category": "Material Selection & Design",
    "tags": ["Ashby Selection", "Specific Strength", "Pressure Vessel Design"],
    "statement": r"""A cylindrical aerospace cabin pressure vessel with diameter $D = 2.0\text{ m}$ (radius $R = 1.0\text{ m}$) and length $L = 6.0\text{ m}$ must withstand an internal operating gauge pressure $p = 120\text{ kPa}$ ($1.2\text{ bar}$) with a design factor of safety $N = 2.0$.
To minimize launch mass, the structural engineer must evaluate three competing candidate alloys:
<br><br>
<table class="data-table">
<thead>
<tr><th>Candidate Alloy</th><th>Density $\rho$ ($\text{g/cm}^3$)</th><th>Modulus $E$ ($\text{GPa}$)</th><th>Yield Strength $\sigma_y$ ($\text{MPa}$)</th><th>Elongation %EL</th></tr>
</thead>
<tbody>
<tr><td>Alloy A: Al 2024-T3</td><td>2.78</td><td>73</td><td>345</td><td>18%</td></tr>
<tr><td>Alloy B: Ti-6Al-4V</td><td>4.43</td><td>114</td><td>880</td><td>14%</td></tr>
<tr><td>Alloy C: Maraging Steel 250</td><td>8.00</td><td>210</td><td>1720</td><td>11%</td></tr>
</tbody>
</table>
<br>
1. Using the von Mises yield criterion with safety factor $N = 2.0$, derive the formula for the minimum wall thickness $t$ of the cylinder.<br>
2. Calculate the required minimum wall thickness $t$ for all three alloys.<br>
3. Calculate the total structural mass $M = \rho \pi D L t$ for each alloy option.<br>
4. Which alloy achieves the lightest overall structure? Calculate the percentage mass saving achieved by the winning alloy over the other two candidates.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Formula for minimum wall thickness under von Mises</strong><br>
In a thin-walled cylinder: $\sigma_\theta = p R / t$, $\sigma_z = p R / (2t) = 0.5 \sigma_\theta$, $\sigma_r \approx 0$.
The von Mises stress was derived in Problem 31:
$$\sigma_{\text{vM}} = \frac{\sqrt{3}}{2} \sigma_\theta = \frac{\sqrt{3}}{2} \frac{p R}{t}$$
For safety factor $N$:
$$\sigma_{\text{vM}} \le \frac{\sigma_y}{N} \implies \frac{\sqrt{3}}{2} \frac{p R}{t} = \frac{\sigma_y}{N} \implies t_{\text{min}} = \frac{\sqrt{3}}{2} \frac{N p R}{\sigma_y}$$
Given $N = 2.0$, $p = 120 \times 10^3\text{ Pa}$, $R = 1.0\text{ m}$:
$$N p R = 2.0 \times 120,000 \times 1.0 = 240,000\text{ N/m}$$
$$t_{\text{min}} = \frac{\sqrt{3}}{2} \times \frac{240,000}{\sigma_y} = \frac{207,846}{\sigma_y}\text{ m} = \frac{207.85}{\sigma_y\text{ (in MPa)}}\text{ mm}$$
</div>
<div class="solution-step">
<strong>Step 2: Required thickness for each alloy</strong><br>
- <em>Alloy A (Al 2024-T3, $\sigma_y = 345\text{ MPa}$):</em>
$$t_A = \frac{207.846}{345} \approx 0.6025\text{ mm} = 6.025 \times 10^{-4}\text{ m}$$
- <em>Alloy B (Ti-6Al-4V, $\sigma_y = 880\text{ MPa}$):</em>
$$t_B = \frac{207.846}{880} \approx 0.2362\text{ mm} = 2.362 \times 10^{-4}\text{ m}$$
- <em>Alloy C (Maraging Steel, $\sigma_y = 1720\text{ MPa}$):</em>
$$t_C = \frac{207.846}{1720} \approx 0.1208\text{ mm} = 1.208 \times 10^{-4}\text{ m}$$
</div>
<div class="solution-step">
<strong>Step 3: Calculate structural shell mass $M = \rho \pi D L t$</strong><br>
Surface area of cylinder: $A_{\text{cyl}} = \pi D L = \pi \times 2.0 \times 6.0 \approx 37.699\text{ m}^2$.
<br>
- <em>Alloy A (Al 2024):</em>
$$\rho_A = 2780\text{ kg/m}^3 \implies M_A = 2780 \times 37.699 \times (6.025 \times 10^{-4}) \approx 63.15\text{ kg}$$
- <em>Alloy B (Ti-6Al-4V):</em>
$$\rho_B = 4430\text{ kg/m}^3 \implies M_B = 4430 \times 37.699 \times (2.362 \times 10^{-4}) \approx 39.45\text{ kg}$$
- <em>Alloy C (Maraging Steel):</em>
$$\rho_C = 8000\text{ kg/m}^3 \implies M_C = 8000 \times 37.699 \times (1.208 \times 10^{-4}) \approx 36.43\text{ kg}$$
</div>
<div class="solution-step">
<strong>Step 4: Comparison and selection</strong><br>
The structural mass ranks:
1. <strong>Maraging Steel 250 ($36.4\text{ kg}$) — Lightest</strong>
2. Ti-6Al-4V ($39.5\text{ kg}$) — $+8.3\%$ heavier
3. Al 2024-T3 ($63.2\text{ kg}$) — $+73.4\%$ heavier
<br>
<em>Ashby index rationale:</em> For a minimum-weight internally pressurized thin shell, the mass minimization index is to maximize <strong>specific strength $\sigma_y / \rho$</strong>:
- $\sigma_y / \rho (\text{Steel}) = 1720 / 8.00 = 215.0\text{ MPa}\cdot\text{cm}^3/\text{g}$
- $\sigma_y / \rho (\text{Ti}) = 880 / 4.43 = 198.6\text{ MPa}\cdot\text{cm}^3/\text{g}$
- $\sigma_y / \rho (\text{Al}) = 345 / 2.78 = 124.1\text{ MPa}\cdot\text{cm}^3/\text{g}$
<br>
Maraging steel yields the lightest vessel ($36.4\text{ kg}$), saving $42.3\%$ mass compared to aluminum 2024-T3. (In practical aerospace design, titanium might still be preferred due to corrosion resistance, damage tolerance, and minimum manufacturing thickness gage limits of $0.12\text{ mm}$ for ultra-thin steel foil).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Thicknesses: $t_A = 0.603\text{ mm}$, $t_B = 0.236\text{ mm}$, $t_C = 0.121\text{ mm}$<br>
Vessel Mass: Maraging Steel $= 36.4\text{ kg}$ (Lightest), Ti-6Al-4V $= 39.5\text{ kg}$, Al 2024-T3 $= 63.2\text{ kg}$<br>
Maraging Steel saves $42.3\%$ mass over aluminum and $8.3\%$ mass over titanium due to its superior specific yield strength ($\sigma_y/\rho = 215$).
</div>"""
})

if __name__ == "__main__":
    print(f"Total problems in P: {len(P)}")
    # Write to ch6_data.py
    out_path = os.path.join(os.path.dirname(__file__), "ch6_data.py")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Chapter 6 Problem Dataset (Mechanical Properties of Metals - 50 Problems)\n")
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
