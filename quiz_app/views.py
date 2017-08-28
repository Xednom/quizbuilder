from django.contrib.auth import (login as auth_login, authenticate)
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views import generic, View

from .forms import RegistrationForm
from .models import Quiz, Question, Choice

# Create your views here.

class QuizView(generic.ListView):
    template_name = 'quiz/user/quiz.html'
    context_object_name = 'latest_quiz_list'

    def get_queryset(self):
        return Quiz.objects.order_by('-date_created')[:5]

class QuestionView(generic.DetailView):
    model = Question
    template_name = 'quiz/user/question.html'

class RegistrationFormView(View):
    form_class = RegistrationForm
    template_name = 'quiz/user/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            _username = form.cleaned_data['username']
            _password = form.cleaned_data['password1']
            user.set_password(_password)
            user.save()
            return redirect(reverse('login'))
        return render(request, 'quiz/user/registration.html', {'form':form})

def login(request):
    _message = 'Please login here'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('quiz'))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Wrong username or password.'
    context = {'message': _message,}
    return render(request, 'quiz/user/login.html', context)
