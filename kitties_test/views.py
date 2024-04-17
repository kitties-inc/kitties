from django.shortcuts import render, redirect

question = {
    1: "Do you like cats?",
    2: "Do you like playing board games?",
    3: "How energetic are you?",
    4: "Do you like mint?",
    5: "How long is your hair?",
    6: "Do you like ducks?"
}

options = {
    1: [
        "Yes! They are the best creatures on the planet!",
        "Yes, I like them",
        "Neutral",
        "Hate cats"
    ],
    2: [
        "Yes! I love it!",
        "Yep, I don’t mind to play",
        "Don’t like it, boring",
        "I hate board games"
    ],
    3: [
        "Energy bursts out of me!",
        "There's enough energy to live an interesting life",
        "There's only enough energy for necessary life tasks",
        "There's just not enough energy at all",
    ],
    4: [
        "Love it!",
        "I kinda like it",
        "Neutral to mint",
        "Don’t like it"
    ],
    5: [
        "Bald",
        "Short",
        "Medium",
        "Long"
    ],
    6: [
        "Adore them!",
        "I like ducks",
        "Neutral",
        "Don’t like them"
    ]
}

answers = []

any_answer = {1, 2, 3, 4}

results = [
    [{3, 4}, any_answer, any_answer, any_answer, any_answer, any_answer],
    [{1, 2}, {1, 2}, {1, 2}, {3, 4}, {2, 3, 4}, any_answer],
    [{1, 2}, {1, 2}, {3, 4}, {3, 4}, {3, 4}, any_answer],
    [{1, 2}, {3, 4}, any_answer, {3, 4}, {4}, any_answer],
    [{1, 2}, {3, 4}, {1, 2, 3}, {1, 2}, {2, 3, 4}, any_answer],
    [{1, 2}, {3, 4}, {1, 2, 3}, {3, 4}, {2, 3, 4}, {1, 2}],
    [{1, 2}, {3, 4}, {4}, {3, 4}, {2, 3, 4}, any_answer],
    [{1, 2}, {3, 4}, {1, 2, 3}, {3, 4}, {1}, any_answer]
]

virus_result = "You're a virus! Just as harmful and awful. Even the most polite cat wouldn't want to deal with you."

boom_result = "You're an explosive kitty! You're like fire, " \
              "always full of energy and emotions! Your love for board games leads " \
              "to sparkling moments and fun evenings with friends. You know how to " \
              "ignite excitement and maintain a festive atmosphere in any company. Your witty " \
              "tactics and strategy make you an unbeatable opponent at the gaming table. " \
              "In your company, it's always fun and interesting because you're a true master of explosive mood!"

potato_result = "You're a hairy potato cat! You're a true master of relaxation and coziness! " \
                "You value peaceful moments and love spending time cuddled up with your loved ones. " \
                "Your tenderness and care make you a wonderful companion for those seeking comfort and " \
                "understanding. You know how to create an atmosphere of harmony and well-being in your " \
                "surroundings. But at the same time, you don't mind getting excited and playing a board game. " \
                "Your witty tactics and strategy make you an unbeatable opponent at the gaming table. " \
                "Though you don't like to go out much, any cat would envy your mane!"

fluffy_result = "You are a fluffy kitty! Fluffy kitty is a true champion when it comes to volume of " \
                "fur and coziness. If you associate yourself with this character, it means you possess a " \
                "softness of character and hospitality. Fluffy loves long lounges on the windowsill, observing " \
                "the world through the glass, and adores being petted, purring with pleasure. His fur isn't " \
                "just a coat, it's a whole system to ensure comfort and warmth.\n" \
                "Fluffy kitty values the homely atmosphere and prefers to spend time with loved ones, " \
                "where care and attention always surround him. He symbolizes warmth and reliability, " \
                "reminding us of the importance of quiet evenings in a cozy environment. Fluffy is a reminder " \
                "that true happiness lies in simplicity and comfort, which we create around ourselves."

addict_result = "You're a drug addict kitty! A drug addict kitty is a cute but somewhat unpredictable character. " \
                "He's constantly in search of another dose of caffeine or catnip to perk him up. His pupils " \
                "are often dilated with delight, and his fur may be slightly tousled as if he just woke up in " \
                "some mysterious place. The cat loves to aimlessly wander around the house in search of the next " \
                "toy or forgotten cup of tea on the table. He loves playing with tea bags and any items that can " \
                "bounce and rustle. Despite his quirks, this cat has a unique charm and always knows how to make " \
                "you laugh with his antics."

