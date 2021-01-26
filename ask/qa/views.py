
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from django.http import Http404, HttpResponseRedirect, HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit',10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page,paginator

def get_main(request):
    qa = Question.objects.new_id()
    page,paginator = paginate(request, qa)
    paginator.baseurl = '/?page='
    return render(request,'main.html',{
        'questions': page.object_list, 
        'paginator': paginator, 
        'page':page })

def get_popular(request):
    qa = Question.objects.popular()
    page,paginator = paginate(request, qa)
    paginator.baseurl = '/?page='
    return render(request, 'main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page })

def get_question(request, qn=None):
    question = get_object_or_404(Question, pk=qn)
    answers = Answer.objects.filter(question = question)
    return render(request, 'question.html', {
            'question': question,
            'answers' : answers
    })