from django.urls import path
from . import views
from . views import alltextbooklist,allnovellist,deletenovels,deletetext


urlpatterns = [
    path('alltextbooklist/',alltextbooklist.as_view()),
    path('allnovellist/',allnovellist.as_view()),
    path('deletetext/<int:pk>',deletetext.as_view()),
    path('deletenovels/<int:pk>',deletenovels.as_view())

]
