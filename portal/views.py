from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import ComplaintForm, RegisterForm
from .models import Complaint

def home(request):
    qs = Complaint.objects.all()
    stats = {
        "total": qs.count(),
        "progress": qs.filter(status="In Progress").count(),
        "resolved": qs.filter(status="Resolved").count(),
        "pending": qs.filter(status="Pending").count(),
    }
    recent = qs.order_by("-created_at")[:5]
    return render(request, "portal/home.html", {"stats": stats, "recent": recent})

def about(request):
    return render(request, "portal/about.html")

def report_issue(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            if request.user.is_authenticated:
                complaint.user = request.user
            complaint.save()
            return render(request, "portal/submitted.html", {"complaint": complaint})
    else:
        initial = {}
        if request.user.is_authenticated:
            initial = {"name": request.user.get_full_name() or request.user.username, "email": request.user.email}
        form = ComplaintForm(initial=initial)
    return render(request, "portal/report.html", {"form": form})

def track_complaint(request):
    complaint = None
    searched = False
    if request.method == "POST":
        searched = True
        ticket = request.POST.get("ticket_id", "").strip().upper()
        email = request.POST.get("email", "").strip()
        complaint = Complaint.objects.filter(ticket_id=ticket, email__iexact=email).first()
        if not complaint:
            messages.error(request, "We couldn't find a complaint with those details. Check the ticket ID and email.")
    return render(request, "portal/track.html", {"complaint": complaint, "searched": searched})

def awareness(request):
    return render(request, "portal/awareness.html")

def reports(request):
    categories = Complaint.objects.values("category").annotate(total=Count("id")).order_by("-total")
    return render(request, "portal/reports.html", {"categories": categories})

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account has been created.")
        return redirect("home")
    return render(request, "portal/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    error = None
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.POST.get("next") or request.GET.get("next")
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect("home")
        error = "Invalid username or password."
    return render(request, "portal/login.html", {"error": error})

def logout_view(request):
    logout(request)
    return redirect("home")
