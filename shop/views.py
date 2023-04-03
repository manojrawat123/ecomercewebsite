from django.shortcuts import render, HttpResponseRedirect
from shop.forms import MyUserCreationForm,MyLoginForm, MyPasswordChangeForm, MyCustomerForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from shop.models import Product, Cart, Customer, OrderPlaced
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
# def home(request):
#     return render(request, "shop/index.html", {"home": "font-bold text-green-500 underline"})

class HomePage(View):
    def get(self, request):
        mobile = Product.objects.filter(category = "M")
        laptop = Product.objects.filter(category = "L")
        tshirt = Product.objects.filter(category = "TS")
        shoes = Product.objects.filter(category = "Shoes")
        vechile = Product.objects.filter(category = "EV")
        bike = Product.objects.filter(category = "BK")
        allitems = Product.objects.all()
        return render(request, "shop/index.html", {"home": "font-bold text-green-500 underline", "mobile": mobile, "laptop": laptop, "tshirt": tshirt, "shoes": shoes
                                                   , "vechiele": vechile, "bike": bike, "allitems": allitems})

def login_page(request):
    if request.method == "POST":
        forms = MyLoginForm(request=request, data= request.POST)
        if forms.is_valid():
            uname = forms.cleaned_data["username"]
            upwd = forms.cleaned_data["password"] 
            user = authenticate(username = uname, password = upwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/profile")
    else:
        forms = MyLoginForm()
    return render(request, "shop/login.html", {"login":"font-bold text-green-500 underline", "forms": forms})



def signup_page(request):
    if request.method == "POST":
        forms = MyUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect("/login")
    else:
        forms = MyUserCreationForm()
    return render(request, "shop/registration.html", {"registration":"font-bold text-green-500 underline" ,"forms": forms})


def add_cart_page(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id = product_id)
    
    Cart(user= user, product = product).save()

    return HttpResponseRedirect("/show-cart")

def show_cart_page(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user= user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discount_price)
                amount += temp_amount
                total_amount = amount +shipping_amount
            return render(request, "shop/cart.html", {"cartc": "font-bold text-green-500 underline","cart": cart, "totalamount": total_amount, "amount": amount})        
        return render(request, "shop/emptycart.html")
    
def remove_item(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter

def plus_cart(request, pk):
    if request.user.is_authenticated:
        user = request.user
        product_id = pk
        cart = Cart.objects.get(Q(product = product_id)& Q(user= request.user))
        cart.quantity +=1
        cart.save()
        return HttpResponseRedirect("/show-cart")
    
def minus_cart(request, pk):
    if request.user.is_authenticated:
        user = request.user
        product_id = pk
        cart = Cart.objects.get(Q(product = product_id)& Q(user= request.user))
        if cart.quantity == 0:
            cart.quantity = 1
        cart.quantity -=1
        cart.save()
        return HttpResponseRedirect("/show-cart")
    
def remove_cart(request, pk):
    if request.user.is_authenticated:
        user = request.user
        product_id = pk
        cart = Cart.objects.get(Q(product = product_id)& Q(user = request.user))
        cart.delete()
        return HttpResponseRedirect("/show-cart")

def delete_items(request, pk):
    if request.user.is_authenticated:
        user = request.user
        product_id = pk
        order = OrderPlaced.objects.filter(Q(product = product_id)& Q(user = request.user))
        order.delete()

        return HttpResponseRedirect("/order")

def adress_page(request):
    adress = Customer.objects.filter(user= request.user)
    return render(request, "shop/adress.html", {"adress": adress, "active": "text-blue-700 bg-blue-100"})


class ProfileView(View):
    def get(self, request):
        forms = MyCustomerForm()
        return render(request, 'shop/profile.html', {'forms': forms, "active": "text-blue-700 bg-blue-100"})
    def post(self, request):
        forms = MyCustomerForm(request.POST)
        if forms.is_valid():
            myuser = request.user
            name = forms.cleaned_data["name"]
            locality = forms.cleaned_data["locality"]
            city = forms.cleaned_data["city"]
            state = forms.cleaned_data["state"]
            zipcode = forms.cleaned_data["zipcode"]
            mydata = Customer(user= myuser, name = name , locality= locality, city= city, state = state, zipcode= zipcode)
            mydata.save()
            messages.success(request,"Your Adress Is updated successfully!!")
            return HttpResponseRedirect("/profile")
        


def checkout_page(request):
    if request.user.is_authenticated:
        user = request.user
        adress = Customer.objects.filter(user= user) 
        

        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]

        if cart_product:
            for p in cart_product:
                temp_amount = (p.quantity * p.product.discount_price)
                amount += temp_amount
                total_amount = amount + shipping_amount
        for i in adress:
            id = i.id
        return render(request, "shop/checkout.html", {"address": adress, "cart": cart,  "totalamount": total_amount, "id": id})

def payment_page(request, pk):
    user = request.user
    customer =  Customer.objects.filter(id= pk)
    cart = Cart.objects.filter(user= user)
    for i in customer:
        customer = i     
    for c in cart:

        OrderPlaced(user= user, customer =  customer, product = c.product,  quantity = c.quantity ).save()
        c.delete()
    return HttpResponseRedirect("/order")

def order_page(request):
    order_placed = OrderPlaced.objects.filter(user = request.user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    order_product = [p for p in OrderPlaced.objects.all() if p.user == request.user]

    if order_product:
        for p in order_product:
            temp_amount = (p.quantity * p.product.discount_price)
            amount += temp_amount
            total_amount = amount +shipping_amount
    return render(request, "shop/orders.html", {"order_placed":order_placed,"totalamount": total_amount, "amount": amount})



def product_page(request, pk):
    item = Product.objects.filter(id = pk)
    item_already_in_cart = False
    item_already_in_cart = Cart.objects.filter(Q(product=pk) & Q(user = request.user)).exists()
    adress = Customer.objects.filter(user= request.user) 
    for i in adress:
            id = i.id
    return render(request, "shop/product.html", {"item": item,"item_in_cart": item_already_in_cart, "id": id})

def buy_page(request):
    return render(request, "shop/buy.html")

def change_password(request):
    forms = MyPasswordChangeForm(request.user, request.POST)
    if forms.is_valid():
        user = forms.save()
        update_session_auth_hash(request, user)  # Important!
        messages.success(request, 'Your password was successfully updated!')
        return HttpResponseRedirect("/")
    else:
        forms = MyPasswordChangeForm(user=request.user)
    return render(request, 'shop/changepassword.html', {"forms": forms} )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login")






#Product Details.
def mobile_details(request, data = None):
    if data == None:
        mobile = Product.objects.filter(category = "M")
    elif data == "oppo":
        mobile = Product.objects.filter(Q(category = "M") & Q(brand_name= "Oppo"))
    elif data == "samsung":
        mobile = Product.objects.filter(Q(category = "M") & Q(brand_name= "Samsung"))
    elif data == "nokia":
        mobile = Product.objects.filter(Q(category = "M") & Q(brand_name= "Nokia"))
    elif data == "less":
        mobile = Product.objects.filter(Q(category = "M") & Q(discount_price__lt = 10000))
    elif data == "above":
        mobile = Product.objects.filter(Q(category = "M") & Q(discount_price__gt = 10000))
    else:
        mobile = {"No Item Of your search":""}
    return render(request, "shop/mobile.html", {"mobiles": mobile})
    
def laptop_details(request, data = None):
    if data == None:
        laptop = Product.objects.filter(category = "L")
    elif data == "dell":
        laptop = Product.objects.filter(Q(category = "L") & Q(brand_name= "Dell"))
    elif data == "hp":
        laptop = Product.objects.filter(Q(category = "L") & Q(brand_name= "Hp"))
    elif data == "less":
        laptop = Product.objects.filter(Q(category = "L") & Q(discount_price__lte = 75000))
    elif data == "above":
        laptop = Product.objects.filter(Q(category = "L") & Q(discount_price__gte = 75000))
    else:
        laptop = {"No Item Of your search":""}
    return render(request, "shop/laptop.html", {"laptop": laptop})

def tshirt_details(request, data = None):
    if data == None:
        tshirt = Product.objects.filter(category = "TS")
    elif data == "blackbery":
        tshirt = Product.objects.filter(Q(category = "TS") & Q(brand_name= "Blackberry"))
    elif data == "addidas":
        tshirt = Product.objects.filter(Q(category = "TS") & Q(brand_name= "Addidas"))
    elif data == "nike":
        tshirt = Product.objects.filter(Q(category = "TS") & Q(brand_name= "Nike"))
    elif data == "less":
        tshirt = Product.objects.filter(Q(category = "TS") & Q(discount_price__lt = 300))
    elif data == "above":
        tshirt = Product.objects.filter(Q(category = "TS") & Q(discount_price__gt = 300))
    else:
        tshirt = {"No Item Of your search":""}
    return render(request, "shop/tshirt.html", {"tshirt": tshirt})

def shoes_details(request, data = None):
    if data == None:
        shoes = Product.objects.filter(category = "SHOES")
    elif data == "frye":
        shoes = Product.objects.filter(Q(category = "SHOES") & Q(brand_name= "Frye"))
    elif data == "addidas":
        shoes = Product.objects.filter(Q(category = "SHOES") & Q(brand_name= "Addidas"))
    elif data == "nike":
        shoes = Product.objects.filter(Q(category = "SHOES") & Q(brand_name= "Nike"))
    elif data == "less":
        shoes = Product.objects.filter(Q(category = "SHOES") & Q(discount_price__lt = 500))
    elif data == "above":
        shoes = Product.objects.filter(Q(category = "SHOES") & Q(discount_price__gt = 500))
    else:
        shoes = {"No Item Of your search":""}
    return render(request, "shop/shoes.html", {"shoes": shoes})

def car_details(request, data = None):
    if data == None:
        car = Product.objects.filter(category = "PV")
    elif data == "shelby":
        car = Product.objects.filter(Q(category = "PV") & Q(brand_name= "Shelby"))
    elif data == "bugati":
        car = Product.objects.filter(Q(category = "PV") & Q(brand_name= "Bugati"))
    elif data == "nano":
        car = Product.objects.filter(Q(category = "PV") & Q(brand_name= "Nano"))
    elif data == "less":
        car = Product.objects.filter(Q(category = "PV") & Q(discount_price__lt = 1000000))
    elif data == "above":
        car = Product.objects.filter(Q(category = "PV") & Q(discount_price__gt = 1000000))
    return render(request, "shop/car.html", {"car": car})

def bike_details(request, data = None):
    if data == None:
        bike = Product.objects.filter(category = "BK")
    elif data == "bmw":
        bike = Product.objects.filter(Q(category = "BK") & Q(brand_name= "BMW"))
    elif data == "herohonda":
        bike = Product.objects.filter(Q(category = "BK") & Q(brand_name= "Hero Honda"))
    elif data == "royalenfield":
        bike = Product.objects.filter(Q(category = "BK") & Q(brand_name= "Royal Enfield"))
    elif data == "less":
        bike = Product.objects.filter(Q(category = "BK") & Q(discount_price__lt = 1000000))
    elif data == "above":
        bike = Product.objects.filter(Q(category = "BK") & Q(discount_price__gt = 1000000))
    return render(request, "shop/bike.html", {"bike": bike})

    






