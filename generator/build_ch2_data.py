# ==============================================================================
# BUILDER FOR CHAPTER 2: 50 PROBLEMS
# Course: Science of Materials | University of Tehran | Prof. Sadeghi
# Prepared by TA Sina Sharifi
# Topic: Atomic Structure & Interatomic Bonding
# ==============================================================================

import json

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

# --- P1 to P15: Fundamental Atomic Physics & Electronic Configuration ---
add(1, "Bohr Atomic Model vs. Wave-Mechanical Model",
    "Atomic Physics", "quantum", "Fundamental",
    r"""<p>The transition from classical quantum theory to modern quantum mechanics fundamentally redefined our understanding of atomic structure.</p>
    <ol type="a">
      <li>State the core postulates of the <strong>Bohr model</strong> of the hydrogen atom, including the angular momentum quantization condition: $L = n \hbar = \frac{n h}{2\pi}$.</li>
      <li>Explain the two revolutionary principles that invalidated Bohr's concept of fixed planar planetary electron orbits: <strong>de Broglie's wave-particle duality</strong> ($\lambda = h/p$) and <strong>Heisenberg's uncertainty principle</strong> ($\Delta x \cdot \Delta p \ge \hbar/2$).</li>
      <li>Define an <strong>atomic orbital</strong> and the <strong>wavefunction probability density</strong> ($|\psi(r, \theta, \phi)|^2$) in the Schrödinger wave-mechanical model.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Bohr Model Postulates</div>
      <ul>
        <li>Electrons revolve around the positively charged nucleus in discrete, stable, circular orbits without radiating electromagnetic energy.</li>
        <li>The orbital angular momentum $L$ of the electron is quantized in integer multiples of reduced Planck's constant:
        $$L = m_e v r = n \hbar = \frac{n h}{2\pi} \quad (n = 1, 2, 3, \dots)$$</li>
        <li>Radiation is absorbed or emitted only when an electron transitions between two discrete stationary energy levels: $\Delta E = E_2 - E_1 = h \nu = \frac{h c}{\lambda}$.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Transition to Wave Mechanics</div>
      <ul>
        <li><strong>de Broglie Hypothesis ($\lambda = h/p$):</strong> Moving subatomic particles possess wave-like properties. An electron in an atom forms a stationary standing wave around the nucleus, requiring an integer number of wavelengths: $2\pi r = n \lambda$.</li>
        <li><strong>Heisenberg Uncertainty Principle ($\Delta x \cdot \Delta p \ge \hbar/2$):</strong> It is physically impossible to simultaneously determine both the exact position $x$ and exact momentum $p$ of an electron. The Bohr concept of a well-defined circular trajectory with simultaneous known radius $r$ and velocity $v$ violates this fundamental quantum limit.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Atomic Orbitals & Probability Density</div>
      <p>In wave mechanics, an electron's state is described by a spatial wavefunction $\psi(r, \theta, \phi)$ satisfying the time-independent Schrödinger equation:</p>
      $$\hat{H} \psi = E \psi$$
      <p>An <strong>atomic orbital</strong> is not a physical track, but a mathematical mathematical spatial distribution. The quantity <strong>$P(r) = |\psi(r, \theta, \phi)|^2 dV$</strong> represents the probability density of finding the electron within a differential volume $dV$ surrounding position $(r, \theta, \phi)$. Orbitals are visualized as 90% or 95% electron probability boundary isosurfaces.</p>
    </div>
    <div class="final-answer-box">
      <strong>Core Conclusion:</strong> The Bohr model assumed deterministic planetary orbits with quantized angular momentum ($m_e v r = n\hbar$). The Schrödinger model replaces orbits with 3D probability density clouds ($|\psi|^2$) governed by wave-particle duality and the uncertainty principle.
    </div>""")

