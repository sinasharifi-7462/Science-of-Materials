# generator/make_ch4_part2.py
# ==============================================================================
# CHAPTER 4: IMPERFECTIONS IN SOLIDS - PART 2 (PROBLEMS 26 TO 50)
# Course: Science of Materials | University of Tehran | Prof. Sadeghi
# Prepared by TA Sina Sharifi
# ==============================================================================

import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_ch4_part1

P = make_ch4_part1.P
add = make_ch4_part1.add

# P26: Edge Dislocation Geometry
add(26, "The Edge Dislocation: Extra Half-Plane, Burgers Vector, and Slip Geometry",
    "Linear Defects & Dislocations", "dislocations", "Fundamental",
    r"""<p>The edge dislocation is the most intuitive geometric model of an atomic line defect.</p>
    <ol type="a">
      <li>Describe the crystal geometry of an <strong>edge dislocation</strong> using the concept of an extra half-plane of atoms.</li>
      <li>State the geometric relationship between the <strong>dislocation line vector $\mathbf{t}$</strong> and the <strong>Burgers vector $\mathbf{b}$</strong> for a pure edge dislocation.</li>
      <li>Define the <strong>slip plane</strong> and the <strong>slip direction</strong> for an edge dislocation. Why is the slip plane uniquely defined for an edge dislocation?</li>
      <li>Distinguish between a positive edge dislocation ($\perp$) and a negative edge dislocation ($\top$). How do they move under an identical applied shear stress?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Geometry of an Edge Dislocation</div>
      <p>An edge dislocation is created by inserting an extra half-plane of atoms into a crystal, terminating abruptly along an internal line within the lattice. The boundary line marking the bottom edge of this extra half-plane is the <strong>dislocation line</strong>. Above the slip plane, atomic planes are compressed together to accommodate the extra sheet; below the slip plane, atomic planes are pulled apart into tension.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Vector Relationship ($\mathbf{b} \perp \mathbf{t}$)</div>
      <p>For a pure edge dislocation, the Burgers vector $\mathbf{b}$ (the vector defining the magnitude and direction of lattice displacement) is strictly <strong>perpendicular</strong> to the dislocation line vector $\mathbf{t}$:</p>
      $$\mathbf{b} \perp \mathbf{t} \quad (\mathbf{b} \cdot \mathbf{t} = 0)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Slip Plane and Slip Direction</div>
      <ul>
        <li><strong>Slip Direction:</strong> Aligned parallel to the Burgers vector $\mathbf{b}$.</li>
        <li><strong>Slip Plane:</strong> The crystallographic plane containing both the dislocation line vector $\mathbf{t}$ and the Burgers vector $\mathbf{b}$. Its unit normal vector is $\mathbf{n} = \frac{\mathbf{t} \times \mathbf{b}}{|\mathbf{t} \times \mathbf{b}|}$.</li>
        <li><strong>Uniqueness:</strong> Because two non-parallel intersecting lines uniquely define a plane in 3D geometry, an edge dislocation has a <strong>single, unique slip plane</strong>. It cannot leave this plane conservatively.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Positive ($\perp$) vs. Negative ($\top$) Edge Dislocations</div>
      <ul>
        <li><strong>Positive Edge Dislocation ($\perp$):</strong> The extra half-plane of atoms lies <em>above</em> the slip plane. Under a positive applied shear stress $\tau$, it glides in the direction of the applied shear stress on top.</li>
        <li><strong>Negative Edge Dislocation ($\top$):</strong> The extra half-plane of atoms lies <em>below</em> the slip plane. Under the same positive shear stress $\tau$, it glides in the <em>opposite</em> direction.</li>
        <li>Both motions produce an identical macroscopic forward shear displacement of magnitude $b$ across the specimen.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Edge Dislocation:</strong> Extra half-plane of atoms &bull; $\mathbf{b} \perp \mathbf{t}$ (strictly perpendicular).<br>
      <strong>Slip Plane:</strong> Uniquely defined by $\mathbf{t} \times \mathbf{b}$ &bull; Slip direction $\parallel \mathbf{b}$.<br>
      Positive ($\perp$) and negative ($\top$) dislocations glide in opposite directions under the same shear stress.
    </div>""")

# P27: Stress Field of an Edge Dislocation
add(27, "Stress Field of an Edge Dislocation and Solute Pinning (Cottrell Atmospheres)",
    "Linear Defects & Dislocations", "dislocations", "Advanced",
    r"""<p>The elastic distortion surrounding an edge dislocation generates an asymmetric internal stress field that interacts strongly with dissolved solute atoms.</p>
    <ol type="a">
      <li>Write down the polar coordinate expressions $(\sigma_{rr}, \sigma_{\theta\theta}, \sigma_{r\theta})$ for the stress field of an edge dislocation oriented along the $z$-axis with Burgers vector along $x$.</li>
      <li>Calculate the hydrostatic stress $\sigma_h = \frac{1}{3}(\sigma_{xx} + \sigma_{yy} + \sigma_{zz})$ surrounding the edge dislocation, identifying where hydrostatic compression and hydrostatic tension are maximized.</li>
      <li>Explain how this stress field drives the segregation of oversized (e.g., carbon in steel) and undersized solute atoms, forming a <strong>Cottrell atmosphere</strong>.</li>
      <li>How does the Cottrell atmosphere explain the sharp <strong>upper and lower yield points</strong> and <strong>Lüders strain bands</strong> in low-carbon mild steels?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Elastic Stress Field Equations in Polar Coordinates</div>
      <p>In linear isotropic elasticity, the stresses surrounding a straight edge dislocation are:</p>
      $$\sigma_{rr} = \sigma_{\theta\theta} = -\frac{G b}{2\pi(1-\nu)} \frac{\sin\theta}{r}$$
      $$\sigma_{r\theta} = \frac{G b}{2\pi(1-\nu)} \frac{\cos\theta}{r}$$
      $$\sigma_{zz} = \nu(\sigma_{rr} + \sigma_{\theta\theta}) = -\frac{2\nu G b}{2\pi(1-\nu)} \frac{\sin\theta}{r}$$
      <p>where $G$ is the shear modulus, $\nu$ is Poisson's ratio, and $\theta$ is the angle measured from the slip direction ($x$-axis).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Hydrostatic Stress $\sigma_h$</div>
      $$\sigma_h = \frac{\sigma_{xx} + \sigma_{yy} + \sigma_{zz}}{3} = \frac{1 + \nu}{3} (\sigma_{rr} + \sigma_{\theta\theta}) = -\frac{(1+\nu) G b}{3\pi(1-\nu)} \frac{\sin\theta}{r}$$
      <ul>
        <li><strong>Above the Slip Plane ($0 < \theta < 180^\circ \implies \sin\theta > 0$):</strong> $\sigma_h < 0$, representing an intense <strong>hydrostatic compressive stress region</strong> (maximum compression directly above at $\theta = 90^\circ$).</li>
        <li><strong>Below the Slip Plane ($180^\circ < \theta < 360^\circ \implies \sin\theta < 0$):</strong> $\sigma_h > 0$, representing an intense <strong>hydrostatic tensile stress region</strong> (maximum dilation directly below at $\theta = 270^\circ$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Cottrell Atmosphere Formation</div>
      <p>Oversized interstitial or substitutional solute atoms (such as carbon or nitrogen in iron) introduce local compressive dilatational strain. When an oversized solute migrates into the expanded <strong>tensile region below the slip plane</strong> ($\theta = 270^\circ$), its positive volume misfit relieves the lattice tensile strain, drastically lowering the total elastic strain energy of the crystal ($\Delta U = -p \Delta V < 0$). Driven by this thermodynamic driving force, solute atoms diffuse toward the dislocation core, forming a dense condensed solute cloud termed a <strong>Cottrell atmosphere</strong> that firmly locks (pins) the dislocation in place.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Upper/Lower Yield Point and Lüders Bands</div>
      <ul>
        <li><strong>Upper Yield Point:</strong> To initiate plastic deformation, an exceptionally high shear stress is required to tear the pinned dislocation away from its anchoring Cottrell solute atmosphere.</li>
        <li><strong>Lower Yield Point:</strong> The instant the dislocation tears free, it moves through the crystal matrix at a much lower glide stress, causing an abrupt load drop on the tensile stress-strain curve.</li>
        <li><strong>Lüders Bands:</strong> The unpinned dislocations multiply rapidly via Frank-Read sources, nucleating localized bands of concentrated plastic deformation (Lüders bands) that propagate along the tensile gauge section at constant lower yield stress until the entire specimen has deformed.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Hydrostatic Stress:</strong> $$\sigma_h = -\frac{(1+\nu)Gb}{3\pi(1-\nu)}\frac{\sin\theta}{r}$$
      Compression above ($\theta = 90^\circ$); Tension below ($\theta = 270^\circ$).<br>
      <strong>Cottrell Atmosphere:</strong> Oversized solutes segregate to the tensile zone, pinning dislocations and causing the <strong>upper/lower yield phenomenon</strong> in low-carbon steel.
    </div>""")

# P28: Screw Dislocation Geometry
add(28, "The Screw Dislocation: Helical Ramp Geometry and Cross-Slip Mechanics",
    "Linear Defects & Dislocations", "dislocations", "Fundamental",
    r"""<p>The screw dislocation represents a topological defect that transforms flat parallel crystallographic planes into a continuous spiral ramp.</p>
    <ol type="a">
      <li>Describe the crystal geometry of a <strong>screw dislocation</strong> using the helical ramp model.</li>
      <li>State the vector relationship between the dislocation line vector $\mathbf{t}$ and the Burgers vector $\mathbf{b}$ for a pure screw dislocation.</li>
      <li>Contrast edge and screw dislocations regarding the uniqueness of their slip planes.</li>
      <li>Explain the phenomenon of <strong>cross-slip</strong>. Why can screw dislocations cross-slip while edge dislocations cannot?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Geometry of a Screw Dislocation</div>
      <p>A screw dislocation is formed by cutting a crystal partially along a plane and shifting one side parallel to the cut edge by one Burgers vector $\mathbf{b}$ relative to the other. Atomic planes perpendicular to the dislocation line are no longer flat parallel discs; instead, they join into a single, continuous, unbroken <strong>helical ramp (Archimedean screw)</strong>. One complete $360^\circ$ circuit around the dislocation line shifts the observer exactly one lattice pitch $b$ along the line.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Vector Relationship ($\mathbf{b} \parallel \mathbf{t}$)</div>
      <p>For a pure screw dislocation, the Burgers vector $\mathbf{b}$ is strictly <strong>parallel (collinear)</strong> to the dislocation line vector $\mathbf{t}$:</p>
      $$\mathbf{b} \parallel \mathbf{t} \quad (\mathbf{b} \times \mathbf{t} = \mathbf{0})$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Uniqueness of Slip Planes</div>
      <ul>
        <li>For an <strong>edge dislocation</strong>, $\mathbf{b}$ and $\mathbf{t}$ are perpendicular, uniquely defining a single plane ($\mathbf{n} \parallel \mathbf{t} \times \mathbf{b}$).</li>
        <li>For a <strong>screw dislocation</strong>, $\mathbf{b}$ and $\mathbf{t}$ are parallel. Because any plane passing through a line contains that line, <strong>any crystallographic plane containing the screw dislocation line can serve as a potential slip plane</strong>! There is no unique slip plane mathematically defined by $\mathbf{t} \times \mathbf{b}$.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Cross-Slip Mechanics</div>
      <p>When a gliding screw dislocation encounters an impenetrable obstacle (e.g., a precipitate or second-phase particle) on its primary slip plane, it does not become permanently blocked. Because its Burgers vector is parallel to the line, the screw dislocation can seamlessly switch glide onto an intersecting slip plane that shares the same Burgers vector $\mathbf{b}$. This non-planar bypass maneuver is called <strong>cross-slip</strong>. Edge dislocations cannot cross-slip because leaving their unique slip plane requires the diffusion-controlled addition or removal of atoms (dislocation climb).</p>
    </div>
    <div class="final-answer-box">
      <strong>Screw Dislocation:</strong> Helical spiral ramp &bull; $\mathbf{b} \parallel \mathbf{t}$ (collinear).<br>
      <strong>Slip Plane:</strong> Non-unique (any plane containing $\mathbf{t}$).<br>
      <strong>Cross-Slip:</strong> Screw dislocations bypass obstacles by switching between intersecting slip planes sharing the same $\mathbf{b}$.
    </div>""")

# P29: Stress Field of a Screw Dislocation
add(29, "Stress Field and Pure Shear Elasticity of a Screw Dislocation",
    "Linear Defects & Dislocations", "dislocations", "Intermediate",
    r"""<p>The elastic strain field surrounding a screw dislocation exhibits pure shear symmetry without dilatational volume changes.</p>
    <ol type="a">
      <li>Using cylindrical coordinates $(r, \theta, z)$ aligned with a straight screw dislocation along the $z$-axis, write down the displacement field $u_z(r, \theta, z)$ and the non-zero stress components.</li>
      <li>Prove that the hydrostatic stress $\sigma_h$ of a screw dislocation is identically <strong>zero</strong> everywhere in linear isotropic elasticity.</li>
      <li>Explain the practical physical consequence of $\sigma_h = 0$ on the interaction between screw dislocations and spherically symmetric substitutional solute atoms (e.g., Ni in Cu).</li>
      <li>Calculate the shear stress $\tau_{\theta z}$ at a distance $r = 1.0 \text{ nm}$ from a screw dislocation in iron ($G = 82 \text{ GPa}, b = 0.248 \text{ nm}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Displacement and Stress Fields of a Screw Dislocation</div>
      <p>Because the atomic planes form a ramp of pitch $b$, the displacement $u_z$ increases linearly from $0$ to $b$ as $\theta$ rotates through $2\pi$:</p>
      $$u_z = \frac{b}{2\pi} \theta, \quad u_r = 0, \quad u_\theta = 0$$
      <p>The only non-zero elastic shear strain is:</p>
      $$\varepsilon_{\theta z} = \frac{1}{2} \left(\frac{1}{r} \frac{\partial u_z}{\partial \theta}\right) = \frac{1}{2} \left(\frac{1}{r} \frac{b}{2\pi}\right) = \frac{b}{4\pi r}$$
      <p>Using Hooke's law in shear ($\tau = 2G\varepsilon$):</p>
      $$\tau_{\theta z} = \tau_{z\theta} = \frac{G b}{2\pi r}$$
      <p>All normal stress components ($\sigma_{rr} = \sigma_{\theta\theta} = \sigma_{zz} = 0$) and other shear stresses ($\tau_{r\theta} = 0$) are identically zero.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Proof that Hydrostatic Stress $\sigma_h = 0$</div>
      $$\sigma_h = \frac{\sigma_{rr} + \sigma_{\theta\theta} + \sigma_{zz}}{3} = \frac{0 + 0 + 0}{3} \equiv \mathbf{0}$$
      <p>A screw dislocation produces pure cylindrical shear distortion with zero volumetric dilation ($\Delta V / V = 0$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Solute Interaction Consequence</div>
      <p>The elastic interaction energy between a point defect with volumetric misfit $\Delta V$ and a dislocation stress field is given by:</p>
      $$U_{\text{elastic}} = -p \Delta V = \sigma_h \Delta V$$
      <p>Because $\sigma_h = 0$ for a screw dislocation, <strong>spherically symmetric substitutional solute atoms do not interact first-order elastically with screw dislocations</strong>! Consequently, solid solution strengthening from spherical misfits is mediated primarily by edge dislocations rather than screw dislocations.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Shear Stress Calculation in Iron at $r = 1.0 \text{ nm}$</div>
      $$\tau = \frac{G b}{2\pi r} = \frac{(82 \times 10^9 \text{ Pa}) \times (0.248 \times 10^{-9} \text{ m})}{2\pi \times (1.0 \times 10^{-9} \text{ m})} = \frac{20.336}{6.283 \times 10^{-9}} = \mathbf{3.237 \times 10^9 \text{ Pa} \approx 3.24 \text{ GPa}}$$
      <p>At $1 \text{ nm}$ from the core, the internal shear stress is immense ($\sim 3.24 \text{ GPa}$), decaying hyperbolically as $1/r$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Stress Field:</strong> $$\tau_{\theta z} = \frac{Gb}{2\pi r}, \quad \sigma_h \equiv 0$$
      <strong>Hydrostatic Stress:</strong> Exactly zero everywhere (pure shear deformation).<br>
      <strong>Solute Interaction:</strong> Zero first-order dilatational interaction with spherical solutes.<br>
      <strong>Shear Stress at $1\text{ nm}$ in Fe:</strong> $\tau = \mathbf{3.24 \text{ GPa}}$.
    </div>""")

