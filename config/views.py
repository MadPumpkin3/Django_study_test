from django.http import HttpResponse
from django.shortcuts import render

# render함수의 Template의 경로는 config/settings 에서 직접 지정한 TEMPLATES/DIRS에 추가한 디렉터리 경로를 기준으로 한다.
def main(request):
    # render 함수에서 첫 번째 인수는 request객체, 두 번째 인수는 Templated의 경로를 지정
    return render(request, "main.html")

def berger_list(request):
    return render(request, "burger_list")