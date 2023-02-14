"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import catalog.views
from catalog.views import triangle

urlpatterns = [
    path('', catalog.views.PersonListView.as_view(), name='person'),

    path('admin/', admin.site.urls),

    path('triangle/', triangle, name='triangle'),

    path('person/create/', catalog.views.create_person, name='create_person'),
    path('person/update/<int:pk>/', catalog.views.update_person, name='update_person'),
    path('email/', catalog.views.send_email, name='send_email')
]
