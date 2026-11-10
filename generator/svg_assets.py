# ==============================================================================
# SCIENCE OF MATERIALS — MIDTERM STUDY SUITE GENERATOR
# High-Resolution Technical Vector SVGs (Dark Blue & Gold Academic Theme)
# ==============================================================================

def svg_tetrahedron():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="nodeGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#f5d061" stop-opacity="0.8"/>
          <stop offset="100%" stop-color="#1e3a8a" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="edgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#d4af37"/>
          <stop offset="100%" stop-color="#38bdf8"/>
        </linearGradient>
      </defs>
      <!-- Background subtle grid -->
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Outer Tetrahedron Edges -->
      <line x1="225" y1="40" x2="80" y2="240" stroke="url(#edgeGrad)" stroke-width="2.5"/>
      <line x1="225" y1="40" x2="370" y2="240" stroke="url(#edgeGrad)" stroke-width="2.5"/>
      <line x1="80" y1="240" x2="370" y2="240" stroke="url(#edgeGrad)" stroke-width="2.5"/>
      <!-- Internal Centroid Edges -->
      <line x1="225" y1="40" x2="225" y2="165" stroke="#d4af37" stroke-width="2" stroke-dasharray="4 3"/>
      <line x1="80" y1="240" x2="225" y2="165" stroke="#d4af37" stroke-width="2" stroke-dasharray="4 3"/>
      <line x1="370" y1="240" x2="225" y2="165" stroke="#d4af37" stroke-width="2" stroke-dasharray="4 3"/>
      
      <!-- Central Core Pulse -->
      <circle cx="225" cy="165" r="28" fill="#172554" stroke="#d4af37" stroke-width="1.5"/>
      <text x="225" y="162" fill="#d4af37" font-family="'Cinzel', Georgia, serif" font-size="11" font-weight="bold" text-anchor="middle">MSE</text>
      <text x="225" y="176" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">PARADIGM</text>

      <!-- Vertex 1: Processing / Synthesis -->
      <circle cx="225" cy="40" r="22" fill="#101c3d" stroke="#d4af37" stroke-width="2"/>
      <text x="225" y="44" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Processing</text>
      <text x="225" y="16" fill="#d4af37" font-family="sans-serif" font-size="9" text-anchor="middle">Synthesis & Heat Treat</text>

      <!-- Vertex 2: Structure -->
      <circle cx="80" cy="240" r="22" fill="#101c3d" stroke="#38bdf8" stroke-width="2"/>
      <text x="80" y="244" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Structure</text>
      <text x="80" y="275" fill="#38bdf8" font-family="sans-serif" font-size="9" text-anchor="middle">Atomic to Micro</text>

      <!-- Vertex 3: Properties -->
      <circle cx="370" cy="240" r="22" fill="#101c3d" stroke="#34d399" stroke-width="2"/>
      <text x="370" y="244" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Properties</text>
      <text x="370" y="275" fill="#34d399" font-family="sans-serif" font-size="9" text-anchor="middle">Mech / Elec / Therm</text>

      <!-- Top Title -->
      <text x="225" y="302" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="500" text-anchor="middle">Interconnected Materials Science & Engineering Tetrahedron</text>
    </svg>
    """

def svg_ashby_chart():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Grid lines -->
      <line x1="60" y1="40" x2="60" y2="260" stroke="#1e293b" stroke-width="1.5"/>
      <line x1="60" y1="260" x2="410" y2="260" stroke="#1e293b" stroke-width="1.5"/>
      <line x1="150" y1="40" x2="150" y2="260" stroke="#14244d" stroke-dasharray="2 3"/>
      <line x1="260" y1="40" x2="260" y2="260" stroke="#14244d" stroke-dasharray="2 3"/>
      <line x1="370" y1="40" x2="370" y2="260" stroke="#14244d" stroke-dasharray="2 3"/>
      <line x1="60" y1="180" x2="410" y2="180" stroke="#14244d" stroke-dasharray="2 3"/>
      <line x1="60" y1="100" x2="410" y2="100" stroke="#14244d" stroke-dasharray="2 3"/>
      
      <!-- Axis Labels -->
      <text x="235" y="295" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Density, ρ (g/cm³) [log scale]</text>
      <text x="20" y="150" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle" transform="rotate(-90 20 150)">Young's Modulus, E (GPa) [log]</text>

      <!-- Material Envelopes -->
      <!-- Ceramics -->
      <ellipse cx="270" cy="85" rx="55" ry="30" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="1.5"/>
      <text x="270" y="88" fill="#fda4af" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">CERAMICS (SiC, Al2O3)</text>

      <!-- Metals & Alloys -->
      <ellipse cx="320" cy="115" rx="65" ry="32" fill="rgba(212, 175, 55, 0.18)" stroke="#d4af37" stroke-width="1.5"/>
      <text x="320" y="118" fill="#fef08a" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">METALS (Steels, Ti, Al)</text>

      <!-- Composites -->
      <ellipse cx="210" cy="130" rx="50" ry="25" fill="rgba(56, 189, 248, 0.18)" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="210" y="133" fill="#bae6fd" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">COMPOSITES (CFRP)</text>

      <!-- Polymers -->
      <ellipse cx="150" cy="210" rx="45" ry="25" fill="rgba(16, 185, 129, 0.18)" stroke="#10b981" stroke-width="1.5"/>
      <text x="150" y="213" fill="#a7f3d0" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">POLYMERS (PE, PC)</text>

      <!-- Guideline line for E/ρ design index -->
      <line x1="80" y1="240" x2="380" y2="60" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="4 2"/>
      <text x="340" y="55" fill="#f59e0b" font-family="sans-serif" font-size="9">E / ρ = const</text>
    </svg>
    """

