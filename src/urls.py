from django.urls import path
from .views import Home, Register, Login, InterestFromLendingMoney, Logout, Business, Agriculture, SavingsAndExpense
urlpatterns = [
    path('',Home,name='homepage'),

    # auth urls
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),

    # user urls
    path('interest-from-lending-money/',InterestFromLendingMoney,name='interest-from-lending-money'),
    path('business/',Business,name='business'),
    path('agriculture/',Agriculture,name='agriculture'),
    path('saving-expense/',SavingsAndExpense,name='saving-expense')
]
