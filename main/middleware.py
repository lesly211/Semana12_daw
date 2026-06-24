class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"[LOG MIDDLEWARE] {request.method} - {request.path}")
        response = self.get_response(request)
        response['X-Custom-Header'] = 'Semana12-DAW'
        response['Content-Security-Policy'] = "default-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com;"
        return response
