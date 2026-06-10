from django.http import JsonResponse

def health_check(request):
    return JsonResponse({
        "status": "online",
        "message": "API is running"
    })