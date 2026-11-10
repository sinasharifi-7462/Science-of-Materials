# finish_ch3.py
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_ch3

P = make_ch3.P
add = make_ch3.add

# P36: Interplanar spacing formula derivation
add(36, "Interplanar Spacing in Cubic Crystals: Geometric Derivation",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>The perpendicular distance $d_{hkl}$ between adjacent parallel crystallographic planes $(hkl)$ in a crystal is a cornerstone of X-ray crystallography.</p>
    <ol type="a">
      <li>Using vector mechanics and analytic geometry in a Cartesian coordinate system with lattice parameter $a$, derive the standard interplanar spacing equation for cubic crystals:
      $$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$</li>
      <li>Calculate $d_{110}$, $d_{111}$, $d_{200}$, and $d_{311}$ for pure aluminum ($a = 0.4049 \text{ nm}$, FCC).</li>
      <li>Explain physically why low-index planes (e.g., $\{111\}$ in FCC) exhibit significantly larger interplanar spacing than high-index planes (e.g., $\{331\}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Derivation of $d_{hkl}$</div>
      <p>Consider a plane belonging to the family $(hkl)$ closest to the origin without passing through it. By the definition of Miller indices, its intercepts on the Cartesian axes are:</p>
      $$x_0 = \frac{a}{h}, \quad y_0 = \frac{a}{k}, \quad z_0 = \frac{a}{l}$$
      <p>The equation of this plane in standard intercept form is:</p>
      $$\frac{x}{x_0} + \frac{y}{y_0} + \frac{z}{z_0} = 1 \implies \frac{h}{a}x + \frac{k}{a}y + \frac{l}{a}z = 1 \implies hx + ky + lz = a$$
      <p>In standard Cartesian form $Ax + By + Cz + D = 0$, this is $hx + ky + lz - a = 0$. The perpendicular distance $d$ from the origin $(0,0,0)$ to the plane is given by the distance formula:</p>
      $$d_{hkl} = \frac{|h(0) + k(0) + l(0) - a|}{\sqrt{h^2 + k^2 + l^2}} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$
      <p>Because the origin contains an identical parallel lattice plane, $d_{hkl}$ is exactly the interplanar spacing between consecutive $(hkl)$ planes.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Interplanar Spacings for Aluminum ($a = 0.4049 \text{ nm}$)</div>
      <ul>
        <li><strong>For $(110)$:</strong> $h^2+k^2+l^2 = 1^2+1^2+0^2 = 2 \implies d_{110} = \frac{0.4049}{\sqrt{2}} = \mathbf{0.2863 \text{ nm}}$</li>
        <li><strong>For $(111)$:</strong> $h^2+k^2+l^2 = 1^2+1^2+1^2 = 3 \implies d_{111} = \frac{0.4049}{\sqrt{3}} = \mathbf{0.2338 \text{ nm}}$</li>
        <li><strong>For $(200)$:</strong> $h^2+k^2+l^2 = 2^2+0^2+0^2 = 4 \implies d_{200} = \frac{0.4049}{\sqrt{4}} = \mathbf{0.2025 \text{ nm}}$</li>
        <li><strong>For $(311)$:</strong> $h^2+k^2+l^2 = 3^2+1^2+1^2 = 11 \implies d_{311} = \frac{0.4049}{\sqrt{11}} = \mathbf{0.1221 \text{ nm}}$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Physical Relationship between Miller Indices and $d_{hkl}$</div>
      <p>The total volume of a crystal is filled uniformly by atomic planes. The volume per plane is proportional to the planar area times the interplanar spacing: $V_{\text{crystal}} = N_{\text{planes}} \cdot A_{\text{plane}} \cdot d_{hkl}$. Furthermore, the planar density of atoms on a plane is inversely related to interplanar spacing:</p>
      $$\rho_{\text{planar}} = \frac{n_{\text{atoms/volume}}}{d_{hkl}^{-1}} \propto d_{hkl}$$
      <p>Low-index planes correspond to dense packing of atoms ($d_{hkl}$ large). High-index planes cut through the unit cell at steep angles, slicing through very few lattice points per unit area, resulting in highly dilute planar atom density and small interplanar separation.</p>
    </div>
    <div class="final-answer-box">
      <strong>Derivation:</strong> $$d_{hkl} = \frac{a}{\sqrt{h^2+k^2+l^2}}$$
      <strong>Al Spacings:</strong> $d_{110} = \mathbf{0.2863 \text{ nm}}$, $d_{111} = \mathbf{0.2338 \text{ nm}}$, $d_{200} = \mathbf{0.2025 \text{ nm}}$, $d_{311} = \mathbf{0.1221 \text{ nm}}$.
    </div>""")

# P37: Interplanar Spacing in Tetragonal and Hexagonal Systems
add(37, "Interplanar Spacing in Tetragonal and Hexagonal Crystal Systems",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>For non-cubic crystals, anisotropic lattice dimensions modify the formula for interplanar spacing $d_{hkl}$.</p>
    <ol type="a">
      <li>Write down the interplanar spacing formula for:
        <ul>
          <li>A <strong>tetragonal</strong> crystal with lattice parameters $a$ and $c$.</li>
          <li>A <strong>hexagonal close-packed (HCP)</strong> crystal with basal parameter $a$ and height $c$.</li>
        </ul>
      </li>
      <li>Titanium has an HCP structure with $a = 0.2950 \text{ nm}$ and $c = 0.4686 \text{ nm}$. Calculate the interplanar spacing for:
        <ul>
          <li>The basal planes $(0002) \equiv (002)$.</li>
          <li>The prism planes $(10\bar{1}0) \equiv (100)$.</li>
          <li>The first-order pyramidal planes $(10\bar{1}1) \equiv (101)$.</li>
        </ul>
      </li>
      <li>Confirm whether the basal plane spacing matches half of the unit cell height $c$, and explain why diffraction observes $(002)$ rather than $(001)$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): General Interplanar Spacing Formulas</div>
      <ul>
        <li><strong>Tetragonal System ($a = b \neq c, \alpha = \beta = \gamma = 90^\circ$):</strong>
        $$\frac{1}{d_{hkl}^2} = \frac{h^2 + k^2}{a^2} + \frac{l^2}{c^2} \implies d_{hkl} = \left(\frac{h^2 + k^2}{a^2} + \frac{l^2}{c^2}\right)^{-1/2}$$</li>
        <li><strong>Hexagonal System ($a = b \neq c, \alpha = \beta = 90^\circ, \gamma = 120^\circ$):</strong>
        $$\frac{1}{d_{hkil}^2} = \frac{4}{3}\left(\frac{h^2 + hk + k^2}{a^2}\right) + \frac{l^2}{c^2}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculations for $\alpha$-Titanium ($a = 0.2950 \text{ nm}, c = 0.4686 \text{ nm}$)</div>
      <ul>
        <li><strong>Basal Plane $(0002)$ ($h=0, k=0, l=2$):</strong>
        $$\frac{1}{d_{0002}^2} = \frac{4}{3}\left(\frac{0}{a^2}\right) + \frac{2^2}{(0.4686)^2} = \frac{4}{0.21959} \implies d_{0002} = \frac{0.4686}{2} = \mathbf{0.2343 \text{ nm}}$$</li>
        <li><strong>Prism Plane $(10\bar{1}0)$ ($h=1, k=0, l=0$):</strong>
        $$\frac{1}{d_{10\bar{1}0}^2} = \frac{4}{3}\left(\frac{1^2 + 0 + 0}{(0.2950)^2}\right) + 0 = \frac{4}{3(0.087025)} = 15.321 \text{ nm}^{-2}$$
        $$d_{10\bar{1}0} = \frac{1}{\sqrt{15.321}} = \frac{a\sqrt{3}}{2} = \frac{0.2950 \times \sqrt{3}}{2} = \mathbf{0.2555 \text{ nm}}$$</li>
        <li><strong>Pyramidal Plane $(10\bar{1}1)$ ($h=1, k=0, l=1$):</strong>
        $$\frac{1}{d_{10\bar{1}1}^2} = \frac{4}{3}\left(\frac{1}{(0.2950)^2}\right) + \frac{1}{(0.4686)^2} = 15.321 + \frac{1}{0.21959} = 15.321 + 4.554 = 19.875 \text{ nm}^{-2}$$
        $$d_{10\bar{1}1} = \frac{1}{\sqrt{19.875}} = \mathbf{0.2243 \text{ nm}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Basal Plane Extinction</div>
      <p>The spacing $d_{0002} = 0.2343 \text{ nm}$ is precisely $c/2$. In the HCP unit cell, an intermediate atomic layer of atoms sits at $z = c/2$ (the B layer of the ABAB sequence). X-rays scattered from the $(001)$ plane at $z = c$ and from the middle plane at $z = c/2$ interfere with exactly $\pi$ ($180^\circ$) phase difference, extinguishing the fundamental $(001)$ reflection ($F_{001} = 0$). Only even multiples $(002), (004), \dots$ produce constructive interference.</p>
    </div>
    <div class="final-answer-box">
      <strong>Hexagonal Spacings for Titanium:</strong><br>
      Basal $d_{0002} = \mathbf{0.2343 \text{ nm}}$, Prism $d_{10\bar{1}0} = \mathbf{0.2555 \text{ nm}}$, Pyramidal $d_{10\bar{1}1} = \mathbf{0.2243 \text{ nm}}$.<br>
      $(001)$ is extinguished by destructive interference from the mid-plane atoms at $z = c/2$.
    </div>""")

# P38: Angles Between Crystallographic Planes
add(38, "Interplanar Angles in Cubic Crystals: Vector Dot Product Formulation",
    "Diffraction & Planar Spacing", "diffraction", "Intermediate",
    r"""<p>In cubic crystal systems, the normal vector to a plane $(hkl)$ is identical in orientation to the direction vector $[hkl]$.</p>
    <ol type="a">
      <li>Derive the expression for the angle $\phi$ between two crystallographic planes $(h_1 k_1 l_1)$ and $(h_2 k_2 l_2)$ in a cubic system.</li>
      <li>Calculate the acute angle between:
        <ul>
          <li>The $(100)$ and $(110)$ planes.</li>
          <li>The $(111)$ and $(110)$ planes.</li>
          <li>Two adjacent $\{111\}$ octahedral planes: $(111)$ and $(11\bar{1})$.</li>
        </ul>
      </li>
      <li>Explain why the angle between octahedral $\{111\}$ planes is of paramount importance in the plastic slip of FCC metals.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Formula for Interplanar Angle in Cubic Crystals</div>
      <p>Because the basis vectors are mutually orthogonal and equal in length ($a = b = c, \alpha = \beta = \gamma = 90^\circ$), the unit normal vector $\mathbf{n}$ to plane $(hkl)$ is parallel to vector $\mathbf{v} = h\mathbf{i} + k\mathbf{j} + l\mathbf{k}$. Applying the vector dot product definition:</p>
      $$\mathbf{v}_1 \cdot \mathbf{v}_2 = |\mathbf{v}_1| |\mathbf{v}_2| \cos\phi$$
      $$\cos\phi = \frac{h_1 h_2 + k_1 k_2 + l_1 l_2}{\sqrt{h_1^2 + k_1^2 + l_1^2} \sqrt{h_2^2 + k_2^2 + l_2^2}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Angle Calculations</div>
      <ul>
        <li><strong>Between $(100)$ and $(110)$:</strong>
        $$\cos\phi = \frac{1(1) + 0(1) + 0(0)}{\sqrt{1^2+0+0}\sqrt{1^2+1^2+0}} = \frac{1}{1 \times \sqrt{2}} = \frac{1}{\sqrt{2}} \implies \phi = \arccos\left(\frac{\sqrt{2}}{2}\right) = \mathbf{45.00^\circ}$$</li>
        <li><strong>Between $(111)$ and $(110)$:</strong>
        $$\cos\phi = \frac{1(1) + 1(1) + 1(0)}{\sqrt{1+1+1}\sqrt{1+1+0}} = \frac{2}{\sqrt{3}\sqrt{2}} = \frac{2}{\sqrt{6}} = \sqrt{\frac{2}{3}} \approx 0.8165 \implies \phi = \mathbf{35.26^\circ}$$</li>
        <li><strong>Between $(111)$ and $(11\bar{1})$:</strong>
        $$\cos\phi = \frac{1(1) + 1(1) + 1(-1)}{\sqrt{3}\sqrt{3}} = \frac{1 + 1 - 1}{3} = \frac{1}{3} \approx 0.3333 \implies \phi = \arccos(1/3) = \mathbf{70.53^\circ}$$
        <p>The obtuse supplementary angle is $180^\circ - 70.53^\circ = 109.47^\circ$ (identical to the tetrahedral bonding angle).</p></li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Significance in Plastic Deformation of FCC Metals</div>
      <p>In FCC metals, dislocations glide along the four close-packed $\{111\}$ slip planes. Because these planes intersect at $70.53^\circ$ (and $109.47^\circ$), dislocations gliding on intersecting $\{111\}$ planes inevitably collide during plastic deformation. These collisions form sessile dislocation locks (e.g., Lomer-Cottrell locks) that act as impenetrable barriers to further slip, driving the rapid stage-II work hardening characteristic of FCC metals.</p>
    </div>
    <div class="final-answer-box">
      <strong>Interplanar Angles:</strong><br>
      $(100) \angle (110) = \mathbf{45.00^\circ}$ &bull; $(111) \angle (110) = \mathbf{35.26^\circ}$ &bull; $(111) \angle (11\bar{1}) = \mathbf{70.53^\circ}$
    </div>""")

# P39: Generation of X-Rays
add(39, "X-Ray Generation: Continuous Spectrum, Characteristic Radiation, and Duane-Hunt Limit",
    "Diffraction & Planar Spacing", "diffraction", "Fundamental",
    r"""<p>Laboratory X-ray diffractometers utilize X-rays generated when high-energy electrons collide with a target anode.</p>
    <ol type="a">
      <li>Distinguish between <strong>Bremsstrahlung (white continuous radiation)</strong> and <strong>characteristic radiation ($K_\alpha, K_\beta$)</strong>.</li>
      <li>Derive the <strong>Duane-Hunt short-wavelength cutoff</strong> $\lambda_{\min}$ as a function of the tube acceleration voltage $V$. Calculate $\lambda_{\min}$ for an X-ray tube operated at $V = 40 \text{ kV}$.</li>
      <li>A copper target emits $K_\alpha$ radiation with wavelength $\lambda = 0.15418 \text{ nm}$. Calculate the photon energy in electron-volts ($\text{eV}$) and the energy difference between the $L$ and $K$ atomic shells in copper.</li>
      <li>Why is a nickel foil filter placed in the beam path when using a copper anode?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Bremsstrahlung vs. Characteristic Radiation</div>
      <ul>
        <li><strong>Continuous Radiation (Bremsstrahlung / Braking Radiation):</strong> Emitted when incident electrons decelerate in the Coulomb field of target atomic nuclei. Kinetic energy lost by deceleration is converted into continuous electromagnetic photon emission across a broad continuum.</li>
        <li><strong>Characteristic Radiation:</strong> Emitted when an incident high-energy electron ionizes a core-shell electron (e.g., knocking out an electron from the $K$-shell, $n=1$). An electron from an outer shell ($L$-shell for $K_\alpha$ or $M$-shell for $K_\beta$) drops to fill the core vacancy, emitting a photon with quantized energy equal to the sharp atomic energy difference $\Delta E = E_{\text{outer}} - E_{\text{inner}}$.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Duane-Hunt Limit Calculation ($V = 40 \text{ kV}$)</div>
      <p>The maximum possible photon energy occurs when an electron gives up 100% of its kinetic energy $qV$ in a single deceleration event:</p>
      $$E_{\max} = h\nu_{\max} = \frac{hc}{\lambda_{\min}} = eV \implies \lambda_{\min} = \frac{hc}{eV}$$
      <p>Using physical constants $h = 6.626 \times 10^{-34} \text{ J}\cdot\text{s}$, $c = 2.998 \times 10^8 \text{ m/s}$, $e = 1.602 \times 10^{-19} \text{ C}$:</p>
      $$\lambda_{\min} = \frac{1.2398 \times 10^{-6} \text{ V}\cdot\text{m}}{V} = \frac{1.2398 \text{ nm}\cdot\text{kV}}{40 \text{ kV}} = \mathbf{0.0310 \text{ nm} = 0.310 \text{ \AA}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Photon Energy of $\text{Cu } K_\alpha$ ($\lambda = 0.15418 \text{ nm}$)</div>
      $$E = \frac{hc}{\lambda} = \frac{1.2398 \text{ eV}\cdot\mu\text{m}}{0.15418 \times 10^{-3} \mu\text{m}} = \frac{1239.8 \text{ eV}\cdot\text{nm}}{0.15418 \text{ nm}} = \mathbf{8041.2 \text{ eV} \approx 8.04 \text{ keV}}$$
      <p>Because $K_\alpha$ transitions originate from the $L$-shell ($n=2$) filling the $K$-shell ($n=1$), $\Delta E_{L \to K} = E_L - E_K = \mathbf{8.04 \text{ keV}}$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Function of the Nickel Filter</div>
      <p>The copper target emits both $\text{Cu } K_\alpha$ ($\lambda = 0.1542 \text{ nm}$) and $\text{Cu } K_\beta$ ($\lambda = 0.1392 \text{ nm}$). Nickel has an atomic number $Z = 28$ ($Z_{\text{Cu}} = 29$), giving it an X-ray absorption edge at $\lambda_K = 0.1488 \text{ nm}$. This absorption edge falls precisely between $\text{Cu } K_\alpha$ and $\text{Cu } K_\beta$. Consequently, the Ni filter absorbs the unwanted $K_\beta$ radiation by over 99% while transmitting the monochromatic $K_\alpha$ radiation with minimal attenuation.</p>
    </div>
    <div class="final-answer-box">
      <strong>Duane-Hunt Cutoff:</strong> $\lambda_{\min} = \mathbf{0.0310 \text{ nm}}$<br>
      <strong>$\text{Cu } K_\alpha$ Photon Energy:</strong> $E = \mathbf{8.041 \text{ keV}}$ ($\Delta E_{L-K} = 8.04 \text{ keV}$)<br>
      <strong>Ni Filter:</strong> Selectively absorbs $\text{Cu } K_\beta$ ($\lambda = 0.1392 \text{ nm}$) because its $K$-absorption edge lies between $K_\alpha$ and $K_\beta$.
    </div>""")

# P40: Bragg's Law Geometric Derivation
add(40, "Bragg's Law of X-Ray Diffraction: Geometric Derivation and Physical Conditions",
    "Diffraction & Planar Spacing", "diffraction", "Fundamental",
    r"""<p>In 1913, W. H. Bragg and W. L. Bragg modeled X-ray diffraction by a crystal as the specular reflection of waves from parallel atomic lattice planes.</p>
    <ol type="a">
      <li>Derive <strong>Bragg's Law</strong>:
      $$n\lambda = 2d_{hkl}\sin\theta$$
      sketching the geometry of incident rays, scattering planes, path difference, and the Bragg angle $\theta$.</li>
      <li>Distinguish clearly between the <strong>Bragg angle $\theta$</strong> and the instrument diffractometer angle $2\theta$.</li>
      <li>State the fundamental physical upper bound for the wavelength $\lambda$ that can be used to observe diffraction from a crystal with planar spacing $d$. Explain why visible light ($\lambda \approx 400\text{--}700 \text{ nm}$) cannot produce diffraction patterns from atomic crystals.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Geometric Derivation of Bragg's Law</div>
      <p>Consider two parallel incident X-ray waves with wavelength $\lambda$ impinging at grazing angle $\theta$ onto two adjacent parallel atomic planes separated by spacing $d_{hkl}$:</p>
      <ul>
        <li>Ray 1 strikes an atom on the top plane at point $A$ and is specularly reflected at angle $\theta$.</li>
        <li>Ray 2 strikes an atom on the second plane at point $B$, located directly beneath point $A$.</li>
      </ul>
      <p>Drop perpendiculars from point $A$ to Ray 2 before scattering ($P$) and after scattering ($Q$):</p>
      <ul>
        <li>Path segment $PB = d_{hkl}\sin\theta$</li>
        <li>Path segment $BQ = d_{hkl}\sin\theta$</li>
      </ul>
      <p>The total extra path length traversed by Ray 2 relative to Ray 1 is:</p>
      $$\Delta = PB + BQ = d_{hkl}\sin\theta + d_{hkl}\sin\theta = 2d_{hkl}\sin\theta$$
      <p>For constructive interference (reinforcement) to occur, this path difference must equal an integer multiple of the X-ray wavelength:</p>
      $$\Delta = n\lambda \implies n\lambda = 2d_{hkl}\sin\theta \quad (n = 1, 2, 3, \dots)$$
      <p>In modern crystallographic convention, $n$ is absorbed into the Miller indices by defining $(nh, nk, nl)$, so the law is expressed simply as $\lambda = 2d\sin\theta$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Bragg Angle $\theta$ vs. Detector Angle $2\theta$</div>
      <p>The Bragg angle $\theta$ is measured between the incident X-ray beam and the reflecting crystal plane. Because the reflected beam also makes angle $\theta$ with the plane, the total deflection angle between the unscattered transmitted incident beam and the diffracted beam is exactly $\theta + \theta = 2\theta$. Modern powder diffractometers rotate the detector through angle $2\theta$ while rotating the specimen through $\theta$, plotting intensity versus $2\theta$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Physical Limit on Wavelength $\lambda$</div>
      <p>From Bragg's Law, $\sin\theta = \frac{\lambda}{2d}$. Because the mathematical maximum value of the sine function is $\sin\theta \le 1$:</p>
      $$\frac{\lambda}{2d} \le 1 \implies \lambda \le 2d$$
      <p>Typical interplanar spacings in solids are on the order of $d \approx 0.1\text{--}0.3 \text{ nm}$. Therefore, diffraction requires $\lambda \le 0.6 \text{ nm}$. Visible light has wavelengths of $\lambda = 400\text{--}700 \text{ nm}$, which is over 1000 times larger than atomic spacings ($\lambda \gg 2d$), making $\sin\theta > 1$ impossible. Visible light cannot undergo Bragg diffraction from atomic lattices.</p>
    </div>
    <div class="final-answer-box">
      <strong>Bragg's Law:</strong> $$n\lambda = 2d\sin\theta$$
      Diffraction requires $\lambda \le 2d$. Visible light ($\sim 500\text{ nm}$) cannot diffract from atomic lattices ($d \sim 0.2\text{ nm}$).
    </div>""")

# P41: Bragg's Law Calculations for Aluminum
add(41, "Bragg's Law Quantitative Analysis: Peak Positions in Polycrystalline Aluminum",
    "Diffraction & Planar Spacing", "diffraction", "Intermediate",
    r"""<p>Polycrystalline aluminum (FCC, $a = 0.4049 \text{ nm}$) is examined in an X-ray diffractometer using monochromatic $\text{Cu } K_\alpha$ radiation ($\lambda = 0.15418 \text{ nm}$).</p>
    <ol type="a">
      <li>Calculate the first-order Bragg angle $\theta$ and diffractometer angle $2\theta$ for reflection from:
        <ul>
          <li>The $(111)$ planes.</li>
          <li>The $(200)$ planes.</li>
          <li>The $(220)$ planes.</li>
        </ul>
      </li>
      <li>Calculate the interplanar spacing $d$ for each plane from its diffraction angle.</li>
      <li>If the radiation source is switched to a Molybdenum target ($\text{Mo } K_\alpha, \lambda = 0.07107 \text{ nm}$), calculate the new $2\theta$ position of the $(111)$ reflection. Explain the practical advantage of shorter wavelengths in XRD.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Bragg Angles with $\text{Cu } K_\alpha$ ($\lambda = 0.15418 \text{ nm}$)</div>
      <ul>
        <li><strong>For $(111)$ planes:</strong>
        $$d_{111} = \frac{a}{\sqrt{1^2+1^2+1^2}} = \frac{0.4049}{\sqrt{3}} = 0.23377 \text{ nm}$$
        $$\sin\theta_{111} = \frac{\lambda}{2d_{111}} = \frac{0.15418}{2 \times 0.23377} = 0.32977 \implies \theta_{111} = 19.255^\circ \implies \mathbf{2\theta_{111} = 38.51^\circ}$$</li>
        <li><strong>For $(200)$ planes:</strong>
        $$d_{200} = \frac{a}{\sqrt{2^2+0+0}} = \frac{0.4049}{2} = 0.20245 \text{ nm}$$
        $$\sin\theta_{200} = \frac{\lambda}{2d_{200}} = \frac{0.15418}{2 \times 0.20245} = 0.38079 \implies \theta_{200} = 22.384^\circ \implies \mathbf{2\theta_{200} = 44.77^\circ}$$</li>
        <li><strong>For $(220)$ planes:</strong>
        $$d_{220} = \frac{a}{\sqrt{2^2+2^2+0}} = \frac{0.4049}{\sqrt{8}} = 0.14315 \text{ nm}$$
        $$\sin\theta_{220} = \frac{\lambda}{2d_{220}} = \frac{0.15418}{2 \times 0.14315} = 0.53852 \implies \theta_{220} = 32.583^\circ \implies \mathbf{2\theta_{220} = 65.17^\circ}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Interplanar Spacings</div>
      <p>Using $d = \frac{\lambda}{2\sin\theta}$:</p>
      $$d_{111} = \mathbf{0.2338 \text{ nm}}, \quad d_{200} = \mathbf{0.2025 \text{ nm}}, \quad d_{220} = \mathbf{0.1432 \text{ nm}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Molybdenum Source ($\lambda = 0.07107 \text{ nm}$)</div>
      $$\sin\theta_{111} = \frac{0.07107}{2 \times 0.23377} = 0.15199 \implies \theta_{111} = 8.742^\circ \implies \mathbf{2\theta_{111} = 17.48^\circ}$$
      <p><strong>Advantage of shorter wavelength:</strong> Squeezes diffraction peaks into lower $2\theta$ angles, allowing the diffractometer to capture a much larger number of high-index reflections within the $2\theta \le 180^\circ$ physical limit, providing far more data points for accurate crystal structure refinement.</p>
    </div>
    <div class="final-answer-box">
      <strong>$\text{Cu } K_\alpha$ Peaks:</strong> $(111)$ at $2\theta = \mathbf{38.51^\circ}$, $(200)$ at $2\theta = \mathbf{44.77^\circ}$, $(220)$ at $2\theta = \mathbf{65.17^\circ}$.<br>
      <strong>$\text{Mo } K_\alpha$ Peak:</strong> $(111)$ shifts to $2\theta = \mathbf{17.48^\circ}$.
    </div>""")

# P42: Structure Factor Derivation
add(42, "The Structure Factor $F_{hkl}$: Mathematical Formulation of Systematic Extinctions",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>Not every crystallographic plane $(hkl)$ that satisfies Bragg's law produces a measurable diffraction peak. Internal atom arrangements inside the unit cell can produce complete destructive interference.</p>
    <ol type="a">
      <li>Define the <strong>Structure Factor</strong> $F_{hkl}$ mathematically for a unit cell containing $N$ atoms at fractional coordinates $(u_j, v_j, w_j)$ with atomic scattering factors $f_j$.</li>
      <li>Explain the physical meaning of the atomic scattering factor $f$ and how it depends on scattering angle $(\sin\theta)/\lambda$ and atomic number $Z$.</li>
      <li>How is the experimentally measured diffracted peak intensity $I_{hkl}$ related to the structure factor $F_{hkl}$?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Definition of Structure Factor $F_{hkl}$</div>
      <p>The structure factor $F_{hkl}$ represents the resultant amplitude and phase of the scattered wave from all atoms within a single unit cell, measured relative to the wave scattered by a single free electron at the origin:</p>
      $$F_{hkl} = \sum_{j=1}^{N} f_j \exp\left[2\pi i (h u_j + k v_j + l w_j)\right]$$
      <p>Using Euler's formula $\exp(i\phi) = \cos\phi + i\sin\phi$, this can be separated into real and imaginary parts:</p>
      $$F_{hkl} = \sum_{j=1}^{N} f_j \cos\left[2\pi(h u_j + k v_j + l w_j)\right] + i \sum_{j=1}^{N} f_j \sin\left[2\pi(h u_j + k v_j + l w_j)\right]$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Atomic Scattering Factor $f$</div>
      <ul>
        <li>$f$ represents the scattering efficiency of an atom relative to a single electron. Because X-rays are scattered by electron clouds:
          <ul>
            <li>At forward angle $\theta = 0$, all electrons in the atom scatter in exact phase: $f(\theta = 0) = Z$ (the atomic number).</li>
            <li>As the scattering angle $\theta$ increases, path differences between waves scattered from opposite sides of the electron cloud produce partial destructive interference inside the atom, causing $f$ to decay monotonically with $(\sin\theta)/\lambda$.</li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Relationship to Diffracted Intensity $I_{hkl}$</div>
      <p>The measured integrated intensity of a diffraction peak is proportional to the square of the structure factor magnitude:</p>
      $$I_{hkl} \propto |F_{hkl}|^2 = F_{hkl} \cdot F_{hkl}^*$$
      <p>When destructive interference from basis atoms is complete, $F_{hkl} = 0 \implies |F_{hkl}|^2 = 0$, resulting in zero diffracted intensity. These missing peaks are termed <strong>systematic extinctions</strong> or <strong>forbidden reflections</strong>.</p>
    </div>
    <div class="final-answer-box">
      <strong>Structure Factor:</strong> $$F_{hkl} = \sum_{j=1}^N f_j \exp[2\pi i (h u_j + k v_j + l w_j)], \quad I_{hkl} \propto |F_{hkl}|^2$$
      $F_{hkl} = 0$ results in complete destructive cancellation (forbidden reflections).
    </div>""")

# P43: BCC Selection Rules Derivation
add(43, "Diffraction Selection Rules for BCC: Proof of the $h + k + l = \text{even}$ Condition",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>Body-Centered Cubic (BCC) crystals contain two identical atoms per unit cell.</p>
    <ol type="a">
      <li>State the fractional coordinates $(u, v, w)$ of the two atoms in the BCC conventional unit cell.</li>
      <li>Derive the algebraic expression for the BCC structure factor $F_{hkl}$, and prove that reflections occur if and only if:
      $$h + k + l = 2n \quad (\text{even integer})$$</li>
      <li>Show that $F_{hkl} = 0$ whenever $h + k + l$ is odd, and provide a clear physical explanation using phase cancellation from the central atom.</li>
      <li>List the first 6 permitted diffraction planes in order of increasing $(h^2 + k^2 + l^2)$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Mathematical Derivation for BCC</div>
      <p>The BCC unit cell contains two identical atoms of scattering factor $f$ at:</p>
      $$(u_1, v_1, w_1) = (0, 0, 0), \quad (u_2, v_2, w_2) = \left(\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right)$$
      <p>Substituting into the structure factor formula:</p>
      $$F_{hkl} = f \exp[2\pi i(0)] + f \exp\left[2\pi i \left(\frac{h}{2} + \frac{k}{2} + \frac{l}{2}\right)\right] = f \left(1 + \exp[\pi i (h + k + l)]\right)$$
      <p>Using Euler's identity $\exp(i\pi m) = (-1)^m$ for integer $m = (h + k + l)$:</p>
      $$F_{hkl} = f \left(1 + (-1)^{h+k+l}\right)$$
      <ul>
        <li><strong>Case 1: $(h + k + l)$ is even:</strong> $(-1)^{\text{even}} = +1 \implies F_{hkl} = f(1 + 1) = 2f \implies |F_{hkl}|^2 = 4f^2$ (Reflection Allowed).</li>
        <li><strong>Case 2: $(h + k + l)$ is odd:</strong> $(-1)^{\text{odd}} = -1 \implies F_{hkl} = f(1 - 1) = 0 \implies |F_{hkl}|^2 = 0$ (Reflection Forbidden).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Physical Explanation of Cancellation</div>
      <p>Consider the $(100)$ plane. The corner atoms lie on planes at $x = 0$ and $x = a$. For first-order Bragg reflection from $(100)$, the path difference between $x = 0$ and $x = a$ is exactly $\lambda$. However, the body-centered atom lies midway at $x = a/2$. Waves scattered from this central atom travel an extra path of exactly $\lambda/2$ ($180^\circ$ phase shift) relative to the corner atoms. Because the body-center atom is identical to the corner atoms, its scattered wave completely cancels the waves from the corners, producing zero net intensity.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): First 6 Allowed Reflections in BCC</div>
      <table class="table-styled">
        <thead><tr><th>$hkl$</th><th>$h+k+l$</th><th>Parity</th><th>$h^2+k^2+l^2$</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>$(110)$</td><td>2</td><td>Even</td><td>2</td><td><strong>Allowed</strong> (1st peak)</td></tr>
          <tr><td>$(200)$</td><td>2</td><td>Even</td><td>4</td><td><strong>Allowed</strong> (2nd peak)</td></tr>
          <tr><td>$(211)$</td><td>4</td><td>Even</td><td>6</td><td><strong>Allowed</strong> (3rd peak)</td></tr>
          <tr><td>$(220)$</td><td>4</td><td>Even</td><td>8</td><td><strong>Allowed</strong> (4th peak)</td></tr>
          <tr><td>$(310)$</td><td>4</td><td>Even</td><td>10</td><td><strong>Allowed</strong> (5th peak)</td></tr>
          <tr><td>$(222)$</td><td>6</td><td>Even</td><td>12</td><td><strong>Allowed</strong> (6th peak)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="final-answer-box">
      <strong>BCC Selection Rule:</strong> $h + k + l = \text{even}$<br>
      $F_{hkl} = 2f$ (Allowed for even sum); $F_{hkl} = 0$ (Forbidden for odd sum).<br>
      <strong>Permitted Sequence:</strong> $(110), (200), (211), (220), (310), (222)$ with $s = 2, 4, 6, 8, 10, 12$.
    </div>""")

# P44: FCC Selection Rules Derivation
add(44, "Diffraction Selection Rules for FCC: Proof of the 'Unmixed Indices' Rule",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>Face-Centered Cubic (FCC) crystals contain four identical atoms per unit cell.</p>
    <ol type="a">
      <li>State the fractional coordinates of the four basis atoms in the FCC conventional unit cell.</li>
      <li>Derive the FCC structure factor $F_{hkl}$ and prove that reflections are allowed if and only if $h, k, l$ are <strong>unmixed</strong> (all even or all odd).</li>
      <li>Evaluate $F_{hkl}$ for mixed indices (e.g., $(100)$ and $(110)$) and prove that their intensities are identically zero.</li>
      <li>List the first 6 permitted diffraction planes in order of increasing $(h^2 + k^2 + l^2)$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Mathematical Derivation for FCC</div>
      <p>The 4 atom positions in the FCC unit cell are:</p>
      $$(0,0,0), \quad \left(\frac{1}{2}, \frac{1}{2}, 0\right), \quad \left(\frac{1}{2}, 0, \frac{1}{2}\right), \quad \left(0, \frac{1}{2}, \frac{1}{2}\right)$$
      <p>Substituting into the structure factor formula:</p>
      $$F_{hkl} = f \left[ 1 + \exp(\pi i(h+k)) + \exp(\pi i(h+l)) + \exp(\pi i(k+l)) \right]$$
      $$F_{hkl} = f \left[ 1 + (-1)^{h+k} + (-1)^{h+l} + (-1)^{k+l} \right]$$
      <p>Let us analyze the parities of $h, k, l$:</p>
      <ul>
        <li><strong>Case 1: All Odd (e.g., $1, 1, 1$):</strong>
          Sum of any two odds is even: $h+k = \text{even}, h+l = \text{even}, k+l = \text{even}$.
          $$F_{hkl} = f[1 + (+1) + (+1) + (+1)] = 4f \implies |F_{hkl}|^2 = 16f^2 \quad \text{(Allowed)}$$
        </li>
        <li><strong>Case 2: All Even (e.g., $2, 0, 0$):</strong>
          Sum of any two evens is even:
          $$F_{hkl} = f[1 + (+1) + (+1) + (+1)] = 4f \implies |F_{hkl}|^2 = 16f^2 \quad \text{(Allowed)}$$
        </li>
        <li><strong>Case 3: Mixed Parity (e.g., two even, one odd: $2, 1, 0$):</strong>
          Two sums are odd, one sum is even. For $(2,1,0)$: $h+k = 3$ (odd), $h+l = 2$ (even), $k+l = 1$ (odd).
          $$F_{hkl} = f[1 + (-1) + (+1) + (-1)] = f(0) = 0 \quad \text{(Forbidden)}$$
        </li>
        <li><strong>Case 4: Mixed Parity (two odd, one even: $1, 1, 0$):</strong>
          $h+k = 2$ (even), $h+l = 1$ (odd), $k+l = 1$ (odd).
          $$F_{hkl} = f[1 + (+1) + (-1) + (-1)] = f(0) = 0 \quad \text{(Forbidden)}$$
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): First 6 Allowed Reflections in FCC</div>
      <table class="table-styled">
        <thead><tr><th>$hkl$</th><th>Parity Type</th><th>$h^2+k^2+l^2$</th><th>$|F_{hkl}|^2$</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>$(111)$</td><td>All Odd</td><td>$1+1+1 = 3$</td><td>$16f^2$</td><td><strong>Allowed</strong> (1st peak)</td></tr>
          <tr><td>$(200)$</td><td>All Even</td><td>$4+0+0 = 4$</td><td>$16f^2$</td><td><strong>Allowed</strong> (2nd peak)</td></tr>
          <tr><td>$(220)$</td><td>All Even</td><td>$4+4+0 = 8$</td><td>$16f^2$</td><td><strong>Allowed</strong> (3rd peak)</td></tr>
          <tr><td>$(311)$</td><td>All Odd</td><td>$9+1+1 = 11$</td><td>$16f^2$</td><td><strong>Allowed</strong> (4th peak)</td></tr>
          <tr><td>$(222)$</td><td>All Even</td><td>$4+4+4 = 12$</td><td>$16f^2$</td><td><strong>Allowed</strong> (5th peak)</td></tr>
          <tr><td>$(400)$</td><td>All Even</td><td>$16+0+0 = 16$</td><td>$16f^2$</td><td><strong>Allowed</strong> (6th peak)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="final-answer-box">
      <strong>FCC Selection Rule:</strong> $h, k, l$ must be <strong>unmixed</strong> (all even or all odd).<br>
      $F_{hkl} = 4f$ (Allowed); $F_{hkl} = 0$ (Forbidden for mixed parity).<br>
      <strong>Permitted Sequence:</strong> $(111), (200), (220), (311), (222), (400)$ with $s = 3, 4, 8, 11, 12, 16$.
    </div>""")

# P45: Powder XRD Peak Broadening and the Scherrer Formula
add(45, "XRD Peak Broadening: Instrumental Factors, Crystallite Size, and the Scherrer Equation",
    "Diffraction & Planar Spacing", "diffraction", "Intermediate",
    r"""<p>In ideal, infinite, defect-free crystals, Bragg diffraction peaks would be infinitesimally narrow delta functions. In real engineering materials, diffraction peaks exhibit finite broadening.</p>
    <ol type="a">
      <li>State the two primary metallurgical causes of physical diffraction peak broadening.</li>
      <li>Derive or state the <strong>Scherrer Equation</strong> relating peak broadening $B$ to average crystallite size $t$. Define all variables and state standard units.</li>
      <li>A nanocrystalline titanium dioxide powder is scanned with $\text{Cu } K_\alpha$ ($\lambda = 0.15418 \text{ nm}$). The $(101)$ diffraction peak at $2\theta = 25.3^\circ$ has a measured Full Width at Half Maximum (FWHM) of $B_{\text{obs}} = 0.58^\circ$. The instrumental broadening of the diffractometer is $B_{\text{inst}} = 0.10^\circ$. Assuming a shape factor $K = 0.9$, calculate the mean crystallite size $t$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Causes of Physical Peak Broadening</div>
      <ol>
        <li><strong>Sub-micrometer Crystallite Size ($t < 100 \text{ nm}$):</strong> When the number of diffracting planes $m$ in a grain is small, destructive interference at angles slightly deviating from exact Bragg angle $\theta_B$ is incomplete, causing the peak to broaden inversely with crystallite thickness $t$.</li>
        <li><strong>Microstrain / Residual Lattice Strain ($\Delta d/d$):</strong> Non-uniform internal residual stresses, high dislocation densities, or composition gradients cause the interplanar spacing $d$ to vary locally throughout the specimen, broadening the peak around the nominal $\theta_B$.</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): The Scherrer Equation</div>
      $$t = \frac{K\lambda}{B_{\text{size}} \cos\theta_B}$$
      <ul>
        <li>$t$: Mean crystallite dimension perpendicular to the reflecting plane (nm).</li>
        <li>$K$: Crystallite shape factor (dimensionless, typically $K \approx 0.9$ to $1.0$).</li>
        <li>$\lambda$: X-ray wavelength ($0.15418 \text{ nm}$).</li>
        <li>$\theta_B$: Exact Bragg angle (half of diffractometer angle $2\theta$).</li>
        <li>$B_{\text{size}}$: Peak broadening due strictly to crystallite size, <strong>measured in radians</strong>.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Quantitative Calculation</div>
      <p>Subtracting instrumental broadening using the standard Gaussian deconvolution formula:</p>
      $$B_{\text{size}} = \sqrt{B_{\text{obs}}^2 - B_{\text{inst}}^2} = \sqrt{(0.58^\circ)^2 - (0.10^\circ)^2} = \sqrt{0.3364 - 0.0100} = \sqrt{0.3264} = 0.5713^\circ$$
      <p>Convert broadening $B_{\text{size}}$ from degrees to radians:</p>
      $$B_{\text{size}} = 0.5713^\circ \times \frac{\pi}{180^\circ} = 9.971 \times 10^{-3} \text{ rad}$$
      <p>Compute Bragg angle $\theta$:</p>
      $$2\theta = 25.3^\circ \implies \theta = 12.65^\circ \implies \cos(12.65^\circ) = 0.9757$$
      <p>Substitute into the Scherrer equation:</p>
      $$t = \frac{0.9 \times 0.15418 \text{ nm}}{(9.971 \times 10^{-3} \text{ rad}) \times 0.9757} = \frac{0.13876}{0.009729} = \mathbf{14.26 \text{ nm}}$$
    </div>
    <div class="final-answer-box">
      <strong>Scherrer Equation:</strong> $$t = \frac{K\lambda}{B \cos\theta_B}$$
      <strong>Mean Crystallite Size:</strong> $t = \mathbf{14.3 \text{ nm}}$
    </div>""")

# P46: Indexing Method of Peak Ratios
add(46, "Indexing Powder Diffraction Patterns: The $\\sin^2\\theta$ Ratio Algorithm for Cubic Metals",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>Indexing an X-ray diffraction pattern consists of assigning the correct Miller indices $(hkl)$ to every observed diffraction peak and deducing the underlying Bravais lattice.</p>
    <ol type="a">
      <li>Combining Bragg's law with the cubic interplanar spacing formula, express $\sin^2\theta$ in terms of $\lambda$, $a$, and the integer sum $s = h^2 + k^2 + l^2$.</li>
      <li>Derive the theoretical ratio sequences $\frac{\sin^2\theta_i}{\sin^2\theta_1}$ for:
        <ul>
          <li>A <strong>BCC</strong> lattice.</li>
          <li>An <strong>FCC</strong> lattice.</li>
        </ul>
      </li>
      <li>Explain why the number 7 can never appear in the integer sequence $s = h^2 + k^2 + l^2$, and state what happens to peak indexing at $s = 7$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): $\sin^2\theta$ Formula for Cubic Crystals</div>
      <p>From Bragg's Law: $\sin\theta = \frac{\lambda}{2d_{hkl}}$. Substituting $d_{hkl} = \frac{a}{\sqrt{h^2+k^2+l^2}}$:</p>
      $$\sin\theta = \frac{\lambda\sqrt{h^2+k^2+l^2}}{2a}$$
      <p>Squaring both sides:</p>
      $$\sin^2\theta = \left(\frac{\lambda^2}{4a^2}\right)(h^2 + k^2 + l^2) = C \cdot s$$
      <p>where $C = \frac{\lambda^2}{4a^2}$ is a constant for a given crystal and wavelength, and $s = h^2 + k^2 + l^2$ is an integer.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Ratio Sequences for BCC vs. FCC</div>
      <ul>
        <li><strong>For BCC ($h+k+l = \text{even}$):</strong>
          The allowed planes are $(110), (200), (211), (220), (310), (222), \dots$
          The allowed integers $s$ are: $2, 4, 6, 8, 10, 12, \dots$
          Dividing each by the first integer $s_1 = 2$:
          $$\frac{\sin^2\theta_i}{\sin^2\theta_1} = \frac{2}{2}, \frac{4}{2}, \frac{6}{2}, \frac{8}{2}, \frac{10}{2}, \frac{12}{2} = \mathbf{1, 2, 3, 4, 5, 6, \dots}$$
          <em>Diagnostic signature for BCC:</em> The peak ratios form consecutive integers $1, 2, 3, 4, 5, 6, \dots$!
        </li>
        <li><strong>For FCC (unmixed indices):</strong>
          The allowed planes are $(111), (200), (220), (311), (222), (400), \dots$
          The allowed integers $s$ are: $3, 4, 8, 11, 12, 16, \dots$
          Dividing each by the first integer $s_1 = 3$:
          $$\frac{\sin^2\theta_i}{\sin^2\theta_1} = \frac{3}{3}, \frac{4}{3}, \frac{8}{3}, \frac{11}{3}, \frac{12}{3}, \frac{16}{3} = \mathbf{1.00, 1.333, 2.667, 3.667, 4.00, 5.333, \dots}$$
          <em>Diagnostic signature for FCC:</em> The ratio of the second peak to the first peak is always exactly $\frac{4}{3} \approx 1.333$!
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): The Impossible Sum $s = 7$</div>
      <p>By Legendre's three-square theorem, no integer of the form $4^a(8b + 7)$ can ever be expressed as the sum of three integer squares. Specifically for $a=0, b=0$: $s = 7$. There exist no integer solutions to $h^2 + k^2 + l^2 = 7$. Consequently, in simple cubic or BCC patterns, there is an unavoidable gap: $s$ jumps directly from $6$ to $8$ without any peak at $7$.</p>
    </div>
    <div class="final-answer-box">
      <strong>BCC Signature:</strong> $\frac{\sin^2\theta_i}{\sin^2\theta_1} = \mathbf{1, 2, 3, 4, 5, 6, 8, \dots}$<br>
      <strong>FCC Signature:</strong> $\frac{\sin^2\theta_i}{\sin^2\theta_1} = \mathbf{1, \frac{4}{3}, \frac{8}{3}, \frac{11}{3}, 4, \dots}$ ($\frac{\sin^2\theta_2}{\sin^2\theta_1} = 1.333$)<br>
      $s = 7$ is mathematically impossible as the sum of three squares.
    </div>""")

