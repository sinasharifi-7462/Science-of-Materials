# generator/make_ch5_part1.py
# ==============================================================================
# CHAPTER 5: DIFFUSION IN SOLIDS - PART 1 (PROBLEMS 1 TO 25)
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

# P1: Diffusion Mechanisms Vacancy vs Interstitial
add(1, "Atomic Mechanisms of Diffusion: Vacancy Diffusion vs. Interstitial Migration",
    "Diffusion Fundamentals", "fundamentals", "Fundamental",
    r"""<p>Diffusion is the phenomenon of material transport by atomic motion within solid crystals.</p>
    <ol type="a">
      <li>Describe the atomic mechanisms of:
        <ul>
          <li><strong>Vacancy Diffusion</strong> (Substitutional / Self-Diffusion).</li>
          <li><strong>Interstitial Diffusion</strong>.</li>
        </ul>
      </li>
      <li>Explain why the activation energy for interstitial diffusion ($Q_{\text{interstitial}} \approx 80\text{--}140 \text{ kJ/mol}$) is substantially lower than for vacancy diffusion ($Q_{\text{substitutional}} \approx 200\text{--}300 \text{ kJ/mol}$) in the same host metal.</li>
      <li>At $900^\circ\text{C}$, the diffusion coefficient of Carbon in FCC iron is $D_{\text{C}} \approx 1.5 \times 10^{-11} \text{ m}^2/\text{s}$, whereas the self-diffusion coefficient of Iron in FCC iron is $D_{\text{Fe}} \approx 2.0 \times 10^{-16} \text{ m}^2/\text{s}$. Compute the ratio $D_{\text{C}} / D_{\text{Fe}}$ and discuss its engineering significance.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Atomic Mechanisms of Diffusion</div>
      <ul>
        <li><strong>Vacancy Diffusion:</strong> Host solvent atoms or substitutional solute atoms migrate from their normal lattice sites into adjacent unoccupied vacant sites. The process requires two coordinated events: a vacancy must first be present on an adjacent neighbor site, and the migrating atom must acquire sufficient thermal vibrational energy to squeeze through surrounding atoms into that vacancy. Operates for self-diffusion and substitutional solutes (e.g., Cu, Ni, Zn).</li>
        <li><strong>Interstitial Diffusion:</strong> Small solute atoms (e.g., H, C, N, O) migrate from one interstitial void (interstice) to an adjacent unoccupied interstitial void. Because host atoms occupy lattice sites and solute concentrations are small, the vast majority of adjacent interstitial voids are empty and immediately available.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Why Interstitial Activation Energy is Much Lower ($Q_{\text{int}} \ll Q_{\text{sub}}$)</div>
      <p>The total activation energy for vacancy-mediated diffusion consists of the sum of two distinct thermodynamic energies:</p>
      $$Q_{\text{substitutional}} = \Delta H_f + \Delta H_m$$
      <p>where $\Delta H_f$ is the enthalpy to create an adjacent vacancy, and $\Delta H_m$ is the enthalpy of atomic migration.</p>
      <p>For interstitial diffusion, neighboring interstitial sites are naturally empty. No prior defect creation step is required ($\Delta H_f = 0$). Furthermore, interstitial atoms are much smaller than host atoms, so squeezing through interstitial bottlenecks requires significantly less elastic lattice distortion:</p>
      $$Q_{\text{interstitial}} = \Delta H_m \ll (\Delta H_f + \Delta H_m)$$
      <p>Consequently, interstitial diffusion proceeds with less than half the activation energy of substitutional diffusion.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Numerical Ratio at $900^\circ\text{C}$ and Engineering Consequence</div>
      $$\frac{D_{\text{C}}}{D_{\text{Fe}}} = \frac{1.5 \times 10^{-11} \text{ m}^2/\text{s}}{2.0 \times 10^{-16} \text{ m}^2/\text{s}} = \mathbf{75,000 \approx 7.5 \times 10^4}$$
      <p>Carbon diffuses roughly <strong>75,000 times faster</strong> through the iron lattice than iron atoms themselves! This enormous kinetic disparity enables rapid industrial case-hardening of steel (carburizing gears in hours at $900^\circ\text{C}$) while keeping the underlying iron grain structure intact.</p>
    </div>
    <div class="final-answer-box">
      <strong>Vacancy Mechanism:</strong> $Q = \Delta H_f + \Delta H_m$ (requires pre-existing vacancy).<br>
      <strong>Interstitial Mechanism:</strong> $Q = \Delta H_m$ only (adjacent sites are empty, smaller solute radius).<br>
      <strong>Kinetic Ratio at $900^\circ\text{C}$:</strong> Carbon diffuses $\mathbf{75,000\times}$ faster than iron in austenite.
    </div>""")

# P2: Interdiffusion vs Self-Diffusion
add(2, "Interdiffusion vs. Self-Diffusion: Tracer Diffusion and Concentration Gradients",
    "Diffusion Fundamentals", "fundamentals", "Fundamental",
    r"""<p>Diffusion processes can occur under uniform chemical composition or in the presence of chemical concentration gradients.</p>
    <ol type="a">
      <li>Differentiate between <strong>Self-Diffusion</strong> and <strong>Interdiffusion (Chemical Diffusion)</strong>.</li>
      <li>How is self-diffusion measured experimentally in the laboratory using radioactive or stable isotopes (<strong>tracer diffusion</strong>)?</li>
      <li>State the thermodynamic driving force for self-diffusion versus interdiffusion. Explain why diffusion can occasionally proceed "uphill" from lower to higher concentration (spinodal decomposition).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Self-Diffusion vs. Interdiffusion</div>
      <ul>
        <li><strong>Self-Diffusion:</strong> Atomic migration occurring in pure elemental crystals or homogeneous alloys in the absence of a chemical composition gradient. Atoms wander randomly by Brownian thermal motion; no net macroscopic mass transport occurs.</li>
        <li><strong>Interdiffusion (Chemical / Impurity Diffusion):</strong> Atomic migration occurring in a concentration gradient (e.g., across a Cu-Ni diffusion couple). Driven by chemical potential gradients, a net directional flux of solute and solvent atoms occurs to homogenize the system.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Radioactive Tracer Diffusion Technique</div>
      <p>To measure self-diffusion in pure nickel, a sub-micron film of radioactive isotope (e.g., $^{63}\text{Ni}$) is electroplated onto a polished pure nickel disc. The sample is annealed at temperature $T$ for time $t$. After cooling, thin parallel surface layers (a few micrometers thick) are sequentially shaved off using a precision lathe or microtome, and the radioactive activity of each layer is measured with a scintillation counter. Fitting the specific radioactivity profile $A(x)$ to the thin-film Gaussian solution:</p>
      $$A(x, t) = \frac{A_0}{\sqrt{\pi D t}} \exp\left(-\frac{x^2}{4Dt}\right)$$
      <p>plotting $\ln A$ versus $x^2$ gives a straight line whose slope $-\frac{1}{4Dt}$ yields the true self-diffusion coefficient $D^*$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Thermodynamic Driving Force and Uphill Diffusion</div>
      <p>The true fundamental thermodynamic driving force for all diffusion is the <strong>gradient of chemical potential $\nabla\mu_i$</strong>, not the concentration gradient $\nabla C_i$:</p>
      $$J_i = -M_i C_i \frac{\partial\mu_i}{\partial x}$$
      <p>For ideal or dilute solutions, $\mu_i = \mu_i^0 + RT \ln C_i$, giving $\frac{\partial\mu_i}{\partial x} = \frac{RT}{C_i}\frac{\partial C_i}{\partial x}$, which reduces to Fick's first law $J = -D \frac{\partial C}{\partial x}$ ("downhill" diffusion from high to low $C$).</p>
      <p>However, inside a thermodynamic miscibility gap (where $\frac{\partial^2 G}{\partial C^2} < 0$), the chemical potential gradient has the opposite sign of the concentration gradient. Atoms spontaneously diffuse from regions of low concentration toward regions of high concentration (<strong>uphill diffusion</strong>) during <strong>spinodal decomposition</strong>, phase-separating into A-rich and B-rich modulated nanostructures without nucleation.</p>
    </div>
    <div class="final-answer-box">
      <strong>Self-Diffusion:</strong> Random thermal motion in pure solids (zero net flux), measured via radioisotope tracers ($A \propto \exp(-x^2/4Dt)$).<br>
      <strong>Interdiffusion:</strong> Net directional transport in a concentration gradient.<br>
      <strong>Driving Force:</strong> Chemical potential gradient $\nabla\mu_i$. Uphill diffusion occurs when $\partial^2 G/\partial C^2 < 0$.
    </div>""")

# P3: Kirkendall Effect
add(3, "The Kirkendall Effect: Marker Shift, Asymmetric Fluxes, and Vacancy Diffusion Proof",
    "Diffusion Fundamentals", "fundamentals", "Intermediate",
    r"""<p>In 1947, Ernest Kirkendall published a landmark experiment on brass-copper diffusion couples that decisively proved the atomic mechanism of solid-state diffusion.</p>
    <ol type="a">
      <li>Describe the experimental setup of the <strong>Kirkendall experiment</strong> (materials, inert markers, and diffusion heat treatment).</li>
      <li>What was the key experimental observation regarding the position of the inert markers after high-temperature annealing?</li>
      <li>Explain how this observation proved that:
        <ul>
          <li>Zinc and copper diffuse at different intrinsic rates ($D_{\text{Zn}} > D_{\text{Cu}}$).</li>
          <li>Diffusion in metals occurs via the <strong>vacancy mechanism</strong> rather than direct ring/exchange mechanisms.</li>
        </ul>
      </li>
      <li>What structural defect forms on the zinc-rich side of the couple as a result of the unequal atomic fluxes?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Experimental Setup of the Kirkendall Experiment</div>
      <p>Ernest Kirkendall and Alice Smigelskas wrapped fine, chemically inert, insoluble molybdenum wires around a block of 70-30 brass ($70\text{ wt}\%\text{ Cu}, 30\text{ wt}\%\text{ Zn}$). They electroplated a thick layer of pure copper over the assembly, embedding the molybdenum wire markers directly at the original weld interface between brass and pure copper. The diffusion couple was then annealed at $785^\circ\text{C}$ for several weeks.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Key Experimental Observation</div>
      <p>Upon cross-sectioning and microscopic inspection, Kirkendall discovered that the inert molybdenum markers had <strong>moved inward toward the brass core</strong>. The distance between the marker wires on opposite sides had measurably decreased.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Decisive Proof of Vacancy Mechanism and Unequal Fluxes</div>
      <ol>
        <li><strong>Unequal Intrinsic Diffusion Rates ($D_{\text{Zn}} > D_{\text{Cu}}$):</strong>
          Zinc atoms (lower melting point, weaker bonds) diffuse out of the brass into the pure copper faster than copper atoms diffuse into the brass ($J_{\text{Zn}} > J_{\text{Cu}}$).
        </li>
        <li><strong>Refutation of Direct Exchange:</strong>
          If diffusion occurred by direct pairwise exchange of adjacent atoms or ring rotation, every atom of Zn moving right would require exactly one atom of Cu moving left ($J_{\text{Zn}} = J_{\text{Cu}}$). Net mass flux across the interface would be zero, and markers could never move.
        </li>
        <li><strong>Confirmation of Vacancy Mechanism:</strong>
          Because each atomic jump requires exchanging with a vacancy, the net outward atomic flux ($J_{\text{Zn}} - J_{\text{Cu}}$) must be balanced by an equal and opposite <strong>net flux of vacancies diffusing into the brass</strong>:
          $$J_v = -(J_{\text{Zn}} - J_{\text{Cu}})$$
          As excess vacancies flow into the brass, lattice planes on the brass side are destroyed by vacancy annihilation (climb of edge dislocations). On the copper side, extra lattice planes are created by vacancy emission. The entire atomic lattice shifts rigidly relative to the inert markers at velocity $v = (D_{\text{Zn}} - D_{\text{Cu}})\frac{dX_{\text{Zn}}}{dx}$.
        </li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Formation of Kirkendall Porosity</div>
      <p>When the influx of vacancies into the faster-diffusing side (brass) exceeds the rate at which edge dislocations can climb and absorb them, the vacancy population becomes supersaturated. The excess vacancies condense and coalesce into macroscopic microscopic voids, termed <strong>Kirkendall voids (porosity)</strong>. This causes embrittlement and delamination in microelectronic solder joints (e.g., Cu-Sn and Ni-Au interfaces in semiconductor packaging).</p>
    </div>
    <div class="final-answer-box">
      <strong>Kirkendall Observation:</strong> Inert markers shift toward the faster-diffusing element ($\text{Zn}$).<br>
      <strong>Scientific Proof:</strong> Proved $D_{\text{Zn}} > D_{\text{Cu}}$ and established the <strong>vacancy diffusion mechanism</strong> (refuting direct exchange).<br>
      <strong>Defect Consequence:</strong> Vacancy supersaturation produces <strong>Kirkendall porosity/voids</strong> on the faster-diffusing side.
    </div>""")

