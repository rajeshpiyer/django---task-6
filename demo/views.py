from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import View
from .models import Patient
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('items')
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Logged in successfully.')
            successful_logins = int(self.request.COOKIES.get('successful_logins', 0))
            successful_logins += 1
            response = super().form_valid(form)
            response.set_cookie('successful_logins', successful_logins)
            return response
        else:
            messages.error(self.request, 'Invalid username or password.')
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        # Increment failed login attempts in session
        self.request.session['failed_attempts'] = self.request.session.get('failed_attempts', 0) + 1
        return super().form_invalid(form)


class CustomLogoutView(View):
    next_page = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect(self.next_page)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

@login_required
def list_items(request):
    items = Patient.objects.all()
    failed_attempts = request.session.get('failed_attempts', 0)
    successful_logins = request.COOKIES.get('successful_logins', 0)
    return render(request, 'items.html', {'items': items,'success':successful_logins,'fail':failed_attempts})
