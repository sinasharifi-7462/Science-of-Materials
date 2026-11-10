# generator/make_ch4_part1.py
# ==============================================================================
# CHAPTER 4: IMPERFECTIONS IN SOLIDS - PART 1 (PROBLEMS 1 TO 25)
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

# P1: Thermodynamic Origin of Vacancies
add(1, "Thermodynamic Origin and Equilibrium Concentration of Vacancies",
    "Point Defects in Metals", "point_defects", "Advanced",
    r"""<p>Unlike linear and planar defects, point vacancies exist in all crystalline materials in thermodynamic equilibrium at all temperatures above absolute zero ($T > 0 \text{ K}$).</p>
    <ol type="a">
      <li>Using thermodynamic principles, explain why an equilibrium concentration of vacancies $N_v$ must exist at temperature $T$, balancing the enthalpy of vacancy formation $\Delta H_v$ against the configurational entropy $\Delta S_{\text{conf}}$.</li>
      <li>Derive the classic equilibrium vacancy concentration equation:
      $$\frac{N_v}{N} = \exp\left(-\frac{Q_v}{k_B T}\right)$$
      where $N$ is the total number of atomic lattice sites, $Q_v$ is the vacancy formation energy per site, and $k_B$ is Boltzmann's constant.</li>
      <li>State typical vacancy fraction magnitudes at room temperature ($300 \text{ K}$) versus near the melting temperature ($T \approx T_m$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Thermodynamic Free Energy Balance</div>
      <p>The equilibrium state of a crystal at constant temperature and pressure corresponds to the minimum of Gibbs free energy:</p>
      $$\Delta G = \Delta H - T \Delta S$$
      <p>Creating $N_v$ vacancies in a crystal with $N$ lattice sites involves two competing thermodynamic effects:</p>
      <ol>
        <li><strong>Enthalpic Cost ($\Delta H = N_v Q_v > 0$):</strong> Removing atoms from lattice sites breaks nearest-neighbor interatomic bonds and creates local elastic distortion. Because bonds are broken, formation enthalpy is positive, which increases $G$ linearly with $N_v$.</li>
        <li><strong>Configurational Entropic Gain ($\Delta S_{\text{conf}} > 0$):</strong> Distributing $N_v$ indistinguishable vacancies among $(N + N_v)$ available lattice sites introduces spatial randomness (mixing). According to Boltzmann's entropy formula $S = k_B \ln \Omega$:
        $$\Omega = \frac{(N + N_v)!}{N! N_v!}$$
        The entropic term $-T\Delta S_{\text{conf}}$ drops steeply with an infinite negative slope $(\partial G / \partial N_v \to -\infty)$ as $N_v \to 0$.</li>
      </ol>
      <p>Because the initial entropic decrease in free energy overwhelms the positive formation enthalpy at any $T > 0 \text{ K}$, the curve $G(N_v)$ always exhibits a distinct free energy minimum at a non-zero vacancy concentration $N_v > 0$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Derivation of Equilibrium Vacancy Concentration</div>
      <p>Using Stirling's approximation ($\ln x! \approx x\ln x - x$ for large $x$):</p>
      $$\ln\Omega \approx (N + N_v)\ln(N + N_v) - (N + N_v) - [N\ln N - N] - [N_v\ln N_v - N_v]$$
      $$\ln\Omega = (N + N_v)\ln(N + N_v) - N\ln N - N_v\ln N_v$$
      <p>The total Gibbs free energy change upon introducing $N_v$ vacancies is:</p>
      $$\Delta G = N_v Q_v - k_B T \left[ (N + N_v)\ln(N + N_v) - N\ln N - N_v\ln N_v \right]$$
      <p>At thermodynamic equilibrium, the free energy is minimized with respect to vacancy count: $\frac{\partial(\Delta G)}{\partial N_v} = 0$:</p>
      $$\frac{\partial(\Delta G)}{\partial N_v} = Q_v - k_B T \left[ \ln(N + N_v) + 1 - (\ln N_v + 1) \right] = 0$$
      $$Q_v - k_B T \ln\left(\frac{N + N_v}{N_v}\right) = 0 \implies \ln\left(\frac{N + N_v}{N_v}\right) = \frac{Q_v}{k_B T}$$
      $$\frac{N + N_v}{N_v} \approx \frac{N}{N_v} = \exp\left(\frac{Q_v}{k_B T}\right) \implies \frac{N_v}{N} = \exp\left(-\frac{Q_v}{k_B T}\right)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Typical Magnitudes</div>
      <ul>
        <li><strong>Room Temperature ($300 \text{ K}$):</strong> Vacancy fractions are negligibly small: $\frac{N_v}{N} \sim 10^{-15}$ to $10^{-10}$ (roughly 1 vacancy per trillion lattice sites).</li>
        <li><strong>Near Melting Point ($T \approx T_m$):</strong> Vacancy fractions increase exponentially to $\frac{N_v}{N} \sim 10^{-4}$ to $10^{-3}$ (roughly 1 vacancy per $1,000$ to $10,000$ lattice sites).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Equilibrium Vacancy Law:</strong> $$\frac{N_v}{N} = \exp\left(-\frac{Q_v}{k_B T}\right)$$
      Vacancies are thermodynamically stable because configurational entropy minimization dominates over formation enthalpy at $T > 0\text{ K}$.
    </div>""")

# P2: Equilibrium Vacancies in Copper
add(2, "Equilibrium Vacancy Concentration in Copper: Room Temperature vs. Near Melting",
    "Point Defects in Metals", "point_defects", "Intermediate",
    r"""<p>Pure copper has an atomic weight $A_{\text{Cu}} = 63.55 \text{ g/mol}$, mass density $\rho = 8.94 \text{ g/cm}^3$, and melting point $T_m = 1084^\circ\text{C}$ ($1357 \text{ K}$). The vacancy formation energy in copper is $Q_v = 0.90 \text{ eV/atom}$.</p>
    <ol type="a">
      <li>Calculate the total number of atomic lattice sites $N$ per cubic meter of copper.</li>
      <li>Calculate the equilibrium vacancy fraction $N_v/N$ and the total number of vacancies per cubic meter $N_v$ at room temperature ($25^\circ\text{C} = 298 \text{ K}$).</li>
      <li>Calculate $N_v/N$ and $N_v$ at $1000^\circ\text{C}$ ($1273 \text{ K}$).</li>
      <li>Determine the ratio of vacancy concentrations $N_v(1000^\circ\text{C}) / N_v(25^\circ\text{C})$ to demonstrate the thermal sensitivity of point defects.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Total Lattice Sites per Cubic Meter ($N$)</div>
      <p>Using mass density $\rho = 8.94 \text{ g/cm}^3 = 8.94 \times 10^6 \text{ g/m}^3$ and Avogadro's number $N_A = 6.022 \times 10^{23} \text{ atoms/mol}$:</p>
      $$N = \frac{\rho N_A}{A} = \frac{(8.94 \times 10^6 \text{ g/m}^3) \times (6.022 \times 10^{23} \text{ atoms/mol})}{63.55 \text{ g/mol}} = \mathbf{8.472 \times 10^{28} \text{ sites/m}^3}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Vacancies at Room Temperature ($T = 298 \text{ K}$)</div>
      <p>Boltzmann's constant $k_B = 8.617 \times 10^{-5} \text{ eV/K}$:</p>
      $$k_B T = (8.617 \times 10^{-5} \text{ eV/K}) \times (298 \text{ K}) = 0.02568 \text{ eV}$$
      $$\frac{N_v}{N} = \exp\left(-\frac{0.90 \text{ eV}}{0.02568 \text{ eV}}\right) = \exp(-35.047) = \mathbf{6.00 \times 10^{-16}}$$
      $$N_v = (6.00 \times 10^{-16}) \times (8.472 \times 10^{28} \text{ m}^{-3}) = \mathbf{5.08 \times 10^{13} \text{ vacancies/m}^3}$$
      <p>In a cubic centimeter ($1 \text{ cm}^3 = 10^{-6} \text{ m}^3$), there are only $\sim 5 \times 10^7$ vacancies among $\sim 8.5 \times 10^{22}$ atoms!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Vacancies at Elevated Temperature ($T = 1273 \text{ K}$)</div>
      $$k_B T = (8.617 \times 10^{-5} \text{ eV/K}) \times (1273 \text{ K}) = 0.10969 \text{ eV}$$
      $$\frac{N_v}{N} = \exp\left(-\frac{0.90 \text{ eV}}{0.10969 \text{ eV}}\right) = \exp(-8.2046) = \mathbf{2.734 \times 10^{-4}}$$
      $$N_v = (2.734 \times 10^{-4}) \times (8.472 \times 10^{28} \text{ m}^{-3}) = \mathbf{2.316 \times 10^{25} \text{ vacancies/m}^3}$$
      <p>At $1000^\circ\text{C}$, roughly 1 in every 3,650 lattice sites is vacant!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Concentration Ratio</div>
      $$\frac{N_v(1000^\circ\text{C})}{N_v(25^\circ\text{C})} = \frac{2.734 \times 10^{-4}}{6.00 \times 10^{-16}} = \mathbf{4.56 \times 10^{11}}$$
      <p>Heating copper from room temperature to $1000^\circ\text{C}$ multiplies the equilibrium vacancy concentration by more than <strong>450 billion times</strong>.</p>
    </div>
    <div class="final-answer-box">
      <strong>Total Sites:</strong> $N = \mathbf{8.47 \times 10^{28} \text{ m}^{-3}}$<br>
      <strong>At $25^\circ\text{C}$ ($298 \text{ K}$):</strong> $N_v/N = \mathbf{6.00 \times 10^{-16}}$, $N_v = \mathbf{5.08 \times 10^{13} \text{ m}^{-3}}$<br>
      <strong>At $1000^\circ\text{C}$ ($1273 \text{ K}$):</strong> $N_v/N = \mathbf{2.73 \times 10^{-4}}$, $N_v = \mathbf{2.32 \times 10^{25} \text{ m}^{-3}}$<br>
      <strong>Thermal Increase Ratio:</strong> $\mathbf{4.56 \times 10^{11}\times}$
    </div>""")

# P3: Quenched-in Vacancies in Aluminum
add(3, "Quenched-in Non-Equilibrium Vacancy Retention in Aluminum",
    "Point Defects in Metals", "point_defects", "Intermediate",
    r"""<p>An aluminum sheet ($A_{\text{Al}} = 26.98 \text{ g/mol}, \rho = 2.70 \text{ g/cm}^3$) is heated to $600^\circ\text{C}$ ($873 \text{ K}$) and then rapidly water-quenched to room temperature ($20^\circ\text{C} = 293 \text{ K}$). The vacancy formation energy in aluminum is $Q_v = 0.75 \text{ eV/atom}$.</p>
    <ol type="a">
      <li>Calculate the equilibrium vacancy fraction $X_v = N_v/N$ at $600^\circ\text{C}$.</li>
      <li>Calculate the equilibrium vacancy fraction at $20^\circ\text{C}$.</li>
      <li>Assuming an ideal ultra-fast quench that traps all high-temperature vacancies into the room-temperature lattice, calculate the <strong>vacancy supersaturation ratio</strong> $S_v = X_v(600^\circ\text{C}) / X_v(20^\circ\text{C})$.</li>
      <li>Explain the metallurgical consequences of these quenched-in excess vacancies during subsequent room-temperature natural aging of heat-treatable aluminum alloys (e.g., Al-Cu 2024).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Equilibrium Vacancy Fraction at $600^\circ\text{C}$ ($873 \text{ K}$)</div>
      $$k_B T_1 = (8.617 \times 10^{-5} \text{ eV/K}) \times (873 \text{ K}) = 0.07523 \text{ eV}$$
      $$X_v(600^\circ\text{C}) = \exp\left(-\frac{0.75 \text{ eV}}{0.07523 \text{ eV}}\right) = \exp(-9.9699) = \mathbf{4.679 \times 10^{-5}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Equilibrium Vacancy Fraction at $20^\circ\text{C}$ ($293 \text{ K}$)</div>
      $$k_B T_2 = (8.617 \times 10^{-5} \text{ eV/K}) \times (293 \text{ K}) = 0.02525 \text{ eV}$$
      $$X_v(20^\circ\text{C}) = \exp\left(-\frac{0.75 \text{ eV}}{0.02525 \text{ eV}}\right) = \exp(-29.705) = \mathbf{1.257 \times 10^{-13}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Vacancy Supersaturation Ratio</div>
      $$S_v = \frac{X_v(600^\circ\text{C})}{X_v(20^\circ\text{C})} = \frac{4.679 \times 10^{-5}}{1.257 \times 10^{-13}} = \mathbf{3.72 \times 10^8}$$
      <p>The quenched alloy contains over <strong>370 million times</strong> more vacancies than the thermodynamic equilibrium value at room temperature!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Metallurgical Consequences in Precipitation Hardening</div>
      <p>Substitutional diffusion of solute atoms (such as copper in aluminum) requires vacancy exchange. At room temperature, equilibrium vacancy concentration is so infinitesimal ($10^{-13}$) that substitutional solute diffusion is practically frozen. However, the trapped non-equilibrium supersaturation of vacancies ($10^{-5}$) accelerates atomic mobility by 8 orders of magnitude. This enables copper solute atoms to diffuse rapidly at room temperature to form Guinier-Preston (GP) zones, leading to spontaneous natural precipitation hardening without requiring external heating.</p>
    </div>
    <div class="final-answer-box">
      <strong>At $600^\circ\text{C}$:</strong> $X_v = \mathbf{4.68 \times 10^{-5}}$ &bull; <strong>At $20^\circ\text{C}$:</strong> $X_v = \mathbf{1.26 \times 10^{-13}}$<br>
      <strong>Supersaturation:</strong> $S_v = \mathbf{3.72 \times 10^8}$<br>
      Quenched-in excess vacancies accelerate solute mobility by $10^8\times$, driving natural room-temperature aging (GP zone formation).
    </div>""")

