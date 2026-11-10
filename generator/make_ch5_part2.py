# generator/make_ch5_part2.py
# ==============================================================================
# CHAPTER 5: DIFFUSION IN SOLIDS - PART 2 (PROBLEMS 26 TO 50)
# Course: Science of Materials | University of Tehran | Prof. Sadeghi
# Prepared by TA Sina Sharifi
# ==============================================================================

import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_ch5_part1

P = make_ch5_part1.P
add = make_ch5_part1.add

# P26: Arrhenius Equation Formulation
add(26, "Temperature Dependence of Diffusion: The Arrhenius Equation and Activation Energy",
    "Arrhenius Law & Energetics", "arrhenius_law", "Fundamental",
    r"""<p>The rate of atomic diffusion increases exponentially with temperature following an Arrhenius relationship.</p>
    <ol type="a">
      <li>State the <strong>Arrhenius equation</strong> for the diffusion coefficient:
      $$D = D_0 \exp\left(-\frac{Q_d}{R T}\right) = D_0 \exp\left(-\frac{Q_d}{k_B T}\right)$$
      Define all variables and state their standard units.</li>
      <li>Explain the microscopic physical meaning of:
        <ul>
          <li>The <strong>pre-exponential factor $D_0$</strong> (frequency factor, jump distance $\alpha a$, vibrational frequency $\nu_0$, and activation entropy $\Delta S$).</li>
          <li>The <strong>activation energy $Q_d$</strong> for vacancy diffusion ($\Delta H_f + \Delta H_m$) versus interstitial diffusion ($\Delta H_m$).</li>
        </ul>
      </li>
      <li>Why does a plot of $\ln D$ versus $1/T$ yield a straight line? State the physical interpretation of the line's slope and $y$-intercept.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): The Arrhenius Equation and Units</div>
      $$D = D_0 \exp\left(-\frac{Q_d}{R T}\right)$$
      <ul>
        <li>$D$: Diffusion coefficient at absolute temperature $T$ ($\mathbf{\text{m}^2/\text{s}}$).</li>
        <li>$D_0$: Temperature-independent pre-exponential factor ($\mathbf{\text{m}^2/\text{s}}$).</li>
        <li>$Q_d$: Activation energy for diffusion ($\mathbf{\text{J/mol}}$ or $\mathbf{\text{kJ/mol}}$ when using gas constant $R = 8.314 \text{ J/(mol}\cdot\text{K)}$; or $\mathbf{\text{eV/atom}}$ when using Boltzmann's constant $k_B = 8.617 \times 10^{-5} \text{ eV/K}$).</li>
        <li>$T$: Absolute temperature in Kelvin ($\mathbf{\text{K}}$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Microscopic Physical Meaning of $D_0$ and $Q_d$</div>
      <ul>
        <li><strong>Pre-exponential Factor $D_0$:</strong>
          From random walk theory, $D = \frac{1}{6} \alpha z a^2 \Gamma$, where $a$ is jump distance, $z$ is coordination number, and $\Gamma$ is successful jump frequency. Transition state theory expresses $D_0$ as:
          $$D_0 = \frac{1}{6} \alpha z a^2 \nu_0 \exp\left(\frac{\Delta S}{R}\right)$$
          where $\nu_0$ is the Debye vibrational frequency ($\sim 10^{13} \text{ s}^{-1}$) and $\Delta S$ is the activation entropy due to lattice distortion during the atomic jump.</li>
        <li><strong>Activation Energy $Q_d$:</strong>
          The potential energy barrier that an atom must overcome to execute a successful jump:
          <ul>
            <li>For <em>substitutional / self-diffusion</em>: $Q_d = \Delta H_f + \Delta H_m$ (energy to form a vacancy plus energy to move into it).</li>
            <li>For <em>interstitial diffusion</em>: $Q_d = \Delta H_m$ (energy to migrate through interstitial bottlenecks; vacancy formation energy is zero).</li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Arrhenius Plot Interpretation</div>
      <p>Taking the natural logarithm of the Arrhenius equation:</p>
      $$\ln D = \ln D_0 - \left(\frac{Q_d}{R}\right) \frac{1}{T}$$
      <p>This matches the standard linear form $y = m x + c$, where $y = \ln D$ and $x = \frac{1}{T}$:</p>
      <ul>
        <li><strong>Slope:</strong> $m = -\frac{Q_d}{R} \implies Q_d = -R \times \text{slope}$.</li>
        <li><strong>$y$-Intercept:</strong> $c = \ln D_0 \implies D_0 = e^c$.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Arrhenius Law:</strong> $$D = D_0 \exp\left(-\frac{Q_d}{RT}\right), \quad \ln D = \ln D_0 - \frac{Q_d}{R}\left(\frac{1}{T}\right)$$
      Slope $= -Q_d/R$ &bull; Intercept $= \ln D_0$.<br>
      $Q_d = \Delta H_f + \Delta H_m$ for substitutional; $Q_d = \Delta H_m$ for interstitial.
    </div>""")

# P27: Arrhenius Two-Point Calculation
add(27, "Two-Point Arrhenius Analysis: Determining $Q_d$ and $D_0$ from Experimental Data",
    "Arrhenius Law & Energetics", "arrhenius_law", "Intermediate",
    r"""<p>The diffusion coefficient of nickel in copper is measured at two different temperatures:</p>
    <div style="text-align:center; margin: 10px 0;">
      At $T_1 = 1000 \text{ K}$ ($727^\circ\text{C}$): $D_1 = 5.40 \times 10^{-16} \text{ m}^2/\text{s}$<br>
      At $T_2 = 1200 \text{ K}$ ($927^\circ\text{C}$): $D_2 = 6.80 \times 10^{-14} \text{ m}^2/\text{s}$<br>
      Universal Gas Constant: $R = 8.314 \text{ J/(mol}\cdot\text{K)}$
    </div>
    <ol type="a">
      <li>Derive the algebraic equation for the activation energy $Q_d$ using data at two temperatures.</li>
      <li>Calculate $Q_d$ in kilojoules per mole ($\text{kJ/mol}$) and in electron-volts per atom ($\text{eV/atom}$).</li>
      <li>Calculate the pre-exponential factor $D_0$ in $\text{m}^2/\text{s}$.</li>
      <li>Predict the diffusion coefficient of nickel in copper at $T_3 = 1300 \text{ K}$ ($1027^\circ\text{C}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Algebraic Derivation for $Q_d$</div>
      $$\ln D_1 = \ln D_0 - \frac{Q_d}{R T_1}, \quad \ln D_2 = \ln D_0 - \frac{Q_d}{R T_2}$$
      <p>Subtracting the first equation from the second:</p>
      $$\ln\left(\frac{D_2}{D_1}\right) = -\frac{Q_d}{R} \left(\frac{1}{T_2} - \frac{1}{T_1}\right) = \frac{Q_d}{R} \left(\frac{T_2 - T_1}{T_1 T_2}\right)$$
      $$Q_d = \frac{R \ln(D_2 / D_1)}{\frac{1}{T_1} - \frac{1}{T_2}} = \frac{R T_1 T_2}{T_2 - T_1} \ln\left(\frac{D_2}{D_1}\right)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation of Activation Energy $Q_d$</div>
      $$\frac{D_2}{D_1} = \frac{6.80 \times 10^{-14}}{5.40 \times 10^{-16}} = 125.926 \implies \ln(125.926) = 4.8357$$
      $$\frac{1}{T_1} - \frac{1}{T_2} = \frac{1}{1000} - \frac{1}{1200} = 1.000 \times 10^{-3} - 8.3333 \times 10^{-4} = 1.6667 \times 10^{-4} \text{ K}^{-1}$$
      $$Q_d = \frac{(8.314 \text{ J/(mol}\cdot\text{K)}) \times 4.8357}{1.6667 \times 10^{-4} \text{ K}^{-1}} = 241,250 \text{ J/mol} = \mathbf{241.3 \text{ kJ/mol}}$$
      <p>Convert to $\text{eV/atom}$ ($1 \text{ eV/atom} = 96.485 \text{ kJ/mol}$):</p>
      $$Q_d = \frac{241.3 \text{ kJ/mol}}{96.485 \text{ kJ/(mol}\cdot\text{eV)}} = \mathbf{2.50 \text{ eV/atom}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation of Pre-Exponential Factor $D_0$</div>
      $$D_0 = D_1 \exp\left(\frac{Q_d}{R T_1}\right)$$
      $$\frac{Q_d}{R T_1} = \frac{241,250 \text{ J/mol}}{(8.314 \text{ J/(mol}\cdot\text{K)}) \times (1000 \text{ K})} = \frac{241,250}{8314} = 29.0173$$
      $$D_0 = (5.40 \times 10^{-16} \text{ m}^2/\text{s}) \times \exp(29.0173) = (5.40 \times 10^{-16}) \times (4.0098 \times 10^{12}) = \mathbf{2.165 \times 10^{-3} \text{ m}^2/\text{s} \approx 2.2 \times 10^{-3} \text{ m}^2/\text{s}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Predicted Diffusivity at $T_3 = 1300 \text{ K}$</div>
      $$\frac{Q_d}{R T_3} = \frac{241,250}{8.314 \times 1300} = \frac{241,250}{10,808.2} = 22.321$$
      $$D_3 = (2.165 \times 10^{-3} \text{ m}^2/\text{s}) \times \exp(-22.321) = (2.165 \times 10^{-3}) \times (2.0235 \times 10^{-10}) = \mathbf{4.38 \times 10^{-13} \text{ m}^2/\text{s}}$$
    </div>
    <div class="final-answer-box">
      <strong>Activation Energy:</strong> $Q_d = \mathbf{241.3 \text{ kJ/mol}} = \mathbf{2.50 \text{ eV/atom}}$.<br>
      <strong>Pre-Exponential Factor:</strong> $D_0 = \mathbf{2.17 \times 10^{-3} \text{ m}^2/\text{s}}$.<br>
      <strong>Predicted Diffusivity at $1300 \text{ K}$:</strong> $D = \mathbf{4.38 \times 10^{-13} \text{ m}^2/\text{s}}$.
    </div>""")

# P28: Linear Regression on Arrhenius Data
add(28, "Least-Squares Linear Regression on Arrhenius Data for Iron Self-Diffusion",
    "Arrhenius Law & Energetics", "arrhenius_law", "Advanced",
    r"""<p>Experimental tracer self-diffusion coefficients for pure FCC $\gamma$-iron are measured at four temperatures:</p>
    <table class="table-styled">
      <thead><tr><th>Temperature $T$ ($^\circ\text{C}$)</th><th>Temperature $T$ (K)</th><th>$1/T$ ($10^{-4} \text{ K}^{-1}$)</th><th>Diffusivity $D$ ($\text{m}^2/\text{s}$)</th><th>$\ln D$</th></tr></thead>
      <tbody>
        <tr><td>$950$</td><td>$1223$</td><td>$8.177$</td><td>$1.85 \times 10^{-16}$</td><td>$-36.228$</td></tr>
        <tr><td>$1050$</td><td>$1323$</td><td>$7.559$</td><td>$1.80 \times 10^{-15}$</td><td>$-33.951$</td></tr>
        <tr><td>$1150$</td><td>$1423$</td><td>$7.027$</td><td>$1.25 \times 10^{-14}$</td><td>$-32.012$</td></tr>
        <tr><td>$1250$</td><td>$1523$</td><td>$6.566$</td><td>$6.40 \times 10^{-14}$</td><td>$-30.380$</td></tr>
      </tbody>
    </table>
    <ol type="a">
      <li>Apply linear regression ($y = m x + c$, where $y = \ln D$ and $x = 1/T$) to compute the best-fit slope $m$ and correlation coefficient $r^2$.</li>
      <li>Calculate the activation energy for self-diffusion in FCC iron ($Q_d$) in $\text{kJ/mol}$.</li>
      <li>Calculate the pre-exponential factor $D_0$ in $\text{m}^2/\text{s}$.</li>
      <li>State the resulting Arrhenius equation for $\gamma$-Fe self-diffusion.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Linear Regression Computations</div>
      <p>Let $x_i = 1/T_i$ and $y_i = \ln D_i$ for $N = 4$ points:</p>
      <ul>
        <li>$\sum x = 8.177 + 7.559 + 7.027 + 6.566 = 29.329 \times 10^{-4} \text{ K}^{-1} \implies \bar{x} = 7.3323 \times 10^{-4}$</li>
        <li>$\sum y = -36.228 - 33.951 - 32.012 - 30.380 = -132.571 \implies \bar{y} = -33.1428$</li>
        <li>$\sum (x_i - \bar{x})^2 = (0.8447)^2 + (0.2267)^2 + (-0.3053)^2 + (-0.7663)^2 = (0.7135 + 0.0514 + 0.0932 + 0.5872) \times 10^{-8} = 1.4453 \times 10^{-8}$</li>
        <li>$\sum (x_i - \bar{x})(y_i - \bar{y}) = (0.8447)(-3.085) + (0.2267)(-0.808) + (-0.3053)(1.131) + (-0.7663)(2.763) = (-2.606 - 0.183 - 0.345 - 2.117) \times 10^{-4} = -5.251 \times 10^{-4}$</li>
      </ul>
      <p>The best-fit slope is:</p>
      $$m = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{-5.251 \times 10^{-4}}{1.4453 \times 10^{-8}} = \mathbf{-36,331 \text{ K}}$$
      <p>The correlation coefficient is $r^2 = 0.9998$, confirming near-perfect Arrhenius linearity.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation of Activation Energy $Q_d$</div>
      <p>Since slope $m = -\frac{Q_d}{R}$:</p>
      $$Q_d = -R \cdot m = -(8.314 \text{ J/(mol}\cdot\text{K)}) \times (-36,331 \text{ K}) = 302,056 \text{ J/mol} = \mathbf{302.1 \text{ kJ/mol}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation of Pre-Exponential Factor $D_0$</div>
      <p>The $y$-intercept is:</p>
      $$c = \bar{y} - m \bar{x} = -33.1428 - (-36,331) \times (7.3323 \times 10^{-4}) = -33.1428 + 26.6399 = \mathbf{-6.5029}$$
      $$D_0 = \exp(c) = \exp(-6.5029) = \mathbf{1.50 \times 10^{-3} \text{ m}^2/\text{s}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Final Arrhenius Equation</div>
      $$D(T) = (1.50 \times 10^{-3} \text{ m}^2/\text{s}) \exp\left(-\frac{302.1 \text{ kJ/mol}}{R T}\right)$$
    </div>
    <div class="final-answer-box">
      <strong>Arrhenius Parameters:</strong><br>
      $Q_d = \mathbf{302.1 \text{ kJ/mol}}$ ($3.13\text{ eV/atom}$) &bull; $D_0 = \mathbf{1.50 \times 10^{-3} \text{ m}^2/\text{s}}$ ($r^2 = 0.9998$).<br>
      <strong>Equation:</strong> $$D = 1.50 \times 10^{-3}\exp\left(-\frac{302,100}{RT}\right) \text{ m}^2/\text{s}$$
    </div>""")

