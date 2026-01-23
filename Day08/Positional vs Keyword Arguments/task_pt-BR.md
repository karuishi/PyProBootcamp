### Múltiplas Entradas
Você pode ter múltiplas entradas em funções. Tudo que você precisa fazer é separá-las com uma vírgula `,`.

### PAUSA 1 
Crie uma função com múltiplas entradas

<div class="hint">
  <code>
def cumprimentar(nome, saudação):

    ____print(f"{saudação} {nome}")
    
cumprimentar("Angela", "Oi!")
</code>
</div>

### PAUSA 2
Modifique a função para que ela imprima os valores esperados.
```
def cumprimentar_com(nome, local)
    Olá nome
    Como é em local
```

### Argumentos Posicionais
Por padrão, quando você cria uma função em Python, ela manterá a ordem dos argumentos na definição da função.

p.ex. Na função abaixo, o primeiro argumento que entra sempre será impresso antes do segundo. `a = 2, b = 1`

```
def minha_função(a, b)
  print(a)
  print(b)
  
 minha_função(2, 1)
 #Ela vai imprimir:
 # 2
 # 1
```

### Argumentos de Palavras-chave
Você pode usar palavras-chave ao fornecer os argumentos quando você chama uma função para que haja menos confusão sobre qual valor é atribuído a qual parâmetro de entrada.

### PAUSA 3 
Chame a função `cumprimentar_com()` usando argumentos de palavras-chave.

<div class="hint">
  <code>
cumprimentar_com(local="Londres", nome="Angela")
</code>
</div>