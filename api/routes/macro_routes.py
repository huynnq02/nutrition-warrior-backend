from django.urls import path
from ..views import macro
urlpatterns = [
path('/calculate-expenditure/method-1', macro.calculate_expenditure_method_1, name='calculate_expenditure_method_1'),
path('/calculate-expenditure/method-2/<str:id>', macro.calculate_expenditure_method_2, name='calculate_expenditure_method_2'),
path('/re-calculate-expenditure/method-2/<str:id>', macro.re_calculate_expenditure_method_2, name='re_calculate_expenditure_method_2'),
path('/calculate-macros', macro.calculate_macros, name='calculate_macros'),
path('/update-expenditure/<str:id>', macro.update_expenditure, name='update_expenditure'),

]
