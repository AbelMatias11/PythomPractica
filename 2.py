#2

entrada = input("Ingrese las calificaciones separadas por comas: ")
calificaciones = []
for calificacion in entrada.split(','):
    try:
            calificaciones.append(int(calificacion))
    except ValueError:
            print(f"Error de tipeo'{calificacion}'")
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Calificaciones ingresadas: {calificaciones}")
        print(f"Promedio de calificaciones: {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones válidas.")
 