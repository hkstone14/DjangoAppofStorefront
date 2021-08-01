from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# returning html templates on user request
def say_hello(request):
    # for all product from Product class query_set = Product.objects.all() #This is not actual query_set(set of SQL
    # queryies) of obj of product. It will be evaluated(will query to the DB) at for each loop or at the time of
    # calling list function.
    # for product in query_set:         #query_set is now being evaluated.
    #     print(product)

    # for one product from Product class
    try:
        product = Product.objects.get(pk=1)  # This will return actual product with pk=1 which is id=1
        print(product)
    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html')
