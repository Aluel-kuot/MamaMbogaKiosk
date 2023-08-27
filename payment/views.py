from django.shortcuts import render , redirect
from .forms import PaymentUploadForm
from .models import Payment

def payment_create_view(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PaymentUploadForm()

    return render(request, 'payment_form.html', {'form': form})




