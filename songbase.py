from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = '18902193'

@app.route('/')
def index():
    #return '<h1>hello world!</h1>'
    return render_template('index.html')


@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    # how to get form data is different for GET vs. POST
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            return render_template('form-demo.html', first_name=session.get('first_name'))
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        # return render_template('form-demo.html', first_name=first_name)
        return redirect(url_for('form_demo'))


@app.route('/user/<string:name>/')
def get_user(name):
    #return 'hello %s your age is %d' % (name, 21)
    return render_template('user.html', user_name=name)


@app.route('/my-song')
def get_all_songs():
    songs = [
            'Song1',
            'Song2',
            'Song3'
            ]
    return render_template('my-song.html', songs=songs)


@app.route('/users')
def show_all_users():
    return '<h2>this is the page for all users</h2>'


if __name__ == '__main__':
    app.run(debug=True)
