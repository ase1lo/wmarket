from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'auth/register.html'


class SignIn(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('products')


# class UserProfile(DetailView):
#     model = CustomUser
#     template_name = 'profile/user_profile.html'
#     context_object_name = 'user'

#     def check_follow(self, follower, author):
#         try:
#             Follower.objects.get(follower=follower, author=author)
#             return True
#         except:
#             return False

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         user = data['user']
#         topics = Topic.objects.filter(author=user)
#         followers = Follower.objects.filter(author=user)
#         # following = Follower.objects.filter(follower=user) <- подписки 
#         data['topics'] = topics
#         data['num_of_topics'] = topics.count()
#         data['num_of_followers'] = followers.count()
#         # data['num_of_following'] = following.count() <- выпод подписок 
#         data['is_follow'] = self.check_follow(self.request.user, user)
#         print(topics)

#         return data


# def follow(request, author_id):
#     follower = request.user
#     author = CustomUser.objects.get(pk=author_id)
#     try:
#         Follower.objects.get(follower=follower, author=author)
#     except:
#         create_follower = Follower.objects.create(follower=follower, author=author)
#         create_follower.save()
#     return redirect(request.path.rstrip('/follow'))


# def unfollow(request, author_id):
#     follower = request.user
#     author = CustomUser.objects.get(pk=author_id)
#     try:
#         tmp = Follower.objects.get(follower=follower, author=author)
#         tmp.delete()
#     except:
#         print('Удалять нечего')
#     return redirect(request.path.rstrip('/unfollow'))
