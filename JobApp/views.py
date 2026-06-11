from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def registerPage(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserRegisterForm()
    context = {
        'form':form,
        'title':'Register Form',
        'btn':'Register'
    }
    return render(req,'base/baseAuthForm.html',context)

def loginPage(req):
    if req.method == 'POST':
        form = UserLoginForm(req,req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            return redirect('dashboard')

    form = UserLoginForm()
    context = {
        'form':form,
        'title':'Login Form',
        'btn':'Login'
    }
    return render(req,'base/baseAuthForm.html',context)

def logoutPage(req):
    logout(req)
    return redirect('login')
@login_required
def dashboardPage(req):
    data = JobModel.objects.all()
    context = {
        'data':data
    }

    return render(req,'pages/dashboard.html',context)
@login_required
def recruiterPage(req):
    try:
        user = RecruiterModel.objects.get(user=req.user)
    except RecruiterModel.DoesNotExist:
        user = RecruiterModel.objects.create(user=req.user)

    if req.method == 'POST':
        form = RecruiterForm(req.POST,req.FILES,instance=user)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = req.user
            data.save()
            return redirect('dashboard')

    form = RecruiterForm(instance=user)
    context = {
        'form':form,
        'title':'Recruiter Form',
        'btn':'Update'
    }

    return render(req,'base/baseForm.html',context)
@login_required
def jobSeekerPage(req):
    try:
        user = JobSeekerModel.objects.get(user=req.user)
    except JobSeekerModel.DoesNotExist:
        user = JobSeekerModel.objects.create(user=req.user)

    if req.method == 'POST':
        form = JobSeekerForm(req.POST,req.FILES,instance=user)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = req.user
            data.save()
            return redirect('dashboard')

    form = JobSeekerForm(instance=user)
    context = {
        'form':form,
        'title':'Job Seeker Form',
        'btn':'Update'
    }

    return render(req,'base/baseForm.html',context)

@login_required
def jobPostPage(req):
    try:
        user = RecruiterModel.objects.get(user=req.user)
    except RecruiterModel.DoesNotExist:
        return redirect('recruiter')
    if req.user.user_type == 'Recruiter':
        if req.method == 'POST':
            form = JobForm(req.POST,req.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user =user
                data.save()
                return redirect('dashboard')


    form = JobForm()
    context = {
        'form':form,
        'title':'Post A Job',
        'btn':'Post'
    }

    return render(req,'base/baseForm.html',context)
@login_required
def jobEditPostPage(req,id):
    try:
        user = RecruiterModel.objects.get(user=req.user)
    except RecruiterModel.DoesNotExist:
        return redirect('recruiter')
    if req.user.user_type == 'Recruiter':
        user_id = JobModel.objects.get(id=id)
        if req.method == 'POST':
            form = JobForm(req.POST,req.FILES, instance=user_id)
            if form.is_valid():
                data = form.save(commit=False)
                data.user =user
                data.save()
                return redirect('dashboard')


    form = JobForm(instance=user_id)
    context = {
        'form':form,
        'title':'Edit Job Post ',
        'btn':'Edit'
    }

    return render(req,'base/baseForm.html',context)
@login_required
def jobDeletePostPage(req,id):
    if req.user.user_type == 'Recruiter':
        JobModel.objects.get(id=id).delete()
        
        return redirect('dashboard')

def skillPage(req):
    if req.method == 'POST':
        form = SkillForm(req.POST)
        if form.is_valid():
            form.save()
            # return redirect('skill')
    data = SkillModel.objects.all()
    form = SkillForm()
    context = {
        'data':data,
        'form':form,
        'title':'Add Skill',
        'btn':'Add'
    }
    return render(req,'base/baseForm.html',context)

@login_required
def applyJobPage(req,id):
    try:
        user = JobSeekerModel.objects.get(user=req.user)
    except JobSeekerModel.DoesNotExist:
        return redirect('jobSeeker')
    job = JobModel.objects.get(id=id)
    if req.user.user_type == 'JobSeeker':
        ApplyJobModel.objects.create(
            job_seeker=user,
            job=job,
            status='Pending'
        )
        messages.success(req,'Applied Successfully')
        return redirect('dashboard')
    
@login_required
def myApplyPage(req):
    try:
        user = JobSeekerModel.objects.get(user=req.user)
    except JobSeekerModel.DoesNotExist:
        return redirect('jobSeeker')
    data = ApplyJobModel.objects.filter(job_seeker=user)
    context = {
        'data':data
    }
    return render(req,'pages/myApply.html',context)


@login_required
def applicantPage(req, id=None): 
    id = JobModel.objects.filter(id=id)

    if id:
        applicants = ApplyJobModel.objects.filter(job=id)
    else:
       
        applicants = ApplyJobModel.objects.all()
        
    return render(req, 'pages/applicant.html', {'applicants': applicants})
@login_required
def shortListPage(req,id):
    apply_job = ApplyJobModel.objects.get(id=id)
    apply_job.status = 'ShortList'
    apply_job.save()
    messages.success(req,'ShortListed Successfully')
    return redirect('applicant')
@login_required
def rejectPage(req,id):
    apply_job = ApplyJobModel.objects.get(id=id)
    apply_job.status = 'Rejected'
    apply_job.save()
    messages.success(req,'Rejected Successfully')
    return redirect('applicant')