from flask import Flask, render_template, request, jsonify
from metadata import extract_metadata

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    file_path = f"uploads/{file.filename}"
    file.save(file_path)

    metadata = extract_metadata(file_path)
    return jsonify(metadata)

if __name__ == "__main__":
    app.run(debug=True)