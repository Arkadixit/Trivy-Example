from flask import Flask
import psycopg2, os
import sys
 
app = Flask(__name__)
db_url = os.getenv("DATABASE_URL", None)
if db_url is None:
    print("No db url from env.")
    sys.exit(1)
 
@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
 
        # Insérer une nouvelle visite
        cur.execute("INSERT INTO visits DEFAULT VALUES;")
        conn.commit()
 
        # Récupérer le nombre total de visites
        cur.execute("SELECT COUNT(*) FROM visits;")
        count = cur.fetchone()[0]
 
        cur.close()
        conn.close()
 
        return f"👋 Hello from Flask! This page has been visited {count} times."
    except Exception as e:
        return f"❌ Database error: {e}"
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)