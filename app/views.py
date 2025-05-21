from icecream import ic
from flask import (
    current_app,
    render_template,
)

from app import db
from app.models import TimingResult

app = current_app

@app.route("/")
def index():
    return render_template("multiplication_trainer.html")

@app.route("/logger/v1/<int:n_exercises>/<float:used_time>/<string:group>")
def log_used_time(n_exercises, used_time, group):
    ic(n_exercises)
    ic(used_time)
    ic(group)

    tr = TimingResult()
    tr.number_of_exercises = n_exercises
    tr.used_time = used_time
    tr.group = group
    db.session.add(tr)
    db.session.commit()
    ic(tr)

    return "ok"