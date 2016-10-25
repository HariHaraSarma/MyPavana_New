"""MyPavana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from MyApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^load/', views.load),
    url(r'^load/', views.LoadView.as_view()),
    #url(r'^load_login/', views.LoadLoginView.as_view()),
    #url(r'^show_stock/', views.show_stock),
    url(r'^show_stock/', views.StockView.as_view()),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^contact/', views.LoadContactView.as_view()),
    url(r'^send_comment/', views.ContactView.as_view()),
    url(r'^logout/', views.LogoutView.as_view()),
    url(r'^show_selected_stock/', views.SelectedStockSearchView.as_view()),
    url(r'^back_to_home/', views.BachtoHomeView.as_view()),
    url(r'^show_dealers/', views.ShowDealerView.as_view()),
]
