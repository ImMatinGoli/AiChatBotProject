from django.shortcuts import render
from django.views import generic

class LogOutConfirmView(generic.TemplateView):
    template_name = 'account/logout_confirm.html'
