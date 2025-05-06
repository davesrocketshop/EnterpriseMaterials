from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("library", views.LibraryListApiView.as_view()),
    # path("library/<str:name>/", views.library_detail),
    path("library/<str:name>/", views.LibraryDetailApiView.as_view()),
    path("modellibrary", views.ModelLibraryListApiView.as_view()),
    path("materiallibrary", views.MaterialLibraryListApiView.as_view()),
    path("libraryModels/<str:name>/", views.LibraryModelsListApiView.as_view()),
    path("libraryMaterials/<str:name>/", views.LibraryMaterialsListApiView.as_view()),
    path("model", views.ModelApiView.as_view()),
    path("model/<uuid:uuid>/", views.ModelDetailApiView.as_view()),
    path("modelProperty/<uuid:uuid>/", views.ModelPropertyApiView.as_view()),
]
