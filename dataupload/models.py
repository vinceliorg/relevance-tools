from django.db import models

class Person(models.Model):
    doc_id=models.CharField(max_length=30, primary_key=True)
    title=models.CharField(max_length=100)
    summary=models.TextField()
    content=models.TextField()

