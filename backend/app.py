from flask import Flask
from flask_cors import CORS
from routes.ask_handler import ask_handler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Register route
app.register_blueprint(ask_handler)

if __name__ == "__main__":
    app.run(debug=True)
