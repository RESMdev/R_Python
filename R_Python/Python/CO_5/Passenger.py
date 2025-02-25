class Passenger:
    """Representa a un pasajero con su información personal.

    Attributes:
        name (str): Nombre del pasajero.
        surname (str): Apellido del pasajero.
        id_card (str): Número de identificación del pasajero.
    """

    def __init__(self, name, surname, id_card):
        """Inicializa una instancia de Passenger.

        Args:
            name (str): Nombre del pasajero.
            surname (str): Apellido del pasajero.
            id_card (str): Número de identificación del pasajero.
        """
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card
    
    def passenger_data(self):
        """Obtiene los datos del pasajero.

        Returns:
            tuple: Una tupla con el nombre, apellido y número de identificación.
        """
        return self.__name, self.__surname, self.__id_card