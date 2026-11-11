/* ==========================================================================
   SCIENCE OF MATERIALS — MIDTERM STUDY SUITE
   Client-Side Interactive Scripts
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initSolutionToggles();
  initExpandCollapseAll();
  initProblemFiltering();
  initJumpNavigator();
  initBookmarks();
  initBackToTop();
  initFormulaModal();
  updateStudyStats();
});

// Helper for typesetting math dynamically
function renderMath(targetElement) {
  if (window.MathJax && window.MathJax.typesetPromise) {
    try {
      if (window.MathJax.typesetClear && targetElement) {
        window.MathJax.typesetClear([targetElement]);
      }
      const promise = targetElement ? window.MathJax.typesetPromise([targetElement]) : window.MathJax.typesetPromise();
      if (promise && promise.catch) {
        promise.catch(err => console.warn('MathJax typesetting warning:', err));
      }
    } catch (e) {
      console.warn('MathJax error:', e);
    }
  }
}

// Toggle individual solution
function initSolutionToggles() {
  document.querySelectorAll('.btn-toggle-solution').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const problemCard = btn.closest('.problem-card');
      if (!problemCard) return;
      const solutionBox = problemCard.querySelector('.solution-container');
      if (!solutionBox) return;

      const isVisible = solutionBox.classList.contains('visible');
      if (isVisible) {
        solutionBox.classList.remove('visible');
        btn.classList.remove('expanded');
        btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg> Show Detailed Solution`;
      } else {
        solutionBox.classList.add('visible');
        btn.classList.add('expanded');
        btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg> Hide Solution`;
        
        // Trigger MathJax re-render for revealed container
        renderMath(solutionBox);
      }
    });
  });
}

// Expand / Collapse All
function initExpandCollapseAll() {
  const expandBtn = document.getElementById('btn-expand-all');
  const collapseBtn = document.getElementById('btn-collapse-all');

  if (expandBtn) {
    expandBtn.addEventListener('click', () => {
      document.querySelectorAll('.problem-card').forEach(card => {
        if (card.style.display !== 'none') {
          const solutionBox = card.querySelector('.solution-container');
          const btn = card.querySelector('.btn-toggle-solution');
          if (solutionBox && btn) {
            solutionBox.classList.add('visible');
            btn.classList.add('expanded');
            btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg> Hide Solution`;
          }
        }
      });
      renderMath();
    });
  }

  if (collapseBtn) {
    collapseBtn.addEventListener('click', () => {
      document.querySelectorAll('.problem-card').forEach(card => {
        const solutionBox = card.querySelector('.solution-container');
        const btn = card.querySelector('.btn-toggle-solution');
        if (solutionBox && btn) {
          solutionBox.classList.remove('visible');
          btn.classList.remove('expanded');
          btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg> Show Detailed Solution`;
        }
      });
    });
  }
}

// Search and Filter Problems
function initProblemFiltering() {
  const searchInput = document.getElementById('problem-search-input');
  const catFilter = document.getElementById('category-filter');
  const diffFilter = document.getElementById('diff-filter');

  function applyFilter() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedCat = catFilter ? catFilter.value : 'all';
    const selectedDiff = diffFilter ? diffFilter.value : 'all';

    const cards = document.querySelectorAll('.problem-card');
    let visibleCount = 0;

    cards.forEach(card => {
      const text = card.innerText.toLowerCase();
      const cardCat = card.getAttribute('data-category') || '';
      const cardDiff = card.getAttribute('data-difficulty') || '';

      const matchesQuery = !query || text.includes(query);
      const matchesCat = (selectedCat === 'all') || (cardCat === selectedCat);
      const matchesDiff = (selectedDiff === 'all') || (cardDiff === selectedDiff);

      if (matchesQuery && matchesCat && matchesDiff) {
        card.style.display = 'block';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    const countDisplay = document.getElementById('visible-problem-count');
    if (countDisplay) {
      countDisplay.textContent = `${visibleCount} Problems Shown`;
    }
  }

  if (searchInput) searchInput.addEventListener('input', applyFilter);
  if (catFilter) catFilter.addEventListener('change', applyFilter);
  if (diffFilter) diffFilter.addEventListener('change', applyFilter);
}

// Quick Jump Navigator
function initJumpNavigator() {
  const jumpSelect = document.getElementById('jump-to-problem');
  if (jumpSelect) {
    jumpSelect.addEventListener('change', (e) => {
      const probId = e.target.value;
      if (!probId) return;
      const targetElem = document.getElementById(probId);
      if (targetElem) {
        targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
        targetElem.style.transition = 'box-shadow 0.4s ease';
        targetElem.style.boxShadow = '0 0 30px rgba(212, 175, 55, 0.7)';
        setTimeout(() => {
          targetElem.style.boxShadow = '';
        }, 1800);
      }
    });
  }
}

// Bookmarking / Study tracking with localStorage
function initBookmarks() {
  const pageId = document.body.getAttribute('data-page-id') || 'general';

  document.querySelectorAll('.btn-bookmark').forEach(btn => {
    const probId = btn.getAttribute('data-problem-id');
    const storageKey = `ut_matsci_review_${pageId}_${probId}`;

    if (localStorage.getItem(storageKey) === 'true') {
      btn.classList.add('active');
      btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="#d4af37" stroke="#d4af37" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg> Mastered`;
    }

    btn.addEventListener('click', () => {
      const isBookmarked = btn.classList.contains('active');
      if (isBookmarked) {
        btn.classList.remove('active');
        btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg> Mark Mastered`;
        localStorage.removeItem(storageKey);
      } else {
        btn.classList.add('active');
        btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="#d4af37" stroke="#d4af37" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg> Mastered`;
        localStorage.setItem(storageKey, 'true');
      }
      updateStudyStats();
    });
  });
}

function updateStudyStats() {
  const counter = document.getElementById('mastered-count-badge');
  if (!counter) return;

  let totalMastered = 0;
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && key.startsWith('ut_matsci_review_') && localStorage.getItem(key) === 'true') {
      totalMastered++;
    }
  }
  counter.textContent = `${totalMastered} Mastered`;
}

// Back to Top Button
function initBackToTop() {
  const backTopBtn = document.getElementById('btn-back-top');
  if (!backTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backTopBtn.classList.add('visible');
    } else {
      backTopBtn.classList.remove('visible');
    }
  });

  backTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// Formula Compendium Modal
function initFormulaModal() {
  const openBtn = document.getElementById('btn-open-formula-sheet');
  const modal = document.getElementById('formula-modal');
  const closeBtn = document.getElementById('btn-close-formula-modal');

  if (openBtn && modal) {
    openBtn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.add('active');
      renderMath(modal);
    });
  }

  if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => {
      modal.classList.remove('active');
    });
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('active');
      }
    });
  }
}
