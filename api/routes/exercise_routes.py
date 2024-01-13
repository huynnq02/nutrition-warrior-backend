from django.urls import path
from ..views import exercise

urlpatterns = [
    path('/get-body-part-list/', exercise.get_body_part_list, name='get_body_part_list'),
    path('/get-exercises-for-body-part/<str:body_part>/', exercise.get_exercises_for_body_part, name='get_exercises_for_body_part'),
    path('/get-equipment-list/', exercise.get_equipment_list, name='get_equipment_list'),
    path('/get-target-list/', exercise.get_target_list, name='get_target_list'),
    path('/get-exercises-by-equipment/<str:equipment_type>/', exercise.get_exercises_by_equipment, name='get_exercises_by_equipment'),
    path('/get-exercises-by-target/<str:target_muscle>/', exercise.get_exercises_by_target, name='get_exercises_by_target'),
    path('/get-exercises-by-name/<str:exercise_name>/', exercise.get_exercises_by_name, name='get_exercises_by_name'),
    path('/get-all-exercises/', exercise.get_all_exercises, name='get_all_exercises'),
]
