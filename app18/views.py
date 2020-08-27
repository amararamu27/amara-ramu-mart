from django.shortcuts import render,redirect
from app18.models import CustomerModel,ProductModel,OrderModel

def showIndex(request):
    return render(request,'index.html')

def adminLogin(request):
    return render(request,"admin_login.html")

def checkAdminDetails(request):
    aname = request.POST.get('a1')
    apass = request.POST.get('a2')

    if aname == 'amara' and apass == 'ramu':
        return render(request,"admin_home.html")
    else:
        return render(request,'admin_login.html',{'data':"Inavalid User!"})

def adminHome(req):
    return render(req,'admin_home.html')

def addProducts(request):
    return render(request,'add_products.html')

def saveProductDetails(request):
    pname = request.POST.get('p1')
    price = request.POST.get('p2')
    qty = request.POST.get('p3')
    photo = request.FILES['p4']

    ProductModel(pname=pname,price=price,quantity=qty,photo=photo).save()

    return redirect('admin_home')

def viewProducts(request):
    return render(request,"viewProducts.html",{'data1':ProductModel.objects.all()})


def customerRegistration(request):
    return render(request,'customer_reg.html')

def saveCustomerDetails(request):
    cname = request.POST.get('c1')
    contact = request.POST.get('c2')
    address = request.POST.get('c3')
    password = request.POST.get('c4')
    photo = request.FILES['c5']

    CustomerModel(cname=cname,contact=contact,address=address,password=password,photo=photo).save()

    return redirect('main')

def customerLogin(request):
    return render(request,'customer_login.html')

def checkCustomerDetails(request):
    cno = request.POST.get('cl1')
    cpass = request.POST.get('cl2')

    try:
        res = CustomerModel.objects.get(contact=cno,password=cpass)
        request.session["user"] = res.cid

        return render(request,'customer_home.html',{'data3':res})
    except CustomerModel.DoesNotExist:
        return render(request,'customer_login.html',{"data2":"Invalid User!"})

def customerHome(request):
    return render(request,'customer_home.html',{'data3':CustomerModel.objects.get(cid=request.session.get('user'))})

def viewAllProducts(request):
    return render(request,'view_all_products.html',{'data4':ProductModel.objects.all()})

def saveOrders(request):
    pid = request.POST.get('pid')
    cid = request.POST.get('cid')

    try:
        OrderModel.objects.get(product_id=pid,customer_id=cid)
        return render(request, 'view_all_products.html', {'data5': "Duplicate Order.",'data4':ProductModel.objects.all()})
    except OrderModel.DoesNotExist:
        OrderModel(product_id=pid,customer_id=cid).save()
        return render(request,'view_all_products.html',{'data5':"Your order has been placed!",'data4':ProductModel.objects.all()})

def showOrders(request):
    res3 = OrderModel.objects.filter(customer_id=request.session.get('user'))
    if res3:
        return render(request, 'my_orders.html', {'data6': res3})
    else:
        return render(request, 'my_orders.html', {'data7': 'You have no orders yet!'})

def updateProduct(request):
    pid = request.GET.get('pid')
    res8 = ProductModel.objects.get(pid=pid)
    return render(request,'update_product.html',{'data8':res8})

def updateDetails(request):
    pid = request.POST.get('u0')
    pname = request.POST.get('u1')
    price = request.POST.get('u2')
    qty = request.POST.get('u3')
    img = request.FILES['u4']
    res7 = ProductModel.objects.get(pid=pid)
    res7.pname = pname
    res7.price = price
    res7.quantity = qty
    res7.photo = img
    print(img)
    res7.save()
    return redirect('view_products')

def deleteProduct(request):
    pid = request.GET.get('pid')
    ProductModel.objects.get(pid=pid).delete()
    return redirect('view_products')

def cancelOrder(request):
    oid = request.POST.get('oid')
    OrderModel.objects.get(oid=oid).delete()
    return render(request, 'my_orders.html', {'data6': OrderModel.objects.filter(customer_id=request.session.get('user'))})

