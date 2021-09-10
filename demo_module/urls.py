"""demo_module URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from demo_app import urls

urlpatterns = [     # 包含项目中的应用程序的 URL
    url(r'^admin/', admin.site.urls),   # 定义了可在管理网站中请求的所有 URL

    url(r'', include('demo_app.urls')),   # 添加 demo_app 的 URL
    # url(r'', include(urls)),
    # 需要先在 demo_app 中创建另一个 urls.py 文件
]
