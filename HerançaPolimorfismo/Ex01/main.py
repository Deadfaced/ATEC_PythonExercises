from dog import Dog
from cat import Cat

def main() -> None:
    dog = Dog("Bobi", "Labrador")
    cat = Cat("Tareco")

    print(f"Nome do cão: {dog.name} de raça {dog.breed}")
    print(f"Nome do gato: {cat.name}")
    dog.describe()
    cat.describe()

if __name__ == "__main__":
    main()