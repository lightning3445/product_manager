from django.shortcuts import render,redirect
from .models import product
from .forms import productform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request):
    if request.method=="POST":
        form=productform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect("product_list")

    else:
        form=productform()

    return render(request,"product_form.html",{
        "form":form # takes your Python 
        # form and sends it to the HTML template.
    })

def product_list(request):
    products=product.objects.all()
    search=request.GET.get("search")

    if search:
        products=product.objects.filter(name__icontains=search)
    else:
        products=product.objects.all()

    return render(request,"product_list.html",{
        "products":products,
        "search":search
    })

def product_detail(request,proid):
    products=product.objects.get(proid=proid)

    return render(request,"product_detail.html",{
        "products":products
    })

def edit_product(request,proid):
    product_obj=product.objects.get(proid=proid)

    if request.method=="POST":

        form=productform(request.POST,request.FILES,instance=product_obj)

        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form=productform(instance=product_obj)

    return render(request,"product_form.html",{
        "form":form
    })

# instance=product_obj tells Django:
# Update this existing product instead of 
# creating a new product.

def delete_product(request,proid):
    product_obj=product.objects.get(proid=proid)
    product_obj.delete()

    return redirect("product_list")

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(
            request=request,
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)
            return redirect('product_list')

    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

#  render means take that html file and show it to the user
