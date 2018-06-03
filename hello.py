from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_word():
    return 'Hello World'

@app.route('/user/<username>')
def show_username(username):
    #show username
    return 'Hello ' + str(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show post ID
    return 'Post  ID {} '.format(post_id)

if __name__ == ('__main__'):
    app.debug = True
    app.run()
