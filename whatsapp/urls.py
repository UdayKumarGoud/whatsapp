"""
URL configuration for whatsapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
# from django.conf import settings
from whatsapp import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from users.views import CustomObtainAuthTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('chat/', include('chat.urls')),
    path('users/', include('users.urls')),
    path("accounts/", include("allauth.urls")),
    path("api/", include("whatsapp.api_router")),
    path('group/', include('groupchat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    # path("api/", include("whatsapp.api_router")),
    # DRF auth token
    path("auth-token/", CustomObtainAuthTokenView.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

# if settings.DEBUG:
#     # This allows the error pages to be debugged during development, just visit
#     # these url in browser to see how these error pages look like.
#     urlpatterns += [
#         path(
#             "400/",
#             default_views.bad_request,
#             kwargs={"exception": Exception("Bad Request!")},
#         ),
#         path(
#             "403/",
#             default_views.permission_denied,
#             kwargs={"exception": Exception("Permission Denied")},
#         ),
#         path(
#             "404/",
#             default_views.page_not_found,
#             kwargs={"exception": Exception("Page not Found")},
#         ),
#         path("500/", default_views.server_error),
#     ]
#     if "debug_toolbar" in settings.INSTALLED_APPS:
#         import debug_toolbar

#         urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

