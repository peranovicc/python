students = ['Marko','Petar','Pavle']
marks = []

for student in students:
    marks.append(int(input('Unesi ocenu za studenta "{}": '.format(student))))


# map returns map object in python3, so we must convert it to list
print(list(map(lambda student,mark: (student,mark),students,marks))) 

# Коришћена функција zip - ствара tuple на основу више листи (спаја редом елементе листи)



