# generator/make_ch8_part2.py
import sys
import os
import re

import make_ch8_part1

P = list(make_ch8_part1.P)

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
    "title": "S-N Wöhler Curves: Endurance Limit in Steels vs. Non-Ferrous Alloys",
    "difficulty": "Easy",
    "category": "Fatigue Failure",
    "tags": ["S-N Curve", "Endurance Limit", "Wöhler Curve", "Fatigue Ratio"],
    "statement": r"""A standard rotating-beam fatigue test (R. R. Moore machine, $R = -1.0$) measures the relationship between stress amplitude $\sigma_a$ and cycles to failure $N_f$, producing an S-N (Wöhler) curve.
<br><br>
1. Contrast the S-N curves of <strong>ferrous alloys</strong> (steels and titanium) and <strong>non-ferrous alloys</strong> (aluminum, copper, magnesium):
   (a) Define the <strong>fatigue endurance limit ($\sigma_e$)</strong> in steels. What does a horizontal plateau at $10^6\text{--}10^7$ cycles signify?<br>
   (b) How is fatigue performance specified for aluminum alloys that show no endurance limit (define <strong>fatigue strength at $N$ cycles</strong>)?<br>
2. For plain carbon and low-alloy steels with $\sigma_{\text{UTS}} \le 1400\text{ MPa}$, the endurance limit is empirically related to tensile strength by the fatigue ratio:
$$\sigma_e \approx 0.50\,\sigma_{\text{UTS}}$$
Calculate $\sigma_e$ for a 1045 medium-carbon steel with $\sigma_{\text{UTS}} = 620\text{ MPa}$.<br>
3. What is the physical dislocation mechanism responsible for the distinct endurance limit in steels that is absent in aluminum?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Comparison of S-N curves</strong><br>
(a) <strong>Ferrous Alloys (Steels):</strong> The S-N curve slopes downward initially, but between $10^6$ and $10^7$ cycles, it bends into a sharp knee and transitions into a flat, horizontal plateau. The stress level corresponding to this horizontal plateau is the <strong>fatigue endurance limit ($\sigma_e$)</strong>. If the cyclic stress amplitude remains below $\sigma_e$, the component can theoretically endure an infinite number of cycles ($N \to \infty$) without ever fracturing.<br>
(b) <strong>Non-Ferrous Alloys (Aluminum):</strong> The S-N curve continues to slope downward continuously with increasing cycles, showing no horizontal plateau. There is no true endurance limit. Instead, engineers define the <strong>fatigue strength at a designated life</strong> (typically $\sigma_{f, 10^7}$ or $\sigma_{f, 10^8}$ cycles), meaning aluminum parts must be designed for a finite, inspected fatigue life rather than infinite life.
</div>
<div class="solution-step">
<strong>Step 2: Calculate endurance limit for 1045 steel</strong><br>
Given $\sigma_{\text{UTS}} = 620\text{ MPa}$:
$$\sigma_e = 0.50 \times 620\text{ MPa} = 310.0\text{ MPa}$$
For smooth polished specimens under fully reversed bending, the steel can withstand infinite cycles at stress amplitudes up to $310\text{ MPa}$.
</div>
<div class="solution-step">
<strong>Step 3: Dislocation mechanism behind the endurance limit</strong><br>
The existence of an endurance limit in steels is governed by <strong>interstitial solute pinning (Cottrell atmospheres)</strong>:
- In steels, mobile interstitial carbon and nitrogen atoms rapidly diffuse to pinning sites and lock dislocations firmly in place.
- If the cyclic stress amplitude is below $\sigma_e$, the stress is insufficient to tear dislocations free from their Cottrell atmospheres or activate new dislocation sources. Dislocation glide is completely suppressed, preventing the formation of persistent slip bands and microcracks.
- In aluminum alloys, there are no interstitial Cottrell atmospheres locking dislocations. Dislocation glide, cross-slip, and irreversible slip steps occur even at infinitesimal cyclic stresses, eventually accumulating enough localized damage to nucleate a fatigue crack given sufficient cycles.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Steels exhibit a true horizontal endurance limit ($\sigma_e \approx 0.5 \sigma_{\text{UTS}}$) below which life is infinite.<br>
Aluminum displays no endurance limit; must be designed for finite life (fatigue strength at $10^7\text{--}10^8$ cycles).<br>
1045 steel endurance limit: $\sigma_e = 310.0\text{ MPa}$.<br>
Endurance limit is created by interstitial carbon Cottrell atmospheres pinning dislocations below threshold stress.
</div>"""
})

# ==========================================
# Problem 27
# ==========================================
add({
    "num": 27,
    "title": "Basquin's Equation for High-Cycle Fatigue (HCF)",
    "difficulty": "Medium",
    "category": "Fatigue Failure",
    "tags": ["Basquin Equation", "High-Cycle Fatigue", "S-N Curve", "Fatigue Exponent"],
    "statement": r"""In the high-cycle fatigue regime ($N_f > 10^4$ cycles), cyclic deformation is predominantly elastic and follows Basquin's power-law equation:
$$\sigma_a = \sigma_f' (2N_f)^b$$
where $\sigma_a$ is the alternating stress amplitude, $2N_f$ is the number of stress reversals to failure (1 cycle $= 2$ reversals), $\sigma_f'$ is the fatigue strength coefficient ($\approx \sigma_{\text{true, fracture}}$), and $b$ is the fatigue strength exponent (typically $-0.05\text{ to }-0.12$).
<br><br>
A forged alloy steel has Basquin parameters: $\sigma_f' = 1150\text{ MPa}$ and $b = -0.085$.
<br><br>
1. Calculate the expected fatigue life $N_f$ (in cycles) under a fully reversed stress amplitude $\sigma_a = 450\text{ MPa}$.<br>
2. Calculate the fatigue life $N_f'$ if the stress amplitude is increased by $20\%$ to $\sigma_a' = 540\text{ MPa}$.<br>
3. By what factor did fatigue life decrease as a result of a modest $20\%$ increase in stress amplitude? What does this demonstrate about fatigue sensitivity?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate fatigue life for $\sigma_a = 450\text{ MPa}$</strong><br>
From $\sigma_a = \sigma_f' (2N_f)^b$:
$$(2N_f)^b = \frac{\sigma_a}{\sigma_f'} \implies 2N_f = \left(\frac{\sigma_a}{\sigma_f'}\right)^{1/b}$$
Given: $\sigma_a = 450\text{ MPa}$, $\sigma_f' = 1150\text{ MPa}$, $b = -0.085$:
$$\frac{1}{b} = \frac{1}{-0.085} \approx -11.7647$$
$$\frac{\sigma_a}{\sigma_f'} = \frac{450}{1150} \approx 0.391304$$
$$2N_f = (0.391304)^{-11.7647} = \left(\frac{1}{0.391304}\right)^{11.7647} = (2.55556)^{11.7647}$$
$$\ln(2.55556) \approx 0.93827$$
$$\text{Exponent} = 11.7647 \times 0.93827 \approx 11.0384$$
$$2N_f = \exp(11.0384) \approx 62,217\text{ reversals}$$
$$N_f = \frac{62,217}{2} \approx 31,108\text{ cycles} \approx 3.11 \times 10^4\text{ cycles}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate fatigue life for $\sigma_a' = 540\text{ MPa}$</strong><br>
$$\frac{\sigma_a'}{\sigma_f'} = \frac{540}{1150} \approx 0.469565$$
$$2N_f' = (0.469565)^{-11.7647} = (2.12963)^{11.7647}$$
$$\ln(2.12963) \approx 0.75595$$
$$\text{Exponent} = 11.7647 \times 0.75595 \approx 8.8935$$
$$2N_f' = \exp(8.8935) \approx 7,284\text{ reversals}$$
$$N_f' = \frac{7,284}{2} \approx 3,642\text{ cycles}$$
</div>
<div class="solution-step">
<strong>Step 3: Life reduction factor and sensitivity</strong><br>
$$\text{Reduction Factor} = \frac{N_f}{N_f'} = \frac{31,108}{3,642} \approx 8.54$$
$$\frac{N_f}{N_f'} = \left(\frac{\sigma_a'}{\sigma_a}\right)^{-1/b} = (1.20)^{11.765} \approx 8.54$$
A mere <strong>$20\%$ increase in stress amplitude causes an $8.5\times$ ($850\%$) collapse in fatigue life</strong>!
This power-law sensitivity ($\sim \sigma^{-12}$) demonstrates why precision in stress calculation, avoidance of minor stress concentrations, and control of surface roughness are critically vital in fatigue design.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
At $\sigma_a = 450\text{ MPa}$: $N_f = 31,108\text{ cycles}$<br>
At $\sigma_a = 540\text{ MPa}$: $N_f = 3,642\text{ cycles}$<br>
A $20\%$ increase in stress reduces fatigue life by $8.5\times$ due to the steep power-law exponent ($1/b \approx -11.8$).
</div>"""
})

# ==========================================
# Problem 28
# ==========================================
add({
    "num": 28,
    "title": "Mean Stress Effects on Fatigue: Goodman vs. Gerber and Soderberg Relations",
    "difficulty": "Hard",
    "category": "Fatigue Failure",
    "tags": ["Goodman Relation", "Gerber Parabola", "Soderberg Line", "Mean Stress Effect"],
    "statement": r"""When a component is subjected to a cyclic stress with non-zero mean stress ($\sigma_m \neq 0$), the permissible alternating stress amplitude $\sigma_a$ is reduced according to empirical mean stress relations:
- <strong>Modified Goodman Line:</strong> $\frac{\sigma_a}{\sigma_e} + \frac{\sigma_m}{\sigma_{\text{UTS}}} = 1$
- <strong>Gerber Parabola:</strong> $\frac{\sigma_a}{\sigma_e} + \left(\frac{\sigma_m}{\sigma_{\text{UTS}}}\right)^2 = 1$
- <strong>Soderberg Line (prevents gross yielding):</strong> $\frac{\sigma_a}{\sigma_e} + \frac{\sigma_m}{\sigma_y} = 1$
<br>
A forged suspension arm made of quenched-and-tempered alloy steel has:
$\sigma_y = 750\text{ MPa}$, $\sigma_{\text{UTS}} = 900\text{ MPa}$, and fully reversed endurance limit $\sigma_e = 420\text{ MPa}$.
The component operates under a mean tensile stress $\sigma_m = 300\text{ MPa}$.
<br><br>
1. Calculate the maximum allowable stress amplitude $\sigma_a$ predicted by:
   (a) The Modified Goodman relation.<br>
   (b) The Gerber parabola.<br>
   (c) The Soderberg relation.<br>
2. Rank the three criteria in order of conservatism.<br>
3. If an operating stress cycle has $\sigma_m = 300\text{ MPa}$ and $\sigma_a = 260\text{ MPa}$, determine whether fatigue failure will occur according to Goodman, Gerber, and Soderberg.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate allowable stress amplitude $\sigma_a$</strong><br>
Given: $\sigma_e = 420\text{ MPa}$, $\sigma_{\text{UTS}} = 900\text{ MPa}$, $\sigma_y = 750\text{ MPa}$, $\sigma_m = 300\text{ MPa}$.
<br>
(a) <em>Modified Goodman:</em>
$$\frac{\sigma_a}{\sigma_e} = 1 - \frac{\sigma_m}{\sigma_{\text{UTS}}} = 1 - \frac{300}{900} = 1 - \frac{1}{3} = \frac{2}{3} \approx 0.6667$$
$$\sigma_{a, \text{Goodman}} = \frac{2}{3} \times 420\text{ MPa} = 280.0\text{ MPa}$$
<br>
(b) <em>Gerber Parabola:</em>
$$\frac{\sigma_a}{\sigma_e} = 1 - \left(\frac{\sigma_m}{\sigma_{\text{UTS}}}\right)^2 = 1 - \left(\frac{300}{900}\right)^2 = 1 - \left(\frac{1}{3}\right)^2 = 1 - \frac{1}{9} = \frac{8}{9} \approx 0.8889$$
$$\sigma_{a, \text{Gerber}} = \frac{8}{9} \times 420\text{ MPa} \approx 373.33\text{ MPa}$$
<br>
(c) <em>Soderberg:</em>
$$\frac{\sigma_a}{\sigma_e} = 1 - \frac{\sigma_m}{\sigma_y} = 1 - \frac{300}{750} = 1 - 0.40 = 0.600$$
$$\sigma_{a, \text{Soderberg}} = 0.600 \times 420\text{ MPa} = 252.0\text{ MPa}$$
</div>
<div class="solution-step">
<strong>Step 2: Conservatism ranking</strong><br>
$$\sigma_{a, \text{Soderberg}} (252\text{ MPa}) < \sigma_{a, \text{Goodman}} (280\text{ MPa}) < \sigma_{a, \text{Gerber}} (373\text{ MPa})$$
1. <strong>Soderberg</strong> is the most conservative criterion because it bases mean stress limit on yield strength ($\sigma_y$), completely guarding against both fatigue and static plastic yielding.
2. <strong>Goodman</strong> provides a balanced, safe engineering design standard and is used widely in aerospace and automotive codes.
3. <strong>Gerber</strong> is the least conservative, fitting experimental test data of ductile metals closely but providing smaller safety margins.
</div>
<div class="solution-step">
<strong>Step 3: Evaluation of proposed cycle ($\sigma_m = 300\text{ MPa}, \sigma_a = 260\text{ MPa}$)</strong><br>
- <em>Under Soderberg ($\sigma_{a, \text{max}} = 252\text{ MPa}$):</em> $\sigma_a = 260\text{ MPa} > 252\text{ MPa} \implies$ <strong>Predicted to FAIL</strong> ($N_S = 252/260 = 0.97$).
- <em>Under Goodman ($\sigma_{a, \text{max}} = 280\text{ MPa}$):</em> $\sigma_a = 260\text{ MPa} < 280\text{ MPa} \implies$ <strong>Predicted to SURVIVE</strong> ($N_G = 280/260 = 1.08$).
- <em>Under Gerber ($\sigma_{a, \text{max}} = 373\text{ MPa}$):</em> $\sigma_a = 260\text{ MPa} \ll 373\text{ MPa} \implies$ <strong>Predicted to SURVIVE</strong> ($N_{\text{Gerber}} = 373/260 = 1.44$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Soderberg: $\sigma_a = 252.0\text{ MPa}$ (Most conservative)<br>
Goodman: $\sigma_a = 280.0\text{ MPa}$ (Standard engineering design)<br>
Gerber: $\sigma_a = 373.3\text{ MPa}$ (Least conservative)<br>
For $\sigma_a = 260\text{ MPa}$ at $\sigma_m = 300\text{ MPa}$: Fails Soderberg ($N = 0.97$), survives Goodman ($N = 1.08$) and Gerber ($N = 1.44$).
</div>"""
})

