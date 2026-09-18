# todo-flask

Todo API kecil pakai Flask + SQLite, gak ada frontend-nya, pure API.

## endpoints

| method | path | fungsi |
|---|---|---|
| GET | /todos | list semua todo |
| POST | /todos | tambah todo (`{"title": "..."}`) |
| PATCH | /todos/:id | toggle done |
| DELETE | /todos/:id | hapus |

## run

```bash
pip install -r requirements.txt
python3 app.py
```

---

## Contact

Need a custom setup, API key, or integration? Reach out: **Fahrissal052@gmail.com**

If this project saved you time, consider [supporting on Saweria](https://saweria.co/dwifahrisal) ☕
