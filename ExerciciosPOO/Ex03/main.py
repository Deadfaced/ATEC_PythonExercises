from thermostat import Thermostat


def main() -> None:
    thermostat = Thermostat("Sala")

    thermostat.set_temperature(22)
    print(f"Temperatura: {thermostat.get_temperature()}")

    try:
        thermostat.set_temperature(35)
    except ValueError as error:
        print(f"Erro: {error}")

    print(f"Temperatura: {thermostat.get_temperature()}")

    thermostat.__target_temperature = 50
    print(f"Temperatura: {thermostat.get_temperature()}")


if __name__ == "__main__":
    main()