add(2, "The Four Quantum Numbers: Physical Significance and Rules",
    "Atomic Physics", "quantum", "Fundamental",
    r"""<p>The wave-mechanical state of every bound atomic electron is uniquely specified by four quantum numbers: $n$, $l$, $m_l$, and $m_s$.</p>
    <ol type="a">
      <li>State the allowed numerical values and physical significance of each of the four quantum numbers.</li>
      <li>Identify the orbital spectroscopic notation ($s, p, d, f$) corresponding to $l = 0, 1, 2, 3$, and state the maximum electron capacity of each subshell ($2(2l + 1)$).</li>
      <li>Determine the total number of allowed electronic quantum states in the $n = 3$ principal shell ($M$-shell).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): The Four Quantum Numbers</div>
      <ul>
        <li><strong>Principal Quantum Number ($n$):</strong> $n = 1, 2, 3, 4, \dots$ Governs the primary energy level of the electron and the radial size (extent) of the electron cloud. Energy increases with $n$.</li>
        <li><strong>Azimuthal / Orbital Angular Momentum Quantum Number ($l$):</strong> $l = 0, 1, 2, \dots, (n - 1)$. Dictates the orbital angular momentum ($L = \sqrt{l(l+1)}\hbar$) and the 3D geometric shape of the electron orbital.</li>
        <li><strong>Magnetic Quantum Number ($m_l$):</strong> $m_l = -l, -l+1, \dots, 0, \dots, +l$ ($2l + 1$ values). Governs the spatial orientation of the orbital in 3D space relative to an external magnetic field.</li>
        <li><strong>Spin Magnetic Quantum Number ($m_s$):</strong> $m_s = +\frac{1}{2}, -\frac{1}{2}$. Dictates the intrinsic spin angular momentum orientation of the electron (spin-up or spin-down).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Spectroscopic Subshells & Capacities</div>
      <ul>
        <li>$l = 0$ &rarr; <strong>$s$ subshell</strong>: 1 orbital ($m_l = 0$), spherical symmetry; capacity = <strong>2 electrons</strong>.</li>
        <li>$l = 1$ &rarr; <strong>$p$ subshell</strong>: 3 orbitals ($m_l = -1, 0, +1$, dumbbell $p_x, p_y, p_z$); capacity = <strong>6 electrons</strong>.</li>
        <li>$l = 2$ &rarr; <strong>$d$ subshell</strong>: 5 orbitals ($m_l = -2, -1, 0, 1, 2$, cloverleaf); capacity = <strong>10 electrons</strong>.</li>
        <li>$l = 3$ &rarr; <strong>$f$ subshell</strong>: 7 orbitals ($m_l = -3, -2, -1, 0, 1, 2, 3$); capacity = <strong>14 electrons</strong>.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Total Allowed States in $n = 3$ ($M$-shell)</div>
      <p>For $n = 3$, allowed $l$ values are $l = 0, 1, 2$:</p>
      <ul>
        <li>$l = 0$ ($3s$): $2(2(0) + 1) = 2$ states</li>
        <li>$l = 1$ ($3p$): $2(2(1) + 1) = 6$ states</li>
        <li>$l = 2$ ($3d$): $2(2(2) + 1) = 10$ states</li>
      </ul>
      <p>Total capacity = $2 + 6 + 10 = \mathbf{18 \text{ electrons}}$. Alternatively, using the general shell capacity theorem: $2 n^2 = 2(3^2) = 2(9) = \mathbf{18}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Final Result:</strong> The $n = 3$ principal shell contains $n^2 = 9$ spatial orbitals accommodating exactly $2 n^2 = \mathbf{18 \text{ electrons}}$ ($3s^2 3p^6 3d^{10}$).
    </div>""")

