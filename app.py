from flask import Flask, render_template
from controllers.videos_controller import videos_blueprint
from controllers.directors_controller import directors_blueprint


app = Flask(__name__)
app.register_blueprint(videos_blueprint)
app.register_blueprint(directors_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)