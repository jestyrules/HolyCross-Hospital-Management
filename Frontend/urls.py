from django.urls import path
from Frontend import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('doctors/<drname>/', views.doctors, name='doctors'),
    path('service/', views.service, name='service'),
    path('appoinmentsave/', views.appoinmentsave, name='appoinmentsave'),
    path('loginfr/', views.loginfr, name='loginfr'),
    path('registersave/', views.registersave, name='registersave'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logout/', views.logout, name='logout'),
    path('blogsave/', views.blogsave, name='blogsave'),
    path('profileedit/', views.profileedit, name='profileedit'),
    path('profile/', views.profile, name='profile'),
    path('proedit/<int:dataid>/', views.proedit, name='proedit'),
    path('profilesave/', views.profilesave, name='profilesave'),
    path('profileupdate/<int:dataid>/', views.profileupdate, name='profileupdate'),
    path('singledoctor/<int:proid>/', views.singledoctor, name='singledoctor'),
    path('videocall/', views.videocall, name='videocall'),
    path('appointment/',views.appointment, name='appointment'),
    path('appointmentsave/',views.appointmentsave, name='appointmentsave'),

    path('pdfindex/', views.indexp),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]



