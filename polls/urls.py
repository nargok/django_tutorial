from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  # 山括弧を使用すると、URLの一部が「キャプチャ」され、キーワード引数としてビュー関数に送信します。
  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]