# P30: Mixed Dislocation
add(30, "The Mixed Dislocation: Vector Decomposition into Edge and Screw Components",
    "Linear Defects & Dislocations", "dislocations", "Intermediate",
    r"""<p>In real engineering crystals, dislocations rarely exist as purely straight edge or screw lines; the vast majority are mixed dislocations.</p>
    <ol type="a">
      <li>Define a <strong>mixed dislocation</strong> in terms of the angle $\alpha$ between the dislocation line vector $\mathbf{t}$ and the Burgers vector $\mathbf{b}$.</li>
      <li>Derive the decomposition of the Burgers vector into its orthogonal edge component ($b_e$) and screw component ($b_s$) as a function of $b$ and $\alpha$.</li>
      <li>A mixed dislocation in copper ($b = 0.256 \text{ nm}$) has its line vector oriented at an angle $\alpha = 60^\circ$ to its Burgers vector (a classic $60^\circ$ dislocation in FCC). Calculate the numerical magnitudes of $b_e$ and $b_s$.</li>
      <li>State the total elastic energy formula per unit length for a mixed dislocation.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition of Mixed Dislocation</div>
      <p>A mixed dislocation is any dislocation where the angle $\alpha$ between the line unit tangent vector $\mathbf{t}$ and the Burgers vector $\mathbf{b}$ satisfies $0^\circ < \alpha < 90^\circ$ (and $90^\circ < \alpha < 180^\circ$). It exhibits characteristics of both edge and screw defects simultaneously.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Vector Decomposition</div>
      <p>The Burgers vector $\mathbf{b}$ can be uniquely resolved into two orthogonal components:</p>
      <ul>
        <li><strong>Screw Component ($\mathbf{b}_s \parallel \mathbf{t}$):</strong> The projection of $\mathbf{b}$ along $\mathbf{t}$:
        $$b_s = b \cos\alpha$$</li>
        <li><strong>Edge Component ($\mathbf{b}_e \perp \mathbf{t}$):</strong> The projection of $\mathbf{b}$ perpendicular to $\mathbf{t}$:
        $$b_e = b \sin\alpha$$</li>
      </ul>
      <p>By Pythagorean vector addition: $b^2 = b_e^2 + b_s^2 = b^2\sin^2\alpha + b^2\cos^2\alpha = b^2$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation for $60^\circ$ Dislocation in Copper ($b = 0.256 \text{ nm}, \alpha = 60^\circ$)</div>
      <ul>
        <li><strong>Screw Component:</strong>
        $$b_s = 0.256 \cos(60^\circ) = 0.256 \times 0.500 = \mathbf{0.128 \text{ nm}}$$</li>
        <li><strong>Edge Component:</strong>
        $$b_e = 0.256 \sin(60^\circ) = 0.256 \times \frac{\sqrt{3}}{2} = 0.256 \times 0.8660 = \mathbf{0.2217 \text{ nm}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Elastic Strain Energy of a Mixed Dislocation</div>
      <p>Because the edge and screw strain fields are mutually orthogonal, cross-terms integrate to zero in linear elasticity. The total strain energy per unit length is simply the sum of edge and screw energies:</p>
      $$E_{\text{mixed}} = E_{\text{edge}} + E_{\text{screw}} = \frac{G b_e^2}{4\pi(1-\nu)} \ln\left(\frac{R}{r_0}\right) + \frac{G b_s^2}{4\pi} \ln\left(\frac{R}{r_0}\right)$$
      $$E_{\text{mixed}} = \frac{G b^2}{4\pi} \left[ \frac{\sin^2\alpha}{1-\nu} + \cos^2\alpha \right] \ln\left(\frac{R}{r_0}\right)$$
      <p>Since $(1-\nu) < 1$, the edge component has higher elastic energy than the screw component for the same $b$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Vector Components:</strong> $b_s = b\cos\alpha$, $b_e = b\sin\alpha$.<br>
      <strong>For $60^\circ$ Dislocation in Cu:</strong> $b_s = \mathbf{0.128 \text{ nm}}$, $b_e = \mathbf{0.222 \text{ nm}}$.<br>
      <strong>Elastic Energy:</strong> $$E = \frac{Gb^2}{4\pi}\left[\frac{\sin^2\alpha}{1-\nu} + \cos^2\alpha\right]\ln\left(\frac{R}{r_0}\right)$$
    </div>""")

# P31: Burgers Circuit Construction
add(31, "The Burgers Circuit: Right-Hand Finish-to-Start (RH/FS) Convention",
    "Linear Defects & Dislocations", "dislocations", "Fundamental",
    r"""<p>The Burgers vector $\mathbf{b}$ is the topological invariant of a dislocation, mathematically defined by constructing a Burgers circuit around the defect.</p>
    <ol type="a">
      <li>Outline the rigorous step-by-step procedure for constructing a Burgers circuit using the <strong>Right-Hand Finish-to-Start (RH/FS) convention</strong>.</li>
      <li>Explain the concept of <strong>closure failure</strong> in real defected crystals versus ideal reference lattices.</li>
      <li>Does the Burgers vector change if the size or path of the Burgers circuit is expanded, provided it encloses the exact same dislocation line?</li>
      <li>What is the closure failure if a Burgers circuit encloses two dislocations with equal and opposite Burgers vectors ($+\mathbf{b}$ and $-\mathbf{b}$)?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Step-by-Step Burgers Circuit Construction (RH/FS Convention)</div>
      <ol>
        <li><strong>Choose Line Direction $\mathbf{t}$::</strong> Arbitrarily assign a positive sense unit vector $\mathbf{t}$ along the dislocation line.</li>
        <li><strong>Construct Real Circuit (Defected Crystal):</strong> Form a closed atom-to-atom circuit encircling the dislocation line in a right-handed sense (using the right-hand grip rule, thumb pointing along $\mathbf{t}$, fingers curl in the direction of traversal). Count the exact number of atomic lattice steps in each direction (e.g., 5 steps up, 5 steps right, 5 steps down, 5 steps left) so the circuit closes perfectly in the real crystal.</li>
        <li><strong>Map to Reference Crystal (Perfect Lattice):</strong> Traverse the exact same sequence of atom-to-atom translation steps in a perfect, defect-free reference crystal.</li>
        <li><strong>Identify Closure Failure:</strong> In the perfect crystal, the path fails to close. The vector required to close the gap from the <strong>Finish ($F$)</strong> point to the <strong>Start ($S$)</strong> point is the <strong>Burgers vector $\mathbf{b}$</strong>:
        $$\mathbf{b} = \vec{FS}$$</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Meaning of Closure Failure</div>
      <p>The closure failure represents the missing (or extra) lattice translation introduced by the defect. It quantitatively measures the net lattice displacement produced by the dislocation.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Independence of Circuit Size and Shape</div>
      <p>The Burgers vector is a <strong>topological invariant</strong>. As long as the circuit does not cross or enclose any additional dislocations, expanding the circuit's perimeter or altering its geometry encloses the exact same core distortion, yielding the identical Burgers vector $\mathbf{b}$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Circuit Enclosing Opposite Dislocations ($+\mathbf{b}$ and $-\mathbf{b}$)</div>
      <p>By topological summation, the net closure failure encloses the sum of all enclosed Burgers vectors:</p>
      $$\mathbf{b}_{\text{net}} = \sum_i \mathbf{b}_i = (+\mathbf{b}) + (-\mathbf{b}) = \mathbf{0}$$
      <p>The circuit closes with zero closure failure ($\mathbf{b}_{\text{net}} = 0$), behaving macroscopically like a perfect crystal.</p>
    </div>
    <div class="final-answer-box">
      <strong>RH/FS Convention:</strong> $\mathbf{b} = \vec{FS}$ (vector drawn from Finish to Start in the perfect reference crystal).<br>
      Topological invariant: independent of circuit size.<br>
      Opposite dislocations cancel out: $\mathbf{b}_{\text{net}} = \mathbf{0}$.
    </div>""")

# P32: Dislocation Loop
add(32, "The Dislocation Loop: Continuous Variation of Dislocation Character",
    "Linear Defects & Dislocations", "dislocations", "Intermediate",
    r"""<p>In crystalline materials undergoing plastic deformation, dislocations frequently expand as closed planar loops.</p>
    <ol type="a">
      <li>Consider a planar circular dislocation loop expanding on a horizontal slip plane with a uniform Burgers vector $\mathbf{b}$ pointing in the $+x$ direction. Analyze the dislocation character (pure edge, pure screw, or mixed) at the four cardinal points:
        <ul>
          <li>Point $A$ (where line tangent $\mathbf{t}$ is parallel to $+y$).</li>
          <li>Point $B$ (where line tangent $\mathbf{t}$ is parallel to $+x$).</li>
          <li>Point $C$ (where line tangent $\mathbf{t}$ is parallel to $-y$).</li>
          <li>Point $D$ (where line tangent $\mathbf{t}$ is parallel to $-x$).</li>
        </ul>
      </li>
      <li>Explain why the Burgers vector $\mathbf{b}$ remains strictly constant at all points around the loop, while the dislocation character varies continuously.</li>
      <li>Under a uniform applied shear stress $\tau_{xz}$, determine the direction of the Peach-Koehler force on every segment of the loop and describe how the loop evolves.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Character at Cardinal Points ($\mathbf{b} \parallel +x$)</div>
      <ul>
        <li><strong>Point $A$ ($\mathbf{t} \parallel +y$):</strong> $\mathbf{t} \perp \mathbf{b}$ ($\mathbf{t} \cdot \mathbf{b} = 0$). This segment is <strong>pure positive edge dislocation ($\perp$)</strong>.</li>
        <li><strong>Point $B$ ($\mathbf{t} \parallel +x$):</strong> $\mathbf{t} \parallel \mathbf{b}$ ($\mathbf{t} \times \mathbf{b} = \mathbf{0}$). This segment is <strong>pure right-handed screw dislocation</strong>.</li>
        <li><strong>Point $C$ ($\mathbf{t} \parallel -y$):</strong> $\mathbf{t} \perp \mathbf{b}$ ($\mathbf{t} \cdot \mathbf{b} = 0$). This segment is <strong>pure negative edge dislocation ($\top$)</strong>.</li>
        <li><strong>Point $D$ ($\mathbf{t} \parallel -x$):</strong> $\mathbf{t}$ is antiparallel to $\mathbf{b}$. This segment is <strong>pure left-handed screw dislocation</strong>.</li>
        <li><strong>Intermediate Points:</strong> As $\mathbf{t}$ rotates continuously around the $360^\circ$ circle, the angle $\alpha$ varies continuously, smoothly transitioning through all mixed character states.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Constancy of Burgers Vector $\mathbf{b}$</div>
      <p>A dislocation line cannot end inside a crystal (it must form a closed loop, end at an external surface, or terminate at another dislocation node). The slip displacement across the sheared interior of the loop is uniform and equal to $\mathbf{b}$. Therefore, $\mathbf{b}$ is a fixed global vector throughout the entire loop, while the local tangent $\mathbf{t}$ rotates continuously in space.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Peach-Koehler Force and Loop Expansion</div>
      <p>The Peach-Koehler force per unit length acting on a dislocation segment is given by:</p>
      $$\mathbf{f}_{\text{PK}} = (\boldsymbol{\sigma} \cdot \mathbf{b}) \times \mathbf{t}$$
      <p>For an applied shear stress $\tau_{xz}$, the force vector $\mathbf{f}_{\text{PK}}$ always acts <strong>perpendicular to the line tangent $\mathbf{t}$ and points radially outward</strong> at every point along the circumference. As a result, the circular loop expands uniformly outward in all directions, shearing the enclosed slip plane by displacement $\mathbf{b}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Loop Segments ($\mathbf{b} \parallel +x$):</strong><br>
      Point A ($\mathbf{t} \parallel +y$): <strong>Positive Edge ($\perp$)</strong> &bull; Point B ($\mathbf{t} \parallel +x$): <strong>Right-Hand Screw</strong><br>
      Point C ($\mathbf{t} \parallel -y$): <strong>Negative Edge ($\top$)</strong> &bull; Point D ($\mathbf{t} \parallel -x$): <strong>Left-Hand Screw</strong><br>
      $\mathbf{b}$ is constant everywhere; Peach-Koehler forces expand the loop radially outward.
    </div>""")

