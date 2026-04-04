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

## Assessment Components
| Component | Description | Grading |
|---|---|---|
| Simulations (7 total) | In-class, 20-30 min play + setup/debrief | Participation credit |
| Empirical homeworks (2-3) | Real data analysis | TA graded |
| Theory quizzes | Timed, in-class, auto-graded | Auto-graded |
| In-class activities | Polls, quick problems, discussion | Completion credit |
| Individual presentation | 1 slide, 3 min, random selection + Zoom backup | Light rubric |

## Status
- [ ] Copy and adapt site scaffold from fall2025-site
- [ ] Update syllabus for new assessment structure
- [ ] Build schedule around simulation days
- [x] Set up fall2026-extra/

## Last Session
- **Date**: 2026-04-03
- Designed full course assessment structure (simulations, empirical HW, timed quizzes, in-class activities, 1-slide individual presentations with random selection)
- Established teaching ecosystem architecture: slides/, book/, gaming/, commons/ under healthcare-markets/, with VS Code workspace linking all components plus semester folders
- Detailed game mechanics for simulations 1A (buy/skip insurance) and 1B (set premiums, compete for simulated buyers)
- Next: build 1A and 1B implementations, starting with 1A (scaffold FastAPI + WebSocket project, then game logic)
