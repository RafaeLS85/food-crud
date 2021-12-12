from django.urls import path
from . import views

# namespace:
app_name = 'food'

urlpatterns = [
    # /food/
    path('', views.list, name='list'),
    # /food/:id/
    path('<int:food_id>/', views.detail, name='detail'),
    # /food/add/
    path('add', views.add, name='add'),
    # /food/update/:id
    path('update/<int:food_id>', views.update, name='update'),
    # /food/delete/:id
    path('delete/<int:food_id>', views.delete, name='delete'),
]