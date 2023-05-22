from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'aaa/index.html', context)

def detail(request):
    question1 = Question.objects.get(id=1)
    question2 = Question.objects.get(id=2)
    question3 = Question.objects.get(id=3)
    question4 = Question.objects.get(id=4)
    context = {'question1': question1, 'question2': question2, 'question3': question3, 'question4': question4}
    return render(request, 'aaa/detail.html', context)

def results(request, course_point):

    context = {'selected_course': "default"}

    if course_point == 1111 or course_point == 1112 or course_point == 1113:
        context['selected_course'] = "올레 9코스"
    elif course_point in [1121, 1122, 1123]:
        context['selected_course'] = "올레 6코스"
    elif course_point in [1211, 1212]:
        context['selected_course'] = "올레 2, 13, 7-1코스"
    elif course_point == 1213:
        context['selected_course'] = "올레 15-B코스"
    elif course_point in [1221, 1222, 1223]:
        context['selected_course'] = "올레 3-B코스"
    elif course_point in [1311, 1312, 1313]:
        context['selected_course'] = "올레 16코스"
    elif course_point in [1321, 1322, 1323]:
        context['selected_course'] = "올레 8, 10코스"
    elif course_point in [1411, 1412, 1413]:
        context['selected_course'] = "올레 3-A코스"
    elif course_point in [1421, 1422, 1423]:
        context['selected_course'] = "올레 18, 19코스"
    elif course_point in [2111, 2112, 2113]:
        context['selected_course'] = "올레 14-1코스"
    elif course_point in [2121, 2122, 2123]:
        context['selected_course'] = "올레 21코스"
    elif course_point in [2211, 2212, 2213]:
        context['selected_course'] = "올레 13코스"
    elif course_point in [2221, 2222, 2223]:
        context['selected_course'] = "올레 1, 1-1, 5코스"
    elif course_point in [2311, 2312, 2313]:
        context['selected_course'] = "올레 11코스"
    elif course_point in [2321, 2322, 2323]:
        context['selected_course'] = "올레 7, 12, 15-A, 20코스"
    elif course_point == 2411:
        context['selected_course'] = "올레 3-A코스"
    elif course_point in [2412, 2413]:
        context['selected_course'] = "올레 14코스"
    elif course_point in [2421, 2422, 2423]:
        context['selected_course'] = "올레 18코스"

    return render(request, 'aaa/result.html', context)

def vote(request):
    question1 = get_object_or_404(Question, pk=1)
    question2 = get_object_or_404(Question, pk=2)
    question3 = get_object_or_404(Question, pk=3)
    question4 = get_object_or_404(Question, pk=4)

    try:
        selected_choice_12 = question1.choice_set.get(pk=request.POST['question1_choice'])
        selected_choice_3456 = question2.choice_set.get(pk=request.POST['question2_choice'])
        selected_choice_78 = question3.choice_set.get(pk=request.POST['question3_choice'])
        selected_choice_91011 = question4.choice_set.get(pk=request.POST['question4_choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'aaa/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:

        course_point = 0

        if selected_choice_12 == Question.objects.get(id=1).choice_set.get(id=1):
            course_point = course_point + 1000
        # 봄 여름
        elif selected_choice_12 == Question.objects.get(id=1).choice_set.get(id=2):
            course_point = course_point + 2000
        # 가을 겨울
        else:
            return

        if selected_choice_3456 == Question.objects.get(id=2).choice_set.get(id=3):
            course_point = course_point + 100
        # 3~4
        elif selected_choice_3456 == Question.objects.get(id=2).choice_set.get(id=4):
            course_point = course_point + 200
        # 4~5
        elif selected_choice_3456 == Question.objects.get(id=2).choice_set.get(id=21):
            course_point = course_point + 300
        # 5~6
        elif selected_choice_3456 == Question.objects.get(id=2).choice_set.get(id=22):
            course_point = course_point + 400
        # 6~7
        else:
            return

        if selected_choice_78 == Question.objects.get(id=3).choice_set.get(id=23):
            course_point = course_point + 10
        # 숲
        elif selected_choice_78 == Question.objects.get(id=3).choice_set.get(id=24):
            course_point = course_point + 20
        # 바다
        else:
            return

        if selected_choice_91011 == Question.objects.get(id=4).choice_set.get(id=25):
            course_point = course_point + 1
        # 상
        elif selected_choice_91011 == Question.objects.get(id=4).choice_set.get(id=26):
            course_point = course_point + 2
        # 중
        elif selected_choice_91011 == Question.objects.get(id=4).choice_set.get(id=27):
            course_point = course_point + 3
        # 하
        else:
            return

        selected_choice_12.votes += 1
        selected_choice_3456.votes += 1
        selected_choice_78.votes += 1
        selected_choice_91011.votes += 1
        selected_choice_12.save()
        selected_choice_3456.save()
        selected_choice_78.save()
        selected_choice_91011.save()

        return HttpResponseRedirect(reverse('aaa:results', args=(int(course_point),)))
