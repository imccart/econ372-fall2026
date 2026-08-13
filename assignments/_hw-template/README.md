# Econ 372 — Empirical Homework

This is the starting template for the empirical homeworks. You will do the
analysis in R or Python with an AI coding assistant, and hand in one document
that reads cleanly and has your code underneath it. Two starters are provided, so
use whichever you prefer. You do not need to learn a new language, and the AI
assistant writes most of the code.

## What's in here

- `code/analysis.ipynb` — a Python **Jupyter notebook** starter.
- `code/analysis.qmd` — a **Quarto** starter (R or Python).
- `data/` — put the homework's data files here. This folder is gitignored, so the
  raw data is never uploaded to GitHub.
- `README.md` — this file.

Use one starter and delete the other if you like.

## 1. Set up your tool

- **Jupyter notebook (`analysis.ipynb`):** open it in VS Code with the Python and
  Jupyter extensions, or in Jupyter through
  [Anaconda](https://www.anaconda.com/download). This is the lighter setup if you
  are newer to this.
- **Quarto (`analysis.qmd`):** install [Quarto](https://quarto.org/docs/get-started/)
  and open it in VS Code or RStudio. Quarto renders the most polished document.

## 2. Add the data

Download the homework's data files from the link in the assignment and put them in
the `data/` folder. Because `data/` is gitignored, the data stays on your computer
and is never pushed to GitHub.

## 3. Do the work

Write your analysis in your starter, using an AI coding assistant to help with the
code. What is graded is your economic reasoning, not the code itself. Keep it
tidy: a section per question, your code and its output shown, figures labeled with
units, and each answer written as a sentence or two that states the number.

## 4. Hand in a clean document with your code underneath

Run everything so your output shows, then commit your work. Your notebook or
Quarto file is what makes the submission both readable and gradable.

- **Jupyter:** commit the executed `analysis.ipynb`. GitHub displays notebooks
  with their output, so it already reads as a clean document.
- **Quarto:** render it (the Render button, or `quarto render`) to a
  self-contained `report.html` or `report.pdf`, and commit both the `.qmd` and the
  rendered file.

Either way, keep the source file (`.ipynb` or `.qmd`) in the repository. That is
what carries your code.

## 5. Put it on GitHub as a private repository

- Create a new repository at <https://github.com/new> and set it to **Private**.
- Connect this folder and push it:

  ```
  git init
  git add .
  git commit -m "Homework"
  git branch -M main
  git remote add origin https://github.com/<your-username>/<your-repo>.git
  git push -u origin main
  ```

- Add the instructor and TA as collaborators so we can open your repository
  (repository Settings, then Collaborators, then Add people):
  - `imccart`
  - `scai5`

## 6. Submit

On Commons, open the Homework submission card and paste your repository link for
this assignment. You can update the link anytime; the time you submit is what is
recorded.

New to git or GitHub? Your TA runs help sessions to get you set up, so you do not
have to figure it out alone.
