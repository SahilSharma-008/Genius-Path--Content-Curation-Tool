from django.contrib import admin
from django.urls import path,include
from main import views

#django admin header
admin.site.site_header="Developer Genius_Path"
admin.site.site_title="Welcome to Dashboard"
admin.site.index_title="Welcome to this portal"

urlpatterns = [
    path('Code with Harry', views.harry, name='cwh'),
    path('Shraddha Khapra', views.shraddha, name='sk'),
    path('Code Help',views.codehelp,name='lovebabbar'),
    path('',views.index,name='home'),
    path('roadmaps.html',views.roadmaps,name='roadmaps'),
    path('doubts.html',views.doubts,name='doubts'),
    path('contact.html',views.contact,name='contact'),
    path('courses.html',views.courses,name='courses'),
    path('index.html',views.index,name='home'),
    path('teachers.html',views.teachers,name='teachers'),
    path('signin.html',views.signin,name='signin'),
    path('signup.html',views.signup,name='signup'),
    path('welcome.html',views.welcome,name='welcome'),
]