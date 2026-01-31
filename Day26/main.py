import random, pandas

"""List Comprehension"""

# Cria uma nova lista baseada em outra com valores + 1
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

# Cria uma lista baseada no range valores dobrados
range_list = [n * 2 for n in range(1, 5)]

# Cria uma nova lista baseada em outra com nomes longos em CAPS
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]

# Cria um novo dicionário baseado em outro com os estudantes que passaram no teste
students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

# print(new_numbers)
# print(range_list)
# print(long_names)
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_df = pandas.DataFrame(student_dict)

# Loop através das linhas do data frame
for (index, row) in student_df.iterrows():
    print(row) # row é um objeto da classe pandas, logo:
    """
    print(row.students) # Para printar os estudantes do data frame
    print(row.score) # Para printar as pontuações do data frame
    if row.students == "Angela": # Trabalhar com condicionais para exibir um resultado
        print(row.score)
    """