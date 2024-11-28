from django.urls import path
from .views import QuestionDetailView, AnswerCreateView
from django.views.generic.base import TemplateView

urlpatterns = [
    path("question/<str:slug>/", QuestionDetailView.as_view(), name="question"),
    path("question/<str:slug>/answer/", AnswerCreateView.as_view(), name="answer_create"),
    path("success/", TemplateView.as_view(template_name="success.html"), name="success_page"),

]