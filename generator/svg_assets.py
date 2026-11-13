# ==============================================================================
# SCIENCE OF MATERIALS — MIDTERM STUDY SUITE GENERATOR
# High-Definition Technical Engineering Diagrams & Charts (Vector SVGs)
# Department of Mechanical Engineering | University of Tehran
# Author: Sina Sharifi | Instructor: Prof. A. Sadeghi
# ==============================================================================

import os

def svg_tetrahedron():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="tetBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#101d3f"/>
      <stop offset="100%" stop-color="#060c1d"/>
    </radialGradient>
    <linearGradient id="goldEdge" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#b48318"/>
    </linearGradient>
    <linearGradient id="cyanEdge" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="faceGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(212, 175, 55, 0.12)"/>
      <stop offset="100%" stop-color="rgba(56, 189, 248, 0.04)"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Canvas Frame with Technical Grid -->
  <rect width="750" height="500" fill="url(#tetBg)" rx="8" stroke="#253861" stroke-width="2"/>
  <g stroke="#1a294d" stroke-width="1" stroke-dasharray="4 6">
    <line x1="50" y1="100" x2="700" y2="100"/>
    <line x1="50" y1="200" x2="700" y2="200"/>
    <line x1="50" y1="300" x2="700" y2="300"/>
    <line x1="50" y1="400" x2="700" y2="400"/>
    <line x1="150" y1="50" x2="150" y2="450"/>
    <line x1="375" y1="50" x2="375" y2="450"/>
    <line x1="600" y1="50" x2="600" y2="450"/>
  </g>

  <!-- Shaded Triangular Faces -->
  <polygon points="375,80 150,380 375,270" fill="url(#faceGrad1)"/>
  <polygon points="375,80 600,380 375,270" fill="rgba(56, 189, 248, 0.08)"/>
  <polygon points="150,380 600,380 375,270" fill="rgba(16, 185, 129, 0.08)"/>

  <!-- Outer Solid Edges -->
  <line x1="375" y1="80" x2="150" y2="380" stroke="url(#goldEdge)" stroke-width="3"/>
  <line x1="375" y1="80" x2="600" y2="380" stroke="url(#goldEdge)" stroke-width="3"/>
  <line x1="150" y1="380" x2="600" y2="380" stroke="url(#goldEdge)" stroke-width="3"/>

  <!-- Interior Centroid Connections -->
  <line x1="375" y1="80" x2="375" y2="270" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 4"/>
  <line x1="150" y1="380" x2="375" y2="270" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 4"/>
  <line x1="600" y1="380" x2="375" y2="270" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 4"/>

  <!-- Modern Extension Vertices (Economics & Environment) -->
  <line x1="375" y1="80" x2="90" y2="180" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
  <line x1="150" y1="380" x2="90" y2="180" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
  <circle cx="90" cy="180" r="28" fill="#1e1b4b" stroke="#f43f5e" stroke-width="2"/>
  <text x="90" y="176" fill="#fecdd3" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">COST</text>
  <text x="90" y="192" fill="#fda4af" font-family="'Inter', sans-serif" font-size="9" text-anchor="middle">Economics</text>

  <line x1="375" y1="80" x2="660" y2="180" stroke="#10b981" stroke-width="2" stroke-dasharray="3 3"/>
  <line x1="600" y1="380" x2="660" y2="180" stroke="#10b981" stroke-width="2" stroke-dasharray="3 3"/>
  <circle cx="660" cy="180" r="28" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
  <text x="660" y="176" fill="#a7f3d0" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">LCA</text>
  <text x="660" y="192" fill="#6ee7b7" font-family="'Inter', sans-serif" font-size="9" text-anchor="middle">Environment</text>

  <!-- Central Centroid Core -->
  <circle cx="375" cy="270" r="38" fill="#0b1736" stroke="url(#goldEdge)" stroke-width="2.5" filter="url(#glow)"/>
  <text x="375" y="266" fill="#fef08a" font-family="'Cinzel', Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">MSE</text>
  <text x="375" y="282" fill="#cbd5e1" font-family="'Inter', sans-serif" font-size="10" font-weight="600" text-anchor="middle">PARADIGM</text>

  <!-- VERTEX 1: PROCESSING (Top) -->
  <g transform="translate(375, 80)">
    <circle cx="0" cy="0" r="34" fill="#14244d" stroke="#facc15" stroke-width="3"/>
    <text x="0" y="-5" fill="#ffffff" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">PROCESSING</text>
    <text x="0" y="12" fill="#facc15" font-family="'Inter', sans-serif" font-size="10" text-anchor="middle">Synthesis</text>
    <!-- Label Card -->
    <rect x="-110" y="-62" width="220" height="24" rx="4" fill="#091329" stroke="#d4af37" stroke-width="1"/>
    <text x="0" y="-46" fill="#fef08a" font-family="'Inter', sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Casting &bull; Sintering &bull; 3D Print &bull; Heat Treat</text>
  </g>

  <!-- VERTEX 2: STRUCTURE (Bottom Left) -->
  <g transform="translate(150, 380)">
    <circle cx="0" cy="0" r="34" fill="#0c4a6e" stroke="#38bdf8" stroke-width="3"/>
    <text x="0" y="-5" fill="#ffffff" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">STRUCTURE</text>
    <text x="0" y="12" fill="#7dd3fc" font-family="'Inter', sans-serif" font-size="10" text-anchor="middle">Multi-Scale</text>
    <!-- Label Card -->
    <rect x="-105" y="44" width="210" height="24" rx="4" fill="#091329" stroke="#38bdf8" stroke-width="1"/>
    <text x="0" y="60" fill="#bae6fd" font-family="'Inter', sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Atomic Lattice &bull; Defects &bull; Grains</text>
  </g>

  <!-- VERTEX 3: PROPERTIES (Bottom Right) -->
  <g transform="translate(600, 380)">
    <circle cx="0" cy="0" r="34" fill="#064e3b" stroke="#34d399" stroke-width="3"/>
    <text x="0" y="-5" fill="#ffffff" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">PROPERTIES</text>
    <text x="0" y="12" fill="#6ee7b7" font-family="'Inter', sans-serif" font-size="10" text-anchor="middle">Intrinsic</text>
    <!-- Label Card -->
    <rect x="-105" y="44" width="210" height="24" rx="4" fill="#091329" stroke="#34d399" stroke-width="1"/>
    <text x="0" y="60" fill="#a7f3d0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Mechanical &bull; Electrical &bull; Thermal</text>
  </g>

  <!-- Banner Bottom -->
  <rect x="180" y="455" width="390" height="32" rx="4" fill="#0f1b38" stroke="#d4af37" stroke-width="1.5"/>
  <text x="375" y="476" fill="#fef08a" font-family="'Cinzel', Georgia, serif" font-size="12" font-weight="bold" text-anchor="middle">
    PERFORMANCE: Service Reliability &bull; Durability &bull; Lifetime
  </text>
