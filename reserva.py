class Reserva:
   def __init__(self, cliente, servicio):
       if cliente is None or servicio is None:
           raise ValueError("Datos inválidos para la reserva")

       self.cliente = cliente
       self.servicio = servicio
       self.estado = "Pendiente"

   def confirmar(self):
       if self.estado != "Pendiente":
           raise Exception("La reserva ya fue procesada")

       self.estado = "Confirmada"

   def cancelar(self):
       if self.estado == "Cancelada":
           raise Exception("La reserva ya está cancelada")

       self.estado = "Cancelada"

   def mostrar(self):
       return f"{self.cliente.mostrar()} | Servicio: {self.servicio.nombre} | Estado: {self.estado}"
