from django.test import TestCase

from .models import MiracleEucharistique, Priere


class MiracleEucharistiqueModelTests(TestCase):
    def test_slug_is_generated_and_uniquified(self):
        premier = MiracleEucharistique.objects.create(
            titre="Miracle de Buenos Aires",
            recit="Premier recit.",
        )
        second = MiracleEucharistique.objects.create(
            titre="Miracle de Buenos Aires",
            recit="Deuxieme recit.",
        )

        self.assertEqual(premier.slug, "miracle-de-buenos-aires")
        self.assertEqual(second.slug, "miracle-de-buenos-aires-2")


class PriereModelTests(TestCase):
    def test_priere_can_be_linked_to_a_miracle(self):
        miracle = MiracleEucharistique.objects.create(
            titre="Miracle de Lanciano",
            recit="Recit du miracle.",
        )
        priere = Priere.objects.create(
            titre="Priere de devotion eucharistique",
            categorie=Priere.Categorie.DEVOTION,
            texte="Seigneur, augmente en nous la foi eucharistique.",
            miracle_associe=miracle,
        )

        self.assertEqual(priere.miracle_associe, miracle)
