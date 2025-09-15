from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=20)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "(" + self.menu_item.title + ")" + " " + self.ingredient.name + ": " + str(self.quantity) + " " + self.ingredient.unit

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.menu_item.title + " - " + self.timestamp.strftime("%B %d, %Y, %I:%M%p")