</svg>"""

def svg_ashby_chart():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="ashbyBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0f1a36"/>
      <stop offset="100%" stop-color="#060c1d"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="url(#ashbyBg)" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Plot Area Frame -->
  <rect x="90" y="40" width="620" height="390" fill="#081024" stroke="#334773" stroke-width="1.5"/>

  <!-- Log-Log Grid Lines -->
  <!-- Vertical Grid (Density: 0.1, 1, 10, 20 g/cm³) -->
  <line x1="160" y1="40" x2="160" y2="430" stroke="#1a294d" stroke-width="1"/>
  <text x="160" y="448" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">0.3</text>
  <line x1="280" y1="40" x2="280" y2="430" stroke="#1a294d" stroke-width="1.2"/>
  <text x="280" y="448" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">1.0</text>
  <line x1="420" y1="40" x2="420" y2="430" stroke="#1a294d" stroke-width="1"/>
  <text x="420" y="448" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">3.0</text>
  <line x1="560" y1="40" x2="560" y2="430" stroke="#1a294d" stroke-width="1.2"/>
  <text x="560" y="448" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">10.0</text>

  <!-- Horizontal Grid (Modulus: 0.01, 0.1, 1, 10, 100, 1000 GPa) -->
  <line x1="90" y1="380" x2="710" y2="380" stroke="#1a294d" stroke-width="1"/>
  <text x="75" y="384" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">0.1</text>
  <line x1="90" y1="300" x2="710" y2="300" stroke="#1a294d" stroke-width="1"/>
  <text x="75" y="304" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">1.0</text>
  <line x1="90" y1="220" x2="710" y2="220" stroke="#1a294d" stroke-width="1"/>
  <text x="75" y="224" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">10</text>
  <line x1="90" y1="140" x2="710" y2="140" stroke="#1a294d" stroke-width="1.2"/>
  <text x="75" y="144" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="end">100</text>
  <line x1="90" y1="60" x2="710" y2="60" stroke="#1a294d" stroke-width="1"/>
  <text x="75" y="64" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="end">1000</text>

  <!-- Axis Titles -->
  <text x="400" y="480" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Density &rho; (g/cm&sup3;) &rarr; [Logarithmic Scale]</text>
  <text x="30" y="235" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle" transform="rotate(-90 30 235)">Young's Modulus E (GPa) &rarr; [Log Scale]</text>

  <!-- DESIGN GUIDE LINES (Ashby Indices) -->
  <!-- Slope 1: M = E / rho (Tension Tie-Rod) -->
  <line x1="120" y1="350" x2="550" y2="70" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6 3"/>
  <rect x="440" y="75" width="130" height="20" rx="3" fill="#1e1808" stroke="#f59e0b" stroke-width="1"/>
  <text x="505" y="89" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">Slope 1: E/&rho; = C</text>

  <!-- Slope 2: M = E^(1/2) / rho (Beam in Bending) -->
  <line x1="150" y1="380" x2="680" y2="140" stroke="#06b6d4" stroke-width="2" stroke-dasharray="6 3"/>
  <rect x="560" y="150" width="140" height="20" rx="3" fill="#082029" stroke="#06b6d4" stroke-width="1"/>
  <text x="630" y="164" fill="#a5f3fc" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">Slope 2: E&frac12;/&rho; = C</text>

  <!-- MATERIAL CLASS ENVELOPES -->
  <!-- 1. Technical Ceramics (Diamond, SiC, Al2O3) -->
  <ellipse cx="440" cy="115" rx="85" ry="42" fill="rgba(244, 63, 94, 0.22)" stroke="#f43f5e" stroke-width="2.5"/>
  <text x="440" y="110" fill="#ffffff" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">CERAMICS</text>
  <text x="440" y="126" fill="#fecdd3" font-family="'Inter', sans-serif" font-size="9.5" text-anchor="middle">SiC &bull; Al&sub2;O&sub3; &bull; Diamond &bull; Si&sub3;N&sub4;</text>

  <!-- 2. Metals & Alloys (Steels, Ti, Al, Cu) -->
  <ellipse cx="530" cy="155" rx="95" ry="46" fill="rgba(212, 175, 55, 0.22)" stroke="#facc15" stroke-width="2.5"/>
  <text x="530" y="150" fill="#ffffff" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">METALS &amp; ALLOYS</text>
  <text x="530" y="166" fill="#fef08a" font-family="'Inter', sans-serif" font-size="9.5" text-anchor="middle">Steels &bull; Ni-alloys &bull; Ti &bull; Al &bull; Cu</text>

  <!-- 3. Composites (CFRP, GFRP) -->
  <ellipse cx="320" cy="175" rx="75" ry="38" fill="rgba(56, 189, 248, 0.22)" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="320" y="170" fill="#ffffff" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">COMPOSITES</text>
  <text x="320" y="186" fill="#bae6fd" font-family="'Inter', sans-serif" font-size="9.5" text-anchor="middle">CFRP &bull; GFRP &bull; MMC &bull; Cermets</text>

  <!-- 4. Polymers (PEEK, PC, Nylon, HDPE) -->
  <ellipse cx="280" cy="285" rx="70" ry="36" fill="rgba(16, 185, 129, 0.22)" stroke="#10b981" stroke-width="2.5"/>
  <text x="280" y="280" fill="#ffffff" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">POLYMERS</text>
  <text x="280" y="296" fill="#a7f3d0" font-family="'Inter', sans-serif" font-size="9.5" text-anchor="middle">PEEK &bull; PC &bull; Nylon &bull; Epoxy &bull; PE</text>

  <!-- 5. Engineering Foams -->
  <ellipse cx="145" cy="355" rx="40" ry="25" fill="rgba(168, 85, 247, 0.22)" stroke="#a855f7" stroke-width="2"/>
  <text x="145" y="353" fill="#ffffff" font-family="'Inter', sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">FOAMS</text>
  <text x="145" y="367" fill="#e9d5ff" font-family="'Inter', sans-serif" font-size="8.5" text-anchor="middle">Polymer/Metal</text>
</svg>"""