# P4: Determining Activation Energy Qv from Arrhenius Plot
add(4, "Determination of Vacancy Formation Energy $Q_v$ from Temperature-Dependent Data",
    "Point Defects in Metals", "point_defects", "Intermediate",
    r"""<p>The electrical resistivity of a high-purity gold wire is measured after quenching from various elevated temperatures. Because each trapped vacancy contributes a fixed increment to electrical resistivity ($\Delta\rho \propto N_v$), the vacancy concentration $N_v/N$ is determined at two temperatures:</p>
    <div style="text-align:center; margin: 10px 0;">
      At $T_1 = 700^\circ\text{C}$ ($973 \text{ K}$): $N_v/N = 2.15 \times 10^{-5}$<br>
      At $T_2 = 900^\circ\text{C}$ ($1173 \text{ K}$): $N_v/N = 1.82 \times 10^{-4}$
    </div>
    <ol type="a">
      <li>Derive an expression for the vacancy formation energy $Q_v$ from measurements at two temperatures $T_1$ and $T_2$.</li>
      <li>Calculate $Q_v$ in electron-volts per atom ($\text{eV/atom}$) and in kilojoules per mole ($\text{kJ/mol}$).</li>
      <li>Predict the equilibrium vacancy concentration at $T_3 = 800^\circ\text{C}$ ($1073 \text{ K}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Two-Point Arrhenius Formula</div>
      <p>Taking the natural logarithm of the vacancy concentration equation:</p>
      $$\ln\left(\frac{N_v}{N}\right) = \ln C - \frac{Q_v}{k_B T}$$
      <p>Evaluating at temperatures $T_1$ and $T_2$ and subtracting:</p>
      $$\ln\left(\frac{N_{v,2}}{N}\right) - \ln\left(\frac{N_{v,1}}{N}\right) = -\frac{Q_v}{k_B}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) = \frac{Q_v}{k_B}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$$
      $$Q_v = \frac{k_B \ln\left(\frac{N_{v,2}}{N_{v,1}}\right)}{\frac{1}{T_1} - \frac{1}{T_2}} = \frac{k_B T_1 T_2}{T_2 - T_1} \ln\left(\frac{N_{v,2}}{N_{v,1}}\right)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation of Formation Energy $Q_v$</div>
      <p>Given $T_1 = 973 \text{ K}$, $T_2 = 1173 \text{ K}$, $N_{v,1}/N = 2.15 \times 10^{-5}$, $N_{v,2}/N = 1.82 \times 10^{-4}$:</p>
      $$\frac{N_{v,2}}{N_{v,1}} = \frac{1.82 \times 10^{-4}}{2.15 \times 10^{-5}} = 8.4651 \implies \ln(8.4651) = 2.13596$$
      $$\frac{1}{T_1} - \frac{1}{T_2} = \frac{1}{973} - \frac{1}{1173} = 1.02775 \times 10^{-3} - 8.52515 \times 10^{-4} = 1.7523 \times 10^{-4} \text{ K}^{-1}$$
      $$Q_v = \frac{(8.617 \times 10^{-5} \text{ eV/K}) \times 2.13596}{1.7523 \times 10^{-4} \text{ K}^{-1}} = \mathbf{1.050 \text{ eV/atom}}$$
      <p>Converting to $\text{kJ/mol}$ using $1 \text{ eV/atom} = 96.485 \text{ kJ/mol}$:</p>
      $$Q_v = 1.050 \times 96.485 = \mathbf{101.3 \text{ kJ/mol}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Vacancy Concentration at $800^\circ\text{C}$ ($1073 \text{ K}$)</div>
      $$\ln\left(\frac{N_{v,3}}{N}\right) = \ln(2.15 \times 10^{-5}) - \frac{1.050 \text{ eV}}{8.617 \times 10^{-5} \text{ eV/K}}\left(\frac{1}{1073} - \frac{1}{973}\right)$$
      $$\frac{1}{1073} - \frac{1}{973} = 9.3197 \times 10^{-4} - 1.02775 \times 10^{-3} = -9.578 \times 10^{-5} \text{ K}^{-1}$$
      $$\Delta\ln = - \frac{1.050}{8.617 \times 10^{-5}} \times (-9.578 \times 10^{-5}) = +1.1671$$
      $$\frac{N_{v,3}}{N} = (2.15 \times 10^{-5}) \times \exp(1.1671) = (2.15 \times 10^{-5}) \times 3.2127 = \mathbf{6.91 \times 10^{-5}}$$
    </div>
    <div class="final-answer-box">
      <strong>Formation Energy:</strong> $Q_v = \mathbf{1.05 \text{ eV/atom}} = \mathbf{101.3 \text{ kJ/mol}}$<br>
      <strong>Predicted Concentration at $800^\circ\text{C}$:</strong> $N_v/N = \mathbf{6.91 \times 10^{-5}}$
    </div>""")

# P5: Self-Interstitials vs Vacancies Energetics
add(5, "Self-Interstitials vs. Vacancies: Elastic Strain Energy and Concentration Disparity",
    "Point Defects in Metals", "point_defects", "Intermediate",
    r"""<p>Point defects in pure elemental metals include both vacancies and self-interstitials.</p>
    <ol type="a">
      <li>Define a <strong>self-interstitial</strong> in a metal crystal.</li>
      <li>Explain why the formation energy of a self-interstitial ($Q_i \approx 3\text{--}5 \text{ eV}$) is substantially higher than the vacancy formation energy ($Q_v \approx 0.8\text{--}1.2 \text{ eV}$) in close-packed metals (FCC and HCP).</li>
      <li>For a metal where $Q_v = 1.0 \text{ eV}$ and $Q_i = 4.0 \text{ eV}$, compute the ratio of equilibrium self-interstitials to vacancies ($N_i / N_v$) at $T = 1000 \text{ K}$.</li>
      <li>Under what non-thermal engineering conditions can large non-equilibrium concentrations of self-interstitials be produced?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition of Self-Interstitial</div>
      <p>A self-interstitial is a host atom that is forced into an interstitial void (a normally unoccupied space between host lattice sites) within its own parent crystal lattice.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Why $Q_i \gg Q_v$ in Close-Packed Metals</div>
      <p>In close-packed FCC and HCP metals, the atomic packing factor is 0.74, leaving only 26% interstitial free space distributed among small tetrahedral and octahedral interstitial voids. The largest interstitial void radius in FCC is only $r_{\text{oct}} = 0.414 R$. Forcing an entire host atom of full radius $R$ into a void of radius $0.414 R$ requires severe outward displacement of all surrounding coordinating atoms, creating an intense, long-range compressive elastic strain field. Conversely, creating a vacancy involves merely removing an atom and slightly relaxing surrounding bonds inward. Because elastic strain energy scales with the square of volume distortion, $Q_i \approx 3\text{--}5 \text{ eV} \gg Q_v \approx 1 \text{ eV}$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Ratio of Interstitials to Vacancies at $T = 1000 \text{ K}$</div>
      <p>Using Boltzmann thermal equilibrium equations:</p>
      $$\frac{N_i}{N_v} = \frac{\exp(-Q_i/k_B T)}{\exp(-Q_v/k_B T)} = \exp\left(-\frac{Q_i - Q_v}{k_B T}\right)$$
      $$\Delta Q = Q_i - Q_v = 4.0 \text{ eV} - 1.0 \text{ eV} = 3.0 \text{ eV}$$
      $$k_B T = (8.617 \times 10^{-5} \text{ eV/K}) \times (1000 \text{ K}) = 0.08617 \text{ eV}$$
      $$\frac{N_i}{N_v} = \exp\left(-\frac{3.0 \text{ eV}}{0.08617 \text{ eV}}\right) = \exp(-34.815) = \mathbf{7.58 \times 10^{-16}}$$
      <p>Even at $1000 \text{ K}$, there is less than one self-interstitial for every $10^{15}$ vacancies! Thermally, self-interstitials are completely negligible.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Non-Thermal Generation Mechanisms</div>
      <p>Large non-equilibrium concentrations of self-interstitials are generated mechanically by <strong>severe plastic deformation</strong> (intersecting dislocation jogs) and by <strong>high-energy particle irradiation</strong> (neutron bombardment in nuclear reactor pressure vessels and ion implantation in semiconductor processing), where ballistic collisions directly knock host atoms out of lattice sites, creating Frenkel-like displacement cascades.</p>
    </div>
    <div class="final-answer-box">
      <strong>Strain Disparity:</strong> Forcing a full-sized atom into an interstitial void causes severe compressive lattice strain ($Q_i \approx 4\text{ eV} \gg Q_v \approx 1\text{ eV}$).<br>
      <strong>Equilibrium Ratio at $1000 \text{ K}$:** $N_i / N_v = \mathbf{7.6 \times 10^{-16}}$ (negligible).<br>
      <strong>Athermal Generation:</strong> Nuclear radiation cascades and severe cold work.
    </div>""")

# Save checkpoint for part 1
print("Part 1: P1-P5 written.")
# P6: Substitutional vs Interstitial Solid Solutions
add(6, "Solid Solutions: Substitutional vs. Interstitial Atomic Mechanisms",
    "Solid Solutions & Solubility", "solid_solutions", "Fundamental",
    r"""<p>When impurity or alloying atoms are added to a metallic host crystal, they can either dissolve to form a single-phase solid solution or precipitate out to form a secondary phase.</p>
    <ol type="a">
      <li>Differentiate between a <strong>substitutional solid solution</strong> and an <strong>interstitial solid solution</strong>.</li>
      <li>Illustrate the localized lattice strain fields (tensile vs. compressive) induced around:
        <ul>
          <li>An oversized substitutional solute atom.</li>
          <li>An undersized substitutional solute atom.</li>
          <li>An interstitial solute atom.</li>
        </ul>
      </li>
      <li>Give two commercial engineering alloy examples of each type of solid solution.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Substitutional vs. Interstitial Solid Solutions</div>
      <ul>
        <li><strong>Substitutional Solid Solution:</strong> Solute atoms directly replace or substitute for host solvent atoms at standard crystalline lattice positions. Occurs when solute and solvent atoms have comparable atomic radii (e.g., Ni dissolved in Cu).</li>
        <li><strong>Interstitial Solid Solution:</strong> Solute atoms occupy the tiny empty interstitial void spaces (octahedral or tetrahedral interstices) located between host solvent atoms, leaving all solvent lattice sites filled. Occurs only when solute atoms are much smaller than solvent atoms ($r_{\text{solute}} \ll R_{\text{solvent}}$), typically restricted to small non-metallic atoms (H, B, C, N, O).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Localized Elastic Lattice Strain Fields</div>
      <ul>
        <li><strong>Oversized Substitutional Atom (e.g., Zn in Cu):</strong> The larger solute atom pushes surrounding host atoms outward, creating a spherically symmetric <strong>compressive strain field</strong> in the surrounding host lattice.</li>
        <li><strong>Undersized Substitutional Atom (e.g., Ni in Cu):</strong> Surrounding host atoms collapse inward toward the smaller solute atom, generating a spherically symmetric <strong>tensile strain field</strong> in the adjacent lattice.</li>
        <li><strong>Interstitial Solute Atom (e.g., C in Fe):</strong> Because the interstitial atom is almost always larger than the natural interstitial void volume, it forces neighboring solvent atoms forcefully outward, generating intense <strong>compressive strain fields</strong> (and in BCC iron, asymmetric tetragonal distortions).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Engineering Alloy Examples</div>
      <ul>
        <li><strong>Substitutional Solid Solutions:</strong>
          <ol>
            <li><em>Cartridge Brass:</em> Zinc ($r = 0.133 \text{ nm}$) substituted into Copper ($r = 0.128 \text{ nm}$) up to $30 \text{ wt}\%$.</li>
            <li><em>Monel / Cupronickel:</em> Nickel ($r = 0.125 \text{ nm}$) dissolved in Copper across the entire $0\text{--}100\%$ range.</li>
          </ol>
        </li>
        <li><strong>Interstitial Solid Solutions:</strong>
          <ol>
            <li><em>Carbon in Ferrite ($\alpha$-Fe) / Austenite ($\gamma$-Fe):</em> Carbon atoms ($r = 0.071 \text{ nm}$) dissolved interstitially in iron.</li>
            <li><em>Interstitial Oxygen in Titanium:</em> Oxygen dissolved interstitially in HCP $\alpha$-Ti, strongly increasing yield strength.</li>
          </ol>
        </li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Substitutional:</strong> Solute replaces host on regular lattice sites (creates spherical tensile or compressive strains).<br>
      <strong>Interstitial:</strong> Tiny solute fits into void spaces (creates severe compressive and shear strains).
    </div>""")

# P7: Hume-Rothery Rules for Complete Solid Solubility
add(7, "Hume-Rothery Empirical Rules for Unlimited Substitutional Solid Solubility",
    "Solid Solutions & Solubility", "solid_solutions", "Fundamental",
    r"""<p>In the 1930s, British metallurgist William Hume-Rothery formulated four empirical criteria governing whether two metals can form a continuous, complete substitutional solid solution across all compositions ($0\text{--}100\%$).</p>
    <ol type="a">
      <li>State and explain all <strong>four Hume-Rothery rules</strong> for complete substitutional solubility.</li>
      <li>Explain the thermodynamic and crystallographic physical mechanism behind each rule.</li>
      <li>What happens to solid solubility if one or more of these rules are moderately violated?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): The Four Hume-Rothery Rules and Their Mechanisms</div>
      <ol>
        <li><strong>Atomic Size Factor Rule:</strong>
          $$\delta = \frac{|r_{\text{solute}} - r_{\text{solvent}}|}{r_{\text{solvent}}} \times 100\% \le 15\%$$
          <em>Physical Mechanism:</em> If atomic radii differ by more than $\sim 15\%$, the elastic strain energy stored in the crystal lattice becomes so excessively high that the system energetically prefers to phase-separate into two distinct crystalline phases to relieve strain.
        </li>
        <li><strong>Crystal Structure Rule:</strong>
          Both elements must possess identical crystal structures (e.g., both FCC, or both BCC).
          <em>Physical Mechanism:</em> To transition continuously from 100% component A to 100% component B without crossing a discontinuous two-phase boundary, the parent space lattice must maintain topological continuity.
        </li>
        <li><strong>Electronegativity Difference Rule:</strong>
          The electronegativities $\chi$ of the two elements must be very close ($\Delta\chi \approx 0$).
          <em>Physical Mechanism:</em> If $\Delta\chi$ is large, the electron transfer tendency favors the formation of an ordered ionic or intermetallic compound (e.g., stoichiometric phase) with high thermodynamic stability rather than a disordered solid solution.
        </li>
        <li><strong>Valency Rule:</strong>
          Both elements should have the same valence; if valences differ, a metal dissolves a solute of higher valence far more readily than a solute of lower valence (relative valency effect).
          <em>Physical Mechanism:</em> Higher-valence solutes contribute more electrons to the conduction Fermi sea, altering the electron-to-atom ($e/a$) ratio up to the Brillouin zone boundary.
        </li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Consequences of Rule Violations</div>
      <p>If any of the Hume-Rothery conditions are violated, complete ($100\%$) mutual isomorphous solubility is impossible. The system exhibits only <strong>partial (terminal) solid solubility</strong>, where solvent A can dissolve only a limited atomic fraction of solute B before reaching a solubility limit, beyond which an intermediate intermetallic phase or two-phase eutectic mixture precipitates.</p>
    </div>
    <div class="final-answer-box">
      <strong>The 4 Hume-Rothery Rules:</strong><br>
      1. Size misfit $\delta \le 15\%$ &bull; 2. Identical crystal structure &bull; 3. Similar electronegativity ($\Delta\chi \approx 0$) &bull; 4. Matching valency (or higher-valence solute).<br>
      Violation leads to restricted partial terminal solubility or intermetallic compound formation.
    </div>""")

