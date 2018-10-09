from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # 山括弧を使用すると、URLの一部が「キャプチャ」され、キーワード引数としてビュー関数に送信します。
  path('<int:question_id>/', views.detail, name='detail'),
  path('<int:question_id>/results/', views.results, name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]