from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse   # pulling from other forms and pages and databases to make availble here
from django.shortcuts import render,redirect

from .forms import ContactForm, LoginForm, RegisterForm # These are two different form's imported from the forms.py

def home_page(request):
    context = {
        "title":"Hello World!",
        "content":" Welcome to the homepage.",

    }
    if request.user.is_authenticated():
        context["premium_content"] = ["Yeahhhhhh"]  # once logged in this premium content becomes accesible; hence the conditional 'if' statement
    return render(request, "home_page.html", context)

def about_page(request):  # Making the about page available by calling def about page
    context = {
    # this is the structure of the page below this line
        "title":"About Page",
        "content":" Welcome to the About page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)  #adding contact form (as a dictionary) created from the forms.py and adding it here  | adding request modifier to check if there is Post data pass to form if not pass none,
    context = {
    # this will be the structure of the contact page it will have title, content and then the form
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form
    }
    if contact_form.is_valid(): # if data provided in form is valid then pass it through and do not clear form.
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

def Blog_page(request):
    context = {
        "title":"Bmiti",
        "content":" Welcome to the Blog."
    }
    return render(request, "home_page.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)  # Displays the login form and listens for data to be intered into the form
    context = {
        "form": form
    }
    print("User logged in")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username") #this will make sure the user is real
        password = form.cleaned_data.get("password") # this will make sure the password is real
        user = authenticate(request, username=username, password=password) # running the username and password
        print(user)
        print(request.user.is_authenticated())  # log them in
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()  # new instance of login form, clears out data inputted
            return redirect("/") #if user is logged in the this function will pass and return to Home  page
        else:
            # Return an 'Invalid login' error message.

            print("Error")

    return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data) # accepts valid data entered into the form
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password) # creating model for future user account creations to follow
        print(new_user)
    return render(request, "auth/register.html", context)

def home_page_old(request):
    html_ ="""<html lang="en">
 <!doctype html>
 <html lang="en">

 <head>
   <!-- Required meta tags -->
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

   <!-- Bootstrap CSS -->
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

   <title>Hello, world!</title>
 </head>

 <body>
   <div class="text-center">

     <h1>Hello, world!</h1>
   </div>
   <!-- Optional JavaScript -->
   <!-- jQuery first, then Popper.js, then Bootstrap JS -->
   <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
 </body>

 </html>

"""
    return HttpResponse(html_)