# P4: Darken's Equations
add(4, "Darken's Phenomenological Relations: Interdiffusion Coefficient $\\tilde{D}$ and Marker Velocity",
    "Diffusion Fundamentals", "fundamentals", "Advanced",
    r"""<p>In 1948, L. S. Darken mathematically unified intrinsic diffusion coefficients with the macroscopic interdiffusion coefficient and marker shift velocity.</p>
    <ol type="a">
      <li>State <strong>Darken's First Equation</strong> for the marker drift velocity $v$:
      $$v = (D_A - D_B) \frac{\partial X_A}{\partial x}$$
      where $D_A$ and $D_B$ are the intrinsic diffusion coefficients of components $A$ and $B$, and $X_A$ is the mole fraction of $A$.</li>
      <li>State <strong>Darken's Second Equation</strong> for the chemical interdiffusion coefficient $\tilde{D}$:
      $$\tilde{D} = X_B D_A + X_A D_B$$</li>
      <li>In a Cu-Ni diffusion couple annealed at $1000^\circ\text{C}$, the concentration of Nickel at the marker interface is $X_{\text{Ni}} = 0.40$ ($X_{\text{Cu}} = 0.60$) and the concentration gradient is $\frac{\partial X_{\text{Ni}}}{\partial x} = 2.5 \times 10^3 \text{ m}^{-1}$. The intrinsic diffusion coefficients are $D_{\text{Cu}} = 4.0 \times 10^{-14} \text{ m}^2/\text{s}$ and $D_{\text{Ni}} = 1.0 \times 10^{-14} \text{ m}^2/\text{s}$.
        <ul>
          <li>Calculate the interdiffusion coefficient $\tilde{D}$.</li>
          <li>Calculate the marker drift velocity $v$ in $\text{nm/s}$ and in $\mu\text{m/day}$.</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Darken's Equations</div>
      <ul>
        <li><strong>Marker Velocity Equation:</strong>
        $$v = (D_A - D_B) \frac{\partial X_A}{\partial x} = -(D_A - D_B) \frac{\partial X_B}{\partial x}$$
        where $v$ is the velocity of the inert marker frame relative to the fixed laboratory frame.</li>
        <li><strong>Chemical Interdiffusion Coefficient:</strong>
        $$\tilde{D} = X_B D_A + X_A D_B$$
        For non-ideal solutions, Darken introduced the thermodynamic factor $\Phi$:
        $$\tilde{D} = (X_B D_A + X_A D_B) \left(1 + \frac{\partial \ln \gamma_A}{\partial \ln X_A}\right)$$
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for Cu-Ni Couple at $1000^\circ\text{C}$</div>
      <p>Given $X_{\text{Cu}} = 0.60, X_{\text{Ni}} = 0.40$, $D_{\text{Cu}} = 4.0 \times 10^{-14} \text{ m}^2/\text{s}$, $D_{\text{Ni}} = 1.0 \times 10^{-14} \text{ m}^2/\text{s}$, and $\frac{\partial X_{\text{Ni}}}{\partial x} = 2.5 \times 10^3 \text{ m}^{-1}$ (meaning $\frac{\partial X_{\text{Cu}}}{\partial x} = -2.5 \times 10^3 \text{ m}^{-1}$):</p>
      <ul>
        <li><strong>Interdiffusion Coefficient $\tilde{D}$:</strong>
        $$\tilde{D} = X_{\text{Ni}} D_{\text{Cu}} + X_{\text{Cu}} D_{\text{Ni}} = (0.40 \times 4.0 \times 10^{-14}) + (0.60 \times 1.0 \times 10^{-14})$$
        $$\tilde{D} = 1.60 \times 10^{-14} + 0.60 \times 10^{-14} = \mathbf{2.20 \times 10^{-14} \text{ m}^2/\text{s}}$$
        </li>
        <li><strong>Marker Velocity $v$:</strong>
        $$v = (D_{\text{Cu}} - D_{\text{Ni}}) \left(-\frac{\partial X_{\text{Cu}}}{\partial x}\right) = (D_{\text{Cu}} - D_{\text{Ni}}) \frac{\partial X_{\text{Ni}}}{\partial x}$$
        $$v = (4.0 \times 10^{-14} - 1.0 \times 10^{-14} \text{ m}^2/\text{s}) \times (2.5 \times 10^3 \text{ m}^{-1})$$
        $$v = (3.0 \times 10^{-14}) \times (2.5 \times 10^3) = \mathbf{7.50 \times 10^{-11} \text{ m/s}}$$
        <p>Convert to $\text{nm/s}$ ($1 \text{ m} = 10^9 \text{ nm}$):</p>
        $$v = (7.50 \times 10^{-11} \text{ m/s}) \times 10^9 \text{ nm/m} = \mathbf{0.075 \text{ nm/s}}$$
        <p>Convert to $\mu\text{m/day}$ ($1 \text{ day} = 86,400 \text{ s}$, $1 \text{ m} = 10^6 \mu\text{m}$):</p>
        $$v = (7.50 \times 10^{-11} \text{ m/s}) \times (86,400 \text{ s/day}) \times 10^6 \mu\text{m/m} = \mathbf{6.48 \mu\text{m/day}}$$
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Darken's Relations:</strong> $\tilde{D} = X_B D_A + X_A D_B$, $v = (D_A - D_B)\frac{\partial X_A}{\partial x}$.<br>
      <strong>Interdiffusion Coefficient:</strong> $\tilde{D} = \mathbf{2.20 \times 10^{-14} \text{ m}^2/\text{s}}$.<br>
      <strong>Marker Velocity:</strong> $v = \mathbf{0.075 \text{ nm/s}} = \mathbf{6.48 \mu\text{m/day}}$ (inward toward Copper).
    </div>""")

# P5: Fick's First Law Steady-State Fundamentals
add(5, "Steady-State Diffusion: Fick's First Law and Physical Meaning of Flux",
    "Steady-State Diffusion (Fick I)", "fick_first_law", "Fundamental",
    r"""<p>Steady-state diffusion occurs when the concentration profile of the diffusing species does not change with time ($\frac{\partial C}{\partial t} = 0$).</p>
    <ol type="a">
      <li>State <strong>Fick's First Law</strong> of diffusion mathematically:
      $$J = -D \frac{dC}{dx}$$
      Define all four terms and state their standard SI units.</li>
      <li>Explain the physical significance of the <strong>negative sign</strong> in the equation.</li>
      <li>Distinguish between mass flux $J_m$ ($\text{kg}/(\text{m}^2\cdot\text{s})$) and atomic flux $J_{\text{at}}$ ($\text{atoms}/(\text{m}^2\cdot\text{s})$). State the conversion formula between them.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Fick's First Law and SI Units</div>
      $$J = -D \frac{dC}{dx}$$
      <ul>
        <li>$J$: <strong>Diffusion Flux</strong>. The mass (or number of atoms) traversing perpendicular to a unit cross-sectional area per unit time. SI units: $\mathbf{\text{kg}/(\text{m}^2\cdot\text{s})}$ or $\mathbf{\text{atoms}/(\text{m}^2\cdot\text{s})}$.</li>
        <li>$D$: <strong>Diffusion Coefficient (Diffusivity)</strong>. The kinetic rate constant for atomic mobility in the host lattice. SI units: $\mathbf{\text{m}^2/\text{s}}$.</li>
        <li>$C$: <strong>Concentration</strong>. The mass (or number of atoms) of solute per unit volume of host. SI units: $\mathbf{\text{kg/m}^3}$ or $\mathbf{\text{atoms/m}^3}$.</li>
        <li>$\frac{dC}{dx}$: <strong>Concentration Gradient</strong>. The spatial rate of change of concentration along direction $x$. SI units: $\frac{\text{kg/m}^3}{\text{m}} = \mathbf{\text{kg/m}^4}$ or $\mathbf{\text{atoms/m}^4}$.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Physical Meaning of the Negative Sign</div>
      <p>Diffusion is a passive, spontaneous transport process driven down a concentration gradient. If concentration decreases with increasing distance ($x$), the spatial slope $\frac{dC}{dx}$ is negative. The negative sign ensures that the resultant net flux $J$ is a positive quantity pointing in the direction of lower concentration:</p>
      $$\frac{dC}{dx} < 0 \implies J = -D \left(-\left|\frac{dC}{dx}\right|\right) > 0 \quad (\text{Net mass flows from High to Low } C)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Mass Flux vs. Atomic Flux Conversion</div>
      <p>Let $M_{\text{solute}}$ be the molar mass ($\text{kg/mol}$) and $N_A = 6.022 \times 10^{23} \text{ atoms/mol}$ be Avogadro's number:</p>
      $$J_{\text{at}} = \frac{J_m \cdot N_A}{M_{\text{solute}}} \quad \left[\frac{\text{atoms}}{\text{m}^2\cdot\text{s}}\right]$$
      $$J_m = \frac{J_{\text{at}} \cdot M_{\text{solute}}}{N_A} \quad \left[\frac{\text{kg}}{\text{m}^2\cdot\text{s}}\right]$$
    </div>
    <div class="final-answer-box">
      <strong>Fick's First Law:</strong> $$J = -D \frac{dC}{dx}$$
      Units: $J \text{ [kg/(m}^2\cdot\text{s)]}$, $D \text{ [m}^2\text{/s]}$, $\frac{dC}{dx} \text{ [kg/m}^4\text{]}$.<br>
      Negative sign enforces transport down the gradient (from high to low concentration).
    </div>""")

# Save checkpoint for part 1 (1 to 5)
print("Ch 5 Part 1: P1-P5 written.")
# P6: Hydrogen Purification through Palladium
add(6, "Steady-State Diffusion: Hydrogen Gas Purification Through a Palladium Foil",
    "Steady-State Diffusion (Fick I)", "fick_first_law", "Intermediate",
    r"""<p>Palladium metal exhibits an extraordinary ability to selectively dissolve and transport hydrogen, making it the industry standard for producing ultra-pure hydrogen gas for semiconductor manufacturing.</p>
    <ol type="a">
      <li>A palladium membrane of thickness $L = 0.20 \text{ mm}$ and cross-sectional area $A = 0.15 \text{ m}^2$ operates at $500^\circ\text{C}$. The diffusion coefficient of hydrogen in palladium at this temperature is $D = 1.6 \times 10^{-9} \text{ m}^2/\text{s}$. The dissolved hydrogen concentrations at the high-pressure and low-pressure surfaces are maintained constant at:
      $$C_A = 2.40 \text{ kg/m}^3 \quad (\text{at } x = 0), \quad C_B = 0.40 \text{ kg/m}^3 \quad (\text{at } x = L)$$
      Calculate the steady-state hydrogen concentration gradient $\frac{dC}{dx}$ through the foil.</li>
      <li>Calculate the mass diffusion flux $J$ in $\text{kg}/(\text{m}^2\cdot\text{s})$ and the atomic flux $J_{\text{at}}$ in $\text{atoms}/(\text{m}^2\cdot\text{s})$ ($M_{\text{H}} = 1.008 \text{ g/mol}$).</li>
      <li>Calculate the total mass of ultra-pure hydrogen gas purified by the membrane per hour ($\text{kg/hr}$).</li>
      <li>If the foil thickness is rolled down to $L = 0.05 \text{ mm}$, calculate the new hourly purification rate.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Steady-State Concentration Gradient</div>
      <p>Under steady-state conditions in a flat planar membrane, the concentration profile is linear:</p>
      $$\frac{dC}{dx} = \frac{C_B - C_A}{L - 0} = \frac{0.40 \text{ kg/m}^3 - 2.40 \text{ kg/m}^3}{0.20 \times 10^{-3} \text{ m}} = \frac{-2.00 \text{ kg/m}^3}{2.0 \times 10^{-4} \text{ m}} = \mathbf{-10,000 \text{ kg/m}^4}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Diffusion Flux Calculations</div>
      <p>Using Fick's First Law ($J = -D \frac{dC}{dx}$):</p>
      $$J = -(1.6 \times 10^{-9} \text{ m}^2/\text{s}) \times (-10,000 \text{ kg/m}^4) = \mathbf{1.60 \times 10^{-5} \text{ kg}/(\text{m}^2\cdot\text{s})}$$
      <p>Calculate atomic flux using $M_{\text{H}} = 1.008 \times 10^{-3} \text{ kg/mol}$:</p>
      $$J_{\text{at}} = \frac{J \cdot N_A}{M_{\text{H}}} = \frac{(1.60 \times 10^{-5} \text{ kg/m}^2\cdot\text{s}) \times (6.022 \times 10^{23} \text{ atoms/mol})}{1.008 \times 10^{-3} \text{ kg/mol}} = \mathbf{9.56 \times 10^{21} \text{ atoms}/(\text{m}^2\cdot\text{s})}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Total Purified Mass per Hour ($A = 0.15 \text{ m}^2$)</div>
      <p>The mass flow rate $\dot{m}$ through area $A$ is:</p>
      $$\dot{m} = J \times A = (1.60 \times 10^{-5} \text{ kg/m}^2\cdot\text{s}) \times (0.15 \text{ m}^2) = 2.40 \times 10^{-6} \text{ kg/s}$$
      <p>In one hour ($t = 3600 \text{ s}$):</p>
      $$m_{\text{hr}} = \dot{m} \times 3600 \text{ s} = (2.40 \times 10^{-6} \text{ kg/s}) \times 3600 \text{ s} = \mathbf{8.64 \times 10^{-3} \text{ kg/hr} = 8.64 \text{ g/hr}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Effect of Reducing Thickness to $0.05 \text{ mm}$</div>
      <p>Since flux is inversely proportional to thickness ($J \propto 1/L$):</p>
      $$\frac{L_1}{L_2} = \frac{0.20 \text{ mm}}{0.05 \text{ mm}} = 4.0$$
      $$m_{\text{hr, new}} = 4.0 \times 8.64 \text{ g/hr} = \mathbf{34.56 \text{ g/hr}}$$
      <p>Reducing membrane thickness by a factor of 4 quadruples the purification throughput without increasing temperature.</p>
    </div>
    <div class="final-answer-box">
      <strong>Gradient:</strong> $\frac{dC}{dx} = \mathbf{-10,000 \text{ kg/m}^4}$<br>
      <strong>Flux:</strong> $J = \mathbf{1.60 \times 10^{-5} \text{ kg/(m}^2\cdot\text{s)}}$, $J_{\text{at}} = \mathbf{9.56 \times 10^{21} \text{ atoms/(m}^2\cdot\text{s)}}$.<br>
      <strong>Purification Rate:</strong> $\mathbf{8.64 \text{ g/hr}}$ at $0.20\text{ mm}$ &bull; $\mathbf{34.56 \text{ g/hr}}$ at $0.05\text{ mm}$.
    </div>""")

# P7: Nitrogen Gas Diffusion Through Iron Plate
add(7, "Steady-State Nitrogen Gas Permeation Through an Industrial Iron Plate",
    "Steady-State Diffusion (Fick I)", "fick_first_law", "Intermediate",
    r"""<p>A chemical synthesis reactor contains ammonia gas at $700^\circ\text{C}$ separated from the atmosphere by an $\alpha$-iron plate of thickness $L = 5.0 \text{ mm}$.</p>
    <div style="text-align:center; margin: 10px 0;">
      Diffusion coefficient of Nitrogen in $\alpha$-iron at $700^\circ\text{C}$: $D = 4.2 \times 10^{-11} \text{ m}^2/\text{s}$<br>
      Nitrogen surface concentrations: $C_1 = 1.20 \text{ kg/m}^3$ (inside face), $C_2 = 0.10 \text{ kg/m}^3$ (outside face)
    </div>
    <ol type="a">
      <li>Calculate the steady-state diffusion flux of nitrogen through the plate.</li>
      <li>Calculate the concentration of nitrogen at a depth of $x = 2.0 \text{ mm}$ from the inside high-pressure face.</li>
      <li>If the total surface area of the plate is $A = 0.80 \text{ m}^2$, calculate the mass of nitrogen lost to the atmosphere per 24-hour day in grams.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Diffusion Flux Calculation</div>
      <p>The linear concentration gradient is:</p>
      $$\frac{dC}{dx} = \frac{C_2 - C_1}{L} = \frac{0.10 - 1.20 \text{ kg/m}^3}{5.0 \times 10^{-3} \text{ m}} = \frac{-1.10}{5.0 \times 10^{-3}} = -220 \text{ kg/m}^4$$
      <p>Using Fick's First Law:</p>
      $$J = -D \frac{dC}{dx} = -(4.2 \times 10^{-11} \text{ m}^2/\text{s}) \times (-220 \text{ kg/m}^4) = \mathbf{9.24 \times 10^{-9} \text{ kg}/(\text{m}^2\cdot\text{s})}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Concentration at Depth $x = 2.0 \text{ mm}$</div>
      <p>For steady-state 1D diffusion, concentration varies linearly with position:</p>
      $$C(x) = C_1 + \left(\frac{dC}{dx}\right) x = 1.20 \text{ kg/m}^3 + (-220 \text{ kg/m}^4) \times (2.0 \times 10^{-3} \text{ m})$$
      $$C(2.0 \text{ mm}) = 1.20 - 0.44 = \mathbf{0.76 \text{ kg/m}^3}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Total Nitrogen Loss per Day ($A = 0.80 \text{ m}^2, t = 86,400 \text{ s}$)</div>
      $$m_{\text{day}} = J \times A \times t = (9.24 \times 10^{-9} \text{ kg/m}^2\cdot\text{s}) \times (0.80 \text{ m}^2) \times (86,400 \text{ s})$$
      $$m_{\text{day}} = (7.392 \times 10^{-9} \text{ kg/s}) \times 86,400 \text{ s} = 6.387 \times 10^{-4} \text{ kg} = \mathbf{0.639 \text{ g/day}}$$
    </div>
    <div class="final-answer-box">
      <strong>Diffusion Flux:</strong> $J = \mathbf{9.24 \times 10^{-9} \text{ kg/(m}^2\cdot\text{s)}}$.<br>
      <strong>Concentration at $2\text{ mm}$:</strong> $C = \mathbf{0.76 \text{ kg/m}^3}$.<br>
      <strong>Daily Nitrogen Loss:</strong> $m_{\text{day}} = \mathbf{0.639 \text{ g/day}}$.
    </div>""")