# P8: Hume-Rothery Application to Copper Alloys
add(8, "Predicting Solid Solubility in Copper Alloys Using Hume-Rothery Criteria",
    "Solid Solutions & Solubility", "solid_solutions", "Intermediate",
    r"""<p>Copper has an atomic radius $r_{\text{Cu}} = 0.1278 \text{ nm}$, FCC crystal structure, Pauling electronegativity $\chi_{\text{Cu}} = 1.90$, and standard valence $+1$ (or $+2$). Data for five candidate alloying elements are tabulated below:</p>
    <table class="table-styled">
      <thead><tr><th>Element</th><th>Atomic Radius $r$ (nm)</th><th>Crystal Structure</th><th>Electronegativity $\chi$</th><th>Common Valence</th></tr></thead>
      <tbody>
        <tr><td>Nickel (Ni)</td><td>0.1246</td><td>FCC</td><td>1.88</td><td>+2</td></tr>
        <tr><td>Zinc (Zn)</td><td>0.1332</td><td>HCP</td><td>1.65</td><td>+2</td></tr>
        <tr><td>Silver (Ag)</td><td>0.1445</td><td>FCC</td><td>1.93</td><td>+1</td></tr>
        <tr><td>Lead (Pb)</td><td>0.1750</td><td>FCC</td><td>1.80</td><td>+2</td></tr>
        <tr><td>Iron (Fe)</td><td>0.1241</td><td>BCC</td><td>1.83</td><td>+2, +3</td></tr>
      </tbody>
    </table>
    <ol type="a">
      <li>Calculate the atomic size mismatch $\delta = \frac{|r - r_{\text{Cu}}|}{r_{\text{Cu}}} \times 100\%$ for each element.</li>
      <li>Systematically evaluate all four Hume-Rothery rules for each element in Copper.</li>
      <li>Predict which element forms a complete isomorphous solid solution with Copper, which elements exhibit moderate partial solubility, and which is virtually insoluble.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Size Mismatch Calculations</div>
      <ul>
        <li><strong>Nickel (Ni):</strong> $\delta = \frac{|0.1246 - 0.1278|}{0.1278} \times 100\% = \mathbf{2.50\%}$ ($\le 15\%$, Excellent)</li>
        <li><strong>Zinc (Zn):</strong> $\delta = \frac{|0.1332 - 0.1278|}{0.1278} \times 100\% = \mathbf{4.23\%}$ ($\le 15\%$, Excellent)</li>
        <li><strong>Silver (Ag):</strong> $\delta = \frac{|0.1445 - 0.1278|}{0.1278} \times 100\% = \mathbf{13.07\%}$ ($\le 15\%$, Borderline)</li>
        <li><strong>Lead (Pb):</strong> $\delta = \frac{|0.1750 - 0.1278|}{0.1278} \times 100\% = \mathbf{36.93\%}$ ($> 15\%$, Severe Violation!)</li>
        <li><strong>Iron (Fe):</strong> $\delta = \frac{|0.1241 - 0.1278|}{0.1278} \times 100\% = \mathbf{2.89\%}$ ($\le 15\%$, Excellent)</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b) & (c): Evaluation and Solubility Predictions</div>
      <ul>
        <li><strong>Nickel (Ni):</strong>
          <ul>
            <li>Size mismatch: $2.5\%$ (Satisfied).</li>
            <li>Structure: FCC matches FCC (Satisfied).</li>
            <li>Electronegativity: $1.88$ vs $1.90 \implies \Delta\chi = 0.02$ (Satisfied).</li>
            <li>Valence: $+2$ (Compatible).</li>
            <li><strong>Prediction:</strong> Satisfies all 4 criteria completely! Forms a <strong>100% complete isomorphous solid solution</strong> across all compositions (Cu-Ni phase diagram is a textbook lens-shaped isomorphous system).</li>
          </ul>
        </li>
        <li><strong>Zinc (Zn):</strong>
          <ul>
            <li>Size mismatch: $4.2\%$ (Satisfied).</li>
            <li>Structure: HCP $\neq$ FCC (Violated!).</li>
            <li>Electronegativity: $\Delta\chi = 0.25$ (Modest).</li>
            <li><strong>Prediction:</strong> Violates the crystal structure rule. Exhibits <strong>partial solid solubility</strong> (up to $\sim 35\text{ wt}\%$ Zn dissolves in FCC $\alpha$-brass before BCC $\beta$-brass precipitates).</li>
          </ul>
        </li>
        <li><strong>Silver (Ag):</strong>
          <ul>
            <li>Size mismatch: $13.1\%$ (Borderline high). Same FCC structure and nearly identical electronegativity.</li>
            <li><strong>Prediction:</strong> Due to significant lattice strain from the large $13\%$ size difference, it exhibits <strong>limited terminal solubility</strong> ($\sim 8\text{ wt}\%$ at eutectic $779^\circ\text{C}$, dropping to $< 0.1\%$ at room temp).</li>
          </ul>
        </li>
        <li><strong>Lead (Pb):</strong>
          <ul>
            <li>Size mismatch: $36.9\%$ (Gross violation!).</li>
            <li><strong>Prediction:</strong> Enormous size mismatch prevents substitution. Lead is <strong>practically insoluble in copper</strong> ($< 0.05\%$), solidifying as discrete, isolated liquid globules in the copper matrix (used for free-machining copper).</li>
          </ul>
        </li>
        <li><strong>Iron (Fe):</strong>
          <ul>
            <li>Size mismatch: $2.9\%$ (Satisfied). Structure: BCC $\neq$ FCC (Violated).</li>
            <li><strong>Prediction:</strong> Violates crystal structure; exhibits <strong>restricted partial solubility</strong> ($\sim 4\text{ wt}\%$ at $1096^\circ\text{C}$).</li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Complete Solubility:</strong> <strong>Nickel</strong> (satisfies all 4 rules: $\delta = 2.5\%$, FCC, $\Delta\chi = 0.02$).<br>
      <strong>Partial Solubility:</strong> <strong>Zinc</strong> ($\delta = 4.2\%$, HCP), <strong>Iron</strong> ($\delta = 2.9\%$, BCC), <strong>Silver</strong> ($\delta = 13.1\%$, FCC).<br>
      <strong>Completely Insoluble:</strong> <strong>Lead</strong> ($\delta = 36.9\% \gg 15\%$).
    </div>""")

# P9: Solid Solubility of Carbon in Iron (FCC vs BCC Paradox)
add(9, "The Interstitial Solubility Paradox: Carbon in FCC Austenite vs. BCC Ferrite",
    "Solid Solutions & Solubility", "solid_solutions", "Advanced",
    r"""<p>In the iron-carbon system, carbon dissolves interstitially. The maximum solid solubility of carbon in FCC austenite ($\gamma$-Fe) is $2.14 \text{ wt}\%$ ($9.23 \text{ at}\%$) at $1147^\circ\text{C}$. In contrast, the maximum solubility of carbon in BCC ferrite ($\alpha$-Fe) is only $0.022 \text{ wt}\%$ ($0.10 \text{ at}\%$) at $727^\circ\text{C}$, a factor of nearly 100 times smaller.</p>
    <ol type="a">
      <li>State the atomic packing factors of FCC ($0.74$) and BCC ($0.68$). Why is the dramatic difference in carbon solubility considered a crystallographic paradox at first glance?</li>
      <li>Calculate the maximum radius of a hard sphere that can fit into an <strong>octahedral interstitial site in FCC iron</strong> without lattice distortion ($R_{\text{Fe}} = 0.129 \text{ nm}$).</li>
      <li>Calculate the maximum radius of a hard sphere that can fit into:
        <ul>
          <li>An <strong>octahedral interstitial site in BCC iron</strong> ($R_{\text{Fe}} = 0.124 \text{ nm}$).</li>
          <li>A <strong>tetrahedral interstitial site in BCC iron</strong>.</li>
        </ul>
      </li>
      <li>Resolve the paradox by explaining the geometry and symmetry of the interstitial sites, the carbon radius ($r_{\text{C}} = 0.071 \text{ nm}$), and the nature of the asymmetric tetragonal distortion in BCC ferrite.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): The Crystallographic Paradox</div>
      <p>BCC ferrite has an atomic packing factor of only $\text{APF} = 0.68$, meaning that 32% of its unit cell volume is unoccupied empty space. FCC austenite has close packing with $\text{APF} = 0.74$, leaving only 26% empty space. Intuitively, one would expect the "looser" BCC lattice to accommodate far more interstitial carbon than the tightly packed FCC lattice. The fact that FCC dissolves 100 times more carbon than BCC constitutes the famous interstitial solubility paradox.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): FCC Octahedral Interstitial Void Radius</div>
      <p>In FCC, octahedral sites are located at the edge centers $(1/2, 0, 0)$ and the body center $(1/2, 1/2, 1/2)$. The edge length is $a_{\text{FCC}} = \frac{4R}{\sqrt{2}} = 2R\sqrt{2}$. Two host atoms and one interstitial void touch along the unit cell edge:</p>
      $$2R + 2r_{\text{oct}} = a_{\text{FCC}} = 2R\sqrt{2} \implies r_{\text{oct}} = R(\sqrt{2} - 1) \approx \mathbf{0.414 R}$$
      <p>For $\gamma$-Fe with $R = 0.129 \text{ nm}$:</p>
      $$r_{\text{oct}}(\text{FCC}) = 0.414 \times 0.129 \text{ nm} = \mathbf{0.0534 \text{ nm}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): BCC Interstitial Void Radii</div>
      <ul>
        <li><strong>BCC Octahedral Site (located at face centers $(1/2, 1/2, 0)$ and edge midpoints $(1/2, 0, 0)$):</strong>
          In BCC, $a_{\text{BCC}} = \frac{4R}{\sqrt{3}}$. The site is coordinated by 6 atoms, but it is <em>asymmetric</em>! Two nearest neighbors lie at distance $a/2$, while four next-nearest neighbors lie at $a/\sqrt{2}$.
          The distance between the two nearest neighbors along the cube axis is:
          $$2R + 2r_{\text{oct}} = a_{\text{BCC}} = \frac{4R}{\sqrt{3}} \implies r_{\text{oct}} = R\left(\frac{2}{\sqrt{3}} - 1\right) \approx \mathbf{0.1547 R}$$
          For $\alpha$-Fe with $R = 0.124 \text{ nm}$:</p>
          $$r_{\text{oct}}(\text{BCC}) = 0.1547 \times 0.124 \text{ nm} = \mathbf{0.0192 \text{ nm}}$$
        </li>
        <li><strong>BCC Tetrahedral Site (located at $(1/2, 1/4, 0)$):</strong>
          $$r_{\text{tet}}(\text{BCC}) = R\left(\sqrt{\frac{5}{3}} - 1\right) \approx \mathbf{0.291 R}$$
          $$r_{\text{tet}}(\text{BCC}) = 0.291 \times 0.124 \text{ nm} = \mathbf{0.0361 \text{ nm}}$$
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Resolution of the Paradox</div>
      <p>The radius of an interstitial carbon atom is $r_{\text{C}} = 0.071 \text{ nm}$:</p>
      <ol>
        <li><strong>In FCC Austenite:</strong> The octahedral void is regular, symmetric, and has radius $0.0534 \text{ nm}$. The size misfit is $\Delta r = 0.071 - 0.0534 = +0.0176 \text{ nm}$ (only $33\%$ oversize). The surrounding 6 iron atoms are pushed outward uniformly in all directions, creating an isotropic strain field of modest energy.</li>
        <li><strong>In BCC Ferrite:</strong> Even though the tetrahedral void ($0.036 \text{ nm}$) is larger, carbon prefers the octahedral site ($0.019 \text{ nm}$) because it only has to displace <em>two</em> nearest-neighbor atoms along a single cube axis rather than four. However, the size misfit is colossal: $\Delta r = 0.071 - 0.0192 = +0.0518 \text{ nm}$ (a massive $270\%$ oversize!). Forcing carbon into this site violently pushes the two nearest iron atoms apart, generating an intense, asymmetric <strong>tetragonal dipole strain</strong>. The elastic strain energy per dissolved carbon atom in BCC is enormous compared to FCC, drastically penalizing solubility to just $0.022 \text{ wt}\%$.</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>FCC Octahedral Void:</strong> $r = 0.414 R = \mathbf{0.0534 \text{ nm}}$ (symmetric, low strain $\implies 2.14\text{ wt}\%$ solubility).<br>
      <strong>BCC Octahedral Void:</strong> $r = 0.154 R = \mathbf{0.0192 \text{ nm}}$ (severely squashed, colossal tetragonal strain $\implies 0.022\text{ wt}\%$ solubility).
    </div>""")

