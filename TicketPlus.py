from Inventario import InventarioStub
from RepositorioFake import RepositorioFake
from repositorio import UsuarioDummy
from unittest.mock import Mock
from Spy import InventarioSpy

class TicketService:

   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviar_confirmacion(usuario)
      return True

inventario_spy = InventarioSpy()
email_mock = Mock()
service = TicketService(inventario_spy, RepositorioFake(), email_mock)
service.comprar(UsuarioDummy(), 1)
resultado = service.comprar(UsuarioDummy(), 2)
email_mock.enviar_confirmacion.assert_called()
print(resultado)
print(inventario_spy.veces_consultado)