# P8: Carbon Flux Across Carburized Plate
add(8, "Steady-State Carbon Flux in a Thin Austenitic Steel Sheet",
    "Steady-State Diffusion (Fick I)", "fick_first_law", "Intermediate",
    r"""<p>A thin sheet of low-carbon steel of thickness $1.5 \text{ mm}$ is exposed to a carburizing atmosphere on one side and a decarburizing atmosphere on the other side at $1000^\circ\text{C}$ until steady-state diffusion is achieved.</p>
    <div style="text-align:center; margin: 10px 0;">
      At $x = 0$ (carburizing face): $C_1 = 1.15 \text{ wt}\%$ Carbon<br>
      At $x = 1.5 \text{ mm}$ (decarburizing face): $C_2 = 0.25 \text{ wt}\%$ Carbon<br>
      Diffusivity of Carbon in $\gamma$-Fe at $1000^\circ\text{C}$: $D = 3.0 \times 10^{-11} \text{ m}^2/\text{s}$<br>
      Density of austenite: $\rho = 7800 \text{ kg/m}^3$
    </div>
    <ol type="a">
      <li>Convert the surface carbon concentrations from weight percent to volumetric concentrations ($C_1, C_2$ in $\text{kg/m}^3$).</li>
      <li>Calculate the carbon diffusion flux through the sheet in $\text{kg}/(\text{m}^2\cdot\text{s})$.</li>
      <li>Calculate the number of carbon atoms exiting $1.0 \text{ cm}^2$ of the decarburizing surface per second.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Volumetric Concentration Conversion</div>
      <p>Using $C [\text{kg/m}^3] = \left(\frac{\text{wt}\%}{100}\right) \times \rho_{\text{steel}}$:</p>
      $$C_1 = \left(\frac{1.15}{100}\right) \times 7800 \text{ kg/m}^3 = \mathbf{89.70 \text{ kg/m}^3}$$
      $$C_2 = \left(\frac{0.25}{100}\right) \times 7800 \text{ kg/m}^3 = \mathbf{19.50 \text{ kg/m}^3}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Diffusion Flux Calculation</div>
      <p>Thickness $L = 1.5 \text{ mm} = 1.5 \times 10^{-3} \text{ m}$:</p>
      $$\frac{dC}{dx} = \frac{C_2 - C_1}{L} = \frac{19.50 - 89.70 \text{ kg/m}^3}{1.5 \times 10^{-3} \text{ m}} = \frac{-70.20}{1.5 \times 10^{-3}} = -46,800 \text{ kg/m}^4$$
      $$J = -D \frac{dC}{dx} = -(3.0 \times 10^{-11} \text{ m}^2/\text{s}) \times (-46,800 \text{ kg/m}^4) = \mathbf{1.404 \times 10^{-6} \text{ kg}/(\text{m}^2\cdot\text{s})}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Atomic Exit Rate per $\text{cm}^2$ ($A = 1.0 \text{ cm}^2 = 1.0 \times 10^{-4} \text{ m}^2$)</div>
      <p>Mass flow rate through $1.0 \text{ cm}^2$:</p>
      $$\dot{m} = J \times A = (1.404 \times 10^{-6} \text{ kg/m}^2\cdot\text{s}) \times (1.0 \times 10^{-4} \text{ m}^2) = 1.404 \times 10^{-10} \text{ kg/s}$$
      <p>Convert to carbon atoms per second ($M_{\text{C}} = 0.012011 \text{ kg/mol}$):</p>
      $$\dot{N} = \frac{\dot{m} \cdot N_A}{M_{\text{C}}} = \frac{(1.404 \times 10^{-10} \text{ kg/s}) \times (6.022 \times 10^{23} \text{ atoms/mol})}{0.012011 \text{ kg/mol}} = \mathbf{7.04 \times 10^{15} \text{ atoms/s}}$$
    </div>
    <div class="final-answer-box">
      <strong>Volumetric Concentrations:</strong> $C_1 = \mathbf{89.7 \text{ kg/m}^3}$, $C_2 = \mathbf{19.5 \text{ kg/m}^3}$.<br>
      <strong>Carbon Flux:</strong> $J = \mathbf{1.404 \times 10^{-6} \text{ kg/(m}^2\cdot\text{s)}}$.<br>
      <strong>Exit Rate per $\text{cm}^2$:</strong> $\mathbf{7.04 \times 10^{15} \text{ atoms/s}}$.
    </div>""")

# P9: Radial Steady-State Diffusion in Cylindrical Pipe
add(9, "Radial Steady-State Diffusion: Mathematical Derivation for Cylindrical Pipe Walls",
    "Steady-State Diffusion (Fick I)", "fick_first_law", "Advanced",
    r"""<p>For cylindrical geometries (such as coolant pipes, fuel cladding tubes, or gas pipelines), diffusion occurs radially through an area that expands with radius $r$.</p>
    <ol type="a">
      <li>Starting from Fick's first law and the condition that total mass flow rate $Q = J(r) \cdot A(r)$ must be independent of radius $r$ in steady state, derive the differential equation for radial concentration $C(r)$.</li>
      <li>Integrate the differential equation to prove that the steady-state concentration profile across a pipe wall (inner radius $r_1$, outer radius $r_2$) is <strong>logarithmic</strong>:
      $$C(r) = C_1 + (C_2 - C_1) \frac{\ln(r / r_1)}{\ln(r_2 / r_1)}$$</li>
      <li>Derive the expression for the total radial mass leakage rate $Q$ per unit length of pipe ($L = 1 \text{ m}$):
      $$\frac{Q}{L} = \frac{2\pi D (C_1 - C_2)}{\ln(r_2 / r_1)}$$</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Differential Equation Formulation</div>
      <p>Consider a pipe of length $L$. At radius $r$, the cylindrical surface area through which diffusion occurs is $A(r) = 2\pi r L$.</p>
      <p>By Fick's first law, radial diffusion flux is $J(r) = -D \frac{dC}{dr}$.</p>
      <p>The total mass flow rate $Q$ across the cylindrical shell is:</p>
      $$Q = J(r) \cdot A(r) = -D \left(\frac{dC}{dr}\right) (2\pi r L) = -2\pi D L r \frac{dC}{dr}$$
      <p>In steady state with no internal sources or sinks, conservation of mass requires $Q = \text{constant}$ (independent of $r$):</p>
      $$r \frac{dC}{dr} = -\frac{Q}{2\pi D L} = \text{constant } K$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Integration for Concentration Profile $C(r)$</div>
      <p>Separating variables:</p>
      $$dC = K \frac{dr}{r} \implies C(r) = K \ln r + C_0$$
      <p>Apply boundary conditions:</p>
      <ul>
        <li>At $r = r_1$: $C(r_1) = C_1 = K \ln r_1 + C_0$</li>
        <li>At $r = r_2$: $C(r_2) = C_2 = K \ln r_2 + C_0$</li>
      </ul>
      <p>Subtracting the two equations:</p>
      $$C_2 - C_1 = K (\ln r_2 - \ln r_1) = K \ln\left(\frac{r_2}{r_1}\right) \implies K = \frac{C_2 - C_1}{\ln(r_2 / r_1)}$$
      <p>Substituting $K$ and solving for $C(r)$:</p>
      $$C(r) - C_1 = K (\ln r - \ln r_1) = K \ln\left(\frac{r}{r_1}\right) = (C_2 - C_1) \frac{\ln(r / r_1)}{\ln(r_2 / r_1)}$$
      $$C(r) = C_1 + (C_2 - C_1) \frac{\ln(r / r_1)}{\ln(r_2 / r_1)}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Total Leakage Rate per Unit Length</div>
      <p>From Part (a), $Q = -2\pi D L K$. Substituting $K = \frac{C_2 - C_1}{\ln(r_2 / r_1)}$:</p>
      $$Q = -2\pi D L \left[\frac{C_2 - C_1}{\ln(r_2 / r_1)}\right] = \frac{2\pi D L (C_1 - C_2)}{\ln(r_2 / r_1)}$$
      <p>Dividing by length $L$:</p>
      $$\frac{Q}{L} = \frac{2\pi D (C_1 - C_2)}{\ln(r_2 / r_1)}$$
    </div>
    <div class="final-answer-box">
      <strong>Radial Profile:</strong> $$C(r) = C_1 + (C_2 - C_1)\frac{\ln(r/r_1)}{\ln(r_2/r_1)}$$
      <strong>Total Radial Leakage per Meter:</strong> $$\frac{Q}{L} = \frac{2\pi D (C_1 - C_2)}{\ln(r_2/r_1)}$$
      Unlike planar walls (linear profile), cylindrical diffusion profiles are fundamentally logarithmic.
    </div>""")

# P10: Quantitative Radial Leakage in Nuclear Cladding
add(10, "Radial Steady-State Permeation: Hydrogen Leakage in Zirconium Cladding Tubes",
    "Steady-State Diffusion (Fick I)", "fick_first_law", "Intermediate",
    r"""<p>In a nuclear pressurized water reactor, fuel pellets are encased in Zircaloy-4 cladding tubes ($D_{\text{H}} = 5.0 \times 10^{-10} \text{ m}^2/\text{s}$ at $350^\circ\text{C}$). The tube dimensions and hydrogen concentrations are:</p>
    <div style="text-align:center; margin: 10px 0;">
      Inner radius $r_1 = 4.0 \text{ mm}$, Outer radius $r_2 = 4.6 \text{ mm}$<br>
      Inner concentration $C_1 = 0.50 \text{ kg/m}^3$, Outer concentration $C_2 = 0.05 \text{ kg/m}^3$
    </div>
    <ol type="a">
      <li>Calculate the hydrogen concentration at the midpoint of the cladding wall ($r_{\text{mid}} = 4.3 \text{ mm}$). Compare this with the simple arithmetic average $(C_1 + C_2)/2$.</li>
      <li>Calculate the total mass rate of hydrogen escaping per meter length of fuel rod ($\text{mg}/(\text{m}\cdot\text{day})$).</li>
      <li>Calculate the radial diffusion flux at the inner surface $J(r_1)$ and outer surface $J(r_2)$, and explain why $J(r_1) > J(r_2)$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Concentration at Midpoint ($r = 4.3 \text{ mm}$)</div>
      $$\ln\left(\frac{r_2}{r_1}\right) = \ln\left(\frac{4.6}{4.0}\right) = \ln(1.15) = 0.13976$$
      $$\ln\left(\frac{r_{\text{mid}}}{r_1}\right) = \ln\left(\frac{4.3}{4.0}\right) = \ln(1.075) = 0.07232$$
      $$C(r_{\text{mid}}) = C_1 + (C_2 - C_1)\frac{\ln(r_{\text{mid}}/r_1)}{\ln(r_2/r_1)} = 0.50 + (0.05 - 0.50) \times \left(\frac{0.07232}{0.13976}\right)$$
      $$C(r_{\text{mid}}) = 0.50 - 0.45 \times (0.51746) = 0.50 - 0.2329 = \mathbf{0.2671 \text{ kg/m}^3}$$
      <p>The simple arithmetic mean is $\frac{0.50 + 0.05}{2} = 0.2750 \text{ kg/m}^3$. The logarithmic profile is slightly lower ($0.2671$) because flux is concentrated over smaller areas at smaller radii.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Mass Rate per Meter Length</div>
      $$\frac{Q}{L} = \frac{2\pi D (C_1 - C_2)}{\ln(r_2 / r_1)} = \frac{2\pi \times (5.0 \times 10^{-10} \text{ m}^2/\text{s}) \times (0.50 - 0.05 \text{ kg/m}^3)}{0.13976}$$
      $$\frac{Q}{L} = \frac{3.1416 \times 10^{-9} \times 0.45}{0.13976} = \frac{1.4137 \times 10^{-9}}{0.13976} = 1.0115 \times 10^{-8} \text{ kg}/(\text{m}\cdot\text{s})$$
      <p>Convert to $\text{mg}/(\text{m}\cdot\text{day})$ ($1 \text{ day} = 86,400 \text{ s}$, $1 \text{ kg} = 10^6 \text{ mg}$):</p>
      $$\frac{Q}{L} = (1.0115 \times 10^{-8} \text{ kg/s}) \times (86,400 \text{ s/day}) \times 10^6 \text{ mg/kg} = \mathbf{873.9 \text{ mg}/(\text{m}\cdot\text{day})}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Flux at Inner vs. Outer Surfaces</div>
      <p>Using $J(r) = \frac{Q/L}{2\pi r}$:</p>
      <ul>
        <li><strong>At $r_1 = 4.0 \times 10^{-3} \text{ m}$:</strong>
        $$J(r_1) = \frac{1.0115 \times 10^{-8}}{2\pi \times (4.0 \times 10^{-3})} = \frac{1.0115 \times 10^{-8}}{0.02513} = \mathbf{4.025 \times 10^{-7} \text{ kg}/(\text{m}^2\cdot\text{s})}$$</li>
        <li><strong>At $r_2 = 4.6 \times 10^{-3} \text{ m}$:</strong>
        $$J(r_2) = \frac{1.0115 \times 10^{-8}}{2\pi \times (4.6 \times 10^{-3})} = \frac{1.0115 \times 10^{-8}}{0.02890} = \mathbf{3.500 \times 10^{-7} \text{ kg}/(\text{m}^2\cdot\text{s})}$$</li>
      </ul>
      <p><em>Physical Explanation:</em> To maintain constant total mass flow rate $Q$, flux times area must be constant ($J_1 A_1 = J_2 A_2$). Because the outer area is $15\%$ larger than the inner area ($A_2 / A_1 = 4.6 / 4.0 = 1.15$), the outer flux is reduced by exactly $1/1.15 = 0.87\times$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Midpoint Concentration:</strong> $C(4.3\text{ mm}) = \mathbf{0.267 \text{ kg/m}^3}$.<br>
      <strong>Daily Leakage:</strong> $\frac{Q}{L} = \mathbf{874 \text{ mg}/(\text{m}\cdot\text{day})}$.<br>
      <strong>Fluxes:</strong> $J(r_1) = \mathbf{4.03 \times 10^{-7} \text{ kg/(m}^2\cdot\text{s)}}$, $J(r_2) = \mathbf{3.50 \times 10^{-7} \text{ kg/(m}^2\cdot\text{s)}}$ ($J_1 r_1 = J_2 r_2$).
    </div>""")

