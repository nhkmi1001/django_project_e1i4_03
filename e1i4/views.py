from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        return render(request, "e1i4/main.html")

    def post(self, request):
        return render(request, "e1i4/main.html")