# P10: Derivation of Interstitial Radii in FCC
add(10, "Geometric Derivation of Interstitial Site Sizes in FCC Crystals",
    "Solid Solutions & Solubility", "solid_solutions", "Intermediate",
    r"""<p>The FCC crystal lattice contains two distinct varieties of interstitial voids: octahedral interstitial sites and tetrahedral interstitial sites.</p>
    <ol type="a">
      <li>State the number and fractional coordinates of all <strong>octahedral sites</strong> in a single FCC unit cell, and determine the net number of octahedral sites per host atom.</li>
      <li>State the number and fractional coordinates of all <strong>tetrahedral sites</strong> in a single FCC unit cell, and determine the net number of tetrahedral sites per host atom.</li>
      <li>Derive the maximum hard-sphere radius ratio $r_{\text{tet}} / R$ for the tetrahedral site in FCC, and compare it to $r_{\text{oct}} / R = 0.414$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Octahedral Interstitial Sites in FCC</div>
      <ul>
        <li><strong>Locations:</strong>
          <ul>
            <li>$1$ at the body center of the unit cell: $(1/2, 1/2, 1/2)$.</li>
            <li>$12$ at the centers of all unit cell edges: $(1/2, 0, 0), (0, 1/2, 0), (0, 0, 1/2), \dots$</li>
          </ul>
        </li>
        <li><strong>Total Count per Unit Cell:</strong>
        $$N_{\text{oct}} = (1 \times 1) + \left(12 \times \frac{1}{4}\right) = 1 + 3 = \mathbf{4 \text{ octahedral sites/cell}}$$</li>
        <li><strong>Ratio per Host Atom:</strong> Since FCC has $n = 4$ host atoms/cell:
        $$\frac{N_{\text{oct}}}{n_{\text{host}}} = \frac{4}{4} = \mathbf{1 \text{ octahedral site per host atom}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Tetrahedral Interstitial Sites in FCC</div>
      <ul>
        <li><strong>Locations:</strong> Each of the 8 sub-cubes of edge length $a/2$ contains a tetrahedral site at its center:
        $$\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right), \left(\frac{3}{4}, \frac{1}{4}, \frac{1}{4}\right), \left(\frac{1}{4}, \frac{3}{4}, \frac{1}{4}\right), \dots$$
        coordinated by 1 corner atom and 3 adjacent face-centered atoms.</li>
        <li><strong>Total Count per Unit Cell:</strong> All 8 sites lie entirely inside the unit cell:
        $$N_{\text{tet}} = 8 \times 1 = \mathbf{8 \text{ tetrahedral sites/cell}}$$</li>
        <li><strong>Ratio per Host Atom:</strong>
        $$\frac{N_{\text{tet}}}{n_{\text{host}}} = \frac{8}{4} = \mathbf{2 \text{ tetrahedral sites per host atom}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Derivation of Tetrahedral Radius Ratio ($r_{\text{tet}}/R$)</div>
      <p>The distance from a corner atom $(0,0,0)$ to the center of the adjacent sub-cube $(a/4, a/4, a/4)$ is:</p>
      $$d_{\text{corner-tet}} = \sqrt{\left(\frac{a}{4}\right)^2 + \left(\frac{a}{4}\right)^2 + \left(\frac{a}{4}\right)^2} = \frac{a\sqrt{3}}{4}$$
      <p>For hard-sphere contact between the corner host atom (radius $R$) and the interstitial sphere (radius $r_{\text{tet}}$):</p>
      $$R + r_{\text{tet}} = \frac{a\sqrt{3}}{4}$$
      <p>In FCC, host atoms touch along the face diagonal: $4R = a\sqrt{2} \implies a = \frac{4R}{\sqrt{2}} = 2R\sqrt{2}$. Substituting for $a$:</p>
      $$R + r_{\text{tet}} = \frac{(2R\sqrt{2})\sqrt{3}}{4} = \frac{2\sqrt{6}}{4}R = \frac{\sqrt{6}}{2}R$$
      $$\frac{r_{\text{tet}}}{R} = \frac{\sqrt{6}}{2} - 1 = \frac{2.4495}{2} - 1 = 1.2247 - 1 = \mathbf{0.2247 \approx 0.225}$$
      <p>Comparison: In FCC, the octahedral site ($r/R = 0.414$) is nearly <strong>twice as large</strong> as the tetrahedral site ($r/R = 0.225$). Solute atoms in FCC exclusively occupy octahedral sites.</p>
    </div>
    <div class="final-answer-box">
      <strong>FCC Sites:</strong> 4 Octahedral sites/cell ($1:1$ ratio) &bull; 8 Tetrahedral sites/cell ($2:1$ ratio).<br>
      <strong>Radii Ratios:</strong> $\frac{r_{\text{oct}}}{R} = \mathbf{0.414}$ &bull; $\frac{r_{\text{tet}}}{R} = \mathbf{0.225}$.
    </div>""")

# P11: Interstitial Radii in BCC
add(11, "Geometric Derivation of Interstitial Void Dimensions in BCC Crystals",
    "Solid Solutions & Solubility", "solid_solutions", "Advanced",
    r"""<p>The BCC crystal structure contains octahedral and tetrahedral interstitial voids with geometric properties markedly different from those in FCC.</p>
    <ol type="a">
      <li>Derive the maximum radius ratio $r_{\text{oct}} / R$ for an octahedral site in BCC iron, specifying the coordinates and nearest-neighbor distances.</li>
      <li>Derive the maximum radius ratio $r_{\text{tet}} / R$ for a tetrahedral site in BCC iron.</li>
      <li>State the total number of octahedral and tetrahedral sites per host atom in a BCC crystal.</li>
      <li>Why does carbon choose the <em>smaller</em> octahedral site ($0.155 R$) over the <em>larger</em> tetrahedral site ($0.291 R$) in BCC iron?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): BCC Octahedral Site Derivation</div>
      <p>Octahedral sites in BCC are located at the center of unit cell faces (e.g., $(1/2, 1/2, 0)$) and the midpoints of unit cell edges (e.g., $(1/2, 0, 0)$). Consider an edge midpoint $(1/2, 0, 0)$:</p>
      <ul>
        <li>It has 2 nearest neighbors along the edge at $(0,0,0)$ and $(1,0,0)$, separated by distance $a$.</li>
        <li>It has 4 next-nearest neighbors in the perpendicular plane at distance $a\sqrt{2}/2 \approx 0.707 a$.</li>
      </ul>
      <p>Hard contact along the edge dictates:</p>
      $$2R + 2r_{\text{oct}} = a_{\text{BCC}}$$
      <p>In BCC, atoms touch along the body diagonal: $4R = a\sqrt{3} \implies a = \frac{4R}{\sqrt{3}}$.</p>
      $$2R + 2r_{\text{oct}} = \frac{4R}{\sqrt{3}} \implies R + r_{\text{oct}} = \frac{2R}{\sqrt{3}} \implies \frac{r_{\text{oct}}}{R} = \frac{2}{\sqrt{3}} - 1 = \mathbf{0.1547 \approx 0.155}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): BCC Tetrahedral Site Derivation</div>
      <p>Tetrahedral sites in BCC are located on cube faces at coordinates such as $(1/2, 1/4, 0)$ and $(1/4, 1/2, 0)$. Consider the site at $(a/2, a/4, 0)$:</p>
      <p>The nearest host atoms are two corner atoms at $(0,0,0)$ and $(a, 0, 0)$, and two body-centered atoms at $(a/2, a/2, a/2)$ and $(a/2, -a/2, a/2)$ (in the adjacent unit cell). The distance from $(0,0,0)$ to $(a/2, a/4, 0)$ is:</p>
      $$d^2 = \left(\frac{a}{2}\right)^2 + \left(\frac{a}{4}\right)^2 + 0^2 = \frac{a^2}{4} + \frac{a^2}{16} = \frac{5a^2}{16} \implies d = \frac{a\sqrt{5}}{4}$$
      <p>Equating this distance to $(R + r_{\text{tet}})$ and substituting $a = \frac{4R}{\sqrt{3}}$:</p>
      $$R + r_{\text{tet}} = \frac{(4R/\sqrt{3})\sqrt{5}}{4} = R\sqrt{\frac{5}{3}}$$
      $$\frac{r_{\text{tet}}}{R} = \sqrt{\frac{5}{3}} - 1 = \sqrt{1.6667} - 1 = 1.2910 - 1 = \mathbf{0.291}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Total Sites per Host Atom in BCC</div>
      <ul>
        <li><strong>Octahedral:</strong> $(6 \text{ faces} \times 1/2) + (12 \text{ edges} \times 1/4) = 3 + 3 = 6$ sites/cell. Since $n = 2$ atoms/cell:
        $$\frac{6}{2} = \mathbf{3 \text{ octahedral sites per host atom}}$$</li>
        <li><strong>Tetrahedral:</strong> 4 sites on each of the 6 faces: $4 \times 6 \times (1/2) = 12$ sites/cell:
        $$\frac{12}{2} = \mathbf{6 \text{ tetrahedral sites per host atom}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Physical Reason for Octahedral Preference</div>
      <p>Although the tetrahedral site is mathematically larger ($0.291 R > 0.155 R$), an interstitial carbon atom ($r_{\text{C}} = 0.57 R$) is larger than <em>both</em> sites. Inserting carbon into a tetrahedral site requires displacing <strong>all four coordinating atoms</strong> radially outward. In the octahedral site, the 4 planar atoms are already far away ($0.707 a = 1.63 R$), so carbon only needs to displace the <strong>two nearest-neighbor atoms</strong> along one cube axis. Displacing 2 atoms requires less total elastic work than displacing 4 atoms. Therefore, carbon resides in the octahedral site, producing the uniaxial tetragonal distortion responsible for Snoek damping and the high hardness of martensite.</p>
    </div>
    <div class="final-answer-box">
      <strong>BCC Interstitial Sizes:</strong> $r_{\text{oct}} = \mathbf{0.155 R}$, $r_{\text{tet}} = \mathbf{0.291 R}$.<br>
      <strong>Site Abundances:</strong> 3 Octahedral &bull; 6 Tetrahedral sites per host atom.<br>
      Carbon chooses octahedral sites because displacing 2 nearest atoms involves less elastic strain energy than displacing 4 atoms.
    </div>""")

# P12: Composition Conversion Weight to Atomic Percent
add(12, "Composition Conversion: Weight Percent to Atomic Percent Derivation and Calculation",
    "Solid Solutions & Solubility", "solid_solutions", "Fundamental",
    r"""<p>Engineering chemical compositions are typically specified in weight percent ($wt\%$), whereas crystallographic and chemical models operate in atomic percent ($at\%$).</p>
    <ol type="a">
      <li>Derive the general equation converting weight percentages ($C_1, C_2$) of a binary alloy into atomic percentage ($C_1'$):
      $$C_1' = \frac{C_1 A_2}{C_1 A_2 + C_2 A_1} \times 100\%$$
      where $A_1$ and $A_2$ are the atomic weights of components 1 and 2.</li>
      <li>Cartridge brass contains $70.0 \text{ wt}\%$ Copper ($\text{Cu}$, $A_{\text{Cu}} = 63.55 \text{ g/mol}$) and $30.0 \text{ wt}\%$ Zinc ($\text{Zn}$, $A_{\text{Zn}} = 65.38 \text{ g/mol}$). Calculate the atomic percentages of $\text{Cu}$ and $\text{Zn}$.</li>
      <li>Explain why the atomic percentage of Copper is higher than its weight percentage.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Derivation</div>
      <p>Consider a standard basis mass of $100 \text{ g}$ of the binary alloy. The mass of each component is $m_1 = C_1 \text{ g}$ and $m_2 = C_2 \text{ g}$.</p>
      <p>The number of moles of each component is:</p>
      $$n_1 = \frac{m_1}{A_1} = \frac{C_1}{A_1}, \quad n_2 = \frac{m_2}{A_2} = \frac{C_2}{A_2}$$
      <p>The total moles in the system is $n_{\text{total}} = n_1 + n_2 = \frac{C_1}{A_1} + \frac{C_2}{A_2}$.</p>
      <p>By definition, atomic percentage is the mole fraction expressed as a percent:</p>
      $$C_1' = \frac{n_1}{n_1 + n_2} \times 100\% = \frac{\frac{C_1}{A_1}}{\frac{C_1}{A_1} + \frac{C_2}{A_2}} \times 100\%$$
      <p>Multiplying the numerator and denominator by $(A_1 A_2)$:</p>
      $$C_1' = \frac{C_1 A_2}{C_1 A_2 + C_2 A_1} \times 100\%$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation for Cartridge Brass ($70\text{ wt}\%\text{ Cu}, 30\text{ wt}\%\text{ Zn}$)</div>
      <p>Using $C_{\text{Cu}} = 70.0, A_{\text{Cu}} = 63.55 \text{ g/mol}$, $C_{\text{Zn}} = 30.0, A_{\text{Zn}} = 65.38 \text{ g/mol}$:</p>
      $$n_{\text{Cu}} = \frac{70.0}{63.55} = 1.1015 \text{ moles}$$
      $$n_{\text{Zn}} = \frac{30.0}{65.38} = 0.4589 \text{ moles}$$
      $$n_{\text{total}} = 1.1015 + 0.4589 = 1.5604 \text{ moles}$$
      $$C_{\text{Cu}}' = \frac{1.1015}{1.5604} \times 100\% = \mathbf{70.59 \text{ at}\%}$$
      $$C_{\text{Zn}}' = \frac{0.4589}{1.5604} \times 100\% = \mathbf{29.41 \text{ at}\%}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Physical Reason for Percentage Shift</div>
      <p>Copper has a lighter atomic weight ($63.55 \text{ g/mol}$) than Zinc ($65.38 \text{ g/mol}$). Consequently, for a given mass, there are more moles (and thus more individual atoms) of copper per gram than zinc. As a general rule, the lighter element always gains numerical percentage when converting from weight percent to atomic percent.</p>
    </div>
    <div class="final-answer-box">
      <strong>Conversion Formula:</strong> $$C_1' = \frac{C_1 A_2}{C_1 A_2 + C_2 A_1} \times 100\%$$
      <strong>Cartridge Brass:</strong> $C_{\text{Cu}}' = \mathbf{70.59 \text{ at}\%}$, $C_{\text{Zn}}' = \mathbf{29.41 \text{ at}\%}$.
    </div>""")

