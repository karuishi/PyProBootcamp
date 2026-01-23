### TODO-1: 
Crie uma função chamada `decrypt()` que recebe `original_text` e `shift_amount` como 2 entradas.

### TODO-2: 
Dentro da função `decrypt()`, desloque cada letra do `original_text` para frente no alfabeto *para trás* pelo `shift_amount` e imprima o texto descriptografado.

<div class="hint">
  Você pode multiplicar qualquer número por -1 para transformá-lo em um número negativo.
</div>


### TODO-3: 
- Combine as funções `encrypt()` e `decrypt()` em uma única função chamada `caesar()`. 
- Use o valor da variável `direction` escolhida pelo usuário para determinar qual funcionalidade usar. 
- chame a função caesar em vez de criptografar/descriptografar e passe todas as três variáveis `direction`/`text`/`shift`.

<div class="hint">
  Lembre-se de que, quando você multiplica um número por -1, ele inverte seu sinal.
por exemplo, <code>3 + ( 5 * -1) </code> é o mesmo que <code>3 - 5</code>.
</div>


<div class="hint">
Deveria dizer:  

<code>Aqui está o resultado codificado: XXX</code>

ou

<code>Aqui está o resultado decodificado: XXX</code> 

</div>