# generator/make_ch7_part1.py
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
    "title": "Theoretical Shear Strength vs. Actual Yield Strength of Crystals",
    "difficulty": "Medium",
    "category": "Dislocation Basics",
    "tags": ["Theoretical Strength", "Frenkel Model", "Dislocations"],
    "statement": r"""In 1926, J. Frenkel calculated the theoretical shear strength $\tau_{\text{theo}}$ of an ideal defect-free crystal by assuming that adjacent atomic planes slide simultaneously over one another:
$$\tau = \tau_{\text{theo}} \sin\left(\frac{2\pi x}{b}\right) \approx \tau_{\text{theo}} \frac{2\pi x}{b}$$
For small displacements, Hooke's law in shear gives $\tau = G \gamma = G (x / d)$, where $d$ is the interplanar spacing and $b$ is the Burgers vector.
<br><br>
1. Derive Frenkel's formula for theoretical shear strength in terms of shear modulus $G$, Burgers vector $b$, and interplanar spacing $d$. Assuming $b \approx d$, show that $\tau_{\text{theo}} \approx \frac{G}{2\pi} \approx \frac{G}{6.28}$.<br>
2. For pure aluminum ($G = 26\text{ GPa}$), calculate $\tau_{\text{theo}}$.<br>
3. The measured critical resolved shear stress of high-purity single-crystal aluminum is only $\tau_{\text{CRSS}} \approx 1.0\text{ MPa}$. Calculate the ratio $\tau_{\text{theo}} / \tau_{\text{CRSS}}$ and explain why the actual strength is three to four orders of magnitude lower.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Derivation of Frenkel's theoretical shear strength</strong><br>
For very small elastic displacements ($x \ll b$):
$$\tau \approx \tau_{\text{theo}} \left(\frac{2\pi x}{b}\right)$$
From Hooke's law, with shear strain $\gamma = x/d$:
$$\tau = G \gamma = G \left(\frac{x}{d}\right)$$
Equating the two expressions as $x \to 0$:
$$\tau_{\text{theo}} \left(\frac{2\pi x}{b}\right) = G \left(\frac{x}{d}\right) \implies \tau_{\text{theo}} = \frac{G}{2\pi} \left(\frac{b}{d}\right)$$
For close-packed planes where the atomic repeat distance equals the interplanar spacing ($b \approx d$):
$$\tau_{\text{theo}} \approx \frac{G}{2\pi} \approx 0.16\,G \approx \frac{G}{6}$$
More refined sinusoidal and interatomic potential models (Mackenzie, Tyson) give $\tau_{\text{theo}} \approx G/30 \text{ to } G/10$.
</div>
<div class="solution-step">
<strong>Step 2: Calculate $\tau_{\text{theo}}$ for aluminum</strong><br>
Given $G = 26\text{ GPa} = 26,000\text{ MPa}$:
$$\tau_{\text{theo}} = \frac{26,000}{2\pi} \approx 4,138\text{ MPa} \approx 4.14\text{ GPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Comparison with actual single-crystal yield strength</strong><br>
$$\frac{\tau_{\text{theo}}}{\tau_{\text{CRSS}}} = \frac{4,138\text{ MPa}}{1.0\text{ MPa}} \approx 4,138$$
<em>Physical explanation:</em> In a perfect crystal, plastic shear requires breaking all interatomic bonds simultaneously across the entire slip plane. In real metals, plastic slip is mediated by the glide of <strong>dislocations</strong> (line defects). A dislocation moves like a ripple in a heavy rug or a caterpillar crawling: only one line of atomic bonds breaks and reforms at any instant, reducing the required force by a factor of 1,000 to 10,000.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Frenkel formula: $\tau_{\text{theo}} = \frac{G}{2\pi}\frac{b}{d} \approx \frac{G}{2\pi}$<br>
Theoretical shear strength for Al: $\tau_{\text{theo}} \approx 4.14\text{ GPa}$<br>
Actual CRSS $= 1.0\text{ MPa}$ ($\sim 4100\times$ lower) due to dislocation-mediated slip.
</div>"""
})

# ==========================================
# Problem 2
# ==========================================
add({
    "num": 2,
    "title": "Peierls-Nabarro Lattice Friction Stress",
    "difficulty": "Hard",
    "category": "Dislocation Basics",
    "tags": ["Peierls-Nabarro Stress", "Lattice Friction", "Dislocation Core Width"],
    "statement": r"""The intrinsic resistance of a crystal lattice to dislocation motion in the absence of thermal activation is given by the Peierls-Nabarro friction stress:
$$\tau_{\text{PN}} = \frac{2G}{1-\nu} \exp\left(-\frac{2\pi w}{b}\right)$$
where $w$ is the dislocation core width, given by $w = \frac{d}{1-\nu}$, $d$ is the interplanar spacing, and $b$ is the magnitude of the Burgers vector.
<br><br>
1. Show that substituting $w$ into the formula yields:
$$\tau_{\text{PN}} = \frac{2G}{1-\nu} \exp\left(-\frac{2\pi d}{b(1-\nu)}\right)$$
2. For an FCC metal ($\nu = 0.34$, $G = 40\text{ GPa}$), dislocation glide occurs on close-packed $\{111\}$ planes with $d = a/\sqrt{3}$ and along $\langle 110\rangle$ with $b = a/\sqrt{2}$. Calculate the ratio $d/b$ and the resulting Peierls stress $\tau_{\text{PN}}$.<br>
3. If the dislocation were forced to glide on the less densely packed $\{100\}$ planes where $d = a/2$ (same $b = a/\sqrt{2}$), calculate the new ratio $d/b$ and the resulting $\tau_{\text{PN}}$.<br>
4. Based on your results, explain why slip in crystals occurs preferentially on planes with the largest interplanar spacing and smallest Burgers vector.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Formula substitution</strong><br>
Substituting $w = \frac{d}{1-\nu}$ into the exponential:
$$\tau_{\text{PN}} = \frac{2G}{1-\nu} \exp\left(-\frac{2\pi d}{b(1-\nu)}\right)$$
The pre-exponential factor is:
$$\frac{2G}{1-\nu} = \frac{2 \times 40\text{ GPa}}{1 - 0.34} = \frac{80}{0.66} \approx 121.2\text{ GPa} = 121,212\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Peierls stress for $\{111\}$ slip in FCC</strong><br>
$$\frac{d}{b} = \frac{a/\sqrt{3}}{a/\sqrt{2}} = \frac{\sqrt{2}}{\sqrt{3}} = \sqrt{\frac{2}{3}} \approx 0.8165$$
The exponent argument is:
$$\frac{2\pi d}{b(1-\nu)} = \frac{2\pi \times 0.8165}{0.66} \approx \frac{5.1302}{0.66} \approx 7.773$$
$$\tau_{\text{PN}, \{111\}} = 121,212 \times \exp(-7.773) = 121,212 \times (4.209 \times 10^{-4}) \approx 51.0\text{ MPa} \approx 1.3 \times 10^{-3} G$$
(In reality, core spreading and partial dislocations lower this to $\sim 10^{-5} G \approx 0.4\text{ MPa}$).
</div>
<div class="solution-step">
<strong>Step 3: Peierls stress for $\{100\}$ slip in FCC</strong><br>
$$\frac{d}{b} = \frac{a/2}{a/\sqrt{2}} = \frac{1}{\sqrt{2}} \approx 0.7071$$
$$\frac{2\pi d}{b(1-\nu)} = \frac{2\pi \times 0.7071}{0.66} \approx \frac{4.4429}{0.66} \approx 6.7317$$
$$\tau_{\text{PN}, \{100\}} = 121,212 \times \exp(-6.7317) = 121,212 \times (1.1925 \times 10^{-3}) \approx 144.5\text{ MPa}$$
This is nearly 3 times higher than on $\{111\}$ planes.
</div>
<div class="solution-step">
<strong>Step 4: Fundamental rule of slip systems</strong><br>
Because the interplanar spacing $d$ appears in the negative exponent:
1. Maximizing $d$ minimizes $\tau_{\text{PN}}$ exponentially. Planes with the largest interplanar spacing are the most widely separated and have the highest atomic planar packing density.
2. Minimizing the Burgers vector $b$ (shortest repeat distance, along close-packed directions) also maximizes the ratio $d/b$ and minimizes the strain energy of the dislocation ($E \propto G b^2$).
Therefore, dislocation slip always operates on close-packed planes along close-packed directions.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\{111\}$ planes: $d/b = \sqrt{2/3} \approx 0.816 \implies \tau_{\text{PN}} \approx 51\text{ MPa}$<br>
$\{100\}$ planes: $d/b = 1/\sqrt{2} \approx 0.707 \implies \tau_{\text{PN}} \approx 145\text{ MPa}$<br>
Widely spaced, close-packed planes drastically minimize Peierls friction stress due to exponential sensitivity on $d/b$.
</div>"""
})

# ==========================================
# Problem 3
# ==========================================
add({
    "num": 3,
    "title": "Slip Systems in FCC, BCC, and HCP Crystal Structures",
    "difficulty": "Easy",
    "category": "Crystallography of Slip",
    "tags": ["Slip Systems", "FCC", "BCC", "HCP"],
    "statement": r"""A slip system is defined as the combination of a slip plane and a slip direction lying within that plane.
<br><br>
1. For Face-Centered Cubic (FCC): identify the family of slip planes, the family of slip directions, and calculate the total number of independent slip systems.<br>
2. For Body-Centered Cubic (BCC): identify the primary slip plane family and the two additional potential slip plane families at elevated temperatures (all sharing the same slip direction family), and calculate the total number of slip systems.<br>
3. For Hexagonal Close-Packed (HCP): identify the basal slip planes and directions, and calculate the number of basal slip systems.<br>
4. Explain why FCC metals (e.g., Cu, Al, Au) are ductile at all temperatures down to absolute zero, whereas HCP metals (e.g., Mg, Zn) exhibit limited room-temperature ductility.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Slip systems in FCC</strong><br>
- Slip planes: $\{111\}$ family (4 non-parallel octahedral planes: $(111), (\bar{1}11), (1\bar{1}1), (11\bar{1})$).<br>
- Slip directions: $\langle 110\rangle$ close-packed directions lying in each plane (3 directions per plane: $\pm [1\bar{1}0], \pm [10\bar{1}], \pm [01\bar{1}]$).<br>
- Total slip systems: $4 \times 3 = \mathbf{12\text{ slip systems}}$.
</div>
<div class="solution-step">
<strong>Step 2: Slip systems in BCC</strong><br>
- Slip directions: $\langle 111\rangle$ (the 4 body diagonals: $[111], [\bar{1}11], [1\bar{1}1], [11\bar{1}]$).<br>
- Slip planes:
  - Primary: $\{110\}$ (6 planes $\times 2$ directions/plane $= 12$ systems)
  - Secondary (moderate $T$): $\{112\}$ (12 planes $\times 1$ direction/plane $= 12$ systems)
  - Tertiary (high $T$): $\{123\}$ (24 planes $\times 1$ direction/plane $= 24$ systems)<br>
- Total potential slip systems: $12 + 12 + 24 = \mathbf{48\text{ slip systems}}$.
</div>
<div class="solution-step">
<strong>Step 3: Slip systems in HCP (Basal)</strong><br>
- Basal slip plane: $(0001)$ (only 1 unique parallel plane family).<br>
- Close-packed directions: $\langle 11\bar{2}0\rangle$ (3 directions at $120^\circ$: $[2\bar{1}\bar{1}0], [\bar{1}2\bar{1}0], [\bar{1}\bar{1}20]$).<br>
- Total basal slip systems: $1 \times 3 = \mathbf{3\text{ slip systems}}$.
</div>
<div class="solution-step">
<strong>Step 4: Taylor criterion and ductility</strong><br>
According to the <strong>Taylor criterion</strong> (von Mises condition), a polycrystalline material requires at least <strong>5 independent slip systems</strong> to accommodate an arbitrary generalized plastic shape change without opening grain boundary voids or cracking.<br>
- FCC metals have 12 slip systems, 5 of which are geometrically independent at all temperatures. Hence FCC metals exhibit high ductility even at liquid helium temperatures.<br>
- HCP metals have only 3 basal slip systems (2 independent), which do not provide any deformation along the $c$-axis. At room temperature, non-basal slip (prismatic $\{10\bar{1}0\}$ or pyramidal $\{10\bar{1}1\}$) requires very high stress, leading to brittle intergranular fracture unless deformation twinning is activated.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
FCC: $\{111\}\langle 110\rangle = 12$ slip systems.<br>
BCC: $\{110\}\langle 111\rangle, \{112\}\langle 111\rangle, \{123\}\langle 111\rangle = 48$ slip systems.<br>
HCP: $(0001)\langle 11\bar{2}0\rangle = 3$ basal slip systems.<br>
FCC satisfies the 5 independent slip system Taylor criterion at all temperatures, while HCP fails it at low/room temperatures.
</div>"""
})

