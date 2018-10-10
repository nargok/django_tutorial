from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # contextはテンプレート変数名を Python オブジェクトにマッピングする辞書です。
  context = {
    'latest_question_list': latest_question_list
  }
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})


  # return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
  response = "You are looking at the resulsts of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You are voting on question %s." % question_id)
