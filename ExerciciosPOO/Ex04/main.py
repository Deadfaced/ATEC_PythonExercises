from reservation import Reservation


def main() -> None:
    requests = [("Ana Silva", 4), ("", 2), ("Rui Costa", 15), ("Marta Lopes", 2)]
    reservations = []

    for customer_name, people in requests:
        try:
            reservation = Reservation(customer_name, people)
        except ValueError as error:
            print(f"Pedido recusado: {error}")
        else:
            reservations.append(reservation)

    print(f"Reservas criadas: {len(reservations)}")
    for reservation in reservations:
        print(f"{reservation.customer_name} ({reservation.people} pessoas)")


if __name__ == "__main__":
    main()
