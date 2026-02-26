from flask import Flask
from sqlalchemy import create_engine
from config import DATABASE_URL

app = Flask(__name__)

engine = create_engine(DATABASE_URL)

@app.route("/")
def home():
    return "Backend connected to Supabase"

if __name__ == "__main__":
    app.run()