from django.shortcuts import render
#汎用的なView用の基底クラス
from django.views import View

class IndexView(View):
    #request:ユーザから送られてきたデータを含むリクエストオブジェクト
    #日記アプリのトップページにアクセスした時に動くメソッド
    def get(self, request):
        #render:画面のレスポンスを返す
        #diary/index.html:返す画面のHTMLファイル
        return render(request, "diary/index.html")

#関数に変換
index = IndexView.as_view()