add(3, "Electronic Configurations of Transition Metals and Ions: Fe, Cu, and Cr",
    "Atomic Physics", "quantum", "Fundamental",
    r"""<p>The chemical, mechanical, and magnetic properties of transition metals are governed by their valence $d$-electron subshells.</p>
    <ol type="a">
      <li>State the <strong>Aufbau Principle</strong>, the <strong>Pauli Exclusion Principle</strong>, and <strong>Hund's Rule of Maximum Multiplicity</strong>.</li>
      <li>Write the complete ground-state electron configuration for neutral Iron (Fe, $Z = 26$), the ferrous ion ($\text{Fe}^{2+}$), and the ferric ion ($\text{Fe}^{3+}$). Which electrons are removed first during ionization?</li>
      <li>Explain the anomalous ground-state configurations of Chromium (Cr, $Z = 24$: $[Ar] 3d^5 4s^1$) and Copper (Cu, $Z = 29$: $[Ar] 3d^{10} 4s^1$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Electronic Governing Rules</div>
      <ul>
        <li><strong>Aufbau Principle:</strong> Electrons sequentially fill the lowest available subshell energy levels first according to the Madelung $(n + l)$ rule.</li>
        <li><strong>Pauli Exclusion Principle:</strong> No two electrons in an atom can have identical sets of all four quantum numbers ($n, l, m_l, m_s$). Each orbital can hold at most two electrons, and they must have antiparallel spins.</li>
        <li><strong>Hund's Rule:</strong> For degenerate orbitals (orbitals with identical energy, such as the five $3d$ orbitals), electrons occupy separate orbitals with parallel spins before pairing up, minimizing electron-electron Coulombic repulsion.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Electron Configurations for Fe, $\text{Fe}^{2+}$, and $\text{Fe}^{3+}$</div>
      <ul>
        <li><strong>Neutral Iron (Fe, $Z = 26$):</strong>
        $$1s^2 2s^2 2p^6 3s^2 3p^6 3d^6 4s^2 \quad \text{or} \quad [\text{Ar}] 3d^6 4s^2$$</li>
        <li><strong>Ferrous Ion ($\text{Fe}^{2+}$):</strong> When transition metals ionize, electrons in the outermost principal shell ($4s$) are removed <em>first</em> because their radial probability distribution extends further from the nucleus than the $3d$ electrons:
        $$[\text{Ar}] 3d^6$$</li>
        <li><strong>Ferric Ion ($\text{Fe}^{3+}$):</strong> Removing a third electron removes one $3d$ electron, producing a half-filled, spherically symmetric $3d^5$ subshell:
        $$[\text{Ar}] 3d^5$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Anomalous Configurations of Cr and Cu</div>
      <ul>
        <li><strong>Chromium (Cr, $Z = 24$):</strong> Expected: $[\text{Ar}] 3d^4 4s^2$. Actual: <strong>$[\text{Ar}] 3d^5 4s^1$</strong>. Promoting one $4s$ electron into the $3d$ subshell creates a half-filled $3d^5$ subshell where all five orbitals have parallel spins. This maximizes the quantum mechanical exchange stabilization energy and minimizes Coulombic pairing energy.</li>
        <li><strong>Copper (Cu, $Z = 29$):</strong> Expected: $[\text{Ar}] 3d^9 4s^2$. Actual: <strong>$[\text{Ar}] 3d^{10} 4s^1$</strong>. Promoting one $4s$ electron into the $3d$ subshell creates a completely full, spherically symmetric $3d^{10}$ subshell, which provides exceptional exchange energy stabilization.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Key Takeaways:</strong><br>
      Fe: $[\text{Ar}] 3d^6 4s^2$ &bull; $\text{Fe}^{2+}$: $[\text{Ar}] 3d^6$ ($4s$ electrons lost first!) &bull; $\text{Fe}^{3+}$: $[\text{Ar}] 3d^5$<br>
      Cr and Cu promote one $4s$ electron to achieve half-filled ($3d^5$) and fully-filled ($3d^{10}$) exchange-stabilized configurations.
    </div>""")

