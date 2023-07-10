from django.db import models
# Create your models here.


# many to many relationship
class Promotion(models.Model):
     Description = models.CharField(max_length=255)
     discount = models.FloatField()
     #product_set

class Collection(models.Model):
     title = models.CharField(max_length=255)
     featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+') 
      # jango cannot create the reverse realtionship because we have collection in product
      # + means don't create reverse relation


class Product(models.Model):
     title = models.CharField(max_length=255)
     slug = models.SlugField(default='-')
     description = models.TextField()    # long text
     # 9999.99 consider is the max price value
     unit_price = models.DecimalField(max_digits=6, decimal_places=2)    # float will round the values we should use decimal
     inventory = models.IntegerField()
     last_update = models.DateTimeField(auto_now=True)   # every time we update a product object django will update this field
     collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
     promotions = models.ManyToManyField(Promotion, related_name= "products")  # jango will create products property in promotion class



class Customer(models.Model):
     MEMBERSHIP_BRONZE = 'B'
     MEMBERSHIP_Silver = 'S'  
     MEMBERSHIP_Gold = 'G'

     MEMBERSHIP_CHOICES = [
          (MEMBERSHIP_BRONZE, 'Bronze'),
          (MEMBERSHIP_Silver, 'Silver'),
          (MEMBERSHIP_Gold, 'Gold'),
     ]
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.EmailField(unique=True)
     phone = models.CharField(max_length=255)
     birth_date = models.DateField(null=True)
     membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE, )


class Order(models.Model):
     PAYMENT_STATUS_PENDING = 'P'
     PAYMENT_STATUS_COMPLETE = 'C'
     PAYMENT_STATUS_FAILED = 'F'
     PAYMENT_STATUS_CHOICES = [
          (PAYMENT_STATUS_PENDING, 'Pending'),
          (PAYMENT_STATUS_COMPLETE, 'Complete'),
          (PAYMENT_STATUS_FAILED, 'Failed')
     ]
     placed_at = models.DateTimeField(auto_now_add=True)
     payment_statuses = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
     customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
     order = models.ForeignKey(Order, on_delete=models.PROTECT)
     product = models.ForeignKey(Product, on_delete=models.PROTECT)
     quantity = models.PositiveBigIntegerField()
     unit_price = models.DecimalField(max_digits=6, decimal_places=2 ) 


class Address(models.Model):
     street = models.CharField(max_length=255)
     city = models.CharField(max_length=255)
     # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key= True )
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)



class Cart(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
     Product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField()