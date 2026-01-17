Uma função, na sua forma mais simples, é apenas um nome que serve como um wrapper para um bloco de código. Você dá um nome a ela e, ao chamar a função por esse nome, todo o código dentro do bloco da função será executado. Isto pode nos ajudar a economizar tempo e reduzir o código repetitivo.

### Definindo uma nova função
```
def <nome_da_função>():
    print("Hello")
    # Faça algo mais
    # Faça algo mais ...
```

### Chamando uma função
Chamar uma função significa simplesmente acioná-la. Podemos chamar uma função em qualquer ponto do nosso código em Python.

```
<nome_da_função>()
```

Colocando tudo junto, por exemplo:
```
# Criando a função
def get_user_name():
    name = input("Qual é o seu nome? ")
    print("Olá, " + name)
    # Dentro da função

# Fora da função
print("Olá")
get_user_name() # Chamando a função
```

Este código resultará na seguinte sequência de saída:
```
Olá
Qual é o seu nome? # Eu digito Angela
Olá
Angela