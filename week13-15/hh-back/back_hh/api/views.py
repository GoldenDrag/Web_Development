from django.shortcuts import render, get_object_or_404
from .models import Company, Vacancy
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CompanySerializer, VacancySerializer


@api_view(['GET'])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        list_json = [company.to_json() for company in companies]
        return Response(list_json, safe=False)


class Company(APIView):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return JsonResponse({'error': 'company does not exist'})
        return Response(company.to_json(), safe=False)

    def put(self, request, company_id):
        company = Company.objects.get(id=company_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


def vacancies_list(request, company_id):
    vacancies = Vacancy.objects.filter(company_id=company_id)
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return Response(list_json, safe=False)


def all_vacancies(request):
    vacancies = Vacancy.objects.all()
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return Response(list_json, safe=False)


def vacancy_detail(request, vacancy_id):
    return Response(get_object_or_404(Vacancy, pk=vacancy_id).to_json(), safe=False)


def top(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    list_json = [vacancy.to_json() for vacancy in vacancies]
    return Response(list_json, safe=False)
