from django.shortcuts import render,redirect
from .models import Food_Categories, OrderForm, Sub
from django.contrib import messages
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.

def Index(request):
    Food_Details={
        'food':Food_Categories.objects.all()
    }
    return render(request,'index.html',Food_Details)

def About(request):
    Food_Details={
        'food':Food_Categories.objects.all()
    }
    return render(request,'about.html',Food_Details)

def categories(request):
    return render(request,'categories.html')

def Base(request):
    Food_Details={
        'food':Food_Categories.objects.all()
    }
    return render(request,'base.html',Food_Details)

def food_categories(request,id):
    Food_Details={
        'food':Sub.objects.filter(foodcate_name_id=id)
    }
    return render(request,'categories.html',Food_Details)

# def sub_categories():
#     Sub_Details={
#         'sub':Sub_Category.objects.all()
#     }
#     return render(request,'subcategories.html',Sub_Details)

def sub(request):
    Sub_Detail={
        'subcate':Sub.objects.all()
    }
    return render(request,'sub.html',Sub_Detail)

def order(request):
    cate_details={
        'cate_c':Food_Categories.objects.all(),
        'food':Food_Categories.objects.all()
    }
    if request.method=='POST':
        f_name=request.POST['FoodName']
        quantity=request.POST['Quantity']
        email=request.POST['Email']
        mobile=request.POST['MobileNumber']
        foodcate_name=request.POST['Cate']
        message=request.POST['Message']
        obj=OrderForm()
        obj.food_name=f_name
        obj.food_quantity=quantity
        obj.customer_email=email
        obj.customer_Mobile=mobile
        obj.foodcate_name_id=foodcate_name
        obj.message=message
        obj.save()
        try:
            messages.success(request,"Order Successfully")
        except:
            messages.error(request,"Order Unsuccessfully")
        return redirect('/home/order_view')
    return render(request,'order.html',cate_details)

def OrderView(request):
    order_details={
        'order':OrderForm.objects.all(),
        'food':Food_Categories.objects.all()
    }
    return render(request,'order_view.html',order_details)

def update(request,id):
    mydata=OrderForm.objects.get(id=id)
    order_data={'data':mydata,'cate_c':Food_Categories.objects.all(),
    'food':Food_Categories.objects.all() 
    }
    if request.method=='POST':
        f_name=request.POST['FoodName']
        quantity=request.POST['Quantity']
        email=request.POST['Email']
        mobile=request.POST['MobileNumber']
        foodcate_name=request.POST['Cate']
        message=request.POST['Message']
        mydata.food_name=f_name
        mydata.food_quantity=quantity
        mydata.customer_email=email
        mydata.customer_Mobile=mobile
        mydata.foodcate_name_id=foodcate_name
        mydata.message=message
        mydata.save()
        order_details={
            'order':OrderForm.objects.all()   
        }
        return redirect('/home/order_view',order_details)
    return render(request,'update.html',context=order_data)
    


def delete(request,id):
    mydata=OrderForm.objects.get(id=id)
    mydata.delete()
    order_details={
        'order':OrderForm.objects.all()
    }
    return redirect('/home/order_view',order_details)


def contact(request):
    if request.method=='POST':
        name=request.POST['userName']
        email=request.POST['Email']
        mobile=request.POST['MobileNumber']
        message=request.POST['Message']
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        email_messages=mail.EmailMessage(f'Email from {name}',f'UserEmail:{email}\nUserPhoneNumber:{mobile}\n\nQUERY:{message}',
        from_email,['rskrishnakeerthana2019@gmail.com'],connection=connection)
        connection.send_messages([email_messages])
        connection.close()
        messages.info(request,"Thanks for your messages! We will get back you soon...")
        return redirect('contact/')
    Food_Details={
        'food':Food_Categories.objects.all()
    } 
    return render(request,'contact.html',Food_Details)

