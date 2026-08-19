from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    # 변수 object_list에 모든 데이터 가져오기
    object_list = Page.objects.all()
    context = {"page_list": object_list}
    return render(request,'diary/page_list.html', context)


def page_detail(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {"page" : page}
    return render(request, 'diary/page_detail.html', context)

