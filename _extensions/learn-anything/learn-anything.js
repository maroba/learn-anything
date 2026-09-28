// learn-anything: client-side helpers shared by all books.
//
// 1. Paragraph references: every content block (paragraph, list item, code block,
//    table, callout, ...) gets a stable-ish id "<section-id>-p<n>" and a ¶ button.
//    Clicking it copies a reference (location, URL and excerpt) that the reader
//    pastes into the Claude chat, so Claude can find the exact spot in the source.
// 2. Changelog: marks the chapter's changelog box as "new" if the chapter was
//    revised since the reader's last visit (stored in localStorage only).
(function () {
  "use strict";

  const STRINGS = {
    de: { copy: "Referenz auf diese Stelle kopieren", copied: "Referenz kopiert – jetzt in den Chat einfügen", failed: "Kopieren fehlgeschlagen", paragraph: "Absatz", isNew: "neu" },
    en: { copy: "Copy a reference to this passage", copied: "Reference copied – paste it into the chat", failed: "Copy failed", paragraph: "paragraph", isNew: "new" },
    el: { copy: "Αντιγραφή αναφοράς σε αυτό το σημείο", copied: "Η αναφορά αντιγράφηκε – επικολλήστε τη στη συνομιλία", failed: "Η αντιγραφή απέτυχε", paragraph: "παράγραφος", isNew: "νέο" },
    es: { copy: "Copiar una referencia a este pasaje", copied: "Referencia copiada – pégala en el chat", failed: "No se pudo copiar", paragraph: "párrafo", isNew: "nuevo" },
    fr: { copy: "Copier une référence à ce passage", copied: "Référence copiée – collez-la dans le chat", failed: "Échec de la copie", paragraph: "paragraphe", isNew: "nouveau" },
    it: { copy: "Copia un riferimento a questo passo", copied: "Riferimento copiato – incollalo nella chat", failed: "Copia non riuscita", paragraph: "paragrafo", isNew: "nuovo" },
  };
  const lang = (document.documentElement.lang || "en").toLowerCase();
  const t = STRINGS[lang] || STRINGS[lang.slice(0, 2)] || STRINGS.en;

  const content = document.getElementById("quarto-document-content");
  if (!content) return;

  const BLOCKS = "p, li, div.sourceCode, table, blockquote, .callout, figure, .cell-output-display, dl";
  const EXCLUDE = "#title-block-header, .la-changes, nav, .quarto-appendix-heading, .callout-header";
  const EXCERPT_LENGTH = 280;

  const clean = (s) => (s || "").replace(/\s+/g, " ").trim();
  const text = (el) => clean(el && el.textContent);

  function sectionOf(el) {
    return el.parentElement ? el.parentElement.closest("section[id]") : null;
  }

  function headingOf(section) {
    const h = section && section.querySelector(":scope > h1, :scope > h2, :scope > h3, :scope > h4, :scope > h5, :scope > h6");
    return text(h);
  }

  // Outermost blocks only: a list item counts once, not once per nested paragraph.
  const blocks = Array.from(content.querySelectorAll(BLOCKS)).filter((el) =>
    !el.closest(EXCLUDE) && !(el.parentElement && el.parentElement.closest(BLOCKS)));

  const counters = new Map();
  blocks.forEach((el) => {
    const section = sectionOf(el);
    const key = section ? section.id : "top";
    const n = (counters.get(key) || 0) + 1;
    counters.set(key, n);

    if (!el.id) el.id = `${key}-p${n}`;
    // Captured now, before MathJax replaces the TeX source with rendered markup.
    const excerpt = text(el);

    const button = document.createElement("button");
    button.type = "button";
    button.className = "la-ref";
    button.textContent = "¶";
    button.title = t.copy;
    button.setAttribute("aria-label", t.copy);
    button.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      copyReference(el, section, n, excerpt);
    });

    el.classList.add("la-ref-target");
    el.prepend(button);
  });

  // Touch devices have no hover: tapping a passage shows its ¶ (tap again or elsewhere to hide).
  if (window.matchMedia("(hover: none)").matches) {
    let active = null;
    content.addEventListener("click", (event) => {
      if (event.target.closest("a, button, input, summary, .callout-header")) return;
      const el = event.target.closest(".la-ref-target");
      if (active && active !== el) active.classList.remove("la-active");
      if (el) el.classList.toggle("la-active");
      active = el;
    });
  }

  function reference(el, section, n, excerpt) {
    const book = text(document.querySelector(".sidebar-title")) || document.title;
    const chapter = text(document.querySelector("#title-block-header h1, h1.title"));
    const trail = [book, chapter, headingOf(section)].filter(Boolean);
    trail.push(`${t.paragraph} ${n}`);

    const url = new URL(window.location.href);
    url.hash = el.id;

    let quote = excerpt;
    if (quote.length > EXCERPT_LENGTH) quote = quote.slice(0, EXCERPT_LENGTH) + " …";

    return `📍 ${trail.join(" › ")}\n${url.href}\n> ${quote}`;
  }

  async function copyReference(el, section, n, excerpt) {
    const ref = reference(el, section, n, excerpt);
    try {
      await navigator.clipboard.writeText(ref);
      toast(t.copied);
    } catch (e) {
      // Fallback for browsers without the async clipboard API.
      const area = document.createElement("textarea");
      area.value = ref;
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      const ok = document.execCommand("copy");
      area.remove();
      toast(ok ? t.copied : t.failed);
    }
    history.replaceState(null, "", `#${el.id}`);
    flash(el);
  }

  let toastEl = null;
  let toastTimer = null;
  function toast(message) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.className = "la-toast";
      toastEl.setAttribute("role", "status");
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = message;
    toastEl.classList.add("la-show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove("la-show"), 2500);
  }

  function flash(el) {
    el.classList.remove("la-flash");
    void el.offsetWidth; // restart the animation
    el.classList.add("la-flash");
  }

  // The ids above did not exist when the browser tried to follow the URL hash.
  if (window.location.hash.length > 1) {
    const target = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
    if (target && target.classList.contains("la-ref-target")) {
      target.scrollIntoView({ block: "center" });
      flash(target);
    }
  }

  // "New since your last visit" badge on the changelog box.
  const changes = content.querySelector(".la-changes[data-latest]");
  const storageKey = `la-last-visit:${window.location.pathname}`;
  let lastVisit = null;
  try {
    lastVisit = localStorage.getItem(storageKey);
    localStorage.setItem(storageKey, new Date().toISOString().slice(0, 10));
  } catch (e) {
    // Storage unavailable (private mode etc.): no badge, nothing else breaks.
  }
  if (changes && lastVisit && changes.dataset.latest > lastVisit) {
    const title = changes.querySelector(".callout-title-container") || changes.querySelector(".callout-header");
    if (title) {
      const badge = document.createElement("span");
      badge.className = "la-new-badge";
      badge.textContent = t.isNew;
      title.appendChild(badge);
    }
  }
})();
