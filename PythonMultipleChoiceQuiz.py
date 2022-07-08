class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompts = [
    'What color are apples?\n(A) Red/Green\n(B) Purple\n(C) Magenta\n\n',
    'What color are bananas?\n(A) Blue\n(B) Cyan\n(C) Yellow\n\n',
    'What color are strawberries\n(A) Brown\n(B) Pink\n(C) Green\n\n'
]

questions = [
    Question(questions_prompts[0],'A'),
    Question(questions_prompts[1],'C'),
    Question(questions_prompts[2],'B'),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    return 'You got ' + str(score) + '/' + str(len(questions))

print(run_test(questions))