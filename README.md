# ReelReads — CS 361 Milestone #1

A book and movie recommendation web app built with Flask.

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/reelreads.git
cd reelreads
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

Then open your browser to: **http://127.0.0.1:5000**

---

## Features

- Browse books and movies on the home page
- Search by keyword, genre, and/or type (IH#7)
- Save/remove favorites with session-based persistence (IH#5)
- Detail pages with full descriptions and time estimates (IH#2, IH#3)

---

## Inclusivity Heuristics Map

| # | Heuristic | Where reflected |
|---|-----------|-----------------|
| IH#1 | Explain benefits | Hero section feature pills; nav tooltips; new-feature banner |
| IH#2 | Explain costs | Time commitment shown on every card and detail sidebar; "no account required" note |
| IH#3 | Control info flow | Short descriptions with "read more" link; dismissible banner; optional details page |
| IH#4 | Keep familiar features | Consistent nav on every page; standard icons (★, ✕); familiar search-bar layout |
| IH#5 | Undo/backtrack | Save is reversible; breadcrumb + Back button on detail; Clear Filters link |
| IH#6 | Explicit path | Toast confirms actions; "Next steps" buttons at page bottoms; empty-state guidance |
| IH#7 | Multiple approaches | Search by keyword AND genre AND type simultaneously; dropdowns auto-submit OR button |
| IH#8 | Mindful tinkering | JS confirm() before remove; two-message confirm before Clear All |

---

## Quality Attributes

| Attribute | Non-functional Requirement | Where demonstrated |
|-----------|---------------------------|--------------------|
| Usability | All 8 Inclusivity Heuristics reflected | See IH map above |
| Maintainability | No function in app.py exceeds 15 lines | Verified in app.py |
| Responsiveness | Home page loads in < 2 seconds | Demo by restarting app 3×  |

---

## User Stories

1. **As a user, I want to search for books/movies by genre so that I can find content that matches my mood.**
   - *Given* the user is on the Search page, *when* they select "Sci-Fi" from the genre dropdown, *then* they see only Sci-Fi items.

2. **As a user, I want to save items to a Favorites list so that I can remember things I want to read or watch later.**
   - *Given* the user clicks ☆ Save on any card, *when* the request completes, *then* the button changes to ★ Saved and a toast confirms the action.

3. **As a user, I want to see how long a book or movie takes to finish so that I can decide if I have time for it.**
   - *Given* the user is on any page (home, search, or detail), *when* they look at any item card, *then* they see a time estimate (e.g., "~5 hours").

---

## Notes

- Uses test/fake data only — no real database or API keys required.
- Do **not** commit `.env` files or secret keys (covered by `.gitignore`).