# P11: Derivation of Fick's Second Law
add(11, "Non-Steady-State Diffusion: Derivation of Fick's Second Law from Mass Continuity",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Advanced",
    r"""<p>In most real-world engineering processes (carburizing, oxidation, heat treatment), concentration varies with both position and time: $C = C(x, t)$.</p>
    <ol type="a">
      <li>Consider a thin planar volume element of thickness $\Delta x$ and cross-sectional area $A$ oriented perpendicular to the diffusion direction $x$. Using the principle of conservation of mass (Rate of Accumulation = Influx - Outflux), derive the 1D <strong>continuity equation</strong>:
      $$\frac{\partial C}{\partial t} = -\frac{\partial J}{\partial x}$$</li>
      <li>Substitute Fick's first law into the continuity equation to derive the general non-steady-state diffusion equation:
      $$\frac{\partial C}{\partial t} = \frac{\partial}{\partial x}\left(D \frac{\partial C}{\partial x}\right)$$</li>
      <li>State <strong>Fick's Second Law</strong> for the special case where diffusivity $D$ is independent of concentration and position:
      $$\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}$$</li>
      <li>Under what physical conditions does diffusivity $D$ depend strongly on concentration, rendering the constant-$D$ assumption invalid?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation from Mass Conservation</div>
      <p>Consider an elemental volume $\Delta V = A \Delta x$ bounded by planes at $x$ and $x + \Delta x$ over time interval $\Delta t$:</p>
      <ul>
        <li>Mass of diffusing solute entering through face at $x$: $m_{\text{in}} = J(x) \cdot A \cdot \Delta t$</li>
        <li>Mass of diffusing solute leaving through face at $x + \Delta x$: $m_{\text{out}} = J(x + \Delta x) \cdot A \cdot \Delta t$</li>
        <li>Net accumulation of solute inside the slice: $\Delta m = m_{\text{in}} - m_{\text{out}} = [J(x) - J(x + \Delta x)] A \Delta t$</li>
      </ul>
      <p>The change in average concentration inside the volume is $\Delta C = \frac{\Delta m}{\Delta V} = \frac{\Delta m}{A \Delta x}$:</p>
      $$\Delta C = \frac{[J(x) - J(x + \Delta x)] A \Delta t}{A \Delta x} = -\frac{J(x + \Delta x) - J(x)}{\Delta x} \Delta t$$
      <p>Dividing by $\Delta t$ and taking the limit as $\Delta x \to 0$ and $\Delta t \to 0$:</p>
      $$\lim_{\Delta t \to 0} \frac{\Delta C}{\Delta t} = -\lim_{\Delta x \to 0} \frac{J(x + \Delta x) - J(x)}{\Delta x} \implies \frac{\partial C}{\partial t} = -\frac{\partial J}{\partial x}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b) & (c): Substitution of Fick's First Law</div>
      <p>From Fick's First Law, $J = -D \frac{\partial C}{\partial x}$. Substituting this flux expression into the continuity equation:</p>
      $$\frac{\partial C}{\partial t} = -\frac{\partial}{\partial x}\left(-D \frac{\partial C}{\partial x}\right) = \frac{\partial}{\partial x}\left(D \frac{\partial C}{\partial x}\right)$$
      <p>If the diffusion coefficient $D$ is constant (independent of $x$ and $C$):</p>
      $$\frac{\partial C}{\partial t} = D \frac{\partial}{\partial x}\left(\frac{\partial C}{\partial x}\right) = D \frac{\partial^2 C}{\partial x^2}$$
      <p>This is <strong>Fick's Second Law</strong>, mathematically identical to Fourier's heat conduction equation.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): When $D = D(C)$ (Concentration-Dependent Diffusivity)</div>
      <p>Diffusivity depends strongly on concentration when:</p>
      <ol>
        <li><strong>High Solute Concentrations:</strong> In concentrated solid solutions (e.g., carbon $> 0.5 \text{ wt}\%$ in austenite, or Cu-Ni couples), dissolved solute alters the host lattice parameter and local bond stiffness, accelerating jump frequencies. In austenite, $D_{\text{C}}$ increases by a factor of 4 as carbon concentration rises from $0.1\%$ to $1.4\%$.</li>
        <li><strong>Non-Ideal Thermodynamic Solutions:</strong> When activity coefficients vary strongly with concentration, Darken's thermodynamic factor $\left(1 + \frac{\partial \ln \gamma}{\partial \ln X}\right)$ causes $D$ to be highly concentration-dependent. (In such cases, the non-linear equation must be solved using the Boltzmann-Matano graphical method).</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>Continuity Equation:</strong> $$\frac{\partial C}{\partial t} = -\frac{\partial J}{\partial x}$$
      <strong>Fick's Second Law (Constant $D$):</strong> $$\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}$$
      $D = D(C)$ occurs in concentrated alloys where solute dilates the lattice or thermodynamics are non-ideal.
    </div>""")

# P12: Semi-Infinite Solid Boundary Conditions and Error Function Solution
add(12, "Non-Steady-State Error Function Solution for a Semi-Infinite Solid",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Fundamental",
    r"""<p>The standard analytical solution to Fick's second law models diffusion into a thick workpiece treated as a semi-infinite solid.</p>
    <ol type="a">
      <li>State the three <strong>initial and boundary conditions</strong> defining the semi-infinite diffusion model:
        <ul>
          <li>Initial condition at $t = 0$.</li>
          <li>Surface boundary condition at $x = 0$ for $t > 0$.</li>
          <li>Far-field boundary condition as $x \to \infty$ for all $t$.</li>
        </ul>
      </li>
      <li>Write down the classic <strong>error function analytical solution</strong>:
      $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$
      Define $C(x,t)$, $C_0$, $C_s$, $x$, $D$, and $t$.</li>
      <li>Explain the physical meaning of the dimensionless similarity variable $\eta = \frac{x}{2\sqrt{Dt}}$.</li>
      <li>What physical criterion determines whether a real finite-thickness component (thickness $2L$) can be accurately treated as a "semi-infinite" solid?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Boundary and Initial Conditions</div>
      <ol>
        <li><strong>Initial Condition:</strong> Before diffusion begins ($t = 0$), the solute is uniformly distributed throughout the solid at bulk concentration $C_0$:
        $$C(x, 0) = C_0 \quad \text{for } 0 \le x < \infty$$</li>
        <li><strong>Surface Boundary Condition:</strong> For all times $t > 0$, the surface at $x = 0$ is held at an instantaneous, constant composition $C_s$ (maintained by an active gas or liquid atmosphere):
        $$C(0, t) = C_s \quad \text{for } t > 0$$</li>
        <li><strong>Far-Field Boundary Condition:</strong> Deep in the interior ($x \to \infty$), the solid is unaffected by surface diffusion, maintaining the original composition:
        $$C(\infty, t) = C_0 \quad \text{for all } t$$</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Analytical Error Function Solution</div>
      $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erfc}\left(\frac{x}{2\sqrt{Dt}}\right)$$
      <ul>
        <li>$C(x,t)$: Solute concentration at depth $x$ after diffusion time $t$.</li>
        <li>$C_0$: Initial uniform bulk concentration of the solid before treatment.</li>
        <li>$C_s$: Constant surface concentration maintained at the interface.</li>
        <li>$x$: Perpendicular depth into the solid ($\text{m}$).</li>
        <li>$D$: Diffusion coefficient ($\text{m}^2/\text{s}$).</li>
        <li>$t$: Diffusion time ($\text{s}$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): The Dimensionless Similarity Variable $\eta = \frac{x}{2\sqrt{Dt}}$</div>
      <p>By defining the Boltzmann similarity variable $\eta = \frac{x}{2\sqrt{Dt}}$, the partial differential equation $\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}$ is converted into an ordinary differential equation $\frac{d^2 C}{d\eta^2} + 2\eta \frac{dC}{d\eta} = 0$. Physically, $\eta$ scales the spatial coordinate $x$ by the characteristic diffusion penetration distance $2\sqrt{Dt}$, collapsing all time-dependent concentration profiles onto a single universal curve.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): The Semi-Infinite Validity Criterion</div>
      <p>A finite component of half-thickness $L$ (or sheet of thickness $2L$ exposed on both sides) behaves as a semi-infinite solid as long as diffusing solute has not penetrated to the center of the part ($x = L$). Because the error function approaches zero ($1 - \text{erf}(z) < 0.005$) for $z \ge 2.0$, the diffusion field penetrates to $x_{\max} \approx 4\sqrt{Dt}$. Therefore, the semi-infinite model is strictly valid as long as:</p>
      $$L > 4\sqrt{Dt} \implies t < \frac{L^2}{16 D}$$
    </div>
    <div class="final-answer-box">
      <strong>Semi-Infinite Solution:</strong> $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{erfc}\left(\frac{x}{2\sqrt{Dt}}\right)$$
      <strong>Validity Criterion:</strong> $L > 4\sqrt{Dt}$ (diffusion depth must not reach the opposing boundary or center of the part).
    </div>""")

# P13: Error Function Properties and Interpolation
add(13, "The Gaussian Error Function: Mathematical Properties, Table Values, and Linear Interpolation",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Fundamental",
    r"""<p>The Gauss error function $\text{erf}(z)$ is the standard mathematical function used in non-steady-state diffusion calculations.</p>
    <ol type="a">
      <li>State the integral definition of the <strong>Gaussian error function</strong>:
      $$\text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-\eta^2} d\eta$$
      State the exact values of $\text{erf}(0)$, $\text{erf}(\infty)$, and $\text{erf}(-z)$.</li>
      <li>Define the <strong>complementary error function</strong> $\text{erfc}(z)$.</li>
      <li>A reference table of error function values is given below:
        <table class="table-styled">
          <thead><tr><th>$z$</th><th>$\text{erf}(z)$</th><th>$z$</th><th>$\text{erf}(z)$</th><th>$z$</th><th>$\text{erf}(z)$</th></tr></thead>
          <tbody>
            <tr><td>0.20</td><td>0.2227</td><td>0.45</td><td>0.4755</td><td>0.70</td><td>0.6778</td></tr>
            <tr><td>0.25</td><td>0.2763</td><td>0.50</td><td>0.5205</td><td>0.75</td><td>0.7112</td></tr>
            <tr><td>0.30</td><td>0.3286</td><td>0.55</td><td>0.5633</td><td>0.80</td><td>0.7421</td></tr>
            <tr><td>0.35</td><td>0.3794</td><td>0.60</td><td>0.6039</td><td>0.85</td><td>0.7707</td></tr>
            <tr><td>0.40</td><td>0.4284</td><td>0.65</td><td>0.6420</td><td>0.90</td><td>0.7969</td></tr>
          </tbody>
        </table>
        Using linear interpolation:
        <ul>
          <li>Find $\text{erf}(0.425)$.</li>
          <li>Find the argument $z$ for which $\text{erf}(z) = 0.5000$.</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Mathematical Definitions and Properties</div>
      $$\text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-\eta^2} d\eta$$
      <ul>
        <li>$\text{erf}(0) = \frac{2}{\sqrt{\pi}} \int_0^0 e^{-\eta^2} d\eta = \mathbf{0}$</li>
        <li>$\text{erf}(\infty) = \frac{2}{\sqrt{\pi}} \left(\frac{\sqrt{\pi}}{2}\right) = \mathbf{1.0}$</li>
        <li>$\text{erf}(-z) = -\text{erf}(z)$ (odd function).</li>
        <li>For small arguments ($z \ll 1$): $\text{erf}(z) \approx \frac{2}{\sqrt{\pi}} z \approx 1.1284 z$.</li>
        <li><strong>Complementary Error Function:</strong> $\text{erfc}(z) = 1 - \text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_z^\infty e^{-\eta^2} d\eta$.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Linear Interpolations</div>
      <ul>
        <li><strong>Finding $\text{erf}(0.425)$ between $z_1 = 0.40$ and $z_2 = 0.45$:</strong>
          $$\text{erf}(0.40) = 0.4284, \quad \text{erf}(0.45) = 0.4755$$
          $$\frac{\text{erf}(0.425) - 0.4284}{0.425 - 0.40} = \frac{0.4755 - 0.4284}{0.45 - 0.40}$$
          $$\text{erf}(0.425) = 0.4284 + \left(\frac{0.025}{0.050}\right) \times (0.4755 - 0.4284)$$
          $$\text{erf}(0.425) = 0.4284 + 0.5 \times (0.0471) = 0.4284 + 0.02355 = \mathbf{0.45195 \approx 0.4520}$$
        </li>
        <li><strong>Finding $z$ for $\text{erf}(z) = 0.5000$:</strong>
          Looking at the table: $\text{erf}(0.45) = 0.4755$ and $\text{erf}(0.50) = 0.5205$.
          $$\frac{z - 0.45}{0.5000 - 0.4755} = \frac{0.50 - 0.45}{0.5205 - 0.4755}$$
          $$z - 0.45 = \frac{0.0245}{0.0450} \times (0.05) = 0.5444 \times 0.05 = 0.02722$$
          $$z = 0.45 + 0.02722 = \mathbf{0.4772}$$
        </li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Properties:</strong> $\text{erf}(0) = 0$, $\text{erf}(\infty) = 1.0$, $\text{erfc}(z) = 1 - \text{erf}(z)$.<br>
      <strong>Interpolations:</strong> $\text{erf}(0.425) = \mathbf{0.4520}$ &bull; For $\text{erf}(z) = 0.5000 \implies z = \mathbf{0.4772}$.
    </div>""")

