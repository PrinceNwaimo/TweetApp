from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from Tweet.models import Post


# Create your views here.

def welcome(request):
    tweets = Post.objects.all()
    return render(request, 'home.html', {"tweets": tweets})


# #
# def tweet_detail(request, pk):
#     try:
#         tweet = Post.objects.get(pk=pk)
#     except ObjectDoesNotExist:
#         return HttpResponse("Tweet with the given id does not exist")
#     return render(request, 'tweet_detail.html', {"tweet": tweet})


# or do this
def tweet_detail(request, pk):
    tweet = get_object_or_404(Post, pk=pk)
    return render(request, 'tweet_detail.html', {"tweet": tweet})


class CreateTweet(generic.CreateView):
    model = Post
    template_name = 'create-tweet.html'
    fields = ['tweet', 'author']
    # fields = '__all__'
