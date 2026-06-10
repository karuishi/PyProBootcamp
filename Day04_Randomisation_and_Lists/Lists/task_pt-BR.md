Você pode criar uma coleção simples de itens ordenados usando uma lista em Python. Por exemplo:

`fruits = ["Cherry", "Apple", "Pear"]`

ou

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### acessando itens em listas

Você pode fornecer o nome da lista seguido de colchetes e o índice do item que deseja. Por exemplo:

`states_of_america[0]`

retornará "Delaware".

Lembre-se de que, em tudo relacionado a computadores, o primeiro número com o qual contamos é 0 e nunca 1. 0, 1, 2, 3 em vez de 1, 2, 3, 4.

### índices negativos

Você pode acessar itens na lista contando a partir do final da lista usando números inteiros negativos. Por exemplo:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] # isso será "Pear"
```

### modificando itens
Você pode usar a mesma sintaxe para acessar itens em uma lista e modificá-los. Por exemplo:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# a lista fruits agora será ["Orange", "Apple", "Pear"]
```

### adicionando itens
Você pode adicionar itens ao final de uma lista usando a função `append()`. Por exemplo:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# a lista fruits agora será ["Cherry", "Apple", "Pear", "Orange"]
```

### documentação de listas
Você pode encontrar a documentação para Listas em Python e outras funções relacionadas a listas aqui: https://docs.python.org/3/tutorial/datastructures.html