duck_result = "You're a duck-cat! A duck-cat is the embodiment of an amazing combination of seeming opposites. " \
              "If you're this character, it means you know how to combine the impossible: contemplations of the " \
              "sublime with cozy pragmatism. The duck-cat easily adapts to changes and is always ready to go with " \
              "the flow, but at the same time, it doesn't lose its cat-like independence and sharpness. It has " \
              "the unique ability to be the center of attention while remaining mysterious and unattainable. This " \
              "character skillfully balances between the hustle and bustle of social life and the tranquility " \
              "of solitude, finding pleasure in every moment. The cat-duck reminds us that sometimes, to find " \
              "harmony, you need to be both a cat and a duck at the same time."

neutered_result = "You're a neutered kitty! A neutered kitty is an embodiment of calmness and relaxation. If you " \
                  "associate yourself with this character, it means you appreciate comfort and coziness, " \
                  "preferring to observe the world from under warm blankets. This kitty loves long naps and " \
                  "soft pillows. It's one of those who can spend the whole day, blissfully stretching in a " \
                  "sunbeam, without feeling an ounce of guilt. Its mantra is 'just a little more sleep.' The " \
                  "neutered kitty is not in a hurry; it finds happiness in small things and simple enjoyment of " \
                  "the moment. It's a reminder that sometimes it's worth stopping and just resting, as true " \
                  "strength lies in peace."

sphinx_result = "You're a sphinx kitty! A sphinx kitty is a true eccentric in the world of meows. If you feel " \
                "close to this character, it means you're someone who isn't afraid to stand out from the crowd " \
                "and always goes their own way. The sphinx kitty has a unique appearance and an equally unique " \
                "character. It loves warmth and comfort, preferring warm hugs and soft blankets. This kitty " \
                "values attention and adores being in the spotlight, while still maintaining its dignity " \
                "and independence."

silly_result = "You're a playful silly kitty! A playful silly kitty is the embodiment of fun and carefree spirit. " \
               "If you relate to this character, it means you never miss a chance to have fun and enjoy life. " \
               "The playful goofball kitty loves games and mischief; you can often find it chasing its own tail, " \
               "playing with shadows, or trying to catch invisible insects. This kitty lives in the moment and " \
               "savors every minute of its life. It's a reminder that joy can be found in the simplest things, and " \
               "sometimes it's worth forgetting about seriousness to truly laugh from the heart. The playful " \
               "goofball kitty is the heart of the party, always ready to share its good mood and infect others " \
               "with its playfulness."

result_text = [
    virus_result, boom_result, potato_result, fluffy_result, addict_result,
    duck_result, neutered_result, sphinx_result, silly_result
]


# match accumulated answer with one of the results
def match_result() -> int:
    # loop over determined results
    for i, res in enumerate(results):
        # if answer matches ith result, return i
        if all(answers[j] in res[j] for j in range(6)):
            return i
    # return last index corresponding to all the other answers
    return len(results)


def home(request):  # вызывается при заходе на сайт, редиректит пользователя на главную страницу
    answers.clear()
    return render(request, "kitties_test/home.html")


def start_test(request):  # вызывается при нажатии начать тест на начальной странице, редиректит на 1 вопрос
    answers.clear()
    return render(request, "kitties_test/question.html",
                  context={"question": question[1],
                           "options": options[1],
                           "question_id": 1})


def next_question(request, current_question_id: int, current_answer: int):
    # тут бизнес логика, связанная с тем, что происходит, когда пользователь
    # выбрал ответ № current_answer в вопросе № current_question_id
    answers.append(current_answer)

    if current_question_id == len(
            question):  # если текущий вопрос был последним, редиректим на страницу с результатом теста

        # обрабатываем результаты всего теста и выдаем сообщение с результатом
        # а че можно вспомогательные комменты удалить теперь да
        result_id = match_result()  # use the result id to access result text and image
        return render(request, "kitties_test/result.html",
                      context={"info_msg": result_text[result_id],
                               "info_img": f"result_{result_id}.jpg"})

    # тут мы в том случае, если текущий вопрос был не последним
    # редиректнули пользователя на следующий вопрос, передав на фронт текст вопроса и номер вопроса
    return render(request, "kitties_test/question.html",
                  context={"question": question[current_question_id + 1],
                           "options": options[current_question_id + 1],
                           "question_id": current_question_id + 1})