# P14: Characteristic Diffusion Distance and Scaling Law
add(14, "The Scaling Law of Diffusion: Characteristic Penetration Depth and the $x^2/t$ Rule",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Fundamental",
    r"""<p>The fundamental parabolic nature of Fick's second law dictates that diffusion distance scales with the square root of time.</p>
    <ol type="a">
      <li>Define the <strong>characteristic diffusion distance (diffusion length)</strong>:
      $$\bar{x} \approx 2\sqrt{Dt} \quad (\text{or } \sqrt{Dt})$$
      Explain why diffusion slows down drastically as penetration depth increases.</li>
      <li>Derive the classic <strong>scaling rule</strong>: For a fixed host metal and constant diffusion temperature, achieving an identical concentration $C_x$ requires:
      $$\frac{x_1^2}{t_1} = \frac{x_2^2}{t_2} \quad \text{or} \quad \frac{x_1}{\sqrt{t_1}} = \frac{x_2}{\sqrt{t_2}}$$</li>
      <li>In a gear carburizing process, a carbon case depth of $0.60 \text{ mm}$ is achieved after $2.0 \text{ hours}$ at $925^\circ\text{C}$.
        <ul>
          <li>Calculate the time required to achieve a case depth of $1.20 \text{ mm}$ (doubling the depth) at the same temperature.</li>
          <li>Calculate the case depth achieved after $8.0 \text{ hours}$ of carburizing.</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Characteristic Diffusion Distance $\bar{x} \approx 2\sqrt{Dt}$</div>
      <p>From the semi-infinite solution, the argument of the error function is $z = \frac{x}{2\sqrt{Dt}}$. Significant composition change occurs when $z \approx 1$, which defines the characteristic penetration distance $\bar{x} \approx 2\sqrt{Dt}$. Because distance scales with $\sqrt{t}$, the penetration velocity is:</p>
      $$v = \frac{d\bar{x}}{dt} = \frac{d(2\sqrt{Dt})}{dt} = \sqrt{\frac{D}{t}} = \frac{2D}{\bar{x}}$$
      <p>As the case depth increases, the penetration speed decays inversely with depth ($v \propto 1/\bar{x}$). To double the depth, the diffusion time must be quadrupled ($4\times$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Derivation of the $x^2/t = \text{constant}$ Scaling Rule</div>
      <p>For fixed initial concentration $C_0$ and surface concentration $C_s$, achieving a specific target concentration $C_x$ means the left side of the error function solution is a constant:</p>
      $$\frac{C_x - C_0}{C_s - C_0} = \text{const} \implies 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{const} \implies \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) = \text{const}$$
      <p>Because the error function is strictly monotonic, its argument must be constant:</p>
      $$\frac{x}{2\sqrt{Dt}} = \text{const} \implies \frac{x^2}{Dt} = \text{const}$$
      <p>At constant temperature, $D$ is constant, giving the scaling rule:</p>
      $$\frac{x_1^2}{t_1} = \frac{x_2^2}{t_2} \iff \frac{x_1}{\sqrt{t_1}} = \frac{x_2}{\sqrt{t_2}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Quantitative Calculations ($x_1 = 0.60 \text{ mm}, t_1 = 2.0 \text{ hr}$)</div>
      <ul>
        <li><strong>Time to achieve $x_2 = 1.20 \text{ mm}$ (doubling case depth):</strong>
        $$\frac{t_2}{t_1} = \left(\frac{x_2}{x_1}\right)^2 = \left(\frac{1.20 \text{ mm}}{0.60 \text{ mm}}\right)^2 = (2.0)^2 = 4.0$$
        $$t_2 = 4.0 \times t_1 = 4.0 \times 2.0 \text{ hr} = \mathbf{8.0 \text{ hours}}$$
        <p>Doubling the case depth requires <strong>4 times the furnace processing time</strong>!</p></li>
        <li><strong>Case depth after $t_3 = 8.0 \text{ hours}$:</strong>
        $$x_3 = x_1 \sqrt{\frac{t_3}{t_1}} = 0.60 \text{ mm} \times \sqrt{\frac{8.0}{2.0}} = 0.60 \times \sqrt{4.0} = 0.60 \times 2 = \mathbf{1.20 \text{ mm}}$$</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Scaling Law:</strong> $$\frac{x_1^2}{t_1} = \frac{x_2^2}{t_2}$$
      Doubling case depth requires <strong>4 times longer</strong> ($t_2 = \mathbf{8.0 \text{ hours}}$).<br>
      Penetration rate decays as $1/\sqrt{t}$.
    </div>""")

# P15: Industrial Gas Carburizing Calculations
add(15, "Industrial Gas Carburizing: Calculating Carburizing Time at Fixed Temperature",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Advanced",
    r"""<p>An automotive transmission gear fabricated from AISI 1020 steel ($0.20 \text{ wt}\%$ Carbon) is gas carburized at $950^\circ\text{C}$ in an atmosphere maintaining a constant surface carbon content of $1.20 \text{ wt}\%$. The diffusion coefficient of carbon in austenite at $950^\circ\text{C}$ is $D = 1.28 \times 10^{-11} \text{ m}^2/\text{s}$.</p>
    <ol type="a">
      <li>Calculate the carburizing time $t$ (in hours and minutes) required to achieve a carbon content of $0.60 \text{ wt}\%$ at a depth of $0.75 \text{ mm}$ below the surface.</li>
      <li>Calculate the carbon content at depth $x = 0.35 \text{ mm}$ after this carburizing duration.</li>
      <li>Why is gas carburizing universally conducted in the FCC austenite phase ($\gamma$-Fe, $T > 912^\circ\text{C}$) rather than the BCC ferrite phase ($\alpha$-Fe)?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Calculation of Carburizing Time $t$</div>
      <p>Given parameters: $C_0 = 0.20 \text{ wt}\%$, $C_s = 1.20 \text{ wt}\%$, $C(x,t) = 0.60 \text{ wt}\%$, $x = 0.75 \text{ mm} = 7.5 \times 10^{-4} \text{ m}$, $D = 1.28 \times 10^{-11} \text{ m}^2/\text{s}$.</p>
      <p>Substitute into the error function equation:</p>
      $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$
      $$\frac{0.60 - 0.20}{1.20 - 0.20} = \frac{0.40}{1.00} = 0.4000 = 1 - \text{erf}(z) \implies \text{erf}(z) = 1.0000 - 0.4000 = 0.6000$$
      <p>From the error function table in Problem 13:</p>
      $$\text{erf}(0.55) = 0.5633, \quad \text{erf}(0.60) = 0.6039$$
      <p>Interpolate for $\text{erf}(z) = 0.6000$:</p>
      $$\frac{z - 0.55}{0.6000 - 0.5633} = \frac{0.60 - 0.55}{0.6039 - 0.5633} \implies \frac{z - 0.55}{0.0367} = \frac{0.05}{0.0406} = 1.2315$$
      $$z - 0.55 = 1.2315 \times 0.0367 = 0.0452 \implies z = \mathbf{0.5952}$$
      <p>Now equate $z = \frac{x}{2\sqrt{Dt}}$:</p>
      $$2\sqrt{Dt} = \frac{x}{z} = \frac{7.5 \times 10^{-4} \text{ m}}{0.5952} = 1.2601 \times 10^{-3} \text{ m}$$
      $$\sqrt{Dt} = 6.3004 \times 10^{-4} \text{ m} \implies Dt = (6.3004 \times 10^{-4})^2 = 3.9695 \times 10^{-7} \text{ m}^2$$
      $$t = \frac{3.9695 \times 10^{-7} \text{ m}^2}{1.28 \times 10^{-11} \text{ m}^2/\text{s}} = 31,012 \text{ seconds}$$
      <p>Convert to hours:</p>
      $$t = \frac{31,012 \text{ s}}{3600 \text{ s/hr}} = \mathbf{8.614 \text{ hours} = 8 \text{ hours and 37 minutes}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Carbon Content at Depth $x = 0.35 \text{ mm}$</div>
      $$z_2 = \frac{x_2}{2\sqrt{Dt}} = \frac{3.5 \times 10^{-4} \text{ m}}{1.2601 \times 10^{-3} \text{ m}} = 0.2777$$
      <p>Interpolate error function for $z_2 = 0.2777$ ($\text{erf}(0.25) = 0.2763, \text{erf}(0.30) = 0.3286$):</p>
      $$\text{erf}(0.2777) = 0.2763 + \left(\frac{0.2777 - 0.25}{0.05}\right) \times (0.3286 - 0.2763) = 0.2763 + 0.554 \times (0.0523) = 0.3053$$
      $$\frac{C(0.35 \text{ mm}) - 0.20}{1.20 - 0.20} = 1 - 0.3053 = 0.6947$$
      $$C(0.35 \text{ mm}) = 0.20 + 0.6947(1.00) = \mathbf{0.895 \text{ wt}\% \approx 0.90 \text{ wt}\%}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Why Austenite Phase is Required</div>
      <p>As proved in Chapter 4, the maximum interstitial solubility of carbon in BCC ferrite ($\alpha$-Fe) is only $0.022 \text{ wt}\%$. It is impossible to achieve a high-carbon hard surface ($0.8\text{--}1.2\text{ wt}\%$) in ferrite because iron carbide (cementite) would immediately precipitate as an impenetrable crust on the outer surface, blocking further carbon absorption. In FCC austenite ($\gamma$-Fe), the maximum solubility is $2.14 \text{ wt}\%$, allowing large quantities of carbon to dissolve in solid solution and subsequently quench into ultra-hard martensite.</p>
    </div>
    <div class="final-answer-box">
      <strong>Carburizing Time:</strong> $t = \mathbf{8.61 \text{ hours}}$ (8 hours 37 minutes).<br>
      <strong>Carbon at $0.35\text{ mm}$:</strong> $C = \mathbf{0.895 \text{ wt}\%}$.<br>
      Austenite is required because its carbon solubility ($2.14\text{ wt}\%$) far exceeds ferrite ($0.022\text{ wt}\%$).
    </div>""")

# Save checkpoint for part 1 (1 to 15)
print("Ch 5 Part 1: P1-P15 written.")
# P16: Case Depth as a Function of Time
add(16, "Gas Carburizing: Predicting Case Depth as a Function of Diffusion Time",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Intermediate",
    r"""<p>In quality control specifications, the effective case depth is defined as the perpendicular distance from the surface to the point where the carbon content reaches a specified hardness threshold (e.g., $0.45 \text{ wt}\%$ Carbon for 50 HRC hardness).</p>
    <div style="text-align:center; margin: 10px 0;">
      Alloy: AISI 8620 steel ($C_0 = 0.20 \text{ wt}\%$)<br>
      Carburizing atmosphere: Constant surface carbon $C_s = 1.00 \text{ wt}\%$ at $927^\circ\text{C}$ ($1200 \text{ K}$)<br>
      Diffusivity of Carbon in $\gamma$-Fe at $927^\circ\text{C}$: $D = 1.20 \times 10^{-11} \text{ m}^2/\text{s}$
    </div>
    <ol type="a">
      <li>Calculate the effective case depth ($C_x = 0.45 \text{ wt}\%$) achieved after $4.0 \text{ hours}$ of carburizing.</li>
      <li>Calculate the case depth after $9.0 \text{ hours}$ of carburizing.</li>
      <li>Confirm whether the ratio of case depths matches the theoretical scaling ratio $\sqrt{t_2 / t_1}$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Case Depth after $4.0 \text{ hours}$ ($t_1 = 14,400 \text{ s}$)</div>
      <p>Evaluate concentration ratio:</p>
      $$\frac{C_x - C_0}{C_s - C_0} = \frac{0.45 - 0.20}{1.00 - 0.20} = \frac{0.25}{0.80} = 0.3125$$
      $$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}(z) \implies \text{erf}(z) = 1 - 0.3125 = 0.6875$$
      <p>From the error function table: $\text{erf}(0.70) = 0.6778$ and $\text{erf}(0.75) = 0.7112$.</p>
      <p>Interpolate for $z$:</p>
      $$\frac{z - 0.70}{0.6875 - 0.6778} = \frac{0.75 - 0.70}{0.7112 - 0.6778} \implies \frac{z - 0.70}{0.0097} = \frac{0.05}{0.0334} = 1.497$$
      $$z - 0.70 = 1.497 \times 0.0097 = 0.0145 \implies z = \mathbf{0.7145}$$
      <p>Compute case depth $x_1$ ($t_1 = 4.0 \times 3600 = 14,400 \text{ s}$):</p>
      $$x_1 = 2 z \sqrt{D t_1} = 2 \times 0.7145 \times \sqrt{(1.20 \times 10^{-11} \text{ m}^2/\text{s}) \times (14,400 \text{ s})}$$
      $$D t_1 = 1.728 \times 10^{-7} \text{ m}^2 \implies \sqrt{D t_1} = 4.157 \times 10^{-4} \text{ m}$$
      $$x_1 = 2 \times 0.7145 \times (4.157 \times 10^{-4} \text{ m}) = 5.940 \times 10^{-4} \text{ m} = \mathbf{0.594 \text{ mm}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Case Depth after $9.0 \text{ hours}$ ($t_2 = 32,400 \text{ s}$)</div>
      $$D t_2 = (1.20 \times 10^{-11}) \times (32,400) = 3.888 \times 10^{-7} \text{ m}^2 \implies \sqrt{D t_2} = 6.235 \times 10^{-4} \text{ m}$$
      $$x_2 = 2 z \sqrt{D t_2} = 2 \times 0.7145 \times (6.235 \times 10^{-4} \text{ m}) = 8.910 \times 10^{-4} \text{ m} = \mathbf{0.891 \text{ mm}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Verification of Scaling Ratio</div>
      $$\frac{x_2}{x_1} = \frac{0.891 \text{ mm}}{0.594 \text{ mm}} = \mathbf{1.500}$$
      $$\sqrt{\frac{t_2}{t_1}} = \sqrt{\frac{9.0 \text{ hr}}{4.0 \text{ hr}}} = \sqrt{2.25} = \mathbf{1.500}$$
      <p>The calculated depth ratio matches the theoretical square-root scaling law with exact precision.</p>
    </div>
    <div class="final-answer-box">
      <strong>Case Depth at $4.0 \text{ hr}$:</strong> $x_1 = \mathbf{0.594 \text{ mm}}$.<br>
      <strong>Case Depth at $9.0 \text{ hr}$:</strong> $x_2 = \mathbf{0.891 \text{ mm}}$.<br>
      Depth ratio matches $\sqrt{t_2/t_1} = \sqrt{9/4} = \mathbf{1.500}$.
    </div>""")

