from django.shortcuts import render

from kitties_test.consts import answers, results, question, result_text, options

from random import randint


def match_result(session_id: int) -> int:
    for i, res in enumerate(results):
        if all(answers[session_id][j] in res[j] for j in range(6)):
            return i
    return len(results)


def home(request):
    return render(request, "kitties_test/home.html")


def start_test(request):
    while (session_id := randint(1, 1_000_000)) in answers:
        pass
    answers[session_id] = []
    return render(request, "kitties_test/question.html",
                  context={"question": question[1],
                           "options": options[1],
                           "question_id": 1,
                           "session_id": session_id})


def next_question(request, current_question_id: int, current_answer: int, session_id: int):
    answers[session_id].append(current_answer)

    if current_question_id == len(question):
        result_id = match_result(session_id)
        answers.pop(session_id)
        return render(request, "kitties_test/result.html",
                      context={"info_msg": result_text[result_id],
                               "info_img": f"result_{result_id}.jpg"})

    return render(request, "kitties_test/question.html",
                  context={"question": question[current_question_id + 1],
                           "options": options[current_question_id + 1],
                           "question_id": current_question_id + 1,
                           "session_id": session_id})