# P13: Composition Conversion Atomic to Weight Percent
add(13, "Composition Conversion: Atomic Percent to Weight Percent Derivation and Calculation",
    "Solid Solutions & Solubility", "solid_solutions", "Fundamental",
    r"""<p>Phase diagrams and theoretical crystallographic calculations often specify alloy formulations in atomic percent ($at\%$).</p>
    <ol type="a">
      <li>Derive the reverse conversion equation calculating weight percentage ($C_1$) from atomic percentages ($C_1', C_2'$):
      $$C_1 = \frac{C_1' A_1}{C_1' A_1 + C_2' A_2} \times 100\%$$</li>
      <li>An advanced aerospace titanium alloy consists of $85.0 \text{ at}\%$ Titanium ($\text{Ti}$, $A_{\text{Ti}} = 47.87 \text{ g/mol}$) and $15.0 \text{ at}\%$ Aluminum ($\text{Al}$, $A_{\text{Al}} = 26.98 \text{ g/mol}$). Calculate the weight percentages of $\text{Ti}$ and $\text{Al}$.</li>
      <li>Determine the average atomic weight $\bar{A}$ of this binary alloy.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Mathematical Derivation</div>
      <p>Consider a basis of $100 \text{ moles}$ of the alloy. The number of moles of each component is $n_1 = C_1'$ and $n_2 = C_2'$.</p>
      <p>The mass of each component is $m_1 = n_1 A_1 = C_1' A_1$ and $m_2 = n_2 A_2 = C_2' A_2$.</p>
      <p>The total alloy mass is $m_{\text{total}} = C_1' A_1 + C_2' A_2$.</p>
      <p>The weight percent is the mass fraction multiplied by 100%:</p>
      $$C_1 = \frac{m_1}{m_{\text{total}}} \times 100\% = \frac{C_1' A_1}{C_1' A_1 + C_2' A_2} \times 100\%$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation for Ti-15 at% Al</div>
      <p>Given $C_{\text{Ti}}' = 85.0, A_{\text{Ti}} = 47.87 \text{ g/mol}$ and $C_{\text{Al}}' = 15.0, A_{\text{Al}} = 26.98 \text{ g/mol}$:</p>
      $$m_{\text{Ti}} = 85.0 \times 47.87 = 4068.95 \text{ g}$$
      $$m_{\text{Al}} = 15.0 \times 26.98 = 404.70 \text{ g}$$
      $$m_{\text{total}} = 4068.95 + 404.70 = 4473.65 \text{ g}$$
      $$C_{\text{Ti}} = \frac{4068.95}{4473.65} \times 100\% = \mathbf{90.95 \text{ wt}\%}$$
      $$C_{\text{Al}} = \frac{404.70}{4473.65} \times 100\% = \mathbf{9.05 \text{ wt}\%}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Average Atomic Weight $\bar{A}$</div>
      $$\bar{A} = \frac{C_{\text{Ti}}' A_{\text{Ti}} + C_{\text{Al}}' A_{\text{Al}}}{100} = \frac{4473.65}{100} = \mathbf{44.74 \text{ g/mol}}$$
      <p>Alternatively, from weight percent: $\bar{A} = \frac{100}{\frac{C_{\text{Ti}}}{A_{\text{Ti}}} + \frac{C_{\text{Al}}}{A_{\text{Al}}}} = \frac{100}{\frac{90.95}{47.87} + \frac{9.05}{26.98}} = \frac{100}{1.900 + 0.335} = \frac{100}{2.235} = \mathbf{44.74 \text{ g/mol}}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Conversion Formula:</strong> $$C_1 = \frac{C_1' A_1}{C_1' A_1 + C_2' A_2} \times 100\%$$
      <strong>Alloy Composition:</strong> $C_{\text{Ti}} = \mathbf{90.95 \text{ wt}\%}$, $C_{\text{Al}} = \mathbf{9.05 \text{ wt}\%}$.<br>
      <strong>Average Atomic Weight:</strong> $\bar{A} = \mathbf{44.74 \text{ g/mol}}$.
    </div>""")

# P14: Composition Conversion Mass per Unit Volume
add(14, "Composition Conversion: Volumetric Concentration and Atom Density Calculation",
    "Solid Solutions & Solubility", "solid_solutions", "Intermediate",
    r"""<p>For diffusion calculations and radiation damage models, composition must be expressed as concentration per unit volume ($C_1''$ in $\text{kg/m}^3$) or atom density ($N_1$ in $\text{atoms/cm}^3$).</p>
    <ol type="a">
      <li>Derive the formula for mass concentration of element 1 per unit volume ($C_1''$ in $\text{g/cm}^3$) in a binary alloy as a function of weight percentages ($C_1, C_2$) and elemental mass densities ($\rho_1, \rho_2$):
      $$C_1'' = \frac{C_1}{\frac{C_1}{\rho_1} + \frac{C_2}{\rho_2}}$$</li>
      <li>Derive the formula for average alloy mass density $\bar{\rho}_{\text{ave}}$.</li>
      <li>A plain low-carbon steel contains $0.20 \text{ wt}\%$ Carbon ($\text{C}$, $A_{\text{C}} = 12.01 \text{ g/mol}$, $\rho_{\text{C}} = 2.25 \text{ g/cm}^3$) and $99.80 \text{ wt}\%$ Iron ($\text{Fe}$, $A_{\text{Fe}} = 55.85 \text{ g/mol}$, $\rho_{\text{Fe}} = 7.87 \text{ g/cm}^3$). Calculate:
        <ul>
          <li>The mass concentration of carbon $C_{\text{C}}''$ in $\text{kg/m}^3$.</li>
          <li>The number of carbon atoms per cubic centimeter ($N_{\text{C}}$ in $\text{atoms/cm}^3$).</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Volumetric Concentration and Density Derivations</div>
      <p>Consider $100 \text{ g}$ of alloy. The total volume $V_{\text{total}}$ occupied by $100 \text{ g}$ is the sum of the volumes of its constituents (assuming zero excess volume of mixing):</p>
      $$V_{\text{total}} = V_1 + V_2 = \frac{m_1}{\rho_1} + \frac{m_2}{\rho_2} = \frac{C_1}{\rho_1} + \frac{C_2}{\rho_2}$$
      <p>The mass concentration of component 1 per unit volume is:</p>
      $$C_1'' = \frac{m_1}{V_{\text{total}}} = \frac{C_1}{\frac{C_1}{\rho_1} + \frac{C_2}{\rho_2}} \quad [\text{g/cm}^3]$$
      <p>The average mass density of the alloy is:</p>
      $$\bar{\rho}_{\text{ave}} = \frac{m_{\text{total}}}{V_{\text{total}}} = \frac{100}{\frac{C_1}{\rho_1} + \frac{C_2}{\rho_2}} \quad [\text{g/cm}^3]$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for $0.20 \text{ wt}\%$ Carbon Steel</div>
      <p>Given $C_{\text{C}} = 0.20, \rho_{\text{C}} = 2.25 \text{ g/cm}^3$, $C_{\text{Fe}} = 99.80, \rho_{\text{Fe}} = 7.87 \text{ g/cm}^3$:</p>
      $$\frac{C_{\text{C}}}{\rho_{\text{C}}} = \frac{0.20}{2.25} = 0.08889 \text{ cm}^3$$
      $$\frac{C_{\text{Fe}}}{\rho_{\text{Fe}}} = \frac{99.80}{7.87} = 12.68107 \text{ cm}^3$$
      $$V_{\text{total}} = 0.08889 + 12.68107 = 12.76996 \text{ cm}^3$$
      <p>The average density of the steel is:</p>
      $$\bar{\rho} = \frac{100}{12.770} = 7.8309 \text{ g/cm}^3 = 7831 \text{ kg/m}^3$$
      <p>The mass concentration of carbon per unit volume is:</p>
      $$C_{\text{C}}'' = \frac{0.20 \text{ g}}{12.770 \text{ cm}^3} = 0.01566 \text{ g/cm}^3 = \mathbf{15.66 \text{ kg/m}^3}$$
      <p>The number density of carbon atoms ($N_{\text{C}}$) is:</p>
      $$N_{\text{C}} = \frac{C_{\text{C}}'' N_A}{A_{\text{C}}} = \frac{(0.01566 \text{ g/cm}^3) \times (6.022 \times 10^{23} \text{ atoms/mol})}{12.01 \text{ g/mol}} = \mathbf{7.85 \times 10^{20} \text{ atoms/cm}^3}$$
    </div>
    <div class="final-answer-box">
      <strong>Carbon Mass Concentration:</strong> $C_{\text{C}}'' = \mathbf{15.66 \text{ kg/m}^3}$<br>
      <strong>Carbon Atom Density:</strong> $N_{\text{C}} = \mathbf{7.85 \times 10^{20} \text{ atoms/cm}^3}$ ($\approx 7.85 \times 10^{26} \text{ atoms/m}^3$).
    </div>""")

# P15: Ternary Alloy Composition Conversion
add(15, "Ternary Alloy Composition Conversion: AISI 304 Stainless Steel ($wt\\%$ to $at\\%$)",
    "Solid Solutions & Solubility", "solid_solutions", "Intermediate",
    r"""<p>AISI 304 austenitic stainless steel is the most widely utilized corrosion-resistant engineering alloy, specified nominally as $18.0 \text{ wt}\%$ Chromium, $8.0 \text{ wt}\%$ Nickel, and balance Iron.</p>
    <div style="text-align:center; margin: 10px 0;">
      Atomic Weights: $A_{\text{Cr}} = 52.00 \text{ g/mol}$, $A_{\text{Ni}} = 58.69 \text{ g/mol}$, $A_{\text{Fe}} = 55.85 \text{ g/mol}$
    </div>
    <ol type="a">
      <li>Write down the general extension of the atomic percent conversion formula for a multicomponent alloy containing $k$ elements:
      $$C_i' = \frac{C_i / A_i}{\sum_{j=1}^k (C_j / A_j)} \times 100\%$$</li>
      <li>Calculate the atomic percentages of $\text{Cr}$, $\text{Ni}$, and $\text{Fe}$ in AISI 304 stainless steel.</li>
      <li>Calculate the mean atomic weight $\bar{A}$ of AISI 304 stainless steel.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Conversion Calculations for AISI 304</div>
      <p>Nominal composition by weight: $C_{\text{Cr}} = 18.0 \text{ wt}\%$, $C_{\text{Ni}} = 8.0 \text{ wt}\%$, $C_{\text{Fe}} = 100 - (18.0 + 8.0) = 74.0 \text{ wt}\%$.</p>
      <p>Basis: $100 \text{ g}$ of alloy. Calculate moles of each element:</p>
      $$n_{\text{Cr}} = \frac{18.0 \text{ g}}{52.00 \text{ g/mol}} = 0.34615 \text{ mol}$$
      $$n_{\text{Ni}} = \frac{8.0 \text{ g}}{58.69 \text{ g/mol}} = 0.13631 \text{ mol}$$
      $$n_{\text{Fe}} = \frac{74.0 \text{ g}}{55.85 \text{ g/mol}} = 1.32498 \text{ mol}$$
      <p>Total moles:</p>
      $$n_{\text{total}} = 0.34615 + 0.13631 + 1.32498 = 1.80744 \text{ mol}$$
      <p>Compute atomic percentages:</p>
      $$C_{\text{Cr}}' = \frac{0.34615}{1.80744} \times 100\% = \mathbf{19.15 \text{ at}\%}$$
      $$C_{\text{Ni}}' = \frac{0.13631}{1.80744} \times 100\% = \mathbf{7.54 \text{ at}\%}$$
      $$C_{\text{Fe}}' = \frac{1.32498}{1.80744} \times 100\% = \mathbf{73.31 \text{ at}\%}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Mean Atomic Weight $\bar{A}$</div>
      $$\bar{A} = \frac{m_{\text{total}}}{n_{\text{total}}} = \frac{100 \text{ g}}{1.80744 \text{ mol}} = \mathbf{55.33 \text{ g/mol}}$$
      <p>Verification: $\bar{A} = \frac{19.15(52.00) + 7.54(58.69) + 73.31(55.85)}{100} = \frac{995.8 + 442.5 + 4094.4}{100} = \mathbf{55.33 \text{ g/mol}}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Atomic Composition:</strong> $C_{\text{Cr}}' = \mathbf{19.15 \text{ at}\%}$, $C_{\text{Ni}}' = \mathbf{7.54 \text{ at}\%}$, $C_{\text{Fe}}' = \mathbf{73.31 \text{ at}\%}$.<br>
      <strong>Mean Atomic Weight:</strong> $\bar{A} = \mathbf{55.33 \text{ g/mol}}$.
    </div>""")

# P16: Point Defects in Ionic Ceramics Electroneutrality
add(16, "Point Defects in Ionic Ceramics: The Electroneutrality Principle",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Fundamental",
    r"""<p>Unlike pure metals, point defects in ionic ceramics cannot be created in arbitrary isolation. The lattice must preserve macroscopic electrical neutrality at all times.</p>
    <ol type="a">
      <li>State the <strong>electroneutrality condition</strong> for an ionic crystal containing point defects.</li>
      <li>Explain why creating an isolated cation vacancy ($\text{V}_{\text{M}}''$) in Magnesium Oxide ($\text{MgO}$) without any compensating defect is thermodynamically impossible.</li>
      <li>List the two primary stoichiometric defect pairs that maintain electroneutrality in pure intrinsic ceramic crystals.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Electroneutrality Condition</div>
      <p>In any macroscopic volume of an ionic crystal, the total quantity of positive electrical charges must exactly equal the total quantity of negative electrical charges:</p>
      $$\sum_i z_i [C_i] = \sum_j z_j [A_j]$$
      <p>Expressed in terms of defect effective charges (relative to the neutral perfect lattice):</p>
      $$\sum q_{\text{eff}} \cdot [D_{\text{pos}}] = \sum |q_{\text{eff}}| \cdot [D_{\text{neg}}]$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Impossibility of Isolated Cation Vacancies in $\text{MgO}$</div>
      <p>A neutral magnesium site holds a $\text{Mg}^{2+}$ cation. If a $\text{Mg}^{2+}$ ion is removed, the vacant site has an effective negative charge of $-2$ relative to the neutral background lattice ($\text{V}_{\text{Mg}}''$). If $1 \text{ mol}$ of isolated $\text{Mg}^{2+}$ vacancies were created without compensating positive charges, the crystal would accumulate $-2 \times 96485 \text{ C} \approx -1.93 \times 10^5 \text{ C}$ of net electrostatic charge. The Coulombic electrostatic self-repulsion energy of such uncompensated charge is billions of times higher than chemical bond energies, instantly causing the crystal to explode mechanically. Consequently, point defects in ceramics must always form as electrically neutral complementary clusters or paired defect reactions.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Intrinsic Stoichiometric Defect Pairs</div>
      <ol>
        <li><strong>Frenkel Defect:</strong> A vacancy-interstitial pair of the same ion (typically the smaller cation).</li>
        <li><strong>Schottky Defect:</strong> A stoichiometric pair of cation and anion vacancies.</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>Electroneutrality Rule:</strong> Total positive effective charges must balance total negative effective charges.<br>
      Isolated charged defects are precluded by massive Coulomb electrostatic repulsion energy.<br>
      <strong>Intrinsic Pairs:</strong> <strong>Frenkel pairs</strong> (vacancy + interstitial) and <strong>Schottky pairs</strong> (cation vacancy + anion vacancy).
    </div>""")

