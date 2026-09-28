-- learn-anything: shared Quarto filter for all books.
--
-- * Attaches learn-anything.js (paragraph references, "new since last visit").
-- * Renders the chapter changelog from front matter:
--
--     changes:
--       - date: 2026-09-28
--         note: "Beispiel zum Aorist ergänzt (Abschnitt 3.2)"
--
--   as a collapsed callout at the top of the chapter, newest entry first.

local LABELS = {
  de = "Zuletzt überarbeitet",
  en = "Last revised",
  el = "Τελευταία αναθεώρηση",
  es = "Última revisión",
  fr = "Dernière révision",
  it = "Ultima revisione",
}

local function label_for(meta)
  local lang = meta.lang and pandoc.utils.stringify(meta.lang) or "en"
  return LABELS[lang] or LABELS[lang:sub(1, 2)] or LABELS.en
end

local function changelog(meta)
  if not meta.changes or #meta.changes == 0 then
    return nil
  end

  local entries = {}
  for _, change in ipairs(meta.changes) do
    table.insert(entries, {
      date = pandoc.utils.stringify(change.date or ""),
      note = change.note or pandoc.Inlines({}),
    })
  end
  table.sort(entries, function(a, b) return a.date > b.date end)

  local items = {}
  for _, e in ipairs(entries) do
    local inlines = pandoc.Inlines({ pandoc.Strong(e.date), pandoc.Str(":"), pandoc.Space() })
    inlines:extend(pandoc.Inlines(e.note))
    table.insert(items, { pandoc.Plain(inlines) })
  end

  local callout = quarto.Callout({
    type = "note",
    appearance = "simple",
    collapse = true,
    title = label_for(meta) .. ": " .. entries[1].date,
    content = pandoc.Blocks({ pandoc.BulletList(items) }),
  })

  return pandoc.Div({ callout }, pandoc.Attr("", { "la-changes" }, { ["data-latest"] = entries[1].date }))
end

function Pandoc(doc)
  if quarto.doc.is_format("html") then
    quarto.doc.add_html_dependency({
      name = "learn-anything",
      version = "0.1.0",
      scripts = { { path = "learn-anything.js", afterBody = true } },
    })

    local box = changelog(doc.meta)
    if box then
      doc.blocks:insert(1, box)
    end
  end
  return doc
end
