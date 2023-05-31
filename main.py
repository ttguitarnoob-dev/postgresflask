from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

#connect postgresql

connection = psycopg2.connect(
    host = "0.0.0.0",
    port = "2000",
    database = "stink.db",
    user = "travis",
    password = "Bungfodder123"
)
cursor = connection.cursor()

#Routes

@app.route('/read')
def read():
    cursor.execute("SELECT * from")