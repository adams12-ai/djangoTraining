from django.db import models


# STRUCTURE MODELS
class Register(models.Model):
    SEXE_CHOICES = [
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin')
    ]
    sexe = models.CharField('sexe', choices=SEXE_CHOICES, max_length=9)
    nom = models.CharField('nom', max_length=25)
    prenom = models.CharField('prénom', max_length=25)
    date_nais = models.DateField('date de naissance', auto_now_add=False)
    lieu_nais = models.CharField('lieu de naissance', max_length=25)

    class Meta:
        verbose_name = 'Customer'

    def __str__(self):
        return '{0} {1}'.format(self.nom, self.prenom)