# ==========================================
# Problem 4
# ==========================================
add({
    "num": 4,
    "title": "Schmid's Law and Resolved Shear Stress Derivation",
    "difficulty": "Medium",
    "category": "Schmid's Law",
    "tags": ["Schmid's Law", "Resolved Shear Stress", "Single Crystal"],
    "statement": r"""Consider a cylindrical single-crystal tensile specimen of cross-sectional area $A_0$ loaded axially with a tensile force $F$. Let $\mathbf{n}$ be the unit normal vector to a slip plane, and $\mathbf{s}$ be the unit vector along a slip direction within that plane.
The angle between the tensile axis and $\mathbf{n}$ is $\phi$, and the angle between the tensile axis and $\mathbf{s}$ is $\lambda$.
<br><br>
1. Derive Schmid's law for the resolved shear stress $\tau_R$ acting along the slip direction in terms of nominal tensile stress $\sigma = F / A_0$, $\phi$, and $\lambda$.<br>
2. Define the Schmid factor $m$. Prove that the maximum theoretical value of $m$ is $0.50$, and find the angles $\phi$ and $\lambda$ at which this maximum occurs.<br>
3. What is the value of $\tau_R$ when: (a) $\phi = 90^\circ$, and (b) $\lambda = 90^\circ$? Explain the physical meaning of these two extreme orientations.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Derivation of Schmid's law</strong><br>
The slip plane is inclined at angle $\phi$ to the tensile axis. The area of the inclined slip plane $A_s$ is:
$$A_s = \frac{A_0}{\cos\phi}$$
The component of the axial tensile force $F$ resolved along the slip direction $\mathbf{s}$ (at angle $\lambda$ to $F$) is:
$$F_s = F \cos\lambda$$
The resolved shear stress $\tau_R$ is the shear force divided by the slip plane area:
$$\tau_R = \frac{F_s}{A_s} = \frac{F \cos\lambda}{A_0 / \cos\phi} = \left(\frac{F}{A_0}\right) \cos\phi \cos\lambda = \sigma \cos\phi \cos\lambda$$
</div>
<div class="solution-step">
<strong>Step 2: Schmid factor and maximum value</strong><br>
The Schmid factor is defined as:
$$m = \cos\phi \cos\lambda$$
Because $\mathbf{s}$ lies in the slip plane ($\mathbf{n} \cdot \mathbf{s} = 0$), the vectors form a right triangle in the plane defined by $\mathbf{n}$ and $\mathbf{s}$. Therefore:
$$\phi + \lambda \ge 90^\circ$$
When the tensile axis lies in the plane containing $\mathbf{n}$ and $\mathbf{s}$, $\lambda = 90^\circ - \phi$:
$$m = \cos\phi \cos(90^\circ - \phi) = \cos\phi \sin\phi = \frac{1}{2}\sin(2\phi)$$
The maximum of $\sin(2\phi)$ is $1$, occurring at:
$$2\phi = 90^\circ \implies \phi = 45^\circ \implies \lambda = 90^\circ - 45^\circ = 45^\circ$$
$$m_{\text{max}} = \frac{1}{2} = 0.50$$
</div>
<div class="solution-step">
<strong>Step 3: Physical interpretation of extreme cases</strong><br>
(a) When $\phi = 90^\circ$: $\cos\phi = 0 \implies \tau_R = 0$. The tensile axis lies parallel to the slip plane. The applied normal force produces zero force component across or along the plane.<br>
(b) When $\lambda = 90^\circ$: $\cos\lambda = 0 \implies \tau_R = 0$. The tensile axis is perpendicular to the slip direction. There is zero force component directed along the direction of dislocation glide.<br>
In both cases, no shear stress drives the dislocation, so plastic slip cannot be initiated on that system regardless of how high $\sigma$ is.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Schmid's Law: $\tau_R = \sigma \cos\phi \cos\lambda = m \sigma$<br>
Maximum Schmid factor: $m_{\text{max}} = 0.50$ at $\phi = \lambda = 45^\circ$<br>
$\tau_R = 0$ when $\phi = 90^\circ$ or $\lambda = 90^\circ$ (zero resolved driving shear force).
</div>"""
})

# ==========================================
# Problem 5
# ==========================================
add({
    "num": 5,
    "title": "Critical Resolved Shear Stress (CRSS) and Single-Crystal Yielding",
    "difficulty": "Medium",
    "category": "Schmid's Law",
    "tags": ["CRSS", "Single Crystal Yield", "Zinc", "Basal Slip"],
    "statement": r"""A single-crystal cylinder of pure zinc (HCP structure) with cross-sectional area $A_0 = 12.0\text{ mm}^2$ is oriented such that the normal to its basal slip plane $(0001)$ makes an angle $\phi = 62.0^\circ$ with the tensile loading axis.
The slip direction $[11\bar{2}0]$ makes an angle $\lambda = 38.0^\circ$ with the tensile axis.
The critical resolved shear stress for basal slip in zinc at room temperature is $\tau_{\text{CRSS}} = 0.18\text{ MPa}$.
<br><br>
1. Verify whether the given angles $\phi$ and $\lambda$ satisfy the geometric constraint $\cos\phi + \cos\lambda \le \dots$ (check whether $\phi + \lambda \ge 90^\circ$).<br>
2. Calculate the Schmid factor $m$ for this slip system.<br>
3. Calculate the macroscopic tensile stress $\sigma_y$ required to initiate plastic yielding.<br>
4. Calculate the required tensile force $F_y$ applied by the testing machine.<br>
5. If the crystal were reoriented such that $\phi = 85^\circ$ and $\lambda = 15^\circ$, calculate the new yield stress $\sigma_y'$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Geometric constraint check</strong><br>
Since the slip direction lies within the slip plane:
$$\phi + \lambda = 62.0^\circ + 38.0^\circ = 100.0^\circ \ge 90.0^\circ$$
This satisfies the required condition for valid 3D angles between the tensile axis, plane normal, and in-plane direction.
</div>
<div class="solution-step">
<strong>Step 2: Calculate Schmid factor $m$</strong><br>
$$m = \cos\phi \cos\lambda = \cos(62.0^\circ) \cos(38.0^\circ)$$
$$\cos(62.0^\circ) \approx 0.46947$$
$$\cos(38.0^\circ) \approx 0.78801$$
$$m = 0.46947 \times 0.78801 \approx 0.36995 \approx 0.370$$
</div>
<div class="solution-step">
<strong>Step 3: Macroscopic tensile yield stress $\sigma_y$</strong><br>
Yielding initiates when $\tau_R = \tau_{\text{CRSS}}$:
$$\tau_{\text{CRSS}} = \sigma_y \times m \implies \sigma_y = \frac{\tau_{\text{CRSS}}}{m} = \frac{0.18\text{ MPa}}{0.36995} \approx 0.4865\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: Applied tensile force $F_y$</strong><br>
$$F_y = \sigma_y A_0 = (0.4865\text{ N/mm}^2) \times (12.0\text{ mm}^2) \approx 5.839\text{ N} \approx 5.84\text{ N}$$
</div>
<div class="solution-step">
<strong>Step 5: Reoriented crystal yield stress</strong><br>
For $\phi = 85^\circ$ and $\lambda = 15^\circ$:
$$\cos(85^\circ) \approx 0.08716, \quad \cos(15^\circ) \approx 0.96593$$
$$m' = 0.08716 \times 0.96593 \approx 0.08419$$
$$\sigma_y' = \frac{\tau_{\text{CRSS}}}{m'} = \frac{0.18\text{ MPa}}{0.08419} \approx 2.138\text{ MPa}$$
Reorienting the crystal so the basal plane is nearly parallel to the tensile axis increases the required yield stress by a factor of $2.138 / 0.4865 \approx 4.4\times$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Schmid factor $m = 0.370$<br>
Yield stress $\sigma_y = 0.487\text{ MPa}$<br>
Yield force $F_y = 5.84\text{ N}$<br>
Reoriented yield stress $\sigma_y' = 2.14\text{ MPa}$ ($4.4\times$ higher).
</div>"""
})

# ==========================================
# Problem 6
# ==========================================
add({
    "num": 6,
    "title": "Identifying Active Slip System in FCC Crystal",
    "difficulty": "Hard",
    "category": "Schmid's Law",
    "tags": ["FCC Single Crystal", "Active Slip System", "Vector Dot Product"],
    "statement": r"""A single crystal of copper (FCC) is loaded in tension along the crystallographic axis $\mathbf{t} = [123]$.
The critical resolved shear stress is $\tau_{\text{CRSS}} = 0.70\text{ MPa}$.
Recall that the slip systems in FCC are $\{111\}\langle 1\bar{1}0\rangle$.
<br><br>
1. Using the vector dot product formula:
$$\cos\phi = \frac{|\mathbf{n} \cdot \mathbf{t}|}{\|\mathbf{n}\| \|\mathbf{t}\|}, \quad \cos\lambda = \frac{|\mathbf{s} \cdot \mathbf{t}|}{\|\mathbf{s}\| \|\mathbf{t}\|}$$
evaluate the Schmid factors for the three slip directions in the $(111)$ slip plane: $\mathbf{s}_1 = [1\bar{1}0]$, $\mathbf{s}_2 = [10\bar{1}]$, and $\mathbf{s}_3 = [01\bar{1}]$.<br>
2. Repeat for the $(\bar{1}11)$ slip plane with directions: $\mathbf{s}_4 = [110]$, $\mathbf{s}_5 = [101]$, and $\mathbf{s}_6 = [0\bar{1}1]$.<br>
3. Identify the primary active slip system with the highest Schmid factor $m_{\text{max}}$.<br>
4. Calculate the macroscopic tensile yield strength $\sigma_y$ of the copper crystal along $[123]$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Evaluate Schmid factors for $(111)$ slip plane</strong><br>
Tensile axis $\mathbf{t} = [123]$:
$$\|\mathbf{t}\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}$$
For plane $\mathbf{n}_1 = [111]$:
$$\|\mathbf{n}_1\| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$$
$$\mathbf{n}_1 \cdot \mathbf{t} = 1(1) + 1(2) + 1(3) = 6 \implies \cos\phi = \frac{6}{\sqrt{3}\sqrt{14}} = \frac{6}{\sqrt{42}}$$
Now for each direction in $(111)$ (note $\|\mathbf{s}\| = \sqrt{2}$):
- $\mathbf{s}_1 = [1\bar{1}0]$:
$$\mathbf{s}_1 \cdot \mathbf{t} = 1(1) - 1(2) + 0(3) = -1 \implies |\mathbf{s}_1 \cdot \mathbf{t}| = 1$$
$$m_1 = \frac{6 \times 1}{\sqrt{42}\sqrt{2}\sqrt{14}} = \frac{6}{\sqrt{42}\sqrt{28}} = \frac{6}{\sqrt{1176}} = \frac{6}{14\sqrt{6}} = \frac{3}{7\sqrt{6}} \approx 0.1750$$
- $\mathbf{s}_2 = [10\bar{1}]$:
$$\mathbf{s}_2 \cdot \mathbf{t} = 1(1) + 0 - 1(3) = -2 \implies |\mathbf{s}_2 \cdot \mathbf{t}| = 2$$
$$m_2 = \frac{6 \times 2}{14\sqrt{6}} = \frac{6}{7\sqrt{6}} \approx 0.3499$$
- $\mathbf{s}_3 = [01\bar{1}]$:
$$\mathbf{s}_3 \cdot \mathbf{t} = 0(1) + 1(2) - 1(3) = -1 \implies |\mathbf{s}_3 \cdot \mathbf{t}| = 1$$
$$m_3 = \frac{6 \times 1}{14\sqrt{6}} \approx 0.1750$$
</div>
<div class="solution-step">
<strong>Step 2: Evaluate Schmid factors for $(\bar{1}11)$ slip plane</strong><br>
For plane $\mathbf{n}_2 = [\bar{1}11]$:
$$\mathbf{n}_2 \cdot \mathbf{t} = -1(1) + 1(2) + 1(3) = 4 \implies \cos\phi = \frac{4}{\sqrt{42}}$$
- $\mathbf{s}_4 = [110]$:
$$\mathbf{s}_4 \cdot \mathbf{t} = 1(1) + 1(2) + 0 = 3 \implies m_4 = \frac{4 \times 3}{14\sqrt{6}} = \frac{12}{14\sqrt{6}} \approx 0.3499$$
- $\mathbf{s}_5 = [101]$:
$$\mathbf{s}_5 \cdot \mathbf{t} = 1(1) + 0 + 1(3) = 4 \implies m_5 = \frac{4 \times 4}{14\sqrt{6}} = \frac{16}{14\sqrt{6}} = \frac{8}{7\sqrt{6}} \approx 0.4666$$
- $\mathbf{s}_6 = [0\bar{1}1]$:
$$\mathbf{s}_6 \cdot \mathbf{t} = 0 - 1(2) + 1(3) = 1 \implies m_6 = \frac{4 \times 1}{14\sqrt{6}} \approx 0.1166$$
</div>
<div class="solution-step">
<strong>Step 3: Primary active slip system</strong><br>
Comparing all values, the highest Schmid factor is:
$$m_{\text{max}} = m_5 = \frac{8}{7\sqrt{6}} \approx 0.4666$$
This corresponds to the primary active slip system: <strong>$(\bar{1}11)[101]$</strong>.
</div>
<div class="solution-step">
<strong>Step 4: Macroscopic tensile yield stress</strong><br>
$$\sigma_y = \frac{\tau_{\text{CRSS}}}{m_{\text{max}}} = \frac{0.70\text{ MPa}}{0.4666} \approx 1.50\text{ MPa}$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Highest Schmid factor $m_{\text{max}} = 0.467$<br>
Primary slip system: $(\bar{1}11)[101]$<br>
Yield strength $\sigma_y = 1.50\text{ MPa}$
</div>"""
})