# P17: Temperature Optimization in Carburizing
add(17, "Thermally Activated Carburizing: Accelerating Case Depth via Temperature Increase",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Advanced",
    r"""<p>To reduce energy consumption and cycle times in heat treatment facilities, metallurgists often increase furnace temperature.</p>
    <div style="text-align:center; margin: 10px 0;">
      Diffusion of Carbon in Austenite: $D_0 = 2.3 \times 10^{-5} \text{ m}^2/\text{s}$, $Q_d = 148.0 \text{ kJ/mol}$ ($R = 8.314 \text{ J/(mol}\cdot\text{K)}$)<br>
      Baseline Process: Carburizing takes $10.0 \text{ hours}$ at $T_1 = 900^\circ\text{C}$ ($1173 \text{ K}$) to achieve a target case depth.
    </div>
    <ol type="a">
      <li>Calculate the diffusion coefficient $D_1$ of carbon in austenite at $900^\circ\text{C}$ ($1173 \text{ K}$).</li>
      <li>Calculate the diffusion coefficient $D_2$ at an elevated temperature $T_2 = 1000^\circ\text{C}$ ($1273 \text{ K}$).</li>
      <li>Derive the relationship between diffusion times ($t_1, t_2$) and diffusivities ($D_1, D_2$) to achieve the identical case depth and concentration profile:
      $$D_1 t_1 = D_2 t_2 \implies t_2 = t_1 \left(\frac{D_1}{D_2}\right)$$</li>
      <li>Calculate the required carburizing time $t_2$ at $1000^\circ\text{C}$ in hours and minutes. Calculate the percentage time savings.</li>
      <li>Discuss one metallurgical trade-off or risk of increasing the carburizing temperature to $1000^\circ\text{C}$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Arrhenius Diffusivity Calculations</div>
      <ul>
        <li><strong>At $T_1 = 900^\circ\text{C} = 1173 \text{ K}$:</strong>
          $$R T_1 = (8.314 \text{ J/(mol}\cdot\text{K)}) \times (1173 \text{ K}) = 9752.3 \text{ J/mol} = 9.7523 \text{ kJ/mol}$$
          $$D_1 = (2.3 \times 10^{-5}) \exp\left(-\frac{148.0}{9.7523}\right) = (2.3 \times 10^{-5}) \exp(-15.1759)$$
          $$D_1 = (2.3 \times 10^{-5}) \times (2.5656 \times 10^{-7}) = \mathbf{5.901 \times 10^{-12} \text{ m}^2/\text{s}}$$
        </li>
        <li><strong>At $T_2 = 1000^\circ\text{C} = 1273 \text{ K}$:</strong>
          $$R T_2 = (8.314) \times (1273) = 10583.7 \text{ J/mol} = 10.5837 \text{ kJ/mol}$$
          $$D_2 = (2.3 \times 10^{-5}) \exp\left(-\frac{148.0}{10.5837}\right) = (2.3 \times 10^{-5}) \exp(-13.9838)$$
          $$D_2 = (2.3 \times 10^{-5}) \times (8.4510 \times 10^{-7}) = \mathbf{1.9437 \times 10^{-11} \text{ m}^2/\text{s}}$$
        </li>
      </ul>
      <p>Diffusivity ratio:</p>
      $$\frac{D_2}{D_1} = \frac{1.9437 \times 10^{-11}}{5.901 \times 10^{-12}} = \mathbf{3.294}$$
      <p>Increasing temperature by just $100^\circ\text{C}$ speeds up carbon mobility by more than $3.3\times$!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c) & (d): Processing Time at $1000^\circ\text{C}$ and Savings</div>
      <p>For an identical concentration profile, the argument $z = \frac{x}{2\sqrt{Dt}}$ is constant for any depth $x$, which requires:</p>
      $$D_1 t_1 = D_2 t_2 \implies t_2 = t_1 \left(\frac{D_1}{D_2}\right)$$
      $$t_2 = 10.0 \text{ hr} \times \left(\frac{1}{3.294}\right) = \mathbf{3.036 \text{ hours} = 3 \text{ hours and 2 minutes}}$$
      <p>Percentage time savings:</p>
      $$\% \text{ Time Saved} = \frac{10.0 - 3.036}{10.0} \times 100\% = \mathbf{69.64\% \approx 70\%}$$
      <p>The furnace cycle is reduced from 10 hours down to just 3 hours.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (e): Metallurgical Trade-Off of High-Temperature Carburizing</div>
      <p>At $1000^\circ\text{C}$, the high thermal energy causes significant <strong>prior austenite grain growth (grain coarsening)</strong>. Coarse austenite grains transform upon quenching into coarse martensite packets, which drastically reduces the impact toughness and fatigue resistance of the core steel. (To mitigate this, microalloyed steels with fine niobium/titanium carbide precipitates are used to pin grain boundaries and prevent grain growth).</p>
    </div>
    <div class="final-answer-box">
      <strong>Diffusivities:</strong> $D_1(900^\circ\text{C}) = \mathbf{5.90 \times 10^{-12} \text{ m}^2/\text{s}}$, $D_2(1000^\circ\text{C}) = \mathbf{1.94 \times 10^{-11} \text{ m}^2/\text{s}}$.<br>
      <strong>Accelerated Time:</strong> $t_2 = \mathbf{3.04 \text{ hours}}$ (saves $\mathbf{70\%}$ of furnace cycle).<br>
      <strong>Trade-off:</strong> Prior austenite grain coarsening degrades core impact toughness.
    </div>""")

# P18: Steel Decarburization
add(18, "Decarburization of Steel: Error Function Depletion Modeling during Open-Air Annealing",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Advanced",
    r"""<p>During hot rolling or forging of high-carbon spring steel in air, oxygen and water vapor in the furnace react with carbon at the surface, creating an unwanted decarburized surface layer.</p>
    <div style="text-align:center; margin: 10px 0;">
      Spring Steel (AISI 1080): Initial uniform carbon content $C_0 = 0.80 \text{ wt}\%$<br>
      Decarburizing furnace atmosphere: Surface carbon maintained at $C_s = 0.05 \text{ wt}\%$ at $900^\circ\text{C}$<br>
      Diffusivity of Carbon in $\gamma$-Fe at $900^\circ\text{C}$: $D = 5.9 \times 10^{-12} \text{ m}^2/\text{s}$<br>
      Annealing duration: $t = 3.0 \text{ hours}$
    </div>
    <ol type="a">
      <li>Write down the error function solution for decarburization (outward diffusion / surface depletion).</li>
      <li>Calculate the carbon content at a depth of $0.20 \text{ mm}$ below the surface after $3.0 \text{ hours}$.</li>
      <li>If quality standards dictate that the steel is unusable wherever the carbon content falls below $0.65 \text{ wt}\%$, calculate the required surface machining depth (grinding allowance) in millimeters to remove the defective decarburized layer.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Decarburization Solution Formula</div>
      <p>The standard semi-infinite solution holds identically for outward diffusion (depletion), where $C_s < C_0$:</p>
      $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right) \implies C(x,t) = C_0 - (C_0 - C_s)\left[1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)\right]$$
      $$C(x,t) = C_s + (C_0 - C_s) \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Carbon Content at Depth $x = 0.20 \text{ mm}$ ($t = 3.0 \text{ hr} = 10,800 \text{ s}$)</div>
      $$2\sqrt{Dt} = 2 \sqrt{(5.9 \times 10^{-12} \text{ m}^2/\text{s}) \times (10,800 \text{ s})} = 2 \sqrt{6.372 \times 10^{-8} \text{ m}^2} = 2 \times (2.524 \times 10^{-4} \text{ m}) = 5.048 \times 10^{-4} \text{ m}$$
      $$z = \frac{x}{2\sqrt{Dt}} = \frac{2.0 \times 10^{-4} \text{ m}}{5.048 \times 10^{-4} \text{ m}} = \mathbf{0.3962}$$
      <p>From the error function table: $\text{erf}(0.35) = 0.3794$ and $\text{erf}(0.40) = 0.4284$.</p>
      $$\text{erf}(0.3962) = 0.3794 + \left(\frac{0.3962 - 0.35}{0.05}\right) \times (0.4284 - 0.3794) = 0.3794 + 0.924 \times (0.0490) = 0.4247$$
      $$C(0.20 \text{ mm}) = 0.05 + (0.80 - 0.05) \times (0.4247) = 0.05 + 0.75 \times 0.4247 = 0.05 + 0.3185 = \mathbf{0.369 \text{ wt}\%}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Grinding Allowance Depth for $C_x = 0.65 \text{ wt}\%$</div>
      $$\frac{C_x - C_0}{C_s - C_0} = \frac{0.65 - 0.80}{0.05 - 0.80} = \frac{-0.15}{-0.75} = 0.2000$$
      $$1 - \text{erf}(z) = 0.2000 \implies \text{erf}(z) = 0.8000$$
      <p>From table: $\text{erf}(0.90) = 0.7969$ and $\text{erf}(0.95) \approx 0.8209$.</p>
      $$\text{erf}(z) = 0.8000 \implies z \approx \mathbf{0.9065}$$
      $$x = 2 z \sqrt{Dt} = 0.9065 \times (5.048 \times 10^{-4} \text{ m}) = 4.576 \times 10^{-4} \text{ m} = \mathbf{0.458 \text{ mm}}$$
      <p>A minimum machining depth of at least <strong>$0.46 \text{ mm}$</strong> must be ground off the spring steel bar to remove the weakened, decarburized outer layer and restore full fatigue resistance.</p>
    </div>
    <div class="final-answer-box">
      <strong>Decarburization Formula:</strong> $C(x,t) = C_s + (C_0 - C_s)\text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$.<br>
      <strong>Carbon Content at $0.20\text{ mm}$:</strong> $C = \mathbf{0.369 \text{ wt}\%}$.<br>
      <strong>Grinding Allowance:</strong> $x_{\text{grind}} = \mathbf{0.458 \text{ mm}}$ (to eliminate depleted zone below $0.65\text{ wt}\%$).
    </div>""")

# P19: Semiconductor Doping Constant Source (Pre-Deposition)
add(19, "Semiconductor Doping: Constant Surface Source (Pre-Deposition Diffusion)",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Intermediate",
    r"""<p>In planar silicon device fabrication, thermal diffusion introduces dopant atoms (such as boron or phosphorus) to form $p\text{-}n$ junctions.</p>
    <div style="text-align:center; margin: 10px 0;">
      Substrate: $n$-type Silicon wafer with uniform background donor doping $C_0 = 1.0 \times 10^{15} \text{ atoms/cm}^3$<br>
      Pre-deposition: Boron dopant source maintains solid solubility surface concentration $C_s = 5.0 \times 10^{19} \text{ atoms/cm}^3$ at $1050^\circ\text{C}$<br>
      Diffusivity of Boron in Silicon at $1050^\circ\text{C}$: $D = 1.40 \times 10^{-13} \text{ cm}^2/\text{s}$<br>
      Diffusion time: $t = 30.0 \text{ minutes}$
    </div>
    <ol type="a">
      <li>State the mathematical form of the concentration profile for constant-source pre-deposition diffusion.</li>
      <li>Define the <strong>metallurgical junction depth $x_j$</strong> and state the mathematical condition that defines it.</li>
      <li>Calculate the junction depth $x_j$ in micrometers ($\mu\text{m}$) after 30 minutes of pre-deposition.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Concentration Profile for Pre-Deposition</div>
      <p>Because the gas phase maintains a constant surface concentration $C_s$ during the entire pre-deposition step, the profile is given by the complementary error function ($\text{erfc}$):</p>
      $$C(x,t) = C_s \text{erfc}\left(\frac{x}{2\sqrt{Dt}}\right) = C_s \left[1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)\right]$$
      <p>(Since $C_s = 5 \times 10^{19} \gg C_0 = 10^{15}$, the background concentration $C_0$ is completely negligible in the denominator).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Definition of Metallurgical Junction Depth $x_j$</div>
      <p>The metallurgical $p\text{-}n$ junction occurs at that precise depth $x_j$ where the concentration of diffused acceptor dopant atoms ($C_{\text{boron}}$) exactly equals the background donor dopant concentration ($C_0$):</p>
      $$C(x_j, t) = C_0 \implies C_s \text{erfc}\left(\frac{x_j}{2\sqrt{Dt}}\right) = C_0 \implies \text{erfc}\left(\frac{x_j}{2\sqrt{Dt}}\right) = \frac{C_0}{C_s}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Junction Depth Calculation</div>
      <p>Diffusion time: $t = 30.0 \times 60 = 1800 \text{ s}$.</p>
      $$2\sqrt{Dt} = 2 \sqrt{(1.40 \times 10^{-13} \text{ cm}^2/\text{s}) \times (1800 \text{ s})} = 2 \sqrt{2.52 \times 10^{-10} \text{ cm}^2} = 2 \times (1.5875 \times 10^{-5} \text{ cm}) = 3.175 \times 10^{-5} \text{ cm}$$
      <p>Evaluate concentration ratio:</p>
      $$\text{erfc}(z_j) = \frac{C_0}{C_s} = \frac{1.0 \times 10^{15} \text{ cm}^{-3}}{5.0 \times 10^{19} \text{ cm}^{-3}} = 2.0 \times 10^{-5}$$
      <p>For very small $\text{erfc}$ values ($\text{erfc}(z) \ll 1$), we use the asymptotic expansion $\text{erfc}(z) \approx \frac{e^{-z^2}}{z\sqrt{\pi}}$ or standard semiconductor tables:</p>
      <ul>
        <li>For $\text{erfc}(z) = 2.0 \times 10^{-5} \implies z_j \approx \mathbf{3.045}$</li>
      </ul>
      <p>Now solve for junction depth $x_j$:</p>
      $$x_j = z_j \times (2\sqrt{Dt}) = 3.045 \times (3.175 \times 10^{-5} \text{ cm}) = 9.668 \times 10^{-5} \text{ cm}$$
      <p>Convert to micrometers ($1 \text{ cm} = 10,000 \mu\text{m}$):</p>
      $$x_j = 9.668 \times 10^{-5} \times 10,000 = \mathbf{0.967 \mu\text{m}}$$
    </div>
    <div class="final-answer-box">
      <strong>Pre-Deposition Profile:</strong> $$C(x,t) = C_s \text{erfc}\left(\frac{x}{2\sqrt{Dt}}\right)$$
      <strong>Junction Condition:</strong> $C(x_j) = C_0 \implies \text{erfc}(z_j) = 2.0 \times 10^{-5} \implies z_j = 3.045$.<br>
      <strong>Junction Depth:</strong> $x_j = \mathbf{0.967 \mu\text{m}}$ ($\approx 0.97 \mu\text{m}$).
    </div>""")

