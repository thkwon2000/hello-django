from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
def hello_times (request, times) :
    message = "안녕하세요" * times
    return HttpResponse(message)
def naver_realtime_keywords(request):
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')
    text = '<br/>\n'.join([tag.text for tag in tag_list])
    return HttpResponse(text)
def naver_blog_search(request):
    query = request.GET.get('query')  #key가 없으면 none을 반환
    if query :
        text = f'(query) 검색할꺼야.'
    else:
        text = '검색어를 지정해주세요.'
    return HttpResponse(text)
def articles_by_year(request, year):
    return HttpResponse(f'''
        {year}년도에 대한 목록
    ''')