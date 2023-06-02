from django.urls import path
from .import views

urlpatterns=[
    path('',views.Index,name='home/'),
    path('about/',views.About,name='about/'),
    path('base/',views.Base,name='base/'),
    path('categories/<int:id>/',views.food_categories,name='categories/<int:id>/'),
    # path('subcategories/',views.sub_categories,name='subcategories/'),
    path('sub/',views.sub,name='sub/'),
    path('order/',views.order,name='order/'),
    path('order_view/',views.OrderView,name='order_view/'),
    path('update/<int:id>/',views.update,name='update/<int:id>/'),
    path('delete/<int:id>/',views.delete,name='delete/<int:id>/'),
    path('contact/',views.contact,name='contact/')
]
