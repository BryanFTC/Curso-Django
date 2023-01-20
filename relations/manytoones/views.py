from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.

def create(request):

    rep = Reporter(first_name='Juanjo', last_name='Ruiz', email="juanjo@gamil.com")
    rep.save()

    art1 = Article(headline='lorem ipsum dolot', pub_date=date(2022,5,5), reporter= rep)
    art1.save()
    art2 = Article(headline='lorem ip dolot', pub_date=date(2022,6,5), reporter= rep)
    art2.save()
    art3 = Article(headline='lorem sum dolot', pub_date=date(2022,7,5), reporter= rep)
    art3.save()

    # result = art1.reporter.first_name
    # result = rep.article_set.all()
    result = rep.article_set.count()
    return HttpResponse(result)