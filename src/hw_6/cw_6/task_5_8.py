"""
Создать список учеников подобной структуры.
Определить средний балл оценок по всем предметам, и
вывести сведения о студентах, средний балл которых больше 4.
"""
pupils = [
  {
        'firstname': 'Masha',
        'group': '22',
        'physics': 7,
        'informatics': 6,
        'history': 8,
  },
{
        'firstname': 'John',
        'group': '19',
        'physics': 3,
        'informatics': 2,
        'history': 4,
  },
{
        'firstname': 'Zoe',
        'group': '17',
        'physics': 5,
        'informatics': 10,
        'history': 6,
  }
]
good_pupils = []

for pupil in pupils:
    average = 0
    for key,value in pupil.items():
        if key in ['physics', 'informatics', 'history']:
            average += value
    if average / 3 > 4:
        good_pupils.append(pupil)

for pupil in good_pupils:
    for key,value in pupil.items():
        print(f'{key}: {value}')
    print('-----------------\n')
