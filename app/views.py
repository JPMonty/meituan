
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
from .request import AddForm

def index(request):
    if request.method == 'POST':
        form = AddForm.AddForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else :
        form = AddForm.AddForm()

    return render(request, 'index.html', {'form' : form })




def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
