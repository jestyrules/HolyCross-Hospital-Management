from django.urls import path

from Backend import views

urlpatterns = [
    # indexpage
    path("indexpage/", views.indexpage, name="indexpage"),
    path("deleteindex/<int:dataid>/", views.deleteindex, name="deleteindex"),

    # Department
    path("department/", views.department, name="department"),
    path("deptsave/", views.deptsave, name="deptsave"),
    path("displaydept/", views.displaydept, name="displaydept"),
    path("editdept/<int:dataid>/", views.editdept, name="editdept"),
    path("updatedept/<int:dataid>/", views.updatedept, name="updatedept"),
    path("deletedept/<int:dataid>/", views.deletedept, name="deletedept"),

    # Doctor List
    path("doctorlist/", views.doctorlist, name="doctorlist"),
    path("doctorsave/", views.doctorsave, name="doctorsave"),
    path("doctordisplay/", views.doctordisplay, name="doctordisplay"),
    path("doctoredit/<int:dataid>/", views.doctoredit, name="doctoredit"),
    path("doctorup/<int:dataid>/", views.doctorup, name="doctorup"),
    path("doctordel/<int:dataid>/", views.doctordel, name="doctordel"),

    # Login Page
    path("loginpg/", views.loginpg, name="loginpg"),
    path("loginsave/", views.loginsave, name="loginsave"),
    path("logoutpg/", views.logoutpg, name="logoutpg"),

    path("staff_page", views.staff_page, name='staff_page'),
]
