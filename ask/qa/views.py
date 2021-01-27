
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from qa.forms import AskForm,AnswerForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

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
    if (request.method == "POST"): #post answer
        form = AnswerForm(request.POST)
        form._user = User.objects.get(id=1)
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect(q.get_url())
    else: #get question
        question = get_object_or_404(Question, pk=qn)
        answers = Answer.objects.filter(question = question)
        form = AnswerForm()
    return render(request, 'question.html', {
            'question': question,
            'answers' : answers,
            'form' : form
    })

def post_question(request): #post question
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = User.objects.get(id=1)
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect(q.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form} )
