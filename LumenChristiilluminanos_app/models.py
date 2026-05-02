from django.db import models
from django.utils.text import slugify


class PublishedContent(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    ordre_affichage = models.PositiveIntegerField(default=0)
    est_publie = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._build_unique_slug()
        super().save(*args, **kwargs)

    def _build_unique_slug(self):
        base_slug = slugify(self.titre)[:240] or self.__class__.__name__.lower()
        slug = base_slug
        counter = 2

        while self.__class__.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            suffix = f"-{counter}"
            slug = f"{base_slug[:255 - len(suffix)]}{suffix}"
            counter += 1

        return slug


class MiracleEucharistique(PublishedContent):
    lieu = models.CharField(max_length=255, blank=True)
    ville = models.CharField(max_length=120, blank=True)
    pays = models.CharField(max_length=120, blank=True)
    date_evenement = models.DateField(blank=True, null=True)
    periode_affichage = models.CharField(
        max_length=120,
        blank=True,
        help_text="Ex. An 1254, 1996, Pentecote 2000.",
    )
    personne_liee = models.CharField(
        max_length=255,
        blank=True,
        help_text="Ex. Carlo Acutis, Sainte Claire, Claudio Gatti.",
    )
    resume = models.TextField(
        blank=True,
        help_text="Courte introduction qui presente le miracle.",
    )
    recit = models.TextField(help_text="Recit principal du miracle.")
    analyse_scientifique = models.TextField(
        blank=True,
        help_text="Resultats d'enquetes, expertises ou constatations.",
    )
    devotion_associee = models.TextField(
        blank=True,
        help_text="Priere, litanie ou meditation attachee au miracle.",
    )
    source = models.TextField(
        blank=True,
        help_text="Reference bibliographique, citation ou temoignage.",
    )
    source_url = models.URLField(blank=True)

    class Meta:
        ordering = ("ordre_affichage", "titre")
        verbose_name = "miracle eucharistique"
        verbose_name_plural = "miracles eucharistiques"


class Priere(PublishedContent):
    class Categorie(models.TextChoices):
        QUOTIDIENNE = "quotidienne", "Quotidienne"
        INTERCESSION = "intercession", "Intercession"
        DEVOTION = "devotion", "Devotion"
        PENITENCE = "penitence", "Penitence"
        PROTECTION = "protection", "Protection"
        REPAS = "repas", "Repas"
        EGLISE = "eglise", "Eglise"
        AUTRE = "autre", "Autre"

    categorie = models.CharField(
        max_length=20,
        choices=Categorie.choices,
        default=Categorie.AUTRE,
    )
    intention = models.CharField(
        max_length=255,
        blank=True,
        help_text="Ex. paix, malades, defunts, familles, vocations.",
    )
    introduction = models.TextField(
        blank=True,
        help_text="Petit texte d'introduction ou contexte d'utilisation.",
    )
    texte = models.TextField(help_text="Texte complet de la priere.")
    miracle_associe = models.ForeignKey(
        MiracleEucharistique,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="prieres_associees",
    )
    contient_variables = models.BooleanField(
        default=False,
        help_text="Cochez si la priere contient des champs comme [Nom du malade].",
    )
    notes_utilisation = models.TextField(
        blank=True,
        help_text="Indications pastorales ou liturgiques optionnelles.",
    )

    class Meta:
        ordering = ("ordre_affichage", "titre")
        verbose_name = "priere"
        verbose_name_plural = "prieres"