def svg_potential_well():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Axes -->
      <line x1="60" y1="120" x2="420" y2="120" stroke="#64748b" stroke-width="1.5"/>
      <line x1="60" y1="30" x2="60" y2="290" stroke="#64748b" stroke-width="1.5"/>
      <text x="415" y="112" fill="#94a3b8" font-family="sans-serif" font-size="11">r</text>
      <text x="40" y="45" fill="#94a3b8" font-family="sans-serif" font-size="11">E</text>
      <text x="45" y="124" fill="#94a3b8" font-family="sans-serif" font-size="10">0</text>

      <!-- Curves: Attraction, Repulsion, Net Energy -->
      <!-- Repulsion ER(r) > 0 -->
      <path d="M 68 35 Q 85 80 120 115 T 280 120" fill="none" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3"/>
      <text x="140" y="70" fill="#f43f5e" font-family="sans-serif" font-size="9">Repulsive E_R = B/r^n</text>

      <!-- Attraction EA(r) < 0 -->
      <path d="M 65 140 Q 140 145 280 130 T 420 122" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3"/>
      <text x="290" y="150" fill="#38bdf8" font-family="sans-serif" font-size="9">Attractive E_A = -A/r^m</text>

      <!-- Net Curve EN(r) -->
      <path d="M 72 38 C 82 170 120 250 170 250 C 230 250 310 145 420 124" fill="none" stroke="#d4af37" stroke-width="2.5"/>
      <text x="320" y="195" fill="#f5d061" font-family="sans-serif" font-size="11" font-weight="bold">Net Energy E_N(r)</text>

      <!-- Minimum Well Indicators -->
      <line x1="170" y1="120" x2="170" y2="250" stroke="#f5d061" stroke-width="1.2" stroke-dasharray="3 3"/>
      <circle cx="170" cy="250" r="4" fill="#d4af37"/>
      <text x="170" y="112" fill="#f5d061" font-family="sans-serif" font-size="10" text-anchor="middle">r_0 (Equilibrium)</text>

      <!-- Bonding Energy E0 -->
      <line x1="60" y1="250" x2="170" y2="250" stroke="#f5d061" stroke-width="1.2" stroke-dasharray="3 3"/>
      <text x="35" y="254" fill="#f5d061" font-family="sans-serif" font-size="10">-E_0</text>
      <text x="180" y="270" fill="#34d399" font-family="sans-serif" font-size="9">Deep well = High Tm & E, Low α</text>
    </svg>
    """

def svg_bonding_types():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Three Panels -->
      <!-- 1. Ionic -->
      <rect x="15" y="40" width="130" height="230" fill="#101c3d" stroke="#d4af37" stroke-width="1" rx="4"/>
      <text x="80" y="65" fill="#f5d061" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">IONIC</text>
      <circle cx="55" cy="120" r="22" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="55" y="125" fill="#ffffff" font-family="sans-serif" font-size="11" text-anchor="middle">Na⁺</text>
      <circle cx="105" cy="120" r="28" fill="#1e1e38" stroke="#10b981" stroke-width="1.5"/>
      <text x="105" y="125" fill="#ffffff" font-family="sans-serif" font-size="11" text-anchor="middle">Cl⁻</text>
      <path d="M 68 105 Q 80 95 90 105" fill="none" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
      <text x="80" y="195" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">Coulombic Attraction</text>
      <text x="80" y="215" fill="#cbd5e1" font-family="sans-serif" font-size="9" text-anchor="middle">Non-directional</text>
      <text x="80" y="235" fill="#a7f3d0" font-family="sans-serif" font-size="9" text-anchor="middle">High Tm, Brittle</text>

      <!-- 2. Covalent -->
      <rect x="160" y="40" width="130" height="230" fill="#101c3d" stroke="#38bdf8" stroke-width="1" rx="4"/>
      <text x="225" y="65" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">COVALENT</text>
      <circle cx="205" cy="120" r="24" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="245" cy="120" r="24" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
      <circle cx="225" cy="115" r="3" fill="#f5d061"/>
      <circle cx="225" cy="125" r="3" fill="#f5d061"/>
      <text x="205" y="124" fill="#ffffff" font-family="sans-serif" font-size="10" text-anchor="middle">C</text>
      <text x="245" y="124" fill="#ffffff" font-family="sans-serif" font-size="10" text-anchor="middle">C</text>
      <text x="225" y="195" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">Shared Electron Pairs</text>
      <text x="225" y="215" fill="#cbd5e1" font-family="sans-serif" font-size="9" text-anchor="middle">Highly Directional</text>
      <text x="225" y="235" fill="#a7f3d0" font-family="sans-serif" font-size="9" text-anchor="middle">Diamond, Polymers</text>

      <!-- 3. Metallic -->
      <rect x="305" y="40" width="130" height="230" fill="#101c3d" stroke="#f43f5e" stroke-width="1" rx="4"/>
      <text x="370" y="65" fill="#fca5a5" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">METALLIC</text>
      <!-- Ion cores -->
      <circle cx="335" cy="105" r="10" fill="#dc2626"/>
      <text x="335" y="108" fill="#fff" font-size="8" text-anchor="middle">+</text>
      <circle cx="370" cy="105" r="10" fill="#dc2626"/>
      <text x="370" y="108" fill="#fff" font-size="8" text-anchor="middle">+</text>
      <circle cx="405" cy="105" r="10" fill="#dc2626"/>
      <text x="405" y="108" fill="#fff" font-size="8" text-anchor="middle">+</text>
      <circle cx="350" cy="135" r="10" fill="#dc2626"/>
      <text x="350" y="138" fill="#fff" font-size="8" text-anchor="middle">+</text>
      <circle cx="390" cy="135" r="10" fill="#dc2626"/>
      <text x="390" y="138" fill="#fff" font-size="8" text-anchor="middle">+</text>
      <!-- Free electron cloud -->
      <circle cx="340" cy="125" r="2" fill="#38bdf8"/>
      <circle cx="365" cy="122" r="2" fill="#38bdf8"/>
      <circle cx="375" cy="148" r="2" fill="#38bdf8"/>
      <text x="370" y="195" fill="#94a3b8" font-family="sans-serif" font-size="9" text-anchor="middle">Delocalized Sea of e⁻</text>
      <text x="370" y="215" fill="#cbd5e1" font-family="sans-serif" font-size="9" text-anchor="middle">High Conductivity</text>
      <text x="370" y="235" fill="#a7f3d0" font-family="sans-serif" font-size="9" text-anchor="middle">Ductile & Malleable</text>
    </svg>
    """

