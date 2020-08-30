from django.shortcuts import render
from django.http import HttpResponseRedirect

from accounts.models import RegisterForm


# VIEWS REGISTER
def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegisterForm()

    return render(request, 'index.html', {'form': form})
