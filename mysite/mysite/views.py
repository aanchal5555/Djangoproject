from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Order.models import Orders,OrderUpdate
from productcart.models import Products, Category,Subcategory
import json




def contactus(request):
    return render(request,'contactus.html')

def chatbot(request):
    return render(request,'chatbot.html')

def home(request):
    try:
        homepage_category = Category.objects.get(name='homepage')
        productdata = Products.objects.filter(category=homepage_category)
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "index.html", data)

    except Category.DoesNotExist:      
        return HttpResponse("Homepage category does not exist")

def render_shirts(request):
    try:   
        mens_category = Category.objects.get(name="Mens")        
        subcategory_name = "shirts"
        subcategory = Subcategory.objects.get(name=subcategory_name)

       
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)

        
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "shirts.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Mens category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'shirts' does not exist")

def render_jeans(request):
    try:    
        mens_category = Category.objects.get(name="Mens")       
        subcategory_name = "jeans"
        subcategory = Subcategory.objects.get(name=subcategory_name)       
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5
        data = {
            'productdata': productdata
        }
        return render(request, "jeans.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Mens category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'jeans' does not exist")

def render_saree(request):
    try:
       
        mens_category = Category.objects.get(name="Womens")

       
        subcategory_name = "saree"
        subcategory = Subcategory.objects.get(name=subcategory_name)

       
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)


        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "saree.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Womens category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'saree' does not exist")

def render_suits(request):
    try:

        mens_category = Category.objects.get(name="Womens")

        
        subcategory_name = "suits"
        subcategory = Subcategory.objects.get(name=subcategory_name)

       
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)

        
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "suits.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Womens category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'suits' does not exist")

def render_wjeans(request):
    try:
        
        mens_category = Category.objects.get(name="Womens")

    
        subcategory_name = "wjeans"
        subcategory = Subcategory.objects.get(name=subcategory_name)

        
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)

        
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "wjeans.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Womens category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'wjeans' does not exist")


def render_top(request):
    try:

        mens_category = Category.objects.get(name="Womens")

        
        subcategory_name = "top"
        subcategory = Subcategory.objects.get(name=subcategory_name)

       
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)

        
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "top.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Womens category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'top' does not exist")


def render_earrings(request):
    try:
       
        mens_category = Category.objects.get(name="Jewellery")

       
        subcategory_name = "earrings"
        subcategory = Subcategory.objects.get(name=subcategory_name)

       
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)

       
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "earings.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Jewellery category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'earrings' does not exist")
    



def render_necklace(request):
    try:
       
        mens_category = Category.objects.get(name="Jewellery")

       
        subcategory_name = "necklace"
        subcategory = Subcategory.objects.get(name=subcategory_name)

        
        productdata = Products.objects.filter(category=mens_category, subcategory=subcategory)

       
        for product in productdata:
            if product.showcase_rating is not None:
                product.rating_difference = 5 - product.showcase_rating
            else:
                product.rating_difference = 5

        data = {
            'productdata': productdata
        }
        return render(request, "necklace.html", data)

    except Category.DoesNotExist:
        return HttpResponse("Jewellery category does not exist")
    except Subcategory.DoesNotExist:
        return HttpResponse("Subcategory 'necklace' does not exist")
    









    
def SignupPage(request):
    if request.method == 'POST':
       
        
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

       
        
        if len(uname) > 10:
            messages.error(request, "username must be under 10 characters")
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, "password do not match")
            return redirect('signup')
        
        if not uname.isalnum():
            messages.error(request, "username only contain letters and numbers")
            return redirect('signup')
        
       

        myuser = User.objects.create_user(uname, email, pass1)
        
        myuser.save()
        messages.success(request, "Your account created successfully")
        return redirect("login")

    else:
        return render(request, 'signup.html')
    
    # Add a return statement here to handle the case when request.method is not 'POST'

def LoginPage(request):
    if request.method == 'POST':
        #get the post parameter
        
        loginusername=request.POST['username']
        loginpassword=request.POST['pass']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"successfully logedin")
            return redirect("/")
        else:
            messages.error(request,"Invalid credentials")
    

    return render(request,"login.html")

def LogoutPage(request):
   
        logout(request)
        messages.success(request,"successfully logedout")
        return redirect("/")
    
    
def productview(request,myid):
    #fetch the product using the id
    product=Products.objects.filter(id=myid)
    print(product)
    return render(request,'productview.html',{'product':product[0]})



def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    return render(request,'checkout.html')
        
        


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'tracker.html')



def render_about(request):
    return render(request, "about.html")



