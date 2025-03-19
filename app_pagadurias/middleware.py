from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class ResgRestrictAccessMiddleware:
    ALLOWED_PATHS = ["/", "/login/", "/logout/", "/admin/login/", "/__reload__/"]
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("calls")
        path = request.path
        if any(path.startswith(allowed_path) for allowed_path in self.ALLOWED_PATHS):
            return self.get_response(request)
        print("Valida el middleware")
        if request.user.is_superuser or request.user.checkForTI:
            print("Usuario con permisos")
            return self.get_response(request)
        
        return redirect('login')