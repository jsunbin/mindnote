from .models import Page
import random

def validate_pages():
    pages = Page.objects.all()
    # 모든 pages 데이터를 돌면서 page의 score가 0 미만 이거나 10을 초과하면, 0부터 10사이의 무작위 정수로 값을 바꾼 후 데이터 베이스에 저장
    for page in pages:
        if page.score < 0 or page.score >10:
            page.score = random.randint(0, 10)
            page.save()