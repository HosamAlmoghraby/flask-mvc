from flask import Flask, render_template, request
import model

app = Flask(__name__)


@app.route('/users/<int:id>', methods=['GET', 'POST'])
def users(id):
    if request.method == 'POST':
        model.User.name = request.form['name']
        model.User.email = request.form['email']
        return 'Post request has been received successfully'

    profile = model.User.getProfile(id=id)
    print(profile)

    return render_template('user.html', profile=profile)


if __name__ == '__main__':
    app.run(debug=True)