# Save checkpoint for part 2 (26-32)
print("Part 2: P26-P32 appended successfully.")
# P33: Dislocation Motion: Glide vs. Climb
add(33, "Dislocation Motion: Conservative Glide vs. Non-Conservative Climb",
    "Linear Defects & Dislocations", "dislocations", "Intermediate",
    r"""<p>Dislocations can move through a crystal via two fundamentally distinct mechanisms depending on temperature and stress.</p>
    <ol type="a">
      <li>Differentiate between <strong>dislocation glide (slip)</strong> and <strong>dislocation climb</strong>.</li>
      <li>Why is dislocation glide classified as a <strong>conservative</strong> process, while dislocation climb is classified as a <strong>non-conservative</strong> process?</li>
      <li>Distinguish between positive climb and negative climb in terms of vacancy absorption and emission.</li>
      <li>Explain why dislocation climb is practically impossible at room temperature in high-melting metals, but becomes the rate-controlling mechanism for high-temperature creep ($T > 0.4 T_m$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Dislocation Glide vs. Dislocation Climb</div>
      <ul>
        <li><strong>Glide (Slip):</strong> The motion of a dislocation within its own slip plane (the plane containing $\mathbf{t}$ and $\mathbf{b}$). It proceeds by consecutively breaking and reforming existing atomic bonds without mass transport.</li>
        <li><strong>Climb:</strong> The motion of an edge dislocation <strong>perpendicular to its slip plane</strong>. It corresponds to the lengthening or shortening of the extra half-plane of atoms, requiring individual atoms to be added to or removed from the bottom row of the extra sheet.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Conservative vs. Non-Conservative Nature</div>
      <ul>
        <li><strong>Conservative Motion (Glide):</strong> The total number of atoms and vacancies in the crystal is strictly conserved. Atoms merely shift their relative positions within the lattice without net diffusion.</li>
        <li><strong>Non-Conservative Motion (Climb):</strong> Atoms must be transferred into or out of the dislocation core. Expanding or contracting the extra half-plane requires the creation or annihilation of point defects (vacancies or interstitials).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Positive vs. Negative Climb</div>
      <ul>
        <li><strong>Positive Climb:</strong> The extra half-plane shrinks (moves upward away from the slip plane). Atoms leave the dislocation line by diffusing away, which is physically achieved by <strong>absorbing vacancies</strong> (or emitting interstitials).</li>
        <li><strong>Negative Climb:</strong> The extra half-plane grows longer (moves downward into the tensile zone). Atoms are added to the dislocation line, which is achieved by <strong>emitting vacancies</strong> (or absorbing interstitials).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Temperature Dependence and Creep</div>
      <p>Because climb requires atomic diffusion, its rate is governed by the self-diffusion coefficient $D = D_0 \exp(-Q_{\text{diff}}/RT)$. At room temperature ($T \ll T_m$), vacancy concentrations ($10^{-15}$) and atomic jump frequencies are virtually zero, locking dislocations into their slip planes. At elevated temperatures ($T > 0.4\text{--}0.5 T_m$), high vacancy populations and rapid thermal diffusion enable edge dislocations to climb over precipitates and obstacles that had pinned them. This climb-assisted obstacle bypass is the fundamental rate-controlling microscopic mechanism of <strong>dislocation power-law creep</strong> in high-temperature turbine blades and steam pipes.</p>
    </div>
    <div class="final-answer-box">
      <strong>Glide:</strong> In-plane motion, conservative, diffusionless, occurs at all temperatures.<br>
      <strong>Climb:</strong> Out-of-plane motion, non-conservative, diffusion-controlled (requires vacancy absorption/emission).<br>
      Climb requires $T > 0.4 T_m$ and governs high-temperature power-law creep.
    </div>""")

# P34: Elastic Strain Energy of a Dislocation
add(34, "Elastic Strain Energy of a Dislocation: Derivation of the $E \\approx \\alpha G b^2$ Law",
    "Linear Defects & Dislocations", "dislocations", "Advanced",
    r"""<p>Dislocations are high-energy non-equilibrium defects that store substantial elastic strain energy in the surrounding crystal lattice.</p>
    <ol type="a">
      <li>Derive the elastic strain energy per unit length $E_{\text{elastic}}$ of a straight screw dislocation by integrating the elastic shear strain energy density $\frac{1}{2}\tau\gamma$ from the core radius $r_0$ to an outer crystal boundary $R$:
      $$E_{\text{screw}} = \frac{G b^2}{4\pi} \ln\left(\frac{R}{r_0}\right)$$</li>
      <li>State the corresponding strain energy equation for a pure edge dislocation, explaining why an edge dislocation stores approximately $30\text{--}50\%$ more elastic energy than a screw dislocation of the same Burgers vector.</li>
      <li>Using typical values ($G = 40 \text{ GPa}$, $b = 0.25 \text{ nm}$, $r_0 \approx b$, $R \approx 10^4 b$):
        <ul>
          <li>Calculate the total energy per unit length $E$ in $\text{J/m}$ and in $\text{eV/nm}$.</li>
          <li>Justify the standard engineering approximation: $E \approx \alpha G b^2$ (with $\alpha \approx 0.5\text{--}1.0$).</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Screw Dislocation Elastic Energy</div>
      <p>Consider a hollow cylinder of length $L = 1$ (unit length), inner radius $r_0$ (dislocation core radius, $\sim b$), and outer radius $R$ (mean distance to nearest neighboring dislocation, $\sim 10^3\text{--}10^5 b$).</p>
      <p>The elastic strain energy density per unit volume is:</p>
      $$u = \frac{1}{2} \tau_{\theta z} \gamma_{\theta z} = \frac{\tau^2}{2G}$$
      <p>Substituting the screw stress field $\tau = \frac{G b}{2\pi r}$:</p>
      $$u(r) = \frac{1}{2G}\left(\frac{G b}{2\pi r}\right)^2 = \frac{G b^2}{8\pi^2 r^2}$$
      <p>Integrating over cylindrical volume elements $dV = (2\pi r dr) \cdot 1$:</p>
      $$E_{\text{screw}} = \int_{r_0}^{R} u(r) \cdot 2\pi r dr = \int_{r_0}^{R} \left(\frac{G b^2}{8\pi^2 r^2}\right) 2\pi r dr = \frac{G b^2}{4\pi} \int_{r_0}^{R} \frac{dr}{r}$$
      $$E_{\text{screw}} = \frac{G b^2}{4\pi} \ln\left(\frac{R}{r_0}\right)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Edge Dislocation Energy and Ratio</div>
      $$E_{\text{edge}} = \frac{G b^2}{4\pi(1-\nu)} \ln\left(\frac{R}{r_0}\right) = \frac{E_{\text{screw}}}{1-\nu}$$
      <p>Because metallic Poisson's ratios are typically $\nu \approx 0.30\text{--}0.33$, the factor $\frac{1}{1-\nu} \approx \frac{1}{0.67} \approx 1.5$. An edge dislocation stores <strong>$50\%$ more elastic energy</strong> than a screw dislocation because it induces both shear strain and compressive/tensile volumetric dilatational strains, whereas a screw dislocation creates only pure shear.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Numerical Evaluation and the $E \approx \alpha G b^2$ Law</div>
      <p>For $R/r_0 \approx 10^4 \implies \ln(10^4) = 4 \ln(10) \approx 9.21$:</p>
      $$\frac{\ln(R/r_0)}{4\pi} = \frac{9.21}{12.566} \approx 0.733$$
      <p>Adding the non-linear core energy $E_{\text{core}} \approx \frac{Gb^2}{10}$, the total energy factor becomes $\alpha \approx 0.8\text{--}1.0$:</p>
      $$E \approx \alpha G b^2 \quad (\alpha \approx 0.5\text{ to }1.0)$$
      <p>Evaluating for $G = 40 \text{ GPa} = 40 \times 10^9 \text{ N/m}^2, b = 0.25 \text{ nm} = 0.25 \times 10^{-9} \text{ m}$ with $\alpha = 0.5$:</p>
      $$E \approx 0.5 \times (40 \times 10^9) \times (0.25 \times 10^{-9})^2 = 0.5 \times (40 \times 10^9) \times (6.25 \times 10^{-20}) = \mathbf{1.25 \times 10^{-9} \text{ J/m}}$$
      <p>Converting to $\text{eV/nm}$ ($1 \text{ eV} = 1.602 \times 10^{-19} \text{ J}$, $1 \text{ m} = 10^9 \text{ nm}$):</p>
      $$E = \frac{1.25 \times 10^{-9} \text{ J/m} \times 10^{-9} \text{ m/nm}}{1.602 \times 10^{-19} \text{ J/eV}} = \mathbf{7.80 \text{ eV/nm}}$$
      <p>Every single nanometer of dislocation line stores roughly $\sim 8 \text{ eV}$ of strain energy (about 1 to 2 eV per atom plane!).</p>
    </div>
    <div class="final-answer-box">
      <strong>Elastic Energy Derivation:</strong> $$E_{\text{screw}} = \frac{Gb^2}{4\pi}\ln\left(\frac{R}{r_0}\right), \quad E_{\text{edge}} = \frac{Gb^2}{4\pi(1-\nu)}\ln\left(\frac{R}{r_0}\right)$$
      <strong>Canonical Rule:</strong> $E \approx \mathbf{\alpha G b^2}$ ($\alpha \approx 0.5\text{--}1.0$).<br>
      <strong>Numerical Value:</strong> $E \approx \mathbf{1.25 \times 10^{-9} \text{ J/m} \approx 7.8 \text{ eV/nm}}$.
    </div>""")

# P35: Frank's Rule for Dislocation Reactions
add(35, "Frank's Energy Criterion: Spontaneous Dislocation Reactions and Vector Combinations",
    "Linear Defects & Dislocations", "dislocations", "Advanced",
    r"""<p>Because dislocation energy scales quadratically with Burgers vector magnitude ($E \propto b^2$), F. C. Frank formulated an energetic criterion predicting whether dislocation reactions proceed spontaneously.</p>
    <ol type="a">
      <li>State <strong>Frank's Rule</strong> for the spontaneous combination of two dislocations ($\mathbf{b}_1 + \mathbf{b}_2 \to \mathbf{b}_3$):
      $$b_1^2 + b_2^2 > b_3^2$$</li>
      <li>In an FCC crystal with lattice parameter $a$, consider two dislocations gliding on intersecting $\{111\}$ slip planes:
      $$\mathbf{b}_1 = \frac{a}{2}[10\bar{1}], \quad \mathbf{b}_2 = \frac{a}{2}[011]$$
      Calculate the resultant Burgers vector $\mathbf{b}_3$, evaluate Frank's criterion, and determine whether the reaction is thermodynamically favorable.</li>
      <li>Evaluate whether the reverse dissociation reaction $\frac{a}{2}[110] \to \frac{a}{2}[100] + \frac{a}{2}[010]$ is energetically favorable in a simple cubic lattice.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Frank's Energy Rule Formulation</div>
      <p>Since the line energy of a dislocation is $E \approx \frac{1}{2}Gb^2$, the change in energy during a reaction where dislocations $\mathbf{b}_1$ and $\mathbf{b}_2$ combine to form $\mathbf{b}_3 = \mathbf{b}_1 + \mathbf{b}_2$ is:</p>
      $$\Delta E \propto b_3^2 - (b_1^2 + b_2^2)$$
      <ul>
        <li>If $b_1^2 + b_2^2 > b_3^2 \implies \Delta E < 0$: The reaction releases elastic strain energy and proceeds <strong>spontaneously</strong>.</li>
        <li>If $b_1^2 + b_2^2 < b_3^2 \implies \Delta E > 0$: The reaction requires external energy input and will <strong>not occur</strong> (the single dislocation $\mathbf{b}_3$ will spontaneously dissociate).</li>
        <li>If $b_1^2 + b_2^2 = b_3^2 \implies \Delta E = 0$: Energetically neutral.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Evaluation in FCC Lattice</div>
      <p>Resultant vector sum:</p>
      $$\mathbf{b}_3 = \mathbf{b}_1 + \mathbf{b}_2 = \frac{a}{2}[10\bar{1}] + \frac{a}{2}[011] = \frac{a}{2}[(1+0), (0+1), (-1+1)] = \frac{a}{2}[110]$$
      <p>Compute square magnitudes:</p>
      $$b_1^2 = \left(\frac{a}{2}\right)^2 (1^2 + 0^2 + (-1)^2) = \frac{a^2}{4}(2) = \frac{a^2}{2}$$
      $$b_2^2 = \left(\frac{a}{2}\right)^2 (0^2 + 1^2 + 1^2) = \frac{a^2}{4}(2) = \frac{a^2}{2}$$
      $$\sum b_{\text{initial}}^2 = b_1^2 + b_2^2 = \frac{a^2}{2} + \frac{a^2}{2} = a^2$$
      $$b_3^2 = \left(\frac{a}{2}\right)^2 (1^2 + 1^2 + 0^2) = \frac{a^2}{4}(2) = \frac{a^2}{2}$$
      <p>Comparing initial and final energies:</p>
      $$b_1^2 + b_2^2 = a^2 \quad \text{vs.} \quad b_3^2 = \frac{a^2}{2}$$
      $$b_1^2 + b_2^2 = a^2 > \frac{a^2}{2} = b_3^2$$
      <p>Because $a^2 > 0.5 a^2$, the reaction <strong>releases exactly 50% of the initial elastic strain energy ($\Delta E = -0.5 a^2$)</strong>. The reaction is <strong>strongly favorable and proceeds spontaneously</strong>, forming an attractive junction or sessile lock (e.g., Lomer lock) that obstructs further slip.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Evaluation of Dissociation $\frac{a}{2}[110] \to \frac{a}{2}[100] + \frac{a}{2}[010]$</div>
      $$b_{\text{parent}}^2 = \left(\frac{a}{2}\right)^2 (1^2 + 1^2 + 0) = \frac{2a^2}{4} = \frac{a^2}{2}$$
      $$b_{\text{product 1}}^2 = \left(\frac{a}{2}\right)^2 (1^2) = \frac{a^2}{4}, \quad b_{\text{product 2}}^2 = \left(\frac{a}{2}\right)^2 (1^2) = \frac{a^2}{4}$$
      $$\sum b_{\text{products}}^2 = \frac{a^2}{4} + \frac{a^2}{4} = \frac{a^2}{2}$$
      $$b_{\text{parent}}^2 = \sum b_{\text{products}}^2 = \frac{a^2}{2}$$
      <p>Because $\Delta E = 0$, there is no elastic energy driving force for dissociation. Due to core energy and repulsive interaction between products, the reaction does not proceed.</p>
    </div>
    <div class="final-answer-box">
      <strong>Frank's Criterion:</strong> Reaction is spontaneous if $\sum b_{\text{initial}}^2 > b_{\text{final}}^2$.<br>
      <strong>FCC Combination:</strong> $\frac{a}{2}[10\bar{1}] + \frac{a}{2}[011] \to \frac{a}{2}[110]$ yields $a^2 > 0.5 a^2$ (spontaneous, releases $50\%$ strain energy).
    </div>""")