# ==========================================
# Problem 7
# ==========================================
add({
    "num": 7,
    "title": "Dislocation Energy and Frank's Rule of Dissociation",
    "difficulty": "Easy",
    "category": "Dislocation Reactions",
    "tags": ["Frank's Rule", "Dislocation Energy", "Burgers Vector"],
    "statement": r"""The elastic strain energy per unit length $E_{\text{el}}$ of a dislocation line is proportional to the square of its Burgers vector magnitude:
$$E_{\text{el}} = \alpha G b^2$$
where $\alpha \approx 0.5\text{ to }1.0$, $G$ is shear modulus, and $b = \|\mathbf{b}\|$.
Frank's rule states that a dislocation reaction $\mathbf{b}_1 \to \mathbf{b}_2 + \mathbf{b}_3$ is energetically favorable if $b_1^2 > b_2^2 + b_3^2$.
<br><br>
In an FCC lattice with lattice parameter $a = 0.361\text{ nm}$ (copper, $G = 48\text{ GPa}$):
<br>
1. Calculate the elastic strain energy per meter of a full dislocation $\mathbf{b}_1 = \frac{a}{2}[110]$ (take $\alpha = 0.5$).<br>
2. Consider the potential dissociation into two Shockley partials:
$$\frac{a}{2}[110] \to \frac{a}{6}[21\bar{1}] + \frac{a}{6}[121]$$
Verify vector conservation ($\mathbf{b}_1 = \mathbf{b}_2 + \mathbf{b}_3$).<br>
3. Apply Frank's rule to determine whether this dissociation is energetically favorable, and calculate the percentage energy reduction.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Dislocation energy of full dislocation $\mathbf{b}_1$</strong><br>
$$\|\mathbf{b}_1\|^2 = \left(\frac{a}{2}\right)^2 (1^2 + 1^2 + 0^2) = \frac{a^2}{4}(2) = \frac{a^2}{2}$$
For copper ($a = 0.361 \times 10^{-9}\text{ m}$, $G = 48 \times 10^9\text{ Pa}$):
$$b_1^2 = \frac{(0.361 \times 10^{-9})^2}{2} = \frac{1.3032 \times 10^{-19}}{2} \approx 6.516 \times 10^{-20}\text{ m}^2$$
$$b_1 = \sqrt{6.516 \times 10^{-20}} \approx 0.2553\text{ nm}$$
The energy per unit length is:
$$E_1 = 0.5 G b_1^2 = 0.5 \times (48 \times 10^9) \times (6.516 \times 10^{-20}) \approx 1.564 \times 10^{-9}\text{ J/m} = 1.564\text{ nJ/m}$$
</div>
<div class="solution-step">
<strong>Step 2: Vector conservation check</strong><br>
$$\mathbf{b}_2 + \mathbf{b}_3 = \frac{a}{6}[2, 1, -1] + \frac{a}{6}[1, 2, 1] = \frac{a}{6}[2+1, 1+2, -1+1] = \frac{a}{6}[3, 3, 0] = \frac{a}{2}[1, 1, 0] = \mathbf{b}_1$$
Vector addition is satisfied perfectly.
</div>
<div class="solution-step">
<strong>Step 3: Frank's energy criterion</strong><br>
Calculate $b_2^2$ and $b_3^2$:
$$b_2^2 = \left(\frac{a}{6}\right)^2 (2^2 + 1^2 + (-1)^2) = \frac{a^2}{36}(4 + 1 + 1) = \frac{6a^2}{36} = \frac{a^2}{6}$$
$$b_3^2 = \left(\frac{a}{6}\right)^2 (1^2 + 2^2 + 1^2) = \frac{a^2}{36}(1 + 4 + 1) = \frac{6a^2}{36} = \frac{a^2}{6}$$
Sum of product energies:
$$b_2^2 + b_3^2 = \frac{a^2}{6} + \frac{a^2}{6} = \frac{2a^2}{6} = \frac{a^2}{3}$$
Compare with $b_1^2$:
$$b_1^2 = \frac{a^2}{2} = 0.50\,a^2$$
$$b_2^2 + b_3^2 = \frac{a^2}{3} \approx 0.333\,a^2$$
Since $b_1^2 > b_2^2 + b_3^2$ ($0.50 > 0.333$), the reaction is <strong>highly energetically favorable</strong>!
$$\text{Percentage energy reduction} = \frac{0.50 - 0.333}{0.50} \times 100\% = \frac{1/6}{1/2} \times 100\% = 33.33\%$$
The dissociation cuts the dislocation elastic strain energy by exactly one-third ($33.3\%$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Dislocation energy $E_1 \approx 1.56\text{ nJ/m}$<br>
$b_1^2 = a^2/2$, whereas $b_2^2 + b_3^2 = a^2/3$<br>
Dissociation is energetically favorable with a $33.3\%$ decrease in strain energy.
</div>"""
})

# ==========================================
# Problem 8
# ==========================================
add({
    "num": 8,
    "title": "Shockley Partials and Stacking Fault Equilibrium Width",
    "difficulty": "Hard",
    "category": "Dislocation Reactions",
    "tags": ["Shockley Partials", "Stacking Fault Energy", "Equilibrium Width"],
    "statement": r"""When a full dislocation in an FCC crystal dissociates into two Shockley partials, a strip of stacking fault (with surface energy $\gamma_{\text{SF}}$) is created between them:
The two partials repel each other with an elastic repulsive force per unit length:
$$F_{\text{rep}} = \frac{G (\mathbf{b}_1 \cdot \mathbf{b}_2)}{2\pi d}$$
where $d$ is the separation distance (ribbon width), $G$ is the shear modulus, and $\mathbf{b}_1 = \frac{a}{6}[21\bar{1}], \mathbf{b}_2 = \frac{a}{6}[121]$.
The stacking fault exerts an attractive surface tension force per unit length $F_{\text{att}} = \gamma_{\text{SF}}$ pulling them together.
<br><br>
1. Calculate the dot product $\mathbf{b}_1 \cdot \mathbf{b}_2$ in terms of lattice parameter $a$.<br>
2. Equating $F_{\text{rep}} = F_{\text{att}}$, derive the formula for the equilibrium stacking fault width $d$.<br>
3. For copper ($a = 0.361\text{ nm}$, $G = 48\text{ GPa}$, $\gamma_{\text{SF}} = 45\text{ mJ/m}^2$), calculate the equilibrium width $d_{\text{Cu}}$.<br>
4. For aluminum ($a = 0.405\text{ nm}$, $G = 26\text{ GPa}$, $\gamma_{\text{SF}} = 160\text{ mJ/m}^2$), calculate $d_{\text{Al}}$.<br>
5. Explain how the difference in ribbon width explains why aluminum cross-slips easily while copper and brass do not.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate dot product $\mathbf{b}_1 \cdot \mathbf{b}_2$</strong><br>
$$\mathbf{b}_1 \cdot \mathbf{b}_2 = \left(\frac{a}{6}\right)^2 [2(1) + 1(2) + (-1)(1)] = \frac{a^2}{36}[2 + 2 - 1] = \frac{3a^2}{36} = \frac{a^2}{12}$$
</div>
<div class="solution-step">
<strong>Step 2: Derive equilibrium width $d$</strong><br>
At mechanical equilibrium, the elastic repulsive force equals the stacking fault tension:
$$F_{\text{rep}} = \frac{G (a^2 / 12)}{2\pi d} = \frac{G a^2}{24\pi d} = \gamma_{\text{SF}}$$
Solving for $d$:
$$d = \frac{G a^2}{24\pi \gamma_{\text{SF}}}$$
</div>
<div class="solution-step">
<strong>Step 3: Stacking fault width for copper</strong><br>
Given: $a = 0.361 \times 10^{-9}\text{ m}$, $G = 48 \times 10^9\text{ Pa}$, $\gamma_{\text{SF}} = 0.045\text{ J/m}^2$:
$$G a^2 = (48 \times 10^9) \times (0.361 \times 10^{-9})^2 = (48 \times 10^9) \times (1.3032 \times 10^{-19}) \approx 6.255 \times 10^{-9}\text{ N}$$
$$24\pi \gamma_{\text{SF}} = 24\pi \times 0.045 \approx 3.3929\text{ N/m}$$
$$d_{\text{Cu}} = \frac{6.255 \times 10^{-9}}{3.3929} \approx 1.844 \times 10^{-9}\text{ m} = 1.84\text{ nm} \approx 7.2\,b$$
</div>
<div class="solution-step">
<strong>Step 4: Stacking fault width for aluminum</strong><br>
Given: $a = 0.405 \times 10^{-9}\text{ m}$, $G = 26 \times 10^9\text{ Pa}$, $\gamma_{\text{SF}} = 0.160\text{ J/m}^2$:
$$G a^2 = (26 \times 10^9) \times (0.405 \times 10^{-9})^2 = (26 \times 10^9) \times (1.64025 \times 10^{-19}) \approx 4.265 \times 10^{-9}\text{ N}$$
$$24\pi \gamma_{\text{SF}} = 24\pi \times 0.160 \approx 12.064\text{ N/m}$$
$$d_{\text{Al}} = \frac{4.265 \times 10^{-9}}{12.064} \approx 0.354 \times 10^{-9}\text{ m} = 0.35\text{ nm} \approx 1.2\,b$$
</div>
<div class="solution-step">
<strong>Step 5: Impact on cross-slip and dynamic recovery</strong><br>
A screw dislocation cannot cross-slip onto an intersecting $\{111\}$ plane while dissociated, because the extended stacking fault ribbon is strictly confined to its original slip plane. To cross-slip, the two partials must first be pinched together (constricted) back into a full dislocation against the repulsive force.<br>
- In aluminum, $\gamma_{\text{SF}}$ is very high ($160\text{ mJ/m}^2$), so the ribbon width is only $0.35\text{ nm}$ ($\approx 1$ atom wide). The constriction energy is negligible, allowing aluminum to cross-slip effortlessly, bypass obstacles, and form well-defined cellular subgrain networks (Stage III dynamic recovery).<br>
- In copper ($\gamma_{\text{SF}} = 45$) and brass ($\gamma_{\text{SF}} < 15$), the wide ribbon ($> 2\text{--}10\text{ nm}$) makes constriction energetically prohibitive, forcing dislocations into planar slip arrays and preventing easy cross-slip.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Equilibrium width formula: $d = \frac{G a^2}{24\pi \gamma_{\text{SF}}}$<br>
Copper ($d = 1.84\text{ nm}$): Wide ribbon, difficult cross-slip, planar slip.<br>
Aluminum ($d = 0.35\text{ nm}$): Narrow ribbon, rapid constriction and easy cross-slip.
</div>"""
})

# ==========================================
# Problem 9
# ==========================================
add({
    "num": 9,
    "title": "Lomer-Cottrell Lock (Dislocation Junction Formation)",
    "difficulty": "Hard",
    "category": "Dislocation Reactions",
    "tags": ["Lomer-Cottrell Lock", "Dislocation Junction", "Strain Hardening"],
    "statement": r"""In FCC metals undergoing multiaxial slip, two dislocations gliding on intersecting $\{111\}$ planes can meet and react to form a sessile (immobile) dislocation junction known as a <strong>Lomer-Cottrell lock</strong>.
Consider the reaction between dislocation $\mathbf{b}_1 = \frac{a}{2}[01\bar{1}]$ gliding on the $(111)$ plane and dislocation $\mathbf{b}_2 = \frac{a}{2}[101]$ gliding on the $(1\bar{1}1)$ plane.
<br><br>
1. Determine the Burgers vector $\mathbf{b}_3 = \mathbf{b}_1 + \mathbf{b}_2$ of the resulting product dislocation.<br>
2. Determine the line of intersection $\mathbf{u}$ of the two slip planes $(111)$ and $(1\bar{1}1)$ by computing their cross product.<br>
3. Show that the product dislocation lies along the intersection line $\mathbf{u}$ and calculate its energy using Frank's rule. Is the reaction energetically favorable?<br>
4. Identify the plane containing both $\mathbf{b}_3$ and $\mathbf{u}$. Explain why this dislocation is strictly sessile (unable to glide), and describe its role in Stage II work hardening.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Burgers vector of the product dislocation</strong><br>
$$\mathbf{b}_3 = \mathbf{b}_1 + \mathbf{b}_2 = \frac{a}{2}[0, 1, -1] + \frac{a}{2}[1, 0, 1] = \frac{a}{2}[0+1, 1+0, -1+1] = \frac{a}{2}[110]$$
</div>
<div class="solution-step">
<strong>Step 2: Line of intersection $\mathbf{u}$ of the two slip planes</strong><br>
$$\mathbf{n}_1 = [1, 1, 1], \quad \mathbf{n}_2 = [1, -1, 1]$$
$$\mathbf{u} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 1 \\ 1 & -1 & 1 \end{vmatrix} = \mathbf{i}(1 - (-1)) - \mathbf{j}(1 - 1) + \mathbf{k}(-1 - 1) = 2\mathbf{i} - 0\mathbf{j} - 2\mathbf{k} = [2, 0, -2]$$
Normalizing to the standard crystallographic direction:
$$\mathbf{u} = [10\bar{1}]$$
</div>
<div class="solution-step">
<strong>Step 3: Frank's rule check</strong><br>
$$b_1^2 = \left(\frac{a}{2}\right)^2 (0 + 1 + 1) = \frac{2a^2}{4} = \frac{a^2}{2}$$
$$b_2^2 = \left(\frac{a}{2}\right)^2 (1 + 0 + 1) = \frac{2a^2}{4} = \frac{a^2}{2}$$
$$b_1^2 + b_2^2 = \frac{a^2}{2} + \frac{a^2}{2} = a^2$$
For the product $\mathbf{b}_3 = \frac{a}{2}[110]$:
$$b_3^2 = \left(\frac{a}{2}\right)^2 (1 + 1 + 0) = \frac{2a^2}{4} = \frac{a^2}{2}$$
Comparing:
$$b_3^2 = 0.50\,a^2 < b_1^2 + b_2^2 = 1.00\,a^2$$
The reaction produces a $50\%$ reduction in strain energy and is <strong>spontaneous and highly favorable</strong>!
</div>
<div class="solution-step">
<strong>Step 4: Why the Lomer-Cottrell lock is sessile</strong><br>
The plane containing both the dislocation line $\mathbf{u} = [10\bar{1}]$ and Burgers vector $\mathbf{b}_3 = \frac{a}{2}[110]$ has normal:
$$\mathbf{n}_{\text{plane}} = \mathbf{u} \times \mathbf{b}_3 \propto [1, 0, -1] \times [1, 1, 0] = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & -1 \\ 1 & 1 & 0 \end{vmatrix} = [1, -1, 1] \dots \text{with partial splitting on } (001)$$
Crucially, when partial dislocations form, the lock forms a triangular sessile stair-rod dislocation wedge on $\{001\}$ planes. In FCC crystals, $\{001\}$ is <strong>not</strong> an active close-packed slip plane at ordinary temperatures. The dislocation is pinned along $\mathbf{u}$, acting as an immovable barrier (lock) that blocks subsequent dislocations on both intersecting slip planes. Dislocation pile-ups form against the lock, leading to linear, rapid strain hardening (Stage II work hardening).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\mathbf{b}_3 = \frac{a}{2}[110]$, line direction $\mathbf{u} = [10\bar{1}]$<br>
Frank's rule: $b_3^2 = a^2/2 < b_1^2 + b_2^2 = a^2$ ($50\%$ energy drop)<br>
The lock is sessile because its slip plane is $\{001\}$, creating a permanent barrier responsible for rapid Stage II strain hardening.
</div>"""
})

