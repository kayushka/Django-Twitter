from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from twitter.forms import AddTweetForm
from twitter.models import Tweet, Message


@login_required
def index_view(request):
    all_tweets = Tweet.objects.all()

    return render(request, 'twitter/index.html', context={'all_tweets': all_tweets})


@login_required
def add_new_tweet_view(request):
    if request.method == "GET":
        form = AddTweetForm()
        return render(request, 'twitter/new_tweet.html', {'form': form})
    else:
        form = AddTweetForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user
            new_tweet = Tweet.objects.create(content=content, user_id=user)
            return redirect('index')
        else:
            return render(request, 'twitter/new_tweet.html', {'form': form})


def home_view(request):
    return render(request, 'twitter/home.html')


@login_required
def user_view(request):
    user = request.user
    user_tweets = Tweet.objects.filter(user_id=user)
    return render(request, 'twitter/user.html', {'user_tweets': user_tweets})


@login_required
def message_view(request):
    all_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'twitter/messages.html', {'messages': all_messages})
