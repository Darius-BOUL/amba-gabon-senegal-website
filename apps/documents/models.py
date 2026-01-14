from django.db import models

class Document(models.Model):
    title = models.CharField("Titre", max_length=255)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.title
