def sort_ascending(numbers):
    return sorted(numbers)


def sort_descending(numbers):
    return sorted(numbers, reverse=True)


def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))


def is_sorted(numbers):
    return numbers == sorted(numbers)


def get_numbers():
    numbers = []

    print("Wpisuj liczby jedna po drugiej.")
    print("Aby zakończyć wpisywanie, wpisz 'stop'.")

    while True:
        value = input("Podaj liczbę: ").strip()

        if value.lower() == "stop":
            break

        try:
            number = float(value)

            if number.is_integer():
                number = int(number)

            numbers.append(number)

        except ValueError:
            print("Błąd! Wpisz poprawną liczbę lub 'stop'.")

    return numbers


def main():
    print("\n=== APLIKACJA DO SORTOWANIA LICZB ===\n")

    numbers = get_numbers()

    if not numbers:
        print("\nNie podano żadnych liczb.")
        return

    print("\n=== WYNIKI ===")
    print("Twoje liczby:", numbers)
    print("Sortowanie rosnące:", sort_ascending(numbers))
    print("Sortowanie malejące:", sort_descending(numbers))


if __name__ == "__main__":
    main()