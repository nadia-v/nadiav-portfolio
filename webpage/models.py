from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    github = models.URLField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Detail(models.Model):
    image = models.ImageField(upload_to='images/')
    details = models.CharField(max_length=2000)
    tech = models.CharField(max_length=200, default='')
    github = models.URLField(max_length=100, default='')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="details")

    def __str__(self):
        return self.project.name

# class Technology(models.Model):
#     tech = models.CharField(max_length=50)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="technologies")

#     def __str__(self):
#         return self.project.name

class Picture(models.Model):
    picture = models.ImageField(upload_to='images/')
    screenshot_description = models.CharField(max_length=200, default='')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="pictures")

    def __str__(self):
        return self.project.name

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name