from django.shortcuts import render, redirect
from .models import post
from collections import deque
from .forms import profileForm
from django.views.generic import DetailView, CreateView
# Create your views here.
def sortInReverse(X):
    return sorted(X,key=lambda x:x[1], reverse=True)

def BbHomepage(request):
    posts = post.objects.all()
    posts_Latest = deque()
    for i in posts:
        posts_Latest.appendleft(i)

    return render(request, 'BbHomepage.html', {'posts': posts_Latest})
def BbAbout(request):
    return render(request, 'BbAbout.html')

class postDetailView(DetailView):
    model = post
class postCreateView(CreateView):
    model = post
    fields = ['content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def BbProfile(request):
    if request.method == 'POST':
        p_form = profileForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('/beatbox/profile/')
    else:
        p_form = profileForm(instance=request.user.profile)
    context = {
        'p_form': p_form
    }
    

    return render(request, 'BbProfile.html', context)