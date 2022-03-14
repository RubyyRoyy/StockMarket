from django.db import models


class StockMarket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=10)
    current_price = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return self.name


class StockQuery(models.Model):
    query = models.TextField()
    username = models.CharField(max_length=100)
    stock_id = models.IntegerField()