# ==========================================
# Problem 29
# ==========================================
add({
    "num": 29,
    "title": "Low-Cycle Fatigue (LCF): The Coffin-Manson Relation and Transition Life",
    "difficulty": "Hard",
    "category": "Fatigue Failure",
    "tags": ["Coffin-Manson", "Low-Cycle Fatigue", "Transition Life", "Plastic Strain"],
    "statement": r"""In Low-Cycle Fatigue (LCF, $N_f < 10^4$ cycles), cyclic loading exceeds the yield strength, and plastic strain amplitude governs damage accumulation.
The total strain amplitude $\frac{\Delta\varepsilon}{2}$ is the sum of elastic and plastic components (Morrow total strain-life equation):
$$\frac{\Delta\varepsilon}{2} = \frac{\Delta\varepsilon_e}{2} + \frac{\Delta\varepsilon_p}{2} = \frac{\sigma_f'}{E} (2N_f)^b + \varepsilon_f' (2N_f)^c$$
where the second term is the <strong>Coffin-Manson relation</strong> for plastic strain life.
For a titanium alloy Ti-6Al-4V ($E = 110\text{ GPa}$):
$\sigma_f' = 1250\text{ MPa}$, $b = -0.095$, $\varepsilon_f' = 0.35$, $c = -0.60$.
<br><br>
1. Define the <strong>transition fatigue life ($2N_t$)</strong> where the elastic strain amplitude equals the plastic strain amplitude ($\Delta\varepsilon_e / 2 = \Delta\varepsilon_p / 2$).<br>
2. Calculate the transition life $2N_t$ (in reversals) and $N_t$ (in cycles) for this titanium alloy.<br>
3. If an aerospace compressor disc operates at an imposed total strain range $\Delta\varepsilon = 0.018$ ($\Delta\varepsilon/2 = 0.009$), which component dominates: elastic or plastic strain? Calculate the expected fatigue life $N_f$.<br>
4. Why is high tensile ductility ($\varepsilon_f'$) the most critical material property for surviving low-cycle fatigue, whereas high tensile strength ($\sigma_{\text{UTS}}$) is required for high-cycle fatigue?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Definition of Transition Life $2N_t$</strong><br>
At the transition life $2N_t$, elastic strain amplitude equals plastic strain amplitude:
$$\frac{\sigma_f'}{E} (2N_t)^b = \varepsilon_f' (2N_t)^c$$
Rearranging:
$$(2N_t)^{b - c} = \frac{\varepsilon_f' E}{\sigma_f'} \implies 2N_t = \left(\frac{\varepsilon_f' E}{\sigma_f'}\right)^{\frac{1}{b - c}}$$
For lives shorter than $2N_t$ (LCF), plastic strain dominates; for lives longer than $2N_t$ (HCF), elastic strain dominates.
</div>
<div class="solution-step">
<strong>Step 2: Calculate transition life $2N_t$</strong><br>
Given: $\sigma_f' = 1250\text{ MPa}$, $E = 110 \times 10^3\text{ MPa}$, $\varepsilon_f' = 0.35$, $b = -0.095$, $c = -0.60$:
$$\frac{\varepsilon_f' E}{\sigma_f'} = \frac{0.35 \times 110,000\text{ MPa}}{1250\text{ MPa}} = \frac{38,500}{1250} = 30.80$$
Exponent:
$$b - c = -0.095 - (-0.60) = +0.505$$
$$\frac{1}{b - c} = \frac{1}{0.505} \approx 1.9802$$
Transition reversals:
$$2N_t = (30.80)^{1.9802} \approx 893\text{ reversals}$$
Transition cycles:
$$N_t = \frac{893}{2} \approx 446\text{ cycles}$$
</div>
<div class="solution-step">
<strong>Step 3: Fatigue life for $\Delta\varepsilon/2 = 0.009$</strong><br>
At $\Delta\varepsilon/2 = 0.009$, the total strain is large, so plastic strain dominates.
Testing Coffin-Manson term alone as first estimate:
$$\varepsilon_f' (2N_f)^c \approx 0.009 \implies (2N_f)^{-0.60} = \frac{0.009}{0.35} \approx 0.025714$$
$$2N_f = (0.025714)^{-1/0.60} = (0.025714)^{-1.6667} \approx 442\text{ reversals}$$
At $2N_f = 442$:
$$\text{Plastic strain} = 0.35 \times (442)^{-0.60} \approx 0.00898$$
$$\text{Elastic strain} = \frac{1250}{110,000} \times (442)^{-0.095} = 0.01136 \times 0.559 \approx 0.00635$$
Total strain $= 0.00898 + 0.00635 = 0.01533 > 0.009$.
Solving $\frac{1250}{110,000}(2N_f)^{-0.095} + 0.35(2N_f)^{-0.60} = 0.009$:
At $2N_f = 1,400$ reversals:
$$\text{Elastic} = 0.01136 \times (1400)^{-0.095} = 0.01136 \times 0.5015 \approx 0.00570$$
$$\text{Plastic} = 0.35 \times (1400)^{-0.60} = 0.35 \times 0.01306 \approx 0.00457$$
Sum $= 0.00570 + 0.00457 = 0.01027$.
At $2N_f = 2,000$ reversals:
$$\text{Elastic} = 0.01136 \times (2000)^{-0.095} = 0.01136 \times 0.4847 \approx 0.00551$$
$$\text{Plastic} = 0.35 \times (2000)^{-0.60} = 0.35 \times 0.01053 \approx 0.00369$$
Sum $= 0.00551 + 0.00369 = 0.00920 \approx 0.0090$.
Thus $2N_f \approx 2,150\text{ reversals} \implies N_f \approx 1,075\text{ cycles}$.
</div>
<div class="solution-step">
<strong>Step 4: Ductility vs. Strength in LCF and HCF</strong><br>
- <em>In Low-Cycle Fatigue (LCF):</em> Deformation is strain-controlled. The material is repeatedly forced through large plastic strains. Plastic strain energy absorption is proportional to ductility ($\varepsilon_f'$). High ductility allows the material to accommodate plastic strain cycles without void nucleation.
- <em>In High-Cycle Fatigue (HCF):</em> Strains are small and purely elastic. Failure is stress-controlled. Resisting dislocation emission requires high yield strength and high ultimate tensile strength ($\sigma_{\text{UTS}}$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Transition life: $2N_t = 893\text{ reversals}$ ($N_t \approx 446\text{ cycles}$).<br>
For $\Delta\varepsilon/2 = 0.009$: $N_f \approx 1,075\text{ cycles}$.<br>
High ductility ($\varepsilon_f'$) governs LCF resistance, whereas high strength ($\sigma_{\text{UTS}}$) governs HCF resistance.
</div>"""
})

