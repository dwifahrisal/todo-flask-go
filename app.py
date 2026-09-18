from flask import Flask, request, jsonify, g
import sqlite3, os

app = Flask(__name__)
DB = "todos.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = sqlite3.connect(DB)
    db.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER DEFAULT 0)")
    db.commit()
    db.close()

@app.get("/todos")
def list_todos():
    rows = get_db().execute("SELECT * FROM todos ORDER BY id DESC").fetchall()
    return jsonify([dict(r) for r in rows])

@app.post("/todos")
def add_todo():
    data = request.get_json(force=True)
    if not data.get("title"):
        return jsonify({"error": "title wajib"}), 400
    cur = get_db().execute("INSERT INTO todos (title) VALUES (?)", (data["title"],))
    get_db().commit()
    return jsonify({"id": cur.lastrowid, "title": data["title"], "done": 0}), 201

@app.patch("/todos/<int:todo_id>")
def toggle_todo(todo_id):
    get_db().execute("UPDATE todos SET done = 1 - done WHERE id = ?", (todo_id,))
    get_db().commit()
    return jsonify({"ok": True})

@app.delete("/todos/<int:todo_id>")
def delete_todo(todo_id):
    get_db().execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    get_db().commit()
    return jsonify({"ok": True})

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
