from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = "reelreads-secret-key-cs361"

# ── Sample data (fake/test data — no real DB needed) ──────────────────────────
ITEMS = [
    {"id": 1,  "type": "book",  "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams",       "genre": "Sci-Fi",    "rating": 4.8, "description": "A comedic sci-fi adventure about the end of Earth and what comes after.", "time_to_finish": "~5 hours"},
    {"id": 2,  "type": "book",  "title": "To Kill a Mockingbird",                "author": "Harper Lee",          "genre": "Drama",     "rating": 4.9, "description": "A powerful story of racial injustice and childhood innocence in the American South.", "time_to_finish": "~7 hours"},
    {"id": 3,  "type": "book",  "title": "Dune",                                 "author": "Frank Herbert",       "genre": "Sci-Fi",    "rating": 4.7, "description": "An epic tale of politics, religion, and ecology on a desert planet.", "time_to_finish": "~21 hours"},
    {"id": 4,  "type": "book",  "title": "Pride and Prejudice",                  "author": "Jane Austen",         "genre": "Romance",   "rating": 4.6, "description": "A witty exploration of manners, marriage, and love in 19th-century England.", "time_to_finish": "~10 hours"},
    {"id": 5,  "type": "book",  "title": "The Name of the Wind",                 "author": "Patrick Rothfuss",    "genre": "Fantasy",   "rating": 4.8, "description": "A legendary hero recounts his extraordinary life in this epic fantasy.", "time_to_finish": "~18 hours"},
    {"id": 6,  "type": "movie", "title": "Inception",                            "author": "Christopher Nolan",   "genre": "Sci-Fi",    "rating": 4.8, "description": "A thief who steals corporate secrets through dream-sharing technology.", "time_to_finish": "~2.5 hours"},
    {"id": 7,  "type": "movie", "title": "The Grand Budapest Hotel",             "author": "Wes Anderson",        "genre": "Comedy",    "rating": 4.6, "description": "A whimsical adventure of a legendary hotel concierge and his lobby boy.", "time_to_finish": "~1.7 hours"},
    {"id": 8,  "type": "movie", "title": "Parasite",                             "author": "Bong Joon-ho",        "genre": "Drama",     "rating": 4.9, "description": "A dark, Oscar-winning thriller about class inequality in South Korea.", "time_to_finish": "~2.2 hours"},
    {"id": 9,  "type": "movie", "title": "Spirited Away",                        "author": "Hayao Miyazaki",      "genre": "Fantasy",   "rating": 4.9, "description": "A young girl wanders into a world of spirits and must work to free her parents.", "time_to_finish": "~2 hours"},
    {"id": 10, "type": "movie", "title": "Everything Everywhere All at Once",    "author": "The Daniels",         "genre": "Sci-Fi",    "rating": 4.8, "description": "A middle-aged laundromat owner discovers she must connect with parallel universe versions of herself.", "time_to_finish": "~2.5 hours"},
]

GENRES = sorted(set(i["genre"] for i in ITEMS))

def get_favorites():
    return session.get("favorites", [])

def get_item_by_id(item_id):
    return next((i for i in ITEMS if i["id"] == item_id), None)


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Home page — IH#1: explains what the app does and why."""
    favorites = get_favorites()
    return render_template("index.html", items=ITEMS, genres=GENRES, favorites=favorites)


@app.route("/search")
def search():
    """Search page — IH#7: multiple search approaches (keyword + genre + type filter)."""
    query   = request.args.get("q", "").strip().lower()
    genre   = request.args.get("genre", "").strip()
    kind    = request.args.get("type", "").strip()   # "book" | "movie" | ""

    results = ITEMS
    if query:
        results = [i for i in results if query in i["title"].lower() or query in i["author"].lower()]
    if genre:
        results = [i for i in results if i["genre"] == genre]
    if kind:
        results = [i for i in results if i["type"] == kind]

    favorites = get_favorites()
    return render_template("search.html", results=results, genres=GENRES,
                           query=query, genre=genre, kind=kind, favorites=favorites)


@app.route("/item/<int:item_id>")
def item_detail(item_id):
    """Detail page — IH#3: users can choose to read more about an item."""
    item = get_item_by_id(item_id)
    if not item:
        return redirect(url_for("index"))
    favorites = get_favorites()
    return render_template("detail.html", item=item, favorites=favorites)


@app.route("/favorites")
def favorites():
    """Favorites page — IH#5: users can manage/undo their saved items."""
    fav_ids = get_favorites()
    fav_items = [get_item_by_id(i) for i in fav_ids if get_item_by_id(i)]
    return render_template("favorites.html", favorites=fav_items)


@app.route("/favorite/toggle/<int:item_id>", methods=["POST"])
def toggle_favorite(item_id):
    """Toggle favorite — IH#5/8: reversible action, confirmation handled in JS."""
    favs = get_favorites()
    if item_id in favs:
        favs.remove(item_id)
        action = "removed"
    else:
        favs.append(item_id)
        action = "added"
    session["favorites"] = favs
    return jsonify({"action": action, "count": len(favs)})


@app.route("/favorite/remove/<int:item_id>", methods=["POST"])
def remove_favorite(item_id):
    """Remove from favorites — IH#8: only called after JS confirmation prompt."""
    favs = get_favorites()
    if item_id in favs:
        favs.remove(item_id)
    session["favorites"] = favs
    return redirect(url_for("favorites"))


@app.route("/clear_favorites", methods=["POST"])
def clear_favorites():
    """Clear all favorites — IH#8: only called after JS confirmation."""
    session["favorites"] = []
    return redirect(url_for("favorites"))


if __name__ == "__main__":
    app.run(debug=True)
