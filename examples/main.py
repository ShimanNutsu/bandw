from bandw.run import Run
import numpy as np

if __name__ == '__main__':
    projects = ['project 1', 'proj', 'projector']
    logs = ['loss', 'accuracy', 'reward']
    for proj in projects:
        for i in range(np.random.choice(np.arange(4, 10))):
            run = Run(project=proj, name='run' + str(i))
            for i in range(np.random.choice(np.arange(40, 60))):
                run.log({np.random.choice(logs): np.random.randint(0, 10)})