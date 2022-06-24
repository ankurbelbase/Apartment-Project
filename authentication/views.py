from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from apartment.decorators import check_recaptcha

from django.views.generic import View
from .forms import SignUpForm



# signup views
class UserSignupForm(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    @method_decorator(check_recaptcha)
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid() and request.recaptcha_is_valid:

            user = form.save(commit = False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns these objects if credential are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #after signup redirect to profile settings
                    return redirect('userprofile:profilesettings')
                    
        return render(request, self.template_name, {'form':form})
            

#logout
def logout_view(request):
    logout(request)
    return redirect('authentication:login')