add(4, "Periodic Trends: Electronegativity, Ionization Energy, and Atomic Radii",
    "Atomic Physics", "periodic", "Fundamental",
    r"""<p>Macroscopic material behavior and chemical bonding are dictated by systematic periodic trends in the periodic table.</p>
    <ol type="a">
      <li>Define <strong>Electronegativity</strong> ($\chi$, Pauling scale), <strong>First Ionization Energy</strong> ($I_1$), and <strong>Electron Affinity</strong> ($EA$).</li>
      <li>Describe and explain the directional trends (across a period from left to right, and down a group from top to bottom) for:
        <ul>
          <li>Effective Nuclear Charge ($Z_{eff} = Z - S$)</li>
          <li>Atomic Radius ($R_{at}$)</li>
          <li>First Ionization Energy ($I_1$)</li>
          <li>Electronegativity ($\chi$)</li>
        </ul>
      </li>
      <li>Explain why the ionic radius of a cation ($\text{Na}^+ = 0.102 \text{ nm}$) is substantially smaller than its parent neutral atom ($\text{Na} = 0.186 \text{ nm}$), whereas the ionic radius of an anion ($\text{Cl}^- = 0.181 \text{ nm}$) is larger than its parent neutral atom ($\text{Cl} = 0.099 \text{ nm}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Fundamental Definitions</div>
      <ul>
        <li><strong>Electronegativity ($\chi$):</strong> The relative ability of an atom in a chemical bond to attract shared electron density toward itself (dimensionless Pauling scale from 0.7 for Fr to 4.0 for F).</li>
        <li><strong>First Ionization Energy ($I_1$):</strong> The minimum energy required to remove the most loosely bound valence electron from an isolated gaseous atom in its ground state: $\text{M}(g) \to \text{M}^+(g) + e^-$.</li>
        <li><strong>Electron Affinity ($EA$):</strong> The energy released when an electron is added to a neutral gaseous atom to form a univalent negative ion: $\text{X}(g) + e^- \to \text{X}^-(g)$.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Periodic Trends Across Rows and Down Groups</div>
      <ul>
        <li><strong>Across a Period (Left to Right):</strong> Protons are added to the nucleus while electrons enter the same principal shell, providing incomplete screening. Consequently, <strong>effective nuclear charge surges ($Z_{eff} \uparrow$)</strong>. The stronger nuclear pull draws the electron cloud inward, causing <strong>atomic radius to decrease ($R_{at} \downarrow$)</strong>, while <strong>ionization energy ($I_1 \uparrow$)</strong> and <strong>electronegativity ($\chi \uparrow$)</strong> increase.</li>
        <li><strong>Down a Group (Top to Bottom):</strong> Principal quantum number increases ($n \uparrow$), adding complete core electron shells. The valence electrons occupy larger orbitals further from the nucleus, shielded by inner shells. Consequently, <strong>atomic radius increases ($R_{at} \uparrow$)</strong>, while <strong>ionization energy ($I_1 \downarrow$)</strong> and <strong>electronegativity ($\chi \downarrow$)</strong> decrease.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Cation Contraction vs. Anion Expansion</div>
      <ul>
        <li><strong>Cation Contraction ($\text{Na} \to \text{Na}^+$):</strong> Neutral Sodium ($[\text{Ne}] 3s^1$) loses its single $3s$ valence electron. The entire $n = 3$ shell is vacated, leaving 11 protons pulling on only 10 electrons ($[\text{Ne}]$ core). The higher proton-to-electron ratio ($11/10$) increases effective nuclear charge per electron, shrinking the radius from 0.186 nm to 0.102 nm (<strong>45% reduction</strong>).</li>
        <li><strong>Anion Expansion ($\text{Cl} \to \text{Cl}^-$):</strong> Neutral Chlorine ($[\text{Ne}] 3s^2 3p^5$) gains an electron to form chloride ($[\text{Ne}] 3s^2 3p^6$). Adding an electron with no change in nuclear charge ($Z = 17$) increases electron-electron Coulombic repulsion in the valence shell, expanding the electron cloud from 0.099 nm to 0.181 nm (<strong>83% expansion</strong>).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Summary:</strong> Across a period: $Z_{eff} \uparrow$, $R_{at} \downarrow$, $\chi \uparrow$, $I_1 \uparrow$. Down a group: $R_{at} \uparrow$, $\chi \downarrow$, $I_1 \downarrow$. Cations are smaller than parent atoms; anions are larger.
    </div>""")

