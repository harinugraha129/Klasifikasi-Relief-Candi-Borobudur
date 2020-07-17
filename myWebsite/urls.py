"""myWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
admin.autodiscover()
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from Data_Train import views as dt_views
from Testing import views as test_views
from Testing import api_ as test_api


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('data_train/', dt_views.index, name="data_train"),

    path('testing/', test_views.index, name="testing"),
    path('testing/upload/', test_views.upload, name="testing_upload"),
    path('testing/delete/<int:id>', test_views.delete, name="testing_delete"),
    path('api/testing/', test_api.testing, name="api_testing"),
    path ('testing/api/', test_api.test_api ),
    path ('testing/api_lantai/', test_api.test_lantai ),
    path ('test_post/api/', test_api.test_post ),


    #REST_FRAMEWORK URLS
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)