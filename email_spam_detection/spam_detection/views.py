# spam_detection/views.py

from django.shortcuts import render
import random  # For demonstration purposes

def index(request):
    return render(request, 'index.html')

def check_spam(request):
    if request.method == 'POST':
        email = request.POST['email']
        # Dummy spam detection logic (replace with your model logic)
        is_spam = random.choice([True, False])
        return render(request, 'result.html', {'email': email, 'is_spam': is_spam})
    return render(request, 'index.html')
