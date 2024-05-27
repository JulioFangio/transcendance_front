"""transtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from .views import homepage
from .views import userpage
from .views import log_in
from .views import sign_up_page
from .views import sign_up_form_page

urlpatterns = [
    path('', homepage, name="homepage"),
    path("user/", userpage, name="userpage"),
    path("log_in/", log_in, name="log_in"),
    path("sign_up/", sign_up_page, name="sign_up_page"),
    path("sign_up_form/", sign_up_form_page, name="sign_up_form_page"),
    path('admin/', admin.site.urls),
]
