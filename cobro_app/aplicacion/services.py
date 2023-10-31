from ..dominio.repositories import PagoRepositorio
import random

class PagoServicio:
    def __init__(self, pagoRepositorio: PagoRepositorio):
        self.pagoRepositorio = pagoRepositorio
        self.clave_solicitud = None

    def Generacion_de_intento(self, token, codigoProducto, montoDebitar):
        self.pagoRepositorio.A_ApiSolicitudCobro(token, codigoProducto, montoDebitar)
        self.clave_solicitud = random.randint(0, 100)
        return self.clave_solicitud
    
    def Recepcion(self, numero_tarjeta, cvv, fecha_expiracion, clave_solicitud):
        return self.pagoRepositorio.B_recepcionar(numero_tarjeta, cvv, fecha_expiracion, clave_solicitud)
    
    def Cobro_exitoso_o_no(self, exito_o_no):
        return self.pagoRepositorio.C_CobroExitoso(exito=exito_o_no)