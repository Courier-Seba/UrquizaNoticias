from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")

        else:
            for mensaje in form.error_messages:
                print(form.error_messages[mensaje])

            return render(
                request=request,
                template_name="register.html",
                context={"form":form}
            )

    form = UserCreationForm
    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
    )
