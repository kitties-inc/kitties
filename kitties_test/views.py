from django.shortcuts import render

map_ = {
    1: "первый вопрос",
    2: "второй вопрос"
}


def home(request):  # вызывается при заходе на сайт, редиректит пользователя на главную страницу
    return render(request, "kitties_test/home.html")


def start_test(request):  # вызывается при нажатии начать тест на начальной странице, редиректит на 1 вопрос
    return render(request, "kitties_test/question.html",
                  context={"question": map_[1],
                           "question_id": 1})


def next_question(request, current_question_id: int, current_answer: int):
    # тут бизнес логика, связанная с тем, что происходит, когда пользователь
    # выбрал ответ № current_answer в вопросе № current_question_id

    if current_question_id == len(map_):  # если текущий вопрос был последним, редиректим на страницу с результатом теста

        # обрабатываем результаты всего теста и выдаем сообщение с результатом
        test_result_text = ''
        return render(request, "kitties_test/result.html",
                      context={"info_msg": test_result_text})

    # тут мы в том случае, если текущий вопрос был не последним
    # редиректнули пользователя на следующий вопрос, передав на фронт текст вопроса и номер вопроса
    return render(request, "kitties_test/question.html",
                  context={"question": map_[current_question_id + 1],
                           "question_id": current_question_id + 1})

