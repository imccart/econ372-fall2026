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
- [x] Repo created + site **published** — live at `imccart.github.io/econ372-fall2026/` (GitHub Pages from `main/docs`; push over SSH with `GIT_SSH_COMMAND` = system OpenSSH). Update loop: edit → `quarto render` → commit → push (Pages auto-rebuilds)
- [x] Set up fall2026-extra/

## Last Session
- **Date**: 2026-06-15
- Scaffolded the site from fall2025-site and **published it** — live at `imccart.github.io/econ372-fall2026/`. Wrote `_quarto.yml`, R-free `index.qmd` (dropped the fall2025 Google-Drive bib-fetch; uses static `files/bib/`), and `syllabus.qmd` (300-pt assessment + AI-required policy, markdown grade tables). Logistics filled (Tue/Thu 2:30–3:45, New Psych 225, 8/26–12/9, OH Thu 1–2 RRR418).
- Built the full **28-session schedule** with linked module tables (slides + book-chapter + homework icons) and an **Assessment** column (Quiz/Sim/Midterm/homework; blank = Q&A day). Midterm Thu 11/19 over ins+phys+hosp. Per-class Detail pages deliberately dropped (redundant with slides). All links verified (no Windows-backslash breakage; see Gotcha above).
- **Open:** TA name (TBD in `syllabus.qmd`); resources carry-over (`resources/index.qmd` placeholder); optional per-class readings refinement.
