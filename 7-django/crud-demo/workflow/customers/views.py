from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Customer
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from django.views.decorators.http import require_http_methods
from django.db.models import Count, Q

# Create your views here.
def list_customers(request):
    customers = Customer.objects.all().order_by("-id").values(
        "id", "name", "email", "phone", "city", "is_active", "created_at"
    )
    return JsonResponse({"customers": list(customers)})
 
@csrf_exempt
@require_http_methods(["PATCH", "PUT"])
def update_customer(request, cid):
    # if request.method != "POST":
    #     return HttpResponseNotAllowed(["POST"])
 
    try:
        customer = Customer.objects.get(id=cid)
    except Customer.DoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status=404)
    try:
        data=json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({'error':'invalid JSON'},status=400)
    print("update data",data)
 
    # update only provided fields
    # customer.name = request.POST.get("name", customer.name)
    # customer.phone = request.POST.get("phone", customer.phone)
    # customer.phone = request.POST.get("phone", customer.phone)
    # customer.city = request.POST.get("city", customer.city)
   
    if "name" in data:
        customer.name = (data["name"] or "").strip()
    if "phone" in data:
        customer.phone = (data["phone"] or "").strip()
    if "city" in data:
        customer.city = (data["city"] or "").strip()
    if "email" in data:
        customer.email = (data["email"] or "").strip()
    if "is_active" in data:
        # Expecting a boolean in JSON (true/false)
        customer.is_active = bool(data["is_active"])
 
    # optional: toggle active
    # if "is_active" in request.POST:
    #     customer.is_active = request.POST.get("is_active") in ["true", "1", "yes", "on"]
 
    customer.save()
    return JsonResponse({"message": "updated", "id": customer.id})
 
@csrf_exempt
@require_http_methods(["DELETE", "POST"])
def delete_customer(request, cid):
    # if request.method != "POST":
    #     return HttpResponseNotAllowed(["POST"])
 
    deleted_count, _ = Customer.objects.filter(id=cid).delete()
    if deleted_count == 0:
        return JsonResponse({"error": "Customer not found"}, status=404)
 
    return JsonResponse({"message": "deleted", "id": cid})
