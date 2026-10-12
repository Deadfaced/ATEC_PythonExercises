from contact import Contact


def main() -> None:
    ana = Contact("Ana Silva", "912345678")
    rui = Contact("Rui Costa", "934567890")

    ana.show_details()
    rui.show_details()

    ana.phone = "961112223"

    ana.show_details()
    rui.show_details()


if __name__ == "__main__":
    main()
