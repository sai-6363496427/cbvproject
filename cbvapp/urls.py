from django.urls import path
from cbvapp import views


urlpatterns = [
    path('',views.companylist.as_view(),name = 'list'),
    path('create/',views.companyCreate.as_view(),name = 'Create'),
    path('<int:pk>/',views.companydetails.as_view(),name = 'detail'),
    path('update/<int:pk>/',views.companyupdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.companydelete.as_view(),name='delete'),
]