# --- P5 to P20: Ionic Bonding & Interatomic Potential Well ---
add(5, "Coulomb's Law and Interatomic Forces in an Ionic Pair",
    "Ionic Bonding", "ionic", "Fundamental",
    r"""<p>Consider an isolated pair of monovalent sodium ($\text{Na}^+$) and chloride ($\text{Cl}^-$) ions separated by a center-to-center distance $r$.</p>
    <ol type="a">
      <li>State <strong>Coulomb's Law</strong> for the attractive force $F_A(r)$ between two ions of valence $Z_1 = +1$ and $Z_2 = -1$. Define all constants and calculate the attractive constant $A$ in SI units ($\text{N}\cdot\text{m}^2$). Use $e = 1.602 \times 10^{-19} \text{ C}$ and $\varepsilon_0 = 8.854 \times 10^{-12} \text{ F/m}$.</li>
      <li>Integrate $F_A(r)$ from infinity to separation $r$ to derive the attractive potential energy $E_A(r) = -A/r$.</li>
      <li>At the equilibrium separation $r_0 = 0.28 \text{ nm}$ ($2.80 \times 10^{-10} \text{ m}$), calculate the magnitude of the attractive force $F_A(r_0)$ in nano-Newtons ($\text{nN}$) and the attractive potential energy $E_A(r_0)$ in both Joules and electron-volts ($\text{eV}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Coulomb's Attractive Force & Constant $A$</div>
      <p>Coulomb's electrostatic attractive force is:</p>
      $$F_A(r) = -\frac{1}{4\pi\varepsilon_0} \frac{|Z_1 Z_2| e^2}{r^2} = -\frac{A}{r^2}$$
      <p>where $A = \frac{|Z_1 Z_2| e^2}{4\pi\varepsilon_0}$. For $Z_1 = +1, Z_2 = -1$:</p>
      $$A = \frac{(1.602 \times 10^{-19} \text{ C})^2}{4 \pi (8.854 \times 10^{-12} \text{ F/m})} = \frac{2.5664 \times 10^{-38}}{1.1127 \times 10^{-10}} = \mathbf{2.3065 \times 10^{-28} \text{ N}\cdot\text{m}^2 \text{ (or J}\cdot\text{m)}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Derivation of Attractive Potential Energy $E_A(r)$</div>
      <p>Taking reference energy as zero at infinite separation ($E_A(\infty) = 0$):</p>
      $$E_A(r) = \int_\infty^r F_A(r') dr' = \int_\infty^r \left( -\frac{A}{r'^2} \right) dr' = \left[ \frac{A}{r'} \right]_\infty^r = -\frac{A}{r}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Numerical Calculations at $r_0 = 0.28 \text{ nm}$</div>
      <p>Given: $r_0 = 0.28 \times 10^{-9} \text{ m}$:</p>
      <ul>
        <li><strong>Attractive Force:</strong>
        $$F_A(r_0) = \frac{A}{r_0^2} = \frac{2.3065 \times 10^{-28} \text{ N}\cdot\text{m}^2}{(2.80 \times 10^{-10} \text{ m})^2} = \frac{2.3065 \times 10^{-28}}{7.84 \times 10^{-20}} = 2.942 \times 10^{-9} \text{ N} = \mathbf{2.94 \text{ nN}}$$</li>
        <li><strong>Attractive Potential Energy:</strong>
        $$E_A(r_0) = -\frac{A}{r_0} = -\frac{2.3065 \times 10^{-28} \text{ J}\cdot\text{m}}{2.80 \times 10^{-10} \text{ m}} = \mathbf{-8.238 \times 10^{-19} \text{ J}}$$
        In electron-volts ($1 \text{ eV} = 1.602 \times 10^{-19} \text{ J}$):
        $$E_A(r_0) = \frac{-8.238 \times 10^{-19} \text{ J}}{1.602 \times 10^{-19} \text{ J/eV}} = \mathbf{-5.14 \text{ eV}}$$</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Final Results:</strong><br>
      Attractive Constant: $A = \mathbf{2.31 \times 10^{-28} \text{ N}\cdot\text{m}^2}$<br>
      At $r_0 = 0.28 \text{ nm}$:<br>
      $F_A(r_0) = \mathbf{2.94 \text{ nN}}$ &bull; $E_A(r_0) = \mathbf{-8.24 \times 10^{-19} \text{ J}} = \mathbf{-5.14 \text{ eV}}$
    </div>""")

