from django.urls import re_path
from mods import views

urlpatterns = [
    re_path(r'^mod-categories/$',
        views.ModCategoryList.as_view(),
        name=views.ModCategoryList.name),
    re_path(r'^mod-categories/(?P<pk>[0-9]+)$',
        views.ModCategoryDetail.as_view(),
        name=views.ModCategoryDetail.name),
    re_path(r'^mod/$',
        views.ModList.as_view(),
        name=views.ModList.name),
    re_path(r'^mod/(?P<pk>[0-9]+)$',
        views.ModDetail.as_view(),
        name=views.ModDetail.name),
    re_path(r'^user/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    re_path(r'^user/(?P<pk>[0-9]+)$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
    re_path(r'^$',
        views.ApiRoot.as_view(),        
        name=views.ApiRoot.name),
]