# P17: Frenkel Defect
add(17, "The Frenkel Defect: Displaced Ion Interstitial-Vacancy Pair in Silver Halides",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Intermediate",
    r"""<p>The Frenkel defect, discovered by Soviet physicist Yakov Frenkel in 1926, is a prominent intrinsic point defect in ionic crystals where cation and anion sizes differ substantially.</p>
    <ol type="a">
      <li>Define a <strong>Frenkel defect</strong> and sketch its atomic configuration in an ionic lattice.</li>
      <li>Why do Frenkel defects almost universally involve the displacement of <strong>cations</strong> rather than <strong>anions</strong>? Under what exceptional circumstance could an anion Frenkel defect occur?</li>
      <li>Silver Chloride ($\text{AgCl}$) exhibits predominant Frenkel defects ($r_{\text{Ag}^+} = 0.126 \text{ nm}, r_{\text{Cl}^-} = 0.181 \text{ nm}$). Explain how Frenkel defects explain the exceptionally high ionic conductivity of $\text{AgCl}$ and its historical role in photographic emulsions.</li>
      <li>Does the formation of Frenkel defects alter the macroscopic density or stoichiometry of the crystal? Explain.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition of Frenkel Defect</div>
      <p>A Frenkel defect is an intrinsic point defect consisting of a <strong>cation vacancy paired with a cation interstitial</strong>. An ion leaves its normal crystallographic lattice site (leaving behind a vacant site) and squeezes into a nearby interstitial position.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Why Cations Form Interstitials</div>
      <p>In almost all ionic compounds, cations are significantly smaller than anions ($r_{\text{cation}} \ll r_{\text{anion}}$) because cations have lost their outermost valence shell while anions have expanded their electron cloud. Interstitial voids between the large close-packed anions are small. The elastic strain energy required to squeeze an ion into an interstitial void is proportional to $(r_{\text{ion}} / r_{\text{void}})^3$. The small cation can fit into interstitial spaces with moderate strain, whereas the colossal anion would require prohibitively immense strain energy.</p>
      <p><em>Exception (Anti-Frenkel Defect):</em> In fluorite-structured crystals (e.g., $\text{CaF}_2, \text{UO}_2$), the lattice has a very open framework with large empty interstitial cages, and the $\text{F}^-$ or $\text{O}^{2-}$ anions can form anion interstitials (anion Frenkel defects).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): High Ionic Conductivity of $\text{AgCl}$</div>
      <p>In $\text{AgCl}$, $\text{Ag}^+$ ions have high polarizability ($4d^{10}$ shell). The formation energy of $\text{Ag}^+$ Frenkel defects is remarkably low ($\sim 1.1 \text{ eV}$). Thermally excited $\text{Ag}^+$ interstitials migrate rapidly through interstitial channels via an interstitialcy (knock-on) mechanism with very low activation energy ($0.15 \text{ eV}$), providing remarkably high electrical conductivity carried purely by silver ions. In photography, photogenerated electrons trap at defects to reduce mobile $\text{Ag}^+$ interstitials into metallic silver sub-nanometer clusters, forming the latent photographic image.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Effect on Stoichiometry and Bulk Density</div>
      <ul>
        <li><strong>Stoichiometry:</strong> Unchanged. The ratio of cations to anions remains exactly $1:1$ because no ions leave the crystal.</li>
        <li><strong>Bulk Density:</strong> Unchanged. The total mass of the crystal is strictly conserved, and the overall volume of the crystal remains virtually identical (minor local dilation around interstitials is offset by vacancy relaxation).</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Frenkel Defect:</strong> Cation vacancy + Cation interstitial pair.<br>
      Cations form interstitials because $r_{\text{cation}} \ll r_{\text{anion}}$, minimizing elastic strain energy.<br>
      <strong>Stoichiometry & Density:</strong> Perfectly conserved (internal ion relocation).
    </div>""")

# P18: Schottky Defect
add(18, "The Schottky Defect: Stoichiometric Vacancy Pairs in Alkali Halides and Oxides",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Intermediate",
    r"""<p>The Schottky defect, discovered by Walter Schottky in 1935, is the dominant point defect in ionic solids where cations and anions have comparable ionic radii.</p>
    <ol type="a">
      <li>Define a <strong>Schottky defect</strong> and state the stoichiometric ratio of vacancies required in:
        <ul>
          <li>Sodium Chloride ($\text{NaCl}$, $1:1$ stoichiometry).</li>
          <li>Calcium Fluoride ($\text{CaF}_2$, $1:2$ stoichiometry).</li>
          <li>Alumina ($\text{Al}_2\text{O}_3$, $2:3$ stoichiometry).</li>
        </ul>
      </li>
      <li>Contrast the effect of Schottky defects versus Frenkel defects on the macroscopic mass density of a crystal.</li>
      <li>Explain why alkali halides (e.g., $\text{NaCl}, \text{KCl}$) favor Schottky defects over Frenkel defects ($r_{\text{Na}^+} = 0.102 \text{ nm}, r_{\text{Cl}^-} = 0.181 \text{ nm}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Definition of Schottky Defect and Stoichiometric Ratios</div>
      <p>A Schottky defect consists of a stoichiometric ratio of <strong>cation vacancies and anion vacancies</strong>. To maintain electroneutrality, ions are removed from their regular internal lattice sites in exact proportion to the chemical formula and deposited onto the external crystal surface:</p>
      <ul>
        <li><strong>In $\text{NaCl}$ ($1:1$):</strong> 1 $\text{Na}^+$ vacancy paired with 1 $\text{Cl}^-$ vacancy.</li>
        <li><strong>In $\text{CaF}_2$ ($1:2$):</strong> 1 $\text{Ca}^{2+}$ vacancy paired with 2 $\text{F}^-$ vacancies.</li>
        <li><strong>In $\text{Al}_2\text{O}_3$ ($2:3$):</strong> 2 $\text{Al}^{3+}$ vacancies paired with 3 $\text{O}^{2-}$ vacancies.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Effect on Macroscopic Density</div>
      <ul>
        <li><strong>Schottky Defects:</strong> Ions migrate from the interior of the crystal to build new unit cells at the external surface. The mass of the crystal is conserved, but the external volume of the crystal increases by the volume of the newly created vacant sites. Therefore, <strong>Schottky defects measurably decrease macroscopic mass density</strong> ($\rho_{\text{meas}} < \rho_{\text{ideal}}$).</li>
        <li><strong>Frenkel Defects:</strong> Ions remain trapped inside the crystal interior within existing interstitial spaces. Volume change is negligible, so <strong>density remains constant</strong>.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Why Alkali Halides Favor Schottky Defects</div>
      <p>In $\text{NaCl}$, the ionic radius ratio is $r_{\text{Na}^+} / r_{\text{Cl}^-} = 0.102 / 0.181 = 0.564$. The $\text{Na}^+$ cation is relatively large—far too large to fit into tetrahedral interstitial voids ($r_{\text{tet}} \approx 0.041 \text{ nm}$) without catastrophic elastic strain. Squeezing a $\text{Na}^+$ ion into an interstitial space to create a Frenkel defect requires $\Delta H_{\text{Frenkel}} \approx 3.0\text{--}4.0 \text{ eV}$. Creating a Schottky pair requires only $\Delta H_{\text{Schottky}} \approx 2.3 \text{ eV}$. Because the formation enthalpy is significantly lower, Schottky defect concentration dominates by many orders of magnitude.</p>
    </div>
    <div class="final-answer-box">
      <strong>Schottky Defect:</strong> Cation vacancy + Anion vacancy stoichiometric group.<br>
      <strong>Density:</strong> Decreases macroscopic density (creates internal empty volume while building new surface layers).<br>
      Favored in $\text{NaCl}$ because cations are too large to fit into interstitial sites without severe strain.
    </div>""")

# P19: Schottky Defect Equilibrium Concentration Derivation
add(19, "Thermodynamics of Schottky Defects: Derivation of Equilibrium Concentration",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Advanced",
    r"""<p>The statistical thermodynamics of paired defects in ionic crystals differs from elemental vacancies because defects are formed in correlated pairs.</p>
    <ol type="a">
      <li>Derive the equilibrium concentration equation for Schottky defects in an $AX$ crystal ($\text{NaCl}$ type):
      $$n_s = N \exp\left(-\frac{\Delta H_s}{2 k_B T}\right)$$
      where $N$ is the number of cation (or anion) lattice sites, and $\Delta H_s$ is the enthalpy required to form one complete Schottky pair. Explain the origin of the <strong>factor of 2</strong> in the denominator.</li>
      <li>In $\text{NaCl}$, the formation enthalpy of a Schottky defect is $\Delta H_s = 2.30 \text{ eV}$. Calculate the fraction of Schottky pairs $n_s/N$ at:
        <ul>
          <li>Room temperature ($T = 300 \text{ K}$).</li>
          <li>Near the melting point ($T = 1000 \text{ K}$).</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Thermodynamic Derivation of Schottky Concentration</div>
      <p>Consider an $AX$ crystal containing $N$ cation sites and $N$ anion sites. Let $n_s$ be the number of Schottky pairs formed (meaning there are $n_s$ cation vacancies and $n_s$ anion vacancies).</p>
      <p>The enthalpy of formation is $\Delta H = n_s \Delta H_s$.</p>
      <p>The number of ways to distribute $n_s$ cation vacancies among $N$ cation sites is $\Omega_c = \frac{N!}{(N - n_s)! n_s!}$.</p>
      <p>The number of ways to distribute $n_s$ anion vacancies among $N$ anion sites is $\Omega_a = \frac{N!}{(N - n_s)! n_s!}$.</p>
      <p>Because cation and anion sublattices are independent, the total configurational multiplicity is:</p>
      $$\Omega_{\text{total}} = \Omega_c \times \Omega_a = \left[ \frac{N!}{(N - n_s)! n_s!} \right]^2$$
      <p>The configurational entropy is:</p>
      $$\Delta S_{\text{conf}} = k_B \ln \Omega_{\text{total}} = 2 k_B \ln\left[ \frac{N!}{(N - n_s)! n_s!} \right]$$
      <p>Applying Stirling's approximation ($\ln N! \approx N\ln N - N$):</p>
      $$\Delta S_{\text{conf}} \approx 2 k_B \left[ N\ln N - (N - n_s)\ln(N - n_s) - n_s\ln n_s \right]$$
      <p>The Gibbs free energy of the crystal is:</p>
      $$\Delta G = n_s \Delta H_s - 2 k_B T \left[ N\ln N - (N - n_s)\ln(N - n_s) - n_s\ln n_s \right]$$
      <p>Minimizing $\Delta G$ with respect to $n_s$: $\frac{\partial \Delta G}{\partial n_s} = 0$:</p>
      $$\frac{\partial \Delta G}{\partial n_s} = \Delta H_s - 2 k_B T \left[ \ln(N - n_s) + 1 - (\ln n_s + 1) \right] = 0$$
      $$\Delta H_s - 2 k_B T \ln\left(\frac{N - n_s}{n_s}\right) = 0 \implies \ln\left(\frac{N}{n_s}\right) \approx \frac{\Delta H_s}{2 k_B T}$$
      $$\frac{n_s}{N} = \exp\left(-\frac{\Delta H_s}{2 k_B T}\right)$$
      <p><strong>Physical Origin of the Factor 2:</strong> Creating one Schottky defect creates <em>two</em> distinct non-interacting vacant sites on two separate sublattices. Each vacancy contributes independently to configurational entropy, doubling the total entropic gain ($\Delta S \propto 2$), which introduces the factor of 2 in the denominator exponent.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculations for $\text{NaCl}$ ($\Delta H_s = 2.30 \text{ eV}$)</div>
      <ul>
        <li><strong>At Room Temperature ($T = 300 \text{ K}$):</strong>
          $$2 k_B T = 2 \times (8.617 \times 10^{-5} \text{ eV/K}) \times (300 \text{ K}) = 0.05170 \text{ eV}$$
          $$\frac{n_s}{N} = \exp\left(-\frac{2.30 \text{ eV}}{0.05170 \text{ eV}}\right) = \exp(-44.487) = \mathbf{4.79 \times 10^{-20}}$$
        </li>
        <li><strong>At Elevated Temperature ($T = 1000 \text{ K}$):</strong>
          $$2 k_B T = 2 \times (8.617 \times 10^{-5} \text{ eV/K}) \times (1000 \text{ K}) = 0.17234 \text{ eV}$$
          $$\frac{n_s}{N} = \exp\left(-\frac{2.30 \text{ eV}}{0.17234 \text{ eV}}\right) = \exp(-13.3457) = \mathbf{1.60 \times 10^{-6}}$$
        </li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Schottky Equilibrium Equation:</strong> $$\frac{n_s}{N} = \exp\left(-\frac{\Delta H_s}{2 k_B T}\right)$$
      <strong>Factor 2:</strong> Originates from the simultaneous entropy of two independent sublattices.<br>
      <strong>Concentrations:</strong> $n_s/N(300 \text{ K}) = \mathbf{4.8 \times 10^{-20}}$, $n_s/N(1000 \text{ K}) = \mathbf{1.6 \times 10^{-6}}$.
    </div>""")

