# Code Translator Web Application

This project is a web-based code translator that allows users to input code in one programming language and convert it to another. It utilizes a Flask web server to handle user requests and integrates with a code translation API.

## Project Structure

- `app.py`: The main application file that sets up the Flask web server and handles routing.
- `templates/index.html`: The HTML structure for the user interface, including a form for code input and language selection.
- `static/style.css`: CSS styles for the web application, defining the visual appearance of the UI elements.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Setup Instructions

1. Ensure you have Python installed on your machine.
2. Create a virtual environment (optional but recommended):
   - Run `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On macOS/Linux: `source venv/bin/activate`
3. Install the required packages:
   - Run `pip install -r requirements.txt`
4. Start the Flask server:
   - Run `python app.py`
5. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Deployment

To deploy this application online, consider using platforms like Heroku, Vercel, or any cloud service that supports Python web applications. Follow their specific deployment instructions for Flask applications.

## Usage

Once the application is running, you can paste your code into the provided input field, select the target programming language for conversion, and submit the form to receive the translated code.