import ModuloNumeros

def main():
    numeros_aleatorios = ModuloNumeros.generar_numeros_aleatorios()
    ModuloNumeros.mostrar_lista(numeros_aleatorios)
    ModuloNumeros.ordenar_y_mostrar(numeros_aleatorios)

if __name__ == "__main__":
    main()