from pprint import pprint

class Flight:
    """Representa un vuelo con su información y gestión de asientos.

    Attributes:
        number (str): Número del vuelo.
        aircraft (Aircraft): Aeronave asignada al vuelo.
        seating (list): Lista de diccionarios que representan los asientos.
    """

    def __init__(self, number, aircraft):
        """Inicializa una instancia de Flight.

        Args:
            number (str): Número del vuelo.
            aircraft (Aircraft): Aeronave asignada al vuelo.
        """
        if not number or len(number) > 5:  # Ejemplo de validación
            raise ValueError("Número de vuelo inválido")
        self.__number = number
        self.__aircraft = aircraft
        self.__seating = [None]  # el 0 no se utiliza
        rows, seats = self.__aircraft.seating_plan()
        for _ in rows:
            self.__seating.append({letter: None for letter in seats})

    def get_number(self):
        """Obtiene el número del vuelo.

        Returns:
            str: Número del vuelo.
        """
        return self.__number

    def get_aircraft_model(self):
        """Obtiene el modelo de la aeronave asignada al vuelo.

        Returns:
            str: Modelo de la aeronave.
        """
        return self.__aircraft.get_model()

    def allocate_passenger(self, seat, passenger_data):
        """Asigna un pasajero a un asiento específico.

        Args:
            seat (str): Designación del asiento (por ejemplo, '12A').
            passenger_data (tuple): Datos del pasajero (nombre, apellido, ID).

        Raises:
            ValueError: Si el asiento ya está ocupado.
        """
        row, letter = self.__parse_seat(seat)
        if row >= len(self.__seating) or letter not in self.__seating[1]:
            raise ValueError(f"Asiento {seat} no existe")
        if self.__seating[row][letter] is not None:
            raise ValueError(f"Asiento {seat} ya está ocupado")
        self.__seating[row][letter] = passenger_data

    def reallocate_passenger(self, from_seat, to_seat):
        """Reasigna un pasajero de un asiento a otro.

        Args:
            from_seat (str): Asiento actual del pasajero.
            to_seat (str): Nuevo asiento para el pasajero.

        Raises:
            ValueError: Si el asiento actual está vacío o el nuevo asiento ya está ocupado.
        """
        from_row, from_letter = self.__parse_seat(from_seat)
        to_row, to_letter = self.__parse_seat(to_seat)
        if self.__seating[from_row][from_letter] is None:
            raise ValueError(f"No hay pasajeros en el asiento {from_seat}")
        if self.__seating[to_row][to_letter] is not None:
            raise ValueError(f"El asiento {to_seat} ya está ocupado")
        self.__seating[to_row][to_letter] = self.__seating[from_row][from_letter]
        self.__seating[from_row][from_letter] = None

    def num_available_seats(self):
        """Obtiene el número de asientos disponibles en el vuelo.

        Returns:
            int: Número de asientos disponibles.
        """
        return sum(sum(1 for seat in row.values() if seat is None) for row in self.__seating[1:])

    def print_seating(self):
        """Imprime el plan de asientos del vuelo."""
        pprint(self.__seating[1:])

    def print_boarding_cards(self):
        """Imprime las tarjetas de embarque de todos los pasajeros asignados."""
        for passenger_data, seat in self.__passenger_seats():
            name, surname, id_card = passenger_data
            print(f"----------------------------------------------------------")
            print(f"|     {name} {surname} {id_card} {seat} {self.__number} {self.__aircraft.get_model()}      |")
            print(f"----------------------------------------------------------")

    def __parse_seat(self, seat):
        """Divide la designación del asiento en fila y letra.

        Args:
            seat (str): Designación del asiento (por ejemplo, '12A').

        Returns:
            tuple: Una tupla con la fila (int) y la letra (str) del asiento.
        """
        row = int(seat[:-1])
        letter = seat[-1]
        return (row, letter)

    def __passenger_seats(self):
        """Genera un iterador sobre los asientos ocupados.

        Yields:
            tuple: Una tupla con los datos del pasajero y la designación del asiento.
        """
        for row_num, row in enumerate(self.__seating[1:], 1):
            for letter, passenger_data in row.items():
                if passenger_data is not None:
                    yield (passenger_data, f"{row_num}{letter}")

    def get_seating(self):
        """Obtiene la lista de asientos del vuelo.

        Returns:
            list: Lista de diccionarios que representan los asientos.
        """
        return self.__seating