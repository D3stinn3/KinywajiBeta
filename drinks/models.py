from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name + '' + self.description


    def my_items(self) -> str:
        count = 0
        while count < int(self.name.count):
            print('Hello Sir')
        
        print("------------")

    def __repr__(self) -> str:
        return super().__repr__(self.my_items)


