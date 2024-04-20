import os
import shutil

project = 'my_project'

try:
    for root, dirs, files in os.walk(project):
        print(f'root -> {root}, dirs -> {dirs}, files -> {files}')
        if 'templates' in dirs and root != project:
            for entry in os.listdir(os.path.join(root, 'templates')):
                shutil.copytree(os.path.join(root, 'templates', entry), os.path.join(project, 'templates', entry))
                print(os.path.join(root, 'templates', entry), os.path.join(project, 'templates', entry))
except FileExistsError:
    print('templates exists')
# very confusing
