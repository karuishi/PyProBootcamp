Você vai construir um programa de criptografia e descriptografia usando a [Cifra de César](https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar).

### Demonstração
https://appbrewery.github.io/python-day8-demo/

### TODO-1: 
Crie uma função chamada `encrypt()` que recebe `original_text` e `shift_amount` como 2 entradas.

### TODO-2: 
Dentro da função 'encrypt', desloque cada letra do `original_text` para frente no alfabeto pelo `shift_amount` e imprima o texto criptografado.

Você pode usar a função `index()` embutida do Python para descobrir a posição de um item em uma lista. Por exemplo:
```
frutas = ["Maçã", "Pêra", "Laranja"]
frutas.index("Pêra") #1
```

Por exemplo, se tivermos os seguintes valores:
```
texto_plano = "ola"
shift_amount = 1
```
O resultado criptografado final deve ser:

`Aqui está o resultado codificado: pmb`

Onde cada uma das letras de 'ola' é deslocada para cima em 1.

<div class="hint">
Vamos desmembrar o problema:

  1. Você precisa de um loop for para percorrer cada uma das letras no texto_plano.
  2. Encontre a posição de cada letra na lista de alfabeto.
  3. Adicione o shift_amount desejado pelo usuário à posição para obter a posição da letra codificada.
  4. Encontre a letra correspondente para aquela posição.
  5. Adicione cada letra codificada a uma nova string e imprima-a após o final do loop.
    
</div>


### TODO-3: 
Chame a função `encrypt()` e passe as entradas do usuário. Você deve ser capaz de testar o código e criptografar uma mensagem.


### TODO-4: 
O que acontece se você tentar deslocar a letra 'z' para a frente por 9? Você consegue corrigir o código?

<div class="hint">
  Existem várias abordagens para fazer isso.
1. Você pode adicionar mais de 1 conjunto do alfabeto na Lista de letras do alfabeto.
2. Você pode deslocar o shift_amount para que esteja sempre entre 0 - 25 e se encaixe na Lista.
3. Você pode usar o módulo para obter o resto.
/div>