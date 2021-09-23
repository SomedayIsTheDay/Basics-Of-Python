import os
dir_dict = {'my_project_1': [{'settings': []}, {'main_app': []}, {'admin_app': []}, {'auth_app': []}]}
for k, v in dir_dict.items():
    if not os.path.exists(k):
        for item in v:
            for v_keys in item.keys():
                os.makedirs(os.path.join(k, v_keys))
    else:
        print('Уже существует')
