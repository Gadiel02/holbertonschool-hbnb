#!/usr/bin/python3
import os
import sqlite3
from part3.hbnb.app import create_app

def execute_sql_script(conn, script_path):
    """Executes a SQL script file against the SQLite database connection."""
    try:
        with open(script_path, 'r') as script:
            conn.executescript(script.read())
        print(f"Successfully executed: {script_path}")
    except Exception as e:
        print(f"Error executing script {script_path}: {e}")

def initialize_database():
    """Initializes the SQLite database by running schema and seed scripts."""
    base_dir = os.path.dirname(__file__)
    db_path = "/Users/priscilalopez/holbertonschool-hbnb/instance/development.db"
    scripts_dir = os.path.join(base_dir, "hbnb/app/persistence")

    # Check if the scripts directory exists
    if not os.path.exists(scripts_dir):
        print("Error: The 'persistence' folder does not exist.")
        return

    # Define paths for schema and seed scripts
    scripts_path = os.path.join(scripts_dir, "scripts.sql")
    seed_path = os.path.join(scripts_dir, "seed.sql")

    # Execute schema and seed scripts
    print("Initializing database...")
    with sqlite3.connect(db_path) as conn:
        execute_sql_script(conn, scripts_path)
        execute_sql_script(conn, seed_path)
    print("Database initialization complete.")

app = create_app()

# Run database initialization within the app context
with app.app_context():
    initialize_database()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
