Laços (loops) nos permitem instruir o computador a repetir ações sem que precisemos escrever código repetidamente. Se quiséssemos que o computador imprimisse os números de 1 a 100, seria muito cansativo digitar uma instrução de impressão para cada número, ou até mesmo digitar todos os números de 1 a 100. Os laços nos permitem criar uma regra, e o computador pode segui-la para realizar uma ação repetida.

### Sintaxe

```
for <nome da variável de cada item> in <uma lista>:
    <faça algo>
    <faça outra coisa>
```

### PAUSA 1 - Seja um Computador
Preveja o que será impresso pelo código abaixo:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

### Identação
A identação é muito importante na programação em Python. Toda vez que você vir o símbolo `:`, deve prestar atenção à identação que vem a seguir.

Por exemplo: Este código se comportará de forma muito diferente

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

desse outro código:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")