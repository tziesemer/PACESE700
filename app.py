import os
import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Fixed: Load secret from environment variable
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Fixed: Parameterized query prevents SQL Injection
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return str(cursor.fetchall())

@app.route("/ping")
def ping():
    host = request.args.get("host")
    # Fixed: subprocess without shell=True prevents Command Injection
    subprocess.run(["ping", "-c", "1", host], check=True)
    return "Pinged"