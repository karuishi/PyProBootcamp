student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# Como 'row' representa uma linha na tabela e a tabela tem colunas chamadas 'letter' e 'code',
#  o Pandas permite acessar os valores diretamnte usando o ponto (.).  
# IMPORTANTE: o 'row' é um objeto da classe Pandas, por isso para acessar o seu valor utiliza-se o (.)
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