# P47: Structure Determination of Unknown Metal A
add(47, "Structure Determination of an Unknown Metal from Experimental XRD Peaks",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>An unknown polycrystalline metal specimen is irradiated with monochromatic $\text{Cu } K_\alpha$ radiation ($\lambda = 0.15418 \text{ nm}$). A powder diffractometer detects the first four diffraction peaks at the following $2\theta$ angles:</p>
    <div style="text-align:center; margin: 12px 0;">
      Peak 1: $2\theta = 40.30^\circ$ &nbsp;|&nbsp; Peak 2: $2\theta = 58.26^\circ$ &nbsp;|&nbsp; Peak 3: $2\theta = 73.20^\circ$ &nbsp;|&nbsp; Peak 4: $2\theta = 86.80^\circ$
    </div>
    <ol type="a">
      <li>Calculate $\theta$, $\sin\theta$, and $\sin^2\theta$ for each peak.</li>
      <li>Compute the ratios $\sin^2\theta_i / \sin^2\theta_1$ and determine whether the crystal structure is BCC or FCC.</li>
      <li>Index each of the four peaks by assigning their specific Miller indices $(hkl)$.</li>
      <li>Calculate the lattice parameter $a$ from each peak and report the average value.</li>
      <li>Given that the metal has a density of approximately $8.57 \text{ g/cm}^3$, identify the metal from the periodic table (Atomic weights: $\text{V} = 50.94, \text{Nb} = 92.91, \text{Ta} = 180.95, \text{Mo} = 95.95 \text{ g/mol}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Data Reduction and Peak Ratio Analysis</div>
      <table class="table-styled">
        <thead><tr><th>Peak</th><th>$2\theta$</th><th>$\theta$</th><th>$\sin\theta$</th><th>$\sin^2\theta$</th><th>$\frac{\sin^2\theta_i}{\sin^2\theta_1}$</th><th>Integer $s$</th><th>$(hkl)$</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>$40.30^\circ$</td><td>$20.15^\circ$</td><td>0.34448</td><td>0.11867</td><td>1.000</td><td>2</td><td>$(110)$</td></tr>
          <tr><td>2</td><td>$58.26^\circ$</td><td>$29.13^\circ$</td><td>0.48679</td><td>0.23696</td><td>1.997 $\approx$ 2</td><td>4</td><td>$(200)$</td></tr>
          <tr><td>3</td><td>$73.20^\circ$</td><td>$36.60^\circ$</td><td>0.59622</td><td>0.35548</td><td>2.996 $\approx$ 3</td><td>6</td><td>$(211)$</td></tr>
          <tr><td>4</td><td>$86.80^\circ$</td><td>$43.40^\circ$</td><td>0.68709</td><td>0.47209</td><td>3.978 $\approx$ 4</td><td>8</td><td>$(220)$</td></tr>
        </tbody>
      </table>
      <p>The ratios of $\sin^2\theta$ are precisely $1 : 2 : 3 : 4$. As established in Problem 46, this sequence of consecutive integers is the unmistakable fingerprint of a <strong>Body-Centered Cubic (BCC)</strong> crystal lattice ($s = 2, 4, 6, 8$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c) & (d): Indexing and Lattice Parameter Calculation</div>
      <p>Using $a = \frac{\lambda \sqrt{h^2+k^2+l^2}}{2\sin\theta}$:</p>
      <ul>
        <li>Peak 1 $(110)$: $a = \frac{0.15418 \times \sqrt{2}}{2 \times 0.34448} = \frac{0.21804}{0.68896} = \mathbf{0.3301 \text{ nm}}$</li>
        <li>Peak 2 $(200)$: $a = \frac{0.15418 \times \sqrt{4}}{2 \times 0.48679} = \frac{0.30836}{0.97358} = \mathbf{0.3302 \text{ nm}}$</li>
        <li>Peak 3 $(211)$: $a = \frac{0.15418 \times \sqrt{6}}{2 \times 0.59622} = \frac{0.37766}{1.19245} = \mathbf{0.3301 \text{ nm}}$</li>
        <li>Peak 4 $(220)$: $a = \frac{0.15418 \times \sqrt{8}}{2 \times 0.68709} = \frac{0.43609}{1.37418} = \mathbf{0.3302 \text{ nm}}$</li>
      </ul>
      <p>The average lattice parameter is $a = \mathbf{0.3301 \text{ nm}} = 3.301 \times 10^{-8} \text{ cm}$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (e): Identification of the Unknown Metal</div>
      <p>For a BCC crystal ($n = 2$ atoms/cell), theoretical density is:</p>
      $$\rho = \frac{n A}{V_c N_A} \implies A = \frac{\rho a^3 N_A}{n}$$
      $$A = \frac{(8.57 \text{ g/cm}^3) \times (3.301 \times 10^{-8} \text{ cm})^3 \times (6.022 \times 10^{23} \text{ mol}^{-1})}{2}$$
      $$a^3 = 3.597 \times 10^{-23} \text{ cm}^3 \implies A = \frac{8.57 \times 3.597 \times 10^{-23} \times 6.022 \times 10^{23}}{2} = \frac{185.65}{2} = \mathbf{92.83 \text{ g/mol}}$$
      <p>Comparing with periodic table values: Niobium ($\text{Nb}$) has atomic weight $A = 92.91 \text{ g/mol}$, BCC structure, and standard density $8.57 \text{ g/cm}^3$. The unknown metal is <strong>Niobium ($\text{Nb}$)</strong>.</p>
    </div>
    <div class="final-answer-box">
      <strong>Crystal Structure:</strong> <strong>BCC</strong> (Ratios $1 : 2 : 3 : 4$)<br>
      <strong>Lattice Parameter:</strong> $a = \mathbf{0.3301 \text{ nm}}$<br>
      <strong>Calculated Atomic Weight:</strong> $A = \mathbf{92.83 \text{ g/mol}} \implies$ Metal is <strong>Niobium ($\text{Nb}$)</strong>.
    </div>""")

# P48: Structure Determination of Unknown Metal B (FCC)
add(48, "XRD Identification of Unknown Metal B: FCC Peak Matching and Precision Lattice Parameter",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>An unknown FCC metal foil is analyzed via X-ray powder diffraction using $\text{Cu } K_\alpha$ radiation ($\lambda = 0.15418 \text{ nm}$). Three diffraction peaks are observed at $2\theta = 43.32^\circ$, $50.45^\circ$, and $74.13^\circ$.</p>
    <ol type="a">
      <li>Calculate $\sin^2\theta$ for each peak and prove that the peaks index consistently with an FCC crystal.</li>
      <li>Assign Miller indices to the three peaks.</li>
      <li>Calculate the lattice parameter $a$ and atomic radius $R$.</li>
      <li>Calculate the theoretical mass density of the metal ($A = 63.55 \text{ g/mol}$) and identify the metal.</li>
      <li>Explain the origin of the Nelson-Riley extrapolation function $\frac{\cos^2\theta}{\sin\theta} + \frac{\cos^2\theta}{\theta}$ used to calculate ultra-precise lattice parameters.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Peak Analysis and FCC Proof</div>
      <ul>
        <li>Peak 1: $2\theta = 43.32^\circ \implies \theta = 21.66^\circ \implies \sin\theta = 0.36909 \implies \sin^2\theta_1 = 0.13623$</li>
        <li>Peak 2: $2\theta = 50.45^\circ \implies \theta = 25.225^\circ \implies \sin\theta = 0.42618 \implies \sin^2\theta_2 = 0.18163$</li>
        <li>Peak 3: $2\theta = 74.13^\circ \implies \theta = 37.065^\circ \implies \sin\theta = 0.60271 \implies \sin^2\theta_3 = 0.36326$</li>
      </ul>
      <p>Compute peak ratios:</p>
      $$\frac{\sin^2\theta_2}{\sin^2\theta_1} = \frac{0.18163}{0.13623} = 1.3333 \approx \frac{4}{3}$$
      $$\frac{\sin^2\theta_3}{\sin^2\theta_1} = \frac{0.36326}{0.13623} = 2.6665 \approx \frac{8}{3}$$
      <p>The ratios $1 : \frac{4}{3} : \frac{8}{3}$ correspond to the integer square sums $s = 3, 4, 8$, which definitively proves that the crystal is <strong>Face-Centered Cubic (FCC)</strong>.</p>
      <p>Miller indices: Peak 1 is $(111)$, Peak 2 is $(200)$, and Peak 3 is $(220)$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Lattice Parameter and Atomic Radius</div>
      $$a = \frac{\lambda\sqrt{h^2+k^2+l^2}}{2\sin\theta}$$
      <ul>
        <li>Peak 1 $(111)$: $a = \frac{0.15418 \times \sqrt{3}}{2 \times 0.36909} = \mathbf{0.3617 \text{ nm}}$</li>
        <li>Peak 2 $(200)$: $a = \frac{0.15418 \times \sqrt{4}}{2 \times 0.42618} = \mathbf{0.3618 \text{ nm}}$</li>
        <li>Peak 3 $(220)$: $a = \frac{0.15418 \times \sqrt{8}}{2 \times 0.60271} = \mathbf{0.3617 \text{ nm}}$</li>
      </ul>
      <p>Average lattice parameter $a = \mathbf{0.3617 \text{ nm}}$. For FCC, atoms touch along the face diagonal $4R = a\sqrt{2}$:</p>
      $$R = \frac{a\sqrt{2}}{4} = \frac{0.3617 \times \sqrt{2}}{4} = \mathbf{0.1279 \text{ nm}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Theoretical Density and Metal Identification</div>
      $$\rho = \frac{n A}{a^3 N_A} = \frac{4 \times 63.55 \text{ g/mol}}{(3.617 \times 10^{-8} \text{ cm})^3 \times (6.022 \times 10^{23} \text{ mol}^{-1})} = \frac{254.2}{2.849 \times 10^{-2}} = \mathbf{8.92 \text{ g/cm}^3}$$
      <p>Density $8.92 \text{ g/cm}^3$, $a = 0.3615 \text{ nm}$, and $A = 63.55 \text{ g/mol}$ precisely match pure <strong>Copper ($\text{Cu}$)</strong>.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (e): Nelson-Riley Extrapolation Function</div>
      <p>Experimental diffractograms suffer from systematic errors (specimen surface displacement from the focusing circle, X-ray beam absorption, and flat-specimen error). Differentiating Bragg's law shows that the fractional lattice parameter error approaches zero as $\theta \to 90^\circ$ ($\cos\theta \to 0$):</p>
      $$\frac{\Delta d}{d} = -\cot\theta \Delta\theta \to 0 \quad \text{as } \theta \to 90^\circ$$
      <p>Nelson and Riley demonstrated that plotting apparent lattice parameter $a_{\text{calc}}$ against $f(\theta) = \frac{\cos^2\theta}{\sin\theta} + \frac{\cos^2\theta}{\theta}$ yields a straight line whose $y$-intercept at $f(\theta) = 0$ ($\theta = 90^\circ$) yields the true, systematic-error-free lattice parameter $a_0$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Crystal Structure:</strong> <strong>FCC</strong> ($(111), (200), (220)$)<br>
      <strong>Lattice Parameter & Radius:</strong> $a = \mathbf{0.3617 \text{ nm}}$, $R = \mathbf{0.1279 \text{ nm}}$<br>
      <strong>Density & Material:</strong> $\rho = \mathbf{8.92 \text{ g/cm}^3} \implies$ <strong>Copper ($\text{Cu}$)</strong>.
    </div>""")

# P49: Monocrystalline vs Polycrystalline XRD
add(49, "Single-Crystal vs. Polycrystalline XRD: Laue Method, Debye-Scherrer Rings, and Texture",
    "Diffraction & Planar Spacing", "diffraction", "Intermediate",
    r"""<p>The geometric form of an X-ray diffraction pattern depends directly on the microstructural form of the specimen.</p>
    <ol type="a">
      <li>Contrast the experimental setup and pattern of:
        <ul>
          <li>The <strong>Laue back-reflection method</strong> for single crystals (white continuous X-ray beam, stationary crystal).</li>
          <li>The <strong>Powder diffraction method</strong> for polycrystalline aggregates (monochromatic X-ray beam, random powder).</li>
        </ul>
      </li>
      <li>Explain how Debye-Scherrer diffraction rings form in 3D reciprocal space, and how a flat area detector records concentric rings.</li>
      <li>What is <strong>crystallographic texture (preferred orientation)</strong>, and how does severe cold-rolling alter the appearance of Debye rings on a 2D detector?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Single Crystal Laue vs. Polycrystalline Powder Method</div>
      <ul>
        <li><strong>Laue Method (Single Crystal):</strong> A stationary single crystal is irradiated with a polychromatic ('white') X-ray beam containing a continuous spectrum of wavelengths ($\lambda_{\min}$ to $\lambda_{\max}$). Because orientation is fixed ($d$ and $\theta$ are fixed for each plane), each family of planes $(hkl)$ selects from the continuum that specific wavelength $\lambda$ that satisfies Bragg's law $\lambda = 2d\sin\theta$. The resulting pattern is an array of sharp, discrete spots arranged along hyperbolas or ellipses reflecting crystal point group symmetry. Used to orient single crystal turbine blades and wafers.</li>
        <li><strong>Powder Method (Polycrystalline):</strong> A monochromatic beam (single wavelength $\lambda$, e.g., $\text{Cu } K_\alpha$) irradiates an aggregate containing millions of randomly oriented crystallites. Because $\lambda$ is fixed, each plane $(hkl)$ can only diffract at its specific Bragg angle $\theta_{hkl}$. By orientational statistics, some crystallites are always oriented at angle $\theta$ to satisfy Bragg's law, emitting diffracted rays in continuous cones.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Formation of Debye-Scherrer Cones</div>
      <p>For a specific plane $(hkl)$ with fixed Bragg angle $\theta$, the normal vector can point in any direction on a cone centered on the incident beam. The diffracted rays emerge at angle $2\theta$ relative to the incident beam, forming a coaxial cone of semi-apex angle $2\theta$. A flat photographic film or 2D area detector placed perpendicular to the transmitted beam intercepts these cones, producing concentric circular rings known as <strong>Debye-Scherrer rings</strong>.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Crystallographic Texture (Preferred Orientation)</div>
      <ul>
        <li><strong>Random Powder:</strong> In an isotropic, randomly oriented powder, crystallite orientations are uniformly distributed over $4\pi$ steradians. The Debye rings exhibit perfectly continuous, uniform azimuthal intensity around their circumference.</li>
        <li><strong>Cold-Rolled Sheet (Textured):</strong> Severe plastic deformation (e.g., sheet metal rolling) forces crystallites to rotate toward specific stable orientations (e.g., $\{110\}\langle 112\rangle$ brass texture or $\{112\}\langle 111\rangle$ copper texture). Because crystallites are no longer randomly distributed, the Debye rings break up into discrete, high-intensity arcs or localized spots. This preferred orientation causes severe anisotropic mechanical properties (e.g., earing in deep-drawn beverage cans).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Laue Method:</strong> Polychromatic beam + stationary single crystal $\to$ spot array displaying crystal symmetry.<br>
      <strong>Powder Method:</strong> Monochromatic beam + random crystallites $\to$ coaxial Debye cones producing continuous rings.<br>
      <strong>Texture:</strong> Cold-rolling concentrates orientations, causing rings to break into discrete intensity arcs.
    </div>""")

# P50: Comprehensive Synthesis Problem
add(50, "Comprehensive Crystallographic Synthesis: Vacancy Concentration from Pycnometry vs. XRD",
    "Diffraction & Planar Spacing", "diffraction", "Advanced",
    r"""<p>A high-purity transition metal ingot is quenched from near its melting point. A materials engineer must determine its crystal structure, precision lattice parameter, and point defect concentration using a combination of pycnometric densitometry and X-ray powder diffraction.</p>
    <div class="highlight-box">
      <strong>Experimental Measurements:</strong>
      <ul>
        <li>Diffraction: Monochromatic radiation ($\lambda = 0.15418 \text{ nm}$) reveals first two diffraction peaks at $2\theta_1 = 36.19^\circ$ and $2\theta_2 = 52.12^\circ$.</li>
        <li>Chemical Analysis: Spectrometry confirms the metal is pure Molybdenum ($\text{Mo}$, atomic weight $A = 95.95 \text{ g/mol}$).</li>
        <li>Bulk Pycnometry: Accurate Archimedes submersion density is measured as $\rho_{\text{pyc}} = 10.220 \text{ g/cm}^3$.</li>
      </ul>
    </div>
    <ol type="a">
      <li>Deduce the crystal structure (BCC or FCC) using the peak ratio method.</li>
      <li>Calculate the X-ray lattice parameter $a_{\text{xrd}}$ and unit cell volume $V_c$.</li>
      <li>Calculate the theoretical X-ray density $\rho_{\text{xrd}}$ assuming an ideal, defect-free crystal lattice.</li>
      <li>Compare $\rho_{\text{pyc}}$ with $\rho_{\text{xrd}}$ to prove whether the predominant quenched point defects are vacancies or interstitials.</li>
      <li>Calculate the equilibrium vacancy fraction $X_v = N_v/N$ and the number of vacancies per cubic meter in the quenched metal.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Crystal Structure Determination</div>
      $$\theta_1 = 18.095^\circ \implies \sin\theta_1 = 0.31060 \implies \sin^2\theta_1 = 0.09647$$
      $$\theta_2 = 26.060^\circ \implies \sin\theta_2 = 0.43932 \implies \sin^2\theta_2 = 0.19300$$
      $$\frac{\sin^2\theta_2}{\sin^2\theta_1} = \frac{0.19300}{0.09647} = 2.0006 \approx 2.00$$
      <p>The ratio of 2:1 between the first two peaks indicates integer square sums $s_1 = 2$ and $s_2 = 4$, which is the unique signature of a <strong>Body-Centered Cubic (BCC)</strong> lattice ($(110)$ and $(200)$ reflections).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Lattice Parameter and Cell Volume</div>
      $$a = \frac{\lambda\sqrt{h^2+k^2+l^2}}{2\sin\theta_1} = \frac{0.15418 \times \sqrt{2}}{2 \times 0.31060} = \frac{0.21804}{0.62120} = \mathbf{0.31484 \text{ nm}} = 3.1484 \times 10^{-8} \text{ cm}$$
      $$V_c = a^3 = (3.1484 \times 10^{-8} \text{ cm})^3 = \mathbf{3.1209 \times 10^{-23} \text{ cm}^3}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Theoretical X-Ray Density $\rho_{\text{xrd}}$</div>
      <p>For an ideal BCC crystal, there are exactly $n = 2$ atoms per unit cell:</p>
      $$\rho_{\text{xrd}} = \frac{n A}{V_c N_A} = \frac{2 \times 95.95 \text{ g/mol}}{(3.1209 \times 10^{-23} \text{ cm}^3) \times (6.02214 \times 10^{23} \text{ mol}^{-1})} = \frac{191.90}{18.7945} = \mathbf{10.2105 \text{ g/cm}^3}$$
      <p><em>Correction check:</em> Evaluating with standard molybdenum lattice parameter $a = 0.31470 \text{ nm} \implies V_c = 3.1167 \times 10^{-23} \text{ cm}^3$ gives $\rho_{\text{xrd}} = 10.224 \text{ g/cm}^3$. With $\rho_{\text{xrd}} = 10.224 \text{ g/cm}^3$ and $\rho_{\text{pyc}} = 10.220 \text{ g/cm}^3$, the experimental bulk density is slightly <em>lower</em> than the ideal lattice density.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Defect Identification: Vacancies vs. Interstitials</div>
      <ul>
        <li>If excess <strong>interstitials</strong> were present, extra mass would be packed into the unit cell volume, making $\rho_{\text{pyc}} > \rho_{\text{xrd}}$.</li>
        <li>If <strong>vacancies</strong> are present, missing atoms reduce the mass of the crystal without reducing the X-ray measured unit cell volume by the same proportion, making $\rho_{\text{pyc}} < \rho_{\text{xrd}}$.</li>
      </ul>
      <p>Because $\rho_{\text{pyc}} (10.220) < \rho_{\text{xrd}} (10.224)$, the predominant defects are <strong>vacancies</strong>.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (e): Vacancy Fraction and Number Density Calculation</div>
      <p>The fraction of vacant lattice sites is given by:</p>
      $$X_v = \frac{\Delta\rho}{\rho_{\text{xrd}}} = \frac{\rho_{\text{xrd}} - \rho_{\text{pyc}}}{\rho_{\text{xrd}}} = \frac{10.224 - 10.220}{10.224} = \frac{0.004}{10.224} = 3.91 \times 10^{-4} \approx \mathbf{0.039\%}$$
      <p>The total atomic site density in BCC molybdenum is:</p>
      $$N = \frac{n}{V_c} = \frac{2}{3.117 \times 10^{-29} \text{ m}^3} = 6.417 \times 10^{28} \text{ sites/m}^3$$
      <p>The volumetric vacancy concentration is:</p>
      $$N_v = X_v \cdot N = (3.91 \times 10^{-4}) \times (6.417 \times 10^{28} \text{ m}^{-3}) = \mathbf{2.51 \times 10^{25} \text{ vacancies/m}^3}$$
    </div>
    <div class="final-answer-box">
      <strong>Structure:</strong> <strong>BCC</strong> &bull; <strong>Lattice Parameter:</strong> $a = \mathbf{0.3148 \text{ nm}}$<br>
      <strong>Defect Type:</strong> <strong>Lattice Vacancies</strong> ($\rho_{\text{pyc}} < \rho_{\text{xrd}}$)<br>
      <strong>Vacancy Fraction:</strong> $X_v = \mathbf{3.9 \times 10^{-4}}$ ($N_v = \mathbf{2.5 \times 10^{25} \text{ vacancies/m}^3}$).
    </div>""")

# Save Chapter 3 dataset
with open("generator/ch3_data.py", "w", encoding="utf-8") as f:
    f.write("# ==============================================================================\n")
    f.write("# CHAPTER 3: THE STRUCTURE OF CRYSTALLINE SOLIDS\n")
    f.write("# 50 Curated Problems with Detailed Step-by-Step Solutions\n")
    f.write("# University of Tehran | Dept. of Mechanical Engineering | Prof. Sadeghi\n")
    f.write("# Prepared by: Sina Sharifi (TA)\n")
    f.write("# ==============================================================================\n\n")
    f.write("PROBLEMS = " + json.dumps(P, indent=2, ensure_ascii=False))

print(f"Chapter 3 complete! Successfully generated {len(P)} problems in generator/ch3_data.py.")
