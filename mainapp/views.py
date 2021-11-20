from django.shortcuts import render
import json

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):

    json_data = open('mainapp/fixtures/products.json', encoding = 'utf-8')
    context = {
        'title': 'GeekShop - Каталог',
        'products': json.load(json_data)
        # 'products': [
        #     {
        #         "name": "Худи черного цвета с монограммами adidas Originals",
        #         "description":"Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
        #         "img":"/static/vendor/img/products/Adidas-hoodie.png",
        #         "prise": 6090.00
        #     },
        #     {
        #         "name": "Синяя куртка The North Face",
        #         "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
        #         "img": "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
        #         "prise": 23725.00
        #     },
        #     {
        #         "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
        #         "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
        #         "img": "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
        #         "prise": 3390.00
        #     },
        #     {
        #         "name": "Черный рюкзак Nike Heritage",
        #         "description": "Плотная ткань. Легкий материал.",
        #         "img": "/static/vendor/img/products/Black-Nike-Heritage-backpack.png",
        #         "prise": 2340.00
        #     },
        #     {
        #         "name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
        #         "description": "Гладкий кожаный верх. Натуральный материал.",
        #         "img": "/static/vendor/img/products/Black-Dr-Martens-shoes.png",
        #         "prise": 13590.00
        #     },
        #     {
        #         "name": "Темно-синие широкие строгие брюки ASOS DESIGN",
        #         "description": "Легкая эластичная ткань сирсакер Фактурная ткань.",
        #         "img": "/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
        #         "prise": 2890.00
        #     }
        # ]
    }
    return render(request, 'mainapp/products.html', context)
