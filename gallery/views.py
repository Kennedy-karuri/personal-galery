from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def welcome(request):
    return render(request,'all-photos/home.html')




def photos_of_day(request):
    date = dt.date.today()
    gallery = Article.todays_photos()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return render(request, 'all-photos/today-photos.html', {"date": date, "gallery": gallery})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

        gallery = Article.days_photos(date)
    return render(request, 'all-photos/past-photos.html',{"date": date,"photos":photos})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})


def article(request,id):
    try:
        article = Article.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"article.html", {"article":article})