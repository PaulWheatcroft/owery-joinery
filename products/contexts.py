from products.models import Category


def list_of_categories(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return context
