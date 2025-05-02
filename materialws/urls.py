from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("library", views.LibraryListApiView.as_view()),
    path("library/<str:name>/", views.library_detail),
    # path("library/<str:name>/", views.LibraryDetailApiView.as_view()),
    path("modellibrary", views.ModelLibraryListApiView.as_view()),
    path("materiallibrary", views.MaterialLibraryListApiView.as_view()),
]
