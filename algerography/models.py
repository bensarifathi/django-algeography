from django.db import models


class Wilaya(models.Model):
    name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Daira(models.Model):
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, related_name="dairas")
    name = models.CharField(max_length=255)
    ar_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name