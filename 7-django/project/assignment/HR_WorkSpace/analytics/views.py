# analytics/views.py
from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render




from django.views.generic import TemplateView


def home(request):
    return render(request, 'analytics/home.html')




def _run_query(sql, params=None):
    with connection.cursor() as cursor:
        cursor.execute(sql, params or [])
        cols = [c[0] for c in cursor.description]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]

def attrition_view(request):
    sql = """
    SELECT
        d.name AS department,
        COUNT(e.id) AS total_employees,
        SUM(CASE WHEN e.exit_date IS NOT NULL THEN 1 ELSE 0 END) AS attrition_count,
        ROUND(
            (SUM(CASE WHEN e.exit_date IS NOT NULL THEN 1 ELSE 0 END) /
            COUNT(e.id)) * 100, 2
        ) AS attrition_rate
    FROM employee e
    JOIN department d ON e.department_id = d.id
    GROUP BY d.name;
    """
    return JsonResponse(_run_query(sql), safe=False)

def tenure_view(request):
    sql = """
    SELECT
        d.name AS department,
        CASE
            WHEN TIMESTAMPDIFF(YEAR, e.hire_date, CURDATE()) < 1 THEN '<1 year'
            WHEN TIMESTAMPDIFF(YEAR, e.hire_date, CURDATE()) BETWEEN 1 AND 3 THEN '1-3 years'
            WHEN TIMESTAMPDIFF(YEAR, e.hire_date, CURDATE()) BETWEEN 3 AND 5 THEN '3-5 years'
            ELSE '>5 years'
        END AS tenure_bucket,
        COUNT(*) AS count
    FROM employee e
    JOIN department d ON d.id = e.department_id
    GROUP BY d.name, tenure_bucket
    ORDER BY d.name, 
             CASE tenure_bucket 
               WHEN '<1 year' THEN 1 
               WHEN '1-3 years' THEN 2 
               WHEN '3-5 years' THEN 3 
               ELSE 4 
             END;
    """
    return JsonResponse(_run_query(sql), safe=False)

def performance_view(request):
    sql = """
    SELECT
        d.name AS department,
        CASE 
            WHEN p.rating >= 4 THEN 'High'
            WHEN p.rating = 3 THEN 'Medium'
            ELSE 'Low'
        END AS segment,
        COUNT(*) AS count
    FROM performance p
    JOIN employee e ON p.employee_id = e.id
    JOIN department d ON e.department_id = d.id
    GROUP BY d.name, segment
    ORDER BY d.name,
             FIELD(segment, 'High', 'Medium', 'Low');
    """
    return JsonResponse(_run_query(sql), safe=False)