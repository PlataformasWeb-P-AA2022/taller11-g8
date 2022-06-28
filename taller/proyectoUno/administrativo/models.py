from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Edificio(models.Model):
    tipo_edificio = (
    ('(Residencial)','residencial'),
    ('(Comercial)','comercial')
    )


    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices = tipo_edificio)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

   """ def obtener_costo_telefonos(self):
        # valor = [t.costo_plan for t in self.numeros_telefonicos.all()]
        # valor = sum(valor)  # [10.2, 20]
        valor = 0;
        for t in self.numeros_telefonicos.all(): # self.num_telefonicos -> me devuelve un listado de obj de tipo Departamento
            valor = valor + t.costo_plan
        return valor

    def obtener_cantidad_telefonos(self):
        """
        """
        valor = len(self.numeros_telefonicos.all())
        return valor"""


class Departamento(models.Model):
    nombre_prop = models.CharField(max_length=100)
    costo_dep = models.DecimalField(max_digits=100, decimal_places=2)
    num_cuartos = models.IntegerField
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="num_dep")

    def __str__(self):
        return "%s %s" % (self.nombre_prop, self.costo_dep, self.num_cuartos)
