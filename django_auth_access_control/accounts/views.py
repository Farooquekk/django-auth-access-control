from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({
            "error":"POST request required"
            
        },status=405)
    

    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username,password=password)

    if user is None:
        return JsonResponse({
            "error":"Invalid Credentials"
        },status=401)
    
    login(request,user)
    return JsonResponse({
        "message":f" {user} --> Logged In Successfully"
    })

@login_required
def profile_view(request):
    return JsonResponse({
        "username":request.user.username,
        "is_authenticated":request.user.is_authenticated
    })

def logout_view(request):
    user = request.user.username
    logout(request)
    return JsonResponse({
        "message":f"{user} --> Logges out successfully"
    })


@permission_required("accounts.can_view_dashboard",raise_exception=True)
def dashboard_view(request):
    return JsonResponse({
        "message":"Dashboard access granted"
    }) 

@permission_required("accounts.can_export_data",raise_exception=True)
def export_view(request):
    return JsonResponse({
        "message":"Data export allowed"
    })