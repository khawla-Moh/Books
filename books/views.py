from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
# Create your views here.



def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if  form.is_valid():
            form.save()
    else:
        form=BookForm()

    return render(request,'books/new.html',{"form":form})



def edit_book(request,pk):
    book=book.objects.get(id=pk)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
        if  form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form=BookForm(instance=book)

    return render(request,'books/edit.html',{'form':form})

def delete_book(request,pk):
    book=bool.objects.get(id=pk)
    book.delete()
    return redirect('/books/')