# P29: Atomic Jump Frequency Calculation
add(29, "Microscopic Diffusion Kinetics: Mean Atomic Jump Frequency and Residence Time",
    "Arrhenius Law & Energetics", "arrhenius_law", "Intermediate",
    r"""<p>Diffusion coefficients directly reflect the microscopic rate at which individual atoms jump between lattice positions.</p>
    <ol type="a">
      <li>From Einstein's random walk theory in a 3D isotropic crystal:
      $$D = \frac{1}{6} \Gamma \lambda^2$$
      where $\Gamma$ is the successful atomic jump frequency ($\text{jumps/s}$) and $\lambda$ is the jump distance. Derive the formula for $\Gamma$ as a function of $D$ and $\lambda$.</li>
      <li>For pure Copper ($a = 0.3615 \text{ nm}$, FCC), nearest-neighbor jump distance is $\lambda = \frac{a\sqrt{2}}{2}$. Calculate $\lambda$ in nanometers and meters.</li>
      <li>At $T = 800^\circ\text{C}$ ($1073 \text{ K}$), the self-diffusivity of copper is $D = 2.0 \times 10^{-16} \text{ m}^2/\text{s}$. Calculate:
        <ul>
          <li>The atomic jump frequency $\Gamma$ ($\text{jumps/s}$).</li>
          <li>The average residence time $\tau = 1/\Gamma$ that a copper atom spends on a single lattice site before making a jump.</li>
        </ul>
      </li>
      <li>Compare $\Gamma$ at $800^\circ\text{C}$ with the atomic vibrational frequency ($\nu_0 \approx 10^{13} \text{ s}^{-1}$), and determine what fraction of lattice vibrations result in a successful jump.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Jump Frequency $\Gamma$</div>
      <p>In a 3D random walk with step length $\lambda$ and jump rate $\Gamma$:</p>
      $$\langle r^2 \rangle = \Gamma t \lambda^2 = 6 D t \implies D = \frac{1}{6} \Gamma \lambda^2 \implies \Gamma = \frac{6 D}{\lambda^2}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Jump Distance in FCC Copper ($a = 0.3615 \text{ nm}$)</div>
      <p>In FCC, nearest neighbors lie along the face diagonal $\frac{a}{2}\langle 110\rangle$:</p>
      $$\lambda = \frac{a\sqrt{2}}{2} = \frac{0.3615 \text{ nm} \times 1.4142}{2} = \mathbf{0.2556 \text{ nm} = 2.556 \times 10^{-10} \text{ m}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for Copper at $800^\circ\text{C}$</div>
      $$\lambda^2 = (2.556 \times 10^{-10} \text{ m})^2 = 6.533 \times 10^{-20} \text{ m}^2$$
      $$\Gamma = \frac{6 \times (2.0 \times 10^{-16} \text{ m}^2/\text{s})}{6.533 \times 10^{-20} \text{ m}^2} = \frac{1.20 \times 10^{-15}}{6.533 \times 10^{-20}} = \mathbf{18,368 \text{ jumps/s} \approx 1.84 \times 10^4 \text{ jumps/s}}$$
      <p>The average residence time is:</p>
      $$\tau = \frac{1}{\Gamma} = \frac{1}{18,368 \text{ s}^{-1}} = \mathbf{5.44 \times 10^{-5} \text{ seconds} = 54.4 \mu\text{s}}$$
      <p>At $800^\circ\text{C}$, a copper atom stays on its lattice site for about 54 microseconds before jumping to an adjacent vacancy.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Success Fraction of Vibrational Attempts</div>
      $$\text{Success Fraction} = \frac{\Gamma}{\nu_0} = \frac{1.84 \times 10^4 \text{ s}^{-1}}{1.0 \times 10^{13} \text{ s}^{-1}} = \mathbf{1.84 \times 10^{-9}}$$
      <p>Only about <strong>2 out of every billion atomic vibrations</strong> possess sufficient thermal energy and an adjacent vacancy to successfully execute a lattice jump!</p>
    </div>
    <div class="final-answer-box">
      <strong>Jump Distance:</strong> $\lambda = \mathbf{0.2556 \text{ nm}}$.<br>
      <strong>Jump Frequency:</strong> $\Gamma = \mathbf{1.84 \times 10^4 \text{ jumps/s}}$ &bull; <strong>Residence Time:</strong> $\tau = \mathbf{54.4 \mu\text{s}}$.<br>
      <strong>Success Probability:</strong> Only $\mathbf{1.8 \times 10^{-9}}$ of lattice vibrations produce a successful jump.
    </div>""")

# P30: Carbon in Austenite Jump Frequency
add(30, "Interstitial Jump Frequency: Carbon Atom Mobility in Austenite at $1000^\circ\text{C}$",
    "Arrhenius Law & Energetics", "arrhenius_law", "Intermediate",
    r"""<p>Because interstitial solutes do not require a vacancy to jump, their jump frequencies are vastly higher than substitutional atoms.</p>
    <div style="text-align:center; margin: 10px 0;">
      Lattice parameter of FCC $\gamma$-Fe at $1000^\circ\text{C}$: $a = 0.364 \text{ nm}$<br>
      Diffusivity of Carbon in $\gamma$-Fe at $1000^\circ\text{C}$: $D_{\text{C}} = 2.0 \times 10^{-11} \text{ m}^2/\text{s}$
    </div>
    <ol type="a">
      <li>In FCC, octahedral interstitial sites lie at edge midpoints $(a/2, 0, 0)$ and body center $(a/2, a/2, a/2)$. Calculate the jump distance $\lambda$ between adjacent octahedral interstitial sites.</li>
      <li>Calculate the jump frequency $\Gamma$ ($\text{jumps/s}$) of a carbon atom in austenite at $1000^\circ\text{C}$.</li>
      <li>Compare this jump frequency with the self-diffusion jump frequency of copper computed in Problem 29, and determine the acceleration ratio.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Interstitial Jump Distance in FCC</div>
      <p>The vector connecting an edge center $(a/2, 0, 0)$ to the adjacent body center $(a/2, a/2, a/2)$ is $(0, a/2, a/2)$. The distance is:</p>
      $$\lambda = \sqrt{0^2 + \left(\frac{a}{2}\right)^2 + \left(\frac{a}{2}\right)^2} = \frac{a\sqrt{2}}{2} = \frac{a}{\sqrt{2}}$$
      $$\lambda = \frac{0.364 \text{ nm}}{\sqrt{2}} = \mathbf{0.2574 \text{ nm} = 2.574 \times 10^{-10} \text{ m}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Jump Frequency Calculation</div>
      $$\lambda^2 = (2.574 \times 10^{-10} \text{ m})^2 = 6.625 \times 10^{-20} \text{ m}^2$$
      $$\Gamma = \frac{6 D}{\lambda^2} = \frac{6 \times (2.0 \times 10^{-11} \text{ m}^2/\text{s})}{6.625 \times 10^{-20} \text{ m}^2} = \frac{1.20 \times 10^{-10}}{6.625 \times 10^{-20}} = \mathbf{1.81 \times 10^9 \text{ jumps/s}}$$
      <p>A dissolved carbon atom jumps nearly <strong>2 billion times every second</strong> at $1000^\circ\text{C}$! Its residence time is less than one nanosecond ($\tau \approx 0.55 \text{ ns}$).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Comparison with Substitutional Jump Rate</div>
      $$\frac{\Gamma_{\text{interstitial}}}{\Gamma_{\text{substitutional}}} = \frac{1.81 \times 10^9 \text{ s}^{-1}}{1.84 \times 10^4 \text{ s}^{-1}} \approx \mathbf{100,000 \times}$$
      <p>Interstitial carbon executes jumps <strong>100,000 times more frequently</strong> than substitutional atoms at comparable temperatures because all adjacent interstitial sites are vacant and migration barriers are low.</p>
    </div>
    <div class="final-answer-box">
      <strong>Jump Distance:</strong> $\lambda = \mathbf{0.2574 \text{ nm}}$.<br>
      <strong>Carbon Jump Frequency:</strong> $\Gamma = \mathbf{1.81 \times 10^9 \text{ jumps/s}}$ ($\sim 2$ billion jumps per second!).<br>
      Carbon jumps $\mathbf{10^5\times}$ faster than substitutional host atoms.
    </div>""")

# Save checkpoint for part 2 (26 to 30)
print("Ch 5 Part 2: P26-P30 written.")
# P31: Interstitial vs Substitutional Energetics in Iron
add(31, "Activation Energy Disparity: Interstitial Carbon vs. Substitutional Iron in Austenite",
    "Arrhenius Law & Energetics", "arrhenius_law", "Intermediate",
    r"""<p>The thermodynamic and kinetic contrast between interstitial and substitutional diffusion is illustrated dramatically by the behavior of iron and carbon in austenite.</p>
    <div style="text-align:center; margin: 10px 0;">
      Carbon in $\gamma$-Fe: $D_0 = 2.3 \times 10^{-5} \text{ m}^2/\text{s}, \quad Q_d = 148 \text{ kJ/mol}$ ($1.53 \text{ eV}$)<br>
      Iron self-diffusion in $\gamma$-Fe: $D_0 = 6.5 \times 10^{-5} \text{ m}^2/\text{s}, \quad Q_d = 284 \text{ kJ/mol}$ ($2.94 \text{ eV}$)
    </div>
    <ol type="a">
      <li>Calculate the diffusion coefficients of Carbon ($D_{\text{C}}$) and Iron ($D_{\text{Fe}}$) in austenite at $950^\circ\text{C}$ ($1223 \text{ K}$).</li>
      <li>Calculate the ratio $D_{\text{C}} / D_{\text{Fe}}$ at $950^\circ\text{C}$.</li>
      <li>Repeat the calculation at $1150^\circ\text{C}$ ($1423 \text{ K}$) and calculate the new ratio. Explain why the ratio decreases as temperature increases.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Calculations at $950^\circ\text{C}$ ($1223 \text{ K}$)</div>
      <p>$R T_1 = (8.314 \text{ J/(mol}\cdot\text{K)}) \times (1223 \text{ K}) = 10,168 \text{ J/mol} = 10.168 \text{ kJ/mol}$.</p>
      <ul>
        <li><strong>Carbon Diffusivity:</strong>
        $$D_{\text{C}} = (2.3 \times 10^{-5}) \exp\left(-\frac{148.0}{10.168}\right) = (2.3 \times 10^{-5}) \exp(-14.555) = \mathbf{1.107 \times 10^{-11} \text{ m}^2/\text{s}}$$</li>
        <li><strong>Iron Self-Diffusivity:</strong>
        $$D_{\text{Fe}} = (6.5 \times 10^{-5}) \exp\left(-\frac{284.0}{10.168}\right) = (6.5 \times 10^{-5}) \exp(-27.931) = \mathbf{4.814 \times 10^{-17} \text{ m}^2/\text{s}}$$</li>
      </ul>
      <p>Ratio at $950^\circ\text{C}$:</p>
      $$\frac{D_{\text{C}}}{D_{\text{Fe}}} = \frac{1.107 \times 10^{-11}}{4.814 \times 10^{-17}} = \mathbf{230,000 \approx 2.3 \times 10^5}$$
      <p>At $950^\circ\text{C}$, carbon diffuses 230,000 times faster than iron!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations at $1150^\circ\text{C}$ ($1423 \text{ K}$)</div>
      <p>$R T_2 = (8.314) \times (1423) = 11,831 \text{ J/mol} = 11.831 \text{ kJ/mol}$.</p>
      <ul>
        <li><strong>Carbon Diffusivity:</strong>
        $$D_{\text{C}} = (2.3 \times 10^{-5}) \exp\left(-\frac{148.0}{11.831}\right) = (2.3 \times 10^{-5}) \exp(-12.509) = \mathbf{8.455 \times 10^{-11} \text{ m}^2/\text{s}}$$</li>
        <li><strong>Iron Self-Diffusivity:</strong>
        $$D_{\text{Fe}} = (6.5 \times 10^{-5}) \exp\left(-\frac{284.0}{11.831}\right) = (6.5 \times 10^{-5}) \exp(-24.005) = \mathbf{2.430 \times 10^{-15} \text{ m}^2/\text{s}}$$</li>
      </ul>
      <p>Ratio at $1150^\circ\text{C}$:</p>
      $$\frac{D_{\text{C}}}{D_{\text{Fe}}} = \frac{8.455 \times 10^{-11}}{2.430 \times 10^{-15}} = \mathbf{34,800 \approx 3.5 \times 10^4}$$
      <p><strong>Physical Explanation:</strong> Because iron self-diffusion has a much higher activation energy ($284 \text{ kJ/mol}$ vs $148 \text{ kJ/mol}$), its Arrhenius slope is much steeper. As temperature increases, the process with the higher activation energy accelerates much more rapidly, shrinking the kinetic disparity from $230,000\times$ at $950^\circ\text{C}$ down to $35,000\times$ at $1150^\circ\text{C}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>At $950^\circ\text{C}$:</strong> $D_{\text{C}} = \mathbf{1.11 \times 10^{-11} \text{ m}^2/\text{s}}$, $D_{\text{Fe}} = \mathbf{4.81 \times 10^{-17} \text{ m}^2/\text{s}}$ &bull; Ratio $= \mathbf{2.3 \times 10^5\times}$.<br>
      <strong>At $1150^\circ\text{C}$:</strong> $D_{\text{C}} = \mathbf{8.46 \times 10^{-11} \text{ m}^2/\text{s}}$, $D_{\text{Fe}} = \mathbf{2.43 \times 10^{-15} \text{ m}^2/\text{s}}$ &bull; Ratio $= \mathbf{3.5 \times 10^4\times}$.<br>
      Higher-activation processes accelerate faster with increasing temperature.
    </div>""")

