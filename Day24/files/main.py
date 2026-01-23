"""
Abre um arquivo para leitura
"""
# file = open("my_file.txt") # O Padrão é leitura
# contents = file.read()
# print(contents)
# file.close() # Precisa fechar o arquivo, após uso, manualmente para não ocupar espaço na memória

# Ou

with open("../../../PyProBootcamp/my_file.txt") as file: #Fecha o arquivo automaticamente após o uso
    contents = file.read()
    print(contents)

"""
Abre um arquivo para escrita
""" 
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.") # Substitui todo o conteúdo do arquivo pelo argumento inserido
    
# Caso não queira, substituir o conteúdo e apenas adicionar

# with open("my_file.txt", mode="a") as file: # append
#     file.write("\nNew text.")
    
"""
Cria um novo arquivo
"""
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")