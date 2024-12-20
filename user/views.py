from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView

from books.models import Book, BookBorrow
from user.models import UserAccount
from .forms import DepositForm, SignupForm


# signup
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Account created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


# login
class UserLoginView(LoginView):
    template_name = 'signin.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)
    


# logout
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('signin')


# profile
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        borrowed_books = Book.objects.filter(borrowed_by=self.request.user)
        borrowed_books_with_dates = []

        for book in borrowed_books:
            borrow_record = BookBorrow.objects.filter(book=book, user=self.request.user).first()
            borrowed_books_with_dates.append({
                'book': book,
                'borrow_date': borrow_record.borrow_date if borrow_record else None
            })

        context['borrowed_books'] = borrowed_books_with_dates
        return context


# deposit money
class DepositMoneyView(FormView):
    template_name = 'deposit_money.html'
    form_class = DepositForm  
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_account = UserAccount.objects.get(user=self.request.user) 
        kwargs['account'] = user_account 
        return kwargs

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount') 
        account = self.request.user.account  
        account.balance += amount 
        account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'${"{:,.2f}".format(float(amount))} was deposited to your account successfully.'
        )

        return super().form_valid(form)
