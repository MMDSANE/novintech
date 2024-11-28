from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, FormView
from django.urls import reverse_lazy
from .models import Question, Answer


class QuestionDetailView(DetailView):
    """
    Handles displaying a specific question.
    """
    model = Question
    template_name = "question.html"
    context_object_name = "question"
    slug_field = "slug"
    slug_url_kwarg = "slug"



class AnswerCreateView(FormView):
    template_name = "question.html"

    def post(self, request, slug, *args, **kwargs):
        question = get_object_or_404(Question, slug=slug)

        # Extract form data
        name = request.POST.get('name', '').strip()
        lastname = request.POST.get('lastname', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        answer = request.POST.get('answer', '').strip()
        file = request.FILES.get('file')

        # Validate required fields
        if not all([name, lastname, phone, email, answer, file]):
            return render(request, self.template_name, {
                'question': question,
                'error': 'All fields are required.',
                'form_data': request.POST,  # To pre-fill the form with entered data
            })

        # Create the answer object
        Answer.objects.create(
            question=question,
            name=name,
            lastname=lastname,
            phone=phone,
            email=email,
            answer=answer,
            file=file,
        )

        # Redirect to the success page
        return redirect("success_page")
