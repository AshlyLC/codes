# Clase TV
class TV():
  def __init__(self):
    self.isOn = False #Estado inicial de TV apagada
    self.isMuted = False #Estado inicial NO muteado
    # Algunos canales predeterminados
    self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
    self.nChannels = len(self.channelList) #Número total de canales
    self.channelIndex = 0 #Indice del canal actual, comienza con el primero, es decir, el canal 2
    self.VOLUME_MINIMUM = 0    # constante 
    self.VOLUME_MAXIMUM = 10   # constante
    self.volume = self.VOLUME_MAXIMUM // 2 #Volumen inicial, mitad del máximo, es decir 10/2 = 5

  def power(self):
    self.isOn = not self.isOn   # toggle para prender o apagar la TV

  def volumeUp(self):
    if not self.isOn: #Si la TV está apagada, no hace nada
      return
    if self.isMuted:
      self.isMuted = False     # cambiar el volumen mientras está silenciado reactiva el sonido
    if self.volume < self.VOLUME_MAXIMUM: #Aumenta el volumen si no ha alcanzado el máximo
      self.volume = self.volume + 1

  def volumeDown(self):
    if not self.isOn: #Si la TV está apagada, no hace nada
      return
    if self.isMuted:
      self.isMuted = False     # cambiar el volumen mientras está silenciado reactiva el sonido
    if self.volume > self.VOLUME_MINIMUM: #Disminuye el volumen si no ha alcanzado el mínimo
      self.volume = self.volume - 1

  def channelUp(self):
    if not self.isOn: #Si la TV está apagada, no hace nada
      return
    self.channelIndex = self.channelIndex + 1
    if self.channelIndex >= self.nChannels:   # si el índice del canal excede el número de canales
      self.channelIndex = 0   # volver al primer canal

  def channelDown(self):
    if not self.isOn: #Si la TV está apagada, no hace nada
      return
    self.channelIndex = self.channelIndex - 1
    if self.channelIndex < 0:    # si el índice del canal es menor que cero
      self.channelIndex = self.nChannels - 1    # volver al último canal

  def mute(self):
    if not self.isOn: #Si la TV está apagada, no hace nada
      return
    self.isMuted = not self.isMuted #toggle entre muteado y no muteado pero solo si el TV está encendido

  def setChannel(self, newChannel): #Para cambiar a un canal especificado
    if newChannel in self.channelList:
      self.channelIndex = self.channelList.index(newChannel)
    # si el nuevo canal no está en nuestra lista de canales, no hace nada

  def showInfo(self):
    print('Estado del TV:')
    if self.isOn:
      print('    La TV está: Encendida')
      print('    El canal es:', self.channelList[self.channelIndex])
      if self.isMuted:
        print('    El volumen es:', self.volume, '(el sonido está silenciado)')
      else:
        print('    El volumen es:', self.volume)
    else:
      print('    TV está: Apagado')


# Código principal
objeto_tv = TV()  # crear el objeto TV
# Encender el TV y mostrar el estado
objeto_tv.power()
objeto_tv.showInfo()

# Cambiar el canal dos veces hacia arriba, aumentar el volumen dos veces, mostrar estado
objeto_tv.channelUp()
objeto_tv.channelUp()
objeto_tv.volumeUp()
objeto_tv.volumeUp()
objeto_tv.showInfo()

# Apagar el TV, mostrar estado, encender el TV, mostrar estado
objeto_tv.power()
objeto_tv.showInfo()
objeto_tv.power()
objeto_tv.showInfo()

# Bajar el volumen, silenciar el sonido, mostrar estado
objeto_tv.volumeDown()
objeto_tv.mute()
objeto_tv.showInfo()

# Cambiar el canal a 11, silenciar el sonido, mostrar estado
objeto_tv.setChannel(11)
objeto_tv.mute()
objeto_tv.showInfo()

# Dos objetos TV con llamadas a sus métodos
# Código principal
objeto_tv1 = TV()  # crear un objeto TV
objeto_tv2 = TV()  # crear otro objeto TV

# Encender ambos televisores
objeto_tv1.power()
objeto_tv2.power()

# Aumentar el volumen de TV1
objeto_tv1.volumeUp()
objeto_tv1.volumeUp()

# Aumentar el volumen de TV2
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()

# Cambiar el canal de TV2, luego silenciarlo
objeto_tv2.setChannel(44)
objeto_tv2.mute()

# Mostrar la información de ambos televisores
objeto_tv1.showInfo()
objeto_tv2.showInfo()