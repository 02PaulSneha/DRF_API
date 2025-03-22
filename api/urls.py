from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename= 'employee') # "basename" this use only for "viewsets.ViewSets"..For the "model viewset" don't have to use anything like this



urlpatterns = [
     
     path('students/' , views.studentsView),
     path('students/<int:pk>/',views.studentDetailViews),
     
     
     #path('employees/', views.Employees.as_view()), # always using ".as_view" while using class based view
     #path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
     
     
     path('', include(router.urls)),
     
     path('blogs/',views.BlogsView.as_view()),
     path('comments/',views.CommentsView.as_view()),
     
     path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
     path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]

