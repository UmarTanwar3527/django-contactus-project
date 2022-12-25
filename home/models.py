from django.db import models

# makemigrations = crate and store in a file
# migrate = apply the pending changes created by makemigrations
# aplly means to write the data in database(db.sqlite3) which is a default database in django 

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    