# ==========================================
# Problem 10
# ==========================================
add({
    "num": 10,
    "title": "Deformation Twinning vs. Slip in HCP and BCC Metals",
    "difficulty": "Medium",
    "category": "Twinning Mechanics",
    "tags": ["Deformation Twinning", "HCP", "BCC", "Cryogenic Deformation"],
    "statement": r"""Plastic deformation occurs by slip or deformation twinning.
<br><br>
1. Compare mechanical slip and deformation twinning across four key criteria:
   (a) Crystallographic orientation change across the deformed region.<br>
   (b) Shear displacement per atomic plane.<br>
   (c) Microscopic appearance under optical microscopy.<br>
   (d) Deformation speed / kinetics.<br>
2. For an HCP magnesium crystal undergoing tensile twinning on the $\{10\bar{1}2\}$ plane along the $\langle 10\bar{1}1\rangle$ direction, the twin shear strain is given by:
$$\gamma_{\text{twin}} = \frac{(c/a)^2 - 3}{\sqrt{3}\,(c/a)}$$
For magnesium, $c/a = 1.624$. Calculate the twin shear strain $\gamma_{\text{twin}}$.<br>
3. Explain why mechanical twinning is favored over dislocation slip at cryogenic temperatures and under ballistic shock loading.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Comparison table between slip and twinning</strong><br>
(a) <em>Orientation change:</em> Slip does NOT reorient the crystal lattice; atomic planes remain parallel. Twinning creates a reoriented mirror-image crystal region related across the twin boundary plane.<br>
(b) <em>Displacement:</em> In slip, shear displacement is an integer multiple of the full Burgers vector $b$ localized to discrete slip planes. In twinning, shear displacement is a fraction of an atomic spacing, distributed uniformly across every successive atomic plane.<br>
(c) <em>Microscopic appearance:</em> Slip appears as thin surface steps (slip lines). Twinning appears as broad lenticular (lens-shaped) bands visible after polishing and etching.<br>
(d) <em>Kinetics:</em> Dislocation slip is thermally activated and progresses continuously. Twinning occurs almost instantaneously at near the speed of sound, often accompanied by an audible cracking or clicking sound ("tin cry").
</div>
<div class="solution-step">
<strong>Step 2: Calculate magnesium twin shear strain $\gamma_{\text{twin}}$</strong><br>
Given $c/a = 1.624$:
$$(c/a)^2 = (1.624)^2 \approx 2.63738$$
$$(c/a)^2 - 3 = 2.63738 - 3.000 = -0.36262$$
Denominator:
$$\sqrt{3}\,(c/a) = 1.73205 \times 1.624 \approx 2.81285$$
Shear strain magnitude:
$$|\gamma_{\text{twin}}| = \frac{0.36262}{2.81285} \approx 0.1289 \approx 12.9\%$$
(The negative sign indicates that for $c/a < \sqrt{3} \approx 1.732$, $\{10\bar{1}2\}$ twins produce tensile extension along the $c$-axis).
</div>
<div class="solution-step">
<strong>Step 3: Why twinning dominates at low temperature and high strain rate</strong><br>
Dislocation slip requires thermal energy to overcome short-range barriers (Peierls lattice friction, forest junctions). At cryogenic temperatures ($T < 77\text{ K}$) or under explosive/ballistic strain rates ($\dot{\varepsilon} > 10^3\text{ s}^{-1}$), the thermal energy $k_B T$ is too low and time is insufficient for thermal activation, driving the required stress for slip above the critical twinning stress. Because mechanical twinning occurs by cooperative shear without requiring thermally activated climbing or cross-slipping, the critical twinning stress is nearly temperature-independent, making twinning the dominant deformation mode under extreme conditions.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Slip: Integer $b$ displacement, no lattice reorientation.<br>
Twinning: Fractional shear on every plane, creates mirror lattice.<br>
Mg twin shear strain: $\gamma_{\text{twin}} = 0.129$ ($12.9\%$).<br>
Twinning is favored at cryogenic temperatures and high strain rates because its activation stress is athermal.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 7 Part 1: P1-P10 added. Current total: {len(P)}")

# ==========================================
# Problem 11
# ==========================================
add({
    "num": 11,
    "title": "Grain Boundaries as Dislocation Obstacles: Physical Mechanisms",
    "difficulty": "Easy",
    "category": "Grain Size Strengthening",
    "tags": ["Grain Boundary Barrier", "Misorientation", "Slip Transfer"],
    "statement": r"""A polycrystalline metal consists of many individual grains (crystallites) separated by grain boundaries.
<br><br>
1. Explain the two primary crystallographic mechanisms by which a high-angle grain boundary impedes the passage of a gliding dislocation.<br>
2. Can a dislocation glide smoothly from Grain A into Grain B across a high-angle boundary without interruption? Explain why or why not.<br>
3. How does the presence of grain boundaries explain why polycrystalline metals are invariably stronger than single crystals of the same composition?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Two primary barrier mechanisms of grain boundaries</strong><br>
1. <strong>Crystallographic Misorientation:</strong> Adjacent grains possess different spatial crystallographic orientations. Because dislocation slip is strictly confined to specific close-packed planes (e.g., $\{111\}$ in FCC), when a dislocation gliding on a slip plane in Grain A reaches the boundary, the corresponding slip plane in Grain B does not align with it. To continue, the dislocation would have to suddenly change its trajectory into a non-coplanar plane, requiring an enormous energy penalty.<br>
2. <strong>Atomic Disordering at the Boundary:</strong> A high-angle grain boundary is an atomically disordered transition zone characterized by broken, stretched, and misaligned bonds. There are no well-defined lattice planes or periodic potentials within the boundary, disrupting the regular glide path of dislocations.
</div>
<div class="solution-step">
<strong>Step 2: Can dislocations glide smoothly across?</strong><br>
No. In almost all cases, a dislocation cannot cross a high-angle boundary directly. Instead, when a dislocation reaches the grain boundary, it is stopped and pinned. As more dislocations arrive on the same slip plane from behind, they form a <strong>dislocation pile-up</strong>. The collective repulsive interactions among piled-up dislocations create an intense stress concentration at the boundary. Only when this local tip stress reaches a critical threshold does it activate a new, independent dislocation source (e.g., a Frank-Read source) in the adjacent Grain B, transferring plastic slip across the boundary indirectly.
</div>
<div class="solution-step">
<strong>Step 3: Polycrystalline vs. single-crystal strength</strong><br>
In a single crystal, once a dislocation starts moving at the critical resolved shear stress ($\tau_{\text{CRSS}} \approx 1\text{ MPa}$), it can travel vast macroscopic distances across the entire crystal without encountering internal boundaries. In contrast, in a polycrystal, dislocation glide is halted every few micrometers (the grain diameter $d$). Hundreds of grain boundaries per millimeter force continuous dislocation pile-up and source activation, raising the macroscopic yield strength by an order of magnitude (e.g., pure Al single crystal yields at $\sim 1\text{ MPa}$, while polycrystalline Al yields at $25\text{--}40\text{ MPa}$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Two mechanisms: (1) Slip plane misorientation across the boundary, and (2) Atomic disorder destroying periodic slip paths.<br>
Dislocations do not cross directly; they pile up and activate new sources in neighboring grains via stress concentration.<br>
Polycrystals are much stronger because internal boundaries halt dislocation mean free path every few microns.
</div>"""
})

# ==========================================
# Problem 12
# ==========================================
add({
    "num": 12,
    "title": "Hall-Petch Equation and Parameter Determination",
    "difficulty": "Medium",
    "category": "Grain Size Strengthening",
    "tags": ["Hall-Petch", "Grain Size", "Yield Strength", "Ferritic Steel"],
    "statement": r"""The Hall-Petch equation describes the relationship between yield strength $\sigma_y$ and average grain diameter $d$:
$$\sigma_y = \sigma_0 + k_y d^{-1/2}$$
where $\sigma_0$ is the friction stress (lattice resistance to dislocation glide) and $k_y$ is the Hall-Petch strengthening coefficient (boundary barrier resistance).
<br><br>
Tensile testing of a low-carbon ferritic steel yields the following experimental data:
- Specimen 1: average grain diameter $d_1 = 49.0\text{ }\mu\text{m}$, yield strength $\sigma_{y1} = 175.0\text{ MPa}$.
- Specimen 2: average grain diameter $d_2 = 9.0\text{ }\mu\text{m}$, yield strength $\sigma_{y2} = 265.0\text{ MPa}$.
<br>
1. Calculate $d^{-1/2}$ for both specimens in units of $\text{m}^{-1/2}$ and $\text{mm}^{-1/2}$.<br>
2. Determine the Hall-Petch constants $\sigma_0$ (in MPa) and $k_y$ (in $\text{MPa}\cdot\text{m}^{1/2}$ and $\text{MPa}\cdot\text{mm}^{1/2}$).<br>
3. Predict the yield strength $\sigma_y$ if the grain size is refined to $d_3 = 2.25\text{ }\mu\text{m}$.<br>
4. What grain size $d_4$ would be required to achieve a yield strength of $\sigma_y = 400.0\text{ MPa}$?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate $d^{-1/2}$</strong><br>
Convert diameters to meters:
$$d_1 = 49.0 \times 10^{-6}\text{ m} \implies d_1^{-1/2} = (49 \times 10^{-6})^{-0.5} = \frac{10^3}{\sqrt{49}} = \frac{1000}{7} \approx 142.857\text{ m}^{-1/2}$$
$$d_2 = 9.0 \times 10^{-6}\text{ m} \implies d_2^{-1/2} = (9 \times 10^{-6})^{-0.5} = \frac{10^3}{\sqrt{9}} = \frac{1000}{3} \approx 333.333\text{ m}^{-1/2}$$
In units of $\text{mm}^{-1/2}$:
$$d_1 = 0.049\text{ mm} \implies d_1^{-1/2} = 4.5175\text{ mm}^{-1/2}$$
$$d_2 = 0.009\text{ mm} \implies d_2^{-1/2} = 10.5409\text{ mm}^{-1/2}$$
</div>
<div class="solution-step">
<strong>Step 2: Determine $\sigma_0$ and $k_y$</strong><br>
Form the system of linear equations:
$$\sigma_{y1} = \sigma_0 + k_y (142.857) = 175.0\text{ MPa}$$
$$\sigma_{y2} = \sigma_0 + k_y (333.333) = 265.0\text{ MPa}$$
Subtracting the first from the second:
$$k_y (333.333 - 142.857) = 265.0 - 175.0$$
$$k_y (190.476) = 90.0 \implies k_y = \frac{90.0}{190.476} \approx 0.4725\text{ MPa}\cdot\text{m}^{1/2}$$
In $\text{MPa}\cdot\text{mm}^{1/2}$:
$$k_y = 0.4725 \times \sqrt{10^{-3}} \approx 0.01494\text{ MPa}\cdot\text{m}^{1/2} \dots \text{or } k_y = 0.4725 \times 1000^{-1/2} \approx 14.94\text{ MPa}\cdot\text{mm}^{1/2}$$
Now solve for $\sigma_0$:
$$\sigma_0 = 175.0 - (0.4725 \times 142.857) = 175.0 - 67.50 = 107.50\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Predict yield strength for $d_3 = 2.25\text{ }\mu\text{m}$</strong><br>
$$d_3 = 2.25 \times 10^{-6}\text{ m} \implies d_3^{-1/2} = \frac{10^3}{\sqrt{2.25}} = \frac{1000}{1.5} \approx 666.667\text{ m}^{-1/2}$$
$$\sigma_y(2.25\text{ }\mu\text{m}) = 107.50 + 0.4725 \times 666.667 = 107.50 + 315.00 = 422.50\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 4: Grain size required for $\sigma_y = 400.0\text{ MPa}$</strong><br>
$$400.0 = 107.50 + 0.4725\,d_4^{-1/2}$$
$$0.4725\,d_4^{-1/2} = 292.50 \implies d_4^{-1/2} = \frac{292.50}{0.4725} \approx 619.048\text{ m}^{-1/2}$$
$$d_4 = (619.048)^{-2} \approx 2.61 \times 10^{-6}\text{ m} = 2.61\text{ }\mu\text{m}$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\sigma_0 = 107.5\text{ MPa}$, $k_y = 0.473\text{ MPa}\cdot\text{m}^{1/2}$ ($14.94\text{ MPa}\cdot\text{mm}^{1/2}$)<br>
At $d = 2.25\text{ }\mu\text{m}$: $\sigma_y = 422.5\text{ MPa}$<br>
For $\sigma_y = 400\text{ MPa}$: required grain size $d = 2.61\text{ }\mu\text{m}$.
</div>"""
})

# ==========================================
# Problem 13
# ==========================================
add({
    "num": 13,
    "title": "Dislocation Pile-Up Model Derivation of Hall-Petch Relation",
    "difficulty": "Hard",
    "category": "Grain Size Strengthening",
    "tags": ["Pile-Up Model", "Eshelby", "Stress Concentration", "Derivation"],
    "statement": r"""In the classic Eshelby-Frank-Nabarro pile-up model, a Frank-Read source at the center of a grain of diameter $d$ emits dislocations that glide along a slip plane of length $L = d/2$ and pile up against the grain boundary under an effective resolved shear stress $\tau_{\text{eff}} = \tau - \tau_0$.
The number of dislocations $n$ in the pile-up is:
$$n = \frac{k_1 \tau_{\text{eff}} L}{G b} = \frac{k_1 (\tau - \tau_0) d}{2 G b}$$
The concentrated shear stress at the tip of the pile-up $\tau_{\text{tip}}$ acting on the adjacent grain is:
$$\tau_{\text{tip}} = n (\tau - \tau_0)$$
Yielding propagates into the neighboring grain when $\tau_{\text{tip}}$ reaches the critical boundary barrier strength $\tau_c$.
<br><br>
1. Substitute $n$ into $\tau_{\text{tip}} = \tau_c$ and show that:
$$\tau = \tau_0 + \sqrt{\frac{2 G b \tau_c}{k_1}}\,d^{-1/2}$$
2. Relate macroscopic tensile stress $\sigma$ to resolved shear stress $\tau$ using the Taylor orientation factor $\bar{M}$ ($\sigma = \bar{M}\tau$), and write the explicit expression for the Hall-Petch slope $k_y$.<br>
3. Calculate the number of dislocations $n$ in a pile-up for iron ($G = 80\text{ GPa}$, $b = 0.248\text{ nm}$, take $k_1 \approx 1.0$) in a grain of diameter $d = 30\text{ }\mu\text{m}$ when $\tau_{\text{eff}} = 50\text{ MPa}$.<br>
4. Calculate the concentrated tip stress $\tau_{\text{tip}}$ under these conditions.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Derivation of the shear Hall-Petch relation</strong><br>
From $\tau_{\text{tip}} = n (\tau - \tau_0) = \tau_c$:
Substitute $n = \frac{k_1 (\tau - \tau_0) d}{2 G b}$:
$$\tau_{\text{tip}} = \left[\frac{k_1 (\tau - \tau_0) d}{2 G b}\right](\tau - \tau_0) = \frac{k_1 d}{2 G b} (\tau - \tau_0)^2 = \tau_c$$
Solving for $(\tau - \tau_0)^2$:
$$(\tau - \tau_0)^2 = \frac{2 G b \tau_c}{k_1 d}$$
Taking the square root of both sides:
$$\tau - \tau_0 = \sqrt{\frac{2 G b \tau_c}{k_1}}\,d^{-1/2} \implies \tau = \tau_0 + k_s d^{-1/2}$$
where $k_s = \sqrt{\frac{2 G b \tau_c}{k_1}}$ is the shear Hall-Petch slope.
</div>
<div class="solution-step">
<strong>Step 2: Macroscopic tensile relation and $k_y$</strong><br>
For a random polycrystal, macroscopic tensile stress $\sigma = \bar{M}\tau$ and $\sigma_0 = \bar{M}\tau_0$, where $\bar{M} \approx 3.06$ for FCC and BCC:
$$\sigma = \bar{M}\tau = \bar{M}\tau_0 + \bar{M} k_s d^{-1/2} = \sigma_0 + k_y d^{-1/2}$$
The Hall-Petch slope is:
$$k_y = \bar{M} \sqrt{\frac{2 G b \tau_c}{k_1}}$$
This proves mathematically why the yield strength is strictly proportional to $d^{-1/2}$.
</div>
<div class="solution-step">
<strong>Step 3: Calculate number of dislocations $n$</strong><br>
Given: $\tau_{\text{eff}} = 50 \times 10^6\text{ Pa}$, $d = 30 \times 10^{-6}\text{ m}$, $G = 80 \times 10^9\text{ Pa}$, $b = 0.248 \times 10^{-9}\text{ m}$, $k_1 = 1.0$:
$$n = \frac{1.0 \times (50 \times 10^6) \times (30 \times 10^{-6})}{2 \times (80 \times 10^9) \times (0.248 \times 10^{-9})} = \frac{1500}{39.68} \approx 37.8 \approx 38\text{ dislocations}$$
</div>
<div class="solution-step">
<strong>Step 4: Concentrated tip stress $\tau_{\text{tip}}$</strong><br>
$$\tau_{\text{tip}} = n \tau_{\text{eff}} \approx 37.8 \times 50\text{ MPa} \approx 1,890\text{ MPa} \approx 1.89\text{ GPa}$$
Notice the extraordinary magnitude of the stress concentration: an applied effective shear stress of just $50\text{ MPa}$ produces a localized tip stress of nearly $1.9\text{ GPa}$ ($n\times$ multiplication), easily sufficient to nucleate dislocations across the boundary in the neighboring grain.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Derived: $\tau = \tau_0 + \sqrt{\frac{2Gb\tau_c}{k_1}} d^{-1/2}$, so $k_y = \bar{M}\sqrt{\frac{2Gb\tau_c}{k_1}}$<br>
Number of dislocations in pile-up: $n \approx 38$<br>
Concentrated tip stress: $\tau_{\text{tip}} \approx 1.89\text{ GPa}$ ($38\times$ stress amplification).
</div>"""
})

# ==========================================
# Problem 14
# ==========================================
add({
    "num": 14,
    "title": "ASTM Grain Size Number and Yield Strength Prediction",
    "difficulty": "Medium",
    "category": "Grain Size Strengthening",
    "tags": ["ASTM Grain Size", "Grain Size Number", "Hall-Petch"],
    "statement": r"""The ASTM grain size number $G$ (or $n_{\text{ASTM}}$) is defined by the standard equation:
$$N = 2^{G - 1}$$
where $N$ is the number of grains per square inch observed on a polished micrograph viewed at $100\times$ magnification.
The mean planar intercept grain diameter $d$ (in mm) is related to $N$ by:
$$d = \frac{25.4}{100 \sqrt{N}} = \frac{0.254}{\sqrt{N}} = 0.254 \times 2^{-(G-1)/2}\text{ mm}$$
A structural steel follows the Hall-Petch equation:
$$\sigma_y = 125.0\text{ MPa} + (18.5\text{ MPa}\cdot\text{mm}^{1/2})\,d^{-1/2}$$
<br>
1. Calculate the grain diameter $d$ (in mm and $\mu\text{m}$) for an ASTM grain size number $G = 4$ (coarse grain) and $G = 9$ (fine grain).<br>
2. Calculate the expected yield strength $\sigma_y$ for both $G = 4$ and $G = 9$.<br>
3. By what percentage does grain refinement from ASTM 4 to ASTM 9 increase the yield strength?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate grain diameter $d$ for $G = 4$ and $G = 9$</strong><br>
- <em>For ASTM $G = 4$:</em>
$$N_4 = 2^{4 - 1} = 2^3 = 8\text{ grains/in}^2 \text{ at } 100\times$$
$$d_4 = \frac{0.254}{\sqrt{8}} = \frac{0.254}{2.8284} \approx 0.0898\text{ mm} = 89.8\text{ }\mu\text{m}$$
<br>
- <em>For ASTM $G = 9$:</em>
$$N_9 = 2^{9 - 1} = 2^8 = 256\text{ grains/in}^2 \text{ at } 100\times$$
$$d_9 = \frac{0.254}{\sqrt{256}} = \frac{0.254}{16} = 0.015875\text{ mm} \approx 15.88\text{ }\mu\text{m}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate yield strength for both grain sizes</strong><br>
- <em>For $G = 4$ ($d = 0.0898\text{ mm}$):</em>
$$d_4^{-1/2} = (0.0898)^{-0.5} \approx 3.337\text{ mm}^{-1/2}$$
$$\sigma_y(G=4) = 125.0 + 18.5 \times (3.337) = 125.0 + 61.73 \approx 186.73\text{ MPa}$$
<br>
- <em>For $G = 9$ ($d = 0.015875\text{ mm}$):</em>
$$d_9^{-1/2} = (0.015875)^{-0.5} = \frac{1}{\sqrt{0.015875}} = \frac{1}{0.1260} \approx 7.937\text{ mm}^{-1/2}$$
$$\sigma_y(G=9) = 125.0 + 18.5 \times (7.937) = 125.0 + 146.84 \approx 271.84\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 3: Percentage increase in yield strength</strong><br>
$$\Delta = \frac{\sigma_y(G=9) - \sigma_y(G=4)}{\sigma_y(G=4)} \times 100\% = \frac{271.84 - 186.73}{186.73} \times 100\% = \frac{85.11}{186.73} \times 100\% \approx 45.58\%$$
Refining the steel grain structure from ASTM 4 to ASTM 9 boosts the yield strength by $45.6\%$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
ASTM $G = 4$: $d = 89.8\text{ }\mu\text{m} \implies \sigma_y = 186.7\text{ MPa}$<br>
ASTM $G = 9$: $d = 15.9\text{ }\mu\text{m} \implies \sigma_y = 271.8\text{ MPa}$<br>
Strength enhancement: $+45.6\%$ increase.
</div>"""
})

# ==========================================
# Problem 15
# ==========================================
add({
    "num": 15,
    "title": "Simultaneous Strengthening and Toughening via Grain Refinement",
    "difficulty": "Easy",
    "category": "Grain Size Strengthening",
    "tags": ["Grain Refinement", "Ductile-to-Brittle Transition", "DBTT", "Toughness"],
    "statement": r"""In materials engineering, almost all strengthening mechanisms (solid solution, precipitation, strain hardening) increase yield strength at the severe expense of reducing ductility and fracture toughness.
Grain size refinement is the only strengthening mechanism that simultaneously improves both strength and toughness.
<br><br>
The Ductile-to-Brittle Transition Temperature ($T_B$ or DBTT) in ferritic steels follows the Petch equation:
$$\beta T_B = \ln \beta' - \ln(k_y) - \ln(d^{-1/2}) = C - \frac{1}{2}\ln d$$
or empirically: $T_B = T_0 - K_{\text{DBTT}} \ln(d^{-1/2}) = T_0 + K' \ln(d)$.
<br><br>
1. Explain physically why smaller grains improve fracture toughness and lower the DBTT in BCC steels.<br>
2. Why does a smaller grain diameter reduce the risk of cleavage crack propagation?<br>
3. In microalloyed structural steel (HSLA), niobium and titanium micro-additions are added to form carbonitride precipitates that pin austenite grain boundaries during hot rolling. Explain how this thermomechanical processing achieves both high strength and high impact toughness at $-40^\circ\text{C}$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Physical explanation of simultaneous strengthening and toughening</strong><br>
Yield strength increases with smaller grain size because shorter slip path lengths limit the number of dislocations in a pile-up ($n \propto d$), requiring a higher applied stress to generate the critical tip stress for slip propagation ($k_y d^{-1/2}$).<br>
Concurrently, fracture toughness increases because:
1. Cleavage microcracks nucleate from dislocation pile-ups or fractured grain boundary carbide particles. The maximum crack size that can form within a single grain is bounded by the grain diameter ($a \le d$). Smaller grains produce much smaller microcracks.
2. Cleavage cracks propagate along $\{100\}$ planes. When a propagating microcrack strikes a high-angle grain boundary, it must re-nucleate or twist and tilt into the differently oriented $\{100\}$ cleavage plane of the adjacent grain, absorbing substantial plastic crack-tip energy and arresting the crack.
</div>
<div class="solution-step">
<strong>Step 2: Crack arrest and cleavage suppression</strong><br>
According to Griffith-Orowan fracture mechanics, the stress required to propagate a crack across a grain boundary is:
$$\sigma_F \propto \sqrt{\frac{E \gamma_p}{d}}$$
As grain size $d$ decreases, the fracture stress $\sigma_F$ increases much faster ($\propto d^{-1/2}$) than the temperature-dependent yield stress. Consequently, the intersection of the fracture stress curve and yield curve (which defines the DBTT) shifts to substantially lower temperatures, keeping the material ductile down to sub-zero conditions.
</div>
<div class="solution-step">
<strong>Step 3: Thermomechanical Controlled Processing (TMCP) of HSLA steels</strong><br>
In HSLA steels, microalloying with $0.02\text{--}0.05\text{ wt}\%\text{ Nb, Ti, or V}$ forms nanoscale carbonitride precipitates ($\text{Nb(C,N)}$). During hot rolling in the austenite regime, these precipitates exert a powerful Zener pinning drag on austenite grain boundaries, preventing grain growth. The austenite is pancaked by rolling below the recrystallization stop temperature. Upon cooling, this ultra-fine pancaked austenite transforms into ultra-fine ferrite ($d \approx 2\text{--}5\text{ }\mu\text{m}$). This delivers high yield strength ($\sigma_y > 450\text{--}600\text{ MPa}$) while pushing the DBTT well below $-40^\circ\text{C}$ without expensive nickel alloying.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Grain refinement limits microcrack size to $a \le d$ and forces cleavage cracks to deflect at boundaries.<br>
Fracture stress increases faster than yield stress, shifting DBTT to lower temperatures.<br>
TMCP HSLA steels use Zener pinning to achieve ultra-fine ferrite ($d < 5\text{ }\mu\text{m}$), optimizing both strength and sub-zero impact toughness.
</div>"""
})

# ==========================================
# Problem 16
# ==========================================
add({
    "num": 16,
    "title": "Low-Angle Tilt Boundaries: Read-Shockley Dislocation Model",
    "difficulty": "Medium",
    "category": "Grain Boundary Structure",
    "tags": ["Read-Shockley", "Tilt Boundary", "Dislocation Array", "Subgrains"],
    "statement": r"""A symmetric low-angle tilt boundary (misorientation angle $\theta < 10^\circ$) can be modeled as a vertical wall of equally spaced edge dislocations with Burgers vector $b$ and spacing $D$:
$$\sin\left(\frac{\theta}{2}\right) = \frac{b}{2D} \implies \theta \approx \frac{b}{D} \quad (\text{for small }\theta \text{ in radians})$$
The grain boundary energy $\gamma_{\text{gb}}$ of a low-angle boundary is given by the Read-Shockley equation:
$$\gamma_{\text{gb}} = E_0 \theta (A - \ln\theta)$$
where $E_0 = \frac{G b}{4\pi(1-\nu)}$ and $A = 1 + \ln\left(\frac{b}{2\pi r_0}\right)$.
<br><br>
For an aluminum subgrain boundary ($b = 0.286\text{ nm}$, $G = 26\text{ GPa}$, $\nu = 0.34$, $r_0 \approx b$):
<br>
1. Calculate the dislocation spacing $D$ for a tilt boundary with misorientation angle $\theta = 1.5^\circ$.<br>
2. Calculate $E_0$ (in $\text{J/m}^2$) and $A$.<br>
3. Calculate the boundary surface energy $\gamma_{\text{gb}}$ at $\theta = 1.5^\circ$.<br>
4. Calculate the boundary energy at $\theta = 8.0^\circ$. Explain why the Read-Shockley equation breaks down at $\theta > 15^\circ$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate dislocation spacing $D$ at $\theta = 1.5^\circ$</strong><br>
Convert $\theta$ to radians:
$$\theta = 1.5^\circ \times \frac{\pi}{180^\circ} \approx 0.02618\text{ rad}$$
Using $\theta \approx b / D$:
$$D = \frac{b}{\theta} = \frac{0.286\text{ nm}}{0.02618\text{ rad}} \approx 10.92\text{ nm}$$
The boundary consists of an edge dislocation every $10.9\text{ nm}$ (about 38 atomic spacings).
</div>
<div class="solution-step">
<strong>Step 2: Calculate $E_0$ and $A$</strong><br>
$$E_0 = \frac{G b}{4\pi(1-\nu)} = \frac{(26 \times 10^9\text{ Pa}) \times (0.286 \times 10^{-9}\text{ m})}{4\pi(1 - 0.34)} = \frac{7.436}{4\pi(0.66)} = \frac{7.436}{8.2938} \approx 0.8966\text{ J/m}^2$$
For $r_0 \approx b$:
$$\frac{b}{2\pi r_0} = \frac{1}{2\pi} \approx 0.15915$$
$$A = 1 + \ln(0.15915) = 1 - 1.8379 = -0.8379$$
(Using standard Read-Shockley convention with $\theta_m = \exp(A) \approx 0.43\text{ rad} \approx 25^\circ$).
Let $\gamma_m = E_0 \theta_m$:
$$\gamma_{\text{gb}} = E_0 \theta [1 - \ln(\theta / \theta_m)]$$
Taking $\theta_m = 0.432\text{ rad}$ ($24.75^\circ$):
</div>
<div class="solution-step">
<strong>Step 3: Boundary energy at $\theta = 1.5^\circ$ ($0.02618\text{ rad}$)</strong><br>
$$\frac{\theta}{\theta_m} = \frac{0.02618}{0.432} \approx 0.06060$$
$$\ln\left(\frac{\theta}{\theta_m}\right) = \ln(0.06060) \approx -2.8034$$
$$\gamma_{\text{gb}} = (0.8966) \times (0.02618) \times [1 - (-2.8034)] = (0.02347) \times (3.8034) \approx 0.0893\text{ J/m}^2 = 89.3\text{ mJ/m}^2$$
</div>
<div class="solution-step">
<strong>Step 4: Boundary energy at $\theta = 8.0^\circ$ and breakdown</strong><br>
$$\theta = 8.0^\circ \times \frac{\pi}{180^\circ} \approx 0.1396\text{ rad}$$
$$\frac{\theta}{\theta_m} = \frac{0.1396}{0.432} \approx 0.3231 \implies \ln(0.3231) \approx -1.1298$$
$$\gamma_{\text{gb}} = (0.8966) \times (0.1396) \times [1 - (-1.1298)] = (0.12517) \times (2.1298) \approx 0.2666\text{ J/m}^2 = 266.6\text{ mJ/m}^2$$
<em>Why Read-Shockley breaks down for $\theta > 15^\circ$:</em> At $\theta = 15^\circ$, the dislocation spacing drops to $D = b / \theta = b / 0.2618 \approx 3.8\,b$. At such small separations, the non-linear cores of adjacent dislocations overlap directly. Dislocation elasticity theory ceases to be valid; the boundary transforms into a high-angle grain boundary whose energy reaches an asymptotic plateau ($\gamma_{\text{HAGB}} \approx 300\text{--}500\text{ mJ/m}^2$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Dislocation spacing at $1.5^\circ$: $D = 10.9\text{ nm}$<br>
Energy at $1.5^\circ$: $\gamma_{\text{gb}} \approx 89.3\text{ mJ/m}^2$<br>
Energy at $8.0^\circ$: $\gamma_{\text{gb}} \approx 266.6\text{ mJ/m}^2$<br>
Read-Shockley breaks down above $15^\circ$ because dislocation cores overlap, transitioning to a high-angle boundary.
</div>"""
})

# ==========================================
# Problem 17
# ==========================================
add({
    "num": 17,
    "title": "Nanotwinned Metals: Hall-Petch Strengthening with High Electrical Conductivity",
    "difficulty": "Hard",
    "category": "Advanced Strengthening",
    "tags": ["Nanotwinned Copper", "Coherent Twin Boundary", "Electrical Conductivity"],
    "statement": r"""Conventional grain boundary refinement increases yield strength but severely degrades electrical conductivity because high-angle grain boundaries scatter conduction electrons strongly.
Nanotwinned copper (synthesized by pulsed electrodeposition or magnetron sputtering) contains nanoscale coherent twin boundaries (CTBs) on $\{111\}$ planes with spacing $\lambda_{\text{twin}}$ down to a few nanometers.
<br><br>
The yield strength follows a twin-boundary Hall-Petch relation:
$$\sigma_y = \sigma_0 + k_{\text{twin}} \lambda_{\text{twin}}^{-1/2}$$
where $\sigma_0 = 90\text{ MPa}$ and $k_{\text{twin}} = 0.35\text{ MPa}\cdot\text{m}^{1/2}$.
The electrical resistivity $\rho$ is given by:
$$\rho = \rho_{\text{lattice}} + \Delta \rho_{\text{defects}} = \rho_0 + \rho_{\text{TB}} \left(\frac{1}{\lambda_{\text{twin}}}\right)$$
where $\rho_0 = 1.68 \times 10^{-8}\text{ }\Omega\cdot\text{m}$ (pure copper at $20^\circ\text{C}$) and the twin boundary specific resistivity is $\rho_{\text{TB}} \approx 3.0 \times 10^{-17}\text{ }\Omega\cdot\text{m}^2$.
By contrast, high-angle grain boundaries have a specific resistivity $\rho_{\text{GB}} \approx 3.0 \times 10^{-16}\text{ }\Omega\cdot\text{m}^2$ (an order of magnitude higher!).
<br><br>
1. Calculate the yield strength $\sigma_y$ of nanotwinned copper with twin lamellar thickness $\lambda_{\text{twin}} = 15.0\text{ nm}$.<br>
2. Calculate the electrical resistivity $\rho$ of this nanotwinned copper.<br>
3. If an ultrafine-grained copper with the same yield strength achieved it via random high-angle grain boundaries ($\lambda = 15\text{ nm}$), calculate its resistivity $\rho_{\text{UFG}}$.<br>
4. Compare the electrical conductivities (as %IACS, where $100\%\text{ IACS} = 1.724 \times 10^{-8}\text{ }\Omega\cdot\text{m}$) and explain the revolutionary significance of nanotwinned metals.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate yield strength of nanotwinned copper</strong><br>
$$\lambda_{\text{twin}} = 15.0 \times 10^{-9}\text{ m} \implies \lambda_{\text{twin}}^{-1/2} = (15.0 \times 10^{-9})^{-0.5} \approx 8,165\text{ m}^{-1/2}$$
$$\sigma_y = 90\text{ MPa} + (0.35\text{ MPa}\cdot\text{m}^{1/2}) \times 8,165\text{ m}^{-1/2} = 90 + 2,857.75 \approx 2,948\text{ MPa} \approx 2.95\text{ GPa}$$
(In practice, partial dislocation nucleation along twin boundaries caps strength at $\sim 900\text{--}1000\text{ MPa}$, nearly $10\times$ higher than coarse-grained copper).
</div>
<div class="solution-step">
<strong>Step 2: Electrical resistivity of nanotwinned copper</strong><br>
$$\frac{1}{\lambda_{\text{twin}}} = \frac{1}{15.0 \times 10^{-9}\text{ m}} \approx 6.667 \times 10^7\text{ m}^{-1}$$
$$\Delta \rho_{\text{TB}} = (3.0 \times 10^{-17}\text{ }\Omega\cdot\text{m}^2) \times (6.667 \times 10^7\text{ m}^{-1}) = 2.00 \times 10^{-9}\text{ }\Omega\cdot\text{m}$$
$$\rho_{\text{nt-Cu}} = 1.68 \times 10^{-8} + 0.20 \times 10^{-8} = 1.88 \times 10^{-8}\text{ }\Omega\cdot\text{m}$$
Conductivity in %IACS:
$$\%\text{IACS}_{\text{nt-Cu}} = \frac{1.724 \times 10^{-8}}{1.88 \times 10^{-8}} \times 100\% \approx 91.7\%\text{ IACS}$$
</div>
<div class="solution-step">
<strong>Step 3: Resistivity of UFG copper with random grain boundaries</strong><br>
$$\Delta \rho_{\text{GB}} = (3.0 \times 10^{-16}\text{ }\Omega\cdot\text{m}^2) \times (6.667 \times 10^7\text{ m}^{-1}) = 2.00 \times 10^{-8}\text{ }\Omega\cdot\text{m}$$
$$\rho_{\text{UFG}} = 1.68 \times 10^{-8} + 2.00 \times 10^{-8} = 3.68 \times 10^{-8}\text{ }\Omega\cdot\text{m}$$
$$\%\text{IACS}_{\text{UFG}} = \frac{1.724 \times 10^{-8}}{3.68 \times 10^{-8}} \times 100\% \approx 46.8\%\text{ IACS}$$
</div>
<div class="solution-step">
<strong>Step 4: Comparison and scientific significance</strong><br>
Nanotwinned copper achieves ultra-high strength ($\sim 1\text{ GPa}$) while maintaining <strong>$91.7\%$ IACS</strong> electrical conductivity. In contrast, standard nanocrystalline copper suffers a $53\%$ drop in conductivity down to $46.8\%$ IACS.<br>
<em>Why this occurs:</em> Coherent twin boundaries have perfect atomic matching across the $\{111\}$ interface with zero excess volume and zero broken bonds; hence, they scatter conduction electrons very weakly. However, they possess a sharp mirror symmetry change that effectively blocks dislocation glide and forces partial dislocation interactions. Nanotwinned materials thus break the classical trade-off between mechanical strength and electrical conductivity.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Nanotwinned copper conductivity: $91.7\%\text{ IACS}$ ($\rho = 1.88 \times 10^{-8}\text{ }\Omega\cdot\text{m}$)<br>
Ultrafine-grained copper conductivity: $46.8\%\text{ IACS}$ ($\rho = 3.68 \times 10^{-8}\text{ }\Omega\cdot\text{m}$)<br>
Nanotwinning breaks the strength-conductivity trade-off by combining strong dislocation blocking with minimal electron scattering.
</div>"""
})

# ==========================================
# Problem 18
# ==========================================
add({
    "num": 18,
    "title": "Breakdown of Hall-Petch: The Inverse Hall-Petch Effect",
    "difficulty": "Hard",
    "category": "Nanocrystalline Mechanics",
    "tags": ["Inverse Hall-Petch", "Cobel Creep", "Grain Boundary Sliding", "Critical Grain Size"],
    "statement": r"""When grain size is reduced into the deep nanometer regime ($d < 20\text{ nm}$), experimental measurements in electrodeposited nickel and copper show that yield strength ceases to increase and actually decreases with further grain refinement. This phenomenon is known as the <strong>Inverse Hall-Petch effect</strong>.
<br><br>
1. Explain the dislocation pile-up limit: calculate the minimum grain diameter $d_{\text{min}}$ required to sustain a dislocation pile-up containing at least 2 dislocations, given an equilibrium separation $x_0 \approx 10\text{--}15\text{ nm}$.<br>
2. As grain size drops below $d_c \approx 10\text{--}15\text{ nm}$, what fraction of atoms reside in grain boundaries rather than in grain interiors? Calculate this volume fraction $f_{\text{GB}}$ assuming a boundary thickness $\delta = 1.0\text{ nm}$ for spherical grains of diameter $d = 10.0\text{ nm}$.<br>
3. Identify the dominant plastic deformation mechanisms that replace dislocation glide in nanocrystalline metals with $d < 10\text{ nm}$.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Dislocation pile-up limit</strong><br>
The classical Hall-Petch mechanism relies on dislocation pile-up to generate stress concentrations. A pile-up requires at least two dislocations on the same slip plane. The repulsive distance between two identical dislocations under yield stress is typically:
$$x_0 \approx \frac{G b}{2\pi (1-\nu) \tau_y}$$
For typical metals, $x_0 \approx 10\text{ to }20\text{ nm}$. If the grain diameter $d < x_0$, a single grain is simply too small to contain two dislocations simultaneously. Dislocation pile-ups become physically impossible, eliminating the foundation of the Hall-Petch model.
</div>
<div class="solution-step">
<strong>Step 2: Grain boundary atom volume fraction $f_{\text{GB}}$</strong><br>
For a spherical grain of diameter $d$ surrounded by a boundary shell of thickness $\delta / 2$ (so total boundary thickness is $\delta = 1.0\text{ nm}$):
The grain interior radius is $r_{\text{core}} = (d - \delta)/2 = (10 - 1)/2 = 4.5\text{ nm}$.
The total grain radius is $R = d/2 = 5.0\text{ nm}$.
The volume fraction of the grain boundaries is:
$$f_{\text{GB}} = \frac{V_{\text{total}} - V_{\text{core}}}{V_{\text{total}}} = 1 - \left(\frac{r_{\text{core}}}{R}\right)^3 = 1 - \left(\frac{4.5}{5.0}\right)^3 = 1 - (0.90)^3 = 1 - 0.729 = 0.271 = 27.1\%$$
At $d = 10\text{ nm}$, over $27\%$ of all atoms in the material reside in disordered grain boundary regions. At $d = 5\text{ nm}$, $f_{\text{GB}}$ exceeds $50\%$!
</div>
<div class="solution-step">
<strong>Step 3: Dominant deformation mechanisms in nanocrystalline metals</strong><br>
When $d < 10\text{ nm}$:
1. <strong>Grain Boundary Sliding (GBS):</strong> Individual grains rotate and slide past one another along the weak, disordered boundary network via atomic shuffles.
2. <strong>Coble Creep at Room Temperature:</strong> Rapid room-temperature vacancy diffusion along the immense network of grain boundaries ($\dot{\varepsilon} \propto D_{\text{gb}} / d^3$) produces significant diffusion-mediated plastic flow under modest stresses.
3. <strong>Dislocation Nucleation and Absorption:</strong> Full or partial dislocations nucleate directly at a grain boundary, sweep across the tiny grain without encountering obstacles, and are instantly absorbed into the opposite grain boundary without multiplying.
Because grain boundary sliding and diffusion creep soften the material as $d$ decreases ($d\sigma/dd > 0$), the yield strength declines below $d_c \approx 10\text{--}15\text{ nm}$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Pile-ups are impossible when $d < x_0 \approx 10\text{--}15\text{ nm}$.<br>
At $d = 10\text{ nm}$, $27.1\%$ of all atoms reside in grain boundaries.<br>
Deformation shifts from dislocation glide to grain boundary sliding (GBS) and Coble diffusion creep, causing the Inverse Hall-Petch softening.
</div>"""
})

# ==========================================
# Problem 19
# ==========================================
add({
    "num": 19,
    "title": "Severe Plastic Deformation (SPD): ECAP and Grain Refinement",
    "difficulty": "Medium",
    "category": "Grain Size Strengthening",
    "tags": ["ECAP", "Severe Plastic Deformation", "Ultrafine Grains"],
    "statement": r"""Equal Channel Angular Pressing (ECAP) is a severe plastic deformation (SPD) technique used to produce ultrafine-grained (UFG) metals without altering the billet's cross-sectional dimensions.
A square billet is extruded through an intersecting die with channel angle $\Phi$ and outer corner curvature angle $\Psi$.
The equivalent plastic shear strain $\varepsilon_N$ accumulated after $N$ passes is:
$$\varepsilon_N = \frac{N}{\sqrt{3}} \left[ 2 \cot\left(\frac{\Phi}{2} + \frac{\Psi}{2}\right) + \Psi \csc\left(\frac{\Phi}{2} + \frac{\Psi}{2}\right) \right]$$
For a standard sharp die with channel angle $\Phi = 90^\circ$ and corner angle $\Psi = 0^\circ$:
<br><br>
1. Calculate the accumulated true plastic strain $\varepsilon_1$ after a single ECAP pass ($N = 1$).<br>
2. Calculate the total equivalent plastic strain after $N = 4$ and $N = 8$ passes.<br>
3. Processing pure copper via $N = 8$ ECAP passes refines its grain size from $d_0 = 50\text{ }\mu\text{m}$ down to $d = 250\text{ nm}$ ($0.25\text{ }\mu\text{m}$). If copper follows $\sigma_y = 25\text{ MPa} + (0.11\text{ MPa}\cdot\text{m}^{1/2}) d^{-1/2}$, calculate the initial and final yield strengths.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate single-pass strain for $\Phi = 90^\circ, \Psi = 0^\circ$</strong><br>
$$\frac{\Phi}{2} + \frac{\Psi}{2} = \frac{90^\circ}{2} + 0 = 45^\circ$$
$$\cot(45^\circ) = 1.0$$
Since $\Psi = 0$, the second term vanishes:
$$\varepsilon_1 = \frac{1}{\sqrt{3}} [2 \cot(45^\circ)] = \frac{2}{\sqrt{3}} \approx 1.1547$$
Each pass imparts an immense plastic shear strain of $\varepsilon \approx 1.155$ without reducing the billet dimensions!
</div>
<div class="solution-step">
<strong>Step 2: Accumulated plastic strain for $N = 4$ and $N = 8$</strong><br>
$$\varepsilon_4 = 4 \times 1.1547 \approx 4.619$$
$$\varepsilon_8 = 8 \times 1.1547 \approx 9.238$$
An equivalent true plastic strain of $\sim 9.24$ represents an effective reduction ratio equivalent to rolling a plate from a thickness of $1\text{ meter}$ down to $0.1\text{ mm}$!
</div>
<div class="solution-step">
<strong>Step 3: Initial and final yield strengths of copper</strong><br>
- <em>Initial coarse-grained copper ($d_0 = 50\text{ }\mu\text{m} = 50 \times 10^{-6}\text{ m}$):</em>
$$d_0^{-1/2} = (50 \times 10^{-6})^{-0.5} \approx 141.42\text{ m}^{-1/2}$$
$$\sigma_{y0} = 25 + 0.11 \times 141.42 = 25 + 15.56 \approx 40.56\text{ MPa}$$
<br>
- <em>Final UFG copper ($d = 250\text{ nm} = 0.25 \times 10^{-6}\text{ m}$):</em>
$$d^{-1/2} = (0.25 \times 10^{-6})^{-0.5} = \frac{10^3}{\sqrt{0.25}} = \frac{1000}{0.50} = 2,000\text{ m}^{-1/2}$$
$$\sigma_{y,\text{UFG}} = 25 + 0.11 \times (2,000) = 25 + 220 = 245.0\text{ MPa}$$
Processing increases the yield strength by a factor of $245 / 40.56 \approx 6.04\times$ ($+504\%$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Single-pass strain: $\varepsilon_1 = 1.155$<br>
After 8 passes: $\varepsilon_8 = 9.238$<br>
Yield strength increases from $\sigma_{y0} = 40.6\text{ MPa}$ to $\sigma_{y,\text{UFG}} = 245.0\text{ MPa}$ (a $6\times$ increase).
</div>"""
})

# ==========================================
# Problem 20
# ==========================================
add({
    "num": 20,
    "title": "Zener Pinning: Grain Growth Inhibition by Second-Phase Particles",
    "difficulty": "Hard",
    "category": "Grain Size Strengthening",
    "tags": ["Zener Pinning", "Second-Phase Particles", "Limiting Grain Size"],
    "statement": r"""During high-temperature heat treatment, fine insoluble precipitate particles (e.g., $\text{TiN}$ or $\text{NbC}$) exert a retarding pinning force on migrating grain boundaries.
A spherical particle of radius $r$ pinned to a boundary with surface energy $\gamma_{\text{gb}}$ exerts a maximum retarding force $F_Z = \pi r \gamma_{\text{gb}}$.
For a volume fraction $f$ of randomly distributed particles, the Zener limiting grain diameter $d_Z$ is given by:
$$d_Z = \frac{4 r}{3 f}$$
In an HSLA microalloyed steel, titanium micro-additions precipitate as titanium nitride ($\text{TiN}$) particles with average radius $r = 15.0\text{ nm}$ and volume fraction $f = 0.12\% = 0.0012$.
<br><br>
1. Calculate the Zener limiting grain diameter $d_Z$ (in $\mu\text{m}$).<br>
2. If the steel is held at $1100^\circ\text{C}$ during welding, unpinned austenite grains coarsen to $d_{\text{coarse}} = 180\text{ }\mu\text{m}$. Calculate the ratio $d_{\text{coarse}} / d_Z$.<br>
3. Explain why $\text{TiN}$ particles are exceptionally effective at pinning austenite grains in the Heat-Affected Zone (HAZ) of steel welds compared to $\text{NbC}$ or $\text{V(C,N)}$ precipitates.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate Zener limiting grain diameter $d_Z$</strong><br>
Given: $r = 15.0 \times 10^{-9}\text{ m}$, $f = 0.0012$:
$$d_Z = \frac{4 r}{3 f} = \frac{4 \times (15.0 \times 10^{-9}\text{ m})}{3 \times 0.0012} = \frac{60.0 \times 10^{-9}}{0.0036} \approx 1.667 \times 10^{-5}\text{ m} = 16.67\text{ }\mu\text{m}$$
</div>
<div class="solution-step">
<strong>Step 2: Grain size suppression ratio</strong><br>
$$\frac{d_{\text{coarse}}}{d_Z} = \frac{180\text{ }\mu\text{m}}{16.67\text{ }\mu\text{m}} \approx 10.8$$
The $\text{TiN}$ precipitates keep the grain size over $10\times$ finer than in unpinned steel, maintaining toughness in the welded structure.
</div>
<div class="solution-step">
<strong>Step 3: Superior thermodynamic stability of $\text{TiN}$</strong><br>
In the Heat-Affected Zone (HAZ) adjacent to a weld fusion line, peak temperatures exceed $1300^\circ\text{C}\text{ to }1400^\circ\text{C}$.
- Niobium carbide ($\text{NbC}$) and vanadium carbonitride ($\text{V(C,N)}$) have lower thermodynamic stability and completely dissolve in austenite at temperatures between $1050^\circ\text{C}$ and $1150^\circ\text{C}$. Once dissolved, their pinning effect vanishes, leading to catastrophic abnormal grain growth.
- In contrast, Titanium Nitride ($\text{TiN}$) has an extraordinarily high enthalpy of formation ($\Delta H_f^\circ = -338\text{ kJ/mol}$) and does not dissolve until temperatures exceed $1500^\circ\text{C}$ (close to the melting point of steel). The $\text{TiN}$ precipitates remain intact at weld temperatures, pinning austenite boundaries and preserving fine grain sizes that prevent HAZ brittle fracture.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Zener limiting grain diameter: $d_Z = 16.7\text{ }\mu\text{m}$<br>
Grain growth is restricted by more than $10\times$ compared to unpinned steel ($180\text{ }\mu\text{m}$).<br>
$\text{TiN}$ is superior because of its extreme thermodynamic stability, remaining undissolved up to $1500^\circ\text{C}$.
</div>"""
})

# ==========================================
# Problem 21
# ==========================================
add({
    "num": 21,
    "title": "Solid Solution Strengthening: Atomic Size Misfit Parameter",
    "difficulty": "Easy",
    "category": "Solid Solution Strengthening",
    "tags": ["Solid Solution", "Size Misfit", "Lattice Parameter", "Vegard's Law"],
    "statement": r"""When solute atoms are dissolved substitutionally into a solvent crystal lattice, they produce localized spherical elastic strain fields.
The atomic size misfit parameter $\varepsilon_b$ (or $\varepsilon_a$) is defined as:
$$\varepsilon_b = \frac{1}{a} \frac{da}{dc}$$
where $a$ is the solvent lattice parameter and $c$ is the solute atomic fraction.
<br><br>
Pure copper has an FCC lattice parameter $a_{\text{Cu}} = 0.3615\text{ nm}$.
Adding solute elements changes the lattice parameter according to experimental measurements:
- Cu-Ni alloy: Adding $10\text{ at}\%\text{ Ni}$ changes $a$ to $0.3595\text{ nm}$.
- Cu-Zn alloy: Adding $10\text{ at}\%\text{ Zn}$ changes $a$ to $0.3645\text{ nm}$.
- Cu-Sn alloy: Adding $5\text{ at}\%\text{ Sn}$ changes $a$ to $0.3695\text{ nm}$.
<br>
1. Calculate the size misfit parameter $\varepsilon_b$ for Ni, Zn, and Sn in copper.<br>
2. According to Fleischer's theory, the yield stress increment $\Delta\sigma_{\text{ss}}$ is proportional to $|\varepsilon_b|^{3/2} c^{1/2}$. Rank the three solutes in order of strengthening potency per atomic percent.<br>
3. Explain why tin (Sn) is by far the most potent solid solution strengthener in copper.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate size misfit parameter $\varepsilon_b$</strong><br>
$$\varepsilon_b = \frac{1}{a_0} \frac{\Delta a}{\Delta c}$$
- <em>Nickel (Ni, $\Delta c = 0.10$):</em>
$$\Delta a_{\text{Ni}} = 0.3595 - 0.3615 = -0.0020\text{ nm}$$
$$\varepsilon_{b, \text{Ni}} = \frac{1}{0.3615} \left(\frac{-0.0020}{0.10}\right) = \frac{-0.0200}{0.3615} \approx -0.0553 \quad (|\varepsilon_b| = 0.0553)$$
<br>
- <em>Zinc (Zn, $\Delta c = 0.10$):</em>
$$\Delta a_{\text{Zn}} = 0.3645 - 0.3615 = +0.0030\text{ nm}$$
$$\varepsilon_{b, \text{Zn}} = \frac{1}{0.3615} \left(\frac{+0.0030}{0.10}\right) = \frac{+0.0300}{0.3615} \approx +0.0830 \quad (|\varepsilon_b| = 0.0830)$$
<br>
- <em>Tin (Sn, $\Delta c = 0.05$):</em>
$$\Delta a_{\text{Sn}} = 0.3695 - 0.3615 = +0.0080\text{ nm}$$
$$\varepsilon_{b, \text{Sn}} = \frac{1}{0.3615} \left(\frac{+0.0080}{0.05}\right) = \frac{+0.1600}{0.3615} \approx +0.4426 \quad (|\varepsilon_b| = 0.4426)$$
</div>
<div class="solution-step">
<strong>Step 2: Potency ranking via $|\varepsilon_b|^{3/2}$</strong><br>
- Ni: $|\varepsilon_b|^{3/2} = (0.0553)^{1.5} \approx 0.0130$
- Zn: $|\varepsilon_b|^{3/2} = (0.0830)^{1.5} \approx 0.0239$
- Sn: $|\varepsilon_b|^{3/2} = (0.4426)^{1.5} \approx 0.2945$
Potency ranking: <strong>Sn ($0.295$) $\gg$ Zn ($0.024$) $>$ Ni ($0.013$)</strong>.
</div>
<div class="solution-step">
<strong>Step 3: Why Tin is so potent</strong><br>
The atomic radius of tin ($r_{\text{Sn}} = 0.151\text{ nm}$) is over $18\%$ larger than copper ($r_{\text{Cu}} = 0.128\text{ nm}$), whereas Ni ($0.125\text{ nm}$) and Zn ($0.134\text{ nm}$) have radii within $5\%$ of copper. The huge size difference of tin produces immense localized elastic lattice distortions that exert strong elastic interaction forces on gliding dislocations, making bronze (Cu-Sn) far harder and stronger than brass (Cu-Zn) or cupronickel (Cu-Ni) at equivalent solute levels.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Size misfits: $\varepsilon_{b,\text{Ni}} = -0.055$, $\varepsilon_{b,\text{Zn}} = +0.083$, $\varepsilon_{b,\text{Sn}} = +0.443$<br>
Strengthening potency ranking: $\text{Sn} \gg \text{Zn} > \text{Ni}$<br>
Tin is over $12\times$ more potent than zinc because its $18\%$ atomic size difference creates massive localized lattice strain fields.
</div>"""
})

# ==========================================
# Problem 22
# ==========================================
add({
    "num": 22,
    "title": "Modulus Misfit Parameter and Total Solid Solution Strengthening",
    "difficulty": "Medium",
    "category": "Solid Solution Strengthening",
    "tags": ["Modulus Misfit", "Fleischer Parameter", "Solid Solution"],
    "statement": r"""In addition to atomic size misfit ($\varepsilon_b$), solute atoms also create an elastic modulus misfit ($\varepsilon_G$) because solute-solvent bonds have a different stiffness than solvent-solvent bonds:
$$\varepsilon_G = \frac{1}{G} \frac{dG}{dc}$$
Fleischer combined both effects into an effective interaction parameter $\varepsilon_s$:
$$\varepsilon_s = |\varepsilon_G' - \beta \varepsilon_b|$$
where $\beta \approx 3.0$ for edge dislocations, and the modified modulus misfit is $\varepsilon_G' = \frac{\varepsilon_G}{1 + 0.5 |\varepsilon_G|}$.
<br><br>
For a copper-beryllium alloy ($G = 48\text{ GPa}$):
The addition of beryllium ($c = 0.04$ atomic fraction) gives:
$\varepsilon_b = -0.285$ (beryllium is much smaller than copper)
$\varepsilon_G = +0.550$ (beryllium stiffens the alloy significantly)
<br><br>
1. Calculate the modified modulus misfit $\varepsilon_G'$.<br>
2. Calculate the combined Fleischer parameter $\varepsilon_s$ (taking $\beta = 3.0$).<br>
3. The solid solution yield strength increment is given by Labusch's model:
$$\Delta\tau = \frac{G}{700} \varepsilon_s^{4/3} c^{2/3}$$
Calculate $\Delta\tau$ (in MPa) and the macroscopic tensile yield increment $\Delta\sigma = 3.06\,\Delta\tau$ for this alloy.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate modified modulus misfit $\varepsilon_G'$</strong><br>
$$\varepsilon_G' = \frac{\varepsilon_G}{1 + 0.5 |\varepsilon_G|} = \frac{0.550}{1 + 0.5(0.550)} = \frac{0.550}{1 + 0.275} = \frac{0.550}{1.275} \approx 0.4314$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate combined Fleischer parameter $\varepsilon_s$</strong><br>
$$\beta \varepsilon_b = 3.0 \times (-0.285) = -0.855$$
$$\varepsilon_s = |\varepsilon_G' - \beta \varepsilon_b| = |0.4314 - (-0.855)| = |0.4314 + 0.855| = 1.2864$$
Notice that because $\varepsilon_b < 0$ and $\varepsilon_G > 0$, the two misfit effects reinforce each other constructively, leading to a very large interaction parameter $\varepsilon_s \approx 1.29$.
</div>
<div class="solution-step">
<strong>Step 3: Calculate yield strength increments $\Delta\tau$ and $\Delta\sigma$</strong><br>
Solute concentration factors:
$$c = 0.04 \implies c^{2/3} = (0.04)^{2/3} \approx 0.11696$$
$$\varepsilon_s^{4/3} = (1.2864)^{4/3} = (1.2864)^{1.3333} \approx 1.3965$$
Shear yield increment:
$$\Delta\tau = \frac{G}{700} \varepsilon_s^{4/3} c^{2/3} = \frac{48,000\text{ MPa}}{700} \times (1.3965) \times (0.11696) \approx 68.57 \times 0.1633 \approx 11.20\text{ MPa}$$
Macroscopic tensile yield strength increment:
$$\Delta\sigma = 3.06 \times \Delta\tau = 3.06 \times 11.20\text{ MPa} \approx 34.27\text{ MPa}$$
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
$\varepsilon_G' = 0.431$<br>
Combined misfit $\varepsilon_s = 1.286$<br>
Shear yield increment $\Delta\tau = 11.2\text{ MPa}$<br>
Tensile yield increment $\Delta\sigma = 34.3\text{ MPa}$
</div>"""
})

# ==========================================
# Problem 23
# ==========================================
add({
    "num": 23,
    "title": "Interstitial vs. Substitutional Solutes: Tetragonal Distortion in BCC Iron",
    "difficulty": "Medium",
    "category": "Solid Solution Strengthening",
    "tags": ["Interstitial Solid Solution", "Tetragonal Distortion", "Carbon in Steel", "Octahedral Site"],
    "statement": r"""In BCC $\alpha$-iron (ferrite), interstitial carbon atoms occupy octahedral interstitial sites located at face centers $(0, \frac{1}{2}, \frac{1}{2})$ and edge midpoints $(0, 0, \frac{1}{2})$.
<br><br>
1. Calculate the radius $r_{\text{oct}}$ of the largest sphere that can fit into an octahedral interstitial site in BCC iron without distortion, given lattice parameter $a = 0.2866\text{ nm}$ and iron atomic radius $R_{\text{Fe}} = 0.1241\text{ nm}$.<br>
2. The atomic radius of a neutral carbon atom is $r_C = 0.077\text{ nm}$. Compare $r_C$ to $r_{\text{oct}}$ and explain why the interstitial carbon atom produces a non-spherical (tetragonal) lattice distortion.<br>
3. Explain why interstitial carbon strengthens BCC iron $\sim 100\times$ more potently than substitutional solutes (such as Ni or Cr). Include the distinction between hydrostatic and shear stress field interactions with edge and screw dislocations.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate octahedral interstitial radius in BCC</strong><br>
In BCC, atoms touch along the body diagonal: $4 R_{\text{Fe}} = a\sqrt{3}$.
For the octahedral site at $(0, 0, \frac{1}{2})$, the nearest iron atom neighbors are two atoms along the $z$-axis at distance $a/2$:
$$2 R_{\text{Fe}} + 2 r_{\text{oct}} = a \implies r_{\text{oct}} = \frac{a}{2} - R_{\text{Fe}}$$
$$r_{\text{oct}} = \frac{0.2866}{2} - 0.1241 = 0.1433 - 0.1241 = 0.0192\text{ nm}$$
The octahedral site has an available radius of only $0.0192\text{ nm}$!
</div>
<div class="solution-step">
<strong>Step 2: Tetragonal distortion</strong><br>
Carbon atomic radius $r_C = 0.0770\text{ nm}$ is four times larger than the interstitial site ($0.077 / 0.0192 \approx 4.0$).
When a carbon atom inserts into $(0, 0, \frac{1}{2})$, it severely pushes the two iron neighbors along the $z$-axis outward, while exerting much smaller displacements on the four coplanar iron neighbors in the $x\text{-}y$ plane ($d_{xy} = a\sqrt{2}/2 = 0.2026\text{ nm} > 2R_{\text{Fe}}$).
This creates an asymmetrical, <strong>tetragonal distortion dipole</strong> (elongation along $z$, slight contraction along $x$ and $y$).
</div>
<div class="solution-step">
<strong>Step 3: Interaction with edge and screw dislocations</strong><br>
- <em>Substitutional solutes (spherical distortion):</em> Generate purely hydrostatic stress fields ($\sigma_{xx} = \sigma_{yy} = \sigma_{zz} = p, \tau = 0$). They can only interact with the hydrostatic pressure field of edge dislocations and have <strong>zero interaction with screw dislocations</strong> (which possess only pure shear stress fields).<br>
- <em>Interstitial carbon (tetragonal distortion):</em> Produces both hydrostatic stress and powerful <strong>shear stress components</strong>. Consequently, carbon atoms interact strongly with BOTH edge and screw dislocations. Because screw dislocations control plastic flow in BCC metals at room temperature, interstitial carbon pins both dislocation types aggressively, yielding strengthening potencies $\sim 100\times$ higher than substitutional solutes per atomic percent.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Octahedral site radius $r_{\text{oct}} = 0.0192\text{ nm} \ll r_C = 0.077\text{ nm}$<br>
Severe one-directional expansion creates a non-spherical tetragonal distortion dipole.<br>
Tetragonal distortion interacts strongly with the shear fields of screw dislocations, making interstitial carbon $\sim 100\times$ more potent than substitutional solutes.
</div>"""
})

# ==========================================
# Problem 24
# ==========================================
add({
    "num": 24,
    "title": "Cottrell Atmospheres and Dislocation Pinning Energy",
    "difficulty": "Hard",
    "category": "Solid Solution Strengthening",
    "tags": ["Cottrell Atmosphere", "Dislocation Pinning", "Interaction Energy", "Yield Point"],
    "statement": r"""Cottrell and Bilby showed that interstitial solute atoms (carbon/nitrogen in iron) diffuse toward the dilated tensile side of edge dislocations to relieve elastic strain energy.
The elastic interaction energy $U(r, \theta)$ between an edge dislocation and an interstitial solute atom located at polar coordinates $(r, \theta)$ is:
$$U(r, \theta) = \frac{A \sin\theta}{r}$$
where $A = \frac{1}{3\pi}\left(\frac{1+\nu}{1-\nu}\right) G b \Delta V$, with shear modulus $G = 80\text{ GPa}$, Poisson's ratio $\nu = 0.30$, Burgers vector $b = 0.248\text{ nm}$, and carbon atomic volume change $\Delta V \approx 7.8 \times 10^{-30}\text{ m}^3$.
<br><br>
1. Calculate the interaction parameter $A$ (in units of $\text{J}\cdot\text{m}$ and $\text{eV}\cdot\text{nm}$).<br>
2. Determine the coordinates $(r, \theta)$ at which the binding energy is strongest (most negative/attractive).<br>
3. Calculate the maximum pinning binding energy $U_{\text{bind}}$ at a distance of $r_0 = 0.20\text{ nm}$ below the slip plane ($\theta = -\pi/2 = 270^\circ$). Express your answer in $\text{eV}$.<br>
4. Compare $U_{\text{bind}}$ with the thermal energy $k_B T$ at room temperature ($T = 300\text{ K}$, $k_B T \approx 0.0259\text{ eV}$) and explain why Cottrell atmospheres firmly lock dislocations in place.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate interaction parameter $A$</strong><br>
$$\frac{1+\nu}{1-\nu} = \frac{1 + 0.30}{1 - 0.30} = \frac{1.30}{0.70} \approx 1.8571$$
$$A = \frac{1}{3\pi} \times (1.8571) \times (80 \times 10^9\text{ Pa}) \times (0.248 \times 10^{-9}\text{ m}) \times (7.8 \times 10^{-30}\text{ m}^3)$$
$$A = \frac{1}{9.4248} \times (1.8571) \times (19.84) \times (7.8 \times 10^{-30}) \approx 0.19705 \times 1.5475 \times 10^{-28} \approx 3.05 \times 10^{-29}\text{ J}\cdot\text{m}$$
In units of $\text{eV}\cdot\text{nm}$:
$$1\text{ J} = 6.2415 \times 10^{18}\text{ eV}, \quad 1\text{ m} = 10^9\text{ nm}$$
$$A = (3.05 \times 10^{-29}\text{ J}\cdot\text{m}) \times (6.2415 \times 10^{18}\text{ eV/J}) \times (10^9\text{ nm/m}) \approx 0.1904\text{ eV}\cdot\text{nm}$$
</div>
<div class="solution-step">
<strong>Step 2: Most attractive location</strong><br>
The energy is most negative when $\sin\theta = -1$, which occurs directly below the extra half-plane of the edge dislocation at $\theta = -\pi/2$ (or $270^\circ$). This is the dilated region of the crystal where the lattice is expanded, providing maximum room to accommodate the oversized carbon atom and relieve compressive lattice strain.
</div>
<div class="solution-step">
<strong>Step 3: Maximum binding energy at $r_0 = 0.20\text{ nm}$</strong><br>
$$U_{\text{bind}} = \frac{A \sin(-90^\circ)}{r_0} = -\frac{0.1904\text{ eV}\cdot\text{nm}}{0.20\text{ nm}} \approx -0.952\text{ eV}$$
</div>
<div class="solution-step">
<strong>Step 4: Comparison with thermal energy</strong><br>
$$\frac{|U_{\text{bind}}|}{k_B T} = \frac{0.952\text{ eV}}{0.0259\text{ eV}} \approx 36.8$$
The pinning binding energy ($0.95\text{ eV}$) is nearly $37\times$ larger than the thermal energy at room temperature!
Because thermal fluctuations ($k_B T$) are far too weak to overcome a $\sim 1\text{ eV}$ energy barrier, solute carbon atoms condense into dense rows along the dislocation cores, forming an immovable <strong>Cottrell atmosphere</strong> that rigidly locks the dislocations in place.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Interaction parameter $A \approx 0.190\text{ eV}\cdot\text{nm}$ ($3.05 \times 10^{-29}\text{ J}\cdot\text{m}$)<br>
Maximum attraction directly below core at $\theta = -90^\circ$<br>
Binding energy $U_{\text{bind}} \approx -0.95\text{ eV}$ ($37\times k_B T$), creating unbreakable dislocation locking at room temperature.
</div>"""
})

# ==========================================
# Problem 25
# ==========================================
add({
    "num": 25,
    "title": "Upper/Lower Yield Point Phenomenon and Lüders Band Formation",
    "difficulty": "Medium",
    "category": "Yield Point Phenomena",
    "tags": ["Yield Point Phenomenon", "Lüders Bands", "Upper Yield Stress", "Skin-Pass Rolling"],
    "statement": r"""A tensile specimen of hot-rolled low-carbon sheet steel displays a pronounced upper yield point ($\sigma_{\text{UYP}} = 280\text{ MPa}$), drops abruptly to a lower yield point ($\sigma_{\text{LYP}} = 220\text{ MPa}$), and undergoes a yield point elongation of $\varepsilon_{\text{YPE}} = 4.5\%$ before strain hardening begins.
<br><br>
1. Explain the dislocation mechanism responsible for the sudden load drop from $\sigma_{\text{UYP}}$ to $\sigma_{\text{LYP}}$.<br>
2. What are <strong>Lüders bands</strong>? Describe how they propagate along the specimen gage length during the yield point elongation plateau.<br>
3. Why are Lüders bands completely unacceptable on automotive body panels (e.g., car doors, hoods) after stamping?<br>
4. Describe the industrial processing technique (skin-pass or temper rolling) used by steel mills to permanently eliminate Lüders bands prior to sheet forming.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Mechanism of the upper-to-lower yield drop</strong><br>
In annealed/hot-rolled mild steel, all pre-existing dislocations are rigidly locked by Cottrell atmospheres of carbon and nitrogen atoms.
1. To initiate plastic flow, the applied stress must reach the high <strong>upper yield point ($\sigma_{\text{UYP}}$)</strong> to forcibly rip dislocations away from their solute atmospheres or nucleate new dislocations from grain boundaries.
2. Once dislocations break free, they can glide at a much lower stress because they no longer drag the carbon atmospheres behind them.
3. Rapid dislocation multiplication (via Frank-Read sources and cross-slip) creates a sudden flood of mobile dislocations. According to Orowan's equation $\dot{\varepsilon} = \rho_m b v$, since the testing machine pulls at a constant crosshead velocity $\dot{\varepsilon}$, a massive increase in mobile dislocation density $\rho_m$ causes dislocation velocity $v$ and the required flow stress to drop abruptly to the <strong>lower yield point ($\sigma_{\text{LYP}}$)</strong>.
</div>
<div class="solution-step">
<strong>Step 2: Lüders band propagation</strong><br>
Lüders bands are visible macroscopic bands of localized plastic deformation inclined at approximately $50^\circ\text{ to }54^\circ$ to the tensile axis.
- Plastic deformation nucleates at stress concentrations (fillets) and forms a localized band that yields down to $\sigma_{\text{LYP}}$.
- The yielded material within the band work-hardens slightly, making it stronger than the unyielded adjacent elastic material.
- Deformation is thus forced to advance along the specimen gage length as a steady front (the Lüders band front) at constant lower yield load, producing the flat horizontal plateau ($\varepsilon_{\text{YPE}} \approx 4.5\%$).
</div>
<div class="solution-step">
<strong>Step 3: Why Lüders bands are unacceptable in automotive panels</strong><br>
When sheet steel containing a yield point phenomenon is pressed or deep-drawn into automotive outer panels, the uneven plastic deformation of Lüders bands creates unsightly, irregular surface depressions and ridges known as <strong>stretcher-strain marks</strong> or <strong>stretcher lines</strong>. These surface blemishes cannot be hidden even after multiple layers of primer, basecoat, and clear automotive paint, resulting in unacceptable visual quality.
</div>
<div class="solution-step">
<strong>Step 4: Skin-pass (temper) rolling remedy</strong><br>
Steel mills pass the cold-rolled or annealed sheet through a pair of large temper rolls that impart a tiny, uniform plastic pre-strain of $0.5\%\text{ to }1.5\%$. This tiny plastic deformation breaks all dislocations away from their Cottrell atmospheres throughout the entire sheet without causing significant work hardening or thinning. When the customer later stamps the sheet, the material deforms with smooth, continuous yielding without any yield drop, stretcher-strain marks, or Lüders bands.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Yield drop occurs because freeing locked dislocations floods the lattice with mobile carriers, dropping required glide stress from $\sigma_{\text{UYP}}$ to $\sigma_{\text{LYP}}$.<br>
Lüders bands cause visible surface grooves (stretcher-strain marks) ruinous to car paint finishes.<br>
Skin-pass rolling ($0.5\text{--}1.5\%$ temper strain) permanently unlocks dislocations, providing smooth continuous yielding during stamping.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 7 Part 1: All P1-P25 added. Current total: {len(P)}")