# P20: Semiconductor Doping Finite Source (Drive-In Diffusion)
add(20, "Semiconductor Doping: Finite Source Drive-In Diffusion and Gaussian Concentration Profile",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Advanced",
    r"""<p>Following pre-deposition, the external dopant source is removed, and a high-temperature "drive-in" step drives the fixed dose of dopant atoms deeper into the silicon substrate.</p>
    <ol type="a">
      <li>State the total dopant dose per unit area $Q$ introduced during a pre-deposition step:
      $$Q = \int_0^\infty C(x) dx = \frac{2}{\sqrt{\pi}} C_s \sqrt{D_{\text{pre}} t_{\text{pre}}}$$</li>
      <li>Write down the <strong>Gaussian analytical solution</strong> for drive-in diffusion from a delta-function surface source of total dose $Q$:
      $$C(x, t) = \frac{Q}{\sqrt{\pi D t}} \exp\left(-\frac{x^2}{4Dt}\right)$$</li>
      <li>A silicon wafer receives a pre-deposition dose of $Q = 1.80 \times 10^{15} \text{ atoms/cm}^2$. It is subsequently driven in at $1100^\circ\text{C}$ ($D = 4.0 \times 10^{-13} \text{ cm}^2/\text{s}$) for $t = 2.0 \text{ hours}$. Background doping is $C_0 = 1.0 \times 10^{15} \text{ atoms/cm}^3$.
        <ul>
          <li>Calculate the surface concentration $C(0, t)$ after drive-in.</li>
          <li>Calculate the final junction depth $x_j$ in micrometers.</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Pre-Deposition Dose and Gaussian Drive-In Solution</div>
      <p>Integrating the pre-deposition complementary error function profile over all $x$ yields the total incorporated dose $Q$ ($\text{atoms/cm}^2$):</p>
      $$Q = \int_0^\infty C_s \text{erfc}\left(\frac{x}{2\sqrt{D_{\text{pre}} t_{\text{pre}}}}\right) dx = \frac{2}{\sqrt{\pi}} C_s \sqrt{D_{\text{pre}} t_{\text{pre}}}$$
      <p>During drive-in, the wafer surface is sealed with an oxidizing ambient ($\text{SiO}_2$ capping layer), so no dopant enters or escapes (zero-flux boundary condition $\left.\frac{\partial C}{\partial x}\right|_{x=0} = 0$). Symmetrical reflection of the infinite Green's function yields the <strong>Gaussian half-space profile</strong>:</p>
      $$C(x, t) = \frac{Q}{\sqrt{\pi D t}} \exp\left(-\frac{x^2}{4Dt}\right)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for $1100^\circ\text{C}$ Drive-In ($t = 2.0 \text{ hr} = 7200 \text{ s}$)</div>
      <p>Given $Q = 1.80 \times 10^{15} \text{ atoms/cm}^2, D = 4.0 \times 10^{-13} \text{ cm}^2/\text{s}, t = 7200 \text{ s}$:</p>
      $$D t = (4.0 \times 10^{-13} \text{ cm}^2/\text{s}) \times (7200 \text{ s}) = 2.88 \times 10^{-9} \text{ cm}^2$$
      $$\sqrt{\pi D t} = \sqrt{\pi \times (2.88 \times 10^{-9} \text{ cm}^2)} = \sqrt{9.0478 \times 10^{-9}} = 9.512 \times 10^{-5} \text{ cm}$$
      <ul>
        <li><strong>Surface Concentration ($x = 0$):</strong>
        $$C(0, t) = \frac{Q}{\sqrt{\pi D t}} = \frac{1.80 \times 10^{15} \text{ cm}^{-2}}{9.512 \times 10^{-5} \text{ cm}} = \mathbf{1.892 \times 10^{19} \text{ atoms/cm}^3}$$
        Notice that surface concentration has dropped from $5 \times 10^{19}$ to $1.89 \times 10^{19}$ as dopant atoms diffuse inward!</li>
        <li><strong>Final Junction Depth $x_j$ (where $C(x_j) = C_0 = 1.0 \times 10^{15} \text{ cm}^{-3}$):</strong>
        $$C_0 = C(0, t) \exp\left(-\frac{x_j^2}{4Dt}\right) \implies \exp\left(-\frac{x_j^2}{4Dt}\right) = \frac{C_0}{C(0, t)}$$
        $$\exp\left(\frac{x_j^2}{4Dt}\right) = \frac{C(0, t)}{C_0} = \frac{1.892 \times 10^{19}}{1.0 \times 10^{15}} = 18,920$$
        $$\frac{x_j^2}{4Dt} = \ln(18,920) = 9.848$$
        $$x_j^2 = 9.848 \times (4Dt) = 9.848 \times (4 \times 2.88 \times 10^{-9} \text{ cm}^2) = 1.1345 \times 10^{-7} \text{ cm}^2$$
        $$x_j = \sqrt{1.1345 \times 10^{-7} \text{ cm}^2} = 3.368 \times 10^{-4} \text{ cm} = \mathbf{3.37 \mu\text{m}}$$
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Gaussian Drive-In:</strong> $$C(x,t) = \frac{Q}{\sqrt{\pi Dt}}\exp\left(-\frac{x^2}{4Dt}\right)$$
      <strong>Surface Concentration:</strong> $C(0) = \mathbf{1.89 \times 10^{19} \text{ atoms/cm}^3}$.<br>
      <strong>Final Junction Depth:</strong> $x_j = \mathbf{3.37 \mu\text{m}}$.
    </div>""")

# P21: Semi-Infinite Diffusion Couple Solution
add(21, "The Infinite Diffusion Couple: Composition Profile and Matano Interface",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Advanced",
    r"""<p>Consider an infinite diffusion couple fabricated by joining semi-infinite block $A$ (pure metal $A$, $C_A = 100\%$, $x < 0$) to semi-infinite block $B$ (pure metal $B$, $C_A = 0\%$, $x > 0$) at $t = 0$.</p>
    <ol type="a">
      <li>Assuming concentration-independent diffusivity $D$, state the analytical solution for the concentration profile $C(x,t)$ across the diffusion couple:
      $$\frac{C(x,t) - C_1}{C_2 - C_1} = \frac{1}{2}\left[1 + \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)\right]$$</li>
      <li>Prove that the concentration at the original welded interface ($x = 0$) remains strictly constant at the exact average value:
      $$C(0, t) = \frac{C_1 + C_2}{2}$$
      for all times $t > 0$.</li>
      <li>A pure Copper block ($C_1 = 100 \text{ at}\%\text{ Cu}$) is bonded to a 70Cu-30Ni alloy block ($C_2 = 70 \text{ at}\%\text{ Cu}$) and annealed at $1000^\circ\text{C}$ ($D = 2.0 \times 10^{-14} \text{ m}^2/\text{s}$) for $t = 48 \text{ hours}$. Calculate the copper concentration at:
        <ul>
          <li>The weld interface ($x = 0$).</li>
          <li>A distance $x = +10 \mu\text{m}$ into the alloy block.</li>
          <li>A distance $x = -10 \mu\text{m}$ into the pure copper block.</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Analytical Solution for Infinite Diffusion Couple</div>
      <p>For an infinite couple with initial conditions $C(x, 0) = C_1$ for $x < 0$ and $C(x, 0) = C_2$ for $x > 0$:</p>
      $$C(x,t) = \left(\frac{C_1 + C_2}{2}\right) - \left(\frac{C_1 - C_2}{2}\right) \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$
      <p>Equivalently written:</p>
      $$\frac{C(x,t) - C_1}{C_2 - C_1} = \frac{1}{2}\left[1 + \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)\right]$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Proof of Invariant Interface Concentration</div>
      <p>At the weld plane $x = 0$ for any time $t > 0$:</p>
      $$z = \frac{0}{2\sqrt{Dt}} = 0 \implies \text{erf}(0) = 0$$
      $$C(0, t) = \frac{C_1 + C_2}{2} - \left(\frac{C_1 - C_2}{2}\right)(0) \equiv \mathbf{\frac{C_1 + C_2}{2}}$$
      <p>The composition at the original interface remains pinned at the exact arithmetic mean of the two initial terminal concentrations for all times.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for Cu / Cu-Ni Couple ($t = 48 \text{ hr} = 172,800 \text{ s}$)</div>
      <p>Given $C_1 = 100 \text{ at}\%$ (for $x < 0$), $C_2 = 70 \text{ at}\%$ (for $x > 0$), $D = 2.0 \times 10^{-14} \text{ m}^2/\text{s}$:</p>
      $$C(0) = \frac{100 + 70}{2} = \mathbf{85.0 \text{ at}\% \text{ Cu}}$$
      $$2\sqrt{Dt} = 2 \sqrt{(2.0 \times 10^{-14}) \times (172,800)} = 2 \sqrt{3.456 \times 10^{-9} \text{ m}^2} = 2 \times (5.879 \times 10^{-5} \text{ m}) = 1.1758 \times 10^{-4} \text{ m} = 117.58 \mu\text{m}$$
      <ul>
        <li><strong>At $x = +10 \mu\text{m}$ (into the alloy):</strong>
        $$z = \frac{+10 \mu\text{m}}{117.58 \mu\text{m}} = +0.08505$$
        <p>Using $\text{erf}(z) \approx \frac{2}{\sqrt{\pi}} z \approx 1.1284 \times 0.08505 = 0.0960$:</p>
        $$C(+10 \mu\text{m}) = 85.0 - \left(\frac{100 - 70}{2}\right)(0.0960) = 85.0 - 15(0.0960) = 85.0 - 1.44 = \mathbf{83.56 \text{ at}\% \text{ Cu}}$$</li>
        <li><strong>At $x = -10 \mu\text{m}$ (into the pure copper):</strong>
        $$z = -0.08505 \implies \text{erf}(-z) = -0.0960$$
        $$C(-10 \mu\text{m}) = 85.0 - 15(-0.0960) = 85.0 + 1.44 = \mathbf{86.44 \text{ at}\% \text{ Cu}}$$</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Diffusion Couple Solution:</strong> $$C(x,t) = \frac{C_1+C_2}{2} - \frac{C_1-C_2}{2}\text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$
      <strong>Interface ($x = 0$):</strong> $C = \mathbf{85.0 \text{ at}\% \text{ Cu}}$ (constant).<br>
      <strong>At $+10\mu\text{m}$:</strong> $C = \mathbf{83.56 \text{ at}\%}$ &bull; <strong>At $-10\mu\text{m}$:</strong> $C = \mathbf{86.44 \text{ at}\%}$.
    </div>""")

# P22: Experimental Diffusivity Extraction
add(22, "Determining Diffusion Coefficient $D$ from an Experimental Composition Profile",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Intermediate",
    r"""<p>An experimental diffusion study measures the concentration profile of zinc diffusing into copper from a constant surface source.</p>
    <div style="text-align:center; margin: 10px 0;">
      Initial zinc concentration: $C_0 = 0.0 \text{ wt}\%$<br>
      Surface zinc concentration: $C_s = 20.0 \text{ wt}\%$ maintained at $800^\circ\text{C}$<br>
      After $t = 16.0 \text{ hours}$ of diffusion, microprobe analysis determines that the zinc concentration is $C_x = 5.0 \text{ wt}\%$ at depth $x = 0.40 \text{ mm}$.
    </div>
    <ol type="a">
      <li>Calculate the normalized concentration ratio $\frac{C_x - C_0}{C_s - C_0}$.</li>
      <li>Determine the value of the argument $z = \frac{x}{2\sqrt{Dt}}$ from the error function table.</li>
      <li>Calculate the diffusion coefficient $D$ of zinc in copper at $800^\circ\text{C}$ in $\text{m}^2/\text{s}$ and in $\text{cm}^2/\text{s}$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Concentration Ratio Evaluation</div>
      $$\frac{C_x - C_0}{C_s - C_0} = \frac{5.0 - 0.0}{20.0 - 0.0} = \frac{5.0}{20.0} = 0.2500$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Finding Argument $z$ from Error Function Table</div>
      $$\frac{C_x - C_0}{C_s - C_0} = 1 - \text{erf}(z) = 0.2500 \implies \text{erf}(z) = 1.0000 - 0.2500 = 0.7500$$
      <p>From the error function table in Problem 13:</p>
      $$\text{erf}(0.80) = 0.7421, \quad \text{erf}(0.85) = 0.7707$$
      <p>Linear interpolation for $\text{erf}(z) = 0.7500$:</p>
      $$\frac{z - 0.80}{0.7500 - 0.7421} = \frac{0.85 - 0.80}{0.7707 - 0.7421} \implies \frac{z - 0.80}{0.0079} = \frac{0.05}{0.0286} = 1.7483$$
      $$z - 0.80 = 1.7483 \times 0.0079 = 0.0138 \implies z = \mathbf{0.8138}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation of Diffusion Coefficient $D$</div>
      <p>Diffusion time: $t = 16.0 \text{ hr} = 16.0 \times 3600 \text{ s} = 57,600 \text{ s}$.</p>
      <p>Depth: $x = 0.40 \text{ mm} = 4.0 \times 10^{-4} \text{ m}$.</p>
      <p>From $z = \frac{x}{2\sqrt{Dt}}$:</p>
      $$\sqrt{Dt} = \frac{x}{2 z} = \frac{4.0 \times 10^{-4} \text{ m}}{2 \times 0.8138} = \frac{4.0 \times 10^{-4} \text{ m}}{1.6276} = 2.4576 \times 10^{-4} \text{ m}$$
      <p>Squaring both sides:</p>
      $$Dt = (2.4576 \times 10^{-4} \text{ m})^2 = 6.0398 \times 10^{-8} \text{ m}^2$$
      $$D = \frac{6.0398 \times 10^{-8} \text{ m}^2}{57,600 \text{ s}} = \mathbf{1.049 \times 10^{-12} \text{ m}^2/\text{s}}$$
      <p>In $\text{cm}^2/\text{s}$ ($1 \text{ m}^2 = 10^4 \text{ cm}^2$):</p>
      $$D = 1.049 \times 10^{-12} \times 10^4 = \mathbf{1.05 \times 10^{-8} \text{ cm}^2/\text{s}}$$
    </div>
    <div class="final-answer-box">
      <strong>Concentration Ratio:</strong> $\frac{C_x-C_0}{C_s-C_0} = \mathbf{0.2500} \implies \text{erf}(z) = 0.7500$.<br>
      <strong>Interpolated Argument:</strong> $z = \mathbf{0.8138}$.<br>
      <strong>Diffusion Coefficient:</strong> $D = \mathbf{1.05 \times 10^{-12} \text{ m}^2/\text{s}} = \mathbf{1.05 \times 10^{-8} \text{ cm}^2/\text{s}}$.
    </div>""")

