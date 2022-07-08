class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Pink\n\n',
    'What color are bananas?\n(a) Yellow/Green\n(b) Orange\n(c) Red\n\n',
    'What color are strawberries\n(a) Pink\n (b) Yellow\n(c) Orange\n\n'
]

question_answers = [
    Question(questions[0],'a'),
    Question(questions[1],'a'),
    Question(questions[2],'a'),
]


def run_test(prompts):
    score = 0
    for question in questions:
        user_answer = input(Question.prompt)
        if user_answer == Question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)))

run_test