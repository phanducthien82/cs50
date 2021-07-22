from django import forms # Thu vien xu ly form
from django.http import HttpResponseRedirect # Thu vien xu ly chuyen trang
from django.shortcuts import render # Thu vien xu ly hien thi
from django.urls import reverse # Thu vien xu ly chuyen chuoi url thanh dia chi trang web

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })

def add(request):
    if request.method == "POST": # Kiem tra neu la nguoi dung gui du lieu
        form = NewTaskForm(request.POST) # Khoi tao form moi tu du lieu cua nguoi dung
        if form.is_valid(): # Kiem tra tinh chinh xac cua du lieu tu phia server
            task = form.cleaned_data["task"]  # Lay truong du lieu tuong ung
            #tasks.append(task) # Them du lieu vao danh sach (CSDL)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:  # Neu du lieu khong chinh xac thi tra lai giao dien la form va nhung du lieu nguoi dung da nhap
            return render(request, "tasks/add.html", {
                "form" : form
            })
    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    }) # Tra lai giao dien form voi du lieu trong