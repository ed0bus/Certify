from django.shortcuts import render, redirect
from .models import Certificate
from django.contrib import messages
from django.views.decorators.cache import cache_page


def index(request):
    certificate = Certificate.objects.all()
    return render(request, "index.html", {"certificates": certificate})


def search_results_view(request):
    if request.method == "GET":
        query = request.GET.get("q")
        if not query:
            messages.error(request, "No query parameter provided.")
            return redirect("home")
        certificate = Certificate.objects.filter(hash__icontains=query).first()
        if certificate:
            return render(request, "verify.html", {"certificate": certificate})
        else:
            messages.success(
                request,
                "The Certificate ID is wrong! Open the database to search for the right one!",
            )
            return redirect("home")
