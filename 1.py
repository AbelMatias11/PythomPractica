#1
while True:
        try:
            combus = input("Ingrese la fracción del combustible X/Y (X e Y enteros): ")
            x, y = map(int, combus.split('/'))

            if x <= 0 or y <= 0 :
                print("Entrada inválida. Asegúrese de que ambos sean enteros positivos.")
                continue

            fraccion = x / y

            if fraccion < 0.01:
                resultado = "E"
            elif fraccion > 0.99:
                resultado = "F"
            else:
                porcentaje = round(fraccion * 100)
                resultado = f"{porcentaje}%"

            print(f"Cantidad de combustible en el tanque: {resultado}")
            break

        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números enteros separados por '/'")
        except ZeroDivisionError:
            print("Error: El denominador (Y) no puede ser cero.")
