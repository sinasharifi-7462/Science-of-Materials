# Science of Materials — Midterm Examination Study Suite
### University of Tehran | Department of Mechanical Engineering
**Course:** Science of Materials (Undergraduate Curriculum)  
**Instructor:** Prof. A. Sadeghi  
**Prepared by:** Sina Sharifi (Teaching Assistant)  

---

## 📖 Overview
This repository contains an offline-functional, interconnected interactive web application designed for students preparing for the Midterm Examination in **Science of Materials**.

The problem suite covers the complete curriculum from **Chapter 1 through Chapter 8** (up to, but not including, Phase Diagrams), featuring exactly **50 comprehensive sample problems per chapter (400 problems total)** with detailed, step-by-step mathematical solutions and boxed final answers.

---

## 🏛️ Curriculum Coverage (400 Problems)

| Chapter | Title | Problems | Focus Areas |
| :---: | :--- | :---: | :--- |
| **01** | **Introduction to Materials Science & Engineering** | **50** | MSE Paradigm, Processing-Structure-Properties-Performance Tetrahedron, Material Classes, Ashby charts. |
| **02** | **Atomic Structure & Interatomic Bonding** | **50** | Electronic configurations, quantum numbers, Lennard-Jones potential well $E(r)$, primary & secondary bonding, thermal expansion. |
| **03** | **The Structure of Crystalline Solids** | **50** | FCC, BCC, HCP unit cells, APF, theoretical density, Miller indices $[uvw]$ and $(hkl)$, planar/linear densities, XRD & Bragg's Law. |
| **04** | **Imperfections in Solids** | **50** | Equilibrium vacancies ($N_v$), Hume-Rothery rules, composition conversions, Schottky/Frenkel defects, Burgers vectors, ASTM grain size. |
| **05** | **Diffusion in Solids** | **50** | Fick's 1st Law ($J = -D \frac{dC}{dx}$), Fick's 2nd Law error function solutions ($\text{erf}$), Arrhenius diffusivity ($Q_d$), industrial steel carburization depths. |
| **06** | **Mechanical Properties of Metals** | **50** | Hooke's Law ($E, G, K, \nu$), 0.2% offset yield, resilience ($U_r$), toughness ($U_t$), true stress-strain ($\sigma_T = K\varepsilon_T^n$), Schmid's Law ($\tau_R$), Hardness testing. |
| **07** | **Dislocations & Strengthening Mechanisms** | **50** | Peierls-Nabarro stress, Hall-Petch grain refinement ($\sigma_0 + k_y d^{-1/2}$), solid solution strengthening, cold work (%CW), Orowan precipitation looping, annealing kinetics. |
| **08** | **Failure: Fracture, Fatigue & Creep** | **50** | Inglis notch concentration ($K_t$), Griffith & Orowan criterion, LEFM Mode I toughness ($K_{Ic}$), Charpy DBTT, fatigue S-N curves, Goodman relations, Paris crack growth, Larson-Miller creep. |
| **Total** | **Comprehensive Midterm Suite** | **400** | **100% Complete Step-by-Step Solutions** |

---

## ✨ Features & Interface
- **Dark Blue Classic Academic Theme:** Hairline borders, typography, and gold accent styling (`#d4af37`).
- **Interactive Solution Toggles:** Solutions are hidden by default for active self-testing; revealed on button click.
- **Real-Time Search & Filters:** Instant live search across problems, equations, and solutions, plus category and difficulty filters.
- **Progress Tracking:** Browser-persisted "Mark Mastered" bookmarking for study progress.
- **Embedded Technical SVGs:** High-resolution native vector diagrams for unit cells, potential wells, diffusion curves, stress-strain curves, and fatigue S-N charts.
- **Master Formula Compendium:** Built-in modal reference of physical constants and governing equations across all 8 chapters.

---

## 🚀 How to Run Locally
No installation or local server is required:
1. Clone or download this repository.
2. Double-click `index.html` to open the cover portal in any modern web browser (Chrome, Edge, Firefox, Safari).

---

## ☁️ Deployment on Cloudflare Pages
The folder `website_for_cloudflare/` is pre-packaged and ready for instant deployment:
1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com).
2. Go to **Workers & Pages** $\to$ **Create** $\to$ **Pages** $\to$ **Upload assets**.
3. Drag and drop the `website_for_cloudflare/` folder.
4. Click **Deploy site**.
