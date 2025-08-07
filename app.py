from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from skin_ai import analyze_skin# This should be your analysis function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return "No file uploaded", 400

    image = request.files['image']
    if image.filename == '':
        return "No selected file", 400

    filename = secure_filename(image.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(image_path)

    # Call the skin analysis logic
    result = analyze_skin(image_path)

    return render_template('result.html', result=result, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)

