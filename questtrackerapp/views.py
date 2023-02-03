from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import registerdetails, assignproject, assignprojecttoteam, createteam
from django.contrib import messages
# Create your views here.


def new(request):
    return render(request, 'new.html')


def homepage(request):
    return render(request, 'border.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            return redirect('/adminpage')
        else:
            return HttpResponse('Invalid')
    return render(request, 'adminlogin.html')


def adminpage(request):
    return render(request, 'adminpage.html')


def managerlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'manager' and password == 'manager':
            return redirect('/managerpage')
        else:
            return HttpResponse('Invalid')
    return render(request, 'managerlogin.html')


def stafflogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            registerdetails.objects.get(Username=username, Password=password)
            save(username, password)
            return redirect('/staffpage')
        except:
            return HttpResponse("Invalid")
    return render(request, 'stafflogin.html')


def staffpage(request):
    return render(request, 'staffpage.html', {'value': q})


def managerpage(request):
    return render(request, 'managerpage.html')


def registerpage(request):
    g = createteam.objects.all()
    if request.method == "POST":
        details = registerdetails()
        name = request.POST['name']
        designation = request.POST['designation']
        gender = request.POST['gender']
        mail = request.POST['email']
        team = request.POST['team']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['password']
        contact = request.POST['contact']
        picture = request.FILES['picture']
        teamlead = request.POST['teamlead']
        details.Name = name
        details.Address = address
        details.Designation = designation
        details.Gender = gender
        details.Email = mail
        details.Team = team
        details.Username = username
        details.Password = password
        details.Contact = contact
        details.Picture = picture
        details.Teamlead = teamlead
        details.save()

    return render(request, 'registerpage.html', {'value': g})


def pending(request):
    d = assignprojecttoteam.objects.filter(Status=False)
    s = d.filter(Verification=True)
    return render(request, 'pendinglist.html', {'value': s})


def approve(request, id):
    data = assignprojecttoteam.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')


def approved(request):
    datas = assignprojecttoteam.objects.filter(Status=True)
    return render(request, 'approved.html', {'value': datas})


def delete(request, id):
    d = assignprojecttoteam.objects.get(id=id)
    assignproject.objects.get(Project_Name=d.Project_Name).delete()
    d.delete()
    return redirect('/approved')


def completedprojects(request):
    p = assignprojecttoteam.objects.filter(Verification=False, Submit=True)
    return render(request, 'completedprojects.html', {'value': p})


def unfinishedprojects(request):
    f = assignprojecttoteam.objects.filter(Submit=False)
    return render(request, 'unfinishedprojects.html', {'value': f})


def unfinishedproject(request):
    f = assignprojecttoteam.objects.filter(Submit=False)
    return render(request, 'unfinishedproject.html', {'value': f})


def verification(request, id):
    s = assignprojecttoteam.objects.get(id=id)
    s.Verification = True
    s.save()
    return redirect('/completedprojects')


def verified(request):
    c = assignprojecttoteam.objects.filter(Verification=True)
    return render(request, 'verifiedprojects.html', {'value': c})


def assignProject(request):
    if request.method == 'POST':
        d = assignproject()
        projectname = request.POST['prjctname']
        project = request.FILES['prjct']
        deadline = request.POST['deadline']
        d.Project = project
        d.Deadline = deadline
        d.Project_Name = projectname
        d.save()

    return render(request, 'assignproject.html')


def save(username, password):
    global un, pd, q
    un = username
    pd = password
    q = registerdetails.objects.get(Username=un, Password=pd)


def viewproject(request):
    s = assignprojecttoteam.objects.filter(Team=q.Team)
    return render(request, 'viewproject.html', {'value': s, 'val': q})


def newprojects(request):
    p = assignproject.objects.all()
    return render(request, 'newproject.html', {'value': p})


def assignprojectstoteam(request):
    a = registerdetails.objects.filter(Teamlead='yes')
    b = assignproject.objects.all()
    if request.method == 'POST':
        team = request.POST['team']
        file = request.FILES['prjct']
        deadline = request.POST['deadline']
        project_name = request.POST['project_name']
        d = assignprojecttoteam()
        tm = a.get(Team=team)
        print(tm, a)
        d.Team = team
        d.Project = file
        d.Deadline = deadline
        d.Project_Name = project_name
        d.Teamlead = tm.Name
        d.save()
    return render(request, 'assignprojecttoteam.html', {'value': a, 'val': b})


def submitproject(request):
    try:
        x = assignprojecttoteam.objects.get(Team=q.Team)
        if request.method == 'POST':
            file = request.FILES['project']
            x.Project_Report = file
            x.Submit = True
            x.save()
        return render(request, 'submitproject.html', {'value': q})
    except:
        return HttpResponse("Your have no assigned projects")



def employeedetails(request):
    c = registerdetails.objects.all()
    return render(request, 'employeedetails.html', {'value': c})


def employeedetail(request):
    c = registerdetails.objects.all()
    return render(request, 'employeedetail.html', {'value': c})


def newteam(request):
    if request.method == "POST":
        team_name = request.POST['Team']
        s = createteam()
        s.Team_Name = team_name
        s.Manager = "Manager"
        s.save()
    return render(request, 'newteam.html')