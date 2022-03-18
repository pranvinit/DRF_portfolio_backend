from django.http import JsonResponse

def index(request):
    return JsonResponse({'msg': 'hey this is the homepage of my api'})

