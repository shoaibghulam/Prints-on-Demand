from django.db import models

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField(max_length=755)  
    profile = models.ImageField(upload_to='profile_images/', blank=True) 
    house_no = models.CharField(max_length=255, blank=True)  
    street_address = models.CharField(max_length=255, blank=True) 
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True) 
    country = models.CharField(max_length=255, blank=True) 
    zip_code = models.CharField(max_length=20, blank=True) 
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=255, blank=True, null=True) 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SaveToFavoriteModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='images/')

class ProductTypeModel(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=1000)
    gelato_uid = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProductSubCategoryModel(models.Model):
    id=models.AutoField(primary_key=True)
    product_type = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)
    gelato_uid = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class ProductModel(models.Model):
    id=models.AutoField(primary_key=True)
    product_sub_cat = models.ForeignKey(ProductSubCategoryModel, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=1000)
    gelato_uid = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductColorModel(models.Model):
    id=models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  # Assuming you store hex codes like "#RRGGBB"

    def __str__(self):
        return self.label

class ProductSizeModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

class ProductOrientationModel(models.Model):
    id=models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label

class ProductImageModel(models.Model):
    id=models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColorModel, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(ProductSizeModel, on_delete=models.SET_NULL, null=True)
    orientation = models.ForeignKey(ProductOrientationModel, on_delete=models.CASCADE)
    image = models.CharField(max_length=1000)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.orientation.label}"
    

class PromptsModel(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    total_arts = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
class ArtsModel(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)
    prompt = models.ForeignKey(PromptsModel, on_delete=models.PROTECT)
    image = models.TextField()  # URL
    is_favorite = models.BooleanField()
    share = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Art by {self.user.email}"
    


class OrdersModel(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)
    house_no = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    total_amount = models.IntegerField()
    paid = models.IntegerField()
    total_items = models.IntegerField()
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    gelato_order_id = models.IntegerField()
    notes = models.TextField()
    order_placed_at = models.DateTimeField()
    stripe_payment_id = models.IntegerField()
    stripe_customer_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order by {self.user.email}"

class OrderItemsModel(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    order = models.ForeignKey(OrdersModel, on_delete=models.CASCADE)
    art = models.ForeignKey(ArtsModel, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE)
    product_sub_category = models.ForeignKey(ProductSubCategoryModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductSizeModel, on_delete=models.CASCADE)
    product_color = models.ForeignKey(ProductColorModel, on_delete=models.CASCADE)
    product_orientation = models.ForeignKey(ProductOrientationModel, on_delete=models.CASCADE)
    gelato_uid = models.CharField(max_length=255)
    amount = models.IntegerField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order Item for {self.art.user.email}"
