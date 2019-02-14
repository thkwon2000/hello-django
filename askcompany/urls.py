"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
#from blog.views import index, hello_times  (blog 아래로 모두 복사해서 옮김)
#from blog.views import articles_by_year

#from django.urls import register_converter
#from blog.converters import FourDigitYearConverter
#from django.urls.coverters import StringConverter


#register_converter(FourDigitYearConverter, 'year')

urlpatterns = [
 #   path('articles/<year:year>/', articles_by_year),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
  #  path('blog/hello_times/<int:times>/',hello_times),
    # re_path(r'blog/hello_times/(?P<times>\d+)/$',hello_times), 위의것과 동일함(정규표현식임)
  #  path('', index),
    path('shop/', include('shop.urls')),
]
