from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

ENDPOINT = 'https://api.npoint.io/2c2e28dada5b385d1194'


@app.route('/')
def home():
    blogs = requests.get(ENDPOINT)
    return render_template('index.html', blogs=blogs.json())


@app.route('/about')
def about():
    blogs = requests.get(ENDPOINT)
    return render_template('about.html', blogs=blogs.json())


@app.route('/contact')
def contact():
    blogs = requests.get(ENDPOINT)
    return render_template('contact.html', blogs=blogs.json())


@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    image_url = url_for('static', filename='assets/img/post-bg.jpg')
    blogs = requests.get(ENDPOINT)
    blog = [blog for blog in blogs.json() if blog['id'] == blog_id]
    return render_template('post.html', blog=blog[0], bg_img=image_url)


if __name__ == "__main__":
    app.run(debug=True)
