from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    basketGame=Game.objects.all()
    
    context={
        'basketGame':basketGame
    }
    return render(request, 'home.html', context)


def about(request):
    basketGame=Game.objects.all()
    
    context={
        'basketGame':basketGame
    }
    return render(request, 'about.html', context)


def contact(request):
    basketGame=Game.objects.all()
    
    context={
        'basketGame':basketGame
    }
    return render(request, 'contact.html', context)


def detail(request, id):
    game = Game.objects.get(id=id)
    deluxe = Game.objects.get(title=game.title, edition=2)
    ultimate = Game.objects.get(title=game.title, edition=3)
    basketGame=Game.objects.all()

    context = {
        'game': game,
        'deluxe': deluxe,
        'ultimate': ultimate,
        'basketGame':basketGame
    }

    return render(request, 'detail.html', context)


def pc(request):
    pc = Game.objects.filter(platform=1, edition=1)
    order_by = request.GET.get("order_by")
    query = request.GET.get("searchInput")
    basketGame=Game.objects.all()

    if query:
        pc = pc.filter(Q(title__icontains=query)).distinct

    if order_by == "low":
        pc = pc.order_by('price')

    if order_by == "high":
        pc = pc.order_by('-price')

    context = {
        'pc': pc,
        'basketGame':basketGame
    }

    return render(request, 'pc.html', context)


def ps5(request):
    ps5 = Game.objects.filter(platform=2, edition=1)
    order_by = request.GET.get("order_by")
    query = request.GET.get("searchInput")
    basketGame=Game.objects.all()

    if query:
        ps5 = ps5.filter(Q(title__icontains=query)).distinct

    if order_by == "low":
        ps5 = ps5.order_by('price')

    if order_by == "high":
        ps5 = ps5.order_by('-price')

    context = {
        'ps5': ps5,
        'basketGame':basketGame
    }

    return render(request, 'ps5.html', context)


def xbox(request):
    xbox = Game.objects.filter(platform=3, edition=1)
    order_by = request.GET.get("order_by")
    query = request.GET.get("searchInput")
    basketGame=Game.objects.all()

    if query:
        xbox = xbox.filter(Q(title__icontains=query)).distinct

    if order_by == "low":
        xbox = xbox.order_by('price')

    if order_by == "high":
        xbox = xbox.order_by('-price')

    context = {
        'xbox': xbox,
        'basketGame':basketGame
    }

    return render(request, 'xbox.html', context)

def profile(request):
    
    return render(request,'profile.html')

def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        surName=request.POST["surName"]
        userName=request.POST["userName"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        
        if password==password2:
            if User.objects.filter(username=userName).exists():
                context={
                    'information':'This username is used. Try a different username!'
                }
                return render(request,'user/register.html',context)
            
            if User.objects.filter(email=email).exists():
                context={
                    'information':'This e-mail address is used. Try a different email address!'
                }
                return render(request,'user/register.html',context)
            
            else:
                user=User.objects.create_user(first_name=name,last_name=surName,username=userName,email=email,password=password)
                user.save()
                pro=Profil(user_id=user.id,profileImg=None)
                pro.save()
                return redirect('/')
        else:
            context = {
                'information':'Your password does not match the replay password you entered!'
            }
            return render(request,'user/register.html',context)
    
    return render(request,'user/register.html')

def loginn(request):
    if request.method=="POST":
        userName=request.POST["userName"]
        password=request.POST["password"]
        
        user=authenticate(request,username=userName,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            context={
                'information':'The username or password you entered is incorrect, try again!'
            }
            
            return render(request,'user/login.html',context)
        
    return render(request,'user/login.html')

def logoutt(request):
    logout(request)
    
    return redirect('/')

@login_required
def profile(request):
    
    profile=Profil.objects.get(user_id=request.user)
    basketGame=Game.objects.all()
    game=Game.objects.all()
    user = User.objects.get(username=request.user)
    liked_games = user.liked_games.all()
    
    if request.method=='POST' and 'profile-img-btn' in request.POST:
        filee=request.FILES.get("image")
        
        if filee:
            profile.profileImg=filee
            profile.save()
            
            context={
                'profile':profile
            }
            
            return render(request,'profile.html',context)
    
    if request.method == "POST" and "save" in request.POST:
        user = request.user
        user.username = request.POST['username']
        user.first_name = request.POST['firstName']
        user.last_name = request.POST['lastName']
        user.email = request.POST['email']
        
        user.save()
        
    context={
        'profile':profile,
        'basketGame':basketGame,
        'game':game,
        'liked_games':liked_games
    }
    
    return render(request,'profile.html',context)

def community(request):
    comment=Comment.objects.all()
    game=Game.objects.all()
    basketGame=Game.objects.all()
    
    if request.method == "POST":
        comment_text = request.POST.get("commentText")
        game_id = request.POST.get("game")  # Seçilen oyunun ID'sini alın
        if comment_text and game_id:
            # Seçilen oyunu veritabanından alın
            game = Game.objects.get(id=game_id)
            # Yeni bir yorum oluşturun ve veritabanına kaydedin
            comment = Comment(comment=comment_text, user=request.user, gameComment=game)
            comment.save()

            # Yorumu oluşturduktan sonra, kullanıcıyı aynı sayfaya yönlendirin veya başka bir sayfaya yönlendirin
            return redirect('community')  # community adlı görünüme yönlendirme yapabilirsiniz
    
    context={
        'comment':comment,
        'game':game,
        'basketGame':basketGame
    }
    
    return render(request,'community.html',context)

def liked(request,id):
    game=Game.objects.get(pk=id)

    if request.user in game.likes.all():
        game.likes.remove(request.user)

    else:
        game.likes.add(request.user)

    game.likes_count=game.likes.count()
    game.save()
    
    return redirect('/')

def basket(request,id):
    game=Game.objects.get(pk=id)

    if request.user in game.basket.all():
        game.basket.remove(request.user)

    else:
        game.basket.add(request.user)

    game.basket_amount=game.basket.count()
    game.save()
    
    return redirect('/')


def completeOrder(request):
    basketGame=Game.objects.all()
    
    context={
        'basketGame':basketGame
    }
    return render(request, 'completeOrder.html', context)