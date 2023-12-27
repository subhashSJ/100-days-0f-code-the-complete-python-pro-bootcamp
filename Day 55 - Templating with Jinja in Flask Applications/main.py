from flask import Flask, render_template
import requests

app = Flask(__name__)

ENDPOINT = 'https://api.npoint.io/c790b4d5cab58020d391'

@app.route('/')
def home():
    blogs = requests.get(ENDPOINT)
    return render_template('index.html', blogs=blogs.json())

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    blogs = requests.get(ENDPOINT)
    blog = [blog for blog in blogs.json() if blog['id'] == blog_id]
    return render_template('post.html', blog=blog[0])


if __name__ == "__main__":
    app.run(debug=True)
