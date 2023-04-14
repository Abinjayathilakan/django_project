from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.form,name='form'),
   # path('add_details',views.add_details,name='add_details'),
   path('signup',views.signup,name='signup'),
   
   path('add_admin', views.add_admin, name='add_admin'),
   
   # path('super', views.super, name='super'),
   
   path('base',views.base,name='base'),
   path('add_course', views.add_course, name='add_course'),
   path('add_coursedb',views.add_coursedb,name='add_coursedb'),
   path('addstudents',views.addstudents,name='addstudents'),
   path('add_studentdb',views.add_studentdb,name='add_studentdb'),
   path('show_student',views.show_student,name='show_student'),
   path('editpage/<int:pk>',views.editpage,name='editpage'),
   path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
   path('add_admins', views.add_admins, name='add_admins'),
   
   
   path('add_teacherdb', views.add_teacherdb, name='add_teacherdb'),
   path('teacher_home', views.teacher_home, name='teacher_home'),
   path('see_profile',views.see_profile,name='see_profile'),
   path('teacher_profile',views.teacher_profile,name='teacher_profile'),
   path('logout',views.logout,name='logout'),
   path('show_teacher',views.show_teacher,name='show_teacher'),
   path('edit_teacher',views.edit_teacher,name='edit_teacher'),
   path('editdb',views.editdb,name='editdb'),
]
