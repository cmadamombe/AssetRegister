from django.urls import path

from assetregister.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)
#app name called users
app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
