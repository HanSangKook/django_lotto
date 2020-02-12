from django.shortcuts import render
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.form import PostForm

def index(request):
    #return HttpResponse('<h1>Hello, world!</h1>')
    #site_1\lotto\template\lotto\default.html ->이렇게 만들어야함

    #site_1\member\templates\index.html (127.0.0.1:8000/member/)
    lottos = GuessNumbers.object.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style ='color:red;'>Hello, world!</h1>")

# def index(request):
#     #브라우저로부터 넘어온 request를 그대로 template(default.html)에게 전달
#     #{}에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음.
#     return render(request, 'lotto/default.html',{})
# # Create your views here.

from .forms import PostForm
    print("******")
    print(request.method)
    print("******")
    print(request.POST)
    print("******")

    if request.method =="post":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            


def post(request):
    form = PostForm
    return render(request, 'lotto/form.html', {'form':form})
