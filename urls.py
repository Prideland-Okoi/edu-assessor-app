from django.urls import path, include
from . import views

# Define the app_name to avoid URL naming conflicts
app_name = 'newtest'

urlpatterns = [
    path('assessments/', views.AssessmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='assessment-list'),
    path('assessments/<int:pk>/', views.AssessmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='assessment-detail'),
    
    path('assessment/', views.AssessmentCreateView.as_view(), name='create-assessment'),
    path('question/', views.QuestionCreateView.as_view(), name='create-question'),
    
    path('questions/', views.QuestionViewSet.as_view({'get': 'list', 'post': 'create'}), name='question-list'),
    path('questions/<int:pk>/', views.QuestionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='question-detail'),
]

# You can include other app-specific URLs here if needed
