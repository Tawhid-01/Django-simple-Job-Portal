from django.urls import path
from .views import *

urlpatterns = [
  path('',loginPage,name='login'),
  path('register/',registerPage,name='register'),
  path('logout/',logoutPage,name='logout'),

  path('recruiter/',recruiterPage,name='recruiter'),
  path('jobSeeker/',jobSeekerPage,name='jobSeeker'),

  path('dashboard/',dashboardPage,name='dashboard'),
  path('jobPost/',jobPostPage,name='jobPost'),
  path('skill/',skillPage,name='skill'),

  path('applyJob/<int:id>',applyJobPage,name='applyJob'),
  path('myApply/',myApplyPage,name='myApply'),
  
  path('applicant/',applicantPage,name='applicant'),
  path('applicant/<int:id>/', applicantPage,name='applicant_detail'),

  path('shortList/<int:id>',shortListPage,name='shortList'),
  path('reject/<int:id>',rejectPage,name='reject'),
  
  path('edit/<int:id>',jobEditPostPage,name='editJob'),
  path('delete/<int:id>',jobDeletePostPage,name='deleteJob'),
]