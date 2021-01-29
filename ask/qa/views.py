
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from qa.forms import AskForm,AnswerForm,UserForm,LoginForm
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
    if (request.method == "POST"): #post answer
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = form.save()
            return HttpResponseRedirect(a.question.get_url())
    else: #get question
        form = AnswerForm()
    return render(request, 'question.html', {
            'question': question,
            'answers' : Answer.objects.filter(question = question),
            'form' : form
    })

def post_question(request): #post question
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect(q.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form} )

#aka register
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form} )

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form} )
