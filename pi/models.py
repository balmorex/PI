from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    ingrediente_id = models.IntegerField(primary_key=True)
    nom_ingrediente = models.CharField(max_length=25)

    def __str__(self):
        return self.nom_ingrediente

class Pizza(models.Model):
    pizza_id = models.IntegerField(primary_key=True)
    nom_pizza = models.CharField(max_length=30)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_pizza

class TipoMasa(models.Model):
	id_tipo_masa = models.IntegerField(primary_key=True)
	nom_tipo = models.CharField(max_length=7)

	def __str__(self):
		return self.nom_tipo

#nuevos
class Empleado(models.Model):
	cod_empleado=models.IntegerField(primary_key=True)
	nom_empleado=models.CharField(max_length=40)
	password_empleado=models.CharField(max_length=16,blank=False)

	def __str__(self):
		return self.nom_empleado

class Cliente(models.Model):
	id_cliente=models.AutoField(primary_key=True)
	"""
	el autofield es para poner un nombre personalizado
	a una id generada automaticamente
	y no usar la que provee django por defecto (id)
	"""
	nom_cliente=models.CharField(max_length=40)
	dir_cliente=models.CharField(max_length=100)
	tel_cliente=models-BigIntegerField()

class Pedido(mdoels.Model):
	cod_pedido=models.IntegerField(primary_key=True)
