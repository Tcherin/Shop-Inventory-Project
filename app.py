from flask import Flask, render_template
from controllers.videos_controller import videos_blueprint
from controllers.suppliers_controller import suppliers_blueprint


app = Flask(__name__)
app.register_blueprint(videos_blueprint)
app.register_blueprint(suppliers_blueprint)

@app.route('/')
def home():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)