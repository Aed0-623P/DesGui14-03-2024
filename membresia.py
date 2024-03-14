from abc import ABC,abstractmethod

class Membresia(ABC):

    def __init__(self,correo_subs:str,num_tarjeta:str):
        self.correo_subs=correo_subs
        self.num_tarjeta=num_tarjeta

    @property
    def correo_subs(self):
        return self.correo_subs
    
    @property
    def num_tarjeta(self):
        return self.num_tarjeta
    
    @abstractmethod
    def cambiar_subscripcion(self, n_membresia:int, ):
        pass

    def _crear_nueva_membresia():
        pass

class MemBasica(Membresia):
    valor = 3000
    devices = 2

    def __init__(self, correo_subs: str, num_tarjeta: int):     #constructor
        super().__init__(correo_subs, num_tarjeta)        #trae constructor padre