def svg_crystal_unit_cells():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Left: BCC -->
      <g transform="translate(40, 50)">
        <text x="75" y="-10" fill="#f5d061" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">BCC (n = 2)</text>
        <!-- Back face -->
        <rect x="25" y="25" width="80" height="80" fill="none" stroke="#475569" stroke-width="1.2" stroke-dasharray="3 3"/>
        <!-- Connecting edges -->
        <line x1="0" y1="60" x2="25" y2="25" stroke="#475569" stroke-width="1.2"/>
        <line x1="80" y1="60" x2="105" y2="25" stroke="#475569" stroke-width="1.2"/>
        <line x1="0" y1="140" x2="25" y2="105" stroke="#475569" stroke-width="1.2"/>
        <line x1="80" y1="140" x2="105" y2="105" stroke="#475569" stroke-width="1.2"/>
        <!-- Front face -->
        <rect x="0" y="60" width="80" height="80" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
        <!-- Center atom -->
        <circle cx="52" cy="82" r="14" fill="#d4af37" stroke="#ffffff" stroke-width="1"/>
        <text x="52" y="86" fill="#070d1e" font-size="9" font-weight="bold" text-anchor="middle">C</text>
        <!-- Corner atoms -->
        <circle cx="0" cy="60" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <circle cx="80" cy="60" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <circle cx="0" cy="140" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <circle cx="80" cy="140" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <!-- Text details -->
        <text x="50" y="165" fill="#94a3b8" font-size="9" text-anchor="middle">a = 4R / √3</text>
        <text x="50" y="180" fill="#a7f3d0" font-size="9" text-anchor="middle">APF = 0.68 | CN = 8</text>
      </g>

      <!-- Right: FCC -->
      <g transform="translate(250, 50)">
        <text x="75" y="-10" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">FCC (n = 4)</text>
        <!-- Back face -->
        <rect x="25" y="25" width="80" height="80" fill="none" stroke="#475569" stroke-width="1.2" stroke-dasharray="3 3"/>
        <!-- Connecting edges -->
        <line x1="0" y1="60" x2="25" y2="25" stroke="#475569" stroke-width="1.2"/>
        <line x1="80" y1="60" x2="105" y2="25" stroke="#475569" stroke-width="1.2"/>
        <line x1="0" y1="140" x2="25" y2="105" stroke="#475569" stroke-width="1.2"/>
        <line x1="80" y1="140" x2="105" y2="105" stroke="#475569" stroke-width="1.2"/>
        <!-- Front face -->
        <rect x="0" y="60" width="80" height="80" fill="none" stroke="#d4af37" stroke-width="1.5"/>
        <!-- Face center atom -->
        <circle cx="40" cy="100" r="12" fill="#10b981" stroke="#ffffff" stroke-width="1"/>
        <!-- Corner atoms -->
        <circle cx="0" cy="60" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <circle cx="80" cy="60" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <circle cx="0" cy="140" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <circle cx="80" cy="140" r="9" fill="#1e3a8a" stroke="#38bdf8"/>
        <!-- Text details -->
        <text x="50" y="165" fill="#94a3b8" font-size="9" text-anchor="middle">a = 2√2 R</text>
        <text x="50" y="180" fill="#a7f3d0" font-size="9" text-anchor="middle">APF = 0.74 | CN = 12</text>
      </g>
    </svg>
    """

def svg_bragg_diffraction():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Plane 1 -->
      <line x1="50" y1="130" x2="400" y2="130" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="100" cy="130" r="7" fill="#d4af37"/>
      <circle cx="180" cy="130" r="7" fill="#d4af37"/>
      <circle cx="260" cy="130" r="7" fill="#d4af37"/>
      <circle cx="340" cy="130" r="7" fill="#d4af37"/>
      <text x="415" y="134" fill="#38bdf8" font-size="10">Plane 1</text>

      <!-- Plane 2 -->
      <line x1="50" y1="210" x2="400" y2="210" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="100" cy="210" r="7" fill="#d4af37"/>
      <circle cx="180" cy="210" r="7" fill="#d4af37"/>
      <circle cx="260" cy="210" r="7" fill="#d4af37"/>
      <circle cx="340" cy="210" r="7" fill="#d4af37"/>
      <text x="415" y="214" fill="#38bdf8" font-size="10">Plane 2</text>

      <!-- Interplanar spacing d -->
      <line x1="75" y1="130" x2="75" y2="210" stroke="#f5d061" stroke-width="1.5"/>
      <path d="M 72 135 L 75 130 L 78 135 M 72 205 L 75 210 L 78 205" stroke="#f5d061" stroke-width="1.5" fill="none"/>
      <text x="65" y="174" fill="#f5d061" font-size="11" font-weight="bold" text-anchor="middle">d_hkl</text>

      <!-- Beam 1: Reflecting on top atom -->
      <line x1="70" y1="50" x2="180" y2="130" stroke="#f43f5e" stroke-width="2"/>
      <line x1="180" y1="130" x2="290" y2="50" stroke="#f43f5e" stroke-width="2"/>

      <!-- Beam 2: Penetrating to bottom atom -->
      <line x1="150" y1="50" x2="260" y2="210" stroke="#fbbf24" stroke-width="2"/>
      <line x1="260" y1="210" x2="370" y2="50" stroke="#fbbf24" stroke-width="2"/>

      <!-- Extra path geometry -->
      <line x1="210" y1="137" x2="260" y2="210" stroke="#a7f3d0" stroke-width="1.2" stroke-dasharray="2 2"/>
      <line x1="260" y1="210" x2="310" y2="137" stroke="#a7f3d0" stroke-width="1.2" stroke-dasharray="2 2"/>

      <text x="225" y="260" fill="#f5d061" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">
        Bragg's Law: nλ = 2 d_hkl sin θ
      </text>
      <text x="225" y="285" fill="#94a3b8" font-size="10" text-anchor="middle">
        Constructive interference occurs when extra path equals integer wavelengths
      </text>
    </svg>
    """