# P32: Allotropy and Diffusion: BCC vs FCC Iron
add(32, "Crystal Structure Effects: Self-Diffusion Disparity Across Iron's Allotropic Phase Change",
    "Arrhenius Law & Energetics", "arrhenius_law", "Advanced",
    r"""<p>Pure iron undergoes an allotropic phase transformation at $912^\circ\text{C}$ ($1185 \text{ K}$), transforming from BCC $\alpha$-ferrite below $912^\circ\text{C}$ to FCC $\gamma$-austenite above $912^\circ\text{C}$.</p>
    <div style="text-align:center; margin: 10px 0;">
      Self-diffusion in BCC $\alpha$-Fe: $D_0 = 2.0 \times 10^{-4} \text{ m}^2/\text{s}, \quad Q_d = 251.0 \text{ kJ/mol}$<br>
      Self-diffusion in FCC $\gamma$-Fe: $D_0 = 6.5 \times 10^{-5} \text{ m}^2/\text{s}, \quad Q_d = 284.0 \text{ kJ/mol}$
    </div>
    <ol type="a">
      <li>Calculate the self-diffusion coefficient of iron in BCC $\alpha$-Fe at $912^\circ\text{C}$ (approaching from below).</li>
      <li>Calculate the self-diffusion coefficient of iron in FCC $\gamma$-Fe at $912^\circ\text{C}$ (approaching from above).</li>
      <li>Compute the ratio $D_{\alpha} / D_{\gamma}$ at the transformation temperature.</li>
      <li>Explain from crystallographic principles (atomic packing factor $\text{APF} = 0.68$ vs $0.74$, coordination number $8$ vs $12$, and saddle-point dilation) why diffusion is dramatically faster in the BCC phase.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Diffusivities at $912^\circ\text{C}$ ($1185 \text{ K}$)</div>
      <p>$R T = (8.314 \text{ J/(mol}\cdot\text{K)}) \times (1185 \text{ K}) = 9852.1 \text{ J/mol} = 9.8521 \text{ kJ/mol}$.</p>
      <ul>
        <li><strong>In BCC $\alpha$-Fe at $912^\circ\text{C}$:</strong>
        $$\frac{Q_d}{R T} = \frac{251.0}{9.8521} = 25.4768$$
        $$D_\alpha = (2.0 \times 10^{-4} \text{ m}^2/\text{s}) \times \exp(-25.4768) = (2.0 \times 10^{-4}) \times (8.621 \times 10^{-12}) = \mathbf{1.724 \times 10^{-15} \text{ m}^2/\text{s}}$$</li>
        <li><strong>In FCC $\gamma$-Fe at $912^\circ\text{C}$:</strong>
        $$\frac{Q_d}{R T} = \frac{284.0}{9.8521} = 28.8263$$
        $$D_\gamma = (6.5 \times 10^{-5} \text{ m}^2/\text{s}) \times \exp(-28.8263) = (6.5 \times 10^{-5}) \times (3.026 \times 10^{-13}) = \mathbf{1.967 \times 10^{-17} \text{ m}^2/\text{s}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Ratio Across the Phase Boundary</div>
      $$\frac{D_\alpha(\text{BCC})}{D_\gamma(\text{FCC})} = \frac{1.724 \times 10^{-15} \text{ m}^2/\text{s}}{1.967 \times 10^{-17} \text{ m}^2/\text{s}} = \mathbf{87.6 \approx 88}$$
      <p>Upon crossing the $912^\circ\text{C}$ transformation line from BCC into FCC, the self-diffusion coefficient drops discontinuously by a factor of <strong>nearly 90 times</strong>!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Crystallographic Explanation</div>
      <ol>
        <li><strong>Atomic Packing Factor:</strong> BCC is an open, non-close-packed crystal structure with $\text{APF} = 0.68$, leaving $32\%$ free volume. FCC is close-packed with $\text{APF} = 0.74$, leaving only $26\%$ free volume.</li>
        <li><strong>Coordination Number and Bond Strength:</strong> In BCC, an atom has only 8 nearest neighbors ($CN = 8$); in FCC, it has 12 nearest neighbors ($CN = 12$). Squeezing an atom between fewer neighbors requires severing or stretching fewer coordinating bonds.</li>
        <li><strong>Saddle-Point Bottleneck:</strong> During a vacancy jump, the migrating atom must push through a constriction formed by coordinating atoms (the saddle-point configuration). In the open BCC lattice, the window between atoms is wider, requiring substantially less elastic strain work ($\Delta H_m$ is lower). Consequently, both activation enthalpy for vacancy formation ($\Delta H_f$) and migration ($\Delta H_m$) are significantly lower in BCC, yielding $Q_{\text{BCC}} = 251 \text{ kJ/mol} < Q_{\text{FCC}} = 284 \text{ kJ/mol}$.</li>
      </ol>
    </div>
    <div class="final-answer-box">
      <strong>At $912^\circ\text{C}$:</strong> $D_\alpha(\text{BCC}) = \mathbf{1.72 \times 10^{-15} \text{ m}^2/\text{s}}$, $D_\gamma(\text{FCC}) = \mathbf{1.97 \times 10^{-17} \text{ m}^2/\text{s}}$.<br>
      <strong>Discontinuity Ratio:</strong> $D_\alpha / D_\gamma = \mathbf{88\times}$.<br>
      BCC diffuses much faster because of lower packing factor ($0.68$ vs $0.74$) and lower coordination ($8$ vs $12$), reducing the saddle-point dilation barrier.
    </div>""")

# P33: Carbon Diffusion Across Allotropic Transformation
add(33, "Interstitial Mobility Across Allotropic Transformation: Carbon in Ferrite vs. Austenite",
    "Arrhenius Law & Energetics", "arrhenius_law", "Intermediate",
    r"""<p>The open crystal structure of BCC iron also dramatically accelerates the interstitial diffusion of carbon compared to FCC austenite.</p>
    <div style="text-align:center; margin: 10px 0;">
      Carbon in BCC $\alpha$-Fe: $D_0 = 6.2 \times 10^{-7} \text{ m}^2/\text{s}, \quad Q_d = 80.0 \text{ kJ/mol}$<br>
      Carbon in FCC $\gamma$-Fe: $D_0 = 2.3 \times 10^{-5} \text{ m}^2/\text{s}, \quad Q_d = 148.0 \text{ kJ/mol}$
    </div>
    <ol type="a">
      <li>Calculate the diffusion coefficient of Carbon in BCC $\alpha$-Fe at $912^\circ\text{C}$ ($1185 \text{ K}$).</li>
      <li>Calculate the diffusion coefficient of Carbon in FCC $\gamma$-Fe at $912^\circ\text{C}$.</li>
      <li>Compute the ratio $D_{\text{C}}(\alpha) / D_{\text{C}}(\gamma)$ at $912^\circ\text{C}$.</li>
      <li>Calculate the ratio at $600^\circ\text{C}$ ($873 \text{ K}$, extrapolating austenite). Explain why the kinetic gap widens so colossally at lower temperatures.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a), (b), & (c): Carbon Diffusivities at $912^\circ\text{C}$ ($1185 \text{ K}$)</div>
      <p>$R T = (8.314) \times (1185) = 9852.1 \text{ J/mol} = 9.8521 \text{ kJ/mol}$.</p>
      <ul>
        <li><strong>In BCC Ferrite ($\alpha$-Fe):</strong>
        $$D_{\text{C}}(\alpha) = (6.2 \times 10^{-7}) \exp\left(-\frac{80.0}{9.8521}\right) = (6.2 \times 10^{-7}) \exp(-8.120) = \mathbf{1.841 \times 10^{-10} \text{ m}^2/\text{s}}$$</li>
        <li><strong>In FCC Austenite ($\gamma$-Fe):</strong>
        $$D_{\text{C}}(\gamma) = (2.3 \times 10^{-5}) \exp\left(-\frac{148.0}{9.8521}\right) = (2.3 \times 10^{-5}) \exp(-15.022) = \mathbf{7.014 \times 10^{-12} \text{ m}^2/\text{s}}$$</li>
      </ul>
      <p>Ratio at $912^\circ\text{C}$:</p>
      $$\frac{D_{\text{C}}(\alpha)}{D_{\text{C}}(\gamma)} = \frac{1.841 \times 10^{-10}}{7.014 \times 10^{-12}} = \mathbf{26.25 \approx 26}$$
      <p>Even though carbon solubility is 100 times smaller in ferrite, its diffusion rate in ferrite is <strong>26 times faster</strong>!</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Extrapolation at $600^\circ\text{C}$ ($873 \text{ K}$)</div>
      <p>$R T = (8.314) \times (873) = 7258.1 \text{ J/mol} = 7.2581 \text{ kJ/mol}$.</p>
      <ul>
        <li>$D_{\text{C}}(\alpha) = (6.2 \times 10^{-7}) \exp\left(-\frac{80.0}{7.2581}\right) = (6.2 \times 10^{-7}) \exp(-11.022) = \mathbf{1.027 \times 10^{-11} \text{ m}^2/\text{s}}$</li>
        <li>$D_{\text{C}}(\gamma) = (2.3 \times 10^{-5}) \exp\left(-\frac{148.0}{7.2581}\right) = (2.3 \times 10^{-5}) \exp(-20.391) = \mathbf{3.238 \times 10^{-14} \text{ m}^2/\text{s}}$</li>
      </ul>
      <p>Ratio at $600^\circ\text{C}$:</p>
      $$\frac{D_{\text{C}}(\alpha)}{D_{\text{C}}(\gamma)} = \frac{1.027 \times 10^{-11}}{3.238 \times 10^{-14}} = \mathbf{317.2 \approx 317}$$
      <p><strong>Physical Reason:</strong> Because the activation energy in austenite ($148 \text{ kJ/mol}$) is nearly double that in ferrite ($80 \text{ kJ/mol}$), lowering the temperature freezes carbon diffusion in austenite far more aggressively, widening the ratio from $26\times$ at $912^\circ\text{C}$ to over $317\times$ at $600^\circ\text{C}$. This ultra-fast carbon diffusion in ferrite governs the formation kinetics of pearlite and bainite.</p>
    </div>
    <div class="final-answer-box">
      <strong>At $912^\circ\text{C}$:</strong> $D_\alpha = \mathbf{1.84 \times 10^{-10} \text{ m}^2/\text{s}}$, $D_\gamma = \mathbf{7.01 \times 10^{-12} \text{ m}^2/\text{s}}$ &bull; Ratio $= \mathbf{26\times}$.<br>
      <strong>At $600^\circ\text{C}$:</strong> Ratio widens to $\mathbf{317\times}$ due to the steep activation energy difference ($148\text{ kJ/mol}$ vs $80\text{ kJ/mol}$).
    </div>""")

# P34: Short-Circuit Diffusion Hierarchy
add(34, "High-Diffusivity Paths: The Short-Circuit Diffusion Hierarchy",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Fundamental",
    r"""<p>Real crystalline materials contain structural defects that provide "short-circuit" pathways for accelerated atomic migration.</p>
    <ol type="a">
      <li>Rank the four primary diffusion pathways in order of increasing diffusion coefficient (fastest to slowest):
      $$D_{\text{surface}}, \quad D_{\text{grain boundary}}, \quad D_{\text{dislocation pipe}}, \quad D_{\text{lattice / volume}}$$</li>
      <li>Rank the corresponding activation energies for these four mechanisms:
      $$Q_{\text{surface}}, \quad Q_{\text{grain boundary}}, \quad Q_{\text{dislocation pipe}}, \quad Q_{\text{lattice}}$$
      Provide empirical approximations relating each short-circuit activation energy to the bulk lattice activation energy $Q_L$.</li>
      <li>Explain why, despite having the lowest diffusivity ($D_L \ll D_{\text{surf}}$), bulk lattice diffusion still accounts for the overwhelming majority of total mass transport at high homologous temperatures ($T > 0.7 T_m$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Diffusivity Hierarchy (Fastest to Slowest)</div>
      $$D_{\text{surface}} > D_{\text{grain boundary}} > D_{\text{dislocation pipe}} \gg D_{\text{lattice / volume}}$$
      <ul>
        <li><strong>External Surfaces:</strong> Atoms are bonded only to the layer below; open 2D space offers minimal geometric resistance.</li>
        <li><strong>Grain Boundaries:</strong> Disordered transition zone containing excess free volume, dilated channels, and reduced bond coordination.</li>
        <li><strong>Dislocation Cores:</strong> 1D pipe containing an extra half-plane termination with high core strain and dilated vacancy-like channels.</li>
        <li><strong>Bulk Lattice:</strong> Perfect close-packed crystal; atoms are constrained by full coordination numbers ($CN = 12$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Activation Energy Hierarchy (Lowest to Highest)</div>
      $$Q_{\text{surface}} < Q_{\text{grain boundary}} < Q_{\text{dislocation pipe}} < Q_{\text{lattice}}$$
      <p>Typical empirical metallurgical rules of thumb:</p>
      <ul>
        <li>$Q_{\text{surface}} \approx 0.25\text{ to }0.35 \times Q_L$</li>
        <li>$Q_{\text{grain boundary}} \approx 0.40\text{ to }0.60 \times Q_L \approx \mathbf{0.5 Q_L}$</li>
        <li>$Q_{\text{dislocation pipe}} \approx 0.60\text{ to }0.70 \times Q_L$</li>
        <li>$Q_{\text{lattice}} \equiv Q_L$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Why Lattice Diffusion Dominates at High Temperature</div>
      <p>The total mass transport is the product of diffusivity and the cross-sectional area fraction of each path:</p>
      $$J_{\text{total}} \propto A_L D_L + A_{\text{gb}} D_{\text{gb}} + A_{\text{pipe}} D_{\text{pipe}}$$
      <p>In a typical polycrystalline metal with grain size $d \approx 50 \mu\text{m}$ and grain boundary width $\delta \approx 0.5 \text{ nm}$:</p>
      $$\frac{A_{\text{gb}}}{A_L} \approx \frac{2\delta}{d} = \frac{2 \times 0.5 \times 10^{-9} \text{ m}}{50 \times 10^{-6} \text{ m}} = 2.0 \times 10^{-5}$$
      <p>Over <strong>$99.998\%$ of the cross-sectional area</strong> consists of bulk crystal lattice! At high temperatures ($T > 0.7 T_m$), thermal energy is sufficient to activate lattice jumps easily ($\exp(-Q_L/RT)$ increases dramatically). The vast geometric area of the bulk crystal completely overwhelms the higher intrinsic diffusivity of the tiny, nanometer-thin boundary network.</p>
    </div>
    <div class="final-answer-box">
      <strong>Diffusivities:</strong> $D_{\text{surf}} > D_{\text{gb}} > D_{\text{pipe}} \gg D_{\text{lattice}}$.<br>
      <strong>Activation Energies:</strong> $Q_{\text{surf}} (\sim 0.3 Q_L) < Q_{\text{gb}} (\sim 0.5 Q_L) < Q_{\text{pipe}} (\sim 0.65 Q_L) < Q_L$.<br>
      Lattice diffusion dominates at high $T$ because lattice cross-sectional area is $> 99.99\%$ of the specimen.
    </div>""")

# P35: Grain Boundary Diffusion Fisher Model
add(35, "Grain Boundary Diffusion: The Fisher Model and Accelerated Boundary Penetration",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>In 1951, J. C. Fisher developed the mathematical foundation for diffusion along an isolated grain boundary embedded in a crystalline matrix.</p>
    <ol type="a">
      <li>Describe the physical assumptions of the <strong>Fisher model</strong>:
        <ul>
          <li>Grain boundary slab width $\delta$ and high boundary diffusivity $D_{\text{gb}}$.</li>
          <li>Low bulk lattice diffusivity $D_L$.</li>
          <li>Lateral leakage of diffusing solute from the boundary into adjacent grains.</li>
        </ul>
      </li>
      <li>Sketch the resulting isoconcentration contours. Why do they form sharp characteristic "wedges" or "fingers" pointing along the grain boundary into the solid?</li>
      <li>In polycrystalline silver at $500^\circ\text{C}$ ($T \approx 0.63 T_m$), the self-diffusivity values are:
      $$D_L = 1.0 \times 10^{-17} \text{ m}^2/\text{s}, \quad D_{\text{gb}} = 1.0 \times 10^{-11} \text{ m}^2/\text{s}$$
      Assuming a boundary width $\delta = 0.50 \text{ nm}$, calculate the ratio $D_{\text{gb}} / D_L$ and discuss how this governs low-temperature intergranular oxidation and corrosion.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Fisher Model Physical Assumptions</div>
      <p>Fisher modeled a grain boundary as a semi-infinite uniform isotropic slab of narrow width $\delta \approx 0.5 \text{ nm}$ oriented perpendicular to the external surface ($y$-axis along the boundary, $x$-axis perpendicular to it). The boundary possesses an exceptionally high diffusion coefficient $D_{\text{gb}} \gg D_L$. Solute diffuses rapidly down the boundary "conduit" along $y$. As solute accumulates in the boundary, it simultaneously diffuses laterally out of the boundary slab into the adjacent low-diffusivity bulk grains along $x$ (lateral leakage).</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Isoconcentration Contours and Wedge Profiles</div>
      <p>Because atomic migration is orders of magnitude faster down the boundary conduit ($D_{\text{gb}} \gg D_L$), solute penetrates to depths along the boundary that are far beyond the reach of normal bulk lattice diffusion. At any given depth, solute leaks slowly into adjacent grain interiors, decaying rapidly with lateral distance $|x|$. The resulting curves of constant concentration $C(x,y) = \text{const}$ form deep, acute, V-shaped <strong>isoconcentration wedges</strong> or "penetration fingers" pointing deep into the material along each grain boundary.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculations for Silver at $500^\circ\text{C}$</div>
      $$\frac{D_{\text{gb}}}{D_L} = \frac{1.0 \times 10^{-11} \text{ m}^2/\text{s}}{1.0 \times 10^{-17} \text{ m}^2/\text{s}} = \mathbf{1,000,000 = 10^6}$$
      <p>At $500^\circ\text{C}$, atoms travel <strong>one million times faster</strong> along grain boundaries than through the grain interiors! In the bulk lattice, the diffusion distance in $t = 10 \text{ hours}$ ($36,000 \text{ s}$) is only $2\sqrt{D_L t} = 2\sqrt{3.6 \times 10^{-13}} \approx 1.2 \mu\text{m}$. Along the grain boundaries, the penetration distance is $2\sqrt{D_{\text{gb}} t} = 2\sqrt{3.6 \times 10^{-7}} \approx 1200 \mu\text{m} = \mathbf{1.2 \text{ mm}}$!</p>
      <p>This colossal kinetic disparity explains why oxygen, molten metals, and aggressive environmental agents rapidly penetrate deep along grain boundaries at moderate temperatures, causing catastrophic stress-corrosion cracking, liquid metal embrittlement (e.g., liquid gallium penetrating aluminum grain boundaries), and intergranular oxidation.</p>
    </div>
    <div class="final-answer-box">
      <strong>Fisher Model:</strong> Fast transport down nanometer slab ($\delta \approx 0.5\text{ nm}$) with lateral leakage into bulk.<br>
      <strong>Morphology:</strong> Sharp V-shaped isoconcentration wedges pointing down boundaries.<br>
      <strong>Silver Ratio at $500^\circ\text{C}$:</strong> $D_{\text{gb}} / D_L = \mathbf{10^6\times}$ (penetration is $1.2\text{ mm}$ along boundary vs $1.2\mu\text{m}$ in bulk).
    </div>""")

# P36: Dislocation Pipe Diffusion and Hart's Equation
add(36, "Dislocation Pipe Diffusion: Hart's Equation and Cold-Work Enhanced Diffusivity",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>In heavily deformed metals, the high density of dislocation lines provides interconnected linear conduits for accelerated diffusion.</p>
    <ol type="a">
      <li>State <strong>Hart's Equation</strong> for the effective apparent diffusion coefficient $D_{\text{eff}}$ in a crystal containing dislocation lines:
      $$D_{\text{eff}} = f D_{\text{pipe}} + (1 - f) D_L$$
      where $f$ is the fraction of atomic lattice sites located within dislocation cores.</li>
      <li>Assuming each dislocation core has a cross-sectional area $A_{\text{core}} \approx 7 \times 10^{-19} \text{ m}^2$ (core radius $r_0 \approx 0.5 \text{ nm}$), express the core site fraction $f$ as a function of dislocation density $\rho_d$ ($\text{m}^{-2}$).</li>
      <li>In cold-rolled aluminum ($\rho_d = 2.0 \times 10^{15} \text{ m}^{-2}$), calculate the core site fraction $f$.</li>
      <li>At $T = 200^\circ\text{C}$ ($473 \text{ K}$), the diffusivities are $D_L = 1.0 \times 10^{-20} \text{ m}^2/\text{s}$ and $D_{\text{pipe}} = 5.0 \times 10^{-14} \text{ m}^2/\text{s}$. Calculate $D_{\text{eff}}$ and compute the enhancement ratio $D_{\text{eff}} / D_L$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Hart's Equation and Core Site Fraction $f$</div>
      <p>Hart's equation models diffusion when atoms sample both lattice and dislocation conduits frequently (random mixing over time $t$ where $\sqrt{D_L t} \gg$ dislocation spacing):</p>
      $$D_{\text{eff}} = f D_{\text{pipe}} + (1 - f) D_L$$
      <p>Let $A_{\text{core}} = \pi r_0^2 \approx \pi (0.47 \times 10^{-9} \text{ m})^2 \approx 7.0 \times 10^{-19} \text{ m}^2$. In a unit cross-sectional area ($1 \text{ m}^2$), there are $\rho_d$ dislocation cores. The total area occupied by dislocation cores is:</p>
      $$f = \frac{A_{\text{cores}}}{A_{\text{total}}} = \rho_d \cdot A_{\text{core}} = \rho_d (\pi r_0^2)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Core Site Fraction in Cold-Rolled Aluminum ($\rho_d = 2.0 \times 10^{15} \text{ m}^{-2}$)</div>
      $$f = (2.0 \times 10^{15} \text{ m}^{-2}) \times (7.0 \times 10^{-19} \text{ m}^2) = \mathbf{1.40 \times 10^{-3} \approx 0.14\%}$$
      <p>Dislocation cores occupy about 0.14% of the crystal volume.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Effective Diffusivity Calculation at $200^\circ\text{C}$</div>
      <p>Given $D_L = 1.0 \times 10^{-20} \text{ m}^2/\text{s}$ and $D_{\text{pipe}} = 5.0 \times 10^{-14} \text{ m}^2/\text{s}$:</p>
      <ul>
        <li>Dislocation pipe contribution:
        $$f D_{\text{pipe}} = (1.40 \times 10^{-3}) \times (5.0 \times 10^{-14} \text{ m}^2/\text{s}) = \mathbf{7.00 \times 10^{-17} \text{ m}^2/\text{s}}$$</li>
        <li>Lattice contribution:
        $$(1 - f) D_L \approx 1 \times (1.0 \times 10^{-20} \text{ m}^2/\text{s}) = \mathbf{1.00 \times 10^{-20} \text{ m}^2/\text{s}}$$</li>
      </ul>
      <p>Total effective diffusivity:</p>
      $$D_{\text{eff}} = 7.00 \times 10^{-17} + 1.00 \times 10^{-20} \approx \mathbf{7.00 \times 10^{-17} \text{ m}^2/\text{s}}$$
      <p>Enhancement ratio:</p>
      $$\frac{D_{\text{eff}}}{D_L} = \frac{7.00 \times 10^{-17}}{1.00 \times 10^{-20}} = \mathbf{7,000 \times}$$
      <p>Severe cold deformation multiplies the effective atomic mobility by <strong>7,000 times</strong>, enabling rapid low-temperature strain-aging and solute segregation.</p>
    </div>
    <div class="final-answer-box">
      <strong>Hart's Equation:</strong> $$D_{\text{eff}} = f D_{\text{pipe}} + (1-f) D_L$$
      <strong>Core Fraction:</strong> $f = \mathbf{1.4 \times 10^{-3}}$ ($0.14\%$).<br>
      <strong>Effective Diffusivity:</strong> $D_{\text{eff}} = \mathbf{7.0 \times 10^{-17} \text{ m}^2/\text{s}}$ (enhanced by $\mathbf{7,000\times}$ over annealed lattice).
    </div>""")

# P37: Harrison's Diffusion Regimes
add(37, "Harrison's Kinetic Regimes: Regimes A, B, and C in Polycrystalline Diffusion",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>In 1961, L. G. Harrison classified diffusion in polycrystalline solids into three distinct kinetic regimes based on the relative magnitudes of bulk diffusion length $\sqrt{D_L t}$, grain size $d$, and boundary width $\delta$.</p>
    <ol type="a">
      <li>Describe the physical characteristics, conditions, and penetration profile of:
        <ul>
          <li><strong>Regime A</strong> ($\sqrt{D_L t} \gg d$)</li>
          <li><strong>Regime B</strong> ($\delta \ll \sqrt{D_L t} \ll d$)</li>
          <li><strong>Regime C</strong> ($\sqrt{D_L t} \ll \delta$)</li>
        </ul>
      </li>
      <li>For each regime, specify which diffusion coefficient is measured experimentally:
        <ul>
          <li>An effective weighted average $D_{\text{eff}}$.</li>
          <li>The product of boundary width and boundary diffusivity ($\delta D_{\text{gb}}$).</li>
          <li>The true isolated grain boundary diffusivity $D_{\text{gb}}$.</li>
        </ul>
      </li>
      <li>At what relative temperatures ($T/T_m$) does each Harrison regime typically operate?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a) & (b): Harrison's Three Kinetic Regimes</div>
      <ul>
        <li><strong>Regime A (High Temperature, Long Times: $\sqrt{D_L t} \gg d$):</strong>
          <ul>
            <li><em>Physics:</em> Atoms diffuse so far during time $t$ that their diffusion distance greatly exceeds the grain diameter $d$. Every atom samples multiple grain boundaries and grain interiors. The diffusion fields of adjacent boundaries overlap completely, yielding smooth planar isoconcentration contours.</li>
            <li><em>Measured Parameter:</em> Follows Fick's law with an effective homogenized diffusivity:
            $$D_{\text{eff}} = D_L + \left(\frac{2\delta}{d}\right) D_{\text{gb}}$$</li>
          </ul>
        </li>
        <li><strong>Regime B (Intermediate Temperature: $\delta \ll \sqrt{D_L t} \ll d$):</strong>
          <ul>
            <li><em>Physics:</em> Fast diffusion occurs down grain boundaries, accompanied by lateral leakage into the immediately adjacent grain interiors. Because $\sqrt{D_L t} \ll d$, the leakage fields from adjacent boundaries do not overlap. Profiles exhibit the classic Fisher V-shaped wedges.</li>
            <li><em>Measured Parameter:</em> Penetration plots of $\ln C$ versus depth $y^{6/5}$ yield the <strong>triple product $s \delta D_{\text{gb}}$</strong> (via the Le Claire / Whipple-Suzuoka equation). One cannot separate $D_{\text{gb}}$ from boundary width $\delta$ without independent assumptions.</li>
          </ul>
        </li>
        <li><strong>Regime C (Low Temperature, Short Times: $\sqrt{D_L t} \ll \delta$):</strong>
          <ul>
            <li><em>Physics:</em> Bulk lattice diffusion is completely frozen ($\sqrt{D_L t} \approx 0$). Zero lateral leakage occurs into grain interiors. Diffusion takes place <em>strictly and exclusively</em> within the two-dimensional grain boundary network, with grains acting as completely inert, impermeable blocks.</li>
            <li><em>Measured Parameter:</em> Standard Fickian Gaussian analysis yields the <strong>true, uncoupled grain boundary diffusivity $D_{\text{gb}}$ directly</strong>!</li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Operating Temperature Regimes</div>
      <ul>
        <li><strong>Regime A:</strong> High homologous temperatures ($T > 0.7\text{--}0.8 T_m$), where bulk lattice diffusion is rapid.</li>
        <li><strong>Regime B:</strong> Intermediate temperatures ($0.4 T_m < T < 0.7 T_m$), typical of industrial heat treatments and creep.</li>
        <li><strong>Regime C:</strong> Low cryogenic to ambient temperatures ($T < 0.3\text{--}0.4 T_m$), typical of thin films and room-temperature aging.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Regime A ($\sqrt{D_Lt} \gg d$):</strong> Complete overlap $\implies$ Measures $D_{\text{eff}}$ ($T > 0.7 T_m$).<br>
      <strong>Regime B ($\delta \ll \sqrt{D_Lt} \ll d$):</strong> Isolated boundary wedges $\implies$ Measures $\delta D_{\text{gb}}$ ($0.4\text{--}0.7 T_m$).<br>
      <strong>Regime C ($\sqrt{D_Lt} \ll \delta$):</strong> Frozen lattice $\implies$ Measures true $D_{\text{gb}}$ directly ($T < 0.4 T_m$).
    </div>""")

# P38: Nanocrystalline Diffusion Acceleration
add(38, "Nanocrystalline Metals: Massive Effective Diffusivity Acceleration from High Boundary Fraction",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>Nanocrystalline materials (grain size $d < 50 \text{ nm}$) contain an enormous volume fraction of grain boundaries and triple junctions.</p>
    <ol type="a">
      <li>Derive the formula for the volume fraction of grain boundaries $f_{\text{gb}}$ in an equiaxed polycrystalline metal with grain diameter $d$ and grain boundary thickness $\delta = 1.0 \text{ nm}$:
      $$f_{\text{gb}} \approx 1 - \left(\frac{d - \delta}{d}\right)^3 \approx \frac{3\delta}{d}$$</li>
      <li>Calculate $f_{\text{gb}}$ for:
        <ul>
          <li>A coarse-grained metal ($d = 50 \mu\text{m}$).</li>
          <li>A fine-grained metal ($d = 5 \mu\text{m}$).</li>
          <li>A nanocrystalline metal ($d = 10 \text{ nm}$).</li>
        </ul>
      </li>
      <li>At $T = 300^\circ\text{C}$ in copper ($D_L = 1.0 \times 10^{-23} \text{ m}^2/\text{s}, D_{\text{gb}} = 1.0 \times 10^{-14} \text{ m}^2/\text{s}$), calculate the effective diffusivity $D_{\text{eff}} \approx f_{\text{gb}} D_{\text{gb}} + (1 - f_{\text{gb}}) D_L$ for the coarse-grained metal vs. the nanocrystalline metal. Compute the acceleration factor.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Grain Boundary Volume Fraction $f_{\text{gb}}$</div>
      <p>Model grains as cubes or spheres of diameter $d$. The crystalline core has dimension $(d - \delta)$. The volume of the grain interior is $V_{\text{core}} = (d - \delta)^3$, and total grain volume is $V_{\text{total}} = d^3$:</p>
      $$f_{\text{gb}} = \frac{V_{\text{total}} - V_{\text{core}}}{V_{\text{total}}} = \frac{d^3 - (d - \delta)^3}{d^3} = 1 - \left(1 - \frac{\delta}{d}\right)^3$$
      <p>Using the binomial expansion for $\delta \ll d$:</p>
      $$\left(1 - \frac{\delta}{d}\right)^3 \approx 1 - \frac{3\delta}{d} \implies f_{\text{gb}} \approx \mathbf{\frac{3\delta}{d}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Grain Boundary Fractions ($\delta = 1.0 \text{ nm} = 1.0 \times 10^{-9} \text{ m}$)</div>
      <ul>
        <li><strong>Coarse-Grained ($d = 50 \mu\text{m} = 5.0 \times 10^{-5} \text{ m}$):</strong>
        $$f_{\text{gb}} = \frac{3 \times (1.0 \times 10^{-9} \text{ m})}{5.0 \times 10^{-5} \text{ m}} = 6.0 \times 10^{-5} = \mathbf{0.006\%}$$</li>
        <li><strong>Fine-Grained ($d = 5 \mu\text{m} = 5.0 \times 10^{-6} \text{ m}$):</strong>
        $$f_{\text{gb}} = \frac{3 \times 1.0 \times 10^{-9}}{5.0 \times 10^{-6}} = 6.0 \times 10^{-4} = \mathbf{0.06\%}$$</li>
        <li><strong>Nanocrystalline ($d = 10 \text{ nm} = 1.0 \times 10^{-8} \text{ m}$):</strong>
        $$f_{\text{gb}} = 1 - \left(\frac{10 - 1}{10}\right)^3 = 1 - (0.9)^3 = 1 - 0.729 = \mathbf{0.271 = 27.1\%}$$
        <p>In a $10 \text{ nm}$ nanocrystal, over <strong>one-quarter of all atoms</strong> reside inside grain boundaries and triple junctions!</p></li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Effective Diffusivity Comparison at $300^\circ\text{C}$</div>
      <p>Given $D_L = 1.0 \times 10^{-23} \text{ m}^2/\text{s}$ and $D_{\text{gb}} = 1.0 \times 10^{-14} \text{ m}^2/\text{s}$:</p>
      <ul>
        <li><strong>For Coarse-Grained Metal ($f_{\text{gb}} = 6.0 \times 10^{-5}$):</strong>
        $$D_{\text{eff}} = (6.0 \times 10^{-5}) \times (1.0 \times 10^{-14}) + (1) \times (1.0 \times 10^{-23}) = 6.0 \times 10^{-19} + 1.0 \times 10^{-23} = \mathbf{6.0 \times 10^{-19} \text{ m}^2/\text{s}}$$</li>
        <li><strong>For Nanocrystalline Metal ($f_{\text{gb}} = 0.271$):</strong>
        $$D_{\text{eff}} = (0.271) \times (1.0 \times 10^{-14}) + (0.729) \times (1.0 \times 10^{-23}) = \mathbf{2.71 \times 10^{-15} \text{ m}^2/\text{s}}$$</li>
      </ul>
      <p>Acceleration factor:</p>
      $$\frac{D_{\text{eff}}(\text{nano})}{D_{\text{eff}}(\text{coarse})} = \frac{2.71 \times 10^{-15}}{6.0 \times 10^{-19}} = \mathbf{4,517 \approx 4,500 \times}$$
      <p>Nanocrystalline copper diffuses <strong>4,500 times faster</strong> than conventional copper, enabling low-temperature sintering and fast diffusion bonding, but creating severe thermal instability (rapid grain coarsening at modest temperatures).</p>
    </div>
    <div class="final-answer-box">
      <strong>Boundary Fractions:</strong> Coarse ($50\mu\text{m}$): $\mathbf{0.006\%}$ &bull; Nano ($10\text{nm}$): $\mathbf{27.1\%}$.<br>
      <strong>Effective Diffusivity:</strong> Coarse: $\mathbf{6.0 \times 10^{-19} \text{ m}^2/\text{s}}$ &bull; Nano: $\mathbf{2.71 \times 10^{-15} \text{ m}^2/\text{s}}$.<br>
      Nanocrystalline grain boundary network accelerates effective diffusivity by $\mathbf{4,500\times}$.
    </div>""")

# P39: Diffusion in Ionic Ceramics Ambipolar
add(39, "Diffusion in Ionic Solids: Electroneutrality Constraint and Ambipolar Coupled Diffusivity",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>In ionic ceramics, cations and anions carry electrical charges, meaning that diffusion of either species in a concentration gradient generates an internal electrical field that couples their motions.</p>
    <ol type="a">
      <li>Explain the origin of the <strong>internal diffusion potential (Nernst field)</strong> when cations and anions diffuse at different rates.</li>
      <li>Derive the <strong>Ambipolar Diffusion Coefficient</strong> $D_{\text{amb}}$ for a stoichiometric binary ionic compound $A^{z+} X^{z-}$:
      $$D_{\text{amb}} = \frac{(z_+ + z_-) D_+ D_-}{z_+ D_+ + z_- D_-}$$</li>
      <li>For Magnesium Oxide ($\text{MgO}$, $z_+ = z_- = 2$) at $1400^\circ\text{C}$, the self-diffusion coefficients are:
      $$D_{\text{Mg}^{2+}} = 1.0 \times 10^{-14} \text{ m}^2/\text{s}, \quad D_{\text{O}^{2-}} = 1.0 \times 10^{-17} \text{ m}^2/\text{s}$$
      Calculate $D_{\text{amb}}$ and show that it is governed almost entirely by the slower-moving species.</li>
      <li>Which ion ($\text{Mg}^{2+}$ or $\text{O}^{2-}$) controls the macroscopic rate of sintering, solid-state grain growth, and high-temperature creep in $\text{MgO}$? Explain why.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Origin of the Internal Ambipolar Electric Field</div>
      <p>Cations are smaller than anions and generally possess much higher individual diffusion coefficients ($D_+ \gg D_-$). If cations diffused freely down a concentration gradient ahead of anions, positive charge would accumulate at the leading edge, leaving negative charge behind. To prevent macroscopic charge separation and uphold strict electroneutrality, an internal electrostatic potential gradient (electric field $E = -\nabla\phi$) is established. This field <strong>retards the faster-moving cations and accelerates the slower-moving anions</strong>, forcing both ions to migrate at a single, coupled mutual rate.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Derivation of Ambipolar Diffusivity $D_{\text{amb}}$</div>
      <p>The total flux of each ion under combined concentration gradient and electric field $E$ is given by the Nernst-Planck equation:</p>
      $$J_+ = -D_+ \frac{dC_+}{dx} + \frac{z_+ e D_+ C_+}{k_B T} E$$
      $$J_- = -D_- \frac{dC_-}{dx} - \frac{z_- e D_- C_-}{k_B T} E$$
      <p>To prevent electrical current flow ($I = e(z_+ J_+ - z_- J_-) = 0$), electroneutrality requires $z_+ J_+ = z_- J_-$. Solving for the electric field $E$ and substituting back gives the coupled ambipolar flux:</p>
      $$J = -D_{\text{amb}} \frac{dC}{dx} \quad \text{where} \quad D_{\text{amb}} = \frac{(z_+ + z_-) D_+ D_-}{z_+ D_+ + z_- D_-}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Calculation for $\text{MgO}$ ($z_+ = z_- = 2$)</div>
      <p>For symmetric valence $z_+ = z_- = 2$:</p>
      $$D_{\text{amb}} = \frac{(2 + 2) D_+ D_-}{2 D_+ + 2 D_-} = \frac{4 D_+ D_-}{2(D_+ + D_-)} = \frac{2 D_+ D_-}{D_+ + D_-}$$
      <p>Since $D_{\text{Mg}} = 10^{-14} \text{ m}^2/\text{s} \gg D_{\text{O}} = 10^{-17} \text{ m}^2/\text{s}$:</p>
      $$D_+ + D_- \approx D_+ \implies D_{\text{amb}} \approx \frac{2 D_+ D_-}{D_+} = 2 D_-$$
      $$D_{\text{amb}} = \frac{2 \times (1.0 \times 10^{-14}) \times (1.0 \times 10^{-17})}{1.0 \times 10^{-14} + 1.0 \times 10^{-17}} = \frac{2.0 \times 10^{-31}}{1.001 \times 10^{-14}} = \mathbf{1.998 \times 10^{-17} \text{ m}^2/\text{s} \approx 2 D_{\text{O}^{2-}}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Rate-Controlling Species in Sintering and Creep</div>
      <p>Macroscopic mass transport processes (sintering, creep, grain boundary sliding) require stoichiometric formula units ($\text{Mg}^{2+} + \text{O}^{2-}$) to move together to build or remove lattice planes. You cannot sinter $\text{MgO}$ by moving only magnesium; oxygen ions must move as well. Because the ambipolar diffusion coefficient is pinned to the slower species ($D_{\text{amb}} \approx 2 D_{\text{O}}$), the <strong>slower-diffusing oxygen ion ($\text{O}^{2-}$) is the strict rate-controlling bottleneck</strong> for all high-temperature deformation and sintering of $\text{MgO}$.</p>
    </div>
    <div class="final-answer-box">
      <strong>Ambipolar Equation:</strong> $$D_{\text{amb}} = \frac{(z_+ + z_-) D_+ D_-}{z_+ D_+ + z_- D_-} \implies D_{\text{amb}} \approx 2 D_{\text{slow}}$$
      <strong>Calculated Value for $\text{MgO}$:</strong> $D_{\text{amb}} = \mathbf{2.0 \times 10^{-17} \text{ m}^2/\text{s}}$.<br>
      The <strong>slower-diffusing oxygen anion</strong> dictates sintering and creep rates.
    </div>""")

# P40: Diffusion in Polymers (Gas Permeability)
add(40, "Diffusion in Polymers: Free Volume Theory, Gas Permeability, and PET Bottle Barriers",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>Diffusion in solid polymers proceeds through dynamically fluctuating interstitial free volume pockets between entangled macromolecular chains.</p>
    <ol type="a">
      <li>Define the <strong>Permeability Coefficient $P$</strong> of a gas through a polymer membrane in terms of the diffusion coefficient $D$ and the solubility coefficient $S$:
      $$P = D \cdot S$$
      State standard SI units for $P$, $D$, and $S$.</li>
      <li>Contrast gas diffusion in <strong>amorphous polymers</strong> versus <strong>semi-crystalline polymers</strong>. Why do crystalline lamellae act as impermeable barriers?</li>
      <li>A polyethylene terephthalate (PET) beverage bottle has a wall thickness of $L = 0.40 \text{ mm}$ and total surface area $A = 0.050 \text{ m}^2$. The permeability coefficient of carbon dioxide ($\text{CO}_2$) in PET at $25^\circ\text{C}$ is $P = 1.20 \times 10^{-17} \text{ m}^2/(\text{s}\cdot\text{Pa})$. The internal carbonation pressure is $P_1 = 3.5 \times 10^5 \text{ Pa}$ ($3.5 \text{ bar}$) and outside ambient pressure is $P_2 = 0 \text{ Pa}$. Calculate the loss rate of $\text{CO}_2$ in grams per month ($M_{\text{CO}_2} = 44.01 \text{ g/mol}$).</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Permeability, Diffusivity, and Solubility</div>
      $$P = D \cdot S$$
      <ul>
        <li>$P$: <strong>Permeability Coefficient</strong>. Measures total steady-state gas transmission per unit pressure gradient. SI units: $\mathbf{\frac{\text{m}^3\text{(STP)}\cdot\text{m}}{\text{m}^2\cdot\text{s}\cdot\text{Pa}} = \frac{\text{m}^2}{\text{s}\cdot\text{Pa}} \text{ or } \frac{\text{kg}\cdot\text{m}}{\text{m}^2\cdot\text{s}\cdot\text{Pa}}}$.</li>
        <li>$D$: <strong>Diffusivity</strong>. Kinetic mobility of gas molecules hopping between polymer free-volume cavities ($\mathbf{\text{m}^2/\text{s}}$).</li>
        <li>$S$: <strong>Solubility Coefficient</strong>. Thermodynamic partition coefficient relating dissolved gas concentration to external partial pressure via Henry's law: $C = S \cdot p$ ($\mathbf{\text{kg}/(\text{m}^3\cdot\text{Pa})}$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Amorphous vs. Semi-Crystalline Polymers</div>
      <ul>
        <li><strong>Amorphous Regions:</strong> Polymer chains are randomly coiled with loose, disordered packing and substantial fractional free volume ($V_f \sim 2.5\text{--}10\%$). Gas molecules easily squeeze through fluctuating free-volume gaps.</li>
        <li><strong>Crystalline Lamellae:</strong> Polymer chains are folded into tightly packed, ordered crystallites with negligible free volume. Gas molecules cannot penetrate crystalline lamellae ($D_{\text{cryst}} \approx 0$).</li>
        <li><strong>Tortuosity Effect:</strong> Crystalline lamellae act as impenetrable obstacles, forcing diffusing gas molecules to follow long, winding, convoluted paths around crystallites. Permeability drops steeply as crystallinity fraction $X_c$ increases:
        $$P = P_{\text{amorphous}} \left(\frac{1 - X_c}{\tau}\right)$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): $\text{CO}_2$ Loss Rate Calculation for PET Bottle</div>
      <p>Given $L = 0.40 \text{ mm} = 4.0 \times 10^{-4} \text{ m}, A = 0.050 \text{ m}^2, \Delta p = 3.5 \times 10^5 \text{ Pa}$, and $P = 1.20 \times 10^{-17} \text{ m}^2/(\text{s}\cdot\text{Pa})$:</p>
      <p>Volumetric flux of gas (at standard temperature and pressure STP, $V_{\text{mol}} = 0.022414 \text{ m}^3/\text{mol}$):</p>
      $$J_v = \frac{P \Delta p}{L} = \frac{(1.20 \times 10^{-17} \text{ m}^2/\text{s}\cdot\text{Pa}) \times (3.5 \times 10^5 \text{ Pa})}{4.0 \times 10^{-4} \text{ m}} = \frac{4.20 \times 10^{-12}}{4.0 \times 10^{-4}} = 1.050 \times 10^{-8} \text{ m}^3\text{(STP)}/(\text{m}^2\cdot\text{s})$$
      <p>Total volumetric gas flow rate through bottle area $A = 0.050 \text{ m}^2$:</p>
      $$\dot{V} = J_v \times A = (1.050 \times 10^{-8}) \times 0.050 = 5.250 \times 10^{-10} \text{ m}^3\text{(STP)/s}$$
      <p>Molar flow rate ($\dot{n} = \dot{V} / V_{\text{mol}}$):</p>
      $$\dot{n} = \frac{5.250 \times 10^{-10} \text{ m}^3/\text{s}}{0.022414 \text{ m}^3/\text{mol}} = 2.3423 \times 10^{-8} \text{ mol/s}$$
      <p>Mass loss rate in grams per second ($M_{\text{CO}_2} = 44.01 \text{ g/mol}$):</p>
      $$\dot{m} = \dot{n} \times 44.01 \text{ g/mol} = (2.3423 \times 10^{-8}) \times 44.01 = 1.0309 \times 10^{-6} \text{ g/s}$$
      <p>Loss in one month ($t = 30 \text{ days} = 30 \times 86,400 = 2,592,000 \text{ s}$):</p>
      $$m_{\text{month}} = (1.0309 \times 10^{-6} \text{ g/s}) \times (2,592,000 \text{ s}) = \mathbf{2.672 \text{ g/month}}$$
      <p>A typical 2-liter soda bottle contains about $8 \text{ g}$ of $\text{CO}_2$. Losing $\sim 2.7 \text{ g/month}$ explains why plastic soda bottles go flat after 2 to 3 months of shelf storage, whereas glass and aluminum cans maintain carbonation indefinitely.</p>
    </div>
    <div class="final-answer-box">
      <strong>Permeability Law:</strong> $P = D \cdot S \implies J = P \frac{\Delta p}{L}$.<br>
      <strong>Crystallinity:</strong> Crystalline lamellae force tortuous paths, reducing permeability.<br>
      <strong>$\text{CO}_2$ Loss:</strong> $\mathbf{2.67 \text{ grams/month}}$ (explains soda flatting in plastic bottles).
    </div>""")

# Save checkpoint for part 2 (31 to 40)
print("Ch 5 Part 2: P31-P40 written.")
# P41: Sintering Kinetics
add(41, "Powder Sintering Kinetics: Initial Neck Growth, Driving Force, and Volume vs. Surface Diffusion",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>Sintering is the solid-state bonding of compacted powder particles at elevated temperatures below their melting point ($T \approx 0.7\text{--}0.9 T_m$).</p>
    <ol type="a">
      <li>State the fundamental thermodynamic driving force for powder sintering.</li>
      <li>In Frenkel and Kuczynski's two-sphere sintering model, the initial neck radius $x$ between two spherical powder particles of radius $R$ grows with time following the power law:
      $$\left(\frac{x}{R}\right)^n = \frac{B \cdot t}{R^m}$$
      State the characteristic exponent $n$ when neck growth is governed by:
        <ul>
          <li><strong>Surface Diffusion</strong> ($n = 7$).</li>
          <li><strong>Grain Boundary Diffusion</strong> ($n = 6$).</li>
          <li><strong>Bulk Volume / Lattice Diffusion</strong> ($n = 5$).</li>
        </ul>
      </li>
      <li>Differentiate between <strong>densifying mechanisms</strong> (grain boundary and lattice diffusion) and <strong>non-densifying mechanisms</strong> (surface diffusion and vapor transport). Why do non-densifying mechanisms coarsen the neck without shrinking the pore volume?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Thermodynamic Driving Force for Sintering</div>
      <p>Fine powders possess an immense total surface area $A_{\text{powder}}$. The fundamental thermodynamic driving force for sintering is the <strong>reduction in total interfacial excess Gibbs free energy</strong> achieved by replacing high-energy solid-vapor external surfaces ($\gamma_{sv} \approx 1.0\text{--}2.0 \text{ J/m}^2$) with lower-energy grain boundaries ($\gamma_{\text{gb}} \approx 0.3\text{--}0.6 \text{ J/m}^2$) and ultimately eliminating pores entirely:</p>
      $$\Delta G_{\text{sintering}} = \Delta (\gamma A) = \gamma_{\text{gb}} A_{\text{gb}} - \gamma_{sv} A_{sv} < 0$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Sintering Neck Growth Exponents $(x/R)^n \propto t$</div>
      <p>The neck growth kinetics depend on the atomic pathway connecting the source of matter to the neck sink:</p>
      <ul>
        <li><strong>Volume / Lattice Diffusion from Boundary ($n = 5, m = 3$):</strong> Matter diffuses from the interparticle grain boundary through the bulk crystal to the neck surface ($x^5 \propto t$).</li>
        <li><strong>Grain Boundary Diffusion ($n = 6, m = 4$):</strong> Matter diffuses along the interparticle grain boundary core to the neck ($x^6 \propto t$).</li>
        <li><strong>Surface Diffusion ($n = 7, m = 4$):</strong> Atoms migrate from the convex particle surface along the exterior surface into the concave neck ($x^7 \propto t$).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Densifying vs. Non-Densifying Mechanisms</div>
      <ul>
        <li><strong>Densifying Mechanisms (Grain Boundary & Volume Diffusion from Boundary):</strong> The source of matter is the grain boundary between the two particle centers. Removing atoms from the interparticle contact zone allows the centers of the two particles to approach each other ($\Delta L / L_0 < 0$). This brings about macroscopic shrinkage, pore elimination, and bulk density increase.</li>
        <li><strong>Non-Densifying Mechanisms (Surface Diffusion & Evaporation-Condensation):</strong> The source of matter is the convex outer surface of the particles. Matter merely redistributes from the convex particle surface to the concave neck. The centers of the two spheres do not move closer together ($\Delta L = 0$); the compact gains mechanical neck strength, but the total volume of pores remains unchanged and bulk density does not increase.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Driving Force:</strong> Elimination of high-energy surface area ($\Delta G = \Delta(\gamma A) < 0$).<br>
      <strong>Growth Exponents:</strong> Surface: $n = \mathbf{7}$ &bull; Boundary: $n = \mathbf{6}$ &bull; Volume: $n = \mathbf{5}$.<br>
      <strong>Densification:</strong> Only grain boundary and bulk diffusion from the boundary draw particle centers together, producing shrinkage.
    </div>""")

# P42: Ingot Homogenization Fourier Decay
add(42, "Casting Homogenization: Fourier Decay of Microsegregation Concentration Gradients",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>During the solidification of cast alloy ingots, non-equilibrium dendritic segregation produces sinusoidal solute variations across the secondary dendrite arm spacing (SDAS, $\lambda$).</p>
    <ol type="a">
      <li>Model the initial segregated solute profile as a 1D spatial sine wave:
      $$C(x, 0) = \bar{C} + \Delta C_0 \sin\left(\frac{2\pi x}{\lambda}\right)$$
      Show that substituting this into Fick's second law yields the time-dependent damping solution:
      $$C(x, t) = \bar{C} + \Delta C_0 \exp\left(-\frac{t}{\tau_{\text{hom}}}\right) \sin\left(\frac{2\pi x}{\lambda}\right)$$
      and derive the expression for the <strong>characteristic homogenization relaxation time $\tau_{\text{hom}}$</strong>:
      $$\tau_{\text{hom}} = \frac{\lambda^2}{4\pi^2 D}$$</li>
      <li>A cast carbon-manganese steel ingot has a secondary dendrite arm spacing $\lambda = 50 \mu\text{m}$. Manganese interdiffusion in austenite at $1200^\circ\text{C}$ has diffusivity $D = 2.0 \times 10^{-14} \text{ m}^2/\text{s}$. Calculate $\tau_{\text{hom}}$ in hours.</li>
      <li>Calculate the soaking time $t$ required at $1200^\circ\text{C}$ to reduce the segregation amplitude by $95\%$ ($\Delta C(t) / \Delta C_0 = 0.05$).</li>
      <li>If a heavy ingot has a coarse dendrite spacing of $\lambda = 200 \mu\text{m}$ ($4\times$ coarser), calculate the new soaking time required.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Derivation of Homogenization Relaxation Time $\tau_{\text{hom}}$</div>
      <p>From Fick's second law: $\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}$.</p>
      <p>Assume a separation of variables solution: $C(x,t) - \bar{C} = X(x) \cdot T(t) = \Delta C_0 \sin\left(\frac{2\pi x}{\lambda}\right) e^{-t/\tau}$.</p>
      <p>Compute spatial derivative:</p>
      $$\frac{\partial^2 C}{\partial x^2} = -\left(\frac{2\pi}{\lambda}\right)^2 \Delta C_0 \sin\left(\frac{2\pi x}{\lambda}\right) e^{-t/\tau} = -\frac{4\pi^2}{\lambda^2} [C(x,t) - \bar{C}]$$
      <p>Compute time derivative:</p>
      $$\frac{\partial C}{\partial t} = -\frac{1}{\tau} [C(x,t) - \bar{C}]$$
      <p>Equating $\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}$:</p>
      $$-\frac{1}{\tau} [C - \bar{C}] = -D \frac{4\pi^2}{\lambda^2} [C - \bar{C}] \implies \frac{1}{\tau} = \frac{4\pi^2 D}{\lambda^2} \implies \tau_{\text{hom}} = \frac{\lambda^2}{4\pi^2 D}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Calculation of $\tau_{\text{hom}}$ ($\lambda = 50 \mu\text{m} = 5.0 \times 10^{-5} \text{ m}, D = 2.0 \times 10^{-14} \text{ m}^2/\text{s}$)</div>
      $$\lambda^2 = (5.0 \times 10^{-5} \text{ m})^2 = 2.50 \times 10^{-9} \text{ m}^2$$
      $$\tau_{\text{hom}} = \frac{2.50 \times 10^{-9} \text{ m}^2}{4\pi^2 \times (2.0 \times 10^{-14} \text{ m}^2/\text{s})} = \frac{2.50 \times 10^{-9}}{7.8957 \times 10^{-13}} = 3166.3 \text{ seconds}$$
      $$\tau_{\text{hom}} = \frac{3166.3 \text{ s}}{3600 \text{ s/hr}} = \mathbf{0.8795 \text{ hours} \approx 52.8 \text{ minutes}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Soaking Time for 95% Segregation Reduction</div>
      $$\frac{\Delta C(t)}{\Delta C_0} = \exp\left(-\frac{t}{\tau_{\text{hom}}}\right) = 0.05 \implies -\frac{t}{\tau_{\text{hom}}} = \ln(0.05) = -2.9957$$
      $$t = 2.9957 \times \tau_{\text{hom}} \approx 3.0 \times \tau_{\text{hom}}$$
      $$t = 2.9957 \times (0.8795 \text{ hr}) = \mathbf{2.635 \text{ hours} \approx 2 \text{ hours and 38 minutes}}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Effect of Coarse Dendrite Spacing ($\lambda = 200 \mu\text{m}$)</div>
      <p>Because homogenization time scales quadratically with dendrite arm spacing ($t \propto \lambda^2$):</p>
      $$\frac{t_2}{t_1} = \left(\frac{\lambda_2}{\lambda_1}\right)^2 = \left(\frac{200 \mu\text{m}}{50 \mu\text{m}}\right)^2 = 4^2 = \mathbf{16.0}$$
      $$t_2 = 16.0 \times 2.635 \text{ hr} = \mathbf{42.16 \text{ hours}}$$
      <p>A $4\times$ increase in dendrite spacing requires multiplying the soaking furnace time by <strong>16 times</strong> (nearly 2 full days of soaking at $1200^\circ\text{C}$), demonstrating why fine as-cast dendrite structures are essential in continuous casting.</p>
    </div>
    <div class="final-answer-box">
      <strong>Relaxation Time Formula:</strong> $$\tau_{\text{hom}} = \frac{\lambda^2}{4\pi^2 D} \implies \tau = \mathbf{0.88 \text{ hours}}$$
      <strong>Soaking Time ($95\%$ elimination):</strong> $t = 3\tau = \mathbf{2.64 \text{ hours}}$.<br>
      For $\lambda = 200\mu\text{m}$, time increases by $16\times$ to $\mathbf{42.2 \text{ hours}}$ ($t \propto \lambda^2$).
    </div>""")

# P43: Internal Oxidation Wagner Theory
add(43, "Internal Oxidation of Dilute Alloys: Wagner's Sub-Surface Oxidation Depth",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>When a dilute solid solution of a reactive solute $B$ in a noble solvent $A$ (e.g., dilute Ag-In or Cu-Al) is exposed to oxygen at high temperature, oxygen dissolves and diffuses inward to precipitate sub-surface oxide particles $BO_v$.</p>
    <ol type="a">
      <li>State the physical conditions required for <strong>internal oxidation</strong> to occur rather than continuous external scale formation.</li>
      <li>State <strong>Wagner's parabolic equation</strong> for the internal oxidation penetration depth $X(t)$:
      $$X(t) = \sqrt{\frac{2 N_O^{(s)} D_O}{v N_B^{(0)}} \cdot t}$$
      where $N_O^{(s)}$ is oxygen surface solubility, $D_O$ is oxygen diffusivity, $N_B^{(0)}$ is initial solute mole fraction, and $v$ is stoichiometric oxygen ratio ($BO_v$).</li>
      <li>In a $\text{Cu}-0.5 \text{ at}\%\text{ Al}$ alloy oxidized at $800^\circ\text{C}$ ($v = 1.5$ for $\text{Al}_2\text{O}_3$), $N_O^{(s)} D_O = 1.20 \times 10^{-14} \text{ m}^2/\text{s}$ and $N_{\text{Al}}^{(0)} = 0.0050$. Calculate the internal oxidation front depth $X$ after $t = 4.0 \text{ hours}$ in micrometers.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Conditions for Internal Oxidation</div>
      <ol>
        <li>The dissolved oxygen permeability in solvent $A$ must exceed the solute diffusion product: $N_O^{(s)} D_O \gg N_B^{(0)} D_B$ (oxygen diffuses inward much faster than solute $B$ can diffuse outward).</li>
        <li>The oxide $BO_v$ must have high thermodynamic stability (very negative free energy of formation $\Delta G_f^\circ$).</li>
        <li>The solute concentration $N_B^{(0)}$ must be dilute (below the critical transition concentration $N_B^* \sim 15\text{--}25 \text{ at}\%$) so that discrete isolated precipitates form rather than a continuous protective external passivation scale.</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b) & (c): Calculation for Cu-0.5 at% Al ($t = 4.0 \text{ hr} = 14,400 \text{ s}$)</div>
      <p>Given $N_O^{(s)} D_O = 1.20 \times 10^{-14} \text{ m}^2/\text{s}, v = 1.5$ (for $\text{AlO}_{1.5} \equiv \text{Al}_2\text{O}_3$), $N_{\text{Al}}^{(0)} = 0.0050$:</p>
      $$v N_{\text{Al}}^{(0)} = 1.5 \times 0.0050 = 0.0075$$
      $$\frac{2 N_O^{(s)} D_O}{v N_{\text{Al}}^{(0)}} = \frac{2 \times (1.20 \times 10^{-14} \text{ m}^2/\text{s})}{0.0075} = \frac{2.40 \times 10^{-14}}{0.0075} = 3.20 \times 10^{-12} \text{ m}^2/\text{s}$$
      <p>Compute oxidation front depth $X(t)$:</p>
      $$X^2 = (3.20 \times 10^{-12} \text{ m}^2/\text{s}) \times (14,400 \text{ s}) = 4.608 \times 10^{-8} \text{ m}^2$$
      $$X = \sqrt{4.608 \times 10^{-8} \text{ m}^2} = 2.1466 \times 10^{-4} \text{ m} = \mathbf{0.2147 \text{ mm} = 214.7 \mu\text{m}}$$
    </div>
    <div class="final-answer-box">
      <strong>Wagner's Law:</strong> $$X(t) = \sqrt{\frac{2 N_O^{(s)} D_O}{v N_B^{(0)}} \cdot t}$$
      <strong>Sub-Surface Oxide Depth:</strong> $X = \mathbf{214.7 \mu\text{m}}$ after 4 hours.
    </div>""")

# P44: Hydrogen Embrittlement and Degassing Bake-Out
add(44, "Hydrogen Diffusion and Trapping: Degassing Bake-Out in High-Strength Steels",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>Hydrogen embrittlement is a catastrophic failure mode in ultra-high-strength fasteners and landing gears caused by interstitial hydrogen absorbed during electroplating or pickling.</p>
    <ol type="a">
      <li>Explain why hydrogen diffuses extraordinarily fast in BCC ferrite ($D_{\text{H}} \approx 10^{-8} \text{ m}^2/\text{s}$ at $25^\circ\text{C}$), but becomes immobilized by <strong>hydrogen trap sites</strong> (dislocation cores, inclusions, grain boundaries).</li>
      <li>Why does baking at $190\text{--}200^\circ\text{C}$ for $24 \text{ hours}$ (ASTM F1940 hydrogen embrittlement relief) successfully de-trap and expel hydrogen from the steel?</li>
      <li>A high-strength steel bolt of diameter $2 R = 12.0 \text{ mm}$ ($R = 6.0 \text{ mm}$) has an effective hydrogen diffusivity at $200^\circ\text{C}$ of $D_{\text{eff}} = 2.5 \times 10^{-10} \text{ m}^2/\text{s}$. Using the cylindrical diffusion estimate $t_{\text{degas}} \approx \frac{R^2}{4 D_{\text{eff}}}$, calculate the minimum baking time in hours.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Fast Diffusion and Trapping Mechanism</div>
      <p>Hydrogen is the smallest atom ($r_{\text{H}} \approx 0.037 \text{ nm}$), residing in the open tetrahedral interstitial sites of BCC ferrite with an ultra-low migration barrier ($Q_m \approx 7\text{ kJ/mol}$). However, microstructural defects (non-metallic inclusions, coherent carbide interfaces, grain boundaries, and the tensile hydrostatic stress fields of dislocation cores) act as deep potential energy wells (traps) with binding energies $E_b \approx 20\text{--}80 \text{ kJ/mol}$. Trapped hydrogen atoms cannot jump until thermally activated out of the trap, reducing apparent room-temperature diffusivity by several orders of magnitude.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Principle of the $200^\circ\text{C}$ De-Embrittlement Bake</div>
      <p>At $190\text{--}200^\circ\text{C}$ ($463\text{--}473 \text{ K}$), thermal energy $k_B T$ is sufficient to overcome the trap binding energy ($E_b$), de-trapping hydrogen atoms back into mobile interstitial solid solution. Once de-trapped, hydrogen diffuses rapidly through the matrix to the external surface and desorbs into the atmosphere as harmless $\text{H}_2$ gas before it can segregate to stress concentration points to nucleate microcracks.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Degassing Baking Time Calculation ($R = 6.0 \text{ mm} = 6.0 \times 10^{-3} \text{ m}$)</div>
      $$R^2 = (6.0 \times 10^{-3} \text{ m})^2 = 3.60 \times 10^{-5} \text{ m}^2$$
      $$t_{\text{degas}} \approx \frac{R^2}{4 D_{\text{eff}}} = \frac{3.60 \times 10^{-5} \text{ m}^2}{4 \times (2.50 \times 10^{-10} \text{ m}^2/\text{s})} = \frac{3.60 \times 10^{-5}}{1.00 \times 10^{-9}} = 36,000 \text{ seconds}$$
      <p>Convert to hours:</p>
      $$t_{\text{degas}} = \frac{36,000 \text{ s}}{3600 \text{ s/hr}} = \mathbf{10.0 \text{ hours}}$$
      <p>Standard aerospace specifications mandate baking for 18 to 24 hours, providing a generous safety factor to ensure complete hydrogen exhaustion.</p>
    </div>
    <div class="final-answer-box">
      <strong>Hydrogen Trapping:</strong> Ultra-fast diffusion is arrested by deep defect traps ($E_b \approx 20\text{--}80\text{ kJ/mol}$).<br>
      <strong>Baking Principle:</strong> $200^\circ\text{C}$ provides thermal energy to de-trap hydrogen and vent it externally.<br>
      <strong>Calculated Bake Time:</strong> $t \approx \mathbf{10.0 \text{ hours}}$ (conforms to standard 24-hr industrial bake).
    </div>""")

