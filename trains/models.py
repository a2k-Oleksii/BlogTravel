from django.db import models


class Train(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Номер потяга")
    from_city = models.ForeignKey("cities.City", on_delete=models.CASCADE, verbose_name="Звідки", related_name="from_city")
    to_city = models.ForeignKey("cities.City", on_delete=models.CASCADE, verbose_name="Куди", related_name="to_city")
    travel_time = models.IntegerField(verbose_name="Час в дорозі")

    class Meta:
        verbose_name = "Потяг"
        verbose_name_plural = "Потяги"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} з м.{self.from_city} в м.{self.to_city}"
