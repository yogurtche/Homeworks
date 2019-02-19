from Modules import modules

st_dict = {
    'name': 'Jorgo Qirjaj',
    'school': 'American University in Bulgaria',
    'grades': [99.92, 92.43, 84.25]
}

print(st_dict)

grade = input('Enter all the grades and separate them by ",": ')

grades = list(map(float, grade.split(",")))

for k in grade:
    modules.add_grade(st_dict, k)

print(st_dict)