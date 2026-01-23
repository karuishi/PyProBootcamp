### Soma
O Python possui muitas funções integradas para nos ajudar a trabalhar com números. Uma delas nos ajuda a calcular a soma (o total).
por exemplo
```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
```
Mas como a `sum()` funciona nos bastidores? O código é escrito pelas pessoas que desenvolveram o Python e pode parecer algo assim:

```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
print(sum)
```



### PAUSA 1 - Max
Há também métodos embutidos do Python chamados `max()` e `min()`, que permitem passar uma lista de números, e eles fornecerão o número mais alto ou mais baixo.

Seu trabalho é descobrir como os programadores de Python poderiam ter construído essa funcionalidade usando loops e condicionais.

## COMPLETE ESTE DESAFIO SEM USAR max()

A você é dada uma lista de notas de exames, e você deve imprimir a maior nota da lista. 
Você precisará usar o que aprendeu sobre Listas, Loops For e Condicionais para imprimir a maior nota na lista de student_scores.
Por exemplo, se as notas fossem:
```
8 65 89 86 55 91 64 89
```
Seu código deve imprimir
```
91
```