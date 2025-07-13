from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def average_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        return round(sum([r.rating for r in reviews]) / reviews.count(), 2)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()

    class Meta:
        unique_together = ('product', 'user')  # prevent duplicates

    def __str__(self):
        return f'{self.product.name} - {self.user.username}'