# P45: Diffusion Barriers in Microelectronics
add(45, "Diffusion Barriers in Microelectronics: Preventing Copper Poisoning in Silicon Chips",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>In modern computer microprocessors, copper interconnect wires are separated from the underlying silicon dielectric by an ultra-thin diffusion barrier (such as Tantalum Nitride, $\text{TaN}$, or Titanium Nitride, $\text{TiN}$).</p>
    <ol type="a">
      <li>Why is a diffusion barrier strictly mandatory between copper metallization and silicon? Explain the catastrophic consequences of copper diffusion into silicon (copper silicide formation and deep-level traps).</li>
      <li>State the essential properties of an ideal microelectronic diffusion barrier.</li>
      <li>At $400^\circ\text{C}$, the diffusion coefficient of Copper in pure Silicon is $D_{\text{Cu-Si}} \approx 1.0 \times 10^{-9} \text{ cm}^2/\text{s}$, whereas in amorphous $\text{TaN}$ it is $D_{\text{Cu-TaN}} \approx 1.0 \times 10^{-18} \text{ cm}^2/\text{s}$. Calculate the time required for copper to diffuse through a $3.0 \text{ nm}$ barrier of $\text{TaN}$ versus a $3.0 \text{ nm}$ layer of bare Silicon using $t \approx x^2 / 2D$.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Necessity of Diffusion Barrier (Copper Poisoning)</div>
      <p>Copper is an ultra-fast interstitial diffuser in silicon. If copper directly contacts silicon during processing or operation ($100\text{--}400^\circ\text{C}$):</p>
      <ol>
        <li>Copper reacts aggressively with silicon at low temperatures ($200^\circ\text{C}$) to form resistive Copper Silicide ($\text{Cu}_3\text{Si}$), causing colossal volumetric expansion that shatters dielectric layers.</li>
        <li>Dissolved copper atoms introduce deep-level electronic trap states right in the center of the silicon energy bandgap ($E_v + 0.52 \text{ eV}$). These states act as lethal generation-recombination centers, annihilating transistor minority carrier lifetimes and producing catastrophic leakage currents that destroy the microprocessor.</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Ideal Properties of a Diffusion Barrier</div>
      <ul>
        <li>Ultra-low copper diffusivity ($D < 10^{-18} \text{ cm}^2/\text{s}$).</li>
        <li>Thermodynamically inert and immiscible with both Cu and Si (no intermetallic formation).</li>
        <li>Amorphous or nanocrystalline microstructure (absence of high-diffusivity grain boundaries).</li>
        <li>Low electrical resistivity and excellent adhesion.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Diffusion Time Calculation ($x = 3.0 \text{ nm} = 3.0 \times 10^{-7} \text{ cm}$)</div>
      $$x^2 = (3.0 \times 10^{-7} \text{ cm})^2 = 9.0 \times 10^{-14} \text{ cm}^2$$
      <ul>
        <li><strong>In Bare Silicon ($D = 1.0 \times 10^{-9} \text{ cm}^2/\text{s}$):</strong>
        $$t_{\text{Si}} \approx \frac{x^2}{2 D} = \frac{9.0 \times 10^{-14} \text{ cm}^2}{2 \times (1.0 \times 10^{-9} \text{ cm}^2/\text{s})} = \mathbf{4.5 \times 10^{-5} \text{ seconds} = 45 \mu\text{s}}$$
        Without a barrier, copper penetrates the entire layer in 45 microseconds!</li>
        <li><strong>In Amorphous $\text{TaN}$ Barrier ($D = 1.0 \times 10^{-18} \text{ cm}^2/\text{s}$):</strong>
        $$t_{\text{TaN}} \approx \frac{9.0 \times 10^{-14} \text{ cm}^2}{2 \times (1.0 \times 10^{-18} \text{ cm}^2/\text{s})} = 45,000 \text{ seconds} = \mathbf{12.5 \text{ hours}}$$
        At normal chip operating temperatures ($75^\circ\text{C}$), $D_{\text{TaN}}$ plunges to $< 10^{-25} \text{ cm}^2/\text{s}$, extending barrier breakthrough lifetime to <strong>over 100 years</strong>.</li>
      </ul>
    </div>
    <div class="final-answer-box">
      <strong>Copper Poisoning:</strong> Forms $\text{Cu}_3\text{Si}$ and mid-gap recombination traps that destroy transistors.<br>
      <strong>Penetration of $3\text{ nm}$ at $400^\circ\text{C}$:</strong> Bare Silicon: $\mathbf{45 \mu\text{s}}$ &bull; $\text{TaN}$ Barrier: $\mathbf{12.5 \text{ hours}}$ ($> 100$ years at operating temp).
    </div>""")

# P46: Intermetallic Growth Kinetics
add(46, "Solid-State Intermetallic Growth: Parabolic Layer Growth in Solder Joints",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>In electronic circuit boards, lead-free solder (e.g., Sn-Ag-Cu) reacts with copper pads to form intermetallic compound (IMC) layers ($\text{Cu}_6\text{Sn}_5$ and $\text{Cu}_3\text{Sn}$).</p>
    <ol type="a">
      <li>State the <strong>parabolic growth law</strong> governing diffusion-controlled planar intermetallic layer thickness $x(t)$:
      $$x(t) = \sqrt{k \cdot t} \quad \text{or} \quad x^2 = k \cdot t$$
      where $k$ is the parabolic growth rate constant.</li>
      <li>At $150^\circ\text{C}$ (accelerated thermal aging), the growth constant for total IMC thickness is $k = 4.0 \times 10^{-16} \text{ m}^2/\text{s}$. Calculate the IMC layer thickness after:
        <ul>
          <li>$t_1 = 100 \text{ hours}$</li>
          <li>$t_2 = 1,000 \text{ hours}$</li>
        </ul>
      </li>
      <li>Why does excessive IMC layer thickness ($x > 5\text{--}8 \mu\text{m}$) cause brittle failure of solder joints under drop-impact mechanical shock?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Parabolic Growth Law Derivation</div>
      <p>For an intermetallic layer to grow, copper and tin atoms must diffuse across the existing intermetallic layer of thickness $x$. By Fick's first law, the flux of reactants arriving at the growth interface is inversely proportional to layer thickness: $J \propto 1/x$. Since the growth velocity is proportional to flux:</p>
      $$\frac{dx}{dt} \propto J \implies \frac{dx}{dt} = \frac{k}{2x} \implies 2x dx = k dt \implies x^2 = k t \implies x(t) = \sqrt{k t}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): IMC Thickness Calculations at $150^\circ\text{C}$ ($k = 4.0 \times 10^{-16} \text{ m}^2/\text{s}$)</div>
      <ul>
        <li><strong>After $t_1 = 100 \text{ hours} = 360,000 \text{ s}$:</strong>
        $$x_1 = \sqrt{(4.0 \times 10^{-16} \text{ m}^2/\text{s}) \times (360,000 \text{ s})} = \sqrt{1.440 \times 10^{-10} \text{ m}^2} = 1.20 \times 10^{-5} \text{ m} = \mathbf{12.0 \mu\text{m}}$$</li>
        <li><strong>After $t_2 = 1,000 \text{ hours} = 3,600,000 \text{ s}$:</strong>
        $$x_2 = \sqrt{(4.0 \times 10^{-16} \text{ m}^2/\text{s}) \times (3,600,000 \text{ s})} = \sqrt{1.440 \times 10^{-9} \text{ m}^2} = 3.795 \times 10^{-5} \text{ m} = \mathbf{37.95 \mu\text{m}}$$</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Drop-Shock Mechanical Failure</div>
      <p>Intermetallic compounds ($\text{Cu}_6\text{Sn}_5, \text{Cu}_3\text{Sn}$) are brittle intermetallic phases with covalent-ionic bonding characteristics, high hardness, and very low fracture toughness ($K_{Ic} \approx 1\text{--}2 \text{ MPa}\sqrt{\text{m}}$). Furthermore, Kirkendall microvoids coalesce at the $\text{Cu}_3\text{Sn}/\text{Cu}$ interface due to unequal diffusion rates. When the layer thickens beyond $\sim 5 \mu\text{m}$, thermal mismatch stresses and Kirkendall void planes cause catastrophic brittle cleavage failure along the IMC interface during mobile phone drop-impact tests.</p>
    </div>
    <div class="final-answer-box">
      <strong>Parabolic Law:</strong> $$x = \sqrt{k t}$$
      <strong>IMC Thicknesses:</strong> $100\text{ hr} \implies x = \mathbf{12.0 \mu\text{m}}$ &bull; $1,000\text{ hr} \implies x = \mathbf{38.0 \mu\text{m}}$.<br>
      Excessive thickness causes drop-shock brittle fracture due to low IMC fracture toughness and interfacial Kirkendall voids.
    </div>""")

