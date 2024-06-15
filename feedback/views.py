# feedback/views.py
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['topic', 'message', 'sender']

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})