def svg_potential_well():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="wellBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0e1836"/>
      <stop offset="100%" stop-color="#060c1d"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="url(#wellBg)" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Center Axis: Energy E = 0 -->
  <line x1="80" y1="180" x2="710" y2="180" stroke="#64748b" stroke-width="2"/>
  <text x="705" y="170" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="12" font-weight="bold">Interatomic Distance r &rarr;</text>
  
  <!-- Vertical Axis: r = 0 -->
  <line x1="90" y1="40" x2="90" y2="460" stroke="#64748b" stroke-width="2"/>
  <text x="65" y="55" fill="#facc15" font-family="'Inter', sans-serif" font-size="13" font-weight="bold">+E</text>
  <text x="65" y="445" fill="#facc15" font-family="'Inter', sans-serif" font-size="13" font-weight="bold">-E</text>
  <text x="65" y="185" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">0</text>

  <!-- Curve 1: Repulsive Potential E_R(r) = B / r^n (Steep positive) -->
  <path d="M 105 45 Q 125 125 180 172 T 400 180" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="5 4"/>
  <rect x="180" y="65" width="220" height="26" rx="4" fill="#2d0612" stroke="#f43f5e" stroke-width="1"/>
  <text x="290" y="82" fill="#fecdd3" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">
    Repulsion E_R(r) = +B / r^n (Pauli)
  </text>

  <!-- Curve 2: Attractive Potential E_A(r) = -A / r^m (Gradual negative) -->
  <path d="M 100 220 Q 200 230 420 200 T 700 184" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5 4"/>
  <rect x="420" y="225" width="230" height="26" rx="4" fill="#042033" stroke="#38bdf8" stroke-width="1"/>
  <text x="535" y="242" fill="#bae6fd" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">
    Attraction E_A(r) = -A / r^m (Coulomb)
  </text>

  <!-- Curve 3: Net Potential Energy Well E_N(r) = E_A + E_R (Thick Gold) -->
  <path d="M 108 50 C 120 280 180 390 260 390 C 350 390 480 220 700 186" fill="none" stroke="#ffd700" stroke-width="4"/>

  <!-- Equilibrium Minimum Well: r0 and E0 -->
  <line x1="260" y1="180" x2="260" y2="390" stroke="#facc15" stroke-width="2" stroke-dasharray="4 3"/>
  <circle cx="260" cy="390" r="7" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
  <text x="260" y="165" fill="#fef08a" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">r&sub0; (Equilibrium Spacing)</text>

  <!-- Well Depth -E0 (Bonding Energy) -->
  <line x1="90" y1="390" x2="260" y2="390" stroke="#facc15" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="50" y="394" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">-E&sub0;</text>

  <!-- Asymmetry & Thermal Expansion Annotation -->
  <g transform="translate(360, 290)">
    <rect x="0" y="0" width="350" height="95" rx="6" fill="#0a1530" stroke="#d4af37" stroke-width="1.5"/>
    <text x="175" y="22" fill="#facc15" font-family="'Inter', sans-serif" font-size="12" font-weight="bold" text-anchor="middle">PHYSICAL CORRELATES OF THE WELL</text>
    <line x1="15" y1="30" x2="335" y2="30" stroke="#253861" stroke-width="1"/>
    <text x="15" y="48" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="10.5">&bull; Well Depth E&sub0; &prop; Melting Point T_m &amp; Cohesive Energy</text>
    <text x="15" y="66" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="10.5">&bull; Well Curvature (d&sup2;E/dr&sup2;) &prop; Young's Modulus E</text>
    <text x="15" y="84" fill="#34d399" font-family="'Inter', sans-serif" font-size="10.5">&bull; Asymmetric Anharmonicity &rarr; Thermal Expansion (&alpha;_L)</text>
  </g>
