from django.http import JsonResponse
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['POST'])
def signup(request):
    data = request.data
    message = 'success'

    return JsonResponse({'status': message})
