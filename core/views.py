# core/views.py
from django.shortcuts import render
import csv

def list_test_cases(request):
    test_cases = []
    with open('cases/test_cases.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_cases.append(row)
    return render(request, 'core/list_test_cases.html', {'test_cases': test_cases})

def test_case_detail(request, casename):
    test_case = None
    with open('cases/test_cases.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['casename'] == casename:
                test_case = row
                break
    return render(request, 'core/test_case_detail.html', {'test_case': test_case})