def svg_point_defects():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Regular atoms grid -->
      <g fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5">
        <!-- Row 1 -->
        <circle cx="80" cy="60" r="12"/><circle cx="150" cy="60" r="12"/><circle cx="220" cy="60" r="12"/><circle cx="290" cy="60" r="12"/><circle cx="360" cy="60" r="12"/>
        <!-- Row 2 -->
        <circle cx="80" cy="130" r="12"/>
        <!-- Vacancy at (150, 130) -->
        <circle cx="150" cy="130" r="12" fill="none" stroke="#f43f5e" stroke-dasharray="3 3"/>
        <circle cx="220" cy="130" r="12"/><circle cx="290" cy="130" r="12"/><circle cx="360" cy="130" r="12"/>
        <!-- Row 3 -->
        <circle cx="80" cy="200" r="12"/><circle cx="150" cy="200" r="12"/>
        <!-- Substitutional impurity at (220, 200) -->
        <circle cx="220" cy="200" r="16" fill="#d4af37" stroke="#ffffff"/>
        <circle cx="290" cy="200" r="12"/><circle cx="360" cy="200" r="12"/>
      </g>
      <!-- Interstitial defect -->
      <circle cx="325" cy="165" r="7" fill="#10b981" stroke="#ffffff" stroke-width="1.2"/>

      <!-- Annotations -->
      <text x="150" y="105" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">Vacancy</text>
      <text x="220" y="240" fill="#f5d061" font-size="10" font-weight="bold" text-anchor="middle">Substitutional Solute</text>
      <text x="365" y="170" fill="#10b981" font-size="10" font-weight="bold">Interstitial</text>

      <text x="225" y="285" fill="#94a3b8" font-size="10" text-anchor="middle">
        Point Defects: Equilibrium vacancy fraction N_v/N = exp(-Q_v / kT)
      </text>
    </svg>
    """

def svg_dislocations():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Extra half plane of atoms (Edge Dislocation) -->
      <text x="225" y="30" fill="#f5d061" font-size="12" font-weight="bold" text-anchor="middle">Edge Dislocation (b ⊥ t)</text>
      
      <!-- Upper region: 5 columns compressed into 4 -->
      <g fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5">
        <circle cx="100" cy="70" r="10"/><circle cx="160" cy="70" r="10"/><circle cx="225" cy="70" r="10"/><circle cx="290" cy="70" r="10"/><circle cx="350" cy="70" r="10"/>
        <circle cx="100" cy="120" r="10"/><circle cx="165" cy="120" r="10"/><circle cx="225" cy="120" r="10"/><circle cx="285" cy="120" r="10"/><circle cx="350" cy="120" r="10"/>
      </g>
      
      <!-- Extra half plane symbol ⊥ -->
      <g stroke="#f43f5e" stroke-width="3">
        <line x1="225" y1="135" x2="225" y2="165"/>
        <line x1="210" y1="165" x2="240" y2="165"/>
      </g>

      <!-- Slip Plane -->
      <line x1="60" y1="165" x2="390" y2="165" stroke="#f5d061" stroke-width="1.5" stroke-dasharray="4 3"/>
      <text x="395" y="169" fill="#f5d061" font-size="9">Slip Plane</text>

      <!-- Lower region: 4 columns expanded -->
      <g fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5">
        <circle cx="100" cy="205" r="10"/><circle cx="180" cy="205" r="10"/><circle cx="270" cy="205" r="10"/><circle cx="350" cy="205" r="10"/>
        <circle cx="100" cy="255" r="10"/><circle cx="180" cy="255" r="10"/><circle cx="270" cy="255" r="10"/><circle cx="350" cy="255" r="10"/>
      </g>

      <!-- Burgers Vector b -->
      <line x1="180" y1="285" x2="270" y2="285" stroke="#34d399" stroke-width="2.5"/>
      <polygon points="266,281 274,285 266,289" fill="#34d399"/>
      <text x="225" y="302" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Burgers Vector b</text>
    </svg>
    """

