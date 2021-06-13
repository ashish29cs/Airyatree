from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="index"),
    path("webpage/home",views.home,name="index"),
    path("webpage/home1",views.home1,name="home"),
    path("home1",views.home1,name="home"),
    path("home",views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("method",views.method,name="method"),
    path("eda",views.eda,name="eda"),
    path("intro",views.intro,name="intro"),
    path("result",views.result,name="result"),
    path("contact",views.contact,name="contact"),
    path("predict",views.predict,name="predict"),
    path("afterlogin",views.afterlogin,name="home2"),
    path("logout",views.home,name="logout"),
    path("data",views.data,name="data")
    
]