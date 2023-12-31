from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
# Create your views here.



def book_list(request):
    data=Book.objects.all( )  #from db get all posts
    context={
        'data':data
    }
    return render(request,'books/book.html',context)




def book_details(request,book_id):
    data=Book.objects.get(id=book_id)
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=data
            myform.save()
    else:
        form=BookForm()

    context={
        'post_de':data,
         'form':form
    }
    return render(request,'books/book_detail.html',context)





def create_book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if  form.is_valid():
            form.save()
    else:
        form=BookForm()

    return render(request,'books/new.html',{"form":form})



def edit_book(request,pk):
    book=Book.objects.get(id=pk)
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
