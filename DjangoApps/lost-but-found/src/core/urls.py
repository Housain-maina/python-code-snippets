from django.contrib import admin
from django.urls import path, include


admin.site.site_title = "LOST BUT FOUND"
admin.site.index_title = "LOST BUT FOUND ADMIN"
admin.site.site_header = "LOST BUT FOUND ADMIN"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("profiles/", include("profiles.urls")),
]
