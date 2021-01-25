from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs): #qs - QuerySet
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
    out_page = None
    try:
		out_page = paginator.page(page)
	except EmptyPage: #пустая последняя страница
		out_page = paginator.page(paginator.num_pages) #вернуть последнюю страницу
    return paginator,out_page

def get_main(request):
    questions_new = Question.objects.new_id()
    paginator,page = paginate(request, questions_new)
    paginator.baseurl = '/?page='
    return render(request, 'templates/main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def get_popular(request):
    questions_popular = Question.objects.popular()
    paginator,page = paginate(request, questions_popular)
    paginator.baseurl = '/popular/?page='
    return render(request, 'templates/main.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

@require_GET
def get_question(request, qn=None):
    question = get_object_or_404(Question, id=qn)
    answers = Answer.objects.filter(question__id = qn)[:]
    return render(request, 'templates/question.html', {
            'question': question,
            'answers' : answers
    })