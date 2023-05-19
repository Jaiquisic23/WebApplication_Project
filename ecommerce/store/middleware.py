from django.shortcuts import redirect
from .models import Customer

class CustomerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                # Si el usuario está autenticado, intenta obtener su objeto Customer
                customer = request.user.customer
            except Customer.DoesNotExist:
                # Si el objeto Customer no existe, crea uno nuevo para el usuario
                customer = Customer.objects.create(user=request.user)

        response = self.get_response(request)

        return response
