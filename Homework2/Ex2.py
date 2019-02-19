from statistics import mean
st_dict = {
    'dict_one': {
        'name': 'Jorgo Qirjaj',
        'grades': [93.54, 34.65, 77.53, 13.76, 98.04] 
        },
    'dict_two': {
        'name': 'Anxhela Beluli',
        'grades': [93.34, 34.22, 68.67, 54.33, 98.54]
    },
    'dict_three': {
        'name':'Flavia Hajna',
        'grades': [43.54, 54.23, 76.67, 87.67, 85.45]
    }
}

for st in st_dict:
    print(st_dict[st]['name'],' has an average grade of {}'.format(mean(st_dict[st]['grades'])))