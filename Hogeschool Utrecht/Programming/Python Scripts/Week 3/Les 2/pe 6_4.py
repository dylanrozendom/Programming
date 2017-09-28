studentencijfers = [ [95, 92, 86 ], [66, 75, 54], [89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    for student in studentencijfers:
        antw = (sum(int(i) for i in student) / 3)
        print(antw)

def gemiddelde_van_alle_studenten(studentencijfers):
    for student in studentencijfers:
        antw = (sum(student)) / 4
        return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))