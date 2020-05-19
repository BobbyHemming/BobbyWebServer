from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User
# from .models import Profile
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from Blogging.forms import SignUpForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserProfile


def blog_home(request):
    return render(request, 'Blogging/BlogHome.html')


class ProfileView(DetailView):
    model = User
    template_name = 'Blogging/profile_detail.html'


class UserIndexView(ListView):
    template_name = 'Blogging/user_index.html'
    model = User

    def get_queryset(self):
        """Return all the users that contain the same string entered in the search bar"""
        query = self.request.GET.get('q')
        object_list = User.objects.filter(Q(username__icontains=query))
        return object_list


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Blogging:BlogHome')
    else:
        form = SignUpForm()
    return render(request, 'Blogging/create_user.html', {'form': form})


@login_required(login_url='Blogging:login')
def EditProfileView(request, pk):
    user = get_object_or_404(User, id=pk)
    user = request.user
    # user = authenticate(username=user.username, password=user.password)

    # if request.method == 'POST':
    #     form = ProfileEditForm(request.POST or None, request.FILES, instance=user.userprofile)
    #     if form.is_valid():
    #         form.save()

    if user is not None:
        form = ProfileEditForm(request.POST or None, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Blogging:profile_detail', kwargs={"pk": user.pk}))
        return render(request, 'Blogging/profile_edit.html', {'form': form})
    else:
        HttpResponseRedirect(reverse('Blogging:BlogHome'))