# P47: Transient Liquid Phase (TLP) Bonding
add(47, "Transient Liquid Phase (TLP) Bonding: Diffusion-Controlled Isothermal Solidification",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>Transient Liquid Phase (TLP) bonding is an advanced joining technique utilized to repair single-crystal nickel superalloy turbine blades without melting the parent metal.</p>
    <ol type="a">
      <li>Describe the four sequential stages of the <strong>TLP bonding process</strong>:
        <ul>
          <li>Insert alloy melting.</li>
          <li>Substrate base metal dissolution.</li>
          <li><strong>Isothermal Solidification</strong>.</li>
          <li>Solid-state homogenization.</li>
        </ul>
      </li>
      <li>Explain the function of the <strong>melting point depressant (MPD)</strong> element (typically Boron, $\sim 2\text{--}3 \text{ wt}\%$) in the interlayer foil.</li>
      <li>Why does the liquid joint solidify <strong>isothermally at constant temperature</strong> without any external cooling?</li>
      <li>Derive the expression for the total isothermal solidification time $t_{\text{iso}}$ as a function of half-joint width $w$ and MPD diffusion coefficient $D$:
      $$t_{\text{iso}} \propto \frac{w^2}{D}$$</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): The Four Stages of TLP Bonding</div>
      <ol>
        <li><strong>Melting of Interlayer:</strong> The assembly is heated to a bonding temperature $T_B$ above the melting point of the thin interlayer foil ($25\text{--}50 \mu\text{m}$ thick) but well below the melting point of the parent base superalloy. The interlayer melts and wets the joint interface.</li>
        <li><strong>Base Metal Dissolution:</strong> The liquid dissolves a thin layer of the solid substrate until thermodynamic solid-liquid phase equilibrium is established at the interface.</li>
        <li><strong>Isothermal Solidification:</strong> The melting point depressant (boron) diffuses out of the liquid joint into the vast solid base metal. As the liquid loses boron, its liquidus temperature rises above $T_B$, causing the solid-liquid interface to advance inward and solidify the entire joint at constant temperature.</li>
        <li><strong>Solid-State Homogenization:</strong> A post-bond heat treatment diffuses residual boron deeply into the matrix, eliminating brittle borides and matching parent single-crystal properties.</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Role of Melting Point Depressant (Boron)</div>
      <p>Nickel melts at $1455^\circ\text{C}$. Adding small interstitial boron atoms ($2\text{--}3\text{ wt}\%$) forms a low-melting eutectic at $1040^\circ\text{C}$. This allows the joint to liquefy at $T_B \approx 1150^\circ\text{C}$ without damaging the surrounding parent superalloy ($T_m \approx 1350^\circ\text{C}$). Furthermore, because boron is an interstitial atom, it diffuses rapidly out of the liquid into the solid base metal.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Mechanism of Isothermal Solidification</div>
      <p>Solidification normally requires cooling ($\Delta T < 0$). In TLP bonding, solidification is driven <strong>chemically by compositional change rather than temperature change</strong>. As boron diffuses away into the solid, the liquid becomes boron-depleted pure nickel-base alloy. Looking at the phase diagram, shifting composition to lower solute increases the melting point above the furnace temperature $T_B$. The joint solidifies completely under strictly isothermal conditions.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Solidification Time Scaling ($t_{\text{iso}} \propto w^2/D$)</div>
      <p>The rate-controlling step is the solid-state diffusion of boron into the base metal. Following Fick's second law for a moving boundary, the distance the solid-liquid interface moves scales with $\sqrt{Dt}$:</p>
      $$w = 2 \gamma \sqrt{D t_{\text{iso}}} \implies t_{\text{iso}} = \frac{w^2}{4 \gamma^2 D} \propto \frac{w^2}{D}$$
      <p>where $w$ is the maximum half-width of the liquid zone and $\gamma$ is a dimensionless growth parameter determined by phase diagram partition coefficients. Halving the joint gap reduces the required furnace time by a factor of 4.</p>
    </div>
    <div class="final-answer-box">
      <strong>TLP Stages:</strong> Foil melting $\to$ Base dissolution $\to$ <strong>Isothermal Solidification</strong> $\to$ Homogenization.<br>
      <strong>Isothermal Mechanism:</strong> Out-diffusion of Boron raises the local melting point, causing solidification at constant $T$.<br>
      <strong>Time Scaling:</strong> $$t_{\text{iso}} \propto \frac{w^2}{D}$$
    </div>""")

# P48: Electromigration in Microelectronics
add(48, "Electromigration in Microelectronic Interconnects: Electron Wind Force and Black's Law",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>Electromigration is directional atomic diffusion in metallic conductors driven by the intense momentum transfer from conducting electrons under high current densities.</p>
    <ol type="a">
      <li>Explain the two competing electrostatic forces acting on a metal ion during current flow:
        <ul>
          <li>The direct electrostatic field force ($\mathbf{F}_{\text{direct}}$).</li>
          <li>The <strong>electron wind force</strong> ($\mathbf{F}_{\text{wind}}$).</li>
        </ul>
        Which force dominates in good metals like copper and aluminum?</li>
      <li>State the <strong>electromigration atomic flux equation</strong>:
      $$J_{\text{EM}} = \frac{C D}{k_B T} Z^* e \rho_e j$$
      defining $Z^*$ (effective valence), $\rho_e$ (electrical resistivity), and $j$ (current density).</li>
      <li>State <strong>Black's Empirical Equation</strong> for the Mean Time to Failure ($\text{MTTF}$) of microelectronic interconnects:
      $$\text{MTTF} = \frac{A}{j^n} \exp\left(\frac{E_a}{k_B T}\right)$$</li>
      <li>A copper interconnect line carrying current density $j_1 = 1.0 \times 10^6 \text{ A/cm}^2$ at $T_1 = 105^\circ\text{C}$ ($378 \text{ K}$) has an estimated failure life of $\text{MTTF}_1 = 10 \text{ years}$ ($E_a = 0.90 \text{ eV}, n = 2$). If overclocking increases current density to $j_2 = 1.5 \times 10^6 \text{ A/cm}^2$ and chip temperature to $T_2 = 125^\circ\text{C}$ ($398 \text{ K}$), calculate the new lifetime $\text{MTTF}_2$ in years.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Direct Force vs. Electron Wind Force</div>
      <ul>
        <li><strong>Direct Electrostatic Force ($\mathbf{F}_{\text{direct}} = Z e \mathbf{E}$):</strong> The electrostatic attraction pulling the positively charged metal ion toward the negative cathode.</li>
        <li><strong>Electron Wind Force ($\mathbf{F}_{\text{wind}} = -e n_e \sigma_{\text{tr}} \lambda_e \mathbf{E}$):</strong> High-velocity conduction electrons colliding with activated metal ions at the saddle-point of their diffusion jump impart ballistic momentum, pushing the metal ions toward the <strong>positive anode</strong>.</li>
        <li>In metals with high electron conductivities, the <strong>electron wind force is $10\text{--}100$ times stronger than the direct electrostatic force</strong>! Metal atoms migrate in the direction of electron flow (from cathode to anode), leaving voids at the cathode and building hillocks/whiskers at the anode.</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b) & (c): Flux and Black's Equation</div>
      <p>The net effective charge is defined as $Z^* = Z_{\text{direct}} + Z_{\text{wind}}$ (typically negative, $Z^* \approx -1\text{ to }-10$):</p>
      $$J_{\text{EM}} = \frac{C D}{k_B T} Z^* e E = \frac{C D}{k_B T} Z^* e (\rho_e j)$$
      <p>In 1969, J. R. Black formulated the standard reliability lifetime equation:</p>
      $$\text{MTTF} = \frac{A}{j^n} \exp\left(\frac{E_a}{k_B T}\right) \quad (n \approx 1.5\text{--}2.0)$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Overclocking Lifetime Calculation</div>
      <p>Given $\text{MTTF}_1 = 10 \text{ years}$, $j_1 = 1.0 \times 10^6 \text{ A/cm}^2, T_1 = 378 \text{ K}$, $j_2 = 1.5 \times 10^6 \text{ A/cm}^2, T_2 = 398 \text{ K}$, $E_a = 0.90 \text{ eV}$, $n = 2$:</p>
      $$\frac{\text{MTTF}_2}{\text{MTTF}_1} = \left(\frac{j_1}{j_2}\right)^n \exp\left[\frac{E_a}{k_B}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)\right]$$
      <ul>
        <li>Current density factor:
        $$\left(\frac{j_1}{j_2}\right)^2 = \left(\frac{1.0}{1.5}\right)^2 = \left(\frac{2}{3}\right)^2 = \mathbf{0.4444}$$</li>
        <li>Thermal factor:
        $$\frac{1}{T_2} - \frac{1}{T_1} = \frac{1}{398} - \frac{1}{378} = 2.5126 \times 10^{-3} - 2.6455 \times 10^{-3} = -1.329 \times 10^{-4} \text{ K}^{-1}$$
        $$\frac{E_a}{k_B} \Delta(1/T) = \frac{0.90 \text{ eV}}{8.617 \times 10^{-5} \text{ eV/K}} \times (-1.329 \times 10^{-4} \text{ K}^{-1}) = 10,444.5 \times (-1.329 \times 10^{-4}) = -1.388$$
        $$\exp(-1.388) = \mathbf{0.2496}$$</li>
      </ul>
      <p>Combined lifetime ratio:</p>
      $$\frac{\text{MTTF}_2}{\text{MTTF}_1} = 0.4444 \times 0.2496 = \mathbf{0.1109}$$
      $$\text{MTTF}_2 = 10 \text{ years} \times 0.1109 = \mathbf{1.11 \text{ years}}$$
      <p>A $50\%$ increase in current density combined with a $20^\circ\text{C}$ temperature rise slashes the microprocessor lifetime from <strong>10 years down to just 1.1 years</strong> (an $89\%$ reduction in reliability!).</p>
    </div>
    <div class="final-answer-box">
      <strong>Electromigration Force:</strong> Dominated by the ballistic <strong>electron wind force</strong> pushing atoms toward the anode.<br>
      <strong>Black's Law:</strong> $$\text{MTTF} = \frac{A}{j^n}\exp\left(\frac{E_a}{k_B T}\right)$$
      Overclocking reduces interconnect lifetime from $\mathbf{10 \text{ years}}$ to $\mathbf{1.1 \text{ years}}$ ($\approx 89\%$ reduction).
    </div>""")

