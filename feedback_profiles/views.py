from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "feedback_profiles/create_profile.html",
    model = UserProfile
    fields = "__all__"
    success_url = "/feedback_profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "feedback_profiles/user_profiles.html"
    context_object_name = "feedback_profiles"