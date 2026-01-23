### TODO-1
- Crie uma String vazia chamada `placeholder`.
- Para cada letra na `chosen_word`, adicione um `_` ao `placeholder`.
- Então, se a `chosen_word` fosse "maçã", o `placeholder` deveria ser `_ _ _ _` com 4 `"_"` representando cada letra para adivinhar.
- Imprima `hint`.

<div class="hint">
  Lembre-se de que você pode usar a função range() dentro de um loop para realizar uma ação por um determinado número de vezes. 
</div>


### TODO-2
- Crie uma string vazia chamada "exibir".
- Percorra cada letra na `chosen_word`
- Se a letra naquela posição corresponder a `guess`, então revele aquela letra em `exibir` naquela posição.
- Por exemplo, se o usuário adivinhou "p" e a palavra escolhida foi "maçã", então `exibir` deveria ser `_ _ _ _ _`.
- Imprima `exibir` e você deve ver a letra adivinhada na posição correta.
- Mas toda letra que não corresponder é representada com um "_".

<div class="hint">
  Lembre-se de que o loop for percorrerá cada letra na chosen_word em ordem. Você pode usar esse fato para criar uma nova string, acrescentando a letra ou um "_".
</div>