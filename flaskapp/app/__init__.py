from flask import Flask,render_template,redirect
# from flask_login import LoginManager,login_required
# from .forms import SimpleForm
from .models import db
from flask_migrate import Migrate
from .routes import project
from .config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(project.bp)


@app.route('/')
def index():
    return {"hello":"welcome testers"}