</svg>"""

def svg_crystal_unit_cells():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="atomGold" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="35%" stop-color="#facc15"/>
      <stop offset="80%" stop-color="#ca8a04"/>
      <stop offset="100%" stop-color="#713f12"/>
    </radialGradient>
    <radialGradient id="atomBlue" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#f0f9ff"/>
      <stop offset="35%" stop-color="#38bdf8"/>
      <stop offset="80%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0c4a6e"/>
    </radialGradient>
    <radialGradient id="atomGreen" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#f0fdf4"/>
      <stop offset="35%" stop-color="#34d399"/>
      <stop offset="80%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#064e3b"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="#070f24" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Title Top Banner -->
  <rect x="160" y="15" width="430" height="36" rx="6" fill="#0d1b3e" stroke="#d4af37" stroke-width="1.5"/>
  <text x="375" y="38" fill="#fef08a" font-family="'Cinzel', Georgia, serif" font-size="14" font-weight="bold" text-anchor="middle">
    METALLIC CRYSTAL UNIT CELLS (FCC, BCC, HCP)
  </text>

  <!-- PANEL 1: BODY-CENTERED CUBIC (BCC) -->
  <g transform="translate(40, 80)">
    <rect width="210" height="370" fill="#0a1329" rx="6" stroke="#d4af37" stroke-width="1.5"/>
    <text x="105" y="30" fill="#facc15" font-family="'Inter', sans-serif" font-size="14" font-weight="bold" text-anchor="middle">BCC LATTICE</text>
    <text x="105" y="48" fill="#cbd5e1" font-family="'Inter', sans-serif" font-size="10.5" text-anchor="middle">&alpha;-Fe, Cr, W, Mo, V</text>
    
    <!-- 3D Cube Perspective -->
    <g transform="translate(30, 80)">
      <!-- Back face -->
      <rect x="35" y="35" width="110" height="110" fill="none" stroke="#334773" stroke-width="1.5" stroke-dasharray="4 3"/>
      <!-- Connecting edges -->
      <line x1="0" y1="85" x2="35" y2="35" stroke="#334773" stroke-width="1.5"/>
      <line x1="110" y1="85" x2="145" y2="35" stroke="#334773" stroke-width="1.5"/>
      <line x1="0" y1="195" x2="35" y2="145" stroke="#334773" stroke-width="1.5"/>
      <line x1="110" y1="195" x2="145" y2="145" stroke="#334773" stroke-width="1.5"/>
      <!-- Front face -->
      <rect x="0" y="85" width="110" height="110" fill="none" stroke="#facc15" stroke-width="2"/>

      <!-- Center Body Atom (Gold) -->
      <circle cx="72" cy="115" r="22" fill="url(#atomGold)" stroke="#ffffff" stroke-width="1.5"/>
      <text x="72" y="120" fill="#000" font-family="'Inter', sans-serif" font-size="10" font-weight="bold" text-anchor="middle">1 Body</text>

      <!-- 8 Corner Atoms (Blue) -->
      <circle cx="0" cy="85" r="14" fill="url(#atomBlue)"/>
      <circle cx="110" cy="85" r="14" fill="url(#atomBlue)"/>
      <circle cx="0" cy="195" r="14" fill="url(#atomBlue)"/>
      <circle cx="110" cy="195" r="14" fill="url(#atomBlue)"/>
      <circle cx="35" cy="35" r="12" fill="url(#atomBlue)" opacity="0.8"/>
      <circle cx="145" cy="35" r="12" fill="url(#atomBlue)" opacity="0.8"/>
    </g>

    <!-- Stats Plaque -->
    <rect x="15" y="295" width="180" height="60" rx="4" fill="#060c1d" stroke="#253861" stroke-width="1"/>
    <text x="105" y="313" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">n = 2 atoms/cell</text>
    <text x="105" y="330" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">a = 4R / &radic;3</text>
    <text x="105" y="347" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">APF = 0.68 | CN = 8</text>
  </g>

  <!-- PANEL 2: FACE-CENTERED CUBIC (FCC) -->
  <g transform="translate(270, 80)">
    <rect width="210" height="370" fill="#0a1329" rx="6" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="105" y="30" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="14" font-weight="bold" text-anchor="middle">FCC LATTICE</text>
    <text x="105" y="48" fill="#cbd5e1" font-family="'Inter', sans-serif" font-size="10.5" text-anchor="middle">&gamma;-Fe, Al, Cu, Ni, Au</text>
    
    <g transform="translate(30, 80)">
      <rect x="35" y="35" width="110" height="110" fill="none" stroke="#334773" stroke-width="1.5" stroke-dasharray="4 3"/>
      <line x1="0" y1="85" x2="35" y2="35" stroke="#334773" stroke-width="1.5"/>
      <line x1="110" y1="85" x2="145" y2="35" stroke="#334773" stroke-width="1.5"/>
      <line x1="0" y1="195" x2="35" y2="145" stroke="#334773" stroke-width="1.5"/>
      <line x1="110" y1="195" x2="145" y2="145" stroke="#334773" stroke-width="1.5"/>
      <rect x="0" y="85" width="110" height="110" fill="none" stroke="#38bdf8" stroke-width="2"/>

      <!-- 6 Face Center Atoms (Green) -->
      <circle cx="55" cy="140" r="18" fill="url(#atomGreen)" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="90" cy="90" r="14" fill="url(#atomGreen)" opacity="0.9"/>
      <circle cx="20" cy="140" r="14" fill="url(#atomGreen)" opacity="0.9"/>

      <!-- Corner Atoms -->
      <circle cx="0" cy="85" r="14" fill="url(#atomBlue)"/>
      <circle cx="110" cy="85" r="14" fill="url(#atomBlue)"/>
      <circle cx="0" cy="195" r="14" fill="url(#atomBlue)"/>
      <circle cx="110" cy="195" r="14" fill="url(#atomBlue)"/>
    </g>

    <rect x="15" y="295" width="180" height="60" rx="4" fill="#060c1d" stroke="#253861" stroke-width="1"/>
    <text x="105" y="313" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">n = 4 atoms/cell</text>
    <text x="105" y="330" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">a = 2&radic;2 R</text>
    <text x="105" y="347" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">APF = 0.74 | CN = 12</text>
  </g>

  <!-- PANEL 3: HEXAGONAL CLOSE-PACKED (HCP) -->
  <g transform="translate(500, 80)">
    <rect width="210" height="370" fill="#0a1329" rx="6" stroke="#34d399" stroke-width="1.5"/>
    <text x="105" y="30" fill="#34d399" font-family="'Inter', sans-serif" font-size="14" font-weight="bold" text-anchor="middle">HCP LATTICE</text>
    <text x="105" y="48" fill="#cbd5e1" font-family="'Inter', sans-serif" font-size="10.5" text-anchor="middle">Ti, Mg, Zn, Zr, Co</text>
    
    <!-- HCP Hexagonal Prism Projection -->
    <g transform="translate(25, 80)">
      <!-- Top Hexagon -->
      <polygon points="80,25 130,45 130,85 80,105 30,85 30,45" fill="none" stroke="#34d399" stroke-width="2"/>
      <!-- Bottom Hexagon -->
      <polygon points="80,125 130,145 130,185 80,205 30,185 30,145" fill="none" stroke="#164e63" stroke-width="1.5" stroke-dasharray="4 3"/>
      <!-- Vertical Pillars -->
      <line x1="80" y1="25" x2="80" y2="125" stroke="#34d399" stroke-width="1.5"/>
      <line x1="130" y1="45" x2="130" y2="145" stroke="#34d399" stroke-width="1.5"/>
      <line x1="30" y1="45" x2="30" y2="145" stroke="#34d399" stroke-width="1.5"/>
      
      <!-- Mid-plane Triangle of 3 Atoms -->
      <circle cx="65" cy="115" r="14" fill="url(#atomGold)"/>
      <circle cx="95" cy="115" r="14" fill="url(#atomGold)"/>
      <circle cx="80" cy="135" r="14" fill="url(#atomGold)"/>

      <!-- Basal Center Atoms -->
      <circle cx="80" cy="65" r="14" fill="url(#atomBlue)"/>
    </g>

    <rect x="15" y="295" width="180" height="60" rx="4" fill="#060c1d" stroke="#253861" stroke-width="1"/>
    <text x="105" y="313" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">n = 6 atoms/cell</text>
    <text x="105" y="330" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">c/a = 1.633 (Ideal)</text>
    <text x="105" y="347" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">APF = 0.74 | CN = 12</text>
  </g>
</svg>"""

