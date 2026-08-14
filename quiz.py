from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return "Hello, World! Welcome to my Flask app."

# Start the local development server
if __name__ == '__main__':
    app.run(debug=True)