def svg_diffusion_profiles():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Axes -->
      <line x1="60" y1="40" x2="60" y2="260" stroke="#64748b" stroke-width="1.5"/>
      <line x1="60" y1="260" x2="410" y2="260" stroke="#64748b" stroke-width="1.5"/>
      <text x="415" y="264" fill="#94a3b8" font-size="11">Depth, x</text>
      <text x="50" y="30" fill="#94a3b8" font-size="11">Conc, C(x,t)</text>

      <!-- Cs and C0 levels -->
      <line x1="55" y1="70" x2="400" y2="70" stroke="#475569" stroke-dasharray="2 3"/>
      <text x="35" y="74" fill="#f5d061" font-size="11" font-weight="bold">C_s</text>

      <line x1="55" y1="240" x2="400" y2="240" stroke="#475569" stroke-dasharray="2 3"/>
      <text x="35" y="244" fill="#94a3b8" font-size="11">C_0</text>

      <!-- Profiles at t1, t2, t3 -->
      <!-- t1 -->
      <path d="M 60 70 Q 110 80 140 180 T 170 240 L 400 240" fill="none" stroke="#f43f5e" stroke-width="2"/>
      <text x="180" y="220" fill="#f43f5e" font-size="10">t_1</text>

      <!-- t2 -->
      <path d="M 60 70 Q 140 85 220 180 T 260 240 L 400 240" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <text x="270" y="220" fill="#38bdf8" font-size="10">t_2 ( > t_1)</text>

      <!-- t3 -->
      <path d="M 60 70 Q 200 95 310 180 T 360 240 L 400 240" fill="none" stroke="#10b981" stroke-width="2"/>
      <text x="370" y="220" fill="#10b981" font-size="10">t_3 ( > t_2)</text>

      <text x="235" y="295" fill="#f5d061" font-size="11" text-anchor="middle">
        (C_x - C_0) / (C_s - C_0) = 1 - erf[ x / (2 √(Dt)) ]
      </text>
    </svg>
    """

def svg_stress_strain_curve():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Axes -->
      <line x1="60" y1="40" x2="60" y2="260" stroke="#64748b" stroke-width="1.5"/>
      <line x1="60" y1="260" x2="420" y2="260" stroke="#64748b" stroke-width="1.5"/>
      <text x="425" y="264" fill="#94a3b8" font-size="11">Strain, ε</text>
      <text x="45" y="30" fill="#94a3b8" font-size="11">Stress, σ</text>

      <!-- Engineering Curve -->
      <path d="M 60 260 L 120 140 Q 170 80 250 80 Q 320 80 370 140" fill="none" stroke="#38bdf8" stroke-width="2.5"/>

      <!-- True Stress Curve diverging after necking -->
      <path d="M 250 80 Q 310 70 370 45" fill="none" stroke="#f5d061" stroke-width="2" stroke-dasharray="3 3"/>
      <text x="375" y="45" fill="#f5d061" font-size="10">True Stress σ_T</text>

      <!-- 0.2% Offset line -->
      <line x1="85" y1="260" x2="140" y2="150" stroke="#f43f5e" stroke-width="1.2" stroke-dasharray="3 2"/>
      <circle cx="135" cy="160" r="4" fill="#f43f5e"/>
      <text x="145" y="165" fill="#f43f5e" font-size="10">σ_y (0.2% yield)</text>
      <text x="85" y="275" fill="#f43f5e" font-size="9" text-anchor="middle">0.002</text>

      <!-- UTS Point -->
      <circle cx="250" cy="80" r="4" fill="#d4af37"/>
      <text x="250" y="65" fill="#d4af37" font-size="10" font-weight="bold" text-anchor="middle">UTS (Necking onset: dσ/dε = σ)</text>

      <!-- Fracture Point -->
      <circle cx="370" cy="140" r="4" fill="#fb7185"/>
      <text x="375" y="155" fill="#fb7185" font-size="10">Fracture</text>

      <!-- Shaded Resilience Area -->
      <polygon points="60,260 120,140 120,260" fill="rgba(56, 189, 248, 0.15)"/>
      <text x="90" y="235" fill="#38bdf8" font-size="9">Resilience U_r</text>
    </svg>
    """