# P20: Non-Stoichiometry in Wüstite Fe(1-x)O
add(20, "Non-Stoichiometric Ceramic Defects: Cation Deficit and Valence Balancing in Wüstite ($\\text{Fe}_{1-x}\\text{O}$)",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Advanced",
    r"""<p>Wüstite ($\text{Fe}_{1-x}\text{O}$) is a classic non-stoichiometric oxide that is never precisely stoichiometric ($x = 0$ is thermodynamically unstable). It exists over a wide stability range with $0.05 \le x \le 0.15$ at $1000^\circ\text{C}$.</p>
    <ol type="a">
      <li>Explain the electronic and atomic defect mechanism that accommodates the deficit of iron cations ($x$) in $\text{Fe}_{1-x}\text{O}$.</li>
      <li>Derive the relationship between the fraction of iron ions in the ferric state ($\text{Fe}^{3+}$) and the non-stoichiometry parameter $x$.</li>
      <li>A chemical assay of a wüstite sample determines $x = 0.080$ ($\text{Fe}_{0.920}\text{O}$). Calculate:
        <ul>
          <li>The percentage of total iron sites that are vacant.</li>
          <li>The fraction and percentage of iron atoms present as $\text{Fe}^{3+}$.</li>
          <li>The fraction and percentage of iron atoms present as $\text{Fe}^{2+}$.</li>
        </ul>
      </li>
      <li>Explain why wüstite exhibits exceptionally high $p$-type electronic electrical conductivity via polaron electron hole hopping.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Defect Mechanism of Non-Stoichiometric $\text{Fe}_{1-x}\text{O}$</div>
      <p>The oxygen sublattice in wüstite remains completely filled and stoichiometric, with every oxygen site carrying an $\text{O}^{2-}$ anion. The deficit of iron corresponds to vacant iron cation sites ($\text{V}_{\text{Fe}}''$, effective charge $-2$). To balance the $-2$ charge of each iron vacancy and maintain macroscopic electroneutrality, two neighboring $\text{Fe}^{2+}$ cations must oxidize to $\text{Fe}^{3+}$ (ferric ions, each carrying an effective positive charge of $+1$: $\text{Fe}_{\text{Fe}}^\bullet$). Thus, for every 1 cation vacancy, exactly 2 $\text{Fe}^{3+}$ ions are created:</p>
      $$\text{Defect Ratio: } 1 \text{ V}_{\text{Fe}}'' \iff 2 \text{ Fe}_{\text{Fe}}^\bullet$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Derivation of Ferric Fraction as a Function of $x$</div>
      <p>Consider the chemical formula $\text{Fe}_{1-x}\text{O}$. The crystal contains 1.0 mole of $\text{O}^{2-}$ anions (total negative charge $= -2.0$).</p>
      <p>Let $y$ be the fraction of iron atoms that are $\text{Fe}^{3+}$, so $(1-y)$ is the fraction of $\text{Fe}^{2+}$. The total moles of iron is $(1-x)$.</p>
      <p>The total positive charge from iron cations is:</p>
      $$Q_+ = 3 \cdot y(1-x) + 2 \cdot (1-y)(1-x) = (1-x)[3y + 2 - 2y] = (1-x)(2 + y)$$
      <p>Equating positive and negative charges ($Q_+ = 2$):</p>
      $$(1-x)(2 + y) = 2 \implies 2 + y = \frac{2}{1-x} \implies y = \frac{2}{1-x} - 2 = \frac{2 - 2(1-x)}{1-x} = \frac{2x}{1-x}$$
      <p>Therefore, the fraction of iron ions in the $\text{Fe}^{3+}$ state is:</p>
      $$\text{Fraction of }\text{Fe}^{3+} = \frac{2x}{1-x}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for $x = 0.080$ ($\text{Fe}_{0.920}\text{O}$)</div>
      <ul>
        <li><strong>Percentage of Vacant Iron Sites:</strong>
          There are $0.920$ Fe atoms for every $1.000$ ideal Fe sites.
          $$\% \text{ Vacant Sites} = \frac{1.000 - 0.920}{1.000} \times 100\% = \mathbf{8.00\%}$$
        </li>
        <li><strong>Fraction and Percentage of $\text{Fe}^{3+}$:</strong>
          $$y = \frac{2(0.080)}{1 - 0.080} = \frac{0.160}{0.920} = \mathbf{0.1739 \implies 17.39\%}$$
        </li>
        <li><strong>Fraction and Percentage of $\text{Fe}^{2+}$:</strong>
          $$1 - y = 1 - 0.1739 = \mathbf{0.8261 \implies 82.61\%}$$
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): $p$-Type Electrical Conduction Mechanism</div>
      <p>An $\text{Fe}^{3+}$ ion on an $\text{Fe}^{2+}$ lattice site can be viewed as an $\text{Fe}^{2+}$ ion that has captured an electron hole ($h^\bullet$). When a small electric field is applied, an electron from an adjacent $\text{Fe}^{2+}$ ion tunnels to the $\text{Fe}^{3+}$ ion. This transfers the ferric state to the neighboring site, effectively causing the electron hole $h^\bullet$ to hop through the cation sublattice. Because $17.4\%$ of the iron sites contain electron holes, wüstite behaves as an extrinsic, defect-dominated <strong>$p$-type semiconductor</strong> with high electronic conductivity ($\sigma \approx 10^2 \text{ S/m}$).</p>
    </div>
    <div class="final-answer-box">
      <strong>Electroneutrality Rule:</strong> $1 \text{ V}_{\text{Fe}}''$ is charge-compensated by $2 \text{ Fe}_{\text{Fe}}^\bullet$ ($\text{Fe}^{3+}$).<br>
      <strong>For $\text{Fe}_{0.92}\text{O}$:</strong> Vacant Cation Sites = $\mathbf{8.00\%}$, $\text{Fe}^{3+} = \mathbf{17.39\%}$, $\text{Fe}^{2+} = \mathbf{82.61\%}$.<br>
      <strong>Conduction:</strong> High $p$-type conductivity via small-polaron hole hopping between $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$.
    </div>""")

# Save checkpoint for part 1 (1 to 20)
print("Part 1: P1-P20 appended successfully.")
# P21: Aliovalent Solute Doping in Halides (CaCl2 in NaCl)
add(21, "Aliovalent Solute Incorporation: Calcium Doping in Sodium Chloride",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Intermediate",
    r"""<p>When an aliovalent impurity (an ion with a valence different from the host ion it replaces) dissolves into an ionic crystal, extrinsic point defects are created to maintain electroneutrality.</p>
    <ol type="a">
      <li>Explain what occurs when divalent Calcium Chloride ($\text{CaCl}_2$) dissolves substitutionally into monovalent Sodium Chloride ($\text{NaCl}$).</li>
      <li>Write the defect incorporation reaction showing whether cation vacancies or anion interstitials are created.</li>
      <li>Calculate the number of sodium vacancies ($\text{V}_{\text{Na}}'$) created when $0.15 \text{ mol}\%$ of $\text{CaCl}_2$ is dissolved in $1.0 \text{ mole}$ of $\text{NaCl}$.</li>
      <li>How does this aliovalent doping affect the ionic conductivity of $\text{NaCl}$ at intermediate temperatures ($200\text{--}400^\circ\text{C}$)?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Mechanism and Defect Reaction</div>
      <p>When $\text{CaCl}_2$ dissolves into $\text{NaCl}$:</p>
      <ul>
        <li>Each $\text{Ca}^{2+}$ cation substitutes for a $\text{Na}^+$ host cation. Because $\text{Ca}^{2+}$ has a $+2$ charge and the normal site has $+1$, the defect has an effective positive charge of $+1$: $\text{Ca}_{\text{Na}}^\bullet$.</li>
        <li>The two associated $\text{Cl}^-$ anions occupy regular anion lattice sites ($\text{Cl}_{\text{Cl}}^\times$), requiring two anion sites.</li>
        <li>To maintain the $1:1$ site ratio of the rock-salt lattice and satisfy macroscopic electroneutrality, an unoccupied $\text{Na}^+$ cation site must be created. This vacant sodium site carries an effective negative charge of $-1$: $\text{V}_{\text{Na}}'$.</li>
      </ul>
      <p>In Kröger-Vink notation:</p>
      $$\text{CaCl}_2 \xrightarrow{\text{NaCl}} \text{Ca}_{\text{Na}}^\bullet + \text{V}_{\text{Na}}' + 2\text{Cl}_{\text{Cl}}^\times$$
      <p>Therefore, for every $\text{Ca}^{2+}$ ion incorporated, exactly <strong>one sodium vacancy ($\text{V}_{\text{Na}}'$)</strong> is formed.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Vacancy Count Calculation</div>
      <p>Given $0.15 \text{ mol}\%$ $\text{CaCl}_2$ in $1.0 \text{ mole}$ of $\text{NaCl}$:</p>
      $$n_{\text{Ca}} = 0.0015 \text{ mol}$$
      <p>Because each $\text{Ca}^{2+}$ produces one $\text{V}_{\text{Na}}'$:</p>
      $$n(\text{V}_{\text{Na}}') = 0.0015 \text{ mol}$$
      <p>Number of sodium vacancies:</p>
      $$N(\text{V}_{\text{Na}}') = (0.0015 \text{ mol}) \times (6.022 \times 10^{23} \text{ vacancies/mol}) = \mathbf{9.033 \times 10^{20} \text{ vacancies}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Effect on Ionic Conductivity</div>
      <p>In intrinsic $\text{NaCl}$ at intermediate temperatures ($T < 500^\circ\text{C}$), thermal Schottky vacancy concentration is negligible ($< 10^{-10}$). However, doping with $0.15 \text{ mol}\% \text{ CaCl}_2$ fixes the extrinsic vacancy concentration at a constant, temperature-independent value of $1.5 \times 10^{-3}$. Because $\text{Na}^+$ ionic conduction proceeds via vacancy hopping, having an extrinsic vacancy population that is millions of times higher than the intrinsic level increases the ionic conductivity of $\text{NaCl}$ by several orders of magnitude in the extrinsic regime.</p>
    </div>
    <div class="final-answer-box">
      <strong>Defect Reaction:</strong> $$\text{CaCl}_2 \xrightarrow{\text{NaCl}} \text{Ca}_{\text{Na}}^\bullet + \text{V}_{\text{Na}}' + 2\text{Cl}_{\text{Cl}}^\times$$
      <strong>Vacancies Created:</strong> $N(\text{V}_{\text{Na}}') = \mathbf{9.03 \times 10^{20} \text{ vacancies/mol}}$.<br>
      <strong>Conductivity:</strong> Increases by $10^4\text{--}10^6\times$ in the extrinsic regime via vacancy-assisted $\text{Na}^+$ migration.
    </div>""")

# P22: Oxygen Ion Conductors: Yttria-Stabilized Zirconia (YSZ)
add(22, "Fast Oxygen Ion Conduction in Yttria-Stabilized Zirconia (YSZ)",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Advanced",
    r"""<p>Yttria-Stabilized Zirconia ($\text{YSZ}$) is the premier solid electrolyte membrane utilized in Solid Oxide Fuel Cells (SOFCs) and automotive exhaust oxygen sensors ($\lambda$-sensors).</p>
    <ol type="a">
      <li>Explain why pure Zirconia ($\text{ZrO}_2$) undergoes catastrophic mechanical shattering during thermal cycling between room temperature and $1200^\circ\text{C}$.</li>
      <li>Write the defect incorporation reaction in Kröger-Vink notation for dissolving trivalent Yttria ($\text{Y}_2\text{O}_3$) into tetravalent Zirconia ($\text{ZrO}_2$).</li>
      <li>For an 8 mol% $\text{Y}_2\text{O}_3$ stabilized zirconia ($8\text{YSZ}$, composition $(0.08 \text{ Y}_2\text{O}_3)_{0.08} (\text{ZrO}_2)_{0.92}$):
        <ul>
          <li>Calculate the percentage of oxygen lattice sites that are vacant.</li>
          <li>Calculate the volumetric concentration of oxygen vacancies in $8\text{YSZ}$ ($\rho \approx 6.0 \text{ g/cm}^3$, fluorite lattice parameter $a = 0.514 \text{ nm}$).</li>
        </ul>
      </li>
      <li>Explain the microscopic mechanism of fast oxygen ion conduction across the solid electrolyte membrane at $800^\circ\text{C}$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Thermal Shock Shattering of Pure $\text{ZrO}_2$</div>
      <p>Pure zirconia undergoes a polymorphic phase transition upon cooling from the tetragonal phase to the monoclinic phase at $\sim 950\text{--}1170^\circ\text{C}$. This martensitic phase change involves a colossal discontinuous <strong>volumetric expansion of $\sim 3\text{--}5\%$</strong> and large shear strain ($7\%$). In unconstrained bulk ceramics, the severe internal transformation stresses exceed the fracture strength, causing immediate catastrophic shattering and fragmentation. Doping with $\text{Y}_2\text{O}_3$ stabilizes the high-symmetry cubic fluorite phase down to room temperature, preventing destructive phase transformations.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Kröger-Vink Defect Reaction</div>
      <p>Trivalent $\text{Y}^{3+}$ replaces tetravalent $\text{Zr}^{4+}$ on the cation sublattice. Each $\text{Y}^{3+}$ carries an effective negative charge of $-1$: $\text{Y}_{\text{Zr}}'$. Dissolving one formula unit of $\text{Y}_2\text{O}_3$ introduces two $\text{Y}_{\text{Zr}}'$ defects (total charge $-2$). To preserve electroneutrality, one oxygen site must remain vacant. An oxygen vacancy carries an effective positive charge of $+2$: $\text{V}_{\text{O}}^{\bullet\bullet}$:</p>
      $$\text{Y}_2\text{O}_3 \xrightarrow{\text{ZrO}_2} 2\text{Y}_{\text{Zr}}' + \text{V}_{\text{O}}^{\bullet\bullet} + 3\text{O}_{\text{O}}^\times$$
      <p>Thus, for every <strong>two $\text{Y}^{3+}$ ions</strong>, exactly <strong>one oxygen vacancy ($\text{V}_{\text{O}}^{\bullet\bullet}$)</strong> is generated.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Quantitative Calculation of Oxygen Vacancy Fraction</div>
      <p>Consider a batch containing $0.08 \text{ mol}$ of $\text{Y}_2\text{O}_3$ and $0.92 \text{ mol}$ of $\text{ZrO}_2$:</p>
      <ul>
        <li>Moles of $\text{Y}^{3+}$ cations: $n_{\text{Y}} = 2 \times 0.08 = 0.16 \text{ mol}$.</li>
        <li>Moles of $\text{Zr}^{4+}$ cations: $n_{\text{Zr}} = 0.92 \text{ mol}$.</li>
        <li>Total cation sites: $N_{\text{cation}} = 0.16 + 0.92 = 1.08 \text{ mol}$.</li>
        <li>In the cubic fluorite structure ($\text{MO}_2$), there are exactly 2 anion sites for every 1 cation site:
        $$N_{\text{anion sites}} = 2 \times N_{\text{cation}} = 2 \times 1.08 = 2.16 \text{ mol of oxygen sites}$$</li>
        <li>Moles of oxygen vacancies formed:
        $$n(\text{V}_{\text{O}}^{\bullet\bullet}) = \frac{1}{2} n_{\text{Y}} = 0.08 \text{ mol}$$</li>
        <li><strong>Percentage of Vacant Oxygen Sites:</strong>
        $$\% \text{ Vacant Sites} = \frac{0.08 \text{ mol}}{2.16 \text{ mol}} \times 100\% = \mathbf{3.704\%}$$
        Roughly 1 in every 27 oxygen sites in $8\text{YSZ}$ is completely empty!</li>
      </ul>
      <p>In the cubic fluorite unit cell ($a = 0.514 \text{ nm} = 5.14 \times 10^{-8} \text{ cm}$), there are 8 oxygen sites per cell. The number of vacancies per unit cell is $8 \times 0.03704 = 0.2963$ vacancies/cell. The unit cell volume is $V_c = (5.14 \times 10^{-8} \text{ cm})^3 = 1.358 \times 10^{-22} \text{ cm}^3$.</p>
      $$N_{\text{vac}} = \frac{0.2963}{1.358 \times 10^{-22} \text{ cm}^3} = \mathbf{2.18 \times 10^{21} \text{ vacancies/cm}^3 = 2.18 \times 10^{27} \text{ m}^{-3}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Microscopic Fast Conduction Mechanism</div>
      <p>At operating temperatures of $700\text{--}900^\circ\text{C}$, thermal energy allows $\text{O}^{2-}$ anions to hop rapidly into adjacent oxygen vacancies ($\text{V}_{\text{O}}^{\bullet\bullet}$). Because the concentration of vacancies is enormous ($3.7\%$) and the open fluorite framework provides interconnected channels with low migration barriers ($E_m \approx 0.8\text{--}0.9 \text{ eV}$), $8\text{YSZ}$ displays high ionic conductivity ($\sigma_i \approx 0.1 \text{ S/cm}$) while remaining an electronic insulator ($t_{\text{ion}} > 0.99$), making it an ideal fuel cell electrolyte.</p>
    </div>
    <div class="final-answer-box">
      <strong>Defect Equation:</strong> $$\text{Y}_2\text{O}_3 \xrightarrow{\text{ZrO}_2} 2\text{Y}_{\text{Zr}}' + \text{V}_{\text{O}}^{\bullet\bullet} + 3\text{O}_{\text{O}}^\times$$
      <strong>Oxygen Vacancies:</strong> $\mathbf{3.70\%}$ of all oxygen sites ($\mathbf{2.18 \times 10^{21} \text{ vacancies/cm}^3}$).<br>
      High ionic conductivity at $800^\circ\text{C}$ is enabled by rapid $\text{O}^{2-}$ hopping into the vast network of extrinsic vacancies.
    </div>""")

