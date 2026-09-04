from django.http import JsonResponse


def hello(request):
    return JsonResponse({
        "message": "Hello from GitHub Actions!",
        "status": "success"
    })