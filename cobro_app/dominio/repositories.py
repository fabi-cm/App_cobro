from .models import *
from abc import ABC, abstractmethod

class PagoRepositorio(ABC):
    @abstractmethod
    def A_ApiSolicitudCobro(self, token, codigoProducto,montoDebitar):
        pass
    @abstractmethod
    def B_recepcionar(self, numero_tarjeta, cvv, fecha_expiracion, clave_solicitud):
        pass
    @abstractmethod
    def C_CobroExitoso(self, exito):
        pass

class DjangoPagoRepositorio(PagoRepositorio):
    def A_ApiSolicitudCobro(self, token, codigoProducto, montoDebitar):
        return ApiSolicitudCobro.objects.create(token=token, codigoProducto=codigoProducto, montoDebitar=montoDebitar)
    
    def B_recepcionar(self, numero_tarjeta, cvv, fecha_expiracion, clave_solicitud):
        return Recepcion.objects.create(numero_tarjeta=numero_tarjeta, cvv=cvv, fecha_expiracion=fecha_expiracion, clave_solicitud=clave_solicitud)
    
    def C_CobroExitoso(self, exito):
        return CobroExitoso.objects.create(request=self.recepcion, exito=exito)