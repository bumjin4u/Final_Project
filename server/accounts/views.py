from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def profile(request, username):
    person = get_user_model().objects.get(username=username)
    serializer = 
    return render(request, 'accounts/profile.html', context)

@require_http_methods(["POST"])
def follow(request, user_pk):
    if request.user.is_authenticated:
        # 나 == request.user
        me = request.user
        # 너 == pk가 user_pk인 유저 (팔로우할 유저)
        you = get_user_model().objects.get(pk=user_pk)
        if me != you:
            if me.followings.filter(pk=user_pk).exists():
                me.followings.remove(you)
            else:
                me.followings.add(you)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')