# P49: Thermomigration (Soret Effect)
add(49, "Thermomigration (Soret Effect): Thermal Gradient Driven Atomic Transport",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Intermediate",
    r"""<p>Thermomigration (the Soret effect) is directional atomic mass transport driven by steep temperature gradients ($\nabla T$).</p>
    <ol type="a">
      <li>State the atomic flux equation for <strong>thermomigration</strong> in a temperature gradient $\frac{dT}{dx}$:
      $$J_{\text{TM}} = -\frac{C D Q^*}{R T^2} \frac{dT}{dx}$$
      Define the <strong>heat of transport $Q^*$</strong> and explain what determines whether solute atoms migrate toward the hotter region ($Q^* < 0$) or the colder region ($Q^* > 0$).</li>
      <li>In nuclear reactor uranium dioxide fuel pellets ($\text{UO}_2$), an extreme temperature gradient of $\nabla T = 5000^\circ\text{C/cm}$ ($5.0 \times 10^5 \text{ K/m}$) exists between the centerline ($2000^\circ\text{C}$) and the cooled surface ($800^\circ\text{C}$). Explain how thermomigration drives oxygen redistribution and the formation of a central void.</li>
      <li>In microelectronic flip-chip solder bumps operating at high power densities, temperature gradients can exceed $1000^\circ\text{C/cm}$. How does thermomigration cause voiding and open-circuit failures?</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Thermomigration Flux and Heat of Transport $Q^*$</div>
      $$J_{\text{TM}} = -\frac{C D Q^*}{R T^2} \frac{dT}{dx}$$
      <p>The <strong>heat of transport $Q^*$</strong> represents the net thermal energy carried by an atom per mole during an atomic jump, minus the enthalpy of the atom on its lattice site:</p>
      <ul>
        <li><strong>If $Q^* > 0$ (Positive Heat of Transport):</strong> The diffusing atom transports excess heat forward. Energetically, jumping toward the colder side lowers free energy: atoms migrate <strong>down the thermal gradient from HOT to COLD</strong>.</li>
        <li><strong>If $Q^* < 0$ (Negative Heat of Transport):</strong> Atoms migrate <strong>up the thermal gradient from COLD to HOT</strong> (common for interstitial carbon and nitrogen in certain refractory metals).</li>
      </ul>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Centerline Void Formation in Nuclear Fuel Pins ($\text{UO}_2$)</div>
      <p>In operating $\text{UO}_2$ nuclear reactor fuel rods, the thermal gradient is immense ($\sim 5 \times 10^5 \text{ K/m}$). Pores and bubbles migrate rapidly up the thermal gradient toward the hot center via an evaporation-condensation mechanism (vaporizing at the hot side of the pore and condensing on the cold side). As millions of pores migrate inward, they coalesce at the cylinder axis, forming a hollow, continuous <strong>central void tunnel</strong> surrounded by columnar grain structures.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Thermomigration in Flip-Chip Solder Bumps</div>
      <p>In high-power semiconductor packaging, Joule heating concentrates at tiny contact corners where current enters the solder bump, generating steep localized temperature gradients ($\nabla T > 1000^\circ\text{C/cm}$ over a $50 \mu\text{m}$ bump). Under this driving force, tin and lead atoms migrate rapidly from the hot silicon chip side toward the colder organic substrate side. This leaves behind a dense band of coalesced vacancy voids at the hot interface, culminating in sudden electrical open-circuit failure.</p>
    </div>
    <div class="final-answer-box">
      <strong>Thermomigration Flux:</strong> $$J_{\text{TM}} = -\frac{CDQ^*}{RT^2}\frac{dT}{dx}$$
      $Q^* > 0 \implies$ transport to COLD &bull; $Q^* < 0 \implies$ transport to HOT.<br>
      Drives central hole formation in nuclear fuel pellets and voiding in microelectronic solder bumps.
    </div>""")

# P50: Comprehensive Diffusion Synthesis Problem
add(50, "Comprehensive Diffusion Synthesis: Multi-Stage Industrial Carburizing and Microstructure Control",
    "Short-Circuit Paths & Microstructure", "short_circuits", "Advanced",
    r"""<p>An automotive powertrain manufacturer produces heavy-duty truck drive pinions from AISI 8620 steel ($C_0 = 0.20 \text{ wt}\%$). The specifications require a surface carbon content of $0.85 \text{ wt}\%$ (to prevent brittle retained austenite) and an effective case depth of $1.00 \text{ mm}$ (where $C = 0.40 \text{ wt}\%$).</p>
    <div class="highlight-box">
      <strong>Two-Stage "Boost-Diffuse" Industrial Carburizing Cycle:</strong>
      <ul>
        <li><strong>Stage 1 (Boost Stage at $950^\circ\text{C}$):</strong> A rich carburizing gas holds surface carbon at the austenite solubility limit $C_s = 1.20 \text{ wt}\%$ for $t_1 = 4.0 \text{ hours}$. ($D_1 = 1.28 \times 10^{-11} \text{ m}^2/\text{s}$).</li>
        <li><strong>Stage 2 (Diffuse Stage at $950^\circ\text{C}$):</strong> The gas atmosphere carbon potential is lowered to hold the surface at $C_s = 0.85 \text{ wt}\%$ while carbon continues diffusing deeper into the core for duration $t_2$.</li>
      </ul>
    </div>
    <ol type="a">
      <li>Calculate the carbon content at depth $x = 1.00 \text{ mm}$ at the conclusion of Stage 1 ($t_1 = 4.0 \text{ hr}$). Is the required specification met by Stage 1 alone?</li>
      <li>Calculate the total mass of carbon absorbed per square meter of gear surface ($M_t$ in $\text{g/m}^2$) during the 4-hour Boost stage.</li>
      <li>Explain the metallurgical necessity of the two-stage "Boost-Diffuse" process: Why would quenching directly from a single-stage carburization at $1.20 \text{ wt}\%$ carbon cause excessive <strong>retained austenite</strong> and microcracking?</li>
      <li>Synthesize how short-circuit grain boundary diffusion during the final oil quench influences the depth of martensite transformation.</li>
    </ol>""",
    r"""<div class="solution-step">
      <div class="solution-step-title">Part (a): Carbon Content after Stage 1 (Boost Stage, $t_1 = 4.0 \text{ hr} = 14,400 \text{ s}$)</div>
      <p>Given $C_0 = 0.20 \text{ wt}\%, C_s = 1.20 \text{ wt}\%, D_1 = 1.28 \times 10^{-11} \text{ m}^2/\text{s}, x = 1.00 \text{ mm} = 1.0 \times 10^{-3} \text{ m}$:</p>
      $$2\sqrt{D_1 t_1} = 2 \sqrt{(1.28 \times 10^{-11} \text{ m}^2/\text{s}) \times (14,400 \text{ s})} = 2 \sqrt{1.8432 \times 10^{-7} \text{ m}^2} = 2 \times (4.2932 \times 10^{-4} \text{ m}) = 8.5865 \times 10^{-4} \text{ m}$$
      $$z = \frac{x}{2\sqrt{D_1 t_1}} = \frac{1.0 \times 10^{-3} \text{ m}}{8.5865 \times 10^{-4} \text{ m}} = \mathbf{1.1646}$$
      <p>Using standard error function values: $\text{erf}(1.10) = 0.8802, \text{erf}(1.20) = 0.9103$:</p>
      $$\text{erf}(1.1646) = 0.8802 + \left(\frac{1.1646 - 1.10}{0.10}\right) \times (0.9103 - 0.8802) = 0.8802 + 0.646 \times (0.0301) = 0.8802 + 0.0194 = \mathbf{0.8996}$$
      $$\frac{C(1.00 \text{ mm}) - 0.20}{1.20 - 0.20} = 1 - \text{erf}(z) = 1 - 0.8996 = 0.1004$$
      $$C(1.00 \text{ mm}) = 0.20 + 0.1004(1.00) = \mathbf{0.300 \text{ wt}\%}$$
      <p><strong>Specification Check:</strong> At $1.00 \text{ mm}$, the carbon content is only $0.30 \text{ wt}\%$, which falls short of the required $0.40 \text{ wt}\%$. The specification is <strong>not met</strong> by Stage 1 alone; additional diffuse time is mandatory.</p>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (b): Total Carbon Absorbed during Boost Stage ($M_t$)</div>
      <p>Using the integrated mass uptake formula from Problem 25:</p>
      $$\Delta C = (1.20 - 0.20 \text{ wt}\%) \times 7800 \text{ kg/m}^3 = 78.0 \text{ kg/m}^3$$
      $$M_t = 2 \Delta C \sqrt{\frac{D_1 t_1}{\pi}} = 2 \times (78.0) \times \sqrt{\frac{1.8432 \times 10^{-7} \text{ m}^2}{\pi}} = 156.0 \times \sqrt{5.867 \times 10^{-8}} = 156.0 \times (2.422 \times 10^{-4} \text{ m})$$
      $$M_t = 0.03779 \text{ kg/m}^2 = \mathbf{37.79 \text{ g/m}^2}$$
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (c): Metallurgical Necessity of Boost-Diffuse Cycle</div>
      <p>If the gear were quenched directly with $1.20 \text{ wt}\%$ surface carbon:</p>
      <ol>
        <li>High dissolved carbon depresses the martensite finish temperature ($M_f$) far below room temperature ($M_f \approx -50^\circ\text{C}$). Upon oil quenching to $25^\circ\text{C}$, the transformation cannot complete, leaving $30\text{--}50\%$ soft, ductile <strong>retained austenite</strong> at the surface. Retained austenite degrades surface hardness from 62 HRC down to $< 52 \text{ HRC}$ and causes catastrophic contact fatigue spalling.</li>
        <li>Excessive carbon causes continuous proeutectoid cementite ($\text{Fe}_3\text{C}$) networks to precipitate along prior austenite grain boundaries during cooling, leading to severe embrittlement.</li>
        <li>The <strong>Diffuse stage</strong> lowers surface carbon to the eutectoid composition ($0.80\text{--}0.85\text{ wt}\%$), raising $M_s/M_f$ to ensure $100\%$ transformation to hard plate martensite while driving carbon deeper to satisfy the $1.00 \text{ mm}$ case depth specification.</li>
      </ol>
    </div>
    <div class="solution-step">
      <div class="solution-step-title">Part (d): Microstructure Synthesis During Quenching</div>
      <p>During the rapid quench, carbon diffusion is kinetically frozen in the bulk lattice, trapping carbon into octahedral interstitial sites to force the diffusionless FCC $\to$ BCT martensite transformation. However, in the lower-carbon core ($0.20 \text{ wt}\%$, high $M_s \approx 420^\circ\text{C}$), the transformation begins earlier, forming high-toughness lath martensite and bainite. The resulting composite component possesses a wear-resistant, high-hardness case ($62 \text{ HRC}$) under compressive residual stress, supported by a ductile, fracture-resistant core ($32 \text{ HRC}$).</p>
    </div>
    <div class="final-answer-box">
      <strong>Stage 1 Result:</strong> $C(1.0\text{ mm}) = \mathbf{0.30 \text{ wt}\%}$ (spec not met; diffuse stage required).<br>
      <strong>Carbon Uptake:</strong> $M_t = \mathbf{37.79 \text{ g/m}^2}$ absorbed in Boost stage.<br>
      <strong>Boost-Diffuse Rationale:</strong> Lowers surface carbon to $0.85\text{ wt}\%$ to eliminate soft retained austenite and grain-boundary carbide networks while driving carbon to $1.0\text{ mm}$ depth.
    </div>""")

# Save Chapter 5 dataset
with open("generator/ch5_data.py", "w", encoding="utf-8") as f:
    f.write("# ==============================================================================\n")
    f.write("# CHAPTER 5: DIFFUSION IN SOLIDS\n")
    f.write("# 50 Curated Problems with Detailed Step-by-Step Solutions\n")
    f.write("# University of Tehran | Dept. of Mechanical Engineering | Prof. Sadeghi\n")
    f.write("# Prepared by: Sina Sharifi (TA)\n")
    f.write("# ==============================================================================\n\n")
    f.write("PROBLEMS = " + json.dumps(P, indent=2, ensure_ascii=False))

print(f"Chapter 5 complete! Successfully generated {len(P)} problems in generator/ch5_data.py.")
