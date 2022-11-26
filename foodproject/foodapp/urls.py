
from django.urls import path,include
from.import views

urlpatterns = [

    path('',views.index,name='index'),
    path('food/<int:food_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_food'),
    path('update<int:id>/',views.update,name='update'),
    path('delete<int:id>/', views.delete, name='delete')
]