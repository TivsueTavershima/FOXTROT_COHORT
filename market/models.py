


from django.db import models




        # Create your models here.
        # A model is a python class that represent a table a table in a database
        # A database is an collectin of data, typically electronic that is stored and managed for efficient retriever
        #        2 TYPES OF DATABASE
        # 1     Relational database == store things in a tabler format, example,MySql,Superbase,PostgreSQL,MonoDB
        # 2     Non-relational database == store things in a non Document format, example, MongoDB,Cassandra,Redis,




        #     {
              
        #         "name": "Office Chair",
        #         "category": "Furniture",
        #         "price": 199.99,
        #         "stock": 20,
        #         "description": "Ergonomic office chair with lumbar support."
        #     }
        # '''
class Market_product(models.Model):
     CATEGORY_CHOICES = (
            ("accessories", "Accessories"),
            ("fashion", "Fashion"),
            ("electronics", "Electronics"),
          )
     
     name = models.CharField(max_length=30)
     category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
     price = models.FloatField()
     stock = models.IntegerField()
     description = models.TextField()
     is_available = models.BooleanField()
     created_at = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return self.name