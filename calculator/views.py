from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):
    context = {}
    return render(request, 'calculator/index.html', context=context)


def user_info(request, name):
    data = DATA
    user_data = data.get(name, {name: "Нет в базе"})
    servings_amount = request.GET.get("servings")
    servings_user_data = dict(user_data)
    if servings_amount is not None:
        servings_user_data.update((x, y * int(servings_amount)) for x, y in servings_user_data.items())
    context = {
        "recipe": servings_user_data,
        "name": name,
        "servings": servings_amount
    }
    return render(request, "calculator/index.html", context)
