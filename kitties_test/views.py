from django.shortcuts import render

from kitties_test.consts import results, answers, question, result_text, options


def match_result() -> int:
    for i, res in enumerate(results):
        if all(answers[j] in res[j] for j in range(6)):
            return i
    return len(results)


def home(request):
    answers.clear()
    return render(request, "kitties_test/home.html")


def start_test(request):
    answers.clear()
    return render(request, "kitties_test/question.html",
                  context={"question": question[1],
                           "options": options[1],
                           "question_id": 1})


def next_question(request, current_question_id: int, current_answer: int):
    answers.append(current_answer)

    if current_question_id == len(question):
        result_id = match_result()
        return render(request, "kitties_test/result.html",
                      context={"info_msg": result_text[result_id],
                               "info_img": f"result_{result_id}.jpg"})

    return render(request, "kitties_test/question.html",
                  context={"question": question[current_question_id + 1],
                           "options": options[current_question_id + 1],
                           "question_id": current_question_id + 1})
