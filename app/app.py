from flask import Flask
import os
import pymysql

# Load config from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
APP_PORT = int(os.getenv("APP_PORT", 5000))

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        conn.close()
        return f"Connected to DB {DB_NAME} successfully!"
    except Exception as e:
        return f"Failed to connect to DB: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)

