def dyv(u, v):
    # u = cadena base
    # v = cadena objetivo
    def resolver(pos_u, pos_v):

        if pos_u == 0: # si la cadena base es vacia, insetamos los valores faltantes
            operaciones = [f"Insertar '{v[k]}'"for k in range(pos_v)]
            return pos_v, operaciones


        if pos_v == 0: # si la cadena objetivo es vacia, eliminamos todos los caracteres de la cadeba base
            operaciones = [ f"Eliminar '{u[k]}'" for k in range(pos_u)]
            return pos_u, operaciones

        # =====================================================
        # Opción 1: Eliminar carácter
        # =====================================================
        costo_eliminar, operaciones_eliminar = resolver(pos_u - 1, pos_v)
        costo_eliminar += 1
        operaciones_eliminar = (operaciones_eliminar + [f"Eliminar '{u[pos_u - 1]}'"])

        # =====================================================
        # Opción 2: Insertar carácter
        # =====================================================

        costo_insertar, operaciones_insertar = resolver(pos_u, pos_v - 1)
        costo_insertar += 1
        operaciones_insertar = (operaciones_insertar+ [f"Insertar '{v[pos_v - 1]}'"])

        # =====================================================
        # Opción 3: Cambiar o mantener carácter
        # =====================================================

        costo_cambiar, operaciones_cambiar = resolver(pos_u - 1, pos_v - 1)

        if u[pos_u - 1] != v[pos_v - 1]: # si los caracteres son diferentes se realiza un cambio
          costo_cambiar += 1
          operaciones_cambiar = ( operaciones_cambiar + [f"cambiar "f"'{u[pos_u - 1]}' "f"por "f"'{v[pos_v - 1]}'"])

        else: # si son iguales se mantiene el cambio y continua
          operaciones_cambiar = ( operaciones_cambiar + [f"Mantener '{u[pos_u - 1]}'"])

        # =====================================================
        # Elegir la mejor opción
        # =====================================================
        if (costo_eliminar <= costo_insertar and costo_eliminar <= costo_cambiar):
            return costo_eliminar, operaciones_eliminar

        elif (costo_insertar <= costo_eliminar and costo_insertar <= costo_cambiar):
            return costo_insertar, operaciones_insertar

        else:
            return costo_cambiar, operaciones_cambiar


    distancia, operaciones = resolver(len(u),len(v))


    return distancia, operaciones