from django.db import models
from mods.mods_models.mod_category import Mod_Category
from mods.mods_models.author import Author

class Mods(models.Model):
    name = models.CharField(max_length=250, db_index=True, help_text='Enter mod name')
    descr_short = models.CharField(max_length=250)
    descr_long = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField()
    game_version = models.FloatField()    
    download_count = models.IntegerField()
    mod_icon = models.ImageField(upload_to='icons')
    #mod_screenshoots = models.ImageField()
    mod_data = models.FileField(upload_to='mod_data')
    #discussions = 
    #changelog = 
    #metrics = 
    mod_category = models.ForeignKey(
        Mod_Category,
        #related_name='mods',
        on_delete=models.CASCADE
    )
    mod_author = models.ForeignKey(
        Author,
        #related_name = 'mods',
        on_delete = models.CASCADE
    )

    class Meta:
        ordering=('date_updated',)

    def __str__(self):
        return self.name