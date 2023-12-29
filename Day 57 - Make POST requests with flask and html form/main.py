from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def authenticate():
    error = None
    if request.method == 'POST':
        #perform authentication
        pass    
    
    return f"Name: {request.form['name']} Password: {request.form['password']}"

if __name__ == '__main__':
    app.run(debug=True)