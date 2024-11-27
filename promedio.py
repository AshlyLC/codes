def Promedio(listaNumeros):
  total=0.0
  elementos=0
  for numero in listaNumeros:
    total+=numero
    elementos+=1
  promedio=total/elementos
  return promedio