# try:
#     file = open("a_file.txt")      # Pode gerar FileNotFoundError
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["y"])       # Pode gerar KeyError
# except FileNotFoundError:
#     file = open("a_file.txt", "w") # Cria o arquivo se ele não existir
#     file.write("Something")
# except KeyError:
#     print("Essa chave não existe.") # Avisa se a chave do dicionário falhar
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
    
    
"""
Raise Exceptions
"""
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight/height**2
print(bmi)