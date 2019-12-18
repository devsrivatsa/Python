from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'srivatsa',
        'title':'Osho',
        'content':'first post content',
        'date_posted':'12th Dec 2019'
    },
    {
        'author': 'Anu',
        'title': 'Sadhguru',
        'content': '2nd post content2',
        'date_posted': '12th Nov 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About...")

if __name__ == '__main__':
    app.run(debug=True)