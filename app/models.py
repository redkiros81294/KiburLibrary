from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
    
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reservation_id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Reservation {self.reservation_id} by {self.user.username}"
    
class BorrowHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrowing_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"    
    

class Fines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fine_id = models.AutoField(primary_key=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2)
    resource = models.ForeignKey('Book', on_delete=models.CASCADE)  # Assuming fines are related to books.
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Fine {self.fine_id} for {self.user.username}"
    

class PDFandFTP(models.Model):
    resource_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='pdfs/')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

