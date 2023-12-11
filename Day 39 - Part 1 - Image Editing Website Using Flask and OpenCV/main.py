from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
import cv2

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_image(filename, operation):
    path = f"C:/Users/Subhash_Jadhav/Desktop/work/100-days-of-code-The-complete-python-pro-bootcamp/Day 39 - Part 1 - Image Editing Website Using Flask and OpenCV/uploads/{
        filename}"
    img = cv2.imread(path)

    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(
                f"C:/Users/Subhash_Jadhav/Desktop/work/100-days-of-code-The-complete-python-pro-bootcamp/Day 39 - Part 1 - Image Editing Website Using Flask and OpenCV/processed/{filename}", imgProcessed)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == 'POST':
        operation = request.form.get('operation')
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "File not found Error"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return "File not selected Error"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            file.save(os.path.join(
                basedir, app.config['UPLOAD_FOLDER'], filename))
            process_image(filename, operation)
            return render_template("index.html")
    return render_template("index.html")


app.run(debug=True)
