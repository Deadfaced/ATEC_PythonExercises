class Thermostat:
    MIN_TEMPERATURE = 10
    MAX_TEMPERATURE = 30

    def __init__(self, room_name: str) -> None:
        self._room_name = room_name
        self.__target_temperature = 20

    def get_temperature(self) -> int:
        return self.__target_temperature

    def set_temperature(self, value: int) -> None:
        if not self.MIN_TEMPERATURE <= value <= self.MAX_TEMPERATURE:
            raise ValueError(f"Temperatura fora do intervalo permitido: {value}")
        self.__target_temperature = value