add(6, "Net Potential Energy Function: Derivation of Equilibrium Separation $r_0$ and Bonding Energy $E_0$",
    "Ionic Bonding", "ionic", "Intermediate",
    r"""<p>The net interatomic potential energy $E_N(r)$ between two bonded ions is given by the general Born-Mie power-law relation:</p>
    $$E_N(r) = E_A(r) + E_R(r) = -\frac{A}{r^m} + \frac{B}{r^n} \quad (n > m)$$
    <ol type="a">
      <li>Apply the physical equilibrium condition to derive an algebraic expression for the equilibrium interatomic separation $r_0$ in terms of $A, B, m,$ and $n$.</li>
      <li>Derive the algebraic expression for the net bonding energy $E_0 = -E_N(r_0)$ in terms of $A, r_0, m,$ and $n$. Show that for simple Coulombic attraction ($m = 1$), $E_0 = \frac{A}{r_0} \left( 1 - \frac{1}{n} \right)$.</li>
      <li>For a pair of monovalent ions with $A = 2.31 \times 10^{-28} \text{ J}\cdot\text{m}$ ($m = 1$), Born repulsive exponent $n = 9$, and equilibrium distance $r_0 = 0.28 \text{ nm}$, calculate:
        <ul>
          <li>The repulsive constant $B$ (in $\text{J}\cdot\text{m}^9$)</li>
          <li>The net dissociation bonding energy $E_0$ (in eV)</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Equilibrium Condition and $r_0$ Derivation</div>
      <p>At equilibrium separation $r_0$, the net force is zero, meaning potential energy is at a minimum:</p>
      $$F_N(r_0) = -\left. \frac{dE_N}{dr} \right|_{r_0} = 0$$
      $$\frac{dE_N}{dr} = \frac{m A}{r^{m+1}} - \frac{n B}{r^{n+1}} = 0 \implies \frac{m A}{r_0^{m+1}} = \frac{n B}{r_0^{n+1}}$$
      <p>Multiplying both sides by $r_0^{n+1}$:</p>
      $$r_0^{n-m} = \frac{n B}{m A} \implies r_0 = \left( \frac{n B}{m A} \right)^{\frac{1}{n - m}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Net Bonding Energy $E_0$ Expression</div>
      <p>From the equilibrium force balance, express the repulsive constant as $B = \frac{m A}{n} r_0^{n-m}$. Substitute $B$ into the net energy equation evaluated at $r_0$:</p>
      $$E_N(r_0) = -\frac{A}{r_0^m} + \frac{B}{r_0^n} = -\frac{A}{r_0^m} + \frac{\frac{m A}{n} r_0^{n-m}}{r_0^n} = -\frac{A}{r_0^m} + \frac{m A}{n r_0^m} = -\frac{A}{r_0^m} \left( 1 - \frac{m}{n} \right)$$
      <p>The bonding energy $E_0$ is defined as the depth of the well ($E_0 = -E_N(r_0)$):</p>
      $$E_0 = \frac{A}{r_0^m} \left( 1 - \frac{m}{n} \right)$$
      <p>For Coulombic attraction ($m = 1$):</p>
      $$E_0 = \frac{A}{r_0} \left( 1 - \frac{1}{n} \right)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Numerical Calculations ($m=1, n=9, r_0 = 0.28 \text{ nm}$)</div>
      <ul>
        <li><strong>Repulsive Constant $B$:</strong>
        $$B = \frac{m A}{n} r_0^{n-1} = \frac{1 \times (2.31 \times 10^{-28})}{9} (2.80 \times 10^{-10})^8$$
        $$(2.80 \times 10^{-10})^8 = 3.771 \times 10^{-77} \text{ m}^8$$
        $$B = \left( 2.567 \times 10^{-29} \right) \times (3.771 \times 10^{-77}) = \mathbf{9.68 \times 10^{-106} \text{ J}\cdot\text{m}^9}$$</li>
        <li><strong>Net Bonding Energy $E_0$:</strong>
        $$E_0 = \frac{A}{r_0} \left( 1 - \frac{1}{9} \right) = \frac{2.31 \times 10^{-28} \text{ J}\cdot\text{m}}{2.80 \times 10^{-10} \text{ m}} \times \left( \frac{8}{9} \right) = (8.25 \times 10^{-19} \text{ J}) \times 0.8889 = \mathbf{7.33 \times 10^{-19} \text{ J}}$$
        In electron-volts:
        $$E_0 = \frac{7.33 \times 10^{-19} \text{ J}}{1.602 \times 10^{-19} \text{ J/eV}} = \mathbf{4.58 \text{ eV}}$$</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Final Results:</strong><br>
      $B = \mathbf{9.68 \times 10^{-106} \text{ J}\cdot\text{m}^9}$<br>
      $E_0 = \mathbf{7.33 \times 10^{-19} \text{ J}} = \mathbf{4.58 \text{ eV}}$<br>
      Notice that repulsion reduces the net binding energy by $1/n$ (here $1/9 \approx 11\%$) compared to pure attractive energy.
    </div>""")

# Save checkpoint
with open("generator/ch2_temp.py", "w", encoding="utf-8") as f:
    f.write(f"COUNT = {len(P)}\n")
print(f"Added up to P6 in Ch 2. Current count: {len(P)}")
