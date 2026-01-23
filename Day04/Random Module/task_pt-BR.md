### Geradores de Números Pseudorrandômicos
Os computadores não são aleatórios, pois são construídos com circuitos e interruptores. Mas a aleatoriedade é muito importante ao desenvolver software, especialmente jogos. Seria muito entediante se cada movimento em um videogame fosse pré-determinado.

Portanto, alguns cientistas da computação inventaram os geradores de números pseudorrandômicos, por exemplo, https://en.wikipedia.org/wiki/Mersenne_Twister

Se você quiser aprender mais sobre geradores de números pseudorrandômicos, recomendo assistir a este vídeo da Khan Academy: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

### O módulo Random em Python
Leia a documentação aqui:  
https://docs.python.org/3/library/random.html

Para usá-lo, primeiro é necessário importá-lo:

`import random`

### Números inteiros aleatórios dentro de um intervalo

```
import random
rand_num = random.randint(1, 10)

# Isso gerará um número inteiro aleatório entre 1 e 10 (inclusive).
```
### Módulos em Python
O Python nos permite colocar o código em arquivos diferentes e importar esse código quando necessário. Isso significa que podemos organizar e modularizar melhor nosso código.

Você pode criar um novo módulo simplesmente criando um novo arquivo `.py` e, em seguida, pode importar variáveis ou funções desse arquivo apenas usando a palavra-chave `import`.

### Números flutuantes aleatórios
Você pode gerar um número aleatório entre 0.0 (inclusivo) e 1.0 (não inclusivo) usando o seguinte código do módulo random:

```
import random
rand_num_0_to_1 = random.random()
```
Isso também pode ser representado assim:

`0.0 <= random.random() < 1.0`

Você pode expandir o intervalo de números aleatórios gerados por esse método usando multiplicação.

Por exemplo: `random.random() * 5`

Isso gerará um número aleatório entre 0 e 5.

Outra maneira de gerar números flutuantes aleatórios é usar a função `uniform()`.

```
import random
random_float = random.uniform(1, 10)
# Isso gerará um número flutuante aleatório entre 1 e 10.
```
Esse método pode ou não incluir o limite superior, dependendo do arredondamento do número flutuante.  
Portanto, é melhor representado assim:

`a <= random.uniform(a,b) <= b`

Então, dependendo de querer incluir ou não o limite superior, você escolherá se deseja usar `random.random()` ou `random.uniform()`.

### PAUSA 1 - Cara ou Coroa
Crie um programa que simule o lançamento de uma moeda usando o que você aprendeu sobre randomização em Python. Ele deve imprimir aleatoriamente "Cara" ou "Coroa" toda vez que for executado.

<div class="hint">
  Você precisará pensar sobre o que aprendeu sobre instruções condicionais em Python.
</div>