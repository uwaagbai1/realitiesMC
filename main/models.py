from django.db import models
from cloudinary.models import CloudinaryField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BaseModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
class Project(BaseModel):

    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250, null=True)
    image = CloudinaryField('image')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
    
class MasterClass(BaseModel):

    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def get_short_content(self):
        return self.content [:200]
        
    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'updated_on'