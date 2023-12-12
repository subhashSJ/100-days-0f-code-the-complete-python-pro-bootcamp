from flask import Flask, render_template, request, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
import cv2

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif'}
SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_image(filename, operation):
    path = f"{basedir}/uploads/{
        filename}"
    img = cv2.imread(path)

    match operation:
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(
                f"{basedir}/processed/{filename}", imgProcessed)
            return f"/processed/{filename}"
        case "cwebp":
            # Assuming filename doesn't contain '.
            cv2.imwrite(
                f"{basedir}/processed/{filename.split('.')[0]}.webp", img)
            return f"/processed/{filename.split('.')[0]}.webp"
        case "cjpg":
            # Assuming filename doesn't contain '.
            cv2.imwrite(
                f"{basedir}/processed/{filename.split('.')[0]}.jpg", img)
            return f"/processed/{filename.split('.')[0]}.jpg"
        case "cpng":
            # Assuming filename doesn't contain '.
            cv2.imwrite(
                f"{basedir}/processed/{filename.split('.')[0]}.png", img)
            return f"/processed/{filename.split('.')[0]}.png"
        case "blur":
            cv2.imwrite(
                f"{basedir}/processed/{filename}", cv2.GaussianBlur(
                    img, (15, 15), 0)
            )
            return f"/processed/{filename}"
        case "rotate90":
            rows, cols, _ = img.shape
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
            rotated_img = cv2.warpAffine(img, M, (cols, rows))

            cv2.imwrite(f"{basedir}/processed/{filename}", rotated_img)
            return f"/processed/{filename}"
        
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
            new_file = process_image(filename, operation)
            flash(
                f"Your image has been processed successfully and is available <a href='{new_file}'  target='_target'>here</a>")
            return render_template("index.html")
    return render_template("index.html")


@app.route("/processed/<filename>")
def processed_image(filename):
    return send_from_directory(os.path.join(basedir, PROCESSED_FOLDER), filename)


app.run(debug=True)
