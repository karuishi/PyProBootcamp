### FAZER-1: 
Importe e imprima o logo de art.py quando o programa iniciar.

### FAZER-2: 
O que acontece se o usuário entrar com um número/símbolo/espaço que não está na Lista `alphabet`?

Você consegue consertar o código para manter o número/símbolo/espaço quando o texto é codificado/decodificado?

por exemplo 
```
original_text = "nos encontramos às 3!"
cipher_text = "XXXX XX XXXXXXXXX XX 3!"
```

<div class="hint">
  Se não for uma letra na Lista alphabet, talvez você possa apenas adicioná-la ao final de cipher_text como o caractere não modificado?
</div>


### FAZER-3: 

Você consegue descobrir uma maneira de reiniciar o programa de cifra?

por exemplo 

`Digite 'sim' se você quiser tentar novamente. Caso contrário, digite 'não'.`

Se digitarem 'sim', então peça novamente pela direção/texto/deslocamento e chame a função `caesar()` novamente.

<div class="hint">
  Tente criar um loop while que continue a executar o programa se o usuário digitar 'sim'.
</div>