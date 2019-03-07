from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Problems, UserAnswer
from django.db.models.aggregates import Count
import random

# Create your views here.
def wellcome(request):
 return render(request,'wellcome.html')

def problems(request):
  randomProblems = Problems.objects.all().order_by('?').first()
  return render(request,'problems.html',{'randomProblems':randomProblems})

def checkAnswer(request):
  answer = request.GET['answerText']
  if answer != "a1":
    return render(request, 'wellcome.html')
  else:
    return render(request,'answer.html')

def answer(request):
  return render(request,'answer.html')
