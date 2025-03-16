from flask import Flask, render_template, request, jsonify
import sqlite3
import razorpay
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('academy.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 email TEXT UNIQUE,
                 password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS payments
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 payment_id TEXT,
                 amount INTEGER,
                 currency TEXT,
                 status TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Razorpay Configuration
razorpay_client = razorpay.Client(auth=(
    os.getenv('RAZORPAY_KEY_ID'),
    os.getenv('RAZORPAY_KEY_SECRET')
))

@app.route('/')
def home():
    return render_template('index.html')

# Add other endpoints from previous implementation (register, login, create_order, verify_payment)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)