def svg_point_defects():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="hostAtom" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#e0f2fe"/>
      <stop offset="35%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </radialGradient>
    <radialGradient id="soluteAtom" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="35%" stop-color="#facc15"/>
      <stop offset="100%" stop-color="#a16207"/>
    </radialGradient>
    <radialGradient id="interAtom" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#dcfce7"/>
      <stop offset="35%" stop-color="#22c55e"/>
      <stop offset="100%" stop-color="#14532d"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="#070f24" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Header -->
  <rect x="180" y="15" width="390" height="34" rx="4" fill="#0f1c3f" stroke="#d4af37" stroke-width="1.5"/>
  <text x="375" y="37" fill="#fef08a" font-family="'Cinzel', Georgia, serif" font-size="13.5" font-weight="bold" text-anchor="middle">
    ATLAS OF POINT DEFECTS IN CRYSTALLINE SOLIDS
  </text>

  <!-- Atomic Crystal Grid (7x5 Grid) -->
  <g transform="translate(60, 70)">
    <!-- Grid Lines (Lattice Planes) -->
    <g stroke="#1e3a8a" stroke-width="1.5" stroke-dasharray="3 3">
      <line x1="40" y1="50" x2="580" y2="50"/>
      <line x1="40" y1="120" x2="580" y2="120"/>
      <line x1="40" y1="190" x2="580" y2="190"/>
      <line x1="40" y1="260" x2="580" y2="260"/>
      <line x1="40" y1="330" x2="580" y2="330"/>
    </g>

    <!-- Row 1 -->
    <circle cx="50" cy="50" r="18" fill="url(#hostAtom)"/><circle cx="140" cy="50" r="18" fill="url(#hostAtom)"/>
    <circle cx="230" cy="50" r="18" fill="url(#hostAtom)"/><circle cx="320" cy="50" r="18" fill="url(#hostAtom)"/>
    <circle cx="410" cy="50" r="18" fill="url(#hostAtom)"/><circle cx="500" cy="50" r="18" fill="url(#hostAtom)"/>
    <circle cx="590" cy="50" r="18" fill="url(#hostAtom)"/>

    <!-- Row 2 (Contains Vacancy & Self-Interstitial) -->
    <circle cx="50" cy="120" r="18" fill="url(#hostAtom)"/>
    <!-- VACANCY (Missing host atom) -->
    <circle cx="140" cy="120" r="18" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="5 3"/>
    <line x1="128" y1="108" x2="152" y2="132" stroke="#ef4444" stroke-width="2"/>
    <line x1="152" y1="108" x2="128" y2="132" stroke="#ef4444" stroke-width="2"/>
    <!-- Self-Interstitial nearby -->
    <circle cx="185" cy="155" r="16" fill="url(#hostAtom)" stroke="#ffffff" stroke-width="1.5"/>

    <circle cx="230" cy="120" r="18" fill="url(#hostAtom)"/><circle cx="320" cy="120" r="18" fill="url(#hostAtom)"/>
    <circle cx="410" cy="120" r="18" fill="url(#hostAtom)"/><circle cx="500" cy="120" r="18" fill="url(#hostAtom)"/>
    <circle cx="590" cy="120" r="18" fill="url(#hostAtom)"/>

    <!-- Row 3 (Contains Substitutional Impurity) -->
    <circle cx="50" cy="190" r="18" fill="url(#hostAtom)"/><circle cx="140" cy="190" r="18" fill="url(#hostAtom)"/>
    <circle cx="230" cy="190" r="18" fill="url(#hostAtom)"/>
    <!-- Large Substitutional Solute -->
    <circle cx="320" cy="190" r="26" fill="url(#soluteAtom)" stroke="#ffffff" stroke-width="2"/>
    <circle cx="410" cy="190" r="18" fill="url(#hostAtom)"/><circle cx="500" cy="190" r="18" fill="url(#hostAtom)"/>
    <circle cx="590" cy="190" r="18" fill="url(#hostAtom)"/>

    <!-- Row 4 (Contains Small Interstitial Solute) -->
    <circle cx="50" cy="260" r="18" fill="url(#hostAtom)"/><circle cx="140" cy="260" r="18" fill="url(#hostAtom)"/>
    <circle cx="230" cy="260" r="18" fill="url(#hostAtom)"/><circle cx="320" cy="260" r="18" fill="url(#hostAtom)"/>
    <!-- Small Interstitial (Carbon/Nitrogen in Fe) -->
    <circle cx="455" cy="225" r="10" fill="url(#interAtom)" stroke="#ffffff" stroke-width="1.5"/>
    <circle cx="410" cy="260" r="18" fill="url(#hostAtom)"/><circle cx="500" cy="260" r="18" fill="url(#hostAtom)"/>
    <circle cx="590" cy="260" r="18" fill="url(#hostAtom)"/>

    <!-- Row 5 -->
    <circle cx="50" cy="330" r="18" fill="url(#hostAtom)"/><circle cx="140" cy="330" r="18" fill="url(#hostAtom)"/>
    <circle cx="230" cy="330" r="18" fill="url(#hostAtom)"/><circle cx="320" cy="330" r="18" fill="url(#hostAtom)"/>
    <circle cx="410" cy="330" r="18" fill="url(#hostAtom)"/><circle cx="500" cy="330" r="18" fill="url(#hostAtom)"/>
    <circle cx="590" cy="330" r="18" fill="url(#hostAtom)"/>
  </g>

  <!-- Defect Labels & Callout Boxes -->
  <!-- Vacancy Callout -->
  <rect x="50" y="80" width="130" height="26" rx="4" fill="#3b070c" stroke="#ef4444" stroke-width="1.5"/>
  <text x="115" y="97" fill="#fca5a5" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">VACANCY</text>

  <!-- Self-interstitial -->
  <rect x="180" y="245" width="135" height="26" rx="4" fill="#0c2d48" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="247" y="262" fill="#bae6fd" font-family="'Inter', sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">Self-Interstitial</text>

  <!-- Substitutional -->
  <rect x="330" y="300" width="170" height="26" rx="4" fill="#2d1d03" stroke="#facc15" stroke-width="1.5"/>
  <text x="415" y="317" fill="#fef08a" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Substitutional Solute</text>

  <!-- Interstitial -->
  <rect x="515" y="280" width="165" height="26" rx="4" fill="#042714" stroke="#22c55e" stroke-width="1.5"/>
  <text x="597" y="297" fill="#bbf7d0" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Interstitial Solute (C)</text>

  <!-- Mathematical Law Bottom Banner -->
  <rect x="120" y="445" width="510" height="36" rx="4" fill="#0a1530" stroke="#d4af37" stroke-width="1.5"/>
  <text x="375" y="468" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">
    N_v / N = exp(-Q_v / k_B T) &bull; Hume-Rothery Rules (&Delta;r &le; 15%)
  </text>
