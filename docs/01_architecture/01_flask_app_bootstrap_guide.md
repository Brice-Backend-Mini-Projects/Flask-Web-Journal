# Flask Application Bootstrap Guide (src Layout)

This document outlines the high-level steps for setting up a properly
structured Flask application using a `src/` layout and the application
factory pattern.

The goal is clean architecture, separation of concerns, and scalability
from day one.

------------------------------------------------------------------------

## 1. Create the Project Root

At the top level of your project:

flask_web_journal/ │ ├── pyproject.toml ├── run.py ├── .env ├──
instance/ └── src/

### Purpose of Each:

-   **pyproject.toml** -- Dependency and project configuration
-   **run.py** -- Entry point for development and deployment
-   **.env** -- Environment variables (local development only)
-   **instance/** -- Runtime files (SQLite DB, local config, etc.)
-   **src/** -- Application source code

------------------------------------------------------------------------

## 2. Establish the `src/` Layout

Inside `src/`, create a package named after your project:

src/ └── flask_web_journal/ ├── **init**.py ├── config.py ├──
extensions.py ├── routes/ ├── services/ ├── models/ └── templates/

### Responsibilities:

-   **`__init__.py`**
    -   Application factory
    -   Config loading
    -   Extension initialization
    -   Blueprint registration
-   **`config.py`**
    -   Environment-based configuration
    -   Reads from `.env`
    -   Defines dev/test/prod settings
-   **`extensions.py`**
    -   Initialize reusable Flask extensions
    -   Keeps factory clean and modular
-   **`routes/`**
    -   Blueprint modules
    -   Request handling only
    -   No business logic
-   **`services/`**
    -   Business logic layer
    -   Keeps routes thin
-   **`models/`**
    -   Database models (if using ORM)
-   **`templates/`**
    -   Jinja templates
    -   Organized by feature if needed

------------------------------------------------------------------------

## 3. Use the Application Factory Pattern

Inside `__init__.py`, define a `create_app()` function that:

1.  Creates the Flask instance
2.  Loads configuration
3.  Initializes extensions
4.  Registers blueprints
5.  Returns the app

This pattern enables: - Clean testing - Multiple environments - Scalable
architecture - Production deployment compatibility

------------------------------------------------------------------------

## 4. Configure Environment Variables

Use a `.env` file for local development.

Example contents:

-   SECRET_KEY
-   DATABASE_URL
-   FLASK_ENV

Do not hardcode secrets in `config.py`.

The config class should read values from environment variables and
provide safe fallbacks where appropriate.

------------------------------------------------------------------------

## 5. Configure the Instance Folder

The `instance/` directory stores runtime artifacts such as:

-   SQLite database files
-   Local configuration overrides
-   Generated files

It should:

-   Exist at the project root
-   Be excluded from version control
-   Not contain application code

This keeps runtime data separate from source code.

------------------------------------------------------------------------

## 6. Create the Entry Point (`run.py`)

`run.py` should:

-   Import `create_app`
-   Instantiate the app
-   Expose it for development and WSGI servers

This file should contain no business logic.

It exists solely to run the application.

------------------------------------------------------------------------

## 7. Running the Application

From the project root:

1.  Activate virtual environment
2.  Ensure `.env` exists
3.  Run the Flask app via CLI or WSGI server

Always run from project root to maintain predictable relative paths.

------------------------------------------------------------------------

## 8. Separation of Concerns

A properly structured Flask app follows this responsibility model:

  Layer         Responsibility
  ------------- ------------------------------------
  Routes        Handle HTTP requests and responses
  Services      Business logic
  Models        Data structure and persistence
  Config        Environment-driven configuration
  Instance      Runtime data
  Entry Point   Application startup

Routes should never contain complex logic. Business logic should never
depend on request context. Configuration should never be hardcoded.

------------------------------------------------------------------------

## 9. Testing Considerations

To support testing:

-   Keep the app factory pattern
-   Allow test configuration override
-   Use separate test database configuration
-   Avoid global state in route modules

Testing becomes straightforward when architecture is clean.

------------------------------------------------------------------------

## 10. Production Readiness Path

Once the basic app works, the next steps typically include:

-   Database integration (SQLAlchemy)
-   Migration support
-   Authentication
-   Logging configuration
-   Docker setup
-   Gunicorn configuration
-   CI/CD integration

The foundational structure described above supports all of these without
refactoring.

------------------------------------------------------------------------

## Architectural Principles Reinforced

-   Source code and runtime artifacts are separated
-   Configuration is environment-driven
-   Business logic is not mixed with routing
-   The app is scalable from day one
-   Deployment does not require structural changes

------------------------------------------------------------------------

This structure is intentionally minimal but professionally aligned.\
It avoids overengineering while preserving long-term flexibility.
