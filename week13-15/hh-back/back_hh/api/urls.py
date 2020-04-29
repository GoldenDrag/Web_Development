from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.companies_list, name='companies'),
    path('companies/<int:company_id>/', views.company_detail, name='company'),
    path('companies/<int:company_id>/vacancies/', views.vacancies_list, name='vacancies'),
    path('vacancies/', views.all_vacancies, name='all vacancies'),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail, name='vacancy'),
    path('vacancies/top_ten/', views.top, name='top ten')
]