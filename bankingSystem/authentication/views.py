from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

import json
from django.views.generic import View

class PersonalFullnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        fullname = data['fname']

        if not str(fullname).isalpha():
            return JsonResponse({'fullname_error': 'Full names should only contain alphabets'}, status=400)
        return JsonResponse({'fullname_valid': True})

        if User.object.filter(fullname=fullname).exists():
            return JsonResponse({'fullname_error': 'Sorry, Full Name already exists, you can try to login'}, status=409)
        return JsonResponse({'fullname_valid': True})








        # Continue with further processing or return a response


        

    
# class businessRegView(view):
#     def get(self, request):
#         return render(request, 'authentication/customers-reg/business-reg.html')
    
# class investorRegView(view):
#     def get(self, request):
#         return render(request, 'authentication/customers-reg/invest-reg.html')
