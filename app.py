from flask import Flask
from sqlalchemy import create_engine
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise Exception("DATABASE_URL not found. Set it in Render Environment Variables.")

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}  # required for Supabase
)

@app.route("/")
def home():
    return "Backend connected to Supabase"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)