</svg>"""

def svg_diffusion_profiles():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="diffBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0f1938"/>
      <stop offset="100%" stop-color="#060c1d"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="url(#diffBg)" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Plot Canvas -->
  <rect x="100" y="50" width="600" height="360" fill="#091226" stroke="#334773" stroke-width="1.5"/>

  <!-- Grid lines -->
  <line x1="100" y1="120" x2="700" y2="120" stroke="#172554" stroke-dasharray="3 3"/>
  <line x1="100" y1="200" x2="700" y2="200" stroke="#172554" stroke-dasharray="3 3"/>
  <line x1="100" y1="280" x2="700" y2="280" stroke="#172554" stroke-dasharray="3 3"/>
  <line x1="100" y1="360" x2="700" y2="360" stroke="#172554" stroke-dasharray="3 3"/>

  <!-- Concentration Levels Cs (Surface) and C0 (Initial) -->
  <line x1="90" y1="90" x2="700" y2="90" stroke="#facc15" stroke-width="2" stroke-dasharray="4 2"/>
  <text x="80" y="94" fill="#facc15" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">C_s</text>
  <text x="705" y="94" fill="#facc15" font-family="'Inter', sans-serif" font-size="11">Constant Surface Concentration</text>

  <line x1="90" y1="380" x2="700" y2="380" stroke="#64748b" stroke-width="2" stroke-dasharray="4 2"/>
  <text x="80" y="384" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="end">C_0</text>
  <text x="705" y="384" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="11">Initial Core Concentration</text>

  <!-- Profiles for Diffusion Times t1 < t2 < t3 -->
  <!-- Curve 1: t1 (Shortest time) -->
  <path d="M 100 90 Q 150 110 200 280 T 260 380 L 700 380" fill="none" stroke="#f43f5e" stroke-width="3"/>
  <circle cx="200" cy="280" r="5" fill="#f43f5e"/>
  <rect x="210" y="240" width="85" height="22" rx="3" fill="#2d0612" stroke="#f43f5e" stroke-width="1"/>
  <text x="252" y="255" fill="#fecdd3" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Time t_1</text>

  <!-- Curve 2: t2 (Intermediate time) -->
  <path d="M 100 90 Q 200 120 320 280 T 420 380 L 700 380" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="320" cy="280" r="5" fill="#38bdf8"/>
  <rect x="330" y="240" width="115" height="22" rx="3" fill="#042033" stroke="#38bdf8" stroke-width="1"/>
  <text x="387" y="255" fill="#bae6fd" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Time t_2 (> t_1)</text>

  <!-- Curve 3: t3 (Longest time) -->
  <path d="M 100 90 Q 300 140 480 280 T 600 380 L 700 380" fill="none" stroke="#34d399" stroke-width="4"/>
  <circle cx="480" cy="280" r="5" fill="#34d399"/>
  <rect x="490" y="240" width="115" height="22" rx="3" fill="#042714" stroke="#34d399" stroke-width="1"/>
  <text x="547" y="255" fill="#a7f3d0" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">Time t_3 (> t_2)</text>

  <!-- Axes Labels -->
  <text x="400" y="445" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Distance From Surface x (Depth into Part) &rarr;</text>
  <text x="35" y="230" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle" transform="rotate(-90 35 230)">Solute Concentration C(x,t) &rarr;</text>

  <!-- Mathematical Formula Box -->
  <rect x="140" y="15" width="470" height="32" rx="4" fill="#0a1530" stroke="#d4af37" stroke-width="1.5"/>
  <text x="375" y="36" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="12.5" font-weight="bold" text-anchor="middle">
    (C_x - C_0) / (C_s - C_0) = 1 - erf[ x / (2 &radic;(Dt)) ]
  </text>
</svg>"""

