from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def user_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        request.session['Name'] = name
        request.session['Email'] = email
        request.session['Phone'] = phone
        request.session['Password'] = password

        return redirect('user_login')
     
    return HttpResponse("registration page here")


def user_login(request):

    if request.method == "POST":
        login_email = request.POST['login-email']
        login_password = request.POST['login-password']

        Email = request.session['Email']
        Password = request.session['Password']

        # print(login_email,Email,Password,login_password)

        if "Email" in request.session:
            if (login_email == Email and login_password == Password):
                Name = request.session['Name']
                Phone = request.session['Phone']
                # request.session.modified = True
                data = {
                    "Name": Name,
                    "Email": Email,
                    "Phone": Phone,
                    "Password": Password,
                }
                return render(request, "app/home.html", {"dt": data})
            else:
                return redirect('login')
        else:
            return redirect('login')
    # else:
        # return redirect('login')
    
    return HttpResponse("login page here")


def user_logout(request):
    del request.session["Email"]
    return redirect('user_registration')


def user_profile(request):
    return HttpResponse("profile page here")
