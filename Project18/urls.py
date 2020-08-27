"""Project18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app18 import views
from django.conf.urls.static import static
from Project18 import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex, name = 'main'),
    path('admin_login/',views.adminLogin, name = 'admin_login'),
    path('check_admin_details/',views.checkAdminDetails, name = 'check_admin_details'),
    path('admin_home/',views.adminHome, name = 'admin_home'),
    path('add_products/',views.addProducts, name = 'add_products'),
    path('save_product_details/',views.saveProductDetails, name = 'save_product_details'),
    path('view_products',views.viewProducts, name = 'view_products'),
    path('customer_reg/',views.customerRegistration, name = 'customer_reg'),
    path('save_customer_details/',views.saveCustomerDetails, name = 'save_customer_details'),
    path('customer_login/',views.customerLogin, name = 'customer_login'),
    path('check_customer_details/',views.checkCustomerDetails, name = 'check_customer_details'),
    path('customer_home/',views.customerHome, name = 'customer_home'),
    path('view_all_products/',views.viewAllProducts, name = 'view_all_products'),
    path('save_orders/',views.saveOrders, name = 'save_orders'),
    path('show_orders/',views.showOrders,name = 'show_orders'),
    path('update_product/',views.updateProduct,name = 'update_product'),
    path('update_details/',views.updateDetails, name = 'update_details'),
    path('delete_product/',views.deleteProduct,name = 'delete_product'),
    path('cancel_order/',views.cancelOrder,name = 'cancel_order')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
