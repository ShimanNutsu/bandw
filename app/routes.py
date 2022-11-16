from flask import Flask, render_template, request
import redis

from utils import get_project_names, get_runs, make_image

app = Flask(__name__)

@app.route('/')
def home():
    names = get_project_names(app.db)
    return render_template('home.html', names=names)

@app.route('/project/<project>', methods=['GET', 'POST'])
def project(project):
    runs = get_runs(app.db, project)
    if request.method == 'GET':
        make_image(app.db, project, runs)
        return render_template('project.html', runs=runs, checked=runs)
    elif request.method == 'POST':
        checked = request.form.getlist('hello')
        make_image(app.db, project, checked)
        return render_template('project.html', runs=runs, checked=checked)

if __name__ == '__main__':
    app.db = redis.StrictRedis(db=0, host='redishost', decode_responses=True)
    app.run(debug=True, host='0.0.0.0', port=8080)