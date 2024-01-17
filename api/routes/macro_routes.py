from django.urls import path
from ..views import macro
urlpatterns = [
path('/macro/calculate-expenditure/method-1/<str:id>', macro.calculate_expenditure_method_1, name='calculate_expenditure_method_1'),
path('/macro/calculate-expenditure/method-2/<str:id>', macro.calculate_expenditure_method_2, name='calculate_expenditure_method_2'),
path('/macro/re-calculate-expenditure/method-2/<str:id>', macro.re_calculate_expenditure_method_2, name='re_calculate_expenditure_method_2'),
path('/macro/calculate-macros/<str:id>', macro.calculate_macros, name='calculate_macros'),
path('/macro/update-expenditure/<str:id>', macro.update_expenditure, name='update_expenditure'),

]
