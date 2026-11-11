# generator/make_ch1_short.py
# ==============================================================================
# SCIENCE OF MATERIALS — CHAPTER 1 CONCISE PROBLEMS GENERATOR
# University of Tehran | Department of Mechanical Engineering
# Author: Sina Sharifi (TA) | Instructor: Prof. A. Sadeghi
# ==============================================================================

import os

problems = [
    # -------------------------------------------------------------------------
    # TOPIC 1: THE MSE PARADIGM & TETRAHEDRON (Problems 1 - 8)
    # -------------------------------------------------------------------------
    {
        "number": 1,
        "title": "Materials Science vs. Materials Engineering",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Fundamental",
        "statement": "<p>State the fundamental distinction between <strong>Materials Science</strong> and <strong>Materials Engineering</strong> in terms of their primary objectives and scope.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Core Definitions</div>
  <ul>
    <li><strong>Materials Science:</strong> Investigates the basic relationships between the internal <em>structure</em> of materials (from atomic scale to microstructure) and their macroscopic <em>properties</em>. Its aim is discovery and understanding.</li>
    <li><strong>Materials Engineering:</strong> Applies established structure-property correlations to design, synthesize, and process materials into functional <em>components</em> that meet specific service, economic, and operational requirements.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Key Distinction:</strong> Materials Science discovers <em>structure-property relationships</em>; Materials Engineering utilizes these relationships to design <em>processing routes and engineered products</em>.
</div>"""
    },
    {
        "number": 2,
        "title": "The Four Vertices of the MSE Tetrahedron",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Fundamental",
        "statement": "<p>Name the four interconnected vertices of the central <strong>Materials Science & Engineering Tetrahedron</strong> and explain the directional dependency connecting them.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: The Four Interdependent Vertices</div>
  <ol>
    <li><strong>Processing:</strong> Synthesis and thermal/mechanical fabrication methods (casting, rolling, sintering, heat treating).</li>
    <li><strong>Structure:</strong> Arrangement of internal components across all length scales (electronic, atomic lattice, defects, grains).</li>
    <li><strong>Properties:</strong> Intrinsic material responses to external stimuli (mechanical, electrical, thermal, magnetic).</li>
    <li><strong>Performance:</strong> Functional effectiveness, reliability, and lifetime of the component in service.</li>
  </ol>
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Linear Flow and Feedback Loops</div>
  <p>The standard sequence is <strong>Processing &rarr; Structure &rarr; Properties &rarr; Performance</strong>. If performance in service is deficient, feedback loops prompt re-engineering of the processing or microstructural design.</p>
</div>
<div class="final-answer-box">
  <strong>Core Paradigm:</strong> $\\text{Processing} \\rightarrow \\text{Structure} \\rightarrow \\text{Properties} \\rightarrow \\text{Performance}$ (with continuous iterative optimization).
</div>"""
    },
    {
        "number": 3,
        "title": "Expanding the Tetrahedron: Economics and Sustainability",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Fundamental",
        "statement": "<p>Why does modern engineering expand the classical 4-vertex tetrahedron by incorporating <strong>Cost / Manufacturing Economics</strong> and <strong>Environmental Sustainability</strong>?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Practical Engineering Realities</div>
  <ul>
    <li><strong>Economic Feasibility:</strong> A material with superior mechanical or thermal properties cannot be adopted industrially if raw material or manufacturing costs exceed market viability.</li>
    <li><strong>Environmental & Lifecycle Impact:</strong> Regulatory compliance, carbon footprint during synthesis, energy consumption, and end-of-life recyclability are now mandatory design constraints.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Expanded Paradigm:</strong> Material selection balances the classic tetrahedron with <em>cost-effectiveness</em> and <em>circular lifecycle sustainability</em>.
</div>"""
    },
    {
        "number": 4,
        "title": "Processing-Structure Relationship: Copper Wire Example",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Fundamental",
        "statement": "<p>Explain how cold-drawing followed by annealing of pure copper wire demonstrates the direct link between <strong>processing</strong> and <strong>internal structure</strong>.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Microstructural Evolution</div>
  <ul>
    <li><strong>Cold Drawing:</strong> Severe plastic deformation increases dislocation density from $10^9 \\text{ m}^{-2}$ to $10^{15} \\text{ m}^{-2}$ and elongates grains, causing work hardening and reduced conductivity.</li>
    <li><strong>Recrystallization Annealing (400&ndash;500 &deg;C):</strong> Thermal energy drives nucleation of new, strain-free equiaxed grains, lowering dislocation density back to $10^9 \\text{ m}^{-2}$.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Conclusion:</strong> Cold drawing generates high dislocation density; subsequent annealing restores strain-free grains, directly proving that <em>processing governs internal structure</em>.
</div>"""
    },
    {
        "number": 5,
        "title": "Structure-Property Relationship: Polycrystal vs. Single Crystal",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Intermediate",
        "statement": "<p>Why do single-crystal nickel-base superalloy turbine blades exhibit dramatically higher creep resistance at 1000 &deg;C than conventional polycrystalline blades?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Creep Mechanism and Grain Boundaries</div>
  <p>At high homologous temperatures ($T > 0.5 T_m$), high-temperature creep occurs predominantly by <strong>grain boundary sliding</strong> and vacancy diffusion along grain boundaries (Coble creep).</p>
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Elimination of Grain Boundaries</div>
  <p>Single-crystal casting eliminates all transverse grain boundaries. With no grain boundaries present, grain boundary sliding and boundary diffusion are completely eliminated, drastically improving creep rupture life.</p>
</div>
<div class="final-answer-box">
  <strong>Core Principle:</strong> Eliminating grain boundaries eliminates grain boundary sliding and Coble diffusion creep, maximizing high-temperature creep resistance.
</div>"""
    },
    {
        "number": 6,
        "title": "Intrinsic Material Property vs. Component Performance",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Fundamental",
        "statement": "<p>Clearly distinguish between an <strong>intrinsic material property</strong> and <strong>component performance</strong>, giving one specific mechanical example of each.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Definitions and Comparisons</div>
  <ul>
    <li><strong>Intrinsic Property:</strong> A characteristic inherent to the material that is independent of size and shape (e.g., Young's modulus $E$, yield strength $\\sigma_y$, electrical resistivity $\\rho_e$).</li>
    <li><strong>Component Performance:</strong> The behavior and durability of a specific engineered part in service, which depends on material properties, geometry, surface finish, stress concentrators, and operating environment (e.g., fatigue life of an aircraft landing gear bolt).</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Summary:</strong> Yield strength $\\sigma_y$ is an <em>intrinsic property</em>; the load capacity and fatigue lifetime of a bolted joint is <em>component performance</em>.
</div>"""
    },
    {
        "number": 7,
        "title": "Hierarchical Length Scales in Materials Structure",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Fundamental",
        "statement": "<p>Rank the five hierarchical structural length scales from smallest to largest and provide typical characteristic dimensions for each.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Hierarchical Ordering</div>
  <ol>
    <li><strong>Subatomic:</strong> Electronic configuration and nuclear structure ($< 0.1 \\text{ nm} = 10^{-10} \\text{ m}$).</li>
    <li><strong>Atomic / Crystal:</strong> Unit cell dimensions and lattice spacing ($0.1 - 1 \\text{ nm}$).</li>
    <li><strong>Nanostructure:</strong> Nanoparticles, precipitates, and quantum dots ($1 - 100 \\text{ nm}$).</li>
    <li><strong>Microstructure:</strong> Grains, phases, and inclusion distributions visible by optical or SEM microscopy ($0.1 - 100 \\,\\mu\\text{m}$).</li>
    <li><strong>Macrostructure:</strong> Overall component geometry and macro-defects visible to the naked eye ($> 1 \\text{ mm}$).</li>
  </ol>
</div>
<div class="final-answer-box">
  <strong>Ranking:</strong> $\\text{Subatomic } (<0.1\\text{ nm}) < \\text{Atomic } (0.1\\text{--}1\\text{ nm}) < \\text{Nanostructure } (1\\text{--}100\\text{ nm}) < \\text{Microstructure } (0.1\\text{--}100\\,\\mu\\text{m}) < \\text{Macrostructure } (>1\\text{ mm})$.
</div>"""
    },
    {
        "number": 8,
        "title": "Reverse Engineering via MSE Feedback Loops",
        "category": "MSE Paradigm",
        "category_slug": "paradigm",
        "difficulty": "Intermediate",
        "statement": "<p>Explain how a fatigue fracture of an automotive crankshaft illustrates the reverse feedback loop within the MSE tetrahedron.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Tracing the Feedback Path</div>
  <ol>
    <li><strong>Performance Failure:</strong> The crankshaft suffers premature fatigue fracture in service.</li>
    <li><strong>Property Investigation:</strong> Fractographic inspection reveals inadequate fatigue endurance limit and poor surface toughness.</li>
    <li><strong>Structural Analysis:</strong> SEM analysis identifies coarse surface inclusions and micro-notches acting as stress concentrators.</li>
    <li><strong>Processing Modification:</strong> The casting process is altered to vacuum degassing (reducing inclusions) and a shot-peening step is introduced to induce beneficial compressive residual surface stresses.</li>
  </ol>
</div>
<div class="final-answer-box">
  <strong>Key Takeaway:</strong> Service failures initiate a reverse traversal: $\\text{Performance Failure} \\rightarrow \\text{Property Defect} \\rightarrow \\text{Microstructural Flaw} \\rightarrow \\text{Processing Redesign}$.
</div>"""
    },

    # -------------------------------------------------------------------------
    # TOPIC 2: HISTORICAL ERAS & EVOLUTION (Problems 9 - 14)
    # -------------------------------------------------------------------------
    {
        "number": 9,
        "title": "Materials As Civilization Markers",
        "category": "Historical Evolution",
        "category_slug": "history",
        "difficulty": "Fundamental",
        "statement": "<p>Why have historical epochs of human civilization (Stone Age, Bronze Age, Iron Age) been designated by materials rather than other technological metrics?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Enabling Technological Boundary</div>
  <p>Human capabilities in hunting, agriculture, warfare, construction, and transport were fundamentally constrained by the materials humans could extract and shape. Mastery of a new material class consistently unlocked new social, economic, and military capabilities.</p>
</div>
<div class="final-answer-box">
  <strong>Core Reason:</strong> Materials represented the primary technological bottleneck limiting the tools, energy extraction, and infrastructure of each human epoch.
</div>"""
    },
    {
        "number": 10,
        "title": "The Bronze Age Metallurgical Revolution",
        "category": "Historical Evolution",
        "category_slug": "history",
        "difficulty": "Fundamental",
        "statement": "<p>What metallurgical advantages did alloying copper with ~10 wt% tin offer over unalloyed native copper, launching the <strong>Bronze Age</strong> (~3000 BC)?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Solid Solution Strengthening & Castability</div>
  <ul>
    <li><strong>Lower Melting Point:</strong> Alloying 10 wt% Sn drops the melting temperature from 1084 &deg;C (pure Cu) to ~1000 &deg;C, significantly easing pyrotechnical smelting and casting.</li>
    <li><strong>Superior Fluidity:</strong> Molten bronze exhibits high fluidity, allowing detailed mold filling for weapons and tools.</li>
    <li><strong>Higher Hardness and Strength:</strong> Sn atoms cause substantial solid-solution lattice distortion, doubling the hardness and tensile strength of pure copper.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Key Advantages:</strong> Lower melting point, superior casting fluidity, and dramatic solid-solution strengthening over unalloyed copper.
</div>"""
    },
    {
        "number": 11,
        "title": "Thermodynamic Barrier: Bronze to Iron Transition",
        "category": "Historical Evolution",
        "category_slug": "history",
        "difficulty": "Intermediate",
        "statement": "<p>Pure copper melts at 1084 &deg;C, while pure iron melts at 1538 &deg;C. Explain why the <strong>Iron Age</strong> (~1200 BC) succeeded the Bronze Age by over a thousand years despite iron's vast geological abundance.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Pyrotechnological Temperature Limitation</div>
  <p>Ancient charcoal hearths with natural or primitive forced drafts could not exceed 1150&ndash;1200 &deg;C. While copper and bronze could be melted and cast liquid, iron (melting at 1538 &deg;C) remained completely solid.</p>
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Solid-State Bloomery Smelting Requirement</div>
  <p>Iron extraction required mastering solid-state reduction of iron ore in a <em>bloomery</em>, yielding a porous spongy solid ("bloom") contaminated with fayalite slag that required arduous thermomechanical forge welding to consolidate.</p>
</div>
<div class="final-answer-box">
  <strong>Primary Cause:</strong> The high melting point of iron ($1538 \\text{ &deg;C}$) exceeded kiln furnace capabilities, forcing a delay until solid-state bloomery smelting and carbon diffusion were invented.
</div>"""
    },
    {
        "number": 12,
        "title": "Ancient Solid-State Bloomery Smelting",
        "category": "Historical Evolution",
        "category_slug": "history",
        "difficulty": "Intermediate",
        "statement": "<p>Briefly describe the chemical reduction reaction in a solid-state bloomery furnace and explain how ancient blacksmiths converted the raw iron bloom into usable wrought iron.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Chemical Reduction</div>
  <p>Carbon monoxide gas ($CO$) generated from burning charcoal reduced solid iron oxide ore without melting the metal:</p>
  $$\\text{Fe}_2\\text{O}_3 + 3\\text{CO} \\rightarrow 2\\text{Fe (solid bloom)} + 3\\text{CO}_2$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Thermomechanical Consolidation</div>
  <p>The spongy solid bloom was reheated to ~1100 &deg;C and vigorously hammered (forged) on an anvil to squeeze out liquid silicate slag and weld the porous iron granules into dense wrought iron.</p>
</div>
<div class="final-answer-box">
  <strong>Summary:</strong> CO gas reduced iron ore in the solid state; repetitive hot forging squeezed out molten slag and consolidated the spongy bloom into wrought iron.
</div>"""
    },
    {
        "number": 13,
        "title": "Metallurgy of Ancient Damascus / Wootz Steel",
        "category": "Historical Evolution",
        "category_slug": "history",
        "difficulty": "Intermediate",
        "statement": "<p>What microstructural feature gave ancient <strong>Damascus blades</strong> (forged from Indian Wootz steel, ~1.5 wt% C) both razor-sharp cutting edges and high impact toughness?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Microstructural Banding</div>
  <p>Damascus steel consisted of macroscopic undulating bands of hard, brittle spheroidal cementite ($\\text{Fe}_3\\text{C}$) particles embedded within a tough, ductile tempered martensite or fine pearlite matrix.</p>
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Role of Trace Refractory Elements</div>
  <p>Trace elements (V, Mo) segregated during slow crucible solidification, pinning carbon and nucleating carbide bands during low-temperature forging cycles ($650 - 850 \\text{ &deg;C}$).</p>
</div>
<div class="final-answer-box">
  <strong>Key Microstructure:</strong> Ultra-hard cementite ($\text{Fe}_3\text{C}$) spheroids provided wear resistance and sharpness, while the ductile pearlitic/martensitic matrix prevented brittle fracture.
</div>"""
    },
    {
        "number": 14,
        "title": "The Bessemer Converter and Mass Steelmaking",
        "category": "Historical Evolution",
        "category_slug": "history",
        "difficulty": "Fundamental",
        "statement": "<p>How did Henry Bessemer's pneumatic converter (1856) revolutionize structural engineering, and what was the chemical mechanism involved?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Exothermic Decarburization</div>
  <p>Air was blown through molten pig iron (~4 wt% C). Oxygen reacted exothermically with excess carbon and silicon:</p>
  $$\\text{C} + \\frac{1}{2}\\text{O}_2 \\rightarrow \\text{CO (gas)} \\uparrow$$
  <p>The heat released kept the iron molten without extra fuel, dropping carbon content to $< 0.3 \\text{ wt%}$ in under 20 minutes.</p>
</div>
<div class="final-answer-box">
  <strong>Impact:</strong> Decreased steel production costs by over 80%, enabling mass production of structural steel for railways, bridges, and skyscrapers.
</div>"""
    },

    # -------------------------------------------------------------------------
    # TOPIC 3: CLASSES OF MATERIALS & BONDING (Problems 15 - 26)
    # -------------------------------------------------------------------------
    {
        "number": 15,
        "title": "The Four Primary Material Classes",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>List the four primary classes of solid engineering materials and identify the dominant interatomic bonding type for each.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Classification and Bonding</div>
  <ol>
    <li><strong>Metals:</strong> Metallic bonding (delocalized sea of valence electrons).</li>
    <li><strong>Ceramics:</strong> Ionic and/or covalent bonding (compounds of metals + non-metals).</li>
    <li><strong>Polymers:</strong> Covalent bonding along macromolecular backbones; secondary (van der Waals / hydrogen) bonds between chains.</li>
    <li><strong>Composites:</strong> Multiphase mixtures combining two or more distinct classes (e.g., ceramic fibers in a polymer matrix).</li>
  </ol>
</div>
<div class="final-answer-box">
  <strong>Summary:</strong> Metals (metallic), Ceramics (ionic/covalent), Polymers (covalent + secondary), Composites (macroscopic multi-phase combination).
</div>"""
    },
    {
        "number": 16,
        "title": "Metallic Bonding: The Electron Sea Model",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>Explain how the <strong>electron sea model</strong> accounts for two characteristic metallic properties: high electrical conductivity and high ductility.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Electrical Conductivity and Ductility</div>
  <ul>
    <li><strong>Electrical Conductivity:</strong> Valence electrons are completely delocalized and free to drift rapidly under an applied electric field without energetic barriers.</li>
    <li><strong>Ductility:</strong> Metallic bonding is non-directional. Atom planes can glide past one another under shear stress (dislocation motion) without disrupting electrostatic bonding cohesion.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Conclusion:</strong> Delocalized free electrons provide mobile charge carriers for electrical conduction and maintain cohesion during shear slip, enabling large plastic deformation.
</div>"""
    },
    {
        "number": 17,
        "title": "Ceramic Bonding and Low Room-Temperature Ductility",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>Why do strong ionic and covalent bonds make ceramics very stiff and wear-resistant, yet extremely brittle under tensile stress at room temperature?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Resistance to Dislocation Motion</div>
  <ul>
    <li><strong>High Stiffness / Hardness:</strong> High bonding energy ($E_0$) creates deep potential energy wells, requiring huge forces to stretch bonds.</li>
    <li><strong>Brittleness:</strong> In ionic crystals, shear slip brings like-charged ions into direct contact, causing catastrophic electrostatic repulsion. In covalent ceramics, bonds are highly directional. Hence, dislocation motion is virtually impossible at room temperature, causing crack propagation rather than yielding.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Core Cause:</strong> Highly directional covalent bonds and electrostatic repulsion of like ions severely restrict dislocation motion, preventing plastic blunting of crack tips.
</div>"""
    },
    {
        "number": 18,
        "title": "Polymers: Primary vs. Secondary Bonding",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>Explain the structural difference between <strong>primary intramolecular bonds</strong> and <strong>secondary intermolecular bonds</strong> in linear polyethylene.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Structural Comparison</div>
  <ul>
    <li><strong>Primary Bonds:</strong> Strong covalent $\\text{C}-\\text{C}$ and $\\text{C}-\\text{H}$ bonds along the chain backbone (bond energy $\\sim 350 - 400 \\text{ kJ/mol}$).</li>
    <li><strong>Secondary Bonds:</strong> Weak van der Waals forces between adjacent polymer chains (bond energy $\\sim 2 - 10 \\text{ kJ/mol}$).</li>
  </ul>
  <p>Under mechanical stress or heating, weak secondary bonds break easily, allowing chains to slide and uncoil, leading to low elastic modulus ($E \\sim 1 \\text{ GPa}$) and high elongation.</p>
</div>
<div class="final-answer-box">
  <strong>Key Distinction:</strong> Covalent backbone bonds ($~350 \\text{ kJ/mol}$) maintain chain integrity; weak van der Waals bonds ($~5 \\text{ kJ/mol}$) govern deformation and melting.
</div>"""
    },
    {
        "number": 19,
        "title": "Thermoplastics vs. Thermosetting Polymers",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>Contrast <strong>thermoplastics</strong> and <strong>thermosets</strong> regarding their molecular chain architecture and response to heating.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Architecture and Thermal Response</div>
  <ul>
    <li><strong>Thermoplastics (e.g., PE, PVC):</strong> Linear or branched chains held by weak secondary forces. They soften reversibly upon heating and solidify upon cooling, allowing easy thermal recycling.</li>
    <li><strong>Thermosets (e.g., Epoxy, Phenolic):</strong> Heavily cross-linked 3D networks with covalent bonds between all chains. They do not melt when heated; they degrade/char at high temperatures and cannot be remelted.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Summary:</strong> Thermoplastics have unlinked chains that melt and re-form reversibly; thermosets form cross-linked covalent networks that permanently degrade rather than melt.
</div>"""
    },
    {
        "number": 20,
        "title": "Elastomers and the Mechanism of Vulcanization",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Intermediate",
        "statement": "<p>What is <strong>vulcanization</strong> in rubber, and how does sulfur cross-linking prevent permanent plastic deformation under cyclic strain?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Cross-Linking Chemistry</div>
  <p>Natural raw rubber consists of tangled polyisoprene chains that slide irreversibly past one another under load (viscous flow). Heating rubber with sulfur atoms creates chemical sulfur bridge cross-links between chains.</p>
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Elastic Recovery Mechanism</div>
  <p>The cross-links act as molecular anchor points. When tension is released, conformational entropy pulls the uncoiled chains back to their original tangled state without permanent viscous slip.</p>
</div>
<div class="final-answer-box">
  <strong>Core Role:</strong> Sulfur cross-links tether adjacent polymer chains, eliminating permanent plastic slip and granting high, reversible elastic recovery ($> 500\\% \\text{ strain}$).
</div>"""
    },
    {
        "number": 21,
        "title": "Engineering Composite: Definition and Phases",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>Define an <strong>engineering composite</strong> and state the distinct roles of the <strong>continuous matrix phase</strong> and the <strong>dispersed reinforcing phase</strong>.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Roles of Matrix and Reinforcement</div>
  <ul>
    <li><strong>Reinforcing Phase (e.g., Carbon fibers):</strong> Carries the primary mechanical load, providing high tensile strength and elastic modulus.</li>
    <li><strong>Matrix Phase (e.g., Epoxy resin):</strong> Protects fibers from abrasion and moisture, binds them into geometry, transfers shear loads between fibers, and prevents fiber buckling.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Composite Synergy:</strong> Fibers provide load-carrying strength and stiffness; matrix transfers stress and provides environmental protection and toughness.
</div>"""
    },
    {
        "number": 22,
        "title": "Longitudinal Rule of Mixtures (Voigt Model)",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Intermediate",
        "statement": "<p>A continuous, aligned carbon-fiber-reinforced epoxy composite contains $V_f = 0.60$ volume fraction of carbon fibers ($E_f = 240 \\text{ GPa}$) in an epoxy matrix ($E_m = 3.5 \\text{ GPa}$). Calculate the longitudinal elastic modulus $E_{cl}$ using the isostrain Voigt model.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Governing Formula (Isostrain)</div>
  $$E_{cl} = V_f E_f + V_m E_m = V_f E_f + (1 - V_f) E_m$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Substitution and Calculation</div>
  $$E_{cl} = (0.60)(240 \\text{ GPa}) + (0.40)(3.5 \\text{ GPa})$$
  $$E_{cl} = 144 + 1.4 = 145.4 \\text{ GPa}$$
</div>
<div class="final-answer-box">
  <strong>Longitudinal Modulus:</strong> $E_{cl} = \\mathbf{145.4 \\text{ GPa}}$
</div>"""
    },
    {
        "number": 23,
        "title": "Transverse Rule of Mixtures (Reuss Model)",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Intermediate",
        "statement": "<p>Using the data from Problem 22 ($V_f = 0.60$, $E_f = 240 \\text{ GPa}$, $E_m = 3.5 \\text{ GPa}$), calculate the transverse elastic modulus $E_{ct}$ using the isostress Reuss model.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Governing Formula (Isostress)</div>
  $$\\frac{1}{E_{ct}} = \\frac{V_f}{E_f} + \\frac{V_m}{E_m} \\implies E_{ct} = \\frac{E_f E_m}{V_m E_f + V_f E_m}$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Calculation</div>
  $$\\frac{1}{E_{ct}} = \\frac{0.60}{240} + \\frac{0.40}{3.5} = 0.0025 + 0.1143 = 0.1168 \\text{ GPa}^{-1}$$
  $$E_{ct} = \\frac{1}{0.1168} = 8.56 \\text{ GPa}$$
</div>
<div class="final-answer-box">
  <strong>Transverse Modulus:</strong> $E_{ct} = \\mathbf{8.56 \\text{ GPa}}$ (heavily dominated by the compliant matrix).
</div>"""
    },
    {
        "number": 24,
        "title": "Critical Fiber Length Calculation",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Intermediate",
        "statement": "<p>Glass fibers have a tensile strength $\\sigma_f^* = 2.0 \\text{ GPa}$ and diameter $d = 12 \\,\\mu\\text{m}$. If the fiber-matrix shear yield strength is $\\tau_c = 25 \\text{ MPa}$, calculate the critical fiber length $l_c$ required for effective reinforcement.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Critical Length Formula</div>
  $$l_c = \\frac{\\sigma_f^* \\cdot d}{2 \\tau_c}$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Computation</div>
  $$l_c = \\frac{(2000 \\text{ MPa})(12 \\times 10^{-6} \\text{ m})}{2 \\times 25 \\text{ MPa}} = \\frac{0.024}{50} = 4.8 \\times 10^{-4} \\text{ m} = 0.48 \\text{ mm}$$
</div>
<div class="final-answer-box">
  <strong>Critical Length:</strong> $l_c = \\mathbf{0.48 \\text{ mm}}$ (fibers must exceed $l_c$ to reach their ultimate tensile strength).
</div>"""
    },
    {
        "number": 25,
        "title": "Specific Strength and Specific Modulus",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>Define <strong>specific strength</strong> and <strong>specific modulus</strong>, and explain why carbon-fiber composites (CFRP) are preferred over structural steel in aerospace fuselages.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Definitions</div>
  $$\\text{Specific Modulus} = \\frac{E}{\\rho}, \\quad \\text{Specific Strength} = \\frac{\\sigma_y}{\\rho}$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Comparison (Steel vs CFRP)</div>
  <p>Steel has high $E = 207 \\text{ GPa}$ but high density $\\rho = 7.85 \\text{ g/cm}^3$ (ratio $\\approx 26$). CFRP has $E = 150 \\text{ GPa}$ and low $\\rho = 1.55 \\text{ g/cm}^3$ (ratio $\\approx 97$). CFRP delivers nearly $4\\times$ the stiffness per unit mass, minimizing aircraft weight and fuel burn.</p>
</div>
<div class="final-answer-box">
  <strong>Conclusion:</strong> High specific properties ($E/\\rho$ and $\\sigma_y/\\rho$) allow dramatic structural mass reductions while preserving structural stiffness and strength.
</div>"""
    },
    {
        "number": 26,
        "title": "CFRP vs. GFRP Engineering Trade-Offs",
        "category": "Material Classes",
        "category_slug": "classes",
        "difficulty": "Fundamental",
        "statement": "<p>Compare <strong>Carbon Fiber Reinforced Polymer (CFRP)</strong> and <strong>Glass Fiber Reinforced Polymer (GFRP)</strong> in terms of stiffness, cost, and impact energy absorption.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Comparative Trade-Offs</div>
  <ul>
    <li><strong>Stiffness:</strong> CFRP ($E \\sim 140 - 230 \\text{ GPa}$) is substantially stiffer than GFRP ($E \\sim 35 - 45 \\text{ GPa}$).</li>
    <li><strong>Raw Material Cost:</strong> Carbon fibers are $5 - 10\\times$ more expensive than E-glass fibers.</li>
    <li><strong>Impact Tolerance:</strong> Glass fibers have higher failure strain ($3 - 4\\%$) than carbon fibers ($1 - 1.5\\%$), offering higher impact energy absorption and damage tolerance before fracture.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Trade-off:</strong> CFRP provides maximum specific stiffness for aerospace; GFRP offers lower cost and higher impact tolerance for boats and wind turbine blades.
</div>"""
    },

    # -------------------------------------------------------------------------
    # TOPIC 4: ADVANCED & FUNCTIONAL MATERIALS (Problems 27 - 36)
    # -------------------------------------------------------------------------
    {
        "number": 27,
        "title": "Band Gap Theory: Metals, Semiconductors, and Insulators",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Fundamental",
        "statement": "<p>Define the <strong>energy band gap</strong> ($E_g$) and state its typical magnitude for electrical conductors, semiconductors, and insulators at room temperature.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Definition and Magnitudes</div>
  <p>The band gap $E_g$ is the forbidden energy interval separating the filled valence band from the empty conduction band.</p>
  <ul>
    <li><strong>Metals (Conductors):</strong> $E_g = 0 \\text{ eV}$ (valence and conduction bands overlap or band is partially filled).</li>
    <li><strong>Semiconductors:</strong> $0 < E_g \\le 2.5 \\text{ eV}$ (e.g., Silicon: $E_g = 1.1 \\text{ eV}$, GaAs: $E_g = 1.42 \\text{ eV}$).</li>
    <li><strong>Insulators:</strong> $E_g > 3.0 \\text{ eV}$ (e.g., Diamond: $E_g = 5.5 \\text{ eV}$, Alumina: $E_g \\approx 8.8 \\text{ eV}$).</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Key Ranges:</strong> Metals ($E_g = 0$), Semiconductors ($E_g \\sim 1 - 2 \\text{ eV}$), Insulators ($E_g > 3 \\text{ eV}$).
</div>"""
    },
    {
        "number": 28,
        "title": "Extrinsic Doping of Silicon: n-type vs. p-type",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Intermediate",
        "statement": "<p>Explain how doping pure tetravalent silicon ($Si$) with phosphorus ($P$, group V) creates an <strong>n-type</strong> semiconductor, whereas doping with boron ($B$, group III) creates a <strong>p-type</strong> semiconductor.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Donor vs. Acceptor Physics</div>
  <ul>
    <li><strong>n-type Doping (Phosphorus, 5 valence $e^-$):</strong> Four electrons form covalent bonds with adjacent Si atoms; the 5th electron is loosely bound in a donor state just below the conduction band and easily ionizes into the conduction band at room temperature (majority carriers: <em>electrons</em>).</li>
    <li><strong>p-type Doping (Boron, 3 valence $e^-$):</strong> Forms only 3 covalent bonds, leaving one vacant bond state (acceptor level just above the valence band) that readily accepts an electron from the valence band, creating a mobile <em>hole</em> (majority carriers: <em>holes</em>).</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Summary:</strong> Group V dopants supply conduction electrons (n-type); Group III dopants generate valence band holes (p-type).
</div>"""
    },
    {
        "number": 29,
        "title": "Temperature Dependence of Electrical Resistivity",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Fundamental",
        "statement": "<p>Why does electrical resistivity <strong>increase</strong> with temperature in pure metals, but <strong>decrease exponentially</strong> in intrinsic semiconductors?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Carrier Density vs. Mobility Mechanisms</div>
  <ul>
    <li><strong>Metals:</strong> Carrier density $n$ is constant. Rising temperature increases lattice thermal vibrations (phonons), increasing electron scattering and lowering mobility $\\mu_e$ ($\\rho$ rises linearly).</li>
    <li><strong>Semiconductors:</strong> Thermal energy excites valence electrons across the band gap: $n_i \\propto \\exp(-E_g / 2kT)$. This exponential surge in free electron-hole pairs overwhelms phonon scattering, causing resistivity to drop sharply.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Key Difference:</strong> In metals, phonon scattering dominates (resistivity rises); in semiconductors, thermal carrier generation dominates (resistivity drops exponentially).
</div>"""
    },
    {
        "number": 30,
        "title": "Biocompatibility and Orthopedic Titanium Alloys",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Fundamental",
        "statement": "<p>Define <strong>biocompatibility</strong> and state two material properties that make $\\text{Ti}-6\\text{Al}-4\\text{V}$ the gold standard for load-bearing orthopedic implants.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Definition and Properties</div>
  <ul>
    <li><strong>Biocompatibility:</strong> The ability of a synthetic material to perform with an appropriate host response without eliciting toxic, allergic, or immunological reactions.</li>
    <li><strong>Passivating Oxide Layer:</strong> Spontaneous formation of a dense, adherent $\\text{TiO}_2$ passive film provides exceptional resistance to physiological saline corrosion.</li>
    <li><strong>Osseointegration & Modulus:</strong> Direct bone adhesion (osseointegration) and relatively low elastic modulus ($E \\approx 110 \\text{ GPa}$, half that of stainless steel) reduces bone stress shielding.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Conclusion:</strong> Robust inert passivity ($\\text{TiO}_2$), excellent osseointegration, and low elastic modulus make titanium ideal for joint prostheses.
</div>"""
    },
    {
        "number": 31,
        "title": "Ceramic Biomaterials: Hydroxyapatite Coatings",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Intermediate",
        "statement": "<p>Why is synthetic <strong>hydroxyapatite</strong> ($\\text{Ca}_{10}(\\text{PO}_4)_6(\\text{OH})_2$) applied as a plasma-sprayed coating on metallic hip stems rather than being used as a bulk structural femoral stem?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Biological and Mechanical Trade-Offs</div>
  <ul>
    <li><strong>Bioactive Surface:</strong> Hydroxyapatite is chemically identical to natural bone mineral. It stimulates osteoblast attachment and bone ingrowth directly into the implant surface.</li>
    <li><strong>Bulk Mechanical Inadequacy:</strong> As a bulk ceramic, hydroxyapatite has low fracture toughness ($K_{Ic} \\sim 1.0 \\text{ MPa}\\sqrt{\\text{m}}$) and low bending strength. A bulk ceramic stem would suffer catastrophic brittle fracture under cyclical body loads.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Strategic Synergy:</strong> The metallic stem carries high structural cyclic bending loads, while the thin hydroxyapatite coating accelerates biological bone fixation.
</div>"""
    },
    {
        "number": 32,
        "title": "Shape Memory Effect in Nitinol (NiTi)",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Intermediate",
        "statement": "<p>Explain the physical mechanism of the <strong>thermal shape memory effect</strong> in equiatomic Nitinol ($\\text{NiTi}$) alloys.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Martensite-Austenite Reversible Transformation</div>
  <ol>
    <li>At high temperature, Nitinol exists in the parent cubic <strong>austenite</strong> phase.</li>
    <li>Cooling below $M_f$ transforms it into twinned monoclinic <strong>martensite</strong> without macroscopic shape change.</li>
    <li>Deforming the material at room temperature detwins the martensite variants, accommodating up to ~8% strain.</li>
    <li>Reheating above $A_f$ triggers a reverse diffusionless transformation back to the parent cubic austenite, perfectly restoring the original pre-deformed shape.</li>
  </ol>
</div>
<div class="final-answer-box">
  <strong>Mechanism:</strong> Diffusionless, crystallographically reversible phase transformation between low-temperature detwinned martensite and high-temperature cubic austenite.
</div>"""
    },
    {
        "number": 33,
        "title": "Superelasticity in Nitinol Stents",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Intermediate",
        "statement": "<p>How does <strong>superelasticity (pseudoelasticity)</strong> allow self-expanding cardiovascular Nitinol stents to recover large strains ($> 8\\%$) at constant human body temperature ($37 \\text{ &deg;C}$)?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Stress-Induced Martensite (SIM)</div>
  <p>At body temperature ($T > A_f$), the alloy is fully austenitic. Mechanical crimping into a catheter applies stress that thermodynamically induces the formation of <strong>stress-induced martensite (SIM)</strong>, absorbing large strains.</p>
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Elastic Recovery Upon Deployment</div>
  <p>Upon ejection into the artery, the constraining stress is removed. The unstable martensite immediately transforms back to parent austenite, exerting a gentle, constant outward radial force against the vessel wall.</p>
</div>
<div class="final-answer-box">
  <strong>Summary:</strong> Mechanical stress induces martensite during crimping; releasing stress triggers immediate reversion to austenite, restoring shape at constant body temperature.
</div>"""
    },
    {
        "number": 34,
        "title": "The Piezoelectric Effect in PZT Ceramics",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Fundamental",
        "statement": "<p>Explain the direct and converse <strong>piezoelectric effect</strong> in Lead Zirconate Titanate ($\\text{Pb}[\\text{Zr}_x\\text{Ti}_{1-x}]\\text{O}_3$, PZT) and give one practical engineering application of each.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Direct vs. Converse Effect</div>
  <ul>
    <li><strong>Direct Effect:</strong> Applying mechanical stress shifts non-centrosymmetric ions in the perovskite crystal lattice, generating a macroscopic electrical polarization / voltage (Application: vibration sensors, spark igniters, accelerometers).</li>
    <li><strong>Converse Effect:</strong> Applying an external electric field displaces ions in the unit cell, inducing a precise mechanical strain / dimensional change (Application: ultrasonic medical transducers, nanopositioning actuators).</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Duality:</strong> Direct effect: $\\text{Mechanical Stress} \\rightarrow \\text{Voltage}$; Converse effect: $\\text{Electric Field} \\rightarrow \\text{Mechanical Displacement}$.
</div>"""
    },
    {
        "number": 35,
        "title": "Nanomaterials: Surface-to-Volume Ratio",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Fundamental",
        "statement": "<p>Why do physical, chemical, and catalytic properties of materials change drastically when particle dimensions shrink below $100 \\text{ nm}$?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Two Dominant Nanoscale Phenomena</div>
  <ul>
    <li><strong>Enormous Surface-to-Volume Ratio ($A/V \\propto 1/r$):</strong> A significant fraction of all atoms reside on the surface with unsatisfied, dangling bonds, drastically increasing chemical reactivity and lowering melting temperatures.</li>
    <li><strong>Quantum Confinement Effects:</strong> When particle size becomes comparable to the de Broglie wavelength of electrons, continuous electronic energy bands split into discrete quantum energy levels, shifting optical absorption and emission spectra.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Core Drivers:</strong> High surface atom fraction (enhanced chemical reactivity) and quantum confinement (tunable electronic and optical band states).
</div>"""
    },
    {
        "number": 36,
        "title": "Carbon Nanotubes and Graphene",
        "category": "Advanced Materials",
        "category_slug": "advanced",
        "difficulty": "Intermediate",
        "statement": "<p>Describe the atomic structure of <strong>graphene</strong> and a <strong>single-walled carbon nanotube (SWCNT)</strong> and compare their theoretical tensile strength to high-strength structural steel.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Structure and Strength</div>
  <ul>
    <li><strong>Graphene:</strong> A single 2D layer of carbon atoms packed in a hexagonal honeycomb lattice with strong $sp^2$ covalent bonds.</li>
    <li><strong>SWCNT:</strong> A seamless cylinder formed by rolling a single graphene sheet into a nanoscale tube.</li>
    <li><strong>Tensile Strength:</strong> Carbon nanotubes have a theoretical strength of $\\approx 100 - 130 \\text{ GPa}$, nearly $100\\times$ higher than high-strength steel (~1.5 GPa), with only one-sixth the density.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Comparison:</strong> Carbon nanotubes possess theoretical tensile strength over $100 \\text{ GPa}$ with density $\\sim 1.3 \\text{ g/cm}^3$, representing the highest specific strength of any known structural material.
</div>"""
    },

    # -------------------------------------------------------------------------
    # TOPIC 5: ASHBY CHARTS & PERFORMANCE INDICES (Problems 37 - 45)
    # -------------------------------------------------------------------------
    {
        "number": 37,
        "title": "Principles of Ashby Property Charts",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Fundamental",
        "statement": "<p>What is an <strong>Ashby materials selection chart</strong>, and why are material property pairs (e.g., Young's modulus $E$ vs. density $\\rho$) typically plotted on logarithmic axes?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Rationale for Log-Log Plots</div>
  <ul>
    <li><strong>Vast Property Range:</strong> Engineering properties span multiple orders of magnitude ($E$ spans from $10^{-3} \\text{ GPa}$ for foams to $10^3 \\text{ GPa}$ for diamond). Log scales condense this spectrum onto a single diagram.</li>
    <li><strong>Linear Guide Lines:</strong> Performance metrics in power-law form ($M = E^{1/2}/\\rho$) transform into straight lines of slope $1, 2,$ or $3$ on log-log plots, allowing rapid graphical screening.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Purpose:</strong> Logarithmic Ashby charts display broad material classes and convert complex optimization equations into linear selection guide lines.
</div>"""
    },
    {
        "number": 38,
        "title": "Derivation: Lightweight Tension Tie-Rod",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>A structural tie-rod of length $L$ must support an axial tensile force $F$ without yielding. Derive the material performance index $M_1$ that must be <strong>maximized</strong> to minimize the mass of the tie-rod.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Objective Function and Constraint</div>
  $$\\text{Mass: } m = A \\cdot L \\cdot \\rho$$
  $$\\text{Constraint (No Yielding): } \\sigma = \\frac{F}{A} \\le \\sigma_y \\implies A = \\frac{F}{\\sigma_y}$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Elimination of Free Variable ($A$)</div>
  $$m = \\left(\\frac{F}{\\sigma_y}\\right) L \\cdot \\rho = (F \\cdot L) \\left(\\frac{\\rho}{\\sigma_y}\\right)$$
  <p>To minimize mass $m$, we must minimize $\\rho / \\sigma_y$, which is equivalent to maximizing its inverse.</p>
</div>
<div class="final-answer-box">
  <strong>Derived Performance Index:</strong> $$M_1 = \\frac{\\sigma_y}{\\rho}$$ (Maximize specific yield strength).
</div>"""
    },
    {
        "number": 39,
        "title": "Tie-Rod Selection: Steel vs. Aluminum 7075-T6",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>Using the index $M = \\sigma_y / \\rho$, evaluate whether <strong>structural steel</strong> ($\\sigma_y = 400 \\text{ MPa}$, $\\rho = 7850 \\text{ kg/m}^3$) or <strong>aluminum 7075-T6</strong> ($\\sigma_y = 500 \\text{ MPa}$, $\\rho = 2800 \\text{ kg/m}^3$) produces a lighter tie-rod for the same load, and calculate the percentage mass savings.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Compute Performance Index for Both Materials</div>
  $$M_{\\text{steel}} = \\frac{400 \\times 10^6 \\text{ Pa}}{7850 \\text{ kg/m}^3} = 50,955 \\text{ J/kg} = 51.0 \\text{ kJ/kg}$$
  $$M_{\\text{Al}} = \\frac{500 \\times 10^6 \\text{ Pa}}{2800 \\text{ kg/m}^3} = 178,571 \\text{ J/kg} = 178.6 \\text{ kJ/kg}$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Mass Ratio and Percentage Savings</div>
  $$\\frac{m_{\\text{Al}}}{m_{\\text{steel}}} = \\frac{M_{\\text{steel}}}{M_{\\text{Al}}} = \\frac{51.0}{178.6} \\approx 0.285$$
  $$\\text{Mass Savings} = (1 - 0.285) \\times 100\\% = 71.5\\%$$
</div>
<div class="final-answer-box">
  <strong>Selection:</strong> Aluminum 7075-T6 provides $\\mathbf{71.5\\%}$ mass reduction compared to steel for identical tensile load capacity.
</div>"""
    },
    {
        "number": 40,
        "title": "Derivation: Lightweight Stiff Beam in Bending",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>A simply supported beam of span $L$ and square cross-section $b \\times b$ must not deflect more than $\\delta$ under a central load $F$. Derive the performance index $M_2$ to be maximized for minimum mass.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Governing Relations</div>
  $$\\text{Mass: } m = b^2 L \\rho, \\quad \\text{Deflection: } \\delta = \\frac{F L^3}{48 E I}, \\quad I = \\frac{b^4}{12}$$
  $$b^2 = \\left(\\frac{F L^3}{4 E \\delta}\\right)^{1/2}$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Mass Formulation and Index Extraction</div>
  $$m = \\left(\\frac{F L^3}{4 \\delta}\\right)^{1/2} L \\left(\\frac{\\rho}{E^{1/2}}\\right)$$
  <p>To minimize mass, we maximize the inverse material grouping.</p>
</div>
<div class="final-answer-box">
  <strong>Derived Performance Index:</strong> $$M_2 = \\frac{E^{1/2}}{\\rho}$$
</div>"""
    },
    {
        "number": 41,
        "title": "Derivation: Lightweight Strong Beam in Bending",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>A beam of span $L$ and square cross-section $b \\times b$ must carry a bending moment $M_b$ without exceeding its yield strength $\\sigma_y$. Derive the performance index $M_3$ to be maximized for minimum beam weight.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Bending Stress and Area Elimination</div>
  $$\\sigma = \\frac{M_b y}{I} = \\frac{M_b (b/2)}{b^4/12} = \\frac{6 M_b}{b^3} \\le \\sigma_y \\implies b = \\left(\\frac{6 M_b}{\\sigma_y}\\right)^{1/3}$$
  $$\\text{Cross-sectional Area: } A = b^2 = \\left(\\frac{6 M_b}{\\sigma_y}\\right)^{2/3}$$
</div>
<div class="solution-step">
  <div class="solution-step-title">Step 2: Total Mass Formulation</div>
  $$m = A L \\rho = (6 M_b)^{2/3} L \\left(\\frac{\\rho}{\\sigma_y^{2/3}}\\right)$$
</div>
<div class="final-answer-box">
  <strong>Derived Performance Index:</strong> $$M_3 = \\frac{\\sigma_y^{2/3}}{\\rho}$$
</div>"""
    },
    {
        "number": 42,
        "title": "Derivation: Lightweight Stiff Plate / Panel",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>A flat panel of fixed width $W$ and length $L$ must resist bending deflection with thickness $t$ as the free variable. Derive the performance index $M_4$ to be maximized for minimum plate mass.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Plate Bending Stiffness</div>
  $$\\text{Bending Stiffness: } S \\propto E t^3 \\implies t \\propto \\left(\\frac{S}{E}\\right)^{1/3}$$
  $$\\text{Plate Mass: } m = W L t \\rho \\propto (W L) S^{1/3} \\left(\\frac{\\rho}{E^{1/3}}\\right)$$
</div>
<div class="final-answer-box">
  <strong>Derived Performance Index:</strong> $$M_4 = \\frac{E^{1/3}}{\\rho}$$
</div>"""
    },
    {
        "number": 43,
        "title": "Performance Index for High-Energy Elastic Springs",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>Derive the material performance index $M$ to be maximized for an elastic spring designed to store the maximum strain energy per unit volume without yielding.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Volumetric Strain Energy (Modulus of Resilience)</div>
  <p>The elastic strain energy stored per unit volume up to yielding is the modulus of resilience $U_r$:</p>
  $$U_r = \\int_0^{\\varepsilon_y} \\sigma \\, d\\varepsilon = \\frac{1}{2} \\sigma_y \\varepsilon_y = \\frac{1}{2} \\frac{\\sigma_y^2}{E}$$
</div>
<div class="final-answer-box">
  <strong>Spring Performance Index:</strong> $$M = \\frac{\\sigma_y^2}{E}$$ (Materials with high yield strength and low modulus, such as spring steels and titanium, store the most energy).
</div>"""
    },
    {
        "number": 44,
        "title": "Thermal Shock Resistance Parameter (R)",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>State the formula for the <strong>thermal shock resistance parameter</strong> $R$ of brittle ceramics subjected to rapid quenching and explain the role of each material property.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Parameter Definition and Property Roles</div>
  $$R = \\frac{\\sigma_f \\cdot k}{E \\cdot \\alpha_L}$$
  <ul>
    <li>$\\sigma_f$: Fracture strength (high strength resists thermal stress).</li>
    <li>$k$: Thermal conductivity (high $k$ dissipates heat fast, minimizing thermal gradients).</li>
    <li>$E$: Young's modulus (low $E$ generates lower stress for a given thermal strain).</li>
    <li>$\\alpha_L$: Thermal expansion coefficient (low $\\alpha_L$ minimizes thermal contraction strains).</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Formula:</strong> $R = \\frac{\\sigma_f k}{E \\alpha_L}$. High strength and conductivity combined with low modulus and low thermal expansion maximize thermal shock survival.
</div>"""
    },
    {
        "number": 45,
        "title": "Interpreting Guide Line Slopes on Ashby Charts",
        "category": "Materials Selection",
        "category_slug": "ashby",
        "difficulty": "Intermediate",
        "statement": "<p>On a $\\log(E)$ vs. $\\log(\\rho)$ Ashby chart, what geometric slopes correspond to the selection lines for: (a) a light tie-rod ($M = E/\\rho$), (b) a light beam ($M = E^{1/2}/\\rho$), and (c) a light plate ($M = E^{1/3}/\\rho$)?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Logarithmic Slope Derivation</div>
  <ul>
    <li>(a) $\\log(E) = \\log(\\rho) + \\log(M) \\implies$ <strong>Slope = 1</strong> (Tension tie-rod).</li>
    <li>(b) $\\frac{1}{2}\\log(E) = \\log(\\rho) + \\log(M) \\implies \\log(E) = 2\\log(\\rho) + 2\\log(M) \\implies$ <strong>Slope = 2</strong> (Bending beam).</li>
    <li>(c) $\\frac{1}{3}\\log(E) = \\log(\\rho) + \\log(M) \\implies \\log(E) = 3\\log(\\rho) + 3\\log(M) \\implies$ <strong>Slope = 3</strong> (Bending plate/panel).</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Slopes:</strong> Tie-rod = <strong>1</strong>; Beam in bending = <strong>2</strong>; Plate in bending = <strong>3</strong>.
</div>"""
    },

    # -------------------------------------------------------------------------
    # TOPIC 6: ECONOMICS, ENVIRONMENT & SUSTAINABILITY (Problems 46 - 50)
    # -------------------------------------------------------------------------
    {
        "number": 46,
        "title": "Cost-Weighted Performance Index",
        "category": "Economics & Environment",
        "category_slug": "sustainability",
        "difficulty": "Intermediate",
        "statement": "<p>In commercial mass production, minimum weight must be balanced against cost. How is the tie-rod performance index $M_1 = \\sigma_y / \\rho$ modified when the design objective is <strong>minimum component cost</strong> rather than minimum weight?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Cost Objective Function</div>
  <p>Let $C_m$ be the price per unit mass (\\$/kg). The total material cost is:</p>
  $$C_{\\text{total}} = m \\cdot C_m = (A \\cdot L \\cdot \\rho) \\cdot C_m$$
  <p>Substituting $A = F / \\sigma_y$ gives:</p>
  $$C_{\\text{total}} = (F \\cdot L) \\left(\\frac{C_m \\rho}{\\sigma_y}\\right)$$
</div>
<div class="final-answer-box">
  <strong>Cost Performance Index:</strong> $$M_{\\text{cost}} = \\frac{\\sigma_y}{C_m \\rho}$$ (Maximize strength per dollar of material).
</div>"""
    },
    {
        "number": 47,
        "title": "Embodied Energy: Primary vs. Recycled Aluminum",
        "category": "Economics & Environment",
        "category_slug": "sustainability",
        "difficulty": "Fundamental",
        "statement": "<p>Compare the <strong>embodied energy</strong> required to produce primary virgin aluminum from bauxite ore (~$200 \\text{ MJ/kg}$) versus remelting recycled scrap aluminum (~$15 \\text{ MJ/kg}$), and compute the energy savings percentage.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Energy Analysis</div>
  <ul>
    <li><strong>Virgin Production (Hall-H&eacute;roult process):</strong> Extremely energy-intensive electrolytic reduction of alumina ($\\text{Al}_2\\text{O}_3$) requires $\\sim 200 \\text{ MJ/kg}$.</li>
    <li><strong>Recycled Production:</strong> Simple remelting requires only the latent heat of fusion plus superheat, consuming $\\sim 15 \\text{ MJ/kg}$.</li>
  </ul>
  $$\\text{Energy Savings} = \\frac{200 - 15}{200} \\times 100\\% = 92.5\\%$$
</div>
<div class="final-answer-box">
  <strong>Savings:</strong> Recycling aluminum saves $\\mathbf{92.5\\%}$ of the energy required for virgin smelting, demonstrating the power of metallurgical circularity.
</div>"""
    },
    {
        "number": 48,
        "title": "Recyclability: Thermoplastics vs. Thermosets vs. Composites",
        "category": "Economics & Environment",
        "category_slug": "sustainability",
        "difficulty": "Fundamental",
        "statement": "<p>Why can <strong>thermoplastics</strong> be easily mechanically recycled by remelting, while <strong>thermosets</strong> and <strong>carbon fiber composites (CFRP)</strong> present severe recycling bottlenecks?</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Molecular Architecture and Recycling</div>
  <ul>
    <li><strong>Thermoplastics:</strong> Linear chains are held by weak secondary bonds. They can be repeatedly melted, extruded, and remolded into new shapes without breaking covalent backbones.</li>
    <li><strong>Thermosets & CFRP:</strong> The polymer matrix is an irreversible, permanently cross-linked 3D covalent network that cannot be melted. Recycling CFRP requires high-temperature pyrolysis or chemical solvolysis to burn or dissolve the matrix, which degrades fiber length and strength.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Recyclability Contrast:</strong> Thermoplastics melt reversibly; cross-linked thermosets cannot melt and require destructive chemical or thermal processes to reclaim fibers.
</div>"""
    },
    {
        "number": 49,
        "title": "Critical Raw Materials in Clean Energy",
        "category": "Economics & Environment",
        "category_slug": "sustainability",
        "difficulty": "Fundamental",
        "statement": "<p>Define what constitutes a <strong>critical raw material</strong> and explain why <strong>Neodymium (Nd)</strong> and <strong>Cobalt (Co)</strong> are classified as critical in modern electric vehicle technologies.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Criteria for Criticality</div>
  <p>A material is classified as critical if it combines <strong>high economic/technological importance</strong> with <strong>high supply disruption risk</strong> (due to geographic concentration of extraction or processing).</p>
  <ul>
    <li><strong>Neodymium (Nd):</strong> Essential for high-flux permanent magnets (NdFeB) in EV traction motors and wind turbines; mining and refining are heavily concentrated geographically.</li>
    <li><strong>Cobalt (Co):</strong> Critical for thermal stability in high-energy Li-ion battery cathodes (NMC); majority extraction is concentrated in politically volatile regions.</li>
  </ul>
</div>
<div class="final-answer-box">
  <strong>Definition:</strong> Critical materials combine high technological indispensability with severe geopolitical supply risk.
</div>"""
    },
    {
        "number": 50,
        "title": "The Four Stages of Life-Cycle Assessment (LCA)",
        "category": "Economics & Environment",
        "category_slug": "sustainability",
        "difficulty": "Fundamental",
        "statement": "<p>Name the four primary lifecycle phases analyzed in a formal engineering <strong>Life-Cycle Assessment (LCA)</strong> for materials selection.</p>",
        "solution": """<div class="solution-step">
  <div class="solution-step-title">Step 1: Four Comprehensive Stages</div>
  <ol>
    <li><strong>Raw Material Extraction:</strong> Mining of ores, petroleum extraction, energy consumption, and environmental habitat disruption.</li>
    <li><strong>Manufacturing & Synthesis:</strong> Refining, alloying, shaping, machining, and component assembly emissions.</li>
    <li><strong>Service Use:</strong> Operating efficiency, fuel consumption (influenced by lightweighting), maintenance, and corrosion durability over component life.</li>
    <li><strong>End-of-Life (EOL):</strong> Disassembly, remanufacturing, recycling efficiency, or landfill degradation.</li>
  </ol>
</div>
<div class="final-answer-box">
  <strong>The 4 LCA Stages:</strong> $\\text{Extraction} \\rightarrow \\text{Manufacturing} \\rightarrow \\text{Service Use} \\rightarrow \\text{End-of-Life (Recycling/Disposal)}$.
</div>"""
    }
]

def generate():
    out_path = os.path.join(os.path.dirname(__file__), "ch1_data.py")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# generator/ch1_data.py\n")
        f.write("# ==============================================================================\n")
        f.write("# CHAPTER 1: INTRODUCTION TO MATERIALS SCIENCE & ENGINEERING\n")
        f.write("# 50 Curated Concise Problems with Step-by-Step Solutions\n")
        f.write("# University of Tehran | Dept. of Mechanical Engineering | Prof. Sadeghi\n")
        f.write("# Prepared by: Sina Sharifi (TA)\n")
        f.write("# ==============================================================================\n\n")
        f.write("PROBLEMS = [\n")
        for p in problems:
            f.write("  {\n")
            f.write(f'    "number": {p["number"]},\n')
            f.write(f'    "title": {repr(p["title"])},\n')
            f.write(f'    "category": {repr(p["category"])},\n')
            f.write(f'    "category_slug": {repr(p["category_slug"])},\n')
            f.write(f'    "difficulty": {repr(p["difficulty"])},\n')
            f.write(f'    "statement": {repr(p["statement"])},\n')
            f.write(f'    "solution": {repr(p["solution"])}\n')
            f.write("  },\n")
        f.write("]\n")
    print(f"Generated {out_path} with {len(problems)} concise problems.")

if __name__ == "__main__":
    generate()
