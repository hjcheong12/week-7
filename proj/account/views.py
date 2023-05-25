from django.shortcuts import render

#로그인
def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']


    user = auth.authenticate(request, username = userid, password = userpw)

    if user is not None:
        auth.login(request, user)
        return redirect('home')
    
    else:
        return render(request, 'login.html')