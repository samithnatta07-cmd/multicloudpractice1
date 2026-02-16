from flask import Flask, jsonify, send_file
import pymysql
import config

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )

@app.route("/skills")
def skills():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM skills")
    data = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

@app.route("/certifications")
def certifications():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM certifications")
    data = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

@app.route("/projects")
def projects():
    return send_file(
        "projects/aws-project.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
