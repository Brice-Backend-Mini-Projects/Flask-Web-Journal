# Project Structure

```plaintext
flask_web_journal/
│
├── pyproject.toml
├── run.py
├── .env
│
├── instance/
│   └── journal_db.db
│
├── src/
│   └── flask_web_journal/
│       ├── __init__.py
│       ├── extensions.py
│       ├── main.py
│       │
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py
│       │
│       ├── routes/
│       │   ├── __init__.py
│       │   └── journal.py
│       │
│       ├── services/
│       │   └── journal_service.py
│       │
│       └── templates/
│           ├── base.html
│           ├── index.html
│           └── entry.html
│
├── tests/
├── .gitignore
├── README.md
└── uv.lock
```
