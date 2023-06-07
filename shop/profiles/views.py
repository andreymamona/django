import logging

from faker import Faker
from profiles.forms import LoginForm, RegisterForm

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

fake = Faker()


logger = logging.getLogger(__name__)


def profiles(request):
    # if request.GET.get('param'):
    #     logger.info(f'My param: {request.GET.get("param")}')
    # if request.GET:
    #     for key, value in request.GET.items():
    #         logger.info(f'My param: {key} - {value}')
    # logger.info(os.getenv("MY_DEBUG_VARIABLE"))
    # logger.info(type(os.getenv("MY_DEBUG_VARIABLE")))
    # logger.info(settings.DEBUG)
    # logger.info(type(settings.DEBUG))
    # logger.info(settings.PRIMARY_VALUE)
    if settings.PRIMARY_VALUE == "FUN":
        ERL = settings.FIRST_CHARACTER
        logger.info(f"Your character is {settings.FIRST_CHARACTER}")
    elif settings.PRIMARY_VALUE == "SMART":
        ERL = settings.SECOND_CHARACTER
        logger.info(f"Your character is {settings.SECOND_CHARACTER}")
    else:
        ERL = "LOSER"
        logger.info("Your character is LOSER")
    return HttpResponse(f"Profile index view. Hi, {ERL}")


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["are_you_older_18"] is True:
                if (
                    form.cleaned_data["password"]
                    == form.cleaned_data["repeat_password"]
                ):
                    # Process validated data

                    User.objects.create_user(
                        email=form.cleaned_data["email"],
                        password=form.cleaned_data["password"],
                        first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        username=form.cleaned_data["username"],
                    )
                    return HttpResponse(
                        "Thanks for registration :) <br> <p><a href='/'>Main page</a></p>"
                    )
                else:
                    return HttpResponse(
                        "Sorry, you entered different passwords <br> <p><a href='/'>Main page</a></p>"
                        "<br> <p><a href='/register'>Registration</a></p>"
                    )
            else:
                return HttpResponse(
                    "Sorry, you must be older than 18 <br> <p><a href='/'>Main page</a></p>"
                )
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


def random_generator(request):
    ...
