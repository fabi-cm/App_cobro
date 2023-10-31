from django.db import models

# a.-
class ApiSolicitudCobro(models.Model):
    token = models.CharField(max_length=255)
    codigoProducto = models.CharField(max_length=255)
    montoDebitar = models.DecimalField(max_digits=10, decimal_places=2)

# b.-
class Recepcion(models.Model):
    # apiSolicitud = models.ForeignKey(ApiSolicitudCobro, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    fecha_expiracion = models.CharField(max_length=5)
    clave_solicitud = models.CharField(max_length=255)

# c.-
class CobroExitoso(models.Model):
    request = models.ForeignKey(Recepcion, on_delete=models.CASCADE)
    exito = models.BooleanField(default=False)