from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        # if request.user.username:
        #     return
        # else:
        #     return redirect("/student/login/")
        if request.path  in ["/student/login/"]:
            return
        if not request.user.username:
            return redirect("/student/login/")