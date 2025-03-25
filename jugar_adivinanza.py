import random

# Diccionario con todos los departamentos de Colombia y sus capitales
departamentos = {
    "Amazonas": "Leticia",
    "Antioquia": "Medellín",
    "Arauca": "Arauca",
    "Atlántico": "Barranquilla",
    "Bolívar": "Cartagena",
    "Boyacá": "Tunja",
    "Caldas": "Manizales",
    "Caquetá": "Florencia",
    "Casanare": "Yopal",
    "Cauca": "Popayán",
    "Cesar": "Valledupar",
    "Chocó": "Quibdó",
    "Córdoba": "Montería",
    "Cundinamarca": "Bogotá",
    "Guainía": "Inírida",
    "Guaviare": "San José del Guaviare",
    "Huila": "Neiva",
    "La Guajira": "Riohacha",
    "Magdalena": "Santa Marta",
    "Meta": "Villavicencio",
    "Nariño": "Pasto",
    "Norte de Santander": "Cúcuta",
    "Putumayo": "Mocoa",
    "Quindío": "Armenia",
    "Risaralda": "Pereira",
    "San Andrés y Providencia": "San Andrés",
    "Santander": "Bucaramanga",
    "Sucre": "Sincelejo",
    "Tolima": "Ibagué",
    "Valle del Cauca": "Cali",
    "Vaupés": "Mitú",
    "Vichada": "Puerto Carreño"
}


def jugar_adivinanza():
    while True:
        # Escoger un departamento al azar
        departamento = random.choice(list(departamentos.keys()))
        capital_correcta = departamentos[departamento]
        intentos = 3

        print(f"\nAdivina la capital de {departamento}. Tienes {intentos} intentos.")

        while intentos > 0:
            respuesta = input("Ingresa la capital (o escribe 'salir' para terminar): ")

            if respuesta.lower() == 'salir':
                print("Hasta luego.")
                return

            if respuesta == capital_correcta:
                print("¡Correcto!")
                # Preguntar si quiere jugar otra ronda
                jugar_otra = input("¿Quieres jugar otra ronda? (sí/no): ").strip().lower()
                if jugar_otra == 'sí':
                    break  # Continuar con otra ronda
                elif jugar_otra == 'no':
                    print("Gracias por jugar. ¡Hasta luego!")
                    return  # Terminar el juego
                else:
                    print("Respuesta no válida. Terminando el juego.")
                    return
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"Incorrecto. Te quedan {intentos} intentos.")
                else:
                    print(
                        f"La capital correcta es {capital_correcta}. Hasta luego, sigue intentando en otra oportunidad.")


def main():
    print("Bienvenido al juego de adivinanza de departamentos y capitales.")
    jugar_adivinanza()


if __name__ == "__main__":
    main()
