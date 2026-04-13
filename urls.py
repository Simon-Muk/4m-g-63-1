from django.urls import path

from . import views


urlpatterns = [
    path('questionnaires/', views.questionnaire_list),
    path('create/', views.questionnaire_create),
    path('update/<int:id>/', views.questionnaire_update),
    path('delete/<int:id>/', views.questionnaire_delete),
]