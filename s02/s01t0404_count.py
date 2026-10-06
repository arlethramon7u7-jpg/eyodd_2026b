# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(n)

def random_function(students): # O(1)
    first = students[0] # O(n)
    total = 0 # O(1)
    new_list = [] # O(1)

    for student in students:
        total += 1 # O(1)
        new_list.append(student) # O(n)

    print(new_list) # O(n)
    return total # O(1)

print(random_function(student_list_01))

# Calcular O(n)