# P23: Kröger-Vink Notation Rules
add(23, "Kröger-Vink Defect Notation: Systematic Rules and Site Balancing Principles",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Fundamental",
    r"""<p>The Kröger-Vink defect notation is the universally accepted IUPAC standard for representing point defects, charge states, and quasi-chemical defect reactions in crystalline solids.</p>
    <ol type="a">
      <li>Explain the systematic structure of a Kröger-Vink symbol:
      $$\mathbf{M}_{\mathbf{S}}^{\mathbf{C}}$$
      defining what the main letter ($\mathbf{M}$), subscript ($\mathbf{S}$), and superscript ($\mathbf{C}$) signify.</li>
      <li>Define the three standard effective charge symbols:
        <ul>
          <li>Cross ($\times$)</li>
          <li>Dot ($\bullet$)</li>
          <li>Prime ($'$)</li>
        </ul>
        Explain how effective charge differs from formal chemical valence.</li>
      <li>State the three fundamental balance rules that must be satisfied by every valid Kröger-Vink quasi-chemical reaction.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Anatomy of a Kröger-Vink Defect Symbol ($\text{M}_{\text{S}}^{\text{C}}$)</div>
      <ul>
        <li><strong>Main Letter ($\text{M}$ - The Entity):</strong> Indicates what species is physically present at the site. Can be an element symbol (e.g., $\text{Al}, \text{Fe}, \text{O}$), a vacancy symbol ($\text{V}$), or an electronic carrier ($e$ for electron, $h$ for electron hole).</li>
        <li><strong>Subscript ($\text{S}$ - The Site):</strong> Indicates the crystallographic lattice site occupied by the entity. Can be a normal lattice site (e.g., $\text{Na}, \text{Cl}, \text{O}, \text{Fe}$) or an interstitial void site ($i$).</li>
        <li><strong>Superscript ($\text{C}$ - The Effective Charge):</strong> Indicates the net electrical charge of the defect <em>relative to the perfect, unperturbed host lattice</em>.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Effective Charge vs. Formal Valence</div>
      <p>Effective charge is defined as: $q_{\text{eff}} = q_{\text{entity}} - q_{\text{site}}$.</p>
      <ul>
        <li><strong>Cross ($\times$):</strong> Effective charge is zero (neutral relative to the perfect crystal). Example: $\text{Na}_{\text{Na}}^\times$ (a $\text{Na}^+$ ion on a $+1$ sodium site: $+1 - (+1) = 0$).</li>
        <li><strong>Dot ($\bullet$):</strong> One unit of positive effective charge ($+1$). Example: $\text{V}_{\text{O}}^{\bullet\bullet}$ (missing $\text{O}^{2-}$ from a $-2$ site has effective charge $0 - (-2) = +2$, written with two dots).</li>
        <li><strong>Prime ($'$):</strong> One unit of negative effective charge ($-1$). Example: $\text{V}_{\text{Na}}'$ (missing $\text{Na}^+$ from a $+1$ site has effective charge $0 - (+1) = -1$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): The Three Fundamental Reaction Balance Rules</div>
      <ol>
        <li><strong>Mass / Conservation of Matter:</strong> The total number of atoms of each chemical element must balance between the left-hand and right-hand sides of the equation. (Vacancies $\text{V}$ have zero mass).</li>
        <li><strong>Electroneutrality / Conservation of Effective Charge:</strong> The algebraic sum of effective charges on the left side must equal the sum on the right side: $\sum q_{\text{eff, reactants}} = \sum q_{\text{eff, products}}$.</li>
        <li><strong>Site Ratio Conservation:</strong> The ratio of cation sites to anion sites in the crystal lattice is strictly fixed by the parent crystal structure (e.g., $1:1$ for $\text{NaCl}$, $1:2$ for $\text{TiO}_2$). Cation and anion lattice sites can only be created or destroyed in proportion to the structural stoichiometry.</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>Kröger-Vink Anatomy:</strong> $\text{Entity}_{\text{Site}}^{\text{Effective Charge}}$<br>
      <strong>Effective Charge:</strong> $\bullet = +1$, $' = -1$, $\times = 0$ (relative to neutral perfect lattice).<br>
      <strong>Balance Laws:</strong> 1. Mass conservation &bull; 2. Effective charge neutrality &bull; 3. Cation-to-anion site ratio preservation.
    </div>""")

# P24: Kröger-Vink Defect Reactions Practice
add(24, "Writing and Balancing Kröger-Vink Defect Equations",
    "Ceramic Defects & Kröger-Vink", "ceramic_defects", "Advanced",
    r"""<p>Apply the principles of Kröger-Vink notation to write balanced defect equations for fundamental thermodynamic and oxidation processes.</p>
    <ol type="a">
      <li>Write the balanced Kröger-Vink reaction for:
        <ul>
          <li>Formation of a <strong>Schottky defect pair</strong> in Magnesium Oxide ($\text{MgO}$).</li>
          <li>Formation of a <strong>Frenkel defect pair</strong> on the cation sublattice of Zinc Oxide ($\text{ZnO}$).</li>
          <li>Formation of an <strong>anion Frenkel defect</strong> in Calcium Fluoride ($\text{CaF}_2$).</li>
        </ul>
      </li>
      <li>Write the defect incorporation reaction for dissolving Alumina ($\text{Al}_2\text{O}_3$) substitutionally into Magnesium Oxide ($\text{MgO}$), assuming cation vacancies charge-compensate.</li>
      <li>Write the high-temperature oxidation reaction of Nickel Oxide ($\text{NiO}$) where oxygen from air ($\text{O}_2\text{(g)}$) incorporates into the lattice, creating cation vacancies and electron holes.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Intrinsic Defect Reactions</div>
      <ul>
        <li><strong>Schottky Pair in $\text{MgO}$ ($1:1$ site ratio):</strong>
        $$\text{null} \rightleftharpoons \text{V}_{\text{Mg}}'' + \text{V}_{\text{O}}^{\bullet\bullet}$$
        <em>Checks:</em> Mass conserved (zero atoms). Charge: $(-2) + (+2) = 0$. Sites: 1 Mg site + 1 O site ($1:1$).</li>
        <li><strong>Cation Frenkel in $\text{ZnO}$:</strong>
        $$\text{Zn}_{\text{Zn}}^\times \rightleftharpoons \text{V}_{\text{Zn}}'' + \text{Zn}_i^{\bullet\bullet}$$
        <em>Checks:</em> Mass: 1 Zn on each side. Charge: $0 = (-2) + (+2)$. Sites: 1 Zn site conserved.</li>
        <li><strong>Anion Frenkel in $\text{CaF}_2$:</strong>
        $$\text{F}_{\text{F}}^\times \rightleftharpoons \text{V}_{\text{F}}^\bullet + \text{F}_i'$$
        <em>Checks:</em> Charge: $0 = (+1) + (-1)$. Mass: 1 F atom. Sites: 1 F site conserved.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Doping $\text{Al}_2\text{O}_3$ into $\text{MgO}$</div>
      <p>Two $\text{Al}^{3+}$ cations substitute for $\text{Mg}^{2+}$ cations: $2\text{Al}_{\text{Mg}}^\bullet$ (total $+2$ charge). Three $\text{O}^{2-}$ anions enter oxygen sites: $3\text{O}_{\text{O}}^\times$. To balance charge and site ratio, one magnesium vacancy ($\text{V}_{\text{Mg}}''$) is created:</p>
      $$\text{Al}_2\text{O}_3 \xrightarrow{\text{MgO}} 2\text{Al}_{\text{Mg}}^\bullet + \text{V}_{\text{Mg}}'' + 3\text{O}_{\text{O}}^\times$$
      <p><em>Site Check:</em> 2 Al sites + 1 V site = 3 Mg sites. Oxygen sites = 3. Cation-to-anion site ratio is $3:3 = 1:1$, preserving the rock-salt structure!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): High-Temperature Oxidation of $\text{NiO}$</div>
      <p>Gaseous oxygen incorporates onto newly formed oxygen sites: $\frac{1}{2}\text{O}_2\text{(g)} \to \text{O}_{\text{O}}^\times$. A matching nickel vacancy is created: $\text{V}_{\text{Ni}}''$. Electroneutrality is maintained by oxidizing two $\text{Ni}^{2+}$ to $\text{Ni}^{3+}$, represented as two electron holes ($2h^\bullet$):</p>
      $$\frac{1}{2}\text{O}_2\text{(g)} \rightleftharpoons \text{O}_{\text{O}}^\times + \text{V}_{\text{Ni}}'' + 2h^\bullet$$
      <p>This reaction proves why $\text{NiO}$ behaves as a $p$-type semiconductor under high oxygen partial pressures.</p>
    </div>
    <div class="final-answer-box">
      <strong>$\text{MgO}$ Schottky:</strong> $\text{null} \rightleftharpoons \text{V}_{\text{Mg}}'' + \text{V}_{\text{O}}^{\bullet\bullet}$<br>
      <strong>$\text{Al}_2\text{O}_3$ in $\text{MgO}$:</strong> $\text{Al}_2\text{O}_3 \to 2\text{Al}_{\text{Mg}}^\bullet + \text{V}_{\text{Mg}}'' + 3\text{O}_{\text{O}}^\times$<br>
      <strong>$\text{NiO}$ Oxidation:</strong> $\frac{1}{2}\text{O}_2\text{(g)} \rightleftharpoons \text{O}_{\text{O}}^\times + \text{V}_{\text{Ni}}'' + 2h^\bullet$.
    </div>""")

# P25: Line Defects Discovery and Theoretical Shear Strength Paradox
add(25, "1D Line Defects: Theoretical Shear Strength Paradox and the Discovery of Dislocations",
    "Linear Defects & Dislocations", "dislocations", "Fundamental",
    r"""<p>In the 1920s, theoretical calculations by Frenkel predicted that defect-free ideal crystals should possess immense shear strengths, yet experimental single crystals yielded at stresses three to four orders of magnitude lower.</p>
    <ol type="a">
      <li>Using Frenkel's sinusoidal atomic shear model, derive the theoretical shear strength of a perfect crystal:
      $$\tau_{\text{theor}} \approx \frac{G}{2\pi} \approx \frac{G}{10}\text{ to }\frac{G}{30}$$
      where $G$ is the shear modulus.</li>
      <li>For pure copper ($G = 48 \text{ GPa}$), calculate $\tau_{\text{theor}}$ and compare it with the measured critical resolved shear stress of real copper single crystals ($\tau_{\text{CRSS}} \approx 0.5 \text{ MPa}$). Compute the discrepancy ratio.</li>
      <li>Explain the conceptual breakthrough proposed simultaneously in 1934 by Orowan, Polanyi, and Taylor that resolved this theoretical strength paradox.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Frenkel's Theoretical Shear Strength Derivation</div>
      <p>Consider two adjacent parallel atomic planes separated by spacing $d$, with repeat distance $b$ along the shear direction. As the top plane is sheared by displacement $x$ relative to the bottom plane, the restoring shear stress must be periodic with period $b$, satisfying:</p>
      $$\tau(x) = \tau_{\max} \sin\left(\frac{2\pi x}{b}\right)$$
      <p>For small elastic displacements ($x \ll b$), Hooke's law must hold: $\tau = G\gamma = G\left(\frac{x}{d}\right)$.</p>
      <p>Using the small-angle approximation $\sin\theta \approx \theta$:</p>
      $$\tau(x) \approx \tau_{\max} \left(\frac{2\pi x}{b}\right) = G\left(\frac{x}{d}\right)$$
      $$\tau_{\max} = \frac{G}{2\pi}\left(\frac{b}{d}\right)$$
      <p>Since the repeat distance $b$ is roughly equal to planar spacing $d$ ($b/d \approx 1$):</p>
      $$\tau_{\text{theor}} = \tau_{\max} \approx \frac{G}{2\pi} \approx \frac{G}{6.28} \approx \mathbf{\frac{G}{10}\text{ to }\frac{G}{30}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Discrepancy Calculation for Copper ($G = 48 \text{ GPa}$)</div>
      $$\tau_{\text{theor}} \approx \frac{48 \times 10^9 \text{ Pa}}{2\pi} \approx 7.64 \times 10^9 \text{ Pa} = \mathbf{7640 \text{ MPa}}$$
      <p>The experimental yield strength of high-purity single-crystal copper is only $\tau_{\text{CRSS}} \approx 0.5 \text{ MPa}$.</p>
      $$\text{Discrepancy Ratio} = \frac{\tau_{\text{theor}}}{\tau_{\text{exp}}} = \frac{7640 \text{ MPa}}{0.5 \text{ MPa}} = \mathbf{15,280 \approx 10^4}$$
      <p>Real metals deform plastically at stresses <strong>10,000 to 100,000 times lower</strong> than the theoretical strength of a perfect lattice!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Resolution by Orowan, Polanyi, and Taylor (1934)</div>
      <p>Frenkel's model assumed that simultaneous rigid shear of entire atomic planes occurs all at once across the entire slip plane (breaking millions of bonds simultaneously). Orowan, Polanyi, and G. I. Taylor independently realized that real crystals contain line defects called <strong>dislocations</strong>. Instead of shearing all bonds at once, slip occurs <em>consecutively</em>, one atomic row at a time, like moving a heavy rug across a floor by pushing a small wrinkle or caterpillar crawl. Because only a single line of bonds breaks and reforms at any instant, the required shear stress is reduced by a factor of $10,000$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Theoretical Strength:</strong> $\tau_{\text{theor}} \approx \frac{G}{2\pi} \approx \mathbf{7.6 \text{ GPa}}$ for Copper.<br>
      <strong>Experimental Strength:</strong> $\tau_{\text{exp}} \approx \mathbf{0.5 \text{ MPa}}$ (Discrepancy factor of $\sim \mathbf{15,000\times}$).<br>
      <strong>Dislocation Breakthrough:</strong> Plastic slip occurs incrementally via line defect glide (one bond row at a time) rather than simultaneous rigid plane shear.
    </div>""")

# Save checkpoint for part 1 (1 to 25)
print("Part 1: All P1-P25 completed!")
