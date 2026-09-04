from django.http import JsonResponse
from .models import Product


def hello(request):
    return JsonResponse({
        "message": "Hello from GitHub Actions!",
        "status": "success"
    })


def products(request):
    data = list(
        Product.objects.values(
            "id",
            "name",
            "price",
            "created_at"
        )
    )

    return JsonResponse({
        "products": data
    })