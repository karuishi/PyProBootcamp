# Define a classe QuizBrain, que gerenciará a lógica do jogo.
class QuizBrain:

    # O método construtor recebe uma lista de perguntas (question_list) quando o QuizBrain é iniciado.
    def __init__(self, question_list):
        # Inicializa o número da pergunta atual como 0 (começando da primeira).
        self.question_number = 0
        # Armazena a lista de perguntas fornecida em um atributo para uso posterior.
        self.question_list = question_list
        self.score = 0

    # Define um método para verificar se a resposta está correta
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got ir right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

    # Define um método para verificar se ainda existem perguntas na lista
    def still_has_questions(self):  
        # Checa se o número da questão (neste caso, usado como índice da lista) é menor que o tamanho da lista e retorna true/false
        return self.question_number < len(self.question_list)

    # Define um método para apresentar a próxima pergunta ao usuário.
    def next_question(self):
        # Recupera o objeto de pergunta atual da lista usando o índice 'question_number'.
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Usa a função input() para mostrar a pergunta formatada (ex: "Q.0: Texto da pergunta (True/False): ") e aguardar a resposta do 
        # usuário.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        