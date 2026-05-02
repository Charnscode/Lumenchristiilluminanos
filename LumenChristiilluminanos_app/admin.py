from django.contrib import admin

from .models import MiracleEucharistique, Priere

# Centralise the back-office identity so every admin page inherits the same
# platform branding.
admin.site.site_header = "Lumenchristiilluminanos"
admin.site.site_title = "Admin Lumenchristiilluminanos"
admin.site.index_title = "Tableau de bord de la plateforme"


@admin.register(MiracleEucharistique)
class MiracleEucharistiqueAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "lieu",
        "pays",
        "periode_affichage",
        "est_publie",
        "ordre_affichage",
    )
    list_filter = ("est_publie", "pays")
    search_fields = (
        "titre",
        "lieu",
        "ville",
        "pays",
        "personne_liee",
        "recit",
        "source",
    )
    ordering = ("ordre_affichage", "titre")
    readonly_fields = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("titre",)}
    fieldsets = (
        (
            "Publication",
            {
                "fields": (
                    "titre",
                    "slug",
                    "ordre_affichage",
                    "est_publie",
                )
            },
        ),
        (
            "Contexte",
            {
                "fields": (
                    "lieu",
                    "ville",
                    "pays",
                    "date_evenement",
                    "periode_affichage",
                    "personne_liee",
                )
            },
        ),
        (
            "Contenu",
            {
                "fields": (
                    "resume",
                    "recit",
                    "analyse_scientifique",
                    "devotion_associee",
                )
            },
        ),
        ("Sources", {"fields": ("source", "source_url")}),
        ("Suivi", {"fields": ("created_at", "updated_at")}),
    )


@admin.register(Priere)
class PriereAdmin(admin.ModelAdmin):
    list_display = (
        "titre",
        "categorie",
        "intention",
        "miracle_associe",
        "est_publie",
        "ordre_affichage",
    )
    list_filter = ("categorie", "est_publie", "contient_variables")
    search_fields = ("titre", "intention", "texte", "notes_utilisation")
    ordering = ("ordre_affichage", "titre")
    readonly_fields = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("titre",)}
    autocomplete_fields = ("miracle_associe",)
    fieldsets = (
        (
            "Publication",
            {
                "fields": (
                    "titre",
                    "slug",
                    "ordre_affichage",
                    "est_publie",
                )
            },
        ),
        (
            "Classification",
            {
                "fields": (
                    "categorie",
                    "intention",
                    "miracle_associe",
                    "contient_variables",
                )
            },
        ),
        ("Contenu", {"fields": ("introduction", "texte", "notes_utilisation")}),
        ("Suivi", {"fields": ("created_at", "updated_at")}),
    )
