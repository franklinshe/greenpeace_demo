from django.db import models

class Evaluator(model.Models):
    name = models.CharFiled(max_length=100)
    def __str__(self):
        return self.name

class Project_Type(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Order(models.Model):
    NRO = models.CharField(max_length=100)
    evaluator = models.ForeignKey(Evaluator, n_delete=models.CASCADE)
    project_type = models.ForeignKey(Project_Type, n_delete=models.CASCADE)
    keyword = models.Charfield(max_length=200, null=True)
    information = models.Charfield(max_length=1000, null=True)
    date_created = model.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.NRO