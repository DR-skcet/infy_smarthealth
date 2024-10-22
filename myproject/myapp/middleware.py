# middleware.py
from django.utils.deprecation import MiddlewareMixin

class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Adjust the CSP as needed
        csp_policy = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://apis.google.com; connect-src 'self' https://apis.google.com; img-src 'self' data: https://*.googleusercontent.com;"
        response['Content-Security-Policy'] = csp_policy
        return response
