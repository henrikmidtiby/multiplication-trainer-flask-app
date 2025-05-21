from flask import (
    current_app,
    render_template,
)

#from app import db
# from app.models import 

app = current_app

@app.route("/")
def index():
    return render_template("multiplication_trainer.html")
