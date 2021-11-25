def podio_olimpico(a,b,c):

  
  if (a<b) and (a<c):
    if (b<c): 
        return   f"1 - {a} minutos\n2 - {b} minutos\n3 - {c} minutos\n"
    else:
        return   f"1 - {a} minutos\n2 - {c} minutos\n3 - {b} minutos\n" 

  if (b<a) and (b<c): 

    if (a<c):
      return   f"1 - {b} minutos\n2 - {a} minutos\n3 - {c} minutos\n"
    else:
      return  f"1 - {b} minutos\n2 - {c} minutos\n3 - {a} minutos\n"

  else:
    
    if (a<b):
      return   f"1 - {c} minutos\n2 - {a} minutos\n3 - {b} minutos\n"
    else:
      return   f"1 - {c} minutos\n2 - {b} minutos\n3 - {a} minutos\n"


print('modificacao')
