from django.shortcuts import render

def index_page(request):
    dances = [
        {
            "name": "Бальные танцы",
            "photo": "images/бальные.jpg",
            "levels": ["Средний", "Профессиональный"],
            "info": {
                "Продолжительность": "1.5 часа",
                "Преподаватель": "Анна Петрова",
                "Стоимость": "2000 руб/мес"
            }
        },
        {
            "name": "Хип-хоп",
            "photo": "images/хип-хоп.jpg",
            "levels": ["Начинающий", "Средний"],
            "info": {
                "Продолжительность": "1 час",
                "Преподаватель": "Иван Сидоров",
                "Стоимость": "1500 руб/мес"
            }
        },
        {
            "name": "Сальса",
            "photo": "images/сальса.jpg",
            "levels": ["Начинающий", "Средний"],
            "info": {
                "Продолжительность": "1.5 часа",
                "Преподаватель": "Мария Иванова",
                "Стоимость": "1800 руб/мес"
            }
        }
    ]

    context = {
        "page_name": 'Танцевальная студия',
        "user_name": 'Кира',
        "user_age": 18,
        "dances": dances
    }
    return render(request, "index.html", context)

def about_page(request):
    return render(request, "about.html")

def achivements_page(request):
    return render(request, "achivements.html")
