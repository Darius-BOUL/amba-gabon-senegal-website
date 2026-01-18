from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

CONTENT_TYPES = [
    ("communique", "Communiqué officiel"),
    ("note", "Note d’information"),
    ("compte_rendu", "Compte rendu"),
    ("annonce", "Annonce"),
    ("message", "Message institutionnel"),
]

class News(models.Model):
    title = models.CharField("Titre", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    content = RichTextField("Contenu") 
    image = CloudinaryField("Image", blank=True, null=True)

    content_type = models.CharField(
        "Type de contenu",
        max_length=20,
        choices=CONTENT_TYPES,
        default="note"
    )

    published_at = models.DateTimeField("Date de publication", auto_now_add=True)
    is_published = models.BooleanField("Publié", default=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while News.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