def svg_stress_strain_curve():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="stressBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0e1836"/>
      <stop offset="100%" stop-color="#060c1d"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="url(#stressBg)" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Plot Canvas -->
  <rect x="90" y="50" width="620" height="370" fill="#081024" stroke="#334773" stroke-width="1.5"/>

  <!-- Shaded Modulus of Resilience Area -->
  <polygon points="90,420 180,240 180,420" fill="rgba(56, 189, 248, 0.22)"/>
  <text x="140" y="380" fill="#7dd3fc" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">U_r (Resilience)</text>

  <!-- Shaded Plastic Toughness Area (Rest of curve) -->
  <path d="M 180 240 Q 260 120 400 120 Q 520 120 620 220 L 620 420 L 180 420 Z" fill="rgba(212, 175, 55, 0.1)"/>
  <text x="380" y="320" fill="#fef08a" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Total Toughness (Energy to Fracture)</text>

  <!-- Engineering Stress-Strain Curve (Cyan Solid) -->
  <path d="M 90 420 L 180 240 Q 260 120 400 120 Q 520 120 620 220" fill="none" stroke="#38bdf8" stroke-width="3.5"/>

  <!-- True Stress-Strain Curve (Gold Dashed - diverges at UTS necking) -->
  <path d="M 400 120 Q 510 100 620 60" fill="none" stroke="#facc15" stroke-width="3" stroke-dasharray="6 4"/>
  <rect x="520" y="40" width="170" height="24" rx="3" fill="#2d1d03" stroke="#facc15" stroke-width="1"/>
  <text x="605" y="56" fill="#fef08a" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">True Stress &sigma;_T = K &epsilon;_T^n</text>

  <!-- 0.2% Offset Construction Line (Ruby) -->
  <line x1="125" y1="420" x2="205" y2="260" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3"/>
  <circle cx="198" cy="275" r="5" fill="#f43f5e"/>
  <text x="125" y="440" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">&epsilon; = 0.002</text>
  
  <rect x="210" y="270" width="130" height="24" rx="3" fill="#3b070c" stroke="#f43f5e" stroke-width="1"/>
  <text x="275" y="286" fill="#fecdd3" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">&sigma;_y (0.2% Yield)</text>

  <!-- UTS Point (Ultimate Tensile Strength / Necking Onset) -->
  <circle cx="400" cy="120" r="6" fill="#facc15" stroke="#ffffff" stroke-width="2"/>
  <rect x="300" y="80" width="200" height="26" rx="4" fill="#0f1c3f" stroke="#d4af37" stroke-width="1.5"/>
  <text x="400" y="97" fill="#fef08a" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">UTS (Necking: d&sigma;/d&epsilon; = &sigma;)</text>

  <!-- Fracture Point -->
  <circle cx="620" cy="220" r="6" fill="#fb7185" stroke="#ffffff" stroke-width="2"/>
  <text x="635" y="235" fill="#fb7185" font-family="'Inter', sans-serif" font-size="12" font-weight="bold">Fracture (&sigma;_f, &epsilon;_f)</text>

  <!-- Hooke's Law Elastic Slope E -->
  <line x1="90" y1="420" x2="180" y2="240" stroke="#ffffff" stroke-width="2"/>
  <text x="110" y="310" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold">Slope = E</text>

  <!-- Axis Titles -->
  <text x="400" y="475" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Engineering Strain &epsilon; &rarr;</text>
  <text x="35" y="235" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle" transform="rotate(-90 35 235)">Engineering Stress &sigma; (MPa) &rarr;</text>
</svg>"""

def svg_hall_petch():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="hpBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0f1a36"/>
      <stop offset="100%" stop-color="#060c1d"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="url(#hpBg)" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Left: Grain Boundary Dislocation Pile-Up Diagram -->
  <g transform="translate(40, 60)">
    <rect width="320" height="380" fill="#091329" rx="6" stroke="#d4af37" stroke-width="1.5"/>
    <text x="160" y="30" fill="#facc15" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">
      GRAIN BOUNDARY PILE-UP
    </text>

    <!-- Grain Boundary Line (Thick diagonal) -->
    <line x1="220" y1="50" x2="220" y2="350" stroke="#f43f5e" stroke-width="4"/>
    <text x="230" y="80" fill="#fca5a5" font-family="'Inter', sans-serif" font-size="11" font-weight="bold">High-Angle Boundary</text>

    <!-- Grain 1 (Left, diameter d) -->
    <text x="100" y="70" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="12" font-weight="bold">Grain 1 (Size d)</text>
    <!-- Frank-Read Dislocation Source S -->
    <circle cx="50" cy="200" r="7" fill="#facc15"/>
    <text x="50" y="225" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">Source</text>

    <!-- Dislocation Pile-Up Line towards boundary -->
    <line x1="50" y1="200" x2="220" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>

    <!-- Dislocation Half-Plane Symbols &perp; -->
    <g stroke="#38bdf8" stroke-width="2.5">
      <line x1="80" y1="190" x2="80" y2="200"/><line x1="72" y1="200" x2="88" y2="200"/>
      <line x1="120" y1="190" x2="120" y2="200"/><line x1="112" y1="200" x2="128" y2="200"/>
      <line x1="155" y1="190" x2="155" y2="200"/><line x1="147" y1="200" x2="163" y2="200"/>
      <line x1="185" y1="190" x2="185" y2="200"/><line x1="177" y1="200" x2="193" y2="200"/>
      <line x1="210" y1="190" x2="210" y2="200"/><line x1="202" y1="200" x2="218" y2="200"/>
    </g>

    <text x="135" y="175" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="10.5" text-anchor="middle">n Dislocations Pile Up</text>
    <rect x="30" y="270" width="260" height="50" rx="4" fill="#14244d" stroke="#38bdf8" stroke-width="1"/>
    <text x="160" y="290" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">&tau;_tip = n &bull; &tau;_applied</text>
    <text x="160" y="308" fill="#bae6fd" font-family="'Inter', sans-serif" font-size="10" text-anchor="middle">Finer grains (smaller d) &rarr; smaller pile-up</text>
  </g>

  <!-- Right: Hall-Petch Plot (Yield Strength vs d^-1/2) -->
  <g transform="translate(390, 60)">
    <rect width="320" height="380" fill="#091329" rx="6" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="30" fill="#38bdf8" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">
      HALL-PETCH RELATION
    </text>

    <!-- Axes -->
    <line x1="50" y1="50" x2="50" y2="310" stroke="#64748b" stroke-width="2"/>
    <line x1="50" y1="310" x2="290" y2="310" stroke="#64748b" stroke-width="2"/>
    <text x="170" y="335" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="11" font-weight="bold">d&minus;&frac12; (mm&minus;&frac12;) &rarr; Finer Grains</text>
    <text x="25" y="180" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" transform="rotate(-90 25 180)">&sigma;_y (MPa) &rarr;</text>

    <!-- Straight Hall-Petch Line (Gold) -->
    <line x1="50" y1="260" x2="250" y2="80" stroke="#facc15" stroke-width="3.5"/>

    <!-- Friction Stress Intercept sigma_0 -->
    <circle cx="50" cy="260" r="5" fill="#f43f5e"/>
    <text x="35" y="265" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="end">&sigma;_0</text>
    <text x="80" y="280" fill="#cbd5e1" font-family="'Inter', sans-serif" font-size="9.5">Lattice friction</text>

    <!-- Slope Triangle (ky) -->
    <path d="M 140 180 L 200 180 L 200 125" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="180" y="195" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">Slope = k_y</text>

    <!-- Inverse Hall-Petch Breakdown (Nanocrystalline regime) -->
    <path d="M 250 80 Q 270 100 280 150" fill="none" stroke="#fb7185" stroke-width="2.5" stroke-dasharray="4 3"/>
    <text x="235" y="65" fill="#fb7185" font-family="'Inter', sans-serif" font-size="9.5">Inverse HP (d &lt; 15 nm)</text>
  </g>

  <!-- Banner Bottom -->
  <rect x="180" y="455" width="390" height="34" rx="4" fill="#0f1b38" stroke="#d4af37" stroke-width="1.5"/>
  <text x="375" y="477" fill="#fef08a" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">
    &sigma;_y = &sigma;_0 + k_y &bull; d^(&minus;1/2) &bull; Simultaneous Strength &amp; Toughness
  </text>
</svg>"""

