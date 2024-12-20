from django.views.generic import CreateView
from .forms import CategoryForm
from .models import Category


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    
    # Custom method to pass additional context (list of categories) to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    # After saving the form, reset the form to a blank one
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object = form.save()  # Save the category
        self.form_class = CategoryForm()  # Reset the form to a blank one after success
        return response

    # Define the success URL (where to redirect after successfully adding a category)
    def get_success_url(self):
        return self.request.path 

