# Define uma nova classe chamada Question (Pergunta).
class Question:
    # O método __init__ é o construtor. Ele é chamado automaticamente sempre que criamos um novo objeto desta classe.
    # Ele recebe 'text' (texto da pergunta) e 'answer' (resposta da pergunta) como parâmetros.
    def __init__(self, text, answer):
        # Atribui o valor do parâmetro 'text' ao atributo 'text' do objeto que está sendo criado.
        self.text = text
        # Atribui o valor do parâmetro 'answer' ao atributo 'answer' do objeto.
        self.answer = answer