# P36: Dislocation Density
add(36, "Dislocation Density: Volumetric Definition and Total Line Length in Cold-Worked Metals",
    "Linear Defects & Dislocations", "dislocations", "Fundamental",
    r"""<p>The total concentration of dislocations within a crystalline solid is quantified by its dislocation density $\rho_d$.</p>
    <ol type="a">
      <li>State the two equivalent geometric definitions of <strong>dislocation density $\rho_d$</strong> and their standard SI units:
        <ul>
          <li>As total dislocation line length per unit volume.</li>
          <li>As the number of dislocation lines intersecting a random unit cross-sectional area.</li>
        </ul>
      </li>
      <li>State typical numerical ranges for $\rho_d$ in:
        <ul>
          <li>A carefully grown high-purity single crystal (e.g., semiconductor silicon).</li>
          <li>A well-annealed polycrystalline metal.</li>
          <li>A heavily cold-rolled steel sheet ($70\text{--}90\%$ cold work).</li>
        </ul>
      </li>
      <li>A cubic block of cold-worked steel measuring $1.0 \text{ cm} \times 1.0 \text{ cm} \times 1.0 \text{ cm}$ has a measured dislocation density of $\rho_d = 1.0 \times 10^{11} \text{ cm}^{-2}$. Calculate the total length of dislocation lines contained inside this single cubic centimeter in kilometers ($\text{km}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Two Equivalent Definitions of Dislocation Density $\rho_d$</div>
      <ol>
        <li><strong>Volumetric Definition:</strong> The total length of all dislocation lines $L_{\text{total}}$ contained within a given volume $V$:
        $$\rho_d = \frac{L_{\text{total}}}{V} \quad \left[\frac{\text{meters}}{\text{meter}^3} = \text{m}^{-2} \text{ or cm}^{-2}\right]$$</li>
        <li><strong>Areal Intercept Definition:</strong> The number of dislocation line piercing points $N_{\text{disloc}}$ intersecting a random plane of cross-sectional area $A$:
        $$\rho_d = \frac{N_{\text{disloc}}}{A} \quad \left[\frac{\text{number}}{\text{meter}^2} = \text{m}^{-2} \text{ or cm}^{-2}\right]$$</li>
      </ol>
      <p>By geometric probability theory, these two definitions are mathematically identical.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Typical Dislocation Density Magnitudes</div>
      <ul>
        <li><strong>Semiconductor Silicon Wafers (Dislocation-Free Czochralski):</strong> $\rho_d \approx 0\text{ to }10^2 \text{ cm}^{-2}$ ($10^2\text{--}10^6 \text{ m}^{-2}$).</li>
        <li><strong>Well-Annealed Metals (e.g., annealed Cu, Al, Fe):</strong> $\rho_d \approx 10^5\text{ to }10^7 \text{ cm}^{-2}$ ($10^9\text{--}10^{11} \text{ m}^{-2}$).</li>
        <li><strong>Heavily Cold-Worked Metals (e.g., rolled or drawn wire):</strong> $\rho_d \approx 10^{10}\text{ to }10^{12} \text{ cm}^{-2}$ ($10^{14}\text{--}10^{16} \text{ m}^{-2}$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Total Dislocation Length in $1 \text{ cm}^3$ of Cold-Worked Steel</div>
      <p>Given $\rho_d = 1.0 \times 10^{11} \text{ cm}^{-2} = 1.0 \times 10^{11} \text{ cm/cm}^3$ and volume $V = 1.0 \text{ cm}^3$:</p>
      $$L_{\text{total}} = \rho_d \times V = (1.0 \times 10^{11} \text{ cm/cm}^3) \times (1.0 \text{ cm}^3) = 1.0 \times 10^{11} \text{ cm}$$
      <p>Convert centimeters to meters ($1 \text{ m} = 100 \text{ cm}$):</p>
      $$L_{\text{total}} = \frac{1.0 \times 10^{11} \text{ cm}}{100 \text{ cm/m}} = 1.0 \times 10^9 \text{ m}$$
      <p>Convert meters to kilometers ($1 \text{ km} = 1,000 \text{ m}$):</p>
      $$L_{\text{total}} = \frac{1.0 \times 10^9 \text{ m}}{1,000 \text{ m/km}} = \mathbf{1,000,000 \text{ km} = 1.0 \times 10^6 \text{ km}}$$
      <p><em>Physical Perspective:</em> Inside a sugar-cube-sized piece ($1 \text{ cm}^3$) of cold-rolled steel, the tangled dislocation lines would wrap around the Earth's equator ($40,075 \text{ km}$) roughly <strong>25 times</strong>!</p>
    </div>
    <div class="final-answer-box">
      <strong>Definitions:</strong> $\rho_d = \frac{L_{\text{total}}}{V} \equiv \frac{N}{A}$ (units $\text{m}^{-2}$ or $\text{cm}^{-2}$).<br>
      <strong>Ranges:</strong> Silicon: $\sim 0$; Annealed Metal: $10^5\text{--}10^7 \text{ cm}^{-2}$; Cold-worked: $10^{10}\text{--}10^{12} \text{ cm}^{-2}$.<br>
      <strong>Total Length in $1 \text{ cm}^3$:</strong> $L_{\text{total}} = \mathbf{1,000,000 \text{ km}}$ (1 million kilometers!).
    </div>""")

# P37: Planar Defects External Surface Energy
add(37, "Planar Defects: External Surfaces, Broken Bond Model, and Surface Energy $\\gamma_s$",
    "Planar & Interfacial Defects", "planar_defects", "Fundamental",
    r"""<p>The external boundary of any crystal represents a two-dimensional planar defect where the 3D crystalline periodicity terminates abruptly.</p>
    <ol type="a">
      <li>Explain the thermodynamic and atomic origin of <strong>surface energy $\gamma_s$</strong> using the broken bond model.</li>
      <li>Why is surface energy always strictly positive ($\gamma_s > 0$)? Explain why liquids spontaneously form spherical droplets and nanocrystals tend toward equilibrium polyhedral shapes (Wulff theorem).</li>
      <li>In an FCC crystal, calculate the fraction of broken nearest-neighbor bonds per atom on:
        <ul>
          <li>The close-packed $\{111\}$ surface plane.</li>
          <li>The $\{100\}$ surface plane.</li>
        </ul>
        Predict which crystallographic plane has the lowest surface energy $\gamma_s$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Broken Bond Model of Surface Energy $\gamma_s$</div>
      <p>In the bulk interior of a crystal, every atom is surrounded by its full complement of nearest neighbors (coordination number $CN$, e.g., $CN = 12$ in FCC), satisfying all interatomic bonds at minimum potential energy $-E_b$. At an external surface, atoms are missing nearest neighbors on the exterior side. Creating a new surface requires cleaving bonds against attractive interatomic forces. The work done to sever these bonds remains stored in the surface atoms as excess reversible Gibbs free energy per unit area: $\gamma_s = \left(\frac{\partial G}{\partial A}\right)_{T, P}$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Why $\gamma_s > 0$ and Geometric Consequences</div>
      <p>Because severing stable bonds always requires positive mechanical work ($\Delta H_{\text{surface}} > 0$), $\gamma_s > 0$ without exception. Thermodynamically, every isolated system spontaneously minimizes its total free energy $G_{\text{total}} = \int \gamma_s dA$. For an isotropic liquid with orientation-independent $\gamma$, the minimum surface area for a given volume is a sphere. For anisotropic crystals, the shape minimizes $\sum \gamma_i A_i$, producing faceted equilibrium polyhedra where low-energy planes form the largest facets (Wulff construction).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Broken Bonds on FCC $\{111\}$ vs. $\{100\}$ Planes ($CN = 12$)</div>
      <ul>
        <li><strong>On $\{111\}$ Plane:</strong>
          In FCC close-packed $\{111\}$ layers, each atom has 6 neighbors in its own plane, 3 neighbors in the layer below, and 3 neighbors in the layer above. When the top half is cleaved, each surface atom loses exactly <strong>3 nearest-neighbor bonds</strong> out of 12:
          $$\text{Broken Bond Fraction} = \frac{3}{12} = \mathbf{25.0\%}$$
        </li>
        <li><strong>On $\{100\}$ Plane:</strong>
          In a square $\{100\}$ surface layer, each atom has 4 neighbors in its own plane, 4 in the layer below, and 4 in the layer above. Surface atoms lose <strong>4 nearest-neighbor bonds</strong> out of 12:
          $$\text{Broken Bond Fraction} = \frac{4}{12} = \mathbf{33.3\%}$$
        </li>
        <li><strong>Comparison:</strong> Because $\{111\}$ surfaces sever fewer bonds per atom and have the highest atomic planar density, the $\{111\}$ planes exhibit the <strong>lowest surface energy $\gamma_s$</strong> in FCC crystals ($\gamma_{111} < \gamma_{100} < \gamma_{110}$).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Broken Bonds in FCC:</strong> $\{111\}$ loses $3/12 = \mathbf{25\%}$ &bull; $\{100\}$ loses $4/12 = \mathbf{33.3\%}$.<br>
      <strong>Lowest Surface Energy:</strong> $\mathbf{\{111\}}$ plane has the lowest $\gamma_s$ because it has the highest planar atomic density and fewest severed bonds.
    </div>""")

# P38: Low-Angle Tilt Boundaries
add(38, "Low-Angle Grain Boundaries: Symmetric Tilt Boundary Modeled as an Edge Dislocation Wall",
    "Planar & Interfacial Defects", "planar_defects", "Intermediate",
    r"""<p>A low-angle grain boundary represents a transition zone between two adjacent crystal grains whose crystallographic orientations differ by a small misorientation angle ($\theta < 10^\circ\text{--}15^\circ$).</p>
    <ol type="a">
      <li>Describe the dislocation architecture of a <strong>symmetric low-angle tilt boundary</strong>.</li>
      <li>Derive the geometric relationship between the tilt misorientation angle $\theta$, the Burgers vector $b$, and the vertical spacing $D$ between adjacent edge dislocations:
      $$\sin\left(\frac{\theta}{2}\right) = \frac{b}{2D} \implies \theta \approx \frac{b}{D} \quad (\text{for small }\theta \text{ in radians})$$</li>
      <li>A symmetric tilt boundary in pure nickel ($b = 0.249 \text{ nm}$) has a measured misorientation angle of $\theta = 1.50^\circ$. Calculate the average spacing $D$ between adjacent edge dislocations in nanometers.</li>
      <li>Explain the Read-Shockley equation $\gamma_{\text{gb}} = \gamma_0 \theta (A - \ln\theta)$ for the energy of low-angle boundaries.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Dislocation Architecture of a Tilt Boundary</div>
      <p>A symmetric low-angle tilt boundary consists of a regular, vertical wall of identical parallel edge dislocations ($\perp$) stacked uniformly one above the other at periodic spacing $D$. The extra half-planes terminate on the boundary plane, producing a wedge-like rotation of the two grain lattices about an axis parallel to the dislocation lines.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Geometric Derivation of Dislocation Spacing $D$</div>
      <p>Consider two adjacent grains rotated symmetrically by angle $\theta/2$ in opposite directions relative to the boundary. Over vertical span $D$ containing one dislocation, the extra half-plane inserts one Burgers vector $b$ of lattice displacement:</p>
      $$\sin\left(\frac{\theta}{2}\right) = \frac{b/2}{D} = \frac{b}{2D}$$
      <p>Applying the small-angle approximation for small tilt angles $\theta \ll 1 \text{ rad}$ ($\sin x \approx x$):</p>
      $$\frac{\theta}{2} \approx \frac{b}{2D} \implies \theta \approx \frac{b}{D} \implies D \approx \frac{b}{\theta}$$
      <p>where $\theta$ must be expressed in <strong>radians</strong>.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation for Nickel ($\theta = 1.50^\circ, b = 0.249 \text{ nm}$)</div>
      <p>Convert misorientation angle $\theta$ from degrees to radians:</p>
      $$\theta = 1.50^\circ \times \frac{\pi}{180^\circ} = 0.02618 \text{ rad}$$
      <p>Calculate dislocation spacing $D$:</p>
      $$D = \frac{b}{\theta} = \frac{0.249 \text{ nm}}{0.02618 \text{ rad}} = \mathbf{9.51 \text{ nm}}$$
      <p>The edge dislocations are stacked in a vertical ladder with a spacing of approximately 9.5 nm (roughly 38 lattice parameters apart).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): The Read-Shockley Boundary Energy Equation</div>
      <p>In 1950, W. T. Read and W. Shockley calculated the elastic strain energy of the dislocation array by summing the overlapping stress fields. Because the alternating compressive and tensile fields of adjacent dislocations cancel each other at distances greater than $D$, the effective outer cutoff radius is $R \approx D = b/\theta$:</p>
      $$\gamma_{\text{gb}} = \frac{E_{\text{disloc}}}{D} = \frac{\theta}{b} \cdot \frac{G b^2}{4\pi(1-\nu)} \ln\left(\frac{e \cdot D}{r_0}\right) = \gamma_0 \theta [A - \ln\theta]$$
      <p>The energy increases steeply from zero at small angles, reaches a maximum around $\theta \approx 15^\circ$, where dislocation cores begin to overlap, and the individual dislocation model breaks down.</p>
    </div>
    <div class="final-answer-box">
      <strong>Dislocation Spacing Law:</strong> $$\theta \approx \frac{b}{D} \implies D \approx \frac{b}{\theta}$$
      <strong>For Ni ($\theta = 1.5^\circ$):</strong> $D = \mathbf{9.51 \text{ nm}}$.<br>
      <strong>Read-Shockley Model:</strong> $\gamma_{\text{gb}} = \gamma_0 \theta(A - \ln\theta)$ (valid for $\theta \le 15^\circ$).
    </div>""")

