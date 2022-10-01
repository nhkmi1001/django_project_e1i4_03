from django.shortcuts import render

# Create your views here.

# 오형석
def index(request):
    return render(request, 'index.html')



def main(request):
    return render(request, 'woong_index.html')