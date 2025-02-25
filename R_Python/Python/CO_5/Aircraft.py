class Aircraft:
    """Representa una aeronave con su información básica y plan de asientos.

    Attributes:
        registration (str): Matrícula de la aeronave.
        model (str): Modelo de la aeronave.
        num_rows (int): Número de filas de asientos.
        num_seats_per_row (int): Número de asientos por fila.
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """Inicializa una instancia de Aircraft.

        Args:
            registration (str): Matrícula de la aeronave.
            model (str): Modelo de la aeronave.
            num_rows (int): Número de filas de asientos.
            num_seats_per_row (int): Número de asientos por fila.
        """
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row
    
    def get_registration(self):
        """Obtiene la matrícula de la aeronave.

        Returns:
            str: Matrícula de la aeronave.
        """
        return self.__registration
    
    def get_model(self):
        """Obtiene el modelo de la aeronave.

        Returns:
            str: Modelo de la aeronave.
        """
        return self.__model
    
    def seating_plan(self):
        """Genera el plan de asientos de la aeronave.

        Returns:
            tuple: Una tupla con dos elementos:
                - rows (list): Lista de números de fila.
                - seats (str): Letras de los asientos.
        """
        rows = list(range(1, self.__num_rows + 1))
        seats = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:self.__num_seats_per_row]
        return (rows, seats)
    
    def num_seats(self):
        """Calcula el número total de asientos en la aeronave.

        Returns:
            int: Número total de asientos.
        """
        return self.__num_rows * self.__num_seats_per_row


class Airbus(Aircraft):
    """Representa un avión de la marca Airbus.

    Attributes:
        registration (str): Matrícula del avión.
        variant (str): Variante del modelo Airbus.
    """

    def __init__(self, registration, variant):
        """Inicializa una instancia de Airbus.

        Args:
            registration (str): Matrícula del avión.
            variant (str): Variante del modelo Airbus.
        """
        super().__init__(registration, "Airbus A319", 23, 6)
        self.__variant = variant
    
    def get_variant(self):
        """Obtiene la variante del modelo Airbus.

        Returns:
            str: Variante del modelo.
        """
        return self.__variant


class Boeing(Aircraft):
    """Representa un avión de la marca Boeing.

    Attributes:
        registration (str): Matrícula del avión.
        airline (str): Aerolínea a la que pertenece el avión.
    """

    def __init__(self, registration, airline):
        """Inicializa una instancia de Boeing.

        Args:
            registration (str): Matrícula del avión.
            airline (str): Aerolínea a la que pertenece el avión.
        """
        super().__init__(registration, "Boeing 777", 56, 9)
        self.__airline = airline
    
    def get_airline(self):
        """Obtiene la aerolínea a la que pertenece el avión.

        Returns:
            str: Nombre de la aerolínea.
        """
        return self.__airline