# P39: Low-Angle Twist Boundaries
add(39, "Low-Angle Twist Boundaries: Cross-Grid Array of Screw Dislocations",
    "Planar & Interfacial Defects", "planar_defects", "Intermediate",
    r"""<p>While tilt boundaries accommodate out-of-plane rotation, twist boundaries accommodate relative in-plane rotation between adjacent grains.</p>
    <ol type="a">
      <li>Describe the dislocation architecture of a <strong>low-angle twist boundary</strong>.</li>
      <li>Relate the twist angle $\phi$ to the Burgers vector $b$ and spacing $D$ between parallel screw dislocations in the orthogonal grid.</li>
      <li>A low-angle twist boundary in copper ($b = 0.256 \text{ nm}$) has a screw dislocation grid spacing of $D = 12.0 \text{ nm}$. Calculate the twist misorientation angle $\phi$ in degrees and arcminutes.</li>
      <li>Contrast the atomic structure of a low-angle grain boundary ($\theta < 15^\circ$) with that of a <strong>high-angle grain boundary</strong> ($\theta > 15^\circ$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Architecture of a Twist Boundary</div>
      <p>A low-angle twist boundary is formed when two adjacent crystal grains are rotated relative to each other by an angle $\phi$ about an axis strictly <strong>perpendicular to the boundary plane</strong>. This pure rotational shear displacement cannot be accommodated by edge dislocations; instead, it is accommodated by a <strong>two-dimensional cross-grid (orthogonal mesh) of two perpendicular sets of screw dislocations</strong> lying entirely within the boundary interface.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Formula Relating Twist Angle $\phi$ to Mesh Spacing $D$</div>
      <p>Each set of screw dislocations with Burgers vector $b$ spaced at interval $D$ accommodates a shear strain of $\gamma = b/D$. For two orthogonal sets producing a rigid rotational twist angle $\phi$ (in radians):</p>
      $$\phi \approx \frac{b}{D} \implies D \approx \frac{b}{\phi}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation for Copper ($b = 0.256 \text{ nm}, D = 12.0 \text{ nm}$)</div>
      $$\phi = \frac{b}{D} = \frac{0.256 \text{ nm}}{12.0 \text{ nm}} = 0.02133 \text{ rad}$$
      <p>Convert radians to degrees:</p>
      $$\phi = 0.02133 \times \frac{180^\circ}{\pi} = \mathbf{1.222^\circ}$$
      <p>Convert fractional degrees to arcminutes ($1^\circ = 60'$):</p>
      $$\phi = 1^\circ + (0.222 \times 60') = \mathbf{1^\circ 13.3'}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Low-Angle vs. High-Angle Grain Boundaries</div>
      <ul>
        <li><strong>Low-Angle Boundaries ($\theta < 15^\circ$):</strong> Composed of discrete, identifiable, well-separated dislocations surrounded by large regions of perfect, undistorted crystalline lattice. Boundary energy $\gamma_{\text{gb}}$ increases with angle following Read-Shockley.</li>
        <li><strong>High-Angle Boundaries ($\theta > 15^\circ$):</strong> As $\theta$ approaches $15^\circ$, the dislocation spacing $D$ shrinks to $3\text{--}4$ atomic diameters ($D \approx b/\theta$). Dislocation cores physically overlap, destroying individual dislocation identity. The boundary becomes an open, disordered, quasi-liquid-like transition zone of structural disorder $2\text{--}5$ atomic layers thick with roughly constant high interfacial energy ($\gamma_{\text{gb}} \approx 0.3\text{--}0.6 \text{ J/m}^2$).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Twist Boundary:</strong> Orthogonal cross-grid of screw dislocations &bull; $\phi \approx b/D$.<br>
      <strong>For Cu ($D = 12\text{ nm}$):</strong> $\phi = \mathbf{1.22^\circ}$ ($1^\circ 13'$).<br>
      Low-angle boundaries consist of discrete dislocations; high-angle boundaries ($\theta > 15^\circ$) consist of overlapping cores forming disordered interfaces.
    </div>""")

# P40: High-Angle Grain Boundaries & Segregation
add(40, "High-Angle Grain Boundaries: Interfacial Energy, Solute Segregation, and Sensitization",
    "Planar & Interfacial Defects", "planar_defects", "Intermediate",
    r"""<p>High-angle grain boundaries ($\theta > 15^\circ$) constitute the vast majority of internal interfaces in commercial engineering metals.</p>
    <ol type="a">
      <li>Explain why the atomic packing density at a high-angle grain boundary is significantly lower than in the interior of a grain, and state the relative magnitude of grain boundary energy $\gamma_{\text{gb}}$ compared to surface energy $\gamma_s$.</li>
      <li>Explain why grain boundaries act as preferred sites for:
        <ul>
          <li>Atomic diffusion (short-circuit grain boundary diffusion).</li>
          <li>Equilibrium solute segregation (e.g., phosphorus in steel causing temper embrittlement).</li>
          <li>Heterogeneous nucleation of second-phase precipitates.</li>
        </ul>
      </li>
      <li>Describe the phenomenon of <strong>sensitization and intergranular corrosion</strong> in austenitic stainless steels (e.g., AISI 304 welded structures). What chemical reaction occurs at grain boundaries between $500\text{--}800^\circ\text{C}$?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Grain Boundary Energy and Packing</div>
      <p>Because the atomic lattices of adjacent grains meet at random spatial orientations, atoms within the boundary plane cannot satisfy the regular coordination polyhedra of either crystal. The interface has a disordered, open structure with lower local packing density, containing excess free volume and numerous distorted, broken bonds. The boundary energy is typically about one-third of the external surface energy: $\gamma_{\text{gb}} \approx \frac{1}{3} \gamma_s$ ($\sim 0.3\text{--}0.8 \text{ J/m}^2$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Grain Boundaries as Preferred Kinetic and Thermodynamic Sites</div>
      <ul>
        <li><strong>Short-Circuit Diffusion:</strong> The open excess volume and distorted bonds provide lower migration activation barriers for atomic jumps. Consequently, grain boundary diffusion coefficients are millions of times higher than bulk lattice diffusion ($D_{\text{gb}} \gg D_L$), dominating mass transport at low to intermediate temperatures ($T < 0.5 T_m$).</li>
        <li><strong>Solute Segregation:</strong> Impurity atoms with severe size misfits (e.g., oversized Phosphorus, Sulfur, Tin in steel) produce large elastic strain in the bulk lattice. Migrating into the open, relaxed sites of the grain boundary relieves this strain energy. Driven by McLean equilibrium segregation, solute concentrations at grain boundaries can reach $1000\times$ higher than bulk levels, causing grain boundary decohesion and temper embrittlement.</li>
        <li><strong>Heterogeneous Nucleation:</strong> Precipitating a new phase at a grain boundary destroys a portion of the high-energy grain boundary area, releasing interfacial energy $\gamma_{\text{gb}}$ that dramatically reduces the thermodynamic activation energy barrier for nucleation ($\Delta G^*_{\text{het}} \ll \Delta G^*_{\text{hom}}$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Sensitization and Intergranular Corrosion in Stainless Steel</div>
      <p>When austenitic stainless steel (e.g., AISI 304, containing $18\text{ wt}\%\text{ Cr}$ and $0.06\text{ wt}\%\text{ C}$) is heated in the range $500\text{--}800^\circ\text{C}$ (e.g., during welding cooling):</p>
      <ol>
        <li>Carbon diffuses rapidly to grain boundaries and reacts with chromium to precipitate Chromium Carbide ($\text{Cr}_{23}\text{C}_6$) along the boundary interface:
        $$23\text{Cr} + 6\text{C} \to \text{Cr}_{23}\text{C}_6$$</li>
        <li>Because chromium diffuses millions of times slower than interstitial carbon, it is drawn only from the immediate nanometer-thin zone adjacent to the boundary. The local chromium concentration in this depleted zone plunges below the critical <strong>$12\text{ wt}\%$ passivation threshold</strong>.</li>
        <li>When exposed to corrosive aqueous environments, this chromium-depleted channel acts as a tiny active anode against the large cathodic grain bodies, dissolving rapidly via galvanic action and causing catastrophic <strong>intergranular attack and grain fallout</strong> (sensitization).</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>High-Angle Boundaries:</strong> Disordered open interface, $\gamma_{\text{gb}} \approx \frac{1}{3}\gamma_s$.<br>
      <strong>Phenomena:</strong> Fast short-circuit diffusion, solute segregation (embrittlement), and preferred precipitate nucleation.<br>
      <strong>Sensitization:</strong> Precipitation of $\text{Cr}_{23}\text{C}_6$ depletes local Cr below $12\text{ wt}\%$, causing severe intergranular corrosion along weld heat-affected zones.
    </div>""")

# P41: Twin Boundaries
add(41, "Twin Boundaries: Coherent vs. Incoherent Interfaces, Annealing vs. Deformation Twins",
    "Planar & Interfacial Defects", "planar_defects", "Fundamental",
    r"""<p>A twin boundary is a special, highly ordered homophase planar defect across which the crystal lattice exhibits a mirror reflection symmetry.</p>
    <ol type="a">
      <li>Define a <strong>twin boundary</strong> and distinguish between:
        <ul>
          <li>A <strong>coherent twin boundary</strong>.</li>
          <li>An <strong>incoherent twin boundary</strong>.</li>
        </ul>
      </li>
      <li>Compare the interfacial energy of a coherent twin boundary ($\gamma_{\text{twin}}$) with that of a general high-angle grain boundary ($\gamma_{\text{gb}}$).</li>
      <li>Differentiate between <strong>annealing twins</strong> (observed in FCC metals like brass and austenitic steel) and <strong>mechanical (deformation) twins</strong> (observed in BCC and HCP metals like iron and zinc) in terms of morphology, origin, and deformation temperature.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition of Coherent vs. Incoherent Twin Boundaries</div>
      <ul>
        <li><strong>Twin Boundary:</strong> A planar interface separating two crystal regions that are crystallographic mirror images of one another across a specific mirror composition plane (twin plane).</li>
        <li><strong>Coherent Twin Boundary:</strong> The boundary plane coincides exactly with the crystallographic twinning plane (e.g., $\{111\}$ in FCC). Atoms in the boundary plane are shared perfectly by both the parent and twinned lattices with zero broken bonds and only minor second-nearest-neighbor bond angle distortion.</li>
        <li><strong>Incoherent Twin Boundary:</strong> The boundary plane does not coincide with the twinning plane (e.g., steps or ledges connecting parallel coherent twin segments). Contains misaligned, strained, and broken bonds.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Interfacial Energy Comparison</div>
      <p>Because a coherent twin boundary preserves perfect nearest-neighbor atomic coordination, its interfacial energy is extraordinarily low—typically only <strong>2% to 5% of a general grain boundary</strong>:</p>
      $$\gamma_{\text{coherent twin}} \approx 0.01\text{ to }0.05 \times \gamma_{\text{gb}} \quad (\sim 10\text{ to }30 \text{ mJ/m}^2)$$
      <p>Incoherent twin boundaries have much higher energy ($\sim 200\text{ to }400 \text{ mJ/m}^2$), approaching general grain boundaries.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Annealing Twins vs. Mechanical (Deformation) Twins</div>
      <ul>
        <li><strong>Annealing Twins (FCC metals, e.g., Brass, Austenitic Steel, Nickel):</strong>
          <ul>
            <li><em>Origin:</em> Form during recrystallization and grain growth after cold working, nucleated by accidental growth errors on $\{111\}$ stacking planes.</li>
            <li><em>Morphology:</em> Broad, straight-sided parallel bands with perfectly rectilinear boundary lines extending across entire grains.</li>
            <li><em>Occurrence:</em> Favored in metals with low stacking fault energy (e.g., brass, $\gamma$-stainless steel; absent in high-SFE aluminum).</li>
          </ul>
        </li>
        <li><strong>Mechanical / Deformation Twins (BCC and HCP metals, e.g., $\alpha$-Fe, Ti, Zn, Mg):</strong>
          <ul>
            <li><em>Origin:</em> Form mechanically via collective homogeneous atomic shear displacements when normal dislocation slip is restricted (e.g., at low temperatures, high strain rates, or in HCP crystals with few slip systems).</li>
            <li><em>Morphology:</em> Narrow, sharp, lenticular (lens-shaped) or needle-like lamellae that taper to sharp points at grain boundaries.</li>
            <li><em>Occurrence:</em> In iron at cryogenic temperatures (Neumann bands) and in titanium/magnesium forming during sheet stamping.</li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Twin Boundary:</strong> Mirror symmetry interface &bull; Coherent twin energy is ultra-low ($\gamma_{\text{twin}} \approx 0.03 \gamma_{\text{gb}}$).<br>
      <strong>Annealing Twins (FCC):</strong> Broad parallel rectilinear bands formed during thermal recrystallization (favored by low SFE).<br>
      <strong>Mechanical Twins (BCC/HCP):</strong> Sharp lenticular needles formed by high-speed or low-temperature plastic shear.
    </div>""")

# P42: Stacking Faults in FCC Crystals
add(42, "Stacking Faults in FCC Crystals: Intrinsic vs. Extrinsic Faults and Stacking Fault Energy",
    "Planar & Interfacial Defects", "planar_defects", "Intermediate",
    r"""<p>Stacking faults are planar errors in the sequential stacking of close-packed atomic planes in FCC and HCP lattices.</p>
    <ol type="a">
      <li>State the normal close-packed stacking sequence of:
        <ul>
          <li>An ideal <strong>FCC</strong> crystal.</li>
          <li>An ideal <strong>HCP</strong> crystal.</li>
        </ul>
      </li>
      <li>Illustrate the stacking sequence of:
        <ul>
          <li>An <strong>intrinsic stacking fault</strong> in FCC (removal of a plane).</li>
          <li>An <strong>extrinsic stacking fault</strong> in FCC (insertion of an extra plane).</li>
        </ul>
        Identify the local HCP micro-layer embedded in the FCC matrix.</li>
      <li>Explain the concept of <strong>Stacking Fault Energy (SFE)</strong> and describe how high SFE (e.g., Aluminum, $\approx 160 \text{ mJ/m}^2$) versus low SFE (e.g., Cartridge Brass, $\approx 15 \text{ mJ/m}^2$) governs dislocation dissociation width ($d \propto 1/\text{SFE}$), cross-slip propensity, and work hardening behavior.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Ideal Stacking Sequences</div>
      <ul>
        <li><strong>FCC $\{111\}$ Planes:</strong> Stacks in a 3-layer periodic sequence:
        $$\dots \text{A B C A B C A B C} \dots$$</li>
        <li><strong>HCP $(0001)$ Basal Planes:</strong> Stacks in a 2-layer periodic sequence:
        $$\dots \text{A B A B A B A B} \dots$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Intrinsic vs. Extrinsic Stacking Faults in FCC</div>
      <ul>
        <li><strong>Intrinsic Stacking Fault (Removal of a plane, e.g., plane B is removed by vacancy condensation):</strong>
        $$\dots \text{A B C A } \mathbf{C A B C} \dots \quad \text{or} \quad \dots \text{A B C A } \underline{\mathbf{B A B}} \text{ C A B} \dots$$
        Notice the underlined local sequence $\text{B A B}$: it forms a slab of <strong>2 layers of HCP stacking</strong> inside the FCC crystal!</li>
        <li><strong>Extrinsic Stacking Fault (Insertion of an extra plane, e.g., plane C inserted by interstitial aggregation):</strong>
        $$\dots \text{A B C A } \mathbf{B} \underline{\mathbf{C B A B}} \text{ C A B} \dots$$
        Notice the local fault contains <strong>3 layers of HCP stacking</strong> bounded by two fault planes.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Stacking Fault Energy (SFE) and Metallurgical Behavior</div>
      <p>A full dislocation $\frac{a}{2}\langle 110\rangle$ dissociates into two Shockley partial dislocations $\frac{a}{6}\langle 112\rangle$ separated by a ribbon of stacking fault. The equilibrium ribbon width $d$ is determined by a force balance between elastic repulsion of the partials and the surface tension of the stacking fault:</p>
      $$d \approx \frac{G b_{\text{partial}}^2}{2\pi \gamma_{\text{SFE}}}$$
      <ul>
        <li><strong>High SFE (e.g., Aluminum, $\text{SFE} \approx 160 \text{ mJ/m}^2$):</strong> The stacking fault ribbon is extremely narrow ($d \approx 1 \text{ nm}$). The partials recombine easily, allowing screw dislocations to <strong>cross-slip effortlessly</strong>. This promotes dynamic recovery, wavy slip lines, and cell dislocation structures.</li>
        <li><strong>Low SFE (e.g., 70-30 Brass, $\text{SFE} \approx 15 \text{ mJ/m}^2$, 304 Stainless, $\sim 20 \text{ mJ/m}^2$):</strong> The stacking fault ribbon is wide ($d > 5\text{--}10 \text{ nm}$). Because partials must constrict to cross-slip, cross-slip is virtually prohibited. Dislocations remain constrained to planar slip arrays, producing intense planar work hardening, high strain-hardening exponents ($n$), and deformation twinning.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>FCC Stacking:</strong> $\text{ABCABC} \dots$ &bull; <strong>HCP Stacking:</strong> $\text{ABAB} \dots$<br>
      <strong>Intrinsic Fault:</strong> Plane removed ($\dots \text{ABCA} \mid \text{CABC} \dots$), creating local HCP layer.<br>
      <strong>SFE Influence:</strong> High SFE (Al) $\implies$ narrow ribbon, easy cross-slip, wavy slip.<br>
      Low SFE (Brass) $\implies$ wide ribbon, blocked cross-slip, planar slip, high work hardening.
    </div>""")

# Save checkpoint for part 2 (33 to 42)
print("Part 2: P33-P42 appended successfully.")
# P43: Phase Boundaries & Interphase Interfaces
add(43, "Phase Boundaries: Coherent, Semicoherent, and Incoherent Interphase Interfaces",
    "Planar & Interfacial Defects", "planar_defects", "Intermediate",
    r"""<p>In multi-phase engineering alloys (such as precipitation-hardened aluminum or nickel-base superalloys), interphase boundaries separate phases with distinct crystal structures and chemical compositions.</p>
    <ol type="a">
      <li>Differentiate between the three fundamental types of interphase boundaries:
        <ul>
          <li><strong>Fully Coherent Interface</strong></li>
          <li><strong>Semicoherent Interface</strong></li>
          <li><strong>Incoherent Interface</strong></li>
        </ul>
      </li>
      <li>Derive the formula for the spacing $D$ between <strong>interfacial misfit dislocations</strong> in a semicoherent interface between two cubic phases with lattice parameters $a_\alpha$ and $a_\beta$ ($a_\beta > a_\alpha$):
      $$\delta = \frac{a_\beta - a_\alpha}{a_\alpha}, \quad D = \frac{a_\alpha}{\delta} = \frac{a_\alpha a_\beta}{a_\beta - a_\alpha}$$</li>
      <li>Compare the three boundary types in terms of interfacial energy ($\gamma_{\text{int}}$) and explain why $\gamma/\gamma'$ interfaces in nickel superalloys remain coherent over thousands of operating hours.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): The Three Classes of Interphase Interfaces</div>
      <ul>
        <li><strong>Fully Coherent Interface:</strong> The two adjoining crystals maintain a one-to-one continuity of atomic planes across the entire boundary with zero broken bonds or dislocations. Lattice parameter differences are accommodated purely by elastic strain in the two lattices.</li>
        <li><strong>Semicoherent Interface:</strong> When the lattice misfit exceeds $\sim 5\%$, elastic strain energy becomes too large to sustain pure coherence. The lattice strains are periodically relieved by an array of <strong>interfacial misfit dislocations</strong> embedded within the boundary plane. Between dislocations, the lattice matches coherently.</li>
        <li><strong>Incoherent Interface:</strong> The atomic structures and lattice spacings of the two phases differ so drastically that no periodic atomic matching occurs across the interface. The boundary is an open, disordered interface akin to a high-angle grain boundary.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Misfit Dislocation Spacing Derivation</div>
      <p>Let $a_\alpha$ and $a_\beta$ be the lattice parameters of the two phases across the interface. Over interface length $D$, let there be $n$ unit cells of phase $\beta$ matching $(n+1)$ unit cells of phase $\alpha$:</p>
      $$D = n a_\beta = (n + 1) a_\alpha \implies n(a_\beta - a_\alpha) = a_\alpha \implies n = \frac{a_\alpha}{a_\beta - a_\alpha}$$
      <p>The misfit parameter is defined as $\delta = \frac{a_\beta - a_\alpha}{a_\alpha}$. Substituting into the expression for $D$:</p>
      $$D = n a_\beta = \left(\frac{a_\alpha}{a_\beta - a_\alpha}\right) a_\beta = \frac{a_\beta}{\delta} \approx \frac{a_\alpha}{\delta} = \frac{a_\alpha a_\beta}{a_\beta - a_\alpha}$$
      <p>Every distance $D$ along the interface, exactly one extra half-plane of atoms ends, forming an edge misfit dislocation of Burgers vector $b \approx a_\alpha$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Interfacial Energies and Superalloy Stability</div>
      <ul>
        <li><strong>Interfacial Energies:</strong>
          <ul>
            <li>Coherent: $\gamma \approx 1\text{ to }50 \text{ mJ/m}^2$ (extremely low).</li>
            <li>Semicoherent: $\gamma \approx 100\text{ to }300 \text{ mJ/m}^2$ (moderate, due to dislocation core energies).</li>
            <li>Incoherent: $\gamma \approx 500\text{ to }1000 \text{ mJ/m}^2$ (high, high structural disorder).</li>
          </ul>
        </li>
        <li><strong>Nickel Superalloys:</strong> In single-crystal turbine blades, the FCC matrix ($\gamma$) and $\text{Ni}_3\text{Al}$ precipitate ($\gamma'$) have nearly identical lattice parameters ($\delta \approx 0.1\text{--}0.5\%$). This ultra-low misfit keeps the $\gamma/\gamma'$ interface <strong>fully coherent with negligible interfacial energy ($\gamma \approx 10\text{ mJ/m}^2$)</strong>. Because the thermodynamic driving force for precipitate coarsening (Ostwald ripening, $d\bar{r}/dt \propto \gamma_{\text{int}} D$) is directly proportional to $\gamma_{\text{int}}$, the precipitates resist coarsening and maintain high creep strength at $1100^\circ\text{C}$ for thousands of hours.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Interface Types:</strong> Coherent ($\gamma < 50\text{ mJ/m}^2$) &bull; Semicoherent ($\gamma \approx 200\text{ mJ/m}^2$) &bull; Incoherent ($\gamma > 500\text{ mJ/m}^2$).<br>
      <strong>Misfit Dislocation Spacing:</strong> $$D = \frac{a_\alpha}{\delta} = \frac{a_\alpha a_\beta}{a_\beta - a_\alpha}$$
      Nickel superalloys maintain coherence due to near-zero misfit ($\delta < 0.5\%$), suppressing Ostwald coarsening.
    </div>""")

# P44: Volume Defects
add(44, "Volume (3D) Defects: Porosity, Second-Phase Inclusions, and Microcracks",
    "Volume Defects & Characterization", "volume_defects", "Fundamental",
    r"""<p>Three-dimensional (volume) defects are macroscopic or microscopic volumetric disruptions in the continuity of a solid component.</p>
    <ol type="a">
      <li>Describe the physical characteristics, origin, and deleterious effects of:
        <ul>
          <li><strong>Gas Porosity vs. Shrinkage Cavities</strong> in cast metal ingots.</li>
          <li><strong>Non-Metallic Inclusions</strong> (e.g., oxides, sulfides, silicates) in structural steels.</li>
          <li><strong>Quench Microcracks</strong> in heat-treated high-carbon steels.</li>
        </ul>
      </li>
      <li>Why do spherical inclusions produce severe stress concentrations under uniaxial tensile loading? State the stress concentration factor $K_t$ for a spherical void.</li>
      <li>Describe industrial quality-control methods (e.g., vacuum degassing, calcium treatment of steel) employed to eliminate or modify volume defects.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Characteristics, Origins, and Detriments of Volume Defects</div>
      <ul>
        <li><strong>Gas Porosity vs. Shrinkage Cavities:</strong>
          <ul>
            <li><em>Gas Porosity:</em> Smooth, spherical microscopic voids caused by the rejection of dissolved gases (hydrogen in Al/steel, nitrogen, oxygen) whose liquid solubility drops abruptly upon solidification.</li>
            <li><em>Shrinkage Cavities:</em> Rough, jagged, dendritic voids formed in the thermal center of a casting because liquid metals contract by $3\text{--}7\%$ upon solidifying without sufficient feeder reservoir (riser) compensation.</li>
            <li><em>Detriment:</em> Both defects drastically reduce fatigue life and act as crack initiation sites under cyclic mechanical loads.</li>
          </ul>
        </li>
        <li><strong>Non-Metallic Inclusions:</strong>
          Exogenous or endogenous particles of deoxidation products (e.g., alumina $\text{Al}_2\text{O}_3$, silica $\text{SiO}_2$, iron-manganese sulfides $\text{MnS}$). Hard, brittle angular inclusions act as severe internal stress raisers, debonding under tensile strain and causing ductile microvoid coalescence or brittle cleavage initiation.</li>
        <li><strong>Quench Microcracks:</strong>
          Sharp planar cracks formed when the volumetric expansion of martensite transformation ($1\text{--}4\%$) coincides with steep thermal contraction gradients during aggressive water quenching of high-carbon steel.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Stress Concentration Factor of a Spherical Void</div>
      <p>Under a uniform uniaxial far-field tensile stress $\sigma_0$, the presence of an isolated spherical cavity redistributes the internal stress field (Goodier's solution in 3D elasticity). At the equator of the spherical void perpendicular to the tensile axis, the local stress is magnified to:</p>
      $$\sigma_{\max} = 2.05 \sigma_0 \implies K_t = \frac{\sigma_{\max}}{\sigma_0} \approx \mathbf{2.0}$$
      <p>For sharp-edged, elongated, or cracked inclusions, $K_t$ can exceed 10 to 50.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Industrial Elimination and Modification Methods</div>
      <ul>
        <li><strong>Vacuum Degassing (VD / VOD):</strong> Molten steel is subjected to high vacuum ($< 1 \text{ mbar}$) prior to casting, stripping dissolved hydrogen ($< 1\text{ ppm}$) and carbon monoxide gases to eliminate gas porosity.</li>
        <li><strong>Calcium Treatment / Inclusion Shape Control:</strong> Adding small amounts of calcium (CaSi) to molten steel converts stringer-like, deformable $\text{MnS}$ and brittle $\text{Al}_2\text{O}_3$ clouds into tiny, isolated, hard spherical calcium aluminates/sulfides, preventing directional embrittlement (lamellar tearing).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Volume Defects:</strong> Porosity (gas vs shrinkage), non-metallic inclusions, and quench microcracks.<br>
      <strong>Stress Concentration:</strong> $K_t \approx \mathbf{2.0}$ for spherical voids (much higher for angular inclusions).<br>
      <strong>Industrial Controls:</strong> Vacuum degassing (gas removal) and calcium treatment (inclusion spherodization).
    </div>""")

# P45: Microscopic Techniques Comparison
add(45, "Materials Characterization: Optical Microscopy, SEM, TEM, and SPM Comparison",
    "Volume Defects & Characterization", "volume_defects", "Fundamental",
    r"""<p>Microstructural characterization across spatial scales from millimeters down to sub-angstroms requires distinct microscopic instruments.</p>
    <ol type="a">
      <li>Compare the following four characterization techniques:
        <ul>
          <li><strong>Optical Microscopy (OM)</strong></li>
          <li><strong>Scanning Electron Microscopy (SEM)</strong></li>
          <li><strong>Transmission Electron Microscopy (TEM)</strong></li>
          <li><strong>Scanning Probe Microscopy (AFM / STM)</strong></li>
        </ul>
        specifying for each: the radiation/probe used, typical resolution limit, maximum practical magnification, and specimen preparation requirements.</li>
      <li>Calculate the theoretical diffraction-limited spatial resolution $d_{\min} = \frac{0.61 \lambda}{\text{NA}}$ of an optical microscope using green light ($\lambda = 550 \text{ nm}$) and an oil-immersion objective ($\text{NA} = 1.40$).</li>
      <li>Calculate the de Broglie wavelength of an electron accelerated through $V = 200 \text{ kV}$ in a TEM, and explain why TEM can resolve individual dislocation lines and crystal lattice planes.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Systematic Instrumentation Comparison</div>
      <table class="table-styled">
        <thead><tr><th>Technique</th><th>Radiation / Probe</th><th>Resolution Limit</th><th>Useful Magnification</th><th>Specimen Preparation</th></tr></thead>
        <tbody>
          <tr><td><strong>Optical (OM)</strong></td><td>Visible Light ($\lambda \approx 400\text{--}700\text{ nm}$)</td><td>$\sim 0.2 \mu\text{m}$ ($200\text{ nm}$)</td><td>$50\times\text{--}1500\times$</td><td>Grinding, fine diamond polish, chemical etching</td></tr>
          <tr><td><strong>SEM</strong></td><td>Focused Electron Beam ($1\text{--}30\text{ kV}$)</td><td>$\sim 1\text{--}5\text{ nm}$</td><td>$20\times\text{--}500,000\times$</td><td>Conductive surface (carbon/gold coating for insulators)</td></tr>
          <tr><td><strong>TEM</strong></td><td>Transmitted High-Energy Electrons ($100\text{--}300\text{ kV}$)</td><td>$\sim 0.05\text{--}0.2\text{ nm}$ ($0.5\text{--}2\text{ \AA}$)</td><td>$5,000\times\text{--}2,000,000\times$</td><td>Electron-transparent foil ($\text{thickness} < 100\text{ nm}$ via FIB/electropolishing)</td></tr>
          <tr><td><strong>AFM / STM</strong></td><td>Physical sharp cantilever tip (radius $\sim 2\text{--}10\text{ nm}$)</td><td>$\sim 0.01\text{ nm}$ (vertical), $0.1\text{ nm}$ (lateral)</td><td>$> 1,000,000\times$</td><td>Flat surface, vibration-isolated table</td></tr>
        </tbody>
      </table>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Abbe Diffraction Resolution Limit of Optical Microscope</div>
      $$d_{\min} = \frac{0.61 \lambda}{\text{NA}} = \frac{0.61 \times 550 \text{ nm}}{1.40} = \frac{335.5}{1.40} = \mathbf{239.6 \text{ nm} \approx 0.24 \mu\text{m}}$$
      <p>Optical microscopy cannot resolve any microstructural feature smaller than approximately a quarter of a micrometer ($240 \text{ nm}$). Because individual dislocations and point defects are nanometer-scale, they are completely invisible in optical microscopes.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Relativistic de Broglie Wavelength for $200 \text{ kV}$ TEM</div>
      <p>Using the relativistic de Broglie equation:</p>
      $$\lambda = \frac{h}{\sqrt{2 m_0 e V \left(1 + \frac{e V}{2 m_0 c^2}\right)}}$$
      <p>For $V = 200 \text{ kV} = 200,000 \text{ V}$ ($e V / 2 m_0 c^2 = 200 / 1022 = 0.1957$):</p>
      $$\lambda = \frac{1.226 \text{ nm}}{\sqrt{V(1 + 0.9785 \times 10^{-6} V)}} = \frac{1.226}{\sqrt{200,000(1 + 0.1957)}} = \frac{1.226}{\sqrt{239,140}} = \frac{1.226}{489.0} = \mathbf{0.00251 \text{ nm} = 0.0251 \text{ \AA}}$$
      <p>The electron wavelength ($0.0025 \text{ nm}$) is over <strong>100,000 times shorter than visible light</strong>! This exceptionally short wavelength allows TEM to produce diffraction contrast that directly images individual dislocation lines, stacking fault fringes, and atomic column projections (HRTEM).</p>
    </div>
    <div class="final-answer-box">
      <strong>Optical Microscope Limit:</strong> $d_{\min} \approx \mathbf{0.24 \mu\text{m}}$ ($240\text{ nm}$).<br>
      <strong>$200 \text{ kV}$ TEM Wavelength:</strong> $\lambda = \mathbf{0.00251 \text{ nm} = 0.0251 \text{ \AA}}$.<br>
      Short electron wavelength enables direct imaging of dislocation strain fields and atomic columns.
    </div>""")

