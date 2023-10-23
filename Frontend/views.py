from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import Deptdb
from Backend.models import Doctordb
from Frontend.models import Appoinmentdb, Registerdb, Blogdb, Profiledb, Appointmentdb
from .forms import DoctorSearchForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from io import BytesIO
from django.template.loader import get_template
from django.views import View



# Create your views here.
def index(request):
    data = Deptdb.objects.all()
    dr = Doctordb.objects.all()
    bl = Blogdb.objects.all()
    if request.method == 'GET':
        form = DoctorSearchForm(request.GET)
        doctors = []

        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            if search_query:
                doctors = Deptdb.objects.filter(
                    DeptName=search_query)
        return render(request, 'index.html', {'form': form, 'data': data, 'doctors': doctors, 'dr': dr, 'bl': bl})


def aboutus(request):
    bl = Blogdb.objects.all()
    return render(request, 'aboutus.html', {'bl': bl})


def blog(request):
    bl = Blogdb.objects.all()
    return render(request, 'blog.html', {'bl': bl})


def doctors(request, drname):
    dr = Doctordb.objects.filter(Department=drname)
    return render(request, 'doctors.html', {'dr': dr})


def service(request):
    dept = Deptdb.objects.all()
    return render(request, 'service.html', {'dept': dept})


def appoinmentsave(request):
    if request.method == "POST":
        dt = request.POST.get('department')
        nm = request.POST.get('name')
        em = request.POST.get('email')
        da = request.POST.get('date')
        tim = request.POST.get('time')
        ph = request.POST.get('phone')
        obj = Appoinmentdb(Department=dt, DrName=nm, Email=em, Phone=ph, Date=da, Time=tim)
        obj.save()
        messages.success(request, "Booking successfully")
        return redirect(index)


def loginfr(request):
    return render(request, 'loginpg.html')


def registersave(request):
    if request.method == "POST":
        un = request.POST.get('username')
        en = request.POST.get('email')
        ps = request.POST.get('password')
        obj = Registerdb(Username=un, Email=en, Password=ps)
        obj.save()
        return redirect(loginfr)


def userlogin(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if Registerdb.objects.filter(Username=user, Password=pwd).exists():
            request.session['username'] = user
            request.session['password'] = pwd
            return redirect(index)
        else:
            return redirect(loginfr)
    else:
        return redirect(loginfr)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(index)


def blogsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        obj = Blogdb(Name=na, Email=em, Subject=sub, Message=msg)
        obj.save()
        return redirect(blog)


def profile(request):
    dt = Profiledb.objects.all()
    return render(request, 'profile.html', {'dt': dt})


def profileedit(request):
    return render(request, 'profileedit.html')


def profilesave(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        image = request.FILES['image']
        obj = Profiledb(Username=username, Name=name, Gender=gender, Birthday=birthday, Email=email, Location=location,
                        Phone=phone, Image=image)
        obj.save()
        return redirect(profile)


def proedit(request, dataid):
    edit = Profiledb.objects.get(id=dataid)
    return render(request, 'proedit.html', {'edit': edit})


def profileupdate(request, dataid):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Profiledb.objects.get(id=dataid).Image
        Profiledb.objects.filter(id=dataid).update(Username=username, Name=name, Gender=gender,
                                                   Birthday=birthday, Email=email, Location=location,
                                                   Phone=phone, Image=file)
        return redirect(profile)


def singledoctor(request, proid):
    single = Doctordb.objects.get(id=proid)
    return render(request, 'singledoctor.html', {'single': single})


def videocall(request):
    return render(request, 'videocall.html')


def joinmeeting(request):
    return render(request, 'videocall.html')


def appointment(request):
    return render(request, 'appoinmentpage.html')


def appointmentsave(request):
    if request.method == 'POST':
        dr = request.POST.get('drname')
        reg = request.POST.get('reg')
        us = request.POST.get('username')
        nm = request.POST.get('name')
        ph = request.POST.get('phone')
        em = request.POST.get('email')
        dt = request.POST.get('date')
        tm = request.POST.get('time')
        obj = Appointmentdb(DrName=dr, Registrations=reg, Name=nm, Username=us, Phone=ph, Email=em, Date=dt, Time=tm)
        obj.save()
        messages.success(request, "Booking successfully")
        return redirect(indexp)


def contact(request):
    if request.method == 'POST':
        message_name = request.POST.get('message_name')
        message_email = request.POST.get('message_email')
        message_subject = request.POST.get('message_subject')
        message = request.POST.get('umessage')

        # Create and send the email
        email_message = render_to_string('email_template.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message_subject': message_subject,
            'message': message,
        })

        send_mail(
            subject=message_subject,
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,  # Set your default 'from' email in settings.py
            recipient_list=[settings.CONTACT_EMAIL],  # Set the recipient email address in settings.py
            html_message=email_message,
        )

        messages.success(request, 'Your message was sent successfully.')
        return redirect('contact')

    return render(request, 'contact.html')


# pdf
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",
    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
}


# Opens up page as PDF
class ViewPDF(View):
    def get(self, request):
        pdf = render_to_pdf('app/pdf_template.html', data)

        return HttpResponse(pdf, content_type='application/pdf')


# Automatically downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('app/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Invoice_%s.pdf' % ("HolyCross")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def indexp(request):
    context = {}
    return render(request, 'app/index.html', context)