# P23: Nitriding Case Hardening
add(23, "Gas Nitriding of Steel: Nitrogen Penetration Depth and Hardness Layer Modeling",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Intermediate",
    r"""<p>Nitriding is a surface-hardening thermochemical treatment conducted in the ferrite phase ($\alpha$-Fe) at $525^\circ\text{C}$ to produce hard surface cases without requiring a subsequent quench.</p>
    <div style="text-align:center; margin: 10px 0;">
      Base alloy: Low-alloy steel ($C_0 = 0.005 \text{ wt}\%$ Nitrogen)<br>
      Nitriding potential maintains surface nitrogen at $C_s = 0.40 \text{ wt}\%$ at $525^\circ\text{C}$ ($798 \text{ K}$)<br>
      Diffusivity of Nitrogen in $\alpha$-Fe at $525^\circ\text{C}$: $D = 2.50 \times 10^{-12} \text{ m}^2/\text{s}$
    </div>
    <ol type="a">
      <li>Calculate the depth $x$ at which the nitrogen concentration reaches $0.10 \text{ wt}\%$ after a $12.0\text{-hour}$ nitriding cycle.</li>
      <li>Why does nitriding at $525^\circ\text{C}$ produce significantly less part distortion than carburizing at $950^\circ\text{C}$?</li>
      <li>How does the presence of strong nitride-forming alloying elements (e.g., Chromium, Aluminum, Vanadium) in Nitralloy steels increase case hardness to $> 1000 \text{ HV}$?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Nitrogen Case Depth Calculation ($t = 12.0 \text{ hr} = 43,200 \text{ s}$)</div>
      <p>Evaluate concentration ratio:</p>
      $$\frac{C_x - C_0}{C_s - C_0} = \frac{0.10 - 0.005}{0.40 - 0.005} = \frac{0.095}{0.395} = 0.2405$$
      $$\text{erf}(z) = 1.0000 - 0.2405 = 0.7595$$
      <p>From table: $\text{erf}(0.80) = 0.7421, \text{erf}(0.85) = 0.7707$.</p>
      $$z - 0.80 = \frac{0.7595 - 0.7421}{0.7707 - 0.7421} \times (0.05) = \frac{0.0174}{0.0286} \times 0.05 = 0.6084 \times 0.05 = 0.0304 \implies z = \mathbf{0.8304}$$
      <p>Compute penetration depth $x$:</p>
      $$2\sqrt{Dt} = 2 \sqrt{(2.50 \times 10^{-12} \text{ m}^2/\text{s}) \times (43,200 \text{ s})} = 2 \sqrt{1.080 \times 10^{-7} \text{ m}^2} = 2 \times (3.2863 \times 10^{-4} \text{ m}) = 6.573 \times 10^{-4} \text{ m}$$
      $$x = z \times (2\sqrt{Dt}) = 0.8304 \times (6.573 \times 10^{-4} \text{ m}) = 5.458 \times 10^{-4} \text{ m} = \mathbf{0.546 \text{ mm}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Why Nitriding Avoids Distortion</div>
      <p>Carburizing is performed at $900\text{--}950^\circ\text{C}$ in the FCC austenite regime and requires aggressive liquid oil/water quenching to transform austenite into martensite, generating massive thermal and transformation stresses that warp gears. Nitriding is performed at $525^\circ\text{C}$ entirely within the ferritic temperature window (below the $727^\circ\text{C}$ eutectoid). No phase transformation or quenching is involved; parts are slowly furnace-cooled, resulting in near-zero dimensional distortion.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Role of Alloying Elements ($\text{Cr, Al, V}$)</div>
      <p>In Nitralloy steels, dissolved Aluminum, Chromium, and Vanadium react with the diffusing nitrogen to precipitate coherent, ultra-fine sub-nanometer alloy nitrides ($\text{AlN}, \text{CrN}, \text{VN}$) within the ferrite grains. These ultra-dense coherent nanoprecipitates create massive dislocation glide resistance via the Orowan bypass mechanism, driving surface hardness to extreme values of $1000\text{--}1200 \text{ HV}$ (70 HRC), providing exceptional wear and anti-scuffing properties.</p>
    </div>
    <div class="final-answer-box">
      <strong>Nitriding Depth:</strong> $x = \mathbf{0.546 \text{ mm}}$ after 12 hours.<br>
      <strong>Zero Distortion:</strong> Performed below $A_1$ ($525^\circ\text{C}$) without phase transformation or quenching.<br>
      <strong>Extreme Hardness:</strong> Coherent precipitation of $\text{AlN}$ and $\text{CrN}$ nanoprecipitates.
    </div>""")

# P24: Dopant Diffusion Comparison (Phosphorus vs Boron in Silicon)
add(24, "Microelectronic Dopant Comparison: Phosphorus ($n$-type) vs. Boron ($p$-type) Junctions",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Intermediate",
    r"""<p>Silicon integrated circuits utilize group III elements (Boron, $p$-type) and group V elements (Phosphorus, Arsenic, $n$-type) for localized doping.</p>
    <div style="text-align:center; margin: 10px 0;">
      At $1000^\circ\text{C}$ ($1273 \text{ K}$):<br>
      Diffusivity of Boron: $D_{\text{B}} = 3.0 \times 10^{-14} \text{ cm}^2/\text{s}$<br>
      Diffusivity of Phosphorus: $D_{\text{P}} = 6.5 \times 10^{-14} \text{ cm}^2/\text{s}$<br>
      Diffusivity of Arsenic: $D_{\text{As}} = 2.0 \times 10^{-15} \text{ cm}^2/\text{s}$
    </div>
    <ol type="a">
      <li>Explain why Phosphorus diffuses more than twice as fast as Boron, while Arsenic diffuses more than 30 times slower than Phosphorus at the same temperature, relating this to covalent radii and interstitialcy migration.</li>
      <li>Calculate the diffusion lengths ($2\sqrt{Dt}$) for Phosphorus and Arsenic after a $1\text{-hour}$ anneal at $1000^\circ\text{C}$.</li>
      <li>Why is Arsenic strongly favored over Phosphorus for creating ultra-shallow source/drain junctions in sub-micron MOSFET transistors?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Atomic Radius and Diffusion Mechanism in Silicon</div>
      <p>Substitutional dopants in silicon migrate via an <strong>interstitialcy mechanism</strong> (kick-out and vacancy-assisted exchange). Phosphorus ($r_{\text{cov}} = 0.106 \text{ nm}$) is relatively small and forms mobile dopant-interstitial pairs ($(\text{P}-I)$) that migrate with low activation energy ($Q \approx 3.66 \text{ eV}$). Arsenic ($r_{\text{cov}} = 0.122 \text{ nm}$) has an atomic radius virtually identical to silicon ($0.118 \text{ nm}$); its large mass and size inhibit interstitialcy kick-out, causing it to migrate strictly via slower neutral vacancy exchanges ($Q \approx 4.05 \text{ eV}$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Diffusion Lengths after $1.0 \text{ hour}$ ($t = 3600 \text{ s}$)</div>
      <ul>
        <li><strong>For Phosphorus ($D_{\text{P}} = 6.5 \times 10^{-14} \text{ cm}^2/\text{s}$):</strong>
        $$2\sqrt{D_{\text{P}} t} = 2 \sqrt{(6.5 \times 10^{-14}) \times (3600)} = 2 \sqrt{2.34 \times 10^{-10} \text{ cm}^2} = 2 \times (1.5297 \times 10^{-5} \text{ cm}) = 3.059 \times 10^{-5} \text{ cm} = \mathbf{0.306 \mu\text{m} = 306 \text{ nm}}$$</li>
        <li><strong>For Arsenic ($D_{\text{As}} = 2.0 \times 10^{-15} \text{ cm}^2/\text{s}$):</strong>
        $$2\sqrt{D_{\text{As}} t} = 2 \sqrt{(2.0 \times 10^{-15}) \times (3600)} = 2 \sqrt{7.20 \times 10^{-12} \text{ cm}^2} = 2 \times (2.683 \times 10^{-6} \text{ cm}) = 5.367 \times 10^{-6} \text{ cm} = \mathbf{0.0537 \mu\text{m} = 53.7 \text{ nm}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Why Arsenic is Preferred for Ultra-Shallow MOSFET Junctions</div>
      <p>In advanced nanometer CMOS transistors, source and drain junctions must have extremely shallow depths ($x_j < 20\text{--}50 \text{ nm}$) to prevent drain-induced barrier lowering (short-channel effects). Phosphorus diffuses so rapidly ($306 \text{ nm/hr}$) that during the thermal budget required to activate implants, it diffuses deeply into the channel, causing catastrophic punch-through leakage. Arsenic's extremely slow diffusivity ($54 \text{ nm/hr}$, nearly $6\times$ shorter penetration) allows the formation of razor-sharp, ultra-shallow, steep dopant profiles that maintain strict short-channel control.</p>
    </div>
    <div class="final-answer-box">
      <strong>Diffusion Lengths ($1\text{ hr}$):</strong> Phosphorus: $\mathbf{306 \text{ nm}}$ &bull; Arsenic: $\mathbf{53.7 \text{ nm}}$.<br>
      <strong>CMOS Advantage:</strong> Arsenic's slow diffusivity prevents lateral and vertical channel encroachment, enabling ultra-shallow source/drain junctions.
    </div>""")

# P25: Time-Integrated Surface Influx
add(25, "Time-Dependent Surface Flux and Total Solute Mass Uptake ($M_t = 2(C_s - C_0)\\sqrt{Dt/\\pi}$)",
    "Non-Steady-State Diffusion (Fick II)", "fick_second_law", "Advanced",
    r"""<p>To determine the total quantity of gas or solute absorbed by a workpiece during a non-steady-state process, the instantaneous surface flux must be integrated over time.</p>
    <ol type="a">
      <li>Differentiating the error function solution with respect to $x$, derive the expression for the <strong>instantaneous surface diffusion flux</strong> $J_0(t) = -D \left.\frac{\partial C}{\partial x}\right|_{x=0}$:
      $$J_0(t) = (C_s - C_0)\sqrt{\frac{D}{\pi t}}$$
      Explain why surface flux is theoretically infinite at $t = 0$ and decays as $1/\sqrt{t}$.</li>
      <li>Integrate $J_0(t)$ from $t = 0$ to $t$ to derive the equation for the <strong>total solute mass absorbed per unit surface area $M_t$</strong>:
      $$M_t = 2 (C_s - C_0) \sqrt{\frac{Dt}{\pi}}$$</li>
      <li>A steel billet ($C_0 = 0.20 \text{ wt}\% = 15.6 \text{ kg/m}^3$) with total surface area $A = 2.5 \text{ m}^2$ is carburized at $950^\circ\text{C}$ ($D = 1.28 \times 10^{-11} \text{ m}^2/\text{s}, C_s = 1.20 \text{ wt}\% = 93.6 \text{ kg/m}^3$) for $t = 6.0 \text{ hours}$. Calculate:
        <ul>
          <li>The instantaneous surface flux $J_0$ at the end of 6 hours in $\text{g}/(\text{m}^2\cdot\text{hr})$.</li>
          <li>The total mass of carbon absorbed by the entire billet in kilograms ($\text{kg}$).</li>
        </ul>
      </li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Instantaneous Surface Flux $J_0(t)$</div>
      <p>From the semi-infinite solution:</p>
      $$C(x,t) = C_0 + (C_s - C_0)\left[1 - \frac{2}{\sqrt{\pi}} \int_0^{\frac{x}{2\sqrt{Dt}}} e^{-\eta^2} d\eta\right]$$
      <p>Differentiating with respect to $x$ using Leibniz's rule:</p>
      $$\frac{\partial C}{\partial x} = -(C_s - C_0) \frac{2}{\sqrt{\pi}} \exp\left(-\frac{x^2}{4Dt}\right) \frac{\partial}{\partial x}\left(\frac{x}{2\sqrt{Dt}}\right) = -\frac{C_s - C_0}{\sqrt{\pi D t}} \exp\left(-\frac{x^2}{4Dt}\right)$$
      <p>Evaluating at the surface $x = 0$ ($\exp(0) = 1$):</p>
      $$\left.\frac{\partial C}{\partial x}\right|_{x=0} = -\frac{C_s - C_0}{\sqrt{\pi D t}}$$
      <p>Applying Fick's first law $J_0 = -D \left.\frac{\partial C}{\partial x}\right|_{x=0}$:</p>
      $$J_0(t) = -D \left(-\frac{C_s - C_0}{\sqrt{\pi D t}}\right) = (C_s - C_0) \frac{D}{\sqrt{\pi D t}} = \mathbf{(C_s - C_0) \sqrt{\frac{D}{\pi t}}}$$
      <p>At $t \to 0$, the concentration step is infinitely steep ($\partial C/\partial x \to -\infty$), yielding infinite initial flux. As a saturated boundary layer forms, the diffusion barrier thickens, causing flux to decay as $1/\sqrt{t}$.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Derivation of Total Solute Mass Absorbed $M_t$</div>
      <p>The total mass absorbed per unit surface area up to time $t$ is the time integral of surface flux:</p>
      $$M_t = \int_0^t J_0(t') dt' = \int_0^t (C_s - C_0) \sqrt{\frac{D}{\pi}} (t')^{-1/2} dt' = (C_s - C_0) \sqrt{\frac{D}{\pi}} \left[ \frac{(t')^{1/2}}{1/2} \right]_0^t$$
      $$M_t = 2 (C_s - C_0) \sqrt{\frac{Dt}{\pi}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for Steel Billet ($t = 6.0 \text{ hr} = 21,600 \text{ s}, A = 2.5 \text{ m}^2$)</div>
      <p>Given $\Delta C = C_s - C_0 = 93.6 - 15.6 = 78.0 \text{ kg/m}^3$, $D = 1.28 \times 10^{-11} \text{ m}^2/\text{s}$:</p>
      <ul>
        <li><strong>Instantaneous Surface Flux at $t = 21,600 \text{ s}$:</strong>
        $$\sqrt{\frac{D}{\pi t}} = \sqrt{\frac{1.28 \times 10^{-11}}{\pi \times 21,600}} = \sqrt{\frac{1.28 \times 10^{-11}}{67,858}} = \sqrt{1.8863 \times 10^{-16}} = 1.3734 \times 10^{-8} \text{ m/s}$$
        $$J_0 = (78.0 \text{ kg/m}^3) \times (1.3734 \times 10^{-8} \text{ m/s}) = 1.0713 \times 10^{-6} \text{ kg}/(\text{m}^2\cdot\text{s})$$
        <p>Convert to $\text{g}/(\text{m}^2\cdot\text{hr})$ ($1 \text{ kg} = 1000 \text{ g}, 1 \text{ hr} = 3600 \text{ s}$):</p>
        $$J_0 = (1.0713 \times 10^{-6}) \times 1000 \times 3600 = \mathbf{3.857 \text{ g}/(\text{m}^2\cdot\text{hr})}$$</li>
        <li><strong>Total Mass Absorbed by Billet:</strong>
        $$M_t = 2 (78.0 \text{ kg/m}^3) \sqrt{\frac{(1.28 \times 10^{-11}) \times (21,600)}{\pi}} = 156.0 \times \sqrt{\frac{2.7648 \times 10^{-7}}{\pi}} = 156.0 \times \sqrt{8.8006 \times 10^{-8}}$$
        $$M_t = 156.0 \times (2.9666 \times 10^{-4} \text{ m}) = 0.04628 \text{ kg/m}^2 = 46.28 \text{ g/m}^2$$
        <p>Total mass for entire area $A = 2.5 \text{ m}^2$:</p>
        $$m_{\text{total}} = M_t \times A = (0.04628 \text{ kg/m}^2) \times (2.5 \text{ m}^2) = \mathbf{0.1157 \text{ kg} = 115.7 \text{ grams}}$$
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Surface Flux Formula:</strong> $$J_0(t) = (C_s - C_0)\sqrt{\frac{D}{\pi t}} \implies J_0(6\text{ hr}) = \mathbf{3.86 \text{ g/(m}^2\cdot\text{hr)}}$$
      <strong>Total Mass Formula:</strong> $$M_t = 2(C_s - C_0)\sqrt{\frac{Dt}{\pi}} \implies m_{\text{total}} = \mathbf{115.7 \text{ grams}}$$ of carbon absorbed.
    </div>""")

# Save checkpoint for part 1 (1 to 25)
print("Ch 5 Part 1: All P1-P25 written successfully!")