# P46: ASTM Grain Size Number Definition and Magnification Scaling
add(46, "Quantitative Metallography: ASTM Grain Size Number $n$ and Magnification Scaling",
    "Volume Defects & Characterization", "volume_defects", "Fundamental",
    r"""<p>The standard ASTM grain size number $n$ is defined by ASTM Standard E112 to quantify the grain size of polycrystalline engineering metals.</p>
    <ol type="a">
      <li>State the mathematical definition of the <strong>ASTM grain size number $n$</strong>:
      $$N = 2^{n-1}$$
      specifying the exact experimental observation conditions under which $N$ is measured.</li>
      <li>Derive the generalized formula for the number of grains per square inch $N_M$ observed at an arbitrary magnification $M \neq 100\times$:
      $$N_M \left(\frac{M}{100}\right)^2 = 2^{n-1} \implies N_M = 2^{n-1} \left(\frac{100}{M}\right)^2$$</li>
      <li>A micrograph of an annealed brass specimen taken at $250\times$ magnification contains an average of 45 grains in a 1 square inch field of view. Calculate the ASTM grain size number $n$.</li>
      <li>Does a higher ASTM grain size number correspond to a finer or coarser grain structure? Explain.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Standard Definition of ASTM Grain Size Number $n$</div>
      <p>The ASTM grain size number $n$ is defined by the relation:</p>
      $$N = 2^{n-1}$$
      <p>where $N$ is the number of whole grains counted per <strong>1 square inch of area ($1.0 \text{ in}^2$)</strong> on a photomicrograph taken at a standardized linear magnification of <strong>$100\times$</strong>.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Magnification Scaling Derivation</div>
      <p>Let $A_{\text{field}} = 1.0 \text{ in}^2$ be the photo area. The true physical area on the specimen surface examined at magnification $M$ is:</p>
      $$A_{\text{true}} = \frac{1.0 \text{ in}^2}{M^2}$$
      <p>At standard $100\times$ magnification, the true physical area examined is $A_{100} = \frac{1.0 \text{ in}^2}{100^2}$.</p>
      <p>Because the real grain density per unit true specimen area is a constant physical property:</p>
      $$\text{Grain Density} = \frac{N_M}{A_{\text{true}, M}} = \frac{N_{100}}{A_{\text{true}, 100}} \implies N_M \cdot M^2 = N_{100} \cdot 100^2$$
      $$N_{100} = N_M \left(\frac{M}{100}\right)^2$$
      <p>Equating this to the ASTM definition $N_{100} = 2^{n-1}$:</p>
      $$N_M \left(\frac{M}{100}\right)^2 = 2^{n-1} \implies N_M = 2^{n-1} \left(\frac{100}{M}\right)^2$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation for Brass ($N_{250} = 45, M = 250\times$)</div>
      <p>First, scale the grain count to standard $100\times$ magnification:</p>
      $$N_{100} = N_M \left(\frac{M}{100}\right)^2 = 45 \times \left(\frac{250}{100}\right)^2 = 45 \times (2.5)^2 = 45 \times 6.25 = \mathbf{281.25 \text{ grains/in}^2}$$
      <p>Now solve for $n$ using $2^{n-1} = N_{100}$:</p>
      $$n - 1 = \frac{\ln(N_{100})}{\ln(2)} = \frac{\ln(281.25)}{\ln(2)} = \frac{5.6392}{0.69315} = 8.135$$
      $$n = 8.135 + 1 = \mathbf{9.14 \approx 9}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): ASTM Number vs. Grain Size Relationship</div>
      <p>Because $N = 2^{n-1}$, a <strong>higher ASTM grain size number corresponds to a larger number of grains per unit area, and hence a much finer (smaller) average grain size</strong>. Conversely, low ASTM numbers ($n = 1\text{--}3$) correspond to coarse grains, while high numbers ($n = 8\text{--}12$) represent fine-grained microstructures.</p>
    </div>
    <div class="final-answer-box">
      <strong>ASTM Definition:</strong> $N_{100} = 2^{n-1}$ at $100\times$.<br>
      <strong>Magnification Scaling:</strong> $$N_{100} = N_M \left(\frac{M}{100}\right)^2$$
      <strong>Calculated Value:</strong> $N_{100} = 281.25 \implies n = \mathbf{9.14 \approx 9}$.<br>
      Higher ASTM number $\implies$ finer grain size.
    </div>""")

# P47: Converting ASTM Grain Size to Mean Diameter
add(47, "ASTM Grain Size Conversion: Calculating Average Grain Diameter and Area",
    "Volume Defects & Characterization", "volume_defects", "Intermediate",
    r"""<p>Engineering designers require physical dimensional units (mean grain diameter $d$ in micrometers) rather than empirical ASTM numbers for Hall-Petch strength calculations.</p>
    <ol type="a">
      <li>Derive the formula relating the mean planar grain cross-sectional area $\bar{A}$ (in $\text{mm}^2$) and average equivalent grain diameter $\bar{d}$ (in $\mu\text{m}$) to the ASTM grain size number $n$, assuming approximately equiaxed hexagonal planar grains.</li>
      <li>Calculate the average grain diameter $\bar{d}$ in micrometers ($\mu\text{m}$) for:
        <ul>
          <li>ASTM grain size $n = 4$ (coarse-grained casting).</li>
          <li>ASTM grain size $n = 8$ (standard fine-grained structural steel).</li>
          <li>ASTM grain size $n = 12$ (microalloyed ultra-fine grained steel).</li>
        </ul>
      </li>
      <li>How does a change of $+1$ in ASTM number change the number of grains and the average grain diameter?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Mean Diameter $\bar{d}$ from ASTM $n$</div>
      <p>At $100\times$ magnification, $1.0 \text{ in}^2$ of photo area corresponds to a true physical area on the specimen of:</p>
      $$A_{\text{true}} = \frac{1.0 \text{ in}^2}{100^2} = 1.0 \times 10^{-4} \text{ in}^2$$
      <p>Converting square inches to square millimeters ($1 \text{ in} = 25.4 \text{ mm} \implies 1 \text{ in}^2 = 645.16 \text{ mm}^2$):</p>
      $$A_{\text{true}} = (1.0 \times 10^{-4}) \times 645.16 \text{ mm}^2 = 0.064516 \text{ mm}^2$$
      <p>The number of grains in this true area is $N = 2^{n-1}$. Therefore, the average planar area per grain $\bar{A}$ is:</p>
      $$\bar{A} = \frac{A_{\text{true}}}{N} = \frac{0.064516 \text{ mm}^2}{2^{n-1}} \quad [\text{mm}^2]$$
      <p>Approximating grain cross-sections as equivalent circles ($\bar{A} = \frac{\pi}{4}\bar{d}^2$):</p>
      $$\bar{d} = \sqrt{\frac{4\bar{A}}{\pi}} = \sqrt{\frac{4 \times 0.064516}{\pi \cdot 2^{n-1}}} = \sqrt{\frac{0.08214}{2^{n-1}}} \text{ mm}$$
      <p>Converting to micrometers ($1 \text{ mm} = 1000 \mu\text{m}$):</p>
      $$\bar{d} = \frac{286.6}{\sqrt{2^{n-1}}} \mu\text{m} = \frac{286.6}{2^{(n-1)/2}} \mu\text{m} = \frac{405.3}{2^{n/2}} \mu\text{m}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculations for $n = 4, 8, 12$</div>
      <ul>
        <li><strong>For ASTM $n = 4$:</strong>
          $$N = 2^{4-1} = 2^3 = 8 \text{ grains/in}^2$$
          $$\bar{A} = \frac{0.064516}{8} = 8.0645 \times 10^{-3} \text{ mm}^2 = 8065 \mu\text{m}^2$$
          $$\bar{d} = \sqrt{\frac{4 \times 8065}{\pi}} = \sqrt{10268} = \mathbf{101.3 \mu\text{m} \approx 0.10 \text{ mm}}$$
        </li>
        <li><strong>For ASTM $n = 8$:</strong>
          $$N = 2^{8-1} = 2^7 = 128 \text{ grains/in}^2$$
          $$\bar{A} = \frac{0.064516}{128} = 5.0403 \times 10^{-4} \text{ mm}^2 = 504 \mu\text{m}^2$$
          $$\bar{d} = \sqrt{\frac{4 \times 504}{\pi}} = \sqrt{641.8} = \mathbf{25.3 \mu\text{m}}$$
        </li>
        <li><strong>For ASTM $n = 12$:</strong>
          $$N = 2^{12-1} = 2^{11} = 2048 \text{ grains/in}^2$$
          $$\bar{A} = \frac{0.064516}{2048} = 3.150 \times 10^{-5} \text{ mm}^2 = 31.5 \mu\text{m}^2$$
          $$\bar{d} = \sqrt{\frac{4 \times 31.5}{\pi}} = \sqrt{40.1} = \mathbf{6.33 \mu\text{m}}$$
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Rule of Thumb for $\Delta n = +1$</div>
      <ul>
        <li>Incrementing $n$ by $+1$ <strong>doubles the number of grains per unit area ($2\times$)</strong>: $N_{n+1} = 2 N_n$.</li>
        <li>Because area scales inversely with $N$, grain area halves ($0.5\times$).</li>
        <li>The average grain diameter decreases by a factor of $\sqrt{2} \approx 1.414$ (meaning $\bar{d}$ is multiplied by $\frac{1}{\sqrt{2}} \approx \mathbf{0.707}$, a $29.3\%$ reduction in diameter).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Diameter Conversion:</strong> $$\bar{d} \approx \frac{286.6}{2^{(n-1)/2}} \mu\text{m}$$
      <strong>Diameters:</strong> ASTM $4 \implies \bar{d} = \mathbf{101.3 \mu\text{m}}$ &bull; ASTM $8 \implies \bar{d} = \mathbf{25.3 \mu\text{m}}$ &bull; ASTM $12 \implies \bar{d} = \mathbf{6.33 \mu\text{m}}$.<br>
      Each $+1$ in ASTM number doubles grain count and reduces diameter by factor of $\sqrt{2}$ ($0.707\times$).
    </div>""")

# P48: Heyn Lineal Intercept Method
add(48, "The Heyn Lineal Intercept Method: Direct Experimental Grain Size Measurement",
    "Volume Defects & Characterization", "volume_defects", "Intermediate",
    r"""<p>The Heyn lineal intercept procedure (ASTM E112) is the most accurate and widely automated metallographic method for measuring true average grain diameter.</p>
    <ol type="a">
      <li>Describe the experimental procedure for performing the <strong>Heyn lineal intercept test</strong> on a polished and etched metallographic specimen.</li>
      <li>Define the mathematical formula for the <strong>mean lineal intercept length $\bar{\ell}$</strong>:
      $$\bar{\ell} = \frac{L_T}{P \cdot M}$$
      defining $L_T$, $P$, and $M$. How is $\bar{\ell}$ converted to true 3D spatial grain size $\bar{d}$?</li>
      <li>A test grid consisting of 5 random lines of total length $L_T = 500 \text{ mm}$ is superimposed over a micrograph of an annealed nickel alloy taken at $M = 400\times$. The total number of grain boundary intersections counted across all lines is $P = 85$.
        <ul>
          <li>Calculate the mean lineal intercept length $\bar{\ell}$ in micrometers.</li>
          <li>Calculate the true mean spherical grain diameter using standard ASTM stereological factor $\bar{d} = 1.571 \bar{\ell}$.</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Experimental Procedure of Heyn Intercept Method</div>
      <ol>
        <li>Prepare a metallographic cross-section by mechanical grinding, polishing to a mirror finish ($0.05 \mu\text{m}$ alumina or colloidal silica), and chemically etching to reveal grain boundary grooves.</li>
        <li>Capture a clear photomicrograph at known calibrated magnification $M$.</li>
        <li>Superimpose a set of random straight test lines (or concentric test circles to eliminate directional bias in elongated grains) of total measured line length $L_T$ onto the image.</li>
        <li>Count the total number of grain boundary intersections $P$ where test lines cut grain boundaries (an intersection that ends exactly on a boundary counts as $0.5$).</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Mean Lineal Intercept Equation and 3D Conversion</div>
      $$\bar{\ell} = \frac{L_T}{P \cdot M}$$
      <ul>
        <li>$L_T$: Total length of all test lines drawn on the photograph ($\text{mm}$).</li>
        <li>$P$: Total number of grain boundary intersection points counted.</li>
        <li>$M$: Linear magnification of the micrograph.</li>
        <li>$L_T / M$: True physical test length sampled on the actual specimen surface.</li>
      </ul>
      <p>A random planar test line slices through grains at arbitrary chords rather than across their maximum diameters. Rigorous stereological mathematical analysis (Fullman, Underwood) proves that for an assembly of uniform equiaxed spherical grains:</p>
      $$\bar{d}_{\text{true}} = \frac{4}{\pi} \bar{\ell} \approx 1.273 \bar{\ell} \quad \text{to} \quad \bar{d}_{\text{ASTM}} = 1.571 \bar{\ell}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations ($L_T = 500 \text{ mm}, M = 400\times, P = 85$)</div>
      <ul>
        <li><strong>Mean Lineal Intercept $\bar{\ell}$:</strong>
        $$\bar{\ell} = \frac{500 \text{ mm}}{85 \times 400} = \frac{500 \text{ mm}}{34,000} = 0.014706 \text{ mm}$$
        $$\bar{\ell} = 0.014706 \times 1000 \mu\text{m/mm} = \mathbf{14.71 \mu\text{m}}$$</li>
        <li><strong>True 3D Spatial Grain Diameter $\bar{d}$:</strong>
        $$\bar{d} = 1.571 \times 14.706 \mu\text{m} = \mathbf{23.10 \mu\text{m}}$$</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Heyn Intercept Formula:</strong> $$\bar{\ell} = \frac{L_T}{P \cdot M}$$
      <strong>Mean Lineal Intercept:</strong> $\bar{\ell} = \mathbf{14.71 \mu\text{m}}$.<br>
      <strong>True 3D Grain Diameter:</strong> $\bar{d} = 1.571 \bar{\ell} = \mathbf{23.1 \mu\text{m}}$.
    </div>""")

