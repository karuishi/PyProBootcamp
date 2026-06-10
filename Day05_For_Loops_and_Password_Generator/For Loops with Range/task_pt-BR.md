A combinação da função `range()` com o Loop For do Python nos permite executar um loop quantas vezes quisermos. Em vez de percorrer cada item em uma lista, podemos percorrer uma faixa de números.

### Função Range

`range(1, 10)`

Esse código não faz nada por si só. Por exemplo, se você tentasse imprimi-lo, ele não forneceria números individuais.

Mas ele pode ser usado em conjunto com Loops For. por exemplo.

```
for numero in range(1, 10):
    print(numero)
```

Isso imprimirá cada um dos números de 1 a 9. Portanto, o intervalo também pode ser expresso assim:

`a <= range(a, b) < b`

Onde a faixa de números é inclusiva do limite inferior, mas não inclusiva do limite superior.

### PAUSA 1 - O desafio de Gauss
Calcule o total dos números entre 1 e 100, inclusive 1 e 100.
