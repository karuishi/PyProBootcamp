O programa irá perguntar:
```
Quantas letras você gostaria em sua senha?
Quantos símbolos você gostaria?
Quantos números você gostaria?
```
O objetivo é obter as respostas do usuário para essas perguntas e então gerar uma senha aleatória. Use seus conhecimentos sobre listas e loops em Python para concluir o desafio.

### Demonstração
https://appbrewery.github.io/python-day5-demo/

### Versão Fácil
Gere a senha em sequência. Letras, depois símbolos, depois números. Se o usuário quiser

4 letras
2 símbolos e
3 números
então a senha pode ser assim:

`fgdx$*924`

Você pode ver que todas as letras estão juntas. Todos os símbolos estão juntos e todos os números se seguem também. Tente resolver este problema primeiro.

<div class="hint">
  Lembre-se que você pode usar a função random.choice() para obter um item aleatório de uma lista! Mas você precisa importar o módulo random primeiro.
</div>


### Versão Difícil
Quando você tiver concluído a versão fácil, estará pronto para enfrentar a versão difícil. Na versão avançada deste projeto a senha final não segue um padrão. Então o exemplo acima pode ficar assim:

`x$d24g*f9`

E toda vez que você gerar uma senha, as posições dos símbolos, números e letras serão diferentes. Isso deixará a senha mais difícil para os hackers decifrarem.

A habilidade essencial de um bom programador é usar o Google para encontrar o que precisa. Seu cérebro é para pensar, não para memorizar funções! Você precisará do Google para resolver este projeto no nível difícil. Se você ficar preso, verifique a dica abaixo sobre o que pesquisar no Google.

<div class="hint">
  Tente pesquisar no Google: "Como embaralhar itens em uma lista em Python"
</div>