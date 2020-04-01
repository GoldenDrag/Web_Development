from django.shortcuts import render, get_object_or_404
from .models import Company, Vacancy
from django.http.response import JsonResponse


def companies_list(request):
    companies = Company.objects.all()
    list_json = [company.to_json() for company in companies]
    return JsonResponse(list_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'company does not exist'})
    return JsonResponse(company.to_json(), safe=False)


def vacancies_list(request, company_id):
    vacancies = Vacancy.objects.filter(company_id=company_id)
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(list_json, safe=False)


def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(list_json, safe=False)


def vacancy_detail(request, vacancy_id):
    return JsonResponse(get_object_or_404(Vacancy, pk=vacancy_id).to_json(), safe=False)


def top(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(list_json, safe=False)
