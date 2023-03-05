from django.conf.urls import url,include
from mainapp import views
urlpatterns = [
     url(r'^$',views.leaderboard,name='leaderboard'),
     url(r'^login/',views.login,name='login'),
     url(r'^log/',views.log,name='log'),
     url(r'^register/',views.register,name='register'),
     url(r'^profile/',views.profile,name='profile'),
     url(r'^compete/',views.compete,name='compete'),
     

]