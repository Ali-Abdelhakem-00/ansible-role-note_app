from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_NAME = 'notes.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, note TEXT, timestamp TEXT)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form['note']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO notes (note, timestamp) VALUES (?, ?)', (note, timestamp))
        conn.commit()
        conn.close()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT note, timestamp FROM notes ORDER BY id DESC')
    notes = c.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80)
