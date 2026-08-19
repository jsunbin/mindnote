from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    # 변수 object_list에 모든 데이터 가져오기
    object_list = Page.objects.all()
    context = {"page_list": object_list}
    return render(request,'diary/page_list.html', context)




# from .models import Post
# Create your views here.

# def post_list(request):
#     # 변수 posts에 모든 Post를 가져와서 넣어주고
#     posts = Post.objects.all()
#     # context에 사전형으로 담아서 템플릿으로 전달할 수 있도록 함
#     context = {"posts": posts}

#     # request를 받아서, posts의 post_list.html을 렌더
#     return render(request, 'posts/post_list.html', context)