import sys
import os

# Agrega el directorio raíz del proyecto al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from Aircraft import Aircraft, Airbus, Boeing
from Passenger import Passenger
from Flight import Flight

# Fixture para crear un vuelo de prueba
@pytest.fixture
def flight():
    aircraft = Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6)
    return Flight(number="BA117", aircraft=aircraft)

# Fixture para crear pasajeros de prueba
@pytest.fixture
def passengers():
    return [
        Passenger("Jack", "Shephard", "85994003S"),
        Passenger("Kate", "Austen", "12589756P"),
        Passenger("James", "Ford", "56278665F"),
        Passenger("John", "Locke", "10265448H"),
        Passenger("Sayid", "Jarrah", "15758664M")
    ]

# Pruebas para la creación de objetos Flight
def test_flight_creation(flight):
    assert flight.get_number() == "BA117"
    assert flight.get_aircraft_model() == "Airbus A319"

def test_invalid_flight_number():
    with pytest.raises(ValueError):
        Flight(number="BA99999", aircraft=Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6))

# Pruebas para la asignación de pasajeros
def test_allocate_passenger(flight, passengers):
    flight.allocate_passenger("12A", passengers[0].passenger_data())
    assert flight.get_seating()[12]["A"] == passengers[0].passenger_data()

def test_allocate_passenger_invalid_seat(flight, passengers):
    with pytest.raises(ValueError):
        flight.allocate_passenger("30A", passengers[0].passenger_data())  # Fila no válida

def test_allocate_passenger_occupied_seat(flight, passengers):
    flight.allocate_passenger("12A", passengers[0].passenger_data())
    with pytest.raises(ValueError):
        flight.allocate_passenger("12A", passengers[1].passenger_data())  # Asiento ocupado

# Pruebas para la reasignación de pasajeros
def test_reallocate_passenger(flight, passengers):
    flight.allocate_passenger("12A", passengers[0].passenger_data())
    flight.reallocate_passenger("12A", "14B")
    assert flight.get_seating()[12]["A"] is None
    assert flight.get_seating()[14]["B"] == passengers[0].passenger_data()

def test_reallocate_passenger_invalid_from_seat(flight, passengers):
    with pytest.raises(ValueError):
        flight.reallocate_passenger("12A", "14B")  # Asiento original vacío

def test_reallocate_passenger_invalid_to_seat(flight, passengers):
    flight.allocate_passenger("12A", passengers[0].passenger_data())
    flight.allocate_passenger("14B", passengers[1].passenger_data())  # Ocupar el asiento 14B
    with pytest.raises(ValueError):
        flight.reallocate_passenger("12A", "14B")  # Asiento destino ocupado

# Pruebas para el número de asientos disponibles
def test_num_available_seats(flight, passengers):
    assert flight.num_available_seats() == 132  # 22 filas * 6 asientos por fila
    flight.allocate_passenger("12A", passengers[0].passenger_data())
    assert flight.num_available_seats() == 131