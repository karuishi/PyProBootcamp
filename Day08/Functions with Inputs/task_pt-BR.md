Anteriormente, vimos que as funções nos permitem embalar o código em um bloco nomeado que pode ser usado repetidamente em um momento posterior.

### PAUSA 1 - Revisão
- Crie uma função chamada `greet()`.
- Escreva 3 declarações `print` dentro da função.
- Chame a função `greet()` e execute o seu código.

### Entradas
Ao adicionar um nome de variável entre parênteses ao criar (definir) uma nova função, isso permite que a função aceite entradas quando chamada.

Isso significa que podemos modificar o comportamento da função cada vez que passamos entradas diferentes.

```
# Criando a função
def myFunction(input):
    print(f"Olá! {input}")
```
```
# Usando a função
myFunction("Tommy") 
# Vai exibir "Olá! Tommy"
```

### Entradas são Variáveis
Quando você cria uma função com entradas, está definindo um nome de variável que será dado aos dados que são passados.

O nome da variável de entrada, por exemplo, `name` neste código aqui: `def greet(name):` é chamado de parâmetro.

O valor da variável de entrada, por exemplo, `Angela` quando você chama a função `greet` anterior: `greet("Angela")` é chamado de argumento.