from django.db import models

# Create your models here.

class OnlineShop(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField('Заголовок', max_length=128) 
    discription = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите уместен ли торг')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "advertisements"
    
    def __str__(self): 
        return 'id = ' + str(self.id) + "," + "Заголовок = " + self.title + "," + " Цена = "  + str(self.price)

   
    

    