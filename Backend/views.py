from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import Deptdb, Doctordb
from Frontend.models import Appointmentdb
from Backend.forms import DoctorSearchForm
from django.contrib import messages

from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def indexpage(request):
    app = Appointmentdb.objects.all()
    if request.method == 'GET':
        form = DoctorSearchForm(request.GET)
        doctors = []

        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            if search_query:
                doctors = Appointmentdb.objects.filter(
                    Registrations=search_query) | Appointmentdb.objects.filter(
                    DrName=search_query
                )
        return render(request, 'indexpage.html', {'form': form, 'doctors': doctors, 'app': app})


def deleteindex(request, dataid):
    obj = Appointmentdb.objects.get(id=dataid)
    obj.delete()
    return redirect(indexpage)


def department(request):
    return render(request, "department.html")


def deptsave(request):
    if request.method == "POST":
        dt = request.POST.get("department")
        ds = request.POST.get("description")
        img = request.FILES["image"]
        obj = Deptdb(DeptName=dt, Description=ds, Image=img)
        obj.save()
        messages.success(request, "Saved successfully")
        return redirect(department)


def displaydept(request):
    data = Deptdb.objects.all()
    return render(request, "displaydept.html", {'data': data})


def editdept(request, dataid):
    data = Deptdb.objects.get(id=dataid)
    return render(request, "editdept.html", {'data': data})


def updatedept(request, dataid):
    if request.method == "POST":
        dt = request.POST.get("department")
        ds = request.POST.get("description")
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Deptdb.objects.get(id=dataid).Image
        Deptdb.objects.filter(id=dataid).update(DeptName=dt, Description=ds, Image=file)
        messages.success(request, "Update successfully")
        return redirect(displaydept)


def deletedept(request, dataid):
    obj = Deptdb.objects.get(id=dataid)
    obj.delete()
    messages.success(request, "Delete successfully")
    return redirect(displaydept)


def doctorlist(request):
    data = Deptdb.objects.all()
    return render(request, "doctorlist.html", {"data": data})


def doctorsave(request):
    if request.method == "POST":
        na = request.POST.get('doctorname')
        dp = request.POST.get('department')
        exp = request.POST.get('experience')
        ed = request.POST.get('education')
        reg = request.POST.get('registration')
        lan = request.POST.get('language')
        abt = request.POST.get('about')
        gn = request.POST.get('gender')
        tm = request.POST.get('timing')
        img = request.FILES['image']
        obj = Doctordb(Name=na, Department=dp, Experience=exp,
                       Education=ed, Language=lan, About=abt,
                       Gender=gn, Timing=tm, Registrations=reg, Image=img)
        obj.save()
        messages.success(request, "Saved successfully")
        return redirect(doctorlist)


def doctordisplay(request):
    data = Doctordb.objects.all()
    return render(request, 'doctordisplay.html', {"data": data})


def doctoredit(request, dataid):
    cat = Doctordb.objects.get(id=dataid)
    data = Deptdb.objects.all()
    return render(request, "doctoredit.html", {"cat": cat, "data": data})


def doctorup(request, dataid):
    if request.method == "POST":
        na = request.POST.get('doctorname')
        dp = request.POST.get('department')
        exp = request.POST.get('experience')
        ed = request.POST.get('education')
        reg = request.POST.get('registration')
        lan = request.POST.get('language')
        abt = request.POST.get('about')
        gn = request.POST.get('gender')
        tm = request.POST.get('timing')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Doctordb.objects.get(id=dataid).Image
        Doctordb.objects.filter(id=dataid).update(Name=na, Department=dp, Experience=exp,
                                                  Education=ed, Language=lan, About=abt,
                                                  Gender=gn, Timing=tm, Registrations=reg, Image=file)
        messages.success(request, "Update successfully")
        return redirect(doctordisplay)


def doctordel(request, dataid):
    obj = Doctordb.objects.get(id=dataid)
    obj.delete()
    messages.success(request, "Delete successfully")
    return redirect(doctordisplay)


def loginpg(req):
    return render(req, "Login.html")


def loginsave(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pwd
                messages.success(request, "Login successfully")
                return redirect(indexpage)

            else:
                messages.error(request, "Invalid Username")
                return redirect(loginpg)

        else:
            messages.error(request, "Invalid Password")
            return redirect(loginpg)


def logoutpg(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully")
    return redirect(loginpg)


def staff_page(request):
    return render(request, 'staff_page.html')


def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def staff_page(request):
    return render(request, 'staff_page.html')
