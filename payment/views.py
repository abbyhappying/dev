from django.shortcuts import render

from . models import ShipppingAddress, Order, OrderItem

# cart文件夹和payment文件夹属于同一根目录，从cart文件夹下的cart文件中import def cart function model
from cart.cart import Cart

from django.http import JsonResponse

# Create your views here.

def checkout(request):

    if request.user.is_authenticated:
        try:
            # if the user_id is connected with shipping info, it will get the shipping info save as context
            shipping_address = ShipppingAddress.objects.get(user=request.user.id)
            context = {'shipping':shipping_address}
            return render(request,'payment/checkout.html', context=context)
        except:
            return render(request,'payment/checkout.html')
    else:
        return render(request,'payment/checkout.html')

def complete_order(request):

    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')

        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        shipping_address = (address1 + "\n" + address2 +"\n" + city+ "\n"+ state+ "\n"+ zipcode+ "\n")

        #shopping cart info include order info and order_item info
        cart = Cart(request)
        total_cost = cart.get_total()

        #create order->registered user with/without shipping address

        if request.user.is_authenticated:

            order = Order.objects.create(full_name = name, email = email, shipping_address=shipping_address,
                                         amount_paid = total_cost, user = request.user)
            order_id = order.pk #order primary key

            for item in cart:
                OrderItem.objects.create(order_id = order_id, product = item['product'], quantity = item['qty'], price = item['price'], user=request.user)

        #create order->guest user: *没有user foreign key
        else:
            order = Order.objects.create(full_name = name, email = email, shipping_address=shipping_address,
                                         amount_paid = total_cost)
            order_id = order.pk #order primary key

            for item in cart:
                OrderItem.objects.create(order_id = order_id, product = item['product'], quantity = item['qty'], price = item['price'])

        order_success = True

        response = JsonResponse({'success':order_success})

        return response


def payment_success(request):

    for key in list(request.session.keys()):
        if key == 'session_key':
            del request.session[key]
    return render(request,'payment/payment-success.html')

def payment_failed(request):

    return render(request,'payment/payment-failed.html')
