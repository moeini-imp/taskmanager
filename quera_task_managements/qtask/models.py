from django.db import models

# Create your models here.


class Owner(models.Model):
    owner_first_name=models.CharField(max_length=50)
    owner_last_name=models.CharField(max_length=50)
    owner_email=models.EmailField()
    owner_team_role=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.owner_first_name} the {self.owner_team_role}'


class Project(models.Model):
    project_name=models.CharField(max_length=100)
    project_manager=models.ForeignKey(Owner,on_delete=models.DO_NOTHING,default="Matin himself")

    def __str__(self):
        return self.project_name

class Tags(models.Model):
    tag_name=models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

    
class Task(models.Model):
    CHOICES=(
        ("HOT","HOT FIX"),
        ("High","High"),
        ("Medium", "Medium"),
        ("Low","Low")
    )
    task_title=models.CharField(blank=False,null=False,max_length=100)
    task_descriptions=models.CharField(blank=True,max_length=200)
    task_blongs_to_project=models.ForeignKey(Project,on_delete=models.CASCADE)
    task_priority=models.CharField(choices=CHOICES,max_length=20)
    task_created_time=models.DateTimeField(auto_now_add=True)
    task_deadline=models.DateTimeField()
    task_owners=models.ManyToManyField(Owner)
    task_tags=models.ForeignKey(Tags,on_delete=models.DO_NOTHING,null=True,default=None)

    def __str__(self):
        return self.task_title