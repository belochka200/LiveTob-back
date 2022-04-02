from django.db import models

class PopularPeople(models.Model):
    title = models.CharField("Имя", max_length=255)
    bored = models.DateField("Дата рождения")
    died = models.DateField("Дата смерти", blank=True, null=True)
    text = models.TextField("Текст")
    image = models.ImageField("Изображение", upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Популярный тоболяк'
        verbose_name_plural = 'Популярные тоболяки'


class InterestingFact(models.Model):
    text = models.TextField("Текст")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Интересный факт'
        verbose_name_plural = 'Интересные факты'