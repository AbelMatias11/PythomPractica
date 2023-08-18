import operaciones
def main():
    a = float(input("1 Ingrese el número: "))
    b = float(input("2 Ingrese el número: "))
    
    print("Suma:", operaciones.suma(a, b))
    print("Resta:", operaciones.resta(a, b))
    print("División:", operaciones.division(a, b))
    print("Producto:", operaciones.producto(a, b))
    

if __name__ == "__main__":
    main()