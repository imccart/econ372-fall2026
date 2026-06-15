# Econ 372 — Fall 2026 Course Site

## Overview
Semester-specific Quarto site for Econ 372 (Health Economics) at Emory, Fall 2026. This repo is thin — syllabus, schedule, assignment descriptions, quiz content. Durable content lives elsewhere.

## Related Components
- **Slides**: `teaching/healthcare-markets/slides/`
- **Book**: `teaching/healthcare-markets/book/`
- **Gaming (simulations)**: `teaching/healthcare-markets/gaming/`
- **Commons (platform)**: `teaching/healthcare-markets/commons/`
- **Assignments (private)**: `econ-372/assignments/` — exam masters, homework masters
- **Semester data (private)**: `econ-372/fall2026-extra/` — grades, enrollment, sim logs

## Based On
Fall 2025 site: `../fall2025-site/`

## Assessment Components (300 pts, ~80% in-class)
| Component | Points | Grading |
|---|---|---|
| Attendance | 20 | 1 pt/check-in (Commons) |
| Q&A panel | 45 | 4-level rubric when randomly drawn |
| Q&A audience | 30 | 2 pts/question (Commons queue), cap 30 |
| Simulations | 25 | best 5 of 7; 3 play + 2 reflection |
| Quizzes | 60 | best 5 of 6, 12 pts, in-class auto-graded (Commons) |
| Midterm | 60 | in-class |
| Empirical homework | 60 | best 2 of 3, AI-required, TA-graded |

Full spec: `healthcare-markets/assessment.md`. (Supersedes the earlier draft that had a 1-slide individual presentation + generic in-class activities.)

## Status
- [x] Copy and adapt site scaffold from fall2025-site (`_quarto.yml`, infra, index, syllabus)
- [x] Update syllabus for the new assessment structure + AI-required policy
- [x] Schedule built — 28 Tue/Thu sessions (8/27–12/8), 4 modules, all 7 sims, all 6 quizzes, HW due-date rows. **Midterm Thu 11/19** covers insurance + physicians + hospitals (before Thanksgiving, not adjacent to a break; 11/17 review). Fall-2025-style linked module tables with slides + book-chapter + assignment icons. **No per-class Detail pages** (dropped — redundant with slides + a maintenance burden). Topics/readings + exact quiz↔sim placement still tunable
- **Gotcha:** absolute local links (`/assignments/…`) render with a Windows backslash (`..\`) and break; use relative `.qmd` links (`../assignments/homework1.qmd`) and always `quarto render` the whole project (per-file render breaks cross-`.qmd` resolution)
- [x] Course logistics filled — Tue/Thu 2:30–3:45pm, New Psychology Building 225, term 8/26–12/9/2026, office hours Thu 1–2pm RRR 418 (TA name still TBD in `syllabus.qmd`)
- [ ] Carry over / refresh resources (worksheets, reviews); `resources/index.qmd` is a placeholder
- [ ] Confirm the GitHub repo name used in `_quarto.yml` (`imccart/econ372-fall2026`) and create it
- [x] Set up fall2026-extra/

## Last Session
- **Date**: 2026-06-15
- Scaffolded the buildable Quarto site from fall2025-site: copied infra (`_extensions/`, `files/`, `html/`), wrote `_quarto.yml` (navbar/sidebar for the new structure — no exam/project pages), an R-free `index.qmd`, and a `syllabus.qmd` adapted to the 300-pt assessment + AI-required policy (grade tables as plain markdown, not R chunks). Added placeholder `schedule/index.qmd` and `resources/index.qmd`.
- Site renders clean (`quarto render`, 8 pages, no warnings, citations resolve). The AI-era assignments (index + homework1-3) are wired into the nav/sidebar.
- Dropped the fall2025 Google Drive bib-fetch from `index.qmd` (uses the static `files/bib/references.bib` instead, so the render needs no Google auth or kernel).
- Open: real schedule + logistics (all TBD placeholders), resources to carry over, confirm/create the `econ372-fall2026` repo.
