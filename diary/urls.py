from django.urls import path

from . import views

app_name = "diary"
#どのリクエストに対してどの関数が動くか定義
urlpatterns = [
    # 第一引数:どのようなパスか　第二引数:動かす関数　第三引数:名前
    #日記アプリのトップページ
    path("", views.index, name = "index"),
]
