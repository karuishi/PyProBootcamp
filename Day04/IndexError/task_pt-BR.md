### Comprimento de uma lista
Você pode obter o comprimento de uma lista (número de itens na lista) ou o comprimento de uma string (número de caracteres na string) usando a função `len()`. https://docs.python.org/3/library/functions.html#len

### IndexError
Quando você tenta acessar um item que não está dentro do intervalo de uma lista, ocorrerá um IndexError. Exemplo:

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) # Isso resultará em um IndexError
```

### Listas aninhadas
Você pode colocar listas dentro de outras listas, o que se torna algo chamado de "Lista Aninhada" ou "Lista 2D". Exemplo:

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
# A lista ficaria assim: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```
Você também pode representar a lista no formato 2D assim:
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]