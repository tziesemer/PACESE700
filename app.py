import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 1. Intentional Hardcoded Secret (Triggers Gitleaks)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7REALKEY1"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY9876543210"
GITHUB_TOKEN = "ghp_9876543210abcdefghijklmnopqrstuv1234"

@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # 2. Intentional SQL Injection (Triggers Semgrep)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return str(cursor.fetchall())

@app.route("/ping")
def ping():
    host = request.args.get("host")
    # 3. Intentional OS Command Injection (Triggers Semgrep)
    os.system("ping -c 1 " + host)
    return "Pinged"
