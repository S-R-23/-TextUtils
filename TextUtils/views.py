from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def analyze(request):
    type_text = request.GET.get("text","default")
    rem_punc =request.GET.get("rempunc","off")
    number=request.GET.get("number","off")

    if rem_punc == "on":
        punctuation=''''!@#$%^&*()_'"{}[]:\;<>,.?/-|'''
        space = ""

        for i in type_text:
            if i not in punctuation:
                space= space+i
        params={"purpose":"remove punctuation","analyzed_text":space}

    if number=="on":
        integer="1234567890"
        space=""
        for i in type_text:
            if i not in integer:
                space=space+i
        params={"purpose":"remove integers","analyzed_text":space}

    return render(request,"analyzing.html",params)

