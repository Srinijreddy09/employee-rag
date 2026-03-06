from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmployeeDetails, EmployeeWork
from .serializers import EmployeeDetailsSerializer
from .services import build_prompt, generate_summary


@api_view(['GET'])
def employee_query(request):

    query = request.GET.get('query')

    if not query:
        return Response({"error": "Query parameter is required"}, status=400)

    employee = None

    # Search by employee ID
    if query.isdigit():
        try:
            employee = EmployeeDetails.objects.get(employee_id=query)
        except EmployeeDetails.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)

    # Search by employee name
    else:
        employees = EmployeeDetails.objects.filter(
            employee_first_name__icontains=query
        )

        if employees.count() == 0:
            return Response({"error": "Employee not found"}, status=404)

        elif employees.count() > 1:
            return Response(
                {"error": "Multiple employees found. Please refine your query"},
                status=400
            )

        employee = employees.first()

    # Fetch work details
    try:
        work = EmployeeWork.objects.get(employee=employee)
    except EmployeeWork.DoesNotExist:
        return Response({"error": "Employee work details not found"}, status=404)

    # Build prompt and summary
    prompt = build_prompt(employee, work)
    summary = generate_summary(prompt)

    serializer = EmployeeDetailsSerializer(employee)

    return Response({
        "summary": summary,
        "employee": serializer.data
    })