def svg_schmid_geometry():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Tensile Cylinder -->
      <rect x="180" y="60" width="90" height="200" fill="#101c3d" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
      <!-- Tensile Force Vectors -->
      <line x1="225" y1="60" x2="225" y2="15" stroke="#f43f5e" stroke-width="3"/>
      <polygon points="220,20 225,10 230,20" fill="#f43f5e"/>
      <text x="240" y="25" fill="#f43f5e" font-size="12" font-weight="bold">F (Tensile Axis)</text>

      <line x1="225" y1="260" x2="225" y2="305" stroke="#f43f5e" stroke-width="3"/>
      <polygon points="220,300 225,310 230,300" fill="#f43f5e"/>

      <!-- Inclined Slip Plane -->
      <ellipse cx="225" cy="160" rx="45" ry="18" fill="rgba(212, 175, 55, 0.3)" stroke="#d4af37" stroke-width="2"/>
      
      <!-- Normal vector n -->
      <line x1="225" y1="160" x2="280" y2="90" stroke="#10b981" stroke-width="2"/>
      <polygon points="274,90 285,85 282,96" fill="#10b981"/>
      <text x="290" y="88" fill="#10b981" font-size="10" font-weight="bold">n (Normal)</text>
      <!-- Angle phi -->
      <path d="M 225 110 A 50 50 0 0 1 250 125" fill="none" stroke="#10b981" stroke-width="1.2"/>
      <text x="245" y="112" fill="#10b981" font-size="10">φ</text>

      <!-- Slip Direction vector -->
      <line x1="225" y1="160" x2="260" y2="170" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="268" y="180" fill="#f59e0b" font-size="10" font-weight="bold">Slip Dir (λ)</text>

      <text x="100" y="160" fill="#f5d061" font-size="11" font-weight="bold">τ_R = σ cos φ cos λ</text>
      <text x="100" y="180" fill="#94a3b8" font-size="9">Yields when τ_R = τ_CRSS</text>
    </svg>
    """

def svg_hall_petch():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Hall-Petch Plot -->
      <line x1="70" y1="50" x2="70" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <line x1="70" y1="250" x2="400" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <text x="390" y="275" fill="#94a3b8" font-size="11" text-anchor="middle">d^(-1/2) (Grain Size Refinement →)</text>
      <text x="30" y="40" fill="#94a3b8" font-size="11">Yield Strength, σ_y</text>

      <!-- Linear Hall-Petch Line -->
      <line x1="70" y1="210" x2="360" y2="70" stroke="#d4af37" stroke-width="2.5"/>
      
      <!-- Friction Stress σ0 intercept -->
      <circle cx="70" cy="210" r="4" fill="#f43f5e"/>
      <text x="45" y="214" fill="#f43f5e" font-size="11" font-weight="bold">σ_0</text>

      <!-- Slope ky -->
      <path d="M 230 135 L 290 135 L 290 106" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3 2"/>
      <text x="260" y="150" fill="#38bdf8" font-size="10">Slope = k_y</text>

      <!-- Hall Petch breakdown at nanometer scale -->
      <path d="M 360 70 Q 380 90 395 140" fill="none" stroke="#fb7185" stroke-width="2" stroke-dasharray="3 3"/>
      <text x="360" y="55" fill="#fb7185" font-size="9">Inverse HP (d &lt; 15 nm)</text>

      <text x="225" y="295" fill="#f5d061" font-size="12" font-weight="bold" text-anchor="middle">
        Hall-Petch Law: σ_y = σ_0 + k_y · d^(-1/2)
      </text>
    </svg>
    """

