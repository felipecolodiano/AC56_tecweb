from django.db import models




class Curso(models.Model):
    
    TIPOS = (
    ('TECNICO','Técnico'),
    ('GRADUACAO','Graduação'),
    ('PGRADUACAO',' Pós-graduação')
  )

    nome = models.CharField(
        'Nome', 
        max_length=120
        )
    sigla = models.CharField(
        'Sigla', 
        max_length=5, 
        unique =True
        )
    tipo = models.CharField(
        'Tipo de Curso', 
        max_length=30,
        choices=TIPOS
        )


class Meta:
    db_table = 'CURSO'