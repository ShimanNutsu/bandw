import matplotlib.pyplot as plt
import numpy as np

def get_project_names(db):
    keys = db.keys()
    if keys == []:
        return []
    projects, _, _ = _split_names(keys)
    return projects

def get_runs(db, project):
    keys = db.keys(_make_name(project))
    if keys == []:
        return []
    _, runs, _ = _split_names(keys)
    return runs

def make_image(db, project, runs):
    if runs == []:
        plt.clf()
        plt.savefig('static/images/plots.png')
        return

    logs = []
    for run in runs:
        keys = db.keys(_make_name(project, run))
        _, _, a = _split_names(keys)
        logs += a
    logs = list(set(logs))
    nrows = (len(logs) + 1) // 2
    
    plt.clf()
    cmap = plt.get_cmap('plasma')
    cmap_arr = cmap(np.linspace(0, 1, len(runs)))
    plt.figure(figsize=(15, 5 * nrows))
    for i, log in enumerate(logs):
        plt.subplot(nrows, 2, i + 1)
        plt.tight_layout()
        for j, run in enumerate(runs):
            values = list(map(int, db.lrange(_make_name(project, run, log), 0, -1)))
            if values != []:
                plt.plot(values, label=run, c=cmap_arr[j])
        plt.title(log)
        plt.legend()
    plt.savefig('static/images/plots.png')
    pass

def _make_name(project, run = None, log = None):
    if run is None:
        return project + ':*'
    if log is None:
        return project + ':' + run + ':*'
    return project + ':' + run + ':' + log

def _split_names(names):
    values = map(list, zip(*[name.split(':') for name in names]))
    return map(lambda x: list(set(x)), values)