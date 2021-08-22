from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models.aggregates import Count, Min, Max, Avg
from store.models import Product, Customer, OrderItem, Collection, Cart, CartItem
from tags.models import TaggedItem


# returning html templates on user request
def say_hello(request):
    # for all product from Product class
    query_set = Product.objects.all() #This is not actual query_set(set of SQL
                                      # queryies) of obj of product. It will be evaluated(will query to the DB) at for each loop or at the time of
                                      # calling list function.
    for product in query_set:         #query_set is now being evaluated.
        print(product)

    # for one product from Product class
    try:
        product = Product.objects.get(pk=1)  # This will return actual product(not query set) with pk=1 which is id=1
        print(product)
    except ObjectDoesNotExist:
        pass

     # filtering the data
    query_set1 = Product.objects.filter(price__gt=20)  # return query set od products with price > 20

    for product in query_set1:
        print(product.price)

    # filtering customer data with .com email
    customer = Customer.objects.filter(email__icontains='.com')

    # sorting the data
    product = Product.objects.order_by('price')  # it will return query set
    product = Product.objects.order_by('price')[0] # it will return 1st product after making order in ASC order.
    product = Product.objects.earliest('price') # same as above
    product = Product.objects.latest('price') # it will return first product after DESC order

    # query with related field
    product1 = Product.objects.values('title', 'collection__title') # return product title with appropriate collection type : pen--> stationary

    # Item which has been ordered.
    query_set12 = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')

    # Aggregates functions
    result = Product.objects.aggregate(count=Count('id'), min_price=Min('price'))

    content_type = ContentType.objects.get_for_model(Product)
    query_set3 = TaggedItem.objects.select_related('tag').filter(content_type=content_type, object_id=1)

    # Creating an object to DB
    collection = Collection(pk=11)  #This will get an item from Collection table with prim. key = 11
    collection.title = 'Games'
    collection.featured_product = None
    collection.save()  # this will send new object to the database

    #Updating an object to DB
    collection = Collection.objects.get(pk=11)
    collection.title = 'Video Games'
    collection.featured_product = None
    collection.save()

    # Deleting a single object
    collection = Collection(pk=11)
    collection.delete()


    return render(request, 'hello.html', {'result': list()})
