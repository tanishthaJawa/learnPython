from Question import Question

prompts = [
    "What color are the apples? \n (A)Red\n B)Green\n",
    "What color are the bananas? \n (A)teal\n B)red\n C)yellow",
    "What color are the peas? \n (A)teal\n B)Green\n C)yellow"
]

questions = [
    Question(prompts[0], "A"),
    Question(prompts[1], "C"),
    Question(prompts[2], "B")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "right")


run_test(questions)
