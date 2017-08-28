from django.conf.urls import url
from django.contrib.auth.views import login, logout

from quiz_app import views

urlpatterns = [
    url(r'^$', views.QuizView.as_view(), name='quiz'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionView.as_view(), name='question'),
    url(r'^register/$', views.RegistrationFormView.as_view(), name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', logout, {'template_name': 'quiz/user/logout_user.html'}, name ='logout'),

]
