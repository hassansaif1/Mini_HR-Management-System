from django.shortcuts import render, redirect,HttpResponse
from .models import LeaveRequest
from .forms import ApplyLeaveForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
    
# Create your views here.

    
@login_required(login_url='/login')
def admin_dashboard(request):
    if not request.user.is_staff:  # only admin
        return redirect('leave_request')

    leaves = LeaveRequest.objects.all().order_by('-created_at')
    return render(request, "admin.html", {"leaves": leaves})


@login_required(login_url='/login')
def update_status(request, id, status):
    if not request.user.is_staff:
        return redirect('leave_request')

    leave = LeaveRequest.objects.get(id=id)
    leave.status = status
    leave.save()
    return redirect('admin_dashboard')


@login_required(login_url='/login')
def leave_request(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')

    leave_request = LeaveRequest.objects.filter(user=request.user).order_by('-created_at') 
    
    return render(request, 'leave_request.html',{"leave_request" : leave_request})

@login_required(login_url='/login')
def apply_leave(request):
    if request.method == "POST":
        form = ApplyLeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user  # Logged-in user ko assign karenge
            leave.save()
            messages.success(request, "Your form is submitted successfully!")
            # Save hone ke baad employee list page pe redirect karenge
            return redirect('leave_request')
    else:
        form = ApplyLeaveForm()

    # GET request ya invalid form ke liye form render karenge
    return render(request, 'leave_apply.html', {'form': form})
    