# ==========================================
# Problem 30
# ==========================================
add({
    "num": 30,
    "title": "Microstructural Stages of Fatigue: Persistent Slip Bands and Crack Initiation",
    "difficulty": "Medium",
    "category": "Fatigue Failure",
    "tags": ["Persistent Slip Bands", "PSB", "Extrusions", "Intrusions", "Stage I Initiation"],
    "statement": r"""Fatigue failure progresses through three distinct physical stages:
$$\text{Stage I: Microscopic Crack Initiation} \longrightarrow \text{Stage II: Stable Crack Propagation} \longrightarrow \text{Stage III: Catastrophic Overload}$$
<br>
1. Describe the formation of <strong>Persistent Slip Bands (PSBs)</strong> in Stage I under cyclic shearing:
   (a) What dislocation structure forms inside PSBs (ladder structure)?<br>
   (b) Describe how irreversible dislocation glide generates surface <strong>extrusions</strong> (ridges) and <strong>intrusions</strong> (notches).<br>
2. Along which crystallographic planes and at what angle to the macroscopic tensile axis does a Stage I crack propagate?<br>
3. What event marks the transition from Stage I initiation to Stage II propagation, and how does the crack growth direction change?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Persistent Slip Bands (PSBs) and surface topography</strong><br>
(a) <em>Ladder Dislocation Structure:</em> Under cyclic plastic straining, dislocations rearrange to minimize elastic energy, forming thin, ribbon-like zones ($1\text{ to }2\text{ }\mu\text{m}$ wide) called <strong>Persistent Slip Bands (PSBs)</strong> that traverse entire grains. Inside the PSB, edge dislocations form a dense, periodic array of parallel dipolar walls ("ladder rungs") spaced $\sim 1\text{ }\mu\text{m}$ apart, with virtually dislocation-free channels between them where screw dislocations glide back and forth.<br>
(b) <em>Extrusions and Intrusions:</em> During forward tensile loading, screw dislocations glide on slip plane 1 and cross-slip. Upon load reversal in compression, reverse glide occurs on a neighboring parallel slip plane 2 rather than the original plane (irreversible slip). Over thousands of cycles, this ratcheting net displacement pumps atomic slabs out of the surface, creating microscopic ridges called <strong>extrusions</strong> (height $\sim 1\text{ }\mu\text{m}$) and sharp micro-notches called <strong>intrusions</strong> (depth $\sim 1\text{ }\mu\text{m}$).
</div>
<div class="solution-step">
<strong>Step 2: Stage I crack propagation</strong><br>
The sharp notch created by a surface intrusion acts as an intense local stress concentration. A Stage I microcrack initiates at the root of the intrusion and propagates by shear along the primary <strong>active close-packed slip planes ($\{111\}$ in FCC) oriented at $45^\circ$</strong> to the macroscopic tensile axis (the orientation of maximum shear stress $\tau_{\text{max}}$).
Stage I crack growth is extremely slow (fractions of a nanometer per cycle) and extends only through 1 to 3 grain diameters ($10\text{--}50\text{ }\mu\text{m}$).
</div>
<div class="solution-step">
<strong>Step 3: Transition from Stage I to Stage II</strong><br>
The transition occurs when:
1. The microcrack reaches an impenetrable obstacle (a high-angle grain boundary or hard phase) that blocks single-plane coplanar shear.
2. The stress intensity factor $K_I$ at the crack tip grows large enough to activate multiple symmetric slip systems on intersecting conjugate planes simultaneously.
At this transition, the crack turns $45^\circ$ and begins propagating <strong>perpendicular ($90^\circ$) to the maximum tensile stress axis</strong> via alternating plastic blunting and resharpening, entering <strong>Stage II macroscopic propagation</strong>.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
PSBs contain dislocation ladder structures where irreversible cyclic slip creates surface extrusions and intrusions.<br>
Stage I crack initiates at intrusion roots and propagates along $45^\circ$ maximum shear planes across $1\text{--}3$ grains.<br>
Stage II transition turns the crack to $90^\circ$ perpendicular to tensile stress, advancing via striation formation.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 8 Part 2: P26-P30 added. Current total: {len(P)}")

# ==========================================
# Problem 31
# ==========================================
add({
    "num": 31,
    "title": "Beachmarks vs. Fatigue Striations: Diagnostic Fractography",
    "difficulty": "Easy",
    "category": "Fatigue Fractography",
    "tags": ["Beachmarks", "Fatigue Striations", "SEM Fractography", "Failure Analysis"],
    "statement": r"""A forensic failure analyst must testify in an aircraft accident investigation regarding the fatigue fracture of a landing gear actuator cylinder.
The report must distinguish unambiguously between <strong>macroscopic beachmarks</strong> (clamshell marks) and <strong>microscopic fatigue striations</strong>.
<br><br>
1. Complete a comprehensive comparison table between beachmarks and fatigue striations across the following 5 criteria:
   (a) Scale of observation / Required magnification.<br>
   (b) Spacing between successive marks.<br>
   (c) Physical origin / Cause of formation.<br>
   (d) Relationship between number of marks and elapsed load cycles ($1:1$ correspondence?).<br>
   (e) Presence in pure, continuous laboratory fatigue tests at constant amplitude.<br>
2. Can a fracture surface exhibit beachmarks without striations? Can it exhibit striations without beachmarks? Explain.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Comparison Table: Beachmarks vs. Striations</strong><br>
<table class="data-table">
<thead>
<tr><th>Diagnostic Feature</th><th>Macroscopic Beachmarks (Clamshell Marks)</th><th>Microscopic Fatigue Striations</th></tr>
</thead>
<tbody>
<tr><td><strong>Scale / Magnification</strong></td><td><strong>Macroscopic</strong>: Clearly visible to the unaided naked eye or under a low-power magnifying glass ($1\times\text{ to }10\times$)</td><td><strong>Microscopic</strong>: Completely invisible to the naked eye; requires a Scanning Electron Microscope (SEM) or TEM ($1,000\times\text{ to }50,000\times$)</td></tr>
<tr><td><strong>Spacing Between Marks</strong></td><td>Millimeters to fractions of a millimeter ($0.1\text{ to }5.0\text{ mm}$)</td><td>Sub-micrometer: fractions of a micron ($0.02\text{ to }2.0\text{ }\mu\text{m}$)</td></tr>
<tr><td><strong>Physical Origin</strong></td><td>Formed by <strong>macro-environmental or load interruptions</strong> (e.g., engine shutdowns, flight duty cycles, changes in mean stress, or corrosion pauses) that allow oxidation/rubbing of the crack tip during halts</td><td>Formed by the <strong>plastic blunting and resharpening</strong> of the crack tip during each individual tensile cycle (Laird-Smith mechanism)</td></tr>
<tr><td><strong>Cycle Correspondence</strong></td><td><strong>NO</strong> $1:1$ correspondence: each beachmark represents thousands or millions of individual flight cycles between major operational pauses</td><td><strong>YES</strong>, approximately $1:1$ correspondence: each individual striation represents the physical advance of the crack front during <strong>one single load cycle</strong> ($da/dN \approx$ striation spacing)</td></tr>
<tr><td><strong>In Continuous Lab Tests</strong></td><td><strong>ABSENT</strong> in uninterrupted constant-amplitude tests; only appears when load is altered or paused</td><td><strong>PRESENT</strong> in almost all ductile metals under cyclic loading regardless of test continuity</td></tr>
</tbody>
</table>
</div>
<div class="solution-step">
<strong>Step 2: Mutual independence of beachmarks and striations</strong><br>
- <em>Beachmarks without striations:</em> <strong>YES</strong>. In brittle or high-strength materials (e.g., cast iron, ultra-high-strength steel $300\text{M}$, or certain titanium alloys), cyclic crack advance may occur by localized micro-cleavage or intergranular cracking without ductile plastic blunting. Clear macroscopic beachmarks can form from service stops, yet high-magnification SEM reveals only cleavage facets with zero striations.<br>
- <em>Striations without beachmarks:</em> <strong>YES</strong>. A specimen tested in a laboratory servo-hydraulic fatigue frame at continuous, constant frequency and constant amplitude runs without interruption until failure. SEM reveals millions of perfect microscopic striations, but the macroscopic fracture surface is completely uniform with zero beachmarks!
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Beachmarks: Macroscopic ($1\times$), millimeter spacing, represent service pauses/stops (no 1:1 cycle relation), point back to origin.<br>
Striations: Microscopic ($5000\times$), sub-micron spacing, represent plastic crack advance per single load cycle ($1:1$ relation).<br>
Beachmarks prove interrupted service; striations prove cyclic mechanical fatigue.
</div>"""
})

# ==========================================
# Problem 32
# ==========================================
add({
    "num": 32,
    "title": r"Paris Law for Fatigue Crack Growth: $\frac{da}{dN} = C (\Delta K)^m$",
    "difficulty": "Medium",
    "category": "Fatigue Crack Propagation",
    "tags": ["Paris Law", "Crack Growth Rate", "Delta K", "Stage II Propagation"],
    "statement": r"""In Stage II fatigue crack propagation, the rate of crack extension per cycle ($da/dN$) is related to the stress intensity factor range $\Delta K$ by the empirical <strong>Paris-Erdogan Law</strong>:
$$\frac{da}{dN} = C (\Delta K)^m$$
where $\Delta K = K_{\text{max}} - K_{\text{min}} = Y \Delta\sigma \sqrt{\pi a}$, $C$ and $m$ are material constants, and $m$ is typically between $2.5$ and $4.0$ for structural metals.
<br><br>
A forged turbine rotor steel has Paris parameters:
$C = 1.80 \times 10^{-11}\text{ m/cycle} \cdot (\text{MPa}\sqrt{\text{m}})^{-m}$ and $m = 3.00$.
The threshold stress intensity factor range for fatigue crack growth is $\Delta K_{\text{th}} = 5.0\text{ MPa}\sqrt{\text{m}}$, and fracture toughness is $K_{Ic} = 75.0\text{ MPa}\sqrt{\text{m}}$.
The rotor is subjected to a cyclic stress range $\Delta\sigma = 220\text{ MPa}$ ($R = 0$, $Y = 1.12$).
<br><br>
1. Calculate the crack growth rate $da/dN$ (in mm/cycle and $\mu\text{m/cycle}$) when the crack length is $a_1 = 3.0\text{ mm}$.<br>
2. Calculate the crack growth rate when the crack has grown to $a_2 = 12.0\text{ mm}$.<br>
3. By what factor did the crack growth rate accelerate between $a = 3\text{ mm}$ and $a = 12\text{ mm}$?<br>
4. Calculate the threshold crack size $a_{\text{th}}$ below which fatigue crack growth cannot occur.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate $da/dN$ for $a_1 = 3.0\text{ mm} = 0.0030\text{ m}$</strong><br>
$$\Delta K_1 = Y \Delta\sigma \sqrt{\pi a_1} = 1.12 \times (220\text{ MPa}) \times \sqrt{\pi \times 0.0030\text{ m}}$$
$$\sqrt{\pi \times 0.0030} = \sqrt{0.0094248} \approx 0.097081\text{ m}^{1/2}$$
$$\Delta K_1 = 1.12 \times 220 \times 0.097081 \approx 23.921\text{ MPa}\sqrt{\text{m}}$$
From Paris Law ($m = 3.00$):
$$\frac{da}{dN} = C (\Delta K_1)^3 = (1.80 \times 10^{-11}) \times (23.921)^3$$
$$(23.921)^3 \approx 13,687.9$$
$$\frac{da}{dN} = (1.80 \times 10^{-11}) \times 13,687.9 \approx 2.464 \times 10^{-7}\text{ m/cycle} = 0.2464\text{ }\mu\text{m/cycle} = 2.46 \times 10^{-4}\text{ mm/cycle}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate $da/dN$ for $a_2 = 12.0\text{ mm} = 0.0120\text{ m}$</strong><br>
Notice that crack length increased by a factor of 4 ($12/3 = 4$).
Since $\Delta K \propto \sqrt{a}$, $\Delta K_2 = \Delta K_1 \sqrt{4} = 2 \Delta K_1$:
$$\Delta K_2 = 2 \times 23.921 = 47.842\text{ MPa}\sqrt{\text{m}}$$
Because $\Delta K_2 < K_{Ic} = 75$, the rotor is still in stable Stage II growth.
$$\frac{da}{dN} = C (\Delta K_2)^3 = C (2 \Delta K_1)^3 = 8 \times \left(\frac{da}{dN}\right)_1$$
$$\left(\frac{da}{dN}\right)_2 = 8 \times (2.464 \times 10^{-7}\text{ m/cycle}) \approx 1.971 \times 10^{-6}\text{ m/cycle} = 1.971\text{ }\mu\text{m/cycle} \approx 1.97 \times 10^{-3}\text{ mm/cycle}$$
</div>
<div class="solution-step">
<strong>Step 3: Acceleration factor</strong><br>
$$\frac{(da/dN)_2}{(da/dN)_1} = \left(\frac{a_2}{a_1}\right)^{m/2} = (4)^{3/2} = (\sqrt{4})^3 = 2^3 = 8.0$$
Quadrupling the crack length accelerates the fatigue crack growth rate by exactly <strong>$8.0\times$</strong> ($800\%$).
</div>
<div class="solution-step">
<strong>Step 4: Threshold crack size $a_{\text{th}}$</strong><br>
Crack growth ceases when $\Delta K \le \Delta K_{\text{th}} = 5.0\text{ MPa}\sqrt{\text{m}}$:
$$\Delta K_{\text{th}} = Y \Delta\sigma \sqrt{\pi a_{\text{th}}} \implies a_{\text{th}} = \frac{1}{\pi}\left(\frac{\Delta K_{\text{th}}}{Y \Delta\sigma}\right)^2$$
$$Y \Delta\sigma = 1.12 \times 220 = 246.4\text{ MPa}$$
$$\frac{\Delta K_{\text{th}}}{Y \Delta\sigma} = \frac{5.0}{246.4} \approx 0.020292\text{ m}^{1/2}$$
$$a_{\text{th}} = \frac{1}{\pi} (0.020292)^2 = \frac{0.00041177}{\pi} \approx 1.31 \times 10^{-4}\text{ m} = 0.131\text{ mm} = 131\text{ }\mu\text{m}$$
Any surface micro-flaw shallower than $131\text{ }\mu\text{m}$ will never propagate under this cyclic stress range!
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
At $a = 3\text{ mm}$: $da/dN = 0.246\text{ }\mu\text{m/cycle}$ ($\Delta K = 23.9\text{ MPa}\sqrt{\text{m}}$)<br>
At $a = 12\text{ mm}$: $da/dN = 1.971\text{ }\mu\text{m/cycle}$ ($\Delta K = 47.8\text{ MPa}\sqrt{\text{m}}$)<br>
Growth rate accelerates by $8.0\times$ due to $(a_2/a_1)^{m/2} = 4^{1.5} = 8$.<br>
Fatigue threshold flaw depth: $a_{\text{th}} = 0.131\text{ mm}$ ($131\text{ }\mu\text{m}$).
</div>"""
})

# ==========================================
# Problem 33
# ==========================================
add({
    "num": 33,
    "title": "Integrating the Paris Law for Fatigue Life Prediction",
    "difficulty": "Hard",
    "category": "Fatigue Crack Propagation",
    "tags": ["Paris Law Integration", "Fatigue Life", "Safe Inspection Interval", "LEFM Life"],
    "statement": r"""A wide plate in a bridge girder subjected to a cyclic stress range $\Delta\sigma = 150\text{ MPa}$ ($R = 0$) contains an edge crack growing from an initial detectable length $a_0 = 2.0\text{ mm}$ ($0.0020\text{ m}$) to a critical length $a_c$.
The steel has fracture toughness $K_{Ic} = 65.0\text{ MPa}\sqrt{\text{m}}$ and Paris law constants $C = 3.0 \times 10^{-11}\text{ m/cycle}\cdot(\text{MPa}\sqrt{\text{m}})^{-3}$ and $m = 3.00$.
Assume $Y = 1.12$ is constant over the growth range.
<br><br>
1. Calculate the critical crack size $a_c$ at which final unstable fracture occurs.<br>
2. Derive the closed-form equation for the total fatigue life $N_f$ by integrating $\frac{da}{dN} = C (Y \Delta\sigma \sqrt{\pi a})^m$ for $m \neq 2$:
$$N_f = \frac{a_0^{1 - m/2} - a_c^{1 - m/2}}{C (Y \Delta\sigma \sqrt{\pi})^m (m/2 - 1)}$$
3. Calculate the number of cycles $N_f$ required for the crack to grow from $a_0 = 2.0\text{ mm}$ to $a_c$.<br>
4. Calculate the cycles required to reach $a = 2 a_0 = 4.0\text{ mm}$. What percentage of total fatigue life is consumed in just the first doubling of crack size?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate critical crack size $a_c$</strong><br>
$$a_c = \frac{1}{\pi}\left(\frac{K_{Ic}}{Y \Delta\sigma}\right)^2$$
$$Y \Delta\sigma = 1.12 \times 150\text{ MPa} = 168.0\text{ MPa}$$
$$\frac{K_{Ic}}{Y \Delta\sigma} = \frac{65.0}{168.0} \approx 0.386905\text{ m}^{1/2}$$
$$a_c = \frac{1}{\pi} (0.386905)^2 = \frac{0.149695}{\pi} \approx 0.047649\text{ m} \approx 47.65\text{ mm}$$
</div>
<div class="solution-step">
<strong>Step 2: Derivation of the integrated Paris equation</strong><br>
$$\frac{da}{dN} = C (Y \Delta\sigma \sqrt{\pi})^m a^{m/2}$$
Separating variables:
$$dN = \frac{da}{C (Y \Delta\sigma \sqrt{\pi})^m a^{m/2}} = \frac{1}{C (Y \Delta\sigma \sqrt{\pi})^m} a^{-m/2} da$$
Integrating from $N = 0$ ($a = a_0$) to $N = N_f$ ($a = a_c$):
$$N_f = \frac{1}{C (Y \Delta\sigma \sqrt{\pi})^m} \left[\frac{a^{1 - m/2}}{1 - m/2}\right]_{a_0}^{a_c} = \frac{a_0^{1 - m/2} - a_c^{1 - m/2}}{C (Y \Delta\sigma \sqrt{\pi})^m (m/2 - 1)}$$
For $m = 3.00$: $m/2 = 1.50$, so $1 - m/2 = -0.50$, and $m/2 - 1 = 0.50$:
$$N_f = \frac{a_0^{-0.5} - a_c^{-0.5}}{0.50\,C (Y \Delta\sigma \sqrt{\pi})^3}$$
</div>
<div class="solution-step">
<strong>Step 3: Numerical calculation of total fatigue life $N_f$</strong><br>
Denominator constants:
$$Y \Delta\sigma \sqrt{\pi} = (168.0\text{ MPa}) \times \sqrt{\pi} \approx 168.0 \times 1.77245 \approx 297.77\text{ MPa}\cdot\text{m}^{1/2}$$
$$(Y \Delta\sigma \sqrt{\pi})^3 = (297.77)^3 \approx 26,402,600$$
$$0.50 \times C \times (Y \Delta\sigma \sqrt{\pi})^3 = 0.50 \times (3.0 \times 10^{-11}) \times 26,402,600 \approx 3.9604 \times 10^{-4}$$
Crack length terms:
$$a_0 = 0.0020\text{ m} \implies a_0^{-0.5} = \frac{1}{\sqrt{0.0020}} \approx 22.3607\text{ m}^{-1/2}$$
$$a_c = 0.04765\text{ m} \implies a_c^{-0.5} = \frac{1}{\sqrt{0.04765}} \approx 4.5810\text{ m}^{-1/2}$$
Numerator:
$$a_0^{-0.5} - a_c^{-0.5} = 22.3607 - 4.5810 = 17.7797\text{ m}^{-1/2}$$
Fatigue life:
$$N_f = \frac{17.7797}{3.9604 \times 10^{-4}} \approx 44,894\text{ cycles}$$
</div>
<div class="solution-step">
<strong>Step 4: Life to reach $a = 4.0\text{ mm}$ and life fraction</strong><br>
$$a_1 = 0.0040\text{ m} \implies a_1^{-0.5} = \frac{1}{\sqrt{0.0040}} \approx 15.8114\text{ m}^{-1/2}$$
$$\Delta(\text{Num}) = 22.3607 - 15.8114 = 6.5493\text{ m}^{-1/2}$$
$$N(2\to 4\text{ mm}) = \frac{6.5493}{3.9604 \times 10^{-4}} \approx 16,537\text{ cycles}$$
Percentage of total life:
$$\% \text{Life} = \frac{16,537}{44,894} \times 100\% \approx 36.83\%$$
Notice that growing just $2.0\text{ mm}$ (from $2\text{ mm}$ to $4\text{ mm}$) consumes nearly $37\%$ of total life, while the remaining $43.65\text{ mm}$ of crack growth sweeps through the remaining $63\%$ of cycles. The majority of fatigue life is spent when the crack is tiny and growing slowly!
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Critical crack size: $a_c = 47.65\text{ mm}$<br>
Total fatigue life: $N_f = 44,894\text{ cycles}$<br>
Cycles to reach $4\text{ mm}$: $N = 16,537\text{ cycles}$ ($36.8\%$ of total life consumed in first $2\text{ mm}$ of growth).
</div>"""
})

# ==========================================
# Problem 34
# ==========================================
add({
    "num": 34,
    "title": "Surface Treatments for Fatigue Enhancement: Shot Peening and Case Hardening",
    "difficulty": "Medium",
    "category": "Surface Engineering",
    "tags": ["Shot Peening", "Nitriding", "Surface Roughness", "Residual Stress"],
    "statement": r"""Because fatigue cracks nucleate almost exclusively at free surfaces, surface engineering can dramatically extend fatigue life.
<br><br>
1. Explain how <strong>shot peening</strong> improves fatigue life:
   (a) What type of residual stress is generated at the surface?<br>
   (b) How does this residual stress alter the effective local mean stress $\sigma_{m,\text{eff}}$ experienced by surface flaws?<br>
2. A heat-treated automotive crankshaft with $\sigma_{\text{UTS}} = 800\text{ MPa}$ and endurance limit $\sigma_e = 400\text{ MPa}$ is subjected to a cyclic surface stress alternating between $0$ and $+500\text{ MPa}$ ($\sigma_a = 250\text{ MPa}, \sigma_m = +250\text{ MPa}$).
   (a) Using Goodman's criterion, show that the unpeened shaft will fail in fatigue.<br>
   (b) If shot peening induces a compressive surface residual stress $\sigma_{\text{res}} = -350\text{ MPa}$, calculate the new effective mean stress $\sigma_{m,\text{eff}}$ and show that the shaft now has infinite fatigue life.<br>
3. Why does severe surface roughness (from coarse turning or EDM machining) or decarburization devastate fatigue performance?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Mechanism of shot peening</strong><br>
(a) High-velocity spherical steel shot impacts the surface, causing localized biaxial plastic stretching of the surface layer. The deeper unyielded elastic core constrains this layer, forcing the surface into a deep layer ($0.2\text{--}0.5\text{ mm}$) of <strong>high compressive residual stress</strong> ($\sigma_{\text{res}} \approx -0.5\text{ to }-0.8\,\sigma_y$).<br>
(b) The static compressive residual stress superimposes directly onto the applied cyclic stress field, shifting the effective local mean stress into compression:
$$\sigma_{m,\text{eff}} = \sigma_{m,\text{applied}} + \sigma_{\text{res}}$$
Compressive residual stress enforces crack closure: microcracks are mechanically squeezed shut during part or all of the cycle, preventing cyclic slip band extrusion and dramatically raising the fatigue limit.
</div>
<div class="solution-step">
<strong>Step 2: Fatigue evaluation of crankshaft</strong><br>
(a) <em>Unpeened shaft:</em> $\sigma_a = 250\text{ MPa}$, $\sigma_m = +250\text{ MPa}$, $\sigma_e = 400\text{ MPa}$, $\sigma_{\text{UTS}} = 800\text{ MPa}$.
Goodman damage ratio:
$$\frac{\sigma_a}{\sigma_e} + \frac{\sigma_m}{\sigma_{\text{UTS}}} = \frac{250}{400} + \frac{250}{800} = 0.625 + 0.3125 = 0.9375$$
With safety factor:
$$N = \frac{1}{0.9375} \approx 1.067$$
If a modest stress concentration of $K_t \ge 1.15$ exists at a fillet, the local stress will exceed Goodman threshold, resulting in <strong>fatigue failure</strong>.
<br>
(b) <em>Shot-peened shaft ($\sigma_{\text{res}} = -350\text{ MPa}$):</em>
$$\sigma_{m,\text{eff}} = +250 + (-350) = -100.0\text{ MPa} \quad (\textbf{compressive mean stress})$$
Under compressive mean stress, Goodman damage does not penalize strength (the mean stress penalty vanishes, $\sigma_a \le \sigma_e$):
$$\sigma_a = 250\text{ MPa} < \sigma_e = 400\text{ MPa}$$
The stress amplitude is only $62.5\%$ of the endurance limit. The shaft operates safely below the endurance limit and achieves <strong>infinite fatigue life</strong>!
</div>
<div class="solution-step">
<strong>Step 3: Surface roughness and decarburization</strong><br>
- <em>Roughness:</em> Machining grooves act as sharp micro-notches with root radius $\rho_t \sim 5\text{--}20\text{ }\mu\text{m}$. By Inglis formula ($K_t \approx 1 + 2\sqrt{R_z/\rho}$), rough surfaces multiply local stress by $2\times$ to $3\times$, nucleating fatigue cracks in early cycles.
- <em>Decarburization:</em> High-temperature exposure without protective atmosphere drains carbon from the surface ($0.1\text{--}0.5\text{ mm}$ layer), turning strong martensite into soft, low-strength ferrite ($\sigma_y$ drops by $70\%$). Fatigue cracks easily nucleate in this soft surface skin, slashing the fatigue limit by up to $60\%$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Shot peening induces deep compressive residual stresses ($\sigma_{\text{res}} < 0$) enforcing crack closure.<br>
Effective mean stress drops from $+250\text{ MPa}$ to $-100\text{ MPa}$, guaranteeing infinite fatigue life.<br>
Surface roughness creates notch concentrations ($K_t$), while decarburization forms a weak ferrite skin that triggers early crack initiation.
</div>"""
})

# ==========================================
# Problem 35
# ==========================================
add({
    "num": 35,
    "title": "Cumulative Fatigue Damage: Palmgren-Miner Linear Damage Rule",
    "difficulty": "Medium",
    "category": "Fatigue Failure",
    "tags": ["Miner's Rule", "Cumulative Damage", "Spectrum Loading", "Fatigue Life"],
    "statement": r"""Real engineering structures (aircraft wings, automotive chassis, railway axles) experience complex variable-amplitude spectrum loading rather than constant stress amplitude.
The <strong>Palmgren-Miner Linear Damage Hypothesis</strong> postulates that each stress cycle consumes a fraction of the total fatigue life:
$$D = \sum_{i=1}^k \frac{n_i}{N_{fi}} = \frac{n_1}{N_{f1}} + \frac{n_2}{N_{f2}} + \dots + \frac{n_k}{N_{fk}} = 1.0$$
where $n_i$ is the number of applied cycles at stress amplitude $\sigma_{ai}$, and $N_{fi}$ is the fatigue life to failure at that stress amplitude.
<br><br>
A forged connecting rod undergoes an operating duty cycle consisting of three distinct stress blocks per hour of engine operation:
- Block 1 (Cruising): $\sigma_{a1} = 280\text{ MPa}$, applied for $n_1 = 8.0 \times 10^4\text{ cycles/hour}$; S-N life is $N_{f1} = 2.0 \times 10^6\text{ cycles}$.
- Block 2 (Acceleration): $\sigma_{a2} = 360\text{ MPa}$, applied for $n_2 = 1.5 \times 10^4\text{ cycles/hour}$; S-N life is $N_{f2} = 1.2 \times 10^5\text{ cycles}$.
- Block 3 (Full Throttle Peak): $\sigma_{a3} = 440\text{ MPa}$, applied for $n_3 = 2.0 \times 10^3\text{ cycles/hour}$; S-N life is $N_{f3} = 1.6 \times 10^4\text{ cycles}$.
<br><br>
1. Calculate the fractional damage $D_i$ contributed by each block per hour of operation.<br>
2. Calculate the total accumulated damage rate per hour $D_{\text{total/hour}}$.<br>
3. Predict the expected operational lifetime of the connecting rod (in operating hours).<br>
4. State two major limitations of Miner's linear damage rule (load sequence effect and cycle interaction).""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate fractional damage $D_i$ per hour</strong><br>
- <em>Block 1 (Cruising):</em>
$$D_1 = \frac{n_1}{N_{f1}} = \frac{8.0 \times 10^4}{2.0 \times 10^6} = \frac{8}{200} = 0.0400 \quad (4.0\%)$$
- <em>Block 2 (Acceleration):</em>
$$D_2 = \frac{n_2}{N_{f2}} = \frac{1.5 \times 10^4}{1.2 \times 10^5} = \frac{15}{120} = 0.1250 \quad (12.5\%)$$
- <em>Block 3 (Full Throttle Peak):</em>
$$D_3 = \frac{n_3}{N_{f3}} = \frac{2.0 \times 10^3}{1.6 \times 10^4} = \frac{2}{16} = 0.1250 \quad (12.5\%)$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate total damage rate per hour</strong><br>
$$D_{\text{total/hour}} = D_1 + D_2 + D_3 = 0.0400 + 0.1250 + 0.1250 = 0.2900\text{ hour}^{-1}$$
Every hour of engine operation consumes $29.0\%$ of the connecting rod's total fatigue endurance!
Notice that although Block 3 accounts for only $2.0 \times 10^3 / (80 + 15 + 2) \times 10^3 \approx 2.06\%$ of all applied cycles, it inflicts $43.1\%$ of the total fatigue damage.
</div>
<div class="solution-step">
<strong>Step 3: Predict operational lifetime in hours</strong><br>
Failure occurs when accumulated damage reaches $D = 1.0$:
$$t_{\text{life}} = \frac{1.0}{D_{\text{total/hour}}} = \frac{1.0}{0.2900} \approx 3.448\text{ operating hours}$$
The connecting rod will fail after approximately $3.45\text{ hours}$ of this severe duty cycle.
</div>
<div class="solution-step">
<strong>Step 4: Limitations of Miner's Rule</strong><br>
1. <strong>Load Sequence Independence:</strong> Miner's rule assumes damage accumulates linearly regardless of the order of loading. In reality, applying a high overload first induces compressive crack-tip residual stresses that retard subsequent crack growth (overload retardation). Conversely, applying low cycles first can accelerate damage without crack closure. Real failures often occur at $D = 0.5\text{ to }2.0$.
2. <strong>Neglect of Sub-Threshold Damage:</strong> In Miner's rule, stress cycles below the initial endurance limit $\sigma_e$ are assumed to inflict zero damage ($N_f = \infty$). However, once higher stress cycles nucleate a microcrack, subsequent low-amplitude cycles that were previously below the endurance limit can now propagate the crack, causing premature failure.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Damage per hour: $D_1 = 0.040$, $D_2 = 0.125$, $D_3 = 0.125 \implies D_{\text{total}} = 0.290\text{ h}^{-1}$<br>
Expected lifetime: $t_{\text{life}} = 3.45\text{ operating hours}$<br>
Limitations: Ignores load sequence/overload retardation effects and ignores propagation by low-amplitude cycles below endurance limit.
</div>"""
})

# ==========================================
# Problem 36
# ==========================================
add({
    "num": 36,
    "title": "Fretting Fatigue and Corrosion Fatigue Phenomena",
    "difficulty": "Medium",
    "category": "Fatigue Failure",
    "tags": ["Fretting Fatigue", "Corrosion Fatigue", "Micro-Slip", "Endurance Limit Destruction"],
    "statement": r"""Two aggressive environmental/mechanical phenomena can drastically reduce or completely destroy the fatigue life of metals: <strong>fretting fatigue</strong> and <strong>corrosion fatigue</strong>.
<br><br>
1. Define <strong>fretting fatigue</strong>:
   (a) What mechanical conditions trigger fretting (contact pressure and micro-slip amplitude)?<br>
   (b) Describe the formation of wear debris ("cocoa" in steel, black powder in aluminum).<br>
   (c) By what percentage can fretting reduce the fatigue endurance limit in bolted joints and turbine blade dovetail roots?<br>
2. Define <strong>corrosion fatigue</strong>:
   (a) Describe the synergistic interaction between cyclic mechanical stress and aqueous electrochemical corrosion.<br>
   (b) How does the S-N curve of a steel tested in saltwater differ from its S-N curve in dry air?<br>
   (c) Why is corrosion fatigue strongly sensitive to cyclic frequency (Hz), whereas mechanical fatigue in air is essentially frequency-independent?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Fretting Fatigue</strong><br>
(a) <em>Conditions:</em> Fretting fatigue occurs at the contact interface between two tightly clamped components (e.g., shrink-fit shafts, press-fit bearings, bolted flange joints, or turbine blade dovetails) subjected to cyclic vibrations. The vibration causes oscillatory tangential <strong>micro-slip</strong> with tiny relative displacements of $5\text{ to }50\text{ }\mu\text{m}$.<br>
(b) <em>Wear debris formation:</em> The micro-slip shears off the protective passive oxide films at microscopic contacting asperity junctions, exposing nascent bare metal. The bare metal cold-welds, tears, and re-oxidizes. The sheared oxidized debris is trapped at the interface, acting as a severe abrasive powder (ferric oxide $\text{Fe}_2\text{O}_3$, appearing as reddish-brown powder known as <strong>"cocoa"</strong> in steels, or fine black alumina powder in aluminum).<br>
(c) <em>Strength reduction:</em> The combined abrasive pitting and severe interfacial shear stresses nucleate microcracks at the edge of the contact patch, reducing the fatigue endurance limit by <strong>$50\%\text{ to }75\%$</strong>!
</div>
<div class="solution-step">
<strong>Step 2: Corrosion Fatigue</strong><br>
(a) <em>Synergistic interaction:</em> Cyclic stress repeatedly ruptures the protective passive oxide film at slip steps on the metal surface. The exposed bare metal anodically dissolves into the electrolyte, forming a sharp microscopic corrosion pit. The pit acts as a severe geometric stress concentrator that nucleates a fatigue crack. The cyclic stress then pumps fresh corrosive fluid in and out of the crack tip, preventing repassivation and accelerating crack growth.<br>
(b) <em>Destruction of the endurance limit:</em> In dry air, steel exhibits a distinct horizontal endurance limit ($\sigma_e$). In a corrosive environment (saltwater, acid rain), <strong>the fatigue endurance limit completely disappears</strong>! The S-N curve continues to plunge downward with increasing cycles; given enough time, the component will fail at any stress amplitude, no matter how small.<br>
(c) <em>Frequency dependence:</em> Mechanical fatigue depends primarily on the number of cycles ($N$), not wall-clock time. In contrast, electrochemical corrosion is a time-dependent chemical reaction. At low testing frequencies (e.g., $0.1\text{ Hz}$ wave action in offshore structures), there is extensive time per cycle for dissolution and hydrogen ingress, causing far greater crack advance per cycle than at high frequencies ($100\text{ Hz}$).
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Fretting occurs under $5\text{--}50\text{ }\mu\text{m}$ micro-slip, producing abrasive "cocoa" debris and slashing endurance limit by $50\text{--}75\%$.<br>
Corrosion fatigue synergistically couples film rupture and anodic dissolution, completely destroying the fatigue endurance limit.<br>
Corrosion fatigue is strongly frequency-dependent because chemical dissolution requires real wall-clock time per cycle.
</div>"""
})

# ==========================================
# Problem 37
# ==========================================
add({
    "num": 37,
    "title": "High-Temperature Creep: The Three Stages of the Creep Curve",
    "difficulty": "Easy",
    "category": "High-Temperature Creep",
    "tags": ["Creep Stages", "Primary Creep", "Secondary Steady-State", "Tertiary Creep"],
    "statement": r"""Creep is the time-dependent, permanent inelastic deformation of materials subjected to sustained mechanical loads at elevated homologous temperatures:
$$T \ge (0.35\text{ to }0.40)\,T_m \quad (\text{in Kelvin})$$
A standard tensile creep test holds a specimen under constant tensile load (or constant stress $\sigma$) at constant elevated temperature $T$, recording strain $\varepsilon$ versus time $t$.
<br><br>
1. Detail the physical characteristics and dominant microstructural processes occurring during each of the four features of a classic creep curve:
   (a) Instantaneous strain ($\varepsilon_0$).<br>
   (b) <strong>Primary (Transient) Creep</strong>: why does the creep rate $d\varepsilon/dt$ decrease with time?<br>
   (c) <strong>Secondary (Steady-State) Creep</strong>: why is the creep rate $\dot{\varepsilon}_s$ constant, and why is this the most critical engineering design parameter?<br>
   (d) <strong>Tertiary Creep</strong>: why does the creep rate accelerate rapidly toward rupture ($t_r$)?<br>
2. Why is lead ($T_m = 327^\circ\text{C} = 600\text{ K}$) susceptible to severe creep deformation at room temperature ($20^\circ\text{C} = 293\text{ K}$), whereas tungsten ($T_m = 3422^\circ\text{C} = 3695\text{ K}$) does not creep until $T > 1200^\circ\text{C}$?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The Four Features of the Creep Curve</strong><br>
(a) <strong>Instantaneous Strain ($\varepsilon_0$):</strong> The immediate elastic ($\sigma/E$) and possible instantaneous plastic strain upon applying the initial load at time $t = 0$.<br>
(b) <strong>Primary (Transient) Creep:</strong> The creep rate continuously <strong>decreases with time</strong> ($d^2\varepsilon/dt^2 < 0$).
<em>Microstructural cause:</em> Gliding dislocations multiply and intersect, forming dense tangles and subgrain cell walls. Strain hardening (work hardening) outpaces thermal recovery, progressively increasing the internal resistance to dislocation glide.<br>
(c) <strong>Secondary (Steady-State) Creep:</strong> The creep rate reaches a constant minimum value:
$$\dot{\varepsilon}_s = \frac{d\varepsilon}{dt} = \text{constant}$$
<em>Microstructural cause:</em> A dynamic dynamic equilibrium (balance) is established between <strong>work hardening</strong> (dislocation multiplication) and <strong>thermal recovery</strong> (dislocation annihilation and climb over obstacles).
<em>Engineering significance:</em> Because secondary creep spans the vast majority ($>80\%$) of the component's service lifetime, the steady-state creep rate $\dot{\varepsilon}_s$ is the primary parameter used in design codes to predict dimensional tolerances and service life.<br>
(d) <strong>Tertiary Creep:</strong> The creep rate accelerates rapidly ($d^2\varepsilon/dt^2 > 0$), culminating in rupture.
<em>Microstructural cause:</em>
1. Microscopic grain boundary cavitation: vacancy condensation nucleates thousands of microscopic cavities along transverse grain boundaries.
2. Cross-sectional necking under constant load increases the true stress ($\sigma = P/A$), accelerating power-law deformation.
3. Microcracks coalesce, leading to intergranular creep rupture at time $t_r$.
</div>
<div class="solution-step">
<strong>Step 2: Homologous temperature comparison</strong><br>
Creep is governed by thermally activated vacancy self-diffusion, which becomes significant only when homologous temperature $T/T_m \ge 0.40$:
- <em>Lead at $20^\circ\text{C}$ ($293\text{ K}$):</em>
$$\frac{T}{T_m} = \frac{293\text{ K}}{600\text{ K}} \approx 0.49 \gg 0.40$$
Room temperature is half of lead's absolute melting point! Lead pipes and roof flashings creep and sag under their own weight at room temperature.
- <em>Tungsten at $20^\circ\text{C}$ ($293\text{ K}$):</em>
$$\frac{T}{T_m} = \frac{293\text{ K}}{3695\text{ K}} \approx 0.079 \ll 0.40$$
For tungsten to reach $T/T_m = 0.40$, temperature must reach $T = 0.40 \times 3695\text{ K} \approx 1478\text{ K} \approx 1205^\circ\text{C}$.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Primary: Creep rate decreases as work hardening dominates.<br>
Secondary: Steady-state rate $\dot{\varepsilon}_s$ governed by perfect dynamic balance between work hardening and thermal recovery (climb).<br>
Tertiary: Creep rate accelerates due to grain boundary cavitation, necking, and microcrack linkage.<br>
Lead creeps at room temperature because $20^\circ\text{C}$ is $0.49 T_m$; tungsten requires $> 1200^\circ\text{C}$ to reach $0.40 T_m$.
</div>"""
})

# ==========================================
# Problem 38
# ==========================================
add({
    "num": 38,
    "title": "Steady-State Creep Power Law: Stress Exponent and Activation Energy",
    "difficulty": "Hard",
    "category": "High-Temperature Creep",
    "tags": ["Norton-Bailey Law", "Power-Law Creep", "Stress Exponent n", "Activation Energy Qc"],
    "statement": r"""The steady-state secondary creep rate $\dot{\varepsilon}_s$ is described by the Norton-Bailey power law:
$$\dot{\varepsilon}_s = A \sigma^n \exp\left(-\frac{Q_c}{R T}\right)$$
where $A$ is a materials constant, $\sigma$ is applied stress, $n$ is the creep stress exponent, $Q_c$ is the activation energy for creep, and $R = 8.314\text{ J}/(\text{mol}\cdot\text{K})$.
<br><br>
In high-temperature creep tests conducted on a stainless steel:
- Test 1: At $T_1 = 650^\circ\text{C}$ ($923\text{ K}$) and $\sigma_1 = 120\text{ MPa}$, $\dot{\varepsilon}_{s1} = 2.50 \times 10^{-8}\text{ s}^{-1}$.
- Test 2: At $T_2 = 650^\circ\text{C}$ ($923\text{ K}$) and $\sigma_2 = 180\text{ MPa}$, $\dot{\varepsilon}_{s2} = 1.90 \times 10^{-7}\text{ s}^{-1}$.
- Test 3: At $T_3 = 700^\circ\text{C}$ ($973\text{ K}$) and $\sigma_3 = 120\text{ MPa}$, $\dot{\varepsilon}_{s3} = 1.35 \times 10^{-7}\text{ s}^{-1}$.
<br><br>
1. Using Tests 1 and 2 (constant temperature), calculate the stress exponent $n = \frac{\ln(\dot{\varepsilon}_{s2} / \dot{\varepsilon}_{s1})}{\ln(\sigma_2 / \sigma_1)}$.<br>
2. What does the magnitude of $n$ indicate regarding the dominant creep mechanism (diffusion creep vs. dislocation power-law creep)?<br>
3. Using Tests 1 and 3 (constant stress), calculate the activation energy for creep $Q_c$ (in $\text{kJ/mol}$).<br>
4. Compare $Q_c$ with the activation energy for self-diffusion in $\gamma$-iron ($Q_{\text{diff}} \approx 280\text{ kJ/mol}$) and explain the physical link.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate stress exponent $n$ (from Tests 1 & 2 at $650^\circ\text{C}$)</strong><br>
$$\frac{\dot{\varepsilon}_{s2}}{\dot{\varepsilon}_{s1}} = \left(\frac{\sigma_2}{\sigma_1}\right)^n$$
Taking natural logarithms:
$$n = \frac{\ln(\dot{\varepsilon}_{s2} / \dot{\varepsilon}_{s1})}{\ln(\sigma_2 / \sigma_1)} = \frac{\ln(1.90 \times 10^{-7} / 2.50 \times 10^{-8})}{\ln(180 / 120)} = \frac{\ln(7.60)}{\ln(1.50)}$$
$$\ln(7.60) \approx 2.02815, \quad \ln(1.50) \approx 0.405465$$
$$n = \frac{2.02815}{0.405465} \approx 5.002 \approx 5.00$$
</div>
<div class="solution-step">
<strong>Step 2: Dominant creep mechanism from $n = 5$</strong><br>
- Diffusional creep (Nabarro-Herring and Coble) is strictly Newtonian viscous flow with $n = 1.0$.
- A stress exponent of $n = 4\text{ to }7$ is the definitive hallmark of <strong>Dislocation Power-Law Creep (Weertman dislocation climb-assisted glide)</strong>.
In this regime, dislocations glide along slip planes until they are blocked by forest obstacles or subgrain boundaries. To continue deforming, edge dislocations must climb over obstacles by absorbing or emitting vacancies, making dislocation climb the rate-limiting step.
</div>
<div class="solution-step">
<strong>Step 3: Calculate activation energy $Q_c$ (from Tests 1 & 3 at $\sigma = 120\text{ MPa}$)</strong><br>
$$\frac{\dot{\varepsilon}_{s3}}{\dot{\varepsilon}_{s1}} = \exp\left[-\frac{Q_c}{R}\left(\frac{1}{T_3} - \frac{1}{T_1}\right)\right]$$
Taking natural logarithms:
$$\ln\left(\frac{\dot{\varepsilon}_{s3}}{\dot{\varepsilon}_{s1}}\right) = -\frac{Q_c}{R} \left(\frac{1}{T_3} - \frac{1}{T_1}\right) = \frac{Q_c}{R} \left(\frac{1}{T_1} - \frac{1}{T_3}\right)$$
Given $T_1 = 923\text{ K}$, $T_3 = 973\text{ K}$:
$$\frac{1}{T_1} - \frac{1}{T_3} = \frac{1}{923} - \frac{1}{973} = 0.00108342 - 0.00102775 \approx 5.567 \times 10^{-5}\text{ K}^{-1}$$
$$\frac{\dot{\varepsilon}_{s3}}{\dot{\varepsilon}_{s1}} = \frac{1.35 \times 10^{-7}}{2.50 \times 10^{-8}} = 5.40 \implies \ln(5.40) \approx 1.6864$$
$$Q_c = \frac{R \ln(\dot{\varepsilon}_{s3} / \dot{\varepsilon}_{s1})}{(1/T_1 - 1/T_3)} = \frac{8.314 \times 1.6864}{5.567 \times 10^{-5}} = \frac{14.0207}{5.567 \times 10^{-5}} \approx 251,854\text{ J/mol} \approx 251.9\text{ kJ/mol}$$
</div>
<div class="solution-step">
<strong>Step 4: Comparison with self-diffusion activation energy</strong><br>
$$\frac{Q_c}{Q_{\text{diff}}} = \frac{251.9\text{ kJ/mol}}{280.0\text{ kJ/mol}} \approx 0.90 \approx 1.0$$
The activation energy for steady-state creep ($Q_c \approx 252\text{ kJ/mol}$) closely matches the activation energy for lattice self-diffusion ($Q_{\text{diff}} \approx 280\text{ kJ/mol}$).
<em>Physical conclusion:</em> This proves experimentally that power-law creep is rate-controlled by the diffusion of vacancies through the crystal lattice to allow edge dislocations to climb out of their glide planes over obstacles.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Stress exponent: $n = 5.00$ (identifies Dislocation Climb Power-Law Creep).<br>
Activation energy for creep: $Q_c \approx 252\text{ kJ/mol}$.<br>
$Q_c \approx Q_{\text{diff}}$ confirms that dislocation climb rate-controlled by vacancy self-diffusion governs steady-state high-temperature creep.
</div>"""
})

# ==========================================
# Problem 39
# ==========================================
add({
    "num": 39,
    "title": "Diffusional Creep: Nabarro-Herring vs. Coble Creep",
    "difficulty": "Hard",
    "category": "High-Temperature Creep",
    "tags": ["Nabarro-Herring", "Coble Creep", "Grain Size Effect", "Diffusional Flow"],
    "statement": r"""At low stresses and high homologous temperatures, deformation occurs by stress-directed vacancy diffusion without dislocation glide (diffusional flow, $n = 1.0$).
Two distinct diffusional creep mechanisms exist:
1. <strong>Nabarro-Herring Creep</strong> (bulk lattice diffusion of vacancies through grain interiors):
$$\dot{\varepsilon}_{\text{NH}} = \frac{A_{\text{NH}} D_L \sigma \Omega}{k_B T d^2}$$
2. <strong>Coble Creep</strong> (vacancy diffusion channeled along grain boundary networks):
$$\dot{\varepsilon}_{\text{Coble}} = \frac{A_{\text{Coble}} \delta D_{\text{gb}} \sigma \Omega}{k_B T d^3}$$
where $d$ is the grain diameter, $D_L$ is lattice diffusivity, $\delta$ is grain boundary width, $D_{\text{gb}}$ is grain boundary diffusivity, and $\Omega$ is atomic volume.
<br><br>
1. Contrast the grain size sensitivity of Nabarro-Herring creep ($\dot{\varepsilon} \propto d^{-2}$) and Coble creep ($\dot{\varepsilon} \propto d^{-3}$).<br>
2. A ceramic turbine nozzle vane creeps by Coble creep at $1100^\circ\text{C}$ with grain size $d_1 = 5.0\text{ }\mu\text{m}$. If hot isostatic pressing coarsens the grain size to $d_2 = 50.0\text{ }\mu\text{m}$ ($10\times$ larger), calculate the ratio $\dot{\varepsilon}_2 / \dot{\varepsilon}_1$.<br>
3. At what temperature regime does Coble creep dominate over Nabarro-Herring creep, and why?<br>
4. Explain why coarse grains or single crystals are strictly required for high-temperature creep resistance, directly opposite to room-temperature Hall-Petch requirements.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Grain size sensitivity comparison</strong><br>
- <em>Nabarro-Herring Creep:</em> Vacancies diffuse across the full grain diameter $d$ through the lattice; the diffusion distance is $L \propto d$, and the gradient is $\Delta C / d \propto 1/d$. The strain rate scales inversely with the <strong>square of grain diameter</strong>:
$$\dot{\varepsilon}_{\text{NH}} \propto \frac{1}{d^2}$$
- <em>Coble Creep:</em> Vacancies diffuse along the 2D network of grain boundaries. In addition to the diffusion distance scaling with $d$, the volume fraction of grain boundary channels also scales inversely with grain diameter ($f_{\text{GB}} \propto \delta / d$). Combining both effects yields an extraordinary cubic inverse dependence:
$$\dot{\varepsilon}_{\text{Coble}} \propto \frac{1}{d^3}$$
</div>
<div class="solution-step">
<strong>Step 2: Grain coarsening calculation for Coble creep</strong><br>
Given: $d_1 = 5.0\text{ }\mu\text{m}$, $d_2 = 50.0\text{ }\mu\text{m}$:
$$\frac{d_2}{d_1} = \frac{50.0}{5.0} = 10$$
Since $\dot{\varepsilon} \propto d^{-3}$:
$$\frac{\dot{\varepsilon}_2}{\dot{\varepsilon}_1} = \left(\frac{d_1}{d_2}\right)^3 = \left(\frac{1}{10}\right)^3 = \frac{1}{1000} = 0.001$$
Increasing the grain size by a factor of 10 reduces the Coble creep rate by a factor of <strong>1,000</strong> ($99.9\%$ reduction)!
</div>
<div class="solution-step">
<strong>Step 3: Temperature regime of Coble vs. Nabarro-Herring</strong><br>
Grain boundary diffusion has a much lower activation energy than bulk lattice diffusion ($Q_{\text{gb}} \approx 0.5\text{ to }0.6\,Q_L$) because the disordered boundary has excess free volume and broken bonds.
- At <strong>moderate homologous temperatures ($0.4\text{ to }0.65 T_m$)</strong>, lattice diffusion is "frozen," but boundary diffusion is active ($D_{\text{gb}} \gg D_L$). Hence, <strong>Coble creep dominates completely</strong>.
- At <strong>very high temperatures ($T > 0.75\text{--}0.80 T_m$)</strong>, bulk lattice diffusion accelerates exponentially and overwhelms the narrow boundary channels, so <strong>Nabarro-Herring creep dominates</strong>.
</div>
<div class="solution-step">
<strong>Step 4: The High-Temperature vs. Room-Temperature Inversion</strong><br>
- <em>At Room Temperature (Hall-Petch):</em> Plastic deformation occurs by dislocation glide. Grain boundaries act as impenetrable barriers to dislocations. Therefore, <strong>fine grains make metals stronger</strong> ($\sigma_y \propto d^{-1/2}$).
- <em>At High Creep Temperatures:</em> Plastic deformation is mediated by vacancy diffusion and grain boundary sliding. Grain boundaries act as rapid diffusion short-circuits and sources/sinks for vacancies. Therefore, <strong>grain boundaries weaken metals at high temperatures</strong> ($\dot{\varepsilon} \propto d^{-3}$). To maximize creep resistance, engineers eliminate grain boundaries entirely by casting <strong>single-crystal turbine blades</strong>.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Nabarro-Herring scales as $d^{-2}$; Coble scales as $d^{-3}$.<br>
Increasing grain size by $10\times$ slashes Coble creep rate by $1,000\times$ ($0.1\%$).<br>
Coble dominates at lower temperatures ($0.4\text{--}0.65 T_m$) because $Q_{\text{gb}} \approx 0.5 Q_L$.<br>
Fine grains strengthen at room temperature (Hall-Petch) but destroy creep resistance at high temperatures, necessitating single-crystal alloys.
</div>"""
})

# ==========================================
# Problem 40
# ==========================================
add({
    "num": 40,
    "title": "Larson-Miller Parameter (LMP) and Creep Rupture Life Extrapolation",
    "difficulty": "Medium",
    "category": "High-Temperature Creep",
    "tags": ["Larson-Miller Parameter", "LMP", "Creep Rupture", "Turbine Blades"],
    "statement": r"""The <strong>Larson-Miller Parameter ($P_{\text{LM}}$ or LMP)</strong> is the industry standard method used to correlate stress, operating temperature, and rupture lifetime on a single master curve:
$$P_{\text{LM}} = T \left[ C + \log_{10}(t_r) \right] \times 10^{-3}$$
where $T$ is absolute temperature in Kelvin, $t_r$ is rupture lifetime in hours, and $C \approx 20$ for nickel-base superalloys and steels.
<br><br>
A Larson-Miller master curve for Inconel 718 superalloy relates LMP to applied tensile stress:
- At $\sigma = 350\text{ MPa}$, the master curve yields $P_{\text{LM}} = 24.50$.
- At $\sigma = 200\text{ MPa}$, the master curve yields $P_{\text{LM}} = 26.20$.
<br>
1. A gas turbine blade operates under a centrifugal stress $\sigma = 350\text{ MPa}$ at a turbine inlet temperature $T_1 = 650^\circ\text{C}$ ($923\text{ K}$). Calculate the expected creep rupture lifetime $t_{r1}$ (in hours and years).<br>
2. Due to a combustion control malfunction, the operating temperature increases by just $50^\circ\text{C}$ to $T_2 = 700^\circ\text{C}$ ($973\text{ K}$) at the same stress ($350\text{ MPa}$). Calculate the new rupture lifetime $t_{r2}$.<br>
3. By what factor did creep lifetime collapse as a consequence of this $50^\circ\text{C}$ temperature surge? What does this demonstrate to gas turbine operators?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Rupture life at $650^\circ\text{C}$ ($923\text{ K}$)</strong><br>
From $P_{\text{LM}} = T [20 + \log_{10}(t_r)] \times 10^{-3} = 24.50$:
$$20 + \log_{10}(t_{r1}) = \frac{24.50 \times 10^3}{T_1} = \frac{24,500}{923\text{ K}} \approx 26.5439$$
$$\log_{10}(t_{r1}) = 26.5439 - 20 = 6.5439$$
$$t_{r1} = 10^{6.5439} \approx 3,498,600\text{ hours} \approx 3.50 \times 10^6\text{ hours}$$
In years:
$$t_{r1} = \frac{3,498,600}{24 \times 365} = \frac{3,498,600}{8,760} \approx 399.4\text{ years}$$
The blade design is exceptionally safe at $650^\circ\text{C}$.
</div>
<div class="solution-step">
<strong>Step 2: Rupture life at $700^\circ\text{C}$ ($973\text{ K}$)</strong><br>
At $T_2 = 973\text{ K}$:
$$20 + \log_{10}(t_{r2}) = \frac{24,500}{973\text{ K}} \approx 25.17985$$
$$\log_{10}(t_{r2}) = 25.17985 - 20 = 5.17985$$
$$t_{r2} = 10^{5.17985} \approx 151,300\text{ hours}$$
In years:
$$t_{r2} = \frac{151,300}{8,760} \approx 17.27\text{ years}$$
</div>
<div class="solution-step">
<strong>Step 3: Life collapse factor and operational takeaway</strong><br>
$$\text{Collapse Factor} = \frac{t_{r1}}{t_{r2}} = \frac{3,498,600\text{ h}}{151,300\text{ h}} \approx 23.12$$
A modest $50^\circ\text{C}$ temperature increase ($+5.4\%$ on the Kelvin scale) causes the creep rupture lifetime to <strong>collapse by a factor of 23</strong>!
<em>Takeaway for operators:</em> Creep damage is an exponential function of temperature ($\propto \exp(-Q/RT)$). In jet engines and power turbines, operating even $15\text{--}20^\circ\text{C}$ above rated firing temperature cuts blade inspection intervals from years to months, risking catastrophic mid-air turbine blade separation.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
At $650^\circ\text{C}$: $t_{r1} \approx 3.50 \times 10^6\text{ hours}$ ($>399\text{ years}$).<br>
At $700^\circ\text{C}$: $t_{r2} \approx 151,300\text{ hours}$ ($17.3\text{ years}$).<br>
Rupture life collapses by $23.1\times$ due to a $50^\circ\text{C}$ temperature surge, illustrating the severe exponential temperature sensitivity of creep.
</div>"""
})

if __name__ == "__main__":
    print(f"Ch 8 Part 2: P26-P40 added. Current total: {len(P)}")

# ==========================================
# Problem 41
# ==========================================
add({
    "num": 41,
    "title": "Deformation Mechanism Maps (Ashby Maps)",
    "difficulty": "Medium",
    "category": "High-Temperature Creep",
    "tags": ["Deformation Mechanism Map", "Ashby Map", "Normalized Stress", "Homologous Temperature"],
    "statement": r"""A <strong>Deformation Mechanism Map (Ashby Map)</strong> is a 2D diagram that plots normalized shear stress ($\tau / G$ or $\sigma / E$) on the vertical axis against homologous temperature ($T / T_m$) on the horizontal axis, mapping out the fields where different deformation mechanisms dominate.
<br><br>
1. Identify the 5 primary deformation fields displayed on an Ashby deformation mechanism map:
   (a) Theoretical shear strength field (at the very top).<br>
   (b) Dislocation glide / Plastic yielding field (low $T$, high stress).<br>
   (c) Dislocation power-law creep field (intermediate-to-high $T$, moderate stress).<br>
   (d) Diffusional flow field (high $T$, low stress, subdivided into Coble and Nabarro-Herring).<br>
   (e) Elastic deformation field (low stress, low $T$).<br>
2. Draw or describe the boundary between Coble creep and Nabarro-Herring creep as a function of temperature and grain size.<br>
3. How do engineers use deformation mechanism maps to select alloy compositions or design changes (e.g., increasing grain size vs adding precipitate dispersoids) to suppress specific failure modes?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The 5 Primary Deformation Fields</strong><br>
(a) <strong>Theoretical Shear Strength ($\tau / G \approx 0.05\text{--}0.10$):</strong> The upper bound where stress is so immense that atomic planes slide over one another simultaneously without dislocations.<br>
(b) <strong>Dislocation Glide / Low-Temperature Plasticity:</strong> Dominates at $T < 0.35 T_m$ and high stress ($\tau > \tau_y$). Dislocation motion is governed by short-range obstacle cutting and Peierls lattice friction.<br>
(c) <strong>Power-Law Dislocation Creep:</strong> Dominates at $0.4 T_m \le T \le 0.8 T_m$ and moderate stresses ($10^{-4} \le \tau/G \le 10^{-2}$). Dislocation glide is rate-limited by vacancy diffusion-assisted dislocation climb over obstacles ($n = 4\text{ to }7$).<br>
(d) <strong>Diffusional Flow:</strong> Dominates at low stresses ($\tau/G < 10^{-4}$) and elevated temperatures ($T > 0.4 T_m$). Stress-directed vacancy migration flows between grain boundaries without dislocation motion ($n = 1$):
- <em>Coble Creep:</em> Dominates at lower temperatures ($0.4\text{--}0.65 T_m$) where grain boundary diffusion ($D_{\text{gb}}$) is much faster than lattice diffusion.
- <em>Nabarro-Herring Creep:</em> Dominates at very high temperatures ($T > 0.75 T_m$) where bulk lattice diffusion ($D_L$) activates.<br>
(e) <strong>Elastic Field:</strong> Low stresses below yield and low temperatures where only reversible elastic Hookean deformation occurs.
</div>
<div class="solution-step">
<strong>Step 2: Coble vs. Nabarro-Herring boundary</strong><br>
The boundary where both diffusional mechanisms contribute equally is found by setting $\dot{\varepsilon}_{\text{Coble}} = \dot{\varepsilon}_{\text{NH}}$:
$$\frac{A_{\text{Coble}} \delta D_{\text{gb}}}{d^3} = \frac{A_{\text{NH}} D_L}{d^2} \implies d_{\text{boundary}} \approx C \delta \frac{D_{\text{gb}}}{D_L}$$
Because $D_{\text{gb}} / D_L \propto \exp\left(\frac{Q_L - Q_{\text{gb}}}{RT}\right)$, as temperature increases, the ratio $D_{\text{gb}} / D_L$ shrinks rapidly.
Therefore:
- In fine-grained materials, Coble creep expands across a wide temperature range.
- In coarse-grained materials, Coble creep shrinks to a tiny sliver, and Nabarro-Herring creep dominates.
</div>
<div class="solution-step">
<strong>Step 3: Engineering design using Ashby maps</strong><br>
By pinpointing the component's exact operating conditions $(\sigma/E, T/T_m)$ on the map, the engineer identifies the active microscopic mechanism:
1. If operating in the <strong>Coble or Nabarro-Herring diffusional field</strong>, increasing grain size ($d \uparrow$) or eliminating grain boundaries entirely (single crystal) will dramatically lower creep rate ($\dot{\varepsilon} \propto d^{-3}$ or $d^{-2}$).
2. If operating in the <strong>Dislocation Power-Law field</strong>, changing grain size has virtually zero effect! Instead, the engineer must introduce fine insoluble precipitate particles (e.g., $\gamma'$ in superalloys) to block dislocation climb and looping.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Fields: Theoretical strength $\to$ Dislocation glide $\to$ Power-law climb creep $\to$ Diffusional flow (Coble/N-H) $\to$ Elastic.<br>
Coble dominates at intermediate $T$ and fine grain sizes; Nabarro-Herring dominates near melting.<br>
Ashby maps guide targeted metallurgical countermeasures: increase grain size against diffusional creep; add coherent precipitates against power-law climb creep.
</div>"""
})

# ==========================================
# Problem 42
# ==========================================
add({
    "num": 42,
    "title": "Single-Crystal Superalloys and Directional Solidification for Turbine Blades",
    "difficulty": "Hard",
    "category": "Advanced Materials",
    "tags": ["Single-Crystal Superalloys", "Directional Solidification", "Turbine Blades", "Creep Design"],
    "statement": r"""High-pressure gas turbine blades in advanced commercial jet engines (e.g., CFM LEAP, GE90, Trent 1000) operate at gas temperatures exceeding $1500^\circ\text{C}$—several hundred degrees above the melting point of nickel!
The evolution of casting technology transformed blade microstructures across three generations:
$$\text{Conventional Equiaxed Polycrystal} \longrightarrow \text{Directionally Solidified (DS) Columnar} \longrightarrow \text{Single-Crystal (SX)}$$
<br>
1. Why are <strong>transverse grain boundaries</strong> (boundaries oriented perpendicular to the centrifugal stress axis) the fatal weak link in high-temperature creep?<br>
2. Describe the investment casting process used to produce <strong>Directionally Solidified (DS)</strong> columnar-grained blades, and explain why DS blades offer superior thermal fatigue and creep resistance.<br>
3. How does a <strong>helical pigtail grain selector</strong> in Bridgman casting isolate a single crystal to grow a complete single-crystal blade (e.g., CMSX-4)?<br>
4. Why can single-crystal superalloys completely eliminate grain boundary strengthening elements (such as carbon, boron, zirconium, and hafnium)? How does their absence dramatically increase the melting/solution heat-treatment temperature?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: The fatal vulnerability of transverse grain boundaries</strong><br>
Under axial centrifugal tensile stress in rotating turbine blades:
1. Transverse grain boundaries (perpendicular to the radial centrifugal load) experience maximum normal tensile stress ($\sigma_n$). This drives rapid vacancy condensation, nucleating grain boundary micro-cavities that link into wedge cracks at triple junctions.
2. Boundaries inclined at $45^\circ$ undergo rapid <strong>grain boundary sliding</strong>, shearing grains past one another.
3. Transverse boundaries act as fast diffusion pathways for oxygen and hot corrosive combustion gases (hot corrosion / oxidation attack).
</div>
<div class="solution-step">
<strong>Step 2: Directionally Solidified (DS) columnar blades</strong><br>
In Directional Solidification (DS), molten superalloy is poured into a ceramic investment shell mold resting on a water-cooled copper chill plate inside a vacuum furnace.
- The mold is slowly withdrawn downward out of the heating zone.
- Unidirectional heat extraction through the chill plate forces columnar grains to grow strictly parallel to the thermal gradient (and parallel to the blade axis).
- <strong>All transverse grain boundaries are completely eliminated!</strong> The only remaining boundaries run longitudinally along the centrifugal stress axis ($\sigma_n = 0$), eliminating grain boundary cavitation and sliding. Furthermore, the longitudinal direction naturally aligns with the low-stiffness $\langle 001\rangle$ crystallographic direction, slashing thermal fatigue stresses by $40\%$.
</div>
<div class="solution-step">
<strong>Step 3: Helical grain selector for Single-Crystal (SX) casting</strong><br>
Above the water-cooled chill plate, a narrow, spiral ceramic constriction known as a <strong>helical pigtail grain selector</strong> is placed between the starter block and the blade cavity:
1. As columnar grains grow upward from the chill plate, they enter the spiral channel.
2. The twisting geometry forces grains to compete: the fastest-growing orientation ($\langle 001\rangle$ dendrites) chokes off competing grains around the spiral bends.
3. By the top of the helix, only <strong>one single, perfectly oriented crystal</strong> emerges, which then fills the entire turbine blade mold without a single grain boundary!
</div>
<div class="solution-step">
<strong>Step 4: Elimination of boundary strengthening elements and melting benefit</strong><br>
In conventional polycrystals, elements like Carbon (forming carbides), Boron, and Zirconium are mandatory to strengthen and pin grain boundaries.
However, these elements form low-melting eutectic phases that severely depress the incipient melting temperature of the alloy ($T_{\text{melt}}$ drops by $50\text{--}80^\circ\text{C}$).
Because Single-Crystal blades have <strong>zero grain boundaries</strong>, grain boundary strengtheners ($\text{C, B, Zr}$) are completely eliminated!
This raises the incipient melting temperature by $>50^\circ\text{C}$, allowing solution heat treatment at up to $1315^\circ\text{C}$. This permits complete dissolution and re-precipitation of a massive $70\%$ volume fraction of ultra-fine coherent $\gamma'$ cubes ($\text{Ni}_3(\text{Al,Ti,Ta})$), enabling sustained operation at unprecedented temperatures.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Transverse boundaries fail by vacancy cavitation, grain boundary sliding, and oxygen attack.<br>
DS eliminates transverse boundaries, creating longitudinal columnar grains with compliant $\langle 001\rangle$ orientation.<br>
Helical grain selector chokes out competing grains to grow a monolithic Single Crystal (SX).<br>
Eliminating C, B, and Zr raises incipient melting by $>50^\circ\text{C}$, enabling $70\%$ coherent $\gamma'$ precipitate loading.
</div>"""
})

# ==========================================
# Problem 43
# ==========================================
add({
    "num": 43,
    "title": "Thermal Fatigue and Constrained Thermal Strains in Power Plant Components",
    "difficulty": "Medium",
    "category": "Fatigue & Creep Interaction",
    "tags": ["Thermal Fatigue", "Thermal Cycling", "Constrained Strain", "Power Plant Piping"],
    "statement": r"""In fossil and nuclear steam power plants, heavy-walled steam pipes and thick turbine casings experience cyclic heating and cooling during start-up, load changes, and shutdowns.
If a component of thermal expansion coefficient $\alpha_L$ undergoes temperature cycling between $T_{\text{min}}$ and $T_{\text{max}}$ ($\Delta T = T_{\text{max}} - T_{\text{min}}$) while fully constrained against thermal expansion in one dimension:
$$\Delta\varepsilon_{\text{thermal}} = \alpha_L \Delta T$$
The mechanical strain imposed on the material is $\Delta\varepsilon = -\alpha_L \Delta T$.
<br><br>
A thick-walled steam pipe is fabricated from a heat-resistant Cr-Mo alloy steel:
$E = 190\text{ GPa}$, $\nu = 0.30$, yield strength $\sigma_y = 420\text{ MPa}$, $\alpha_L = 13.5 \times 10^{-6}\text{ K}^{-1}$, and Coffin-Manson low-cycle fatigue parameters: $\varepsilon_f' = 0.40$, $c = -0.55$.
<br><br>
1. Calculate the constrained elastic stress amplitude $\sigma = E \alpha_L \Delta T / 2$ for a minor temperature cycle $\Delta T = 120^\circ\text{C}$. Does the pipe yield?<br>
2. During an emergency plant trip, the pipe undergoes a rapid temperature cycle $\Delta T = 380^\circ\text{C}$. Calculate the imposed total strain range $\Delta\varepsilon_{\text{thermal}}$.<br>
3. Calculate the plastic strain range $\Delta\varepsilon_p = \Delta\varepsilon_{\text{thermal}} - \frac{2\sigma_y}{E}$.<br>
4. Using the Coffin-Manson relation $\Delta\varepsilon_p / 2 = \varepsilon_f' (2N_f)^c$, calculate the number of thermal shock cycles $N_f$ the pipe can survive before cracking.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Minor thermal cycle ($\Delta T = 120^\circ\text{C}$)</strong><br>
$$\sigma_{\text{thermal}} = E \alpha_L \Delta T = (190 \times 10^9\text{ Pa}) \times (13.5 \times 10^{-6}\text{ K}^{-1}) \times (120\text{ K})$$
$$\sigma_{\text{thermal}} = (190 \times 10^9) \times (1.62 \times 10^{-3}) = 3.078 \times 10^8\text{ Pa} = 307.8\text{ MPa}$$
$$\sigma_a = \frac{\sigma_{\text{thermal}}}{2} = 153.9\text{ MPa}$$
Comparing with yield strength $\sigma_y = 420\text{ MPa}$:
$$\sigma_{\text{thermal}} = 307.8\text{ MPa} < \sigma_y = 420\text{ MPa}$$
The thermal stress remains purely elastic. The pipe does NOT yield, operating safely in the high-cycle fatigue regime.
</div>
<div class="solution-step">
<strong>Step 2: Total thermal strain for $\Delta T = 380^\circ\text{C}$</strong><br>
$$\Delta\varepsilon_{\text{thermal}} = \alpha_L \Delta T = (13.5 \times 10^{-6}\text{ K}^{-1}) \times (380\text{ K}) = 5.130 \times 10^{-3} = 0.513\%$$
</div>
<div class="solution-step">
<strong>Step 3: Calculate plastic strain range $\Delta\varepsilon_p$</strong><br>
Elastic strain range capacity:
$$\Delta\varepsilon_e = \frac{2\sigma_y}{E} = \frac{2 \times 420\text{ MPa}}{190,000\text{ MPa}} \approx 4.421 \times 10^{-3}$$
Plastic strain range:
$$\Delta\varepsilon_p = \Delta\varepsilon_{\text{thermal}} - \Delta\varepsilon_e = 5.130 \times 10^{-3} - 4.421 \times 10^{-3} = 7.09 \times 10^{-4} = 0.000709$$
Plastic strain amplitude:
$$\frac{\Delta\varepsilon_p}{2} = \frac{7.09 \times 10^{-4}}{2} = 3.545 \times 10^{-4}$$
</div>
<div class="solution-step">
<strong>Step 4: Calculate thermal fatigue life $N_f$</strong><br>
From Coffin-Manson:
$$\frac{\Delta\varepsilon_p}{2} = \varepsilon_f' (2N_f)^c \implies (2N_f)^c = \frac{\Delta\varepsilon_p / 2}{\varepsilon_f'}$$
Given $\varepsilon_f' = 0.40$, $c = -0.55$:
$$\frac{3.545 \times 10^{-4}}{0.40} \approx 8.8625 \times 10^{-4}$$
$$(2N_f)^{-0.55} = 8.8625 \times 10^{-4} \implies 2N_f = (8.8625 \times 10^{-4})^{-1 / 0.55}$$
$$-\frac{1}{0.55} \approx -1.81818$$
$$2N_f = (8.8625 \times 10^{-4})^{-1.81818} = (1128.35)^{1.81818}$$
$$\ln(1128.35) \approx 7.0285$$
$$\text{Exponent} = 1.81818 \times 7.0285 \approx 12.779$$
$$2N_f = \exp(12.779) \approx 354,700\text{ reversals}$$
$$N_f = \frac{354,700}{2} \approx 177,350\text{ cycles}$$
If the severe emergency trip thermal shock is unmitigated and occurs with local stress concentrations ($K_t \sim 2\text{--}3$), fatigue life will drop into hundreds of cycles.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
At $\Delta T = 120^\circ\text{C}$: $\sigma_{\text{thermal}} = 307.8\text{ MPa} < \sigma_y$ (purely elastic, no yielding).<br>
At $\Delta T = 380^\circ\text{C}$: $\Delta\varepsilon_{\text{thermal}} = 5.13 \times 10^{-3}$, plastic strain range $\Delta\varepsilon_p = 7.09 \times 10^{-4}$.<br>
Thermal fatigue life: $N_f \approx 177,000\text{ full emergency thermal cycles}$.
</div>"""
})

# ==========================================
# Problem 44
# ==========================================
add({
    "num": 44,
    "title": "Creep-Fatigue Interaction and Dwell Time Effects",
    "difficulty": "Hard",
    "category": "Fatigue & Creep Interaction",
    "tags": ["Creep-Fatigue Interaction", "Dwell Time", "Hold Time", "Damage Envelope"],
    "statement": r"""In aircraft jet engines and gas turbines, turbine discs and blades operate under cyclic fatigue loading combined with prolonged high-temperature steady-state cruise periods (dwell time or hold time at peak tensile load).
This combined degradation is known as <strong>Creep-Fatigue Interaction</strong>.
<br><br>
1. Contrast pure cyclic fatigue (zero dwell time, continuous triangular/sinusoidal cycling at $1\text{ Hz}$) with creep-fatigue cycling containing a 10-minute tensile dwell hold at peak stress $\sigma_{\text{max}}$. How does a tensile hold time affect fatigue crack growth rate $da/dN$ and total cycle life $N_f$?<br>
2. Explain why a <strong>tensile dwell hold</strong> is catastrophically damaging, while a <strong>compressive dwell hold</strong> at $\sigma_{\text{min}}$ is relatively benign (or even beneficial).<br>
3. The ASME Boiler and Pressure Vessel Code (Section III, Subsection NH) evaluates creep-fatigue damage using the bilinear interaction diagram:
$$\sum_{i=1}^k \frac{n_i}{N_{fi}} + \sum_{j=1}^m \frac{\Delta t_j}{t_{rj}} \le D_{\text{allowable}}$$
Draw or describe this damage interaction envelope (where $D_{\text{allowable}}$ can drop to $(0.3, 0.3)$ at the bilinear intersection point).""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Effect of tensile dwell hold time</strong><br>
- <em>Continuous fatigue (zero hold):</em> Cracks propagate by mechanical cyclic blunting/resharpening (Stage II striation growth). Crack growth rate is typically $\sim 10^{-7}\text{ m/cycle}$.<br>
- <em>Tensile dwell hold (e.g., 10 min hold at $\sigma_{\text{max}}$):</em>
During the sustained tensile dwell period at elevated temperature ($> 0.5 T_m$), high-temperature creep cavity nucleation occurs along grain boundaries ahead of the fatigue crack tip. When the next cyclic fatigue unloading/reloading pulse occurs, the crack front does not have to cut through solid metal; instead, it rapidly links with the pre-existing creep micro-cavities.
This accelerates the crack growth rate $da/dN$ by <strong>$10\times$ to $100\times$</strong>, reducing total fatigue life $N_f$ by an order of magnitude.
</div>
<div class="solution-step">
<strong>Step 2: Tensile hold vs. Compressive hold</strong><br>
- <em>Tensile Dwell Hold:</em> Sustained tensile stress drives vacancy diffusion toward transverse grain boundaries, creating intergranular creep voids, severe stress relaxation at the tip, and accelerated grain boundary oxidation.
- <em>Compressive Dwell Hold:</em> Squeezes grain boundaries under compression. Vacancies are expelled from grain boundaries rather than condensed, preventing void nucleation. Furthermore, compressive stress relaxation causes residual tensile stresses upon unloading, shifting the subsequent cycle in a way that retards crack growth.
</div>
<div class="solution-step">
<strong>Step 3: ASME Bilinear Creep-Fatigue Damage Envelope</strong><br>
Total damage is the sum of cyclic fatigue damage $D_f = \sum (n/N_f)$ and time-dependent creep damage $D_c = \sum (\Delta t / t_r)$.
If damage were purely linear (Miner's rule), the boundary would be a straight diagonal line $D_f + D_c = 1.0$.
However, because creep cavitation and cyclic fatigue damage interact synergistically, the ASME Code mandates a severely constricted <strong>bilinear envelope</strong>:
- The envelope connects $(D_f = 1, D_c = 0) \to (0.3, 0.3) \to (D_f = 0, D_c = 1.0)$.
- At the critical interaction point, failure occurs when fatigue damage is only $0.30$ and creep damage is only $0.30$ (sum $= 0.60 \ll 1.0$)!
Designing high-temperature components must account for this severe synergistic penalty.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Tensile dwell holds nucleate intergranular creep cavities, accelerating fatigue crack growth by $10\text{--}100\times$.<br>
Tensile holds cause cavitation; compressive holds suppress void formation.<br>
ASME bilinear design envelope accounts for synergy: failure can occur at $(D_f = 0.3, D_c = 0.3)$ due to severe cross-damage interaction.
</div>"""
})

# ==========================================
# Problem 45
# ==========================================
add({
    "num": 45,
    "title": "Creep Cavitation and Intergranular Rupture: Hull-Rimmer Model",
    "difficulty": "Hard",
    "category": "High-Temperature Creep",
    "tags": ["Creep Cavitation", "Hull-Rimmer Model", "Intergranular Rupture", "Wedge Cracks"],
    "statement": r"""During tertiary creep, fracture occurs by the nucleation, growth, and coalescence of microscopic cavities on grain boundaries oriented transverse to the applied tensile stress $\sigma$.
Two distinct cavitation morphologies develop:
1. <strong>r-type cavities</strong> (rounded/spherical voids along transverse grain boundaries).
2. <strong>w-type cracks</strong> (wedge-shaped cracks at grain boundary triple junctions).
<br><br>
In the classic Hull-Rimmer model, rounded cavities of radius $r$ spaced at center-to-center distance $2a$ along a grain boundary grow by vacancy diffusion along the boundary interface:
$$\frac{dr}{dt} = \frac{D_{\text{gb}} \delta \Omega}{2 k_B T r a} \left(\sigma - \frac{2\gamma_s}{r}\right)$$
where $\sigma$ is the tensile stress, $2\gamma_s / r$ is the capillary sintering stress, $D_{\text{gb}}$ is boundary diffusivity, $\delta$ is boundary thickness, and $\Omega$ is atomic volume.
<br><br>
1. What is the critical threshold cavity radius $r_{\text{crit}} = \frac{2\gamma_s}{\sigma}$? What happens to a cavity with $r < r_{\text{crit}}$ versus $r > r_{\text{crit}}$?<br>
2. For an austenitic steel under tensile creep stress $\sigma = 100\text{ MPa}$ at $650^\circ\text{C}$ ($\gamma_s = 1.2\text{ J/m}^2$), calculate $r_{\text{crit}}$ (in nm).<br>
3. Describe the mechanism by which grain boundary sliding drives the formation of <strong>w-type wedge cracks</strong> at triple junctions.<br>
4. Why does adding trace amounts of boron ($0.003\text{--}0.005\text{ wt}\%$) to nickel superalloys and steels retard creep cavitation?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Critical threshold radius $r_{\text{crit}}$</strong><br>
The term $\left(\sigma - \frac{2\gamma_s}{r}\right)$ represents the net driving force for cavity growth.
The capillary surface tension of the void exerts a compressive Laplace sintering pressure $P_{\text{cap}} = 2\gamma_s / r$ attempting to collapse the void.
- If $r < r_{\text{crit}} = \frac{2\gamma_s}{\sigma}$: Laplace pressure exceeds applied tensile stress ($P_{\text{cap}} > \sigma$). The cavity shrinks and sinters shut ($dr/dt < 0$).
- If $r > r_{\text{crit}}$: Applied tensile stress overcomes capillary surface tension ($\sigma > P_{\text{cap}}$). The cavity absorbs vacancies continuously and expands unstably until rupture ($dr/dt > 0$).
</div>
<div class="solution-step">
<strong>Step 2: Calculate $r_{\text{crit}}$ at $\sigma = 100\text{ MPa}$</strong><br>
Given: $\gamma_s = 1.2\text{ J/m}^2$, $\sigma = 100\text{ MPa} = 1.0 \times 10^8\text{ Pa}$:
$$r_{\text{crit}} = \frac{2 \gamma_s}{\sigma} = \frac{2 \times 1.2\text{ J/m}^2}{1.0 \times 10^8\text{ Pa}} = \frac{2.4}{1.0 \times 10^8} = 2.4 \times 10^{-8}\text{ m} = 24.0\text{ nm}$$
Any micro-void larger than $24\text{ nm}$ in radius will grow continuously under this creep stress.
</div>
<div class="solution-step">
<strong>Step 3: Mechanism of w-type wedge cracks at triple junctions</strong><br>
Under elevated temperature shear stresses, adjacent grains slide past one another along grain boundary planes (grain boundary sliding).
Where three grains intersect at a <strong>triple junction line</strong>, grain boundary sliding cannot proceed smoothly due to geometric constraint. The sliding of Grain 1 past Grain 2 creates an intense concentrated tensile stress at the triple point where the boundary terminates against Grain 3. This localized tensile singularity opens a triangular, wedge-shaped fissure (w-type crack) that propagates along the transverse grain boundary.
</div>
<div class="solution-step">
<strong>Step 4: Beneficial role of trace Boron</strong><br>
Boron atoms have an atomic radius intermediate between interstitial carbon and substitutional iron/nickel.
1. Boron segregates strongly to high-angle grain boundaries, filling open atomic voids and lowering grain boundary interfacial free energy ($\gamma_{\text{gb}}$).
2. Boron retards grain boundary self-diffusion ($D_{\text{gb}}$ decreases), slowing the vacancy flux that feeds cavity growth.
3. Boron suppresses grain boundary sliding by pinning boundary dislocations, preventing stress concentrations that open triple-point wedge cracks.
Adding just $30\text{--}50\text{ ppm}$ of boron can increase creep rupture life by $300\%\text{ to }500\%$!
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Critical cavity radius: $r_{\text{crit}} = \frac{2\gamma_s}{\sigma} = 24.0\text{ nm}$ (cavities $>24\text{ nm}$ grow unstably).<br>
Wedge cracks form at triple junctions due to geometric constraint blocking grain boundary sliding.<br>
Trace boron ($30\text{--}50\text{ ppm}$) segregates to grain boundaries, lowering diffusion diffusivity ($D_{\text{gb}}$) and suppressing sliding.
</div>"""
})

# ==========================================
# Problem 46
# ==========================================
add({
    "num": 46,
    "title": "The Monkman-Grant Empirical Creep Rupture Relationship",
    "difficulty": "Medium",
    "category": "High-Temperature Creep",
    "tags": ["Monkman-Grant", "Creep Rupture Life", "Minimum Creep Rate", "Empirical Scaling"],
    "statement": r"""In 1956, F. C. Monkman and N. J. Grant demonstrated that for a given alloy across a wide range of stresses and temperatures, the minimum steady-state creep rate $\dot{\varepsilon}_s$ is inversely proportional to the rupture lifetime $t_r$:
$$\dot{\varepsilon}_s^m \times t_r = C_{\text{MG}}$$
or in logarithmic form:
$$\log_{10}(t_r) = \log_{10}(C_{\text{MG}}) - m \log_{10}(\dot{\varepsilon}_s)$$
where $m \approx 0.8\text{ to }1.0$ and $C_{\text{MG}}$ is a material constant representing the strain accumulated during secondary creep.
<br><br>
For a heat-resistant 2.25Cr-1Mo boiler steel, creep laboratory testing determines Monkman-Grant parameters:
$m = 0.95$ and $C_{\text{MG}} = 0.080$ ($8.0\%$ strain).
<br><br>
1. An in-service extensometer on a high-pressure steam line records a steady-state creep rate $\dot{\varepsilon}_s = 4.0 \times 10^{-6}\text{ h}^{-1}$.
Calculate the expected remaining creep rupture life $t_r$ (in hours and operating years).<br>
2. If another boiler tube of the same steel exhibits an accelerated steady-state creep rate $\dot{\varepsilon}_s' = 3.2 \times 10^{-5}\text{ h}^{-1}$, calculate its rupture life $t_r'$.<br>
3. Explain why the Monkman-Grant relationship is an invaluable tool for plant operators conducting online structural health monitoring.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate rupture life $t_r$ for $\dot{\varepsilon}_s = 4.0 \times 10^{-6}\text{ h}^{-1}$</strong><br>
From $\dot{\varepsilon}_s^m \times t_r = C_{\text{MG}}$:
$$t_r = \frac{C_{\text{MG}}}{\dot{\varepsilon}_s^m}$$
Given: $m = 0.95$, $C_{\text{MG}} = 0.080$, $\dot{\varepsilon}_s = 4.0 \times 10^{-6}\text{ h}^{-1}$:
$$\dot{\varepsilon}_s^{0.95} = (4.0 \times 10^{-6})^{0.95}$$
$$\log_{10}(4.0 \times 10^{-6}) = \log_{10}(4.0) - 6 = 0.60206 - 6 = -5.39794$$
$$0.95 \times (-5.39794) = -5.12804$$
$$\dot{\varepsilon}_s^{0.95} = 10^{-5.12804} \approx 7.4466 \times 10^{-6}\text{ h}^{-0.95}$$
Rupture lifetime:
$$t_r = \frac{0.080}{7.4466 \times 10^{-6}} \approx 10,743\text{ hours}$$
In operating years ($8,760\text{ h/year}$):
$$t_r = \frac{10,743}{8,760} \approx 1.226\text{ years} \approx 1.23\text{ years}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate rupture life for accelerated rate $\dot{\varepsilon}_s' = 3.2 \times 10^{-5}\text{ h}^{-1}$</strong><br>
$$\log_{10}(3.2 \times 10^{-5}) = 0.50515 - 5 = -4.49485$$
$$0.95 \times (-4.49485) = -4.27011$$
$$(\dot{\varepsilon}_s')^{0.95} = 10^{-4.27011} \approx 5.369 \times 10^{-5}\text{ h}^{-0.95}$$
$$t_r' = \frac{0.080}{5.369 \times 10^{-5}} \approx 1,490\text{ hours}$$
In operating months:
$$t_r' = \frac{1,490}{24 \times 30.5} \approx 2.03\text{ months}$$
An $8\times$ increase in creep rate slashes the tube's remaining life from over 1.2 years down to just 2 months!
</div>
<div class="solution-step">
<strong>Step 3: Engineering value for online monitoring</strong><br>
In high-temperature petrochemical and power plants, waiting for tertiary creep necking to occur is dangerous because tertiary creep accelerates to rupture with terrifying speed.
The Monkman-Grant relation allows engineers to measure the creep rate early in the component's life (during secondary steady-state creep, within the first few hundred hours of service) and accurately extrapolate the total rupture lifetime years in advance. This enables scheduled preventative maintenance and scheduled tube replacement before catastrophic boiler rupture occurs.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
For $\dot{\varepsilon}_s = 4.0 \times 10^{-6}\text{ h}^{-1}$: $t_r = 10,743\text{ hours}$ ($1.23\text{ years}$).<br>
For $\dot{\varepsilon}_s = 3.2 \times 10^{-5}\text{ h}^{-1}$: $t_r' = 1,490\text{ hours}$ ($2.0\text{ months}$).<br>
Monkman-Grant enables early prediction of total rupture life from non-destructive strain rate monitoring during steady-state secondary creep.
</div>"""
})

# ==========================================
# Problem 47
# ==========================================
add({
    "num": 47,
    "title": "Quench Cracking and Transformation Stresses in Heat-Treated Steels",
    "difficulty": "Medium",
    "category": "Thermal & Residual Stresses",
    "tags": ["Quench Cracking", "Martensite Transformation", "Transformation Stresses", "Volume Expansion"],
    "statement": r"""During the water quenching of high-carbon alloy steel components (e.g., gears, tools), two competing physical stress mechanisms develop:
1. <strong>Thermal Stresses:</strong> The surface cools faster than the core, contracting elastically while the hot core resists.
2. <strong>Transformation Stresses:</strong> The diffusionless transformation of FCC austenite into BCT martensite involves a substantial volume expansion:
$$\frac{\Delta V}{V} \approx +3.5\%\text{ to }+4.2\%$$
<br>
1. Explain the sequence of stress reversal during quenching: why does the surface end up in intense <strong>residual tensile stress</strong> at the end of the quench if martensite forms in the core after the surface has already hardened?<br>
2. Why does <strong>quench cracking</strong> occur predominantly during the final stages of cooling (below the $M_s$ and $M_f$ temperatures, $< 150^\circ\text{C}$) rather than at high temperatures?<br>
3. Describe two heat treatment techniques used to completely eliminate quench cracking:
   (a) <strong>Martempering (Marquenching)</strong>.<br>
   (b) <strong>Austempering</strong>.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Mechanism of residual stress reversal and surface tension</strong><br>
1. <em>Initial cooling:</em> The surface cools rapidly, dropping below the Martensite Start temperature ($M_s$) and transforming into hard, brittle martensite. This transformation causes an expansion ($\Delta V/V \approx +4\%$). The hotter, soft austenitic core accommodates this expansion by plastic yielding.
2. <em>Later cooling:</em> As the core finally cools below $M_s$, it now undergoes its own $+4\%$ martensitic expansion.
3. <em>Final state:</em> The already hardened, rigid martensitic surface shell cannot stretch elastically to accommodate the expanding core. The expanding core pushes outward against the rigid shell, driving the surface into <strong>intense tensile residual stress</strong> ($\sigma_{\text{res}} > +500\text{--}800\text{ MPa}$).
</div>
<div class="solution-step">
<strong>Step 2: Why quench cracking occurs below $M_f$ ($< 150^\circ\text{C}$)</strong><br>
At high temperatures ($> 300^\circ\text{C}$), austenite is ductile and easily relaxes localized stresses via plastic slip.
Below $150^\circ\text{C}$ (between $M_s$ and $M_f$), untempered virgin martensite is formed throughout the microstructure. Freshly formed high-carbon martensite is an extremely hard, brittle, body-centered tetragonal phase supersaturated with carbon, with virtually zero dislocation mobility and negligible fracture toughness ($K_{Ic} < 15\text{ MPa}\sqrt{\text{m}}$).
When peak residual tensile stresses coincide with this ultra-brittle, untempered martensite, brittle cleavage cracks (quench cracks) propagate instantaneously from fillets and corners with a loud, ringing sound.
</div>
<div class="solution-step">
<strong>Step 3: Two heat treatment techniques to eliminate quench cracking</strong><br>
(a) <strong>Martempering (Marquenching):</strong> The steel is quenched from austenitizing temperature into a hot molten salt bath maintained just above the $M_s$ temperature (typically $200^\circ\text{C}\text{--}250^\circ\text{C}$). The part is held until the temperature equalizes completely across the entire cross-section (eliminating thermal gradients). The part is then removed and cooled slowly in air through the martensite range ($M_s \to M_f$). Martensite forms uniformly and simultaneously throughout both surface and core, eliminating transformational stress gradients and banishing quench cracks.<br>
(b) <strong>Austempering:</strong> The steel is quenched into a molten salt bath held in the lower bainite range ($250^\circ\text{C}\text{ to }400^\circ\text{C}$, above $M_s$) and held isothermally until austenite transforms completely into <strong>bainite</strong>. Bainite has high strength combined with outstanding ductility and toughness, avoiding untempered martensite entirely without needing subsequent tempering.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Late transformation expansion of the core forces the rigid martensitic surface into high tensile residual stress.<br>
Cracking occurs below $150^\circ\text{C}$ because fresh untempered martensite has virtually zero fracture toughness ($K_{Ic} < 15\text{ MPa}\sqrt{\text{m}}$).<br>
Martempering equalizes temperature above $M_s$ before slow air cooling; Austempering transforms steel into tough lower bainite.
</div>"""
})

# ==========================================
# Problem 48
# ==========================================
add({
    "num": 48,
    "title": "Liquid Metal Embrittlement (LME): Solid-Liquid Wetting Catastrophe",
    "difficulty": "Hard",
    "category": "Environmental Fracture",
    "tags": ["LME", "Liquid Metal Embrittlement", "Wetting", "Galvanized Steel Welding"],
    "statement": r"""<strong>Liquid Metal Embrittlement (LME)</strong> is a catastrophic form of environmental degradation where a normally ductile solid metal undergoes instantaneous, brittle intergranular fracture upon coming into contact with a specific molten liquid metal while under tensile stress.
Classic susceptible couples include:
- Solid steel in contact with liquid zinc ($\text{Zn}$, melting point $419.5^\circ\text{C}$) or liquid copper ($\text{Cu}$).
- Solid aluminum in contact with liquid gallium ($\text{Ga}$, melting point $29.8^\circ\text{C}$) or mercury ($\text{Hg}$).
- Solid titanium in contact with liquid cadmium ($\text{Cd}$).
<br><br>
1. Describe the thermodynamics of grain boundary wetting by a liquid metal:
Using Smith's wetting angle equation: $\cos\left(\frac{\theta}{2}\right) = \frac{\gamma_{\text{gb}}}{2 \gamma_{\text{sl}}}$, explain the condition for complete liquid penetration along grain boundaries ($\theta = 0^\circ$).<br>
2. A single droplet of liquid gallium placed on a bent sheet of ductile aluminum causes the sheet to shatter in two under hand pressure in seconds. Describe the microscopic transport mechanism.<br>
3. In the automotive industry, why has the spot welding of galvanized (zinc-coated) advanced high-strength steels (AHSS) experienced severe liquid metal embrittlement cracking?""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Thermodynamics of grain boundary wetting</strong><br>
The equilibrium dihedral contact angle $\theta$ between a liquid metal and a solid grain boundary is:
$$\cos\left(\frac{\theta}{2}\right) = \frac{\gamma_{\text{gb}}}{2 \gamma_{\text{sl}}}$$
where $\gamma_{\text{gb}}$ is the solid grain boundary energy and $\gamma_{\text{sl}}$ is the solid-liquid interfacial energy.
- When $\gamma_{\text{gb}} < 2 \gamma_{\text{sl}}$: $\theta > 0$. The liquid forms discrete lenticular droplets at grain boundaries.
- When $\gamma_{\text{gb}} \ge 2 \gamma_{\text{sl}}$: The right-hand side exceeds 1.0, so the contact angle drops to $\mathbf{\theta = 0^\circ}$.
At $\theta = 0^\circ$, <strong>complete grain boundary wetting</strong> occurs: the liquid metal spreads spontaneously and continuously along every grain boundary network, replacing high-energy solid-solid atomic bonds with low-energy solid-liquid interfaces.
</div>
<div class="solution-step">
<strong>Step 2: The Gallium-Aluminum Catastrophe</strong><br>
When liquid gallium contacts aluminum:
1. Gallium atoms wet the aluminum grain boundaries instantaneously ($\theta = 0^\circ$).
2. Driven by capillarity and stress gradients, liquid gallium diffuses along the grain boundary network at extraordinary speeds of several millimeters per second!
3. The liquid gallium atoms completely sever the interatomic cohesive bonds between adjacent aluminum grains.
4. Cohesive strength drops to virtually zero ($\sigma_{\text{th}} \approx 0$). The solid polycrystal transforms into a loose collection of unbonded grains, shattering like dry sand under the lightest applied touch.
</div>
<div class="solution-step">
<strong>Step 3: LME in resistance spot welding of galvanized AHSS</strong><br>
In automotive manufacturing, steel body sheets are hot-dip galvanized with a zinc coating ($5\text{--}10\text{ }\mu\text{m}$) for corrosion protection:
1. During resistance spot welding, electric current heats the weld nugget above $1400^\circ\text{C}$. The adjacent zinc coating melts at $419.5^\circ\text{C}$.
2. Advanced High-Strength Steels (AHSS, e.g., dual-phase and martensitic steels) require high electrode clamping forces and undergo severe thermal expansion contractions, creating high local tensile stresses ($> 800\text{ MPa}$) on the sheet surface.
3. The combination of molten liquid zinc, high surface tensile stress, and susceptible high-strength steel microstructure triggers Liquid Metal Embrittlement. Liquid zinc penetrates the prior austenite grain boundaries beneath the welding electrode, forming deep cracks ($0.2\text{--}0.5\text{ mm}$ deep) that compromise crashworthiness.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Complete wetting occurs when $\gamma_{\text{gb}} \ge 2\gamma_{\text{sl}}$ ($\theta = 0^\circ$), causing liquid to penetrate boundaries spontaneously.<br>
Liquid Ga severs atomic bonds between Al grains at speeds of millimeters per second, destroying all cohesion.<br>
Galvanized AHSS spot welding suffers LME due to the combination of molten zinc ($>420^\circ\text{C}$) and severe clamping tensile stresses.
</div>"""
})

# ==========================================
# Problem 49
# ==========================================
add({
    "num": 49,
    "title": "Adhesive Wear: The Archard Wear Equation",
    "difficulty": "Easy",
    "category": "Surface Mechanics & Wear",
    "tags": ["Archard Wear Law", "Adhesive Wear", "Wear Coefficient", "Hardness"],
    "statement": r"""Surface degradation by mechanical wear accounts for immense economic losses and machine downtime.
The classic <strong>Archard Wear Equation</strong> models the volume of material removed by adhesive sliding wear ($V_{\text{wear}}$):
$$V_{\text{wear}} = K \frac{W L}{H}$$
where $K$ is the dimensionless wear coefficient, $W$ is the normal load applied between contacting surfaces, $L$ is the sliding distance, and $H$ is the hardness of the softer contacting material (typically Vickers hardness in $\text{N/m}^2$ or $\text{Pa}$).
<br><br>
A bronze bearing sleeve in a mechanical press operates under a normal load $W = 4.5\text{ kN}$ against a hardened steel shaft.
The bronze has a Vickers hardness $H = 120\text{ HV} \approx 1.18 \times 10^9\text{ N/m}^2$ ($1.18\text{ GPa}$) and an adhesive wear coefficient $K = 2.4 \times 10^{-5}$.
The shaft rotates at $N = 300\text{ rpm}$ with a journal radius $R = 40.0\text{ mm}$.
<br><br>
1. Calculate the sliding speed $v$ (in m/s) and the total sliding distance $L$ accumulated after $1000\text{ hours}$ of continuous operation.<br>
2. Calculate the total volume of bronze worn away $V_{\text{wear}}$ (in $\text{mm}^3$).<br>
3. The bearing contact area is $A = 2400\text{ mm}^2$. Calculate the uniform wear depth $h_{\text{wear}} = V_{\text{wear}} / A$ (in mm).<br>
4. State the fundamental design principle implied by Archard's equation for maximizing wear resistance.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Calculate sliding speed $v$ and total sliding distance $L$</strong><br>
Shaft diameter: $D = 2R = 0.080\text{ m}$.
Circumference per revolution:
$$C_{\text{rev}} = \pi D = \pi \times 0.080\text{ m} \approx 0.251327\text{ m/rev}$$
Sliding speed:
$$v = C_{\text{rev}} \times \left(\frac{300\text{ rev}}{60\text{ s}}\right) = 0.251327 \times 5.0\text{ rev/s} \approx 1.2566\text{ m/s}$$
Total operating time in seconds:
$$t = 1000\text{ h} \times 3,600\text{ s/h} = 3.60 \times 10^6\text{ s}$$
Total sliding distance:
$$L = v \times t = (1.2566\text{ m/s}) \times (3.60 \times 10^6\text{ s}) \approx 4,523,893\text{ m} \approx 4.524 \times 10^6\text{ m}$$
</div>
<div class="solution-step">
<strong>Step 2: Calculate worn volume $V_{\text{wear}}$</strong><br>
Given: $K = 2.4 \times 10^{-5}$, $W = 4,500\text{ N}$, $H = 1.18 \times 10^9\text{ N/m}^2$:
$$V_{\text{wear}} = K \frac{W L}{H} = (2.4 \times 10^{-5}) \times \frac{(4500\text{ N}) \times (4.5239 \times 10^6\text{ m})}{1.18 \times 10^9\text{ N/m}^2}$$
$$\text{Numerator} = (2.4 \times 10^{-5}) \times (2.03575 \times 10^{10}\text{ N}\cdot\text{m}) = 4.8858 \times 10^5\text{ N}\cdot\text{m}$$
$$V_{\text{wear}} = \frac{4.8858 \times 10^5}{1.18 \times 10^9} \approx 4.1405 \times 10^{-4}\text{ m}^3$$
Convert to $\text{mm}^3$ ($1\text{ m}^3 = 10^9\text{ mm}^3$):
$$V_{\text{wear}} = (4.1405 \times 10^{-4}\text{ m}^3) \times 10^9\text{ mm}^3/\text{m}^3 \approx 414,050\text{ mm}^3 \approx 414.1\text{ cm}^3$$
(With proper boundary lubrication, $K$ drops by $1000\times$ to $10^{-8}$, giving $V_{\text{wear}} \approx 0.41\text{ cm}^3$).
</div>
<div class="solution-step">
<strong>Step 3: Calculate wear depth $h_{\text{wear}}$</strong><br>
Given contact area $A = 2400\text{ mm}^2$:
$$h_{\text{wear}} = \frac{V_{\text{wear}}}{A} = \frac{414,050\text{ mm}^3}{2400\text{ mm}^2} \approx 172.5\text{ mm} \quad (\text{unlubricated dry sliding})$$
Under hydrodynamic oil film lubrication ($K = 2.4 \times 10^{-8}$):
$$h_{\text{wear, lubricated}} = \frac{172.5\text{ mm}}{1000} \approx 0.173\text{ mm} = 173\text{ }\mu\text{m}$$
</div>
<div class="solution-step">
<strong>Step 4: Fundamental design rule for wear resistance</strong><br>
According to Archard's equation ($V_{\text{wear}} \propto 1/H$):
To maximize sliding wear resistance:
1. <strong>Maximize surface hardness ($H$):</strong> Use case hardening (carburizing, nitriding, induction hardening) or hard ceramic coatings (TiN, CrN, diamond-like carbon DLC).
2. <strong>Minimize wear coefficient ($K$):</strong> Maintain full hydrodynamic fluid-film lubrication to eliminate direct metal-to-metal contact, and pair metallurgically incompatible metals that resist adhesive cold-welding.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Sliding distance: $L = 4,524\text{ km}$ ($v = 1.26\text{ m/s}$).<br>
Dry worn volume: $V_{\text{wear}} = 414.1\text{ cm}^3$; Lubricated wear depth: $h_{\text{wear}} \approx 173\text{ }\mu\text{m}$.<br>
Archard principle: Wear volume is inversely proportional to surface hardness ($V \propto 1/H$); maximize hardness and maintain hydrodynamic lubrication.
</div>"""
})

# ==========================================
# Problem 50
# ==========================================
add({
    "num": 50,
    "title": "Comprehensive Failure Analysis: Jet Engine Turbine Shaft Forensic Diagnosis",
    "difficulty": "Hard",
    "category": "Comprehensive Failure Analysis",
    "tags": ["Failure Analysis", "Fractography", "Fatigue vs Creep", "Root Cause Analysis"],
    "statement": r"""A high-pressure jet engine turbine rotor shaft fabricated from nickel-base superalloy Inconel 718 fractured catastrophically during flight, triggering an uncontained engine shutdown.
A forensic engineering metallurgical team conducts an investigation of the fractured shaft.
<br><br>
The laboratory examination reveals the following physical findings:
- <strong>Visual Inspection:</strong> A single fracture surface originating at a sharp internal oil lubricating hole (fillet radius $R = 0.20\text{ mm}$). Clear macroscopic, curved beachmarks originate at the hole and radiate across $65\%$ of the shaft cross-sectional area.
- <strong>SEM Fractography (Mid-Section):</strong> High-magnification ($15,000\times$) electron micrographs reveal regular, parallel striations perpendicular to the propagation direction, with an average spacing of $\delta = 0.45\text{ }\mu\text{m/cycle}$.
- <strong>SEM Fractography (Origin Zone):</strong> Intergranular micro-cavities and micro-cracks along transverse grain boundaries surrounded by heavy chromium oxide scale ($\text{Cr}_2\text{O}_3$).
- <strong>SEM Fractography (Final Zone):</strong> $100\%$ dimpled rupture (microvoid coalescence) inclined at $45^\circ$ to the shaft axis.
<br><br>
1. Synthesize these forensic findings and reconstruct the sequential chain of failure:
   (a) Identify the precise initiation site and root cause defect.<br>
   (b) Identify the mode and mechanism of Stage I crack initiation.<br>
   (c) Identify the mode and mechanism of Stage II crack propagation.<br>
   (d) Identify the final fracture mode in Stage III.<br>
2. Using the measured striation spacing $\delta = 0.45\text{ }\mu\text{m/cycle}$ and Paris Law parameters for Inconel 718 ($C = 1.20 \times 10^{-11}\text{ m/cycle}\cdot(\text{MPa}\sqrt{\text{m}})^{-3.2}, m = 3.20$), calculate the effective cyclic stress intensity range $\Delta K$ acting during mid-life propagation.<br>
3. Formulate three mandatory engineering corrective actions to permanently prevent future turbine shaft failures.""",
    "solution": r"""<div class="solution-step">
<strong>Step 1: Sequential Forensic Failure Reconstruction</strong><br>
(a) <strong>Initiation Site & Root Cause:</strong> The fracture initiated at the sharp internal oil lubrication hole. The tiny fillet radius ($R = 0.20\text{ mm}$) acted as a severe geometric notch stress concentration ($K_t \approx 3.5\text{--}4.0$), amplifying centrifugal and torsional cyclic operating stresses.<br>
(b) <strong>Stage I Initiation (Creep-Fatigue & Oxidation):</strong> The presence of intergranular micro-cavities and heavy chromium oxide scale at the origin proves that initiation was driven by <strong>high-temperature creep-fatigue interaction and localized oxidation</strong>. Prolonged engine cruise dwell times under high thermal and centrifugal stresses nucleated creep cavities along transverse grain boundaries at the notch root.<br>
(c) <strong>Stage II Propagation (Mechanical Fatigue):</strong> The clear macroscopic beachmarks and fine microscopic fatigue striations ($\delta = 0.45\text{ }\mu\text{m}$) confirm classic <strong>Stage II cyclic mechanical fatigue crack propagation</strong>. The crack grew cycle-by-cycle over thousands of flight take-off/climb/cruise duty cycles, advancing across $65\%$ of the shaft cross-section without detection.<br>
(d) <strong>Stage III Final Rupture:</strong> Once the fatigue crack consumed $65\%$ of the cross-section, the net remaining ligament could no longer support the maximum engine torque. The stress intensity factor exceeded the fracture toughness ($K_I \ge K_{Ic}$), triggering sudden, unstable <strong>ductile overload shear rupture (microvoid coalescence dimples)</strong> at $45^\circ$ shear lips.
</div>
<div class="solution-step">
<strong>Step 2: Calculate effective stress intensity range $\Delta K$</strong><br>
Because each fatigue striation corresponds approximately to the crack advance per cycle:
$$\frac{da}{dN} \approx \delta = 0.45\text{ }\mu\text{m/cycle} = 4.50 \times 10^{-7}\text{ m/cycle}$$
From Paris Law $\frac{da}{dN} = C (\Delta K)^m$:
$$(\Delta K)^m = \frac{da/dN}{C} \implies \Delta K = \left(\frac{da/dN}{C}\right)^{1/m}$$
Given $C = 1.20 \times 10^{-11}$, $m = 3.20$:
$$\frac{da/dN}{C} = \frac{4.50 \times 10^{-7}}{1.20 \times 10^{-11}} = 37,500$$
$$\Delta K = (37,500)^{1/3.20} = (37,500)^{0.3125} \approx 26.85\text{ MPa}\sqrt{\text{m}}$$
During mid-life propagation, the crack tip experienced an effective cyclic stress intensity range of $\Delta K \approx 26.9\text{ MPa}\sqrt{\text{m}}$.
</div>
<div class="solution-step">
<strong>Step 3: Mandatory Engineering Corrective Actions</strong><br>
1. <strong>Design Modification (Reduce $K_t$):</strong> Increase the oil hole fillet radius from $R = 0.20\text{ mm}$ to $R \ge 1.50\text{ mm}$ and incorporate an elliptical chamfer relief, reducing the stress concentration factor $K_t$ from $3.8$ down to $< 1.8$.<br>
2. <strong>Surface Engineering (Compressive Residual Stresses):</strong> Mandate automated <strong>internal shot peening or ball burnishing</strong> inside all oil lubrication bores to induce deep compressive residual stresses ($\sigma_{\text{res}} \le -600\text{ MPa}$), counteracting the tensile mean stress and preventing creep-fatigue crack nucleation.<br>
3. <strong>NDI Inspection Protocol:</strong> Implement mandatory periodic ultrasonic or eddy current non-destructive inspection (NDI) of internal oil bores at intervals calculated using fracture mechanics integration ($N_{\text{inspect}} = N_f / 2 \approx 5,000\text{ flight cycles}$), guaranteeing detection of subcritical cracks before they exceed the safe threshold.
</div>
<div class="boxed-answer">
<strong>Key Results:</strong><br>
Root cause: Severe stress concentration at sharp oil hole ($R = 0.2\text{ mm}$) combined with high-temperature creep-fatigue and oxidation.<br>
Stage II propagation: Cyclic mechanical fatigue advancing $0.45\text{ }\mu\text{m/cycle}$ across $65\%$ of cross-section ($\Delta K \approx 26.9\text{ MPa}\sqrt{\text{m}}$).<br>
Stage III final failure: Rapid ductile shear overload rupture.<br>
Corrective actions: Increase fillet radius to $R \ge 1.5\text{ mm}$, shot peen internal bore for compressive residual stress, and institute periodic ultrasonic NDI inspections.
</div>"""
})

if __name__ == "__main__":
    print(f"Total problems in P: {len(P)}")
    # Write to ch8_data.py
    out_path = os.path.join(os.path.dirname(__file__), "ch8_data.py")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Chapter 8 Problem Dataset (Failure: Fracture, Fatigue & Creep - 50 Problems)\n")
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
