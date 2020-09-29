from django.shortcuts import render, redirect
from .models import post, like
from .forms import profileForm, EditForm, EditLikesForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def sortInReverse(X):
    return sorted(X,key=lambda x:x[1], reverse=True)

def BbHomepage(request):
    posts = post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if User.is_authenticated:
        current = request.user

    context = {
        'page_obj': page_obj,
        'current_user': current,
    }
    return render(request, 'BbHomepage.html', context)

postToEdit = None

def BbEditPost(request, pk):
    global postToEdit
    postToEdit = post.objects.get(id=pk)
    context = {
        'post': postToEdit
    }
    return render(request, 'BbEditPost.html', context)

def BbEditedPost(request):
    global postToEdit
    if request.method == 'POST':
        postEdit = EditForm(request.POST, request.FILES, instance=postToEdit)
        if postEdit.is_valid():
            postEdit.save()
            return redirect('/beatbox/')
        else:
            return redirect('/beatbox/post/edit/'+ str(postToEdit.id))

def BbDeletePost(request, pk):
    postToDelete = post.objects.get(id=pk)
    try:
        liketToDelete = like.objects.all().filter(liked_post_id=pk).delete()
        postToDelete.delete()
    except ObjectDoesNotExist:
        postToDelete.delete()
    except NameError:
        postToDelete.delete()
    return redirect('/beatbox/')

def BbCreatePost(request):
    if request.method == 'POST':
        newPostContent = request.POST['Content']
        newPostImage = request.FILES.get('Image', 'post_default.png')
        if User.is_authenticated:
            currentUser = request.user
            newPost = post.objects.create(author=currentUser, content=newPostContent, image=newPostImage)
            newPost.save()
            return redirect("/beatbox/")
        else:
            messages.info(request, "Login Required")
            return redirect("/accounts/login/")

def BbLikePost(request, keys):
    KEYS = keys
    keysList = list(map(int, KEYS.split(",")))
    print(keysList)
    user = request.user
    for i in keysList:
        post_liked = post.objects.get(id=i)
        if len(like.objects.all().filter(user=request.user, liked_post=post_liked)) > 0:
            print("Already Liked")
        else:
            post_liked.users_whomst_liked.add(user)
            post_liked.save()
            like_Action = like.objects.create(user=user, liked_post=post_liked)
            like_Action.save()
            updated_likes = post_liked.likes + 1
            likes_add = EditLikesForm({'likes': updated_likes}, instance=post_liked)
            if likes_add.is_valid():
                likes_add.save()
            print("Just Liked!")
            
    return HttpResponse('<script>location.replace("/beatbox/")</script>')

def BbProfile(request):
    if request.method == 'POST':
        profileChange = profileForm(request.POST, request.FILES, instance=request.user.profile)
        if profileChange.is_valid():
            profileChange.save()
            return redirect('/beatbox/profile/')
        else:
            return redirect('/beatbox/')
    else:
        profileToShow = request.user.profile
        context = {
            "profile": profileToShow
        }
        return render(request, 'BbProfile.html', context)