def svg_annealing_stages():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Axes -->
      <line x1="60" y1="50" x2="60" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <line x1="60" y1="250" x2="420" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <text x="240" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">Annealing Temperature (1 Hour) →</text>
      <text x="45" y="40" fill="#94a3b8" font-size="11">Properties</text>

      <!-- Vertical Stage Dividers -->
      <line x1="160" y1="50" x2="160" y2="250" stroke="#475569" stroke-dasharray="3 3"/>
      <line x1="300" y1="50" x2="300" y2="250" stroke="#475569" stroke-dasharray="3 3"/>

      <!-- Stage Labels -->
      <text x="110" y="65" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">I. RECOVERY</text>
      <text x="230" y="65" fill="#f5d061" font-size="10" font-weight="bold" text-anchor="middle">II. RECRYSTALLIZATION</text>
      <text x="360" y="65" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">III. GRAIN GROWTH</text>

      <!-- Tensile Strength Curve (Drops sharply in stage II) -->
      <path d="M 60 90 L 160 95 C 190 100 210 200 290 210 L 410 220" fill="none" stroke="#f43f5e" stroke-width="2.5"/>
      <text x="110" y="110" fill="#f43f5e" font-size="9">Tensile Strength / Hardness</text>

      <!-- Ductility Curve (Surges in stage II) -->
      <path d="M 60 230 L 160 225 C 190 220 220 120 290 110 L 410 105" fill="none" stroke="#34d399" stroke-width="2.5"/>
      <text x="350" y="125" fill="#34d399" font-size="9">Ductility (%EL)</text>

      <!-- Grain Size Curve (Grows in stage III) -->
      <path d="M 290 230 Q 350 210 410 160" fill="none" stroke="#f5d061" stroke-width="2" stroke-dasharray="3 2"/>
      <text x="360" y="185" fill="#f5d061" font-size="9">Grain Size d</text>
    </svg>
    """

def svg_fatigue_sn():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Axes -->
      <line x1="60" y1="50" x2="60" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <line x1="60" y1="250" x2="420" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <text x="240" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">Cycles to Failure, N (Log Scale) →</text>
      <text x="30" y="40" fill="#94a3b8" font-size="11">Stress Amp, S</text>

      <!-- Steel Curve with Endurance Limit -->
      <path d="M 60 70 Q 140 100 220 150 L 410 150" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="280" y="140" fill="#38bdf8" font-size="10" font-weight="bold">Ferrous Alloys (Steels)</text>
      <!-- Endurance Limit Line -->
      <line x1="55" y1="150" x2="220" y2="150" stroke="#f5d061" stroke-dasharray="2 3"/>
      <text x="35" y="154" fill="#f5d061" font-size="10" font-weight="bold">σ_e</text>
      <text x="280" y="170" fill="#f5d061" font-size="9">Fatigue Limit (Infinite Life)</text>

      <!-- Aluminum / Non-ferrous Curve (No fatigue limit) -->
      <path d="M 60 110 Q 180 160 410 230" fill="none" stroke="#fb7185" stroke-width="2.5"/>
      <text x="280" y="220" fill="#fb7185" font-size="10" font-weight="bold">Non-Ferrous (Al, Cu, Mg)</text>
      <text x="280" y="245" fill="#cbd5e1" font-size="9">Continuous decline</text>
    </svg>
    """