# P49: Grain Boundary Surface Area per Unit Volume (Sv)
add(49, "Quantitative Stereology: Grain Boundary Interfacial Area per Unit Volume ($S_v = 2 P_L$)",
    "Volume Defects & Characterization", "volume_defects", "Advanced",
    r"""<p>Stereology provides exact mathematical relationships connecting two-dimensional planar measurements on a cut section to three-dimensional volumetric parameters.</p>
    <ol type="a">
      <li>Derive the classic Saltykov-Smith stereological relationship proving that the total grain boundary surface area per unit volume $S_v$ (in $\text{mm}^2/\text{mm}^3 = \text{mm}^{-1}$) is exactly twice the number of boundary intercepts per unit length $P_L$:
      $$S_v = 2 P_L$$
      regardless of grain shape or distribution.</li>
      <li>For the nickel alloy examined in Problem 48 ($P = 85$ intercepts over true line length $L_{\text{true}} = \frac{500 \text{ mm}}{400} = 1.25 \text{ mm}$):
        <ul>
          <li>Calculate $P_L$ in $\text{mm}^{-1}$.</li>
          <li>Calculate $S_v$ in $\text{mm}^{-1}$ and $\text{cm}^2/\text{cm}^3$.</li>
        </ul>
      </li>
      <li>Calculate the total grain boundary surface area contained inside a $10 \text{ cm} \times 10 \text{ cm} \times 10 \text{ cm}$ turbine casing fabricated from this alloy.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Derivation of $S_v = 2 P_L$</div>
      <p>Consider an arbitrary isotropic 3D surface of total area $S$ randomly distributed inside volume $V$. Let a random test line of length $L$ traverse this volume.</p>
      <p>By Buffon-Laplace geometric probability theory, consider a tiny surface element $dA$ oriented at angle $\theta$ to the test line. The projected cross-sectional area perpendicular to the line is $dA \cos\theta$. Integrating over all random spatial orientations on a hemisphere ($0 \le \theta \le \pi/2$):</p>
      $$\langle \cos\theta \rangle = \frac{\int_0^{\pi/2} \cos\theta \sin\theta d\theta}{\int_0^{\pi/2} \sin\theta d\theta} = \frac{1/2}{1} = \frac{1}{2}$$
      <p>The probability that the test line of length $L$ intersects surface element $dA$ is $\frac{L \cdot \langle dA_{\text{proj}} \rangle}{V} = \frac{L \cdot \frac{1}{2} dA}{V}$.</p>
      <p>Integrating over all surface elements $S = \int dA$ gives the expected number of intersections $P$:</p>
      $$P = \frac{1}{2} \left(\frac{S}{V}\right) L = \frac{1}{2} S_v L$$
      <p>Dividing by line length $L$ and defining $P_L = P/L$:</p>
      $$P_L = \frac{1}{2} S_v \implies S_v = 2 P_L$$
      <p>This remarkable fundamental theorem of stereology is exact and completely independent of grain geometry, size distribution, or convexity!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation of $P_L$ and $S_v$</div>
      <p>True line length sampled on the specimen:</p>
      $$L_{\text{true}} = \frac{L_T}{M} = \frac{500 \text{ mm}}{400} = 1.25 \text{ mm}$$
      <p>Compute lineal intercept density $P_L$:</p>
      $$P_L = \frac{P}{L_{\text{true}}} = \frac{85}{1.25 \text{ mm}} = \mathbf{68.0 \text{ mm}^{-1} = 680 \text{ cm}^{-1}}$$
      <p>Apply the stereological theorem $S_v = 2 P_L$:</p>
      $$S_v = 2 \times 68.0 \text{ mm}^{-1} = \mathbf{136.0 \text{ mm}^{-1}}$$
      <p>Convert to $\text{cm}^2/\text{cm}^3$ ($1 \text{ mm}^{-1} = \frac{1 \text{ mm}^2}{1 \text{ mm}^3} = \frac{10^{-2} \text{ cm}^2}{10^{-3} \text{ cm}^3} = 10 \text{ cm}^{-1}$):</p>
      $$S_v = 136.0 \times 10 = \mathbf{1,360 \text{ cm}^2/\text{cm}^3}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Total Interfacial Area in Turbine Casing ($V = 1000 \text{ cm}^3$)</div>
      <p>Total volume of a $10 \text{ cm} \times 10 \text{ cm} \times 10 \text{ cm}$ block:</p>
      $$V_{\text{casing}} = (10 \text{ cm})^3 = 1,000 \text{ cm}^3 = 1.0 \times 10^{-3} \text{ m}^3$$
      $$S_{\text{total}} = S_v \times V_{\text{casing}} = (1,360 \text{ cm}^2/\text{cm}^3) \times (1,000 \text{ cm}^3) = 1,360,000 \text{ cm}^2$$
      <p>Convert square centimeters to square meters ($1 \text{ m}^2 = 10,000 \text{ cm}^2$):</p>
      $$S_{\text{total}} = \frac{1,360,000 \text{ cm}^2}{10,000 \text{ cm}^2/\text{m}^2} = \mathbf{136.0 \text{ m}^2}$$
      <p>Inside this $1 \text{ liter}$ metal block, the internal grain boundary area covers over <strong>$136 \text{ m}^2$</strong> (equivalent to the floor space of an entire residential apartment!).</p>
    </div>
    <div class="final-answer-box">
      <strong>Stereological Theorem:</strong> $$S_v = 2 P_L$$
      <strong>Lineal Intercept Density:</strong> $P_L = \mathbf{68.0 \text{ mm}^{-1}}$ &bull; <strong>Specific Boundary Area:</strong> $S_v = \mathbf{1,360 \text{ cm}^2/\text{cm}^3}$.<br>
      <strong>Total Area in $1 \text{ L}$ Casing:</strong> $S_{\text{total}} = \mathbf{136 \text{ m}^2}$.
    </div>""")

# P50: Comprehensive Defect Synthesis Problem
add(50, "Comprehensive Defect Synthesis: Multi-Defect Characterization of Quenched, Deformed Microalloyed Steel",
    "Volume Defects & Characterization", "volume_defects", "Advanced",
    r"""<p>A structural engineering component manufactured from microalloyed low-carbon steel is subjected to hot rolling, rapid water quenching, and subsequent cold deformation. A materials testing laboratory performs a comprehensive defect analysis across four distinct dimensional scales (0D, 1D, 2D, and 3D):</p>
    <div class="highlight-box">
      <strong>Experimental Laboratory Measurements:</strong>
      <ul>
        <li><strong>0D Defects:</strong> Resistometry determines a quenched-in vacancy concentration of $X_v = 2.40 \times 10^{-4}$. Chemical analysis reveals $0.15 \text{ wt}\%$ dissolved interstitial Carbon ($A_{\text{C}} = 12.01 \text{ g/mol}, A_{\text{Fe}} = 55.85 \text{ g/mol}$).</li>
        <li><strong>1D Defects:</strong> Transmission Electron Microscopy (TEM) reveals a dislocation density of $\rho_d = 5.0 \times 10^{14} \text{ m}^{-2}$ with Burgers vector $b = 0.248 \text{ nm}$ ($G = 80 \text{ GPa}$).</li>
        <li><strong>2D Defects:</strong> Metallography at $M = 100\times$ counts $N = 64 \text{ grains/in}^2$.</li>
        <li><strong>3D Defects:</strong> Archimedes densitometry measures an apparent bulk density of $\rho_{\text{bulk}} = 7.780 \text{ g/cm}^3$, whereas theoretical X-ray density is $\rho_{\text{ideal}} = 7.865 \text{ g/cm}^3$.</li>
      </ul>
    </div>
    <ol type="a">
      <li>Convert the carbon concentration from weight percent ($wt\%$) to atomic percent ($at\%$).</li>
      <li>Calculate the total stored elastic strain energy of the dislocations per cubic meter of steel ($E_{\text{stored}}$ in $\text{MJ/m}^3$), using $E \approx \frac{1}{2} G b^2 \rho_d$.</li>
      <li>Determine the ASTM grain size number $n$ and the mean grain diameter $\bar{d}$ in micrometers.</li>
      <li>Calculate the percentage volumetric porosity ($V_{\text{pore}} / V_{\text{total}} \times 100\%$) present as 3D casting/rolling voids.</li>
      <li>Synthesize these findings to explain how the interaction between these 0D, 1D, and 2D defects controls the yield strength of the steel.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Carbon Composition Conversion ($wt\% \to at\%$)</div>
      <p>Given $C_{\text{C}} = 0.15 \text{ wt}\%$ and $C_{\text{Fe}} = 99.85 \text{ wt}\%$:</p>
      $$n_{\text{C}} = \frac{0.15}{12.011} = 0.012489 \text{ mol}$$
      $$n_{\text{Fe}} = \frac{99.85}{55.845} = 1.78798 \text{ mol}$$
      $$n_{\text{total}} = 0.012489 + 1.78798 = 1.80047 \text{ mol}$$
      $$C_{\text{C}}' = \frac{0.012489}{1.80047} \times 100\% = \mathbf{0.6936 \text{ at}\% \approx 0.69 \text{ at}\%}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Stored Elastic Dislocation Energy</div>
      <p>Using $E_{\text{stored}} = \frac{1}{2} G b^2 \rho_d$:</p>
      $$b^2 = (0.248 \times 10^{-9} \text{ m})^2 = 6.1504 \times 10^{-20} \text{ m}^2$$
      $$E_{\text{line}} = \frac{1}{2} G b^2 = 0.5 \times (80 \times 10^9 \text{ Pa}) \times (6.1504 \times 10^{-20} \text{ m}^2) = 2.460 \times 10^{-9} \text{ J/m}$$
      <p>Volumetric stored energy density:</p>
      $$E_{\text{stored}} = E_{\text{line}} \times \rho_d = (2.460 \times 10^{-9} \text{ J/m}) \times (5.0 \times 10^{14} \text{ m}^{-2}) = \mathbf{1.230 \times 10^6 \text{ J/m}^3 = 1.23 \text{ MJ/m}^3}$$
      <p>This $1.23 \text{ MJ/m}^3$ of trapped elastic strain provides the thermodynamic driving force for subsequent recrystallization upon annealing.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): ASTM Grain Size Number and Diameter</div>
      <p>At $100\times$, $N = 64 \text{ grains/in}^2$:</p>
      $$2^{n-1} = 64 = 2^6 \implies n - 1 = 6 \implies \mathbf{n = 7}$$
      <p>Calculate mean grain diameter using $\bar{d} \approx \frac{286.6}{2^{(n-1)/2}} \mu\text{m}$:</p>
      $$\bar{d} = \frac{286.6}{2^{6/2}} = \frac{286.6}{2^3} = \frac{286.6}{8} = \mathbf{35.8 \mu\text{m}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Volumetric Porosity Calculation</div>
      $$\% \text{ Porosity} = \frac{\rho_{\text{ideal}} - \rho_{\text{bulk}}}{\rho_{\text{ideal}}} \times 100\% = \frac{7.865 - 7.780}{7.865} \times 100\% = \frac{0.085}{7.865} \times 100\% = \mathbf{1.08\%}$$
      <p>The steel contains $1.08\%$ volume fraction of 3D pores and microvoids.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (e): Multi-Defect Yield Strength Synthesis</div>
      <p>The yield strength of this steel is governed by the superposition of four distinct defect mechanisms:</p>
      <ol>
        <li><strong>Grain Boundaries (2D Defects):</strong> The fine grain size ($d = 35.8 \mu\text{m}$) provides Hall-Petch boundary strengthening ($\Delta\sigma_{\text{gb}} = k_y d^{-1/2}$) by acting as impenetrable barriers to dislocation pile-ups.</li>
        <li><strong>Dislocation Tangling (1D Defects):</strong> The high dislocation density ($\rho_d = 5 \times 10^{14} \text{ m}^{-2}$) contributes work hardening via Taylor forest dislocation hardening ($\Delta\sigma_{\text{disloc}} = M \alpha G b \sqrt{\rho_d} \approx 270 \text{ MPa}$).</li>
        <li><strong>Solute Interstitials & Vacancies (0D Defects):</strong> Quenched-in excess vacancies ($2.4 \times 10^{-4}$) accelerate carbon atom migration at modest temperatures, enabling carbon solutes ($0.69 \text{ at}\%$) to diffuse to dislocation cores, forming dense Cottrell atmospheres that pin dislocations and produce a high upper yield strength.</li>
        <li><strong>3D Porosity (Volume Defects):</strong> The $1.08\%$ porosity degrades fatigue endurance and tensile ductility without contributing to yield strength.</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>Carbon at%:</strong> $C_{\text{C}}' = \mathbf{0.69 \text{ at}\%}$ &bull; <strong>Stored Dislocation Energy:</strong> $E_{\text{stored}} = \mathbf{1.23 \text{ MJ/m}^3}$.<br>
      <strong>Grain Structure:</strong> ASTM $n = \mathbf{7}$, Mean Diameter $\bar{d} = \mathbf{35.8 \mu\text{m}}$ &bull; <strong>Porosity:</strong> $\mathbf{1.08\%}$ by volume.<br>
      <strong>Yield Strength Synthesis:</strong> Hall-Petch boundary strengthening + Taylor dislocation forest hardening + Cottrell interstitial solute pinning.
    </div>""")

# Save Chapter 4 dataset
with open("generator/ch4_data.py", "w", encoding="utf-8") as f:
    f.write("# ==============================================================================\n")
    f.write("# CHAPTER 4: IMPERFECTIONS IN SOLIDS\n")
    f.write("# 50 Curated Problems with Detailed Step-by-Step Solutions\n")
    f.write("# University of Tehran | Dept. of Mechanical Engineering | Prof. Sadeghi\n")
    f.write("# Prepared by: Sina Sharifi (TA)\n")
    f.write("# ==============================================================================\n\n")
    f.write("PROBLEMS = " + json.dumps(P, indent=2, ensure_ascii=False))

print(f"Chapter 4 complete! Successfully generated {len(P)} problems in generator/ch4_data.py.")
