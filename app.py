from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from llm.summary_model import summarize_code
from llm.debug_model import explain_error
from utils import run_code_and_get_errors
from database import save_submission

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py', 'java', 'cpp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    summary = ""
    debug = ""

    if request.method == "POST":
        # Check if file uploaded
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(filepath)
                with open(filepath, 'r', encoding='utf-8') as f:
                    code = f.read()

        # If pasted code also exists, it will override file content
        if request.form.get("code"):
            code = request.form["code"]

        level = request.form["level"]

        summary = summarize_code(code, level)
        error_output = run_code_and_get_errors(code)
        debug = explain_error(error_output)

        save_submission(code, summary, debug)

    return render_template("index.html", code=code, summary=summary, debug=debug)

if __name__ == "__main__":
    app.run(debug=True)