def svg_charpy_dbtt():
    return """
    <svg viewBox="0 0 450 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <rect width="450" height="320" fill="#080f24" rx="6"/>
      <!-- Axes -->
      <line x1="60" y1="50" x2="60" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <line x1="60" y1="250" x2="420" y2="250" stroke="#64748b" stroke-width="1.5"/>
      <text x="240" y="280" fill="#94a3b8" font-size="11" text-anchor="middle">Testing Temperature, T (°C) →</text>
      <text x="30" y="40" fill="#94a3b8" font-size="11">Impact Energy (J)</text>

      <!-- FCC Curve: High toughness at all temps -->
      <path d="M 60 90 Q 240 85 410 80" fill="none" stroke="#34d399" stroke-width="2.5"/>
      <text x="300" y="70" fill="#34d399" font-size="10" font-weight="bold">FCC Metals (Al, Cu, γ-Fe)</text>
      <text x="300" y="95" fill="#a7f3d0" font-size="9">No DBTT; ductile at 0 K</text>

      <!-- BCC Curve: Sharp S-curve DBTT -->
      <path d="M 60 230 L 160 225 Q 210 220 230 160 Q 250 100 300 95 L 410 95" fill="none" stroke="#f43f5e" stroke-width="2.5"/>
      <text x="140" y="210" fill="#f43f5e" font-size="10" font-weight="bold">BCC Steels</text>

      <!-- DBTT Indicator -->
      <line x1="235" y1="50" x2="235" y2="250" stroke="#f5d061" stroke-width="1.2" stroke-dasharray="3 3"/>
      <circle cx="235" cy="160" r="4" fill="#f5d061"/>
      <text x="235" y="295" fill="#f5d061" font-size="11" font-weight="bold" text-anchor="middle">DBTT</text>
      <text x="120" y="245" fill="#94a3b8" font-size="9">Brittle Cleavage</text>
      <text x="350" y="115" fill="#94a3b8" font-size="9">Ductile Shear Lips</text>
    </svg>
    """
