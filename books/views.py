from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm, ReviewForm
from books.models import Book, BookBorrow
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.utils.timezone import now


class AddBookCreateView(LoginRequiredMixin ,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class DetailBookView(DetailView):
    model = Book
    template_name = 'book_details.html'
    context_object_name = 'book'

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book
            new_review.name = request.user.get_full_name()
            new_review.email = request.user.email
            new_review.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        context['review_form'] = ReviewForm()
        return context



# borrow book
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.user.account.balance >= book.borrow_price:
        request.user.account.balance -= book.borrow_price
        request.user.account.save()

        BookBorrow.objects.create(book=book, user=request.user, borrow_date=now())

        book.borrowed_by.add(request.user)
        book.save()
        
        messages.success(request, f"Book borrowed successfully !")
    else:
        messages.error(request, "Sorry, you don't have sufficient balance to borrow this book.")
    
    return redirect('profile')



def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.user in book.borrowed_by.all():
        request.user.account.balance += book.borrow_price
        request.user.account.save()

        book.borrowed_by.remove(request.user)
        book.save()

        messages.success(request, f"Book returned successfully!")
    else:
        messages.error(request, "You have not borrowed this book.")
    
    return redirect('profile')

