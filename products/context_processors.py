from .models import Category

def base_dropdown_list(request):

    category = Category.objects.order_by("name")
    return {
        'category': category
    }