def svg_charpy_dbtt():
    return """<svg viewBox="0 0 750 500" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="charpyBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0e1736"/>
      <stop offset="100%" stop-color="#060c1d"/>
    </radialGradient>
  </defs>

  <rect width="750" height="500" fill="url(#charpyBg)" rx="8" stroke="#253861" stroke-width="2"/>

  <!-- Plot Canvas Frame -->
  <rect x="90" y="40" width="620" height="380" fill="#081024" stroke="#334773" stroke-width="1.5"/>

  <!-- Axes -->
  <line x1="90" y1="380" x2="710" y2="380" stroke="#64748b" stroke-width="2"/>
  <line x1="90" y1="40" x2="90" y2="380" stroke="#64748b" stroke-width="2"/>
  <text x="400" y="445" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Test Temperature T (&deg;C) &rarr;</text>
  <text x="35" y="230" fill="#f8fafc" font-family="'Inter', sans-serif" font-size="13" font-weight="bold" text-anchor="middle" transform="rotate(-90 35 230)">Charpy V-Notch Impact Energy (Joules) &rarr;</text>

  <!-- Curve 1: FCC Metals (Al, Cu, Austenitic Stainless Steel) - NO DBTT -->
  <path d="M 100 100 Q 380 90 690 80" fill="none" stroke="#34d399" stroke-width="4"/>
  <rect x="420" y="60" width="260" height="26" rx="4" fill="#042714" stroke="#34d399" stroke-width="1.5"/>
  <text x="550" y="77" fill="#a7f3d0" font-family="'Inter', sans-serif" font-size="11.5" font-weight="bold" text-anchor="middle">
    FCC Alloys (Al, Cu, Austenitic 304 SS)
  </text>
  <text x="550" y="105" fill="#6ee7b7" font-family="'Inter', sans-serif" font-size="10">No DBTT &bull; Ductile at Cryogenic Temps</text>

  <!-- Curve 2: High-Strength Steels (Moderate toughness, low transition) -->
  <path d="M 100 280 Q 400 240 690 200" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6 3"/>
  <text x="560" y="215" fill="#fde68a" font-family="'Inter', sans-serif" font-size="11" font-weight="bold">High-Strength Steels / Ti Alloys</text>

  <!-- Curve 3: Low-Carbon BCC Structural Steels (Pronounced S-shaped DBTT) -->
  <path d="M 100 350 L 250 340 Q 340 330 380 230 Q 420 130 500 120 L 690 120" fill="none" stroke="#f43f5e" stroke-width="4"/>
  <rect x="140" y="325" width="130" height="24" rx="4" fill="#3b070c" stroke="#f43f5e" stroke-width="1"/>
  <text x="205" y="341" fill="#fca5a5" font-family="'Inter', sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Low-Carbon Steel</text>

  <!-- Upper Shelf & Lower Shelf Annotations -->
  <rect x="520" y="135" width="160" height="40" rx="4" fill="#14244d" stroke="#38bdf8" stroke-width="1"/>
  <text x="600" y="152" fill="#bae6fd" font-family="'Inter', sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">UPPER SHELF</text>
  <text x="600" y="167" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="9.5" text-anchor="middle">100% Fibrous Shear Rupture</text>

  <rect x="120" y="270" width="160" height="40" rx="4" fill="#14244d" stroke="#38bdf8" stroke-width="1"/>
  <text x="200" y="287" fill="#bae6fd" font-family="'Inter', sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">LOWER SHELF</text>
  <text x="200" y="302" fill="#94a3b8" font-family="'Inter', sans-serif" font-size="9.5" text-anchor="middle">100% Brittle Cleavage</text>

  <!-- DBTT Vertical Divider Line -->
  <line x1="390" y1="40" x2="390" y2="380" stroke="#ffd700" stroke-width="2.5" stroke-dasharray="6 4"/>
  <circle cx="390" cy="230" r="7" fill="#facc15" stroke="#ffffff" stroke-width="2"/>
  
  <rect x="310" y="390" width="160" height="28" rx="4" fill="#0b1736" stroke="#ffd700" stroke-width="1.5"/>
  <text x="390" y="409" fill="#fef08a" font-family="'Inter', sans-serif" font-size="11.5" font-weight="bold" text-anchor="middle">DBTT Transition Temp</text>
</svg>"""

def export_all_svgs(output_dir="assets/images"):
    os.makedirs(output_dir, exist_ok=True)
    svgs = {
        "ch1_tetrahedron.svg": svg_tetrahedron(),
        "ch1_ashby.svg": svg_ashby_chart(),
        "ch2_potential_well.svg": svg_potential_well(),
        "ch3_crystal_unit_cells.svg": svg_crystal_unit_cells(),
        "ch4_point_defects.svg": svg_point_defects(),
        "ch5_diffusion_profiles.svg": svg_diffusion_profiles(),
        "ch6_stress_strain_curve.svg": svg_stress_strain_curve(),
        "ch7_hall_petch.svg": svg_hall_petch(),
        "ch8_charpy_dbtt.svg": svg_charpy_dbtt(),
    }
    for fname, code in svgs.items():
        with open(os.path.join(output_dir, fname), "w", encoding="utf-8") as f:
            f.write(code)
    print(f"Exported {len(svgs)} standalone vector SVGs to {output_dir}")

if __name__ == "__main__":
    export_all_svgs("assets/images")
    export_all_svgs("website_for_cloudflare/assets/images")
