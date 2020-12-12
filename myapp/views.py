from datetime import datetime

from django.utils import timezone

from django.urls import reverse
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SearchForm, ReviewForm
from .forms import OrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.


def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'top_list': top_list, 'last_login': request.session.get('last_login', False)})
    # response = HttpResponse()
    # heading1 = '<p>' + 'List of topics: ' + '</p>'
    # response.write(heading1)
    # for topic in top_list:
    #    para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
    #    response.write(para)


#
#   cor_list = Course.objects.all().order_by('-title')[:5]
#   heading2 = '<br><p>' + 'List of Courses: ' + '</p>'
#   response.write(heading2)
#   for course in cor_list:
#       para1 = '<p>' + str(course.title) + ': $' + str(course.price) + '</p>'
#       response.write(para1)
#   return response

def about(request):
    about_visits = request.COOKIES.get('about_visits')
    if about_visits:
        about_visits = int(about_visits) + 1
    else:
        about_visits = 1
    response = render(request, 'myapp/about.html', {'about_visits': about_visits})
    response.set_cookie('about_visits', about_visits, expires=300)
    return response
    # response = HttpResponse()
    # head1 = '<p><b>' + 'This is an E-learning Website! Search our Topics to find all available Courses.' + '</b></p>'
    # response.write(head1)
    # return response


def detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    course_list = Course.objects.filter(topic=topic)
    return render(request, 'myapp/detail.html', {'course_list': course_list, 'topic': topic})
    # response = HttpResponse()
    # para = '<p><b>' + str(topic.name).upper() + '<br>' + 'Length: ' + str(topic.length) + '</b></p>'
    # response.write(para)

    # heading1 = '<p>' + 'List of available courses:' + '</p>'
    # response.write(heading1)
    # for course in course_list:
    #    para1 = '<p>' + str(course.title) + '</p>'
    #    response.write(para1)
    # return response


def findcourses(request):
    # breakpoint()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Student_Name']
            length = form.cleaned_data['Preferred_course_duration']
            max_price = form.cleaned_data['Maximum_price']
            if length:
                topics = Topic.objects.filter(length=length)
            else:
                topics = Topic.objects.all()
            courselist = []
            for top in topics:
                courselist = courselist + list(top.courses.filter(price__lt=max_price))
            return render(request, 'myapp/results.html', {'courselist': courselist, 'name': name, 'length': length})
        else:
            return HttpResponse('Invalid data')
    else:
        form = SearchForm()
        return render(request, 'myapp/findcourses.html', {'form': form})


def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            courses = form.cleaned_data['courses']
            order = form.save()
            student = order.student
            status = order.order_status
            order.save()
            if status == 1:
                for c in courses:
                    student.registered_courses.add(c)
                    # order.courses.add(c)
            return render(request, 'myapp/order_response.html', {'courses': courses, 'order': order})
        else:
            return render(request, 'myapp/place_order.html', {'form': form})

    else:
        form = OrderForm()
        return render(request, 'myapp/place_order.html', {'form': form})


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            if 1 <= rating <= 5:
                review = form.save()
                course = review.course
                course.num_reviews += 1
                course.save()
                # return index(request)
                return redirect('myapp:index')
            else:
                return render(request, 'myapp/review.html',
                              {'form': form, 'messege': 'You must enter a rating between 1 and 5!'})
        else:
            return HttpResponse('Invalid data')
    else:
        form = ReviewForm()
        return render(request, 'myapp/review.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['last_login'] = str(datetime.now().isoformat(',', 'seconds'))
                request.session.set_expiry(3600)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:index'))


def my_account(request):
    if request.user.is_authenticated:
        sid = request.user.id
        try:
            if Student.objects.get(pk=sid):
                user = get_object_or_404(Student, pk=sid)
                tops = Student.objects.filter(id=sid).values_list("interested_in__name", flat=True)
                cors = Student.objects.filter(id=sid).values_list('registered_courses__title', flat=True)
                return render(request, 'myapp/myaccount.html', {'user': user, 'tops': tops, 'cors': cors})
        except:
            return render(request, 'myapp/myaccount.html', {'message': 'You are not a registered student! Please Login as Student!!'})
    else:
        return render(request, 'myapp/myaccount.html', {'message': 'Please Login First!'})
