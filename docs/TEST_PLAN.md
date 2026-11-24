# Plan testów aplikacji do sortowania liczb

## 1. Informacje ogólne

**Nazwa projektu:** Aplikacja do sortowania liczb

**Cel testów:** Sprawdzenie poprawności działania funkcji odpowiedzialnych za sortowanie liczb, usuwanie duplikatów, sprawdzanie kolejności elementów oraz pobieranie danych od użytkownika.

**Zakres testów:** Moduł `src/app.py`.

**Środowisko testowe:**
- Python 3.12
- PyTest 9.0.2
- System Windows

## 2. Scenariusze testowe

| ID | Nazwa testu | Opis | Oczekiwany rezultat |
|---|---|---|---|
| TC-01 | Sortowanie rosnące | Wywołanie funkcji `sort_ascending()` | Liczby zostają posortowane rosnąco |
| TC-02 | Sortowanie malejące | Wywołanie funkcji `sort_descending()` | Liczby zostają posortowane malejąco |
| TC-03 | Usuwanie duplikatów | Wywołanie funkcji `remove_duplicates()` | Powtarzające się elementy zostają usunięte |
| TC-04 | Sprawdzanie sortowania | Wywołanie funkcji `is_sorted()` | Funkcja poprawnie określa, czy lista jest posortowana |
| TC-05 | Pobieranie liczb | Wprowadzenie liczb całkowitych | Program poprawnie zapisuje podane liczby |
| TC-06 | Liczby zmiennoprzecinkowe | Wprowadzenie liczb z częścią dziesiętną | Program poprawnie zapisuje liczby zmiennoprzecinkowe |
| TC-07 | Nieprawidłowe dane | Wprowadzenie tekstu zamiast liczby | Program informuje o błędzie i pozwala kontynuować |
| TC-08 | Puste dane | Zakończenie wpisywania bez podania liczb | Program zwraca pustą listę |

## 3. Wyniki testowania

Testy automatyczne zostały wykonane przy użyciu biblioteki PyTest.

Polecenie użyte do uruchomienia testów:

```bash
python -m pytest src/ -v
```

**Wynik testowania:**
- Liczba wszystkich testów: 8
- Testy zakończone powodzeniem: 8
- Testy zakończone niepowodzeniem: 0

**Końcowy rezultat: PASS**

## 4. Podsumowanie

Wszystkie osiem testów zakończyło się powodzeniem. Potwierdzono poprawność działania funkcji sortujących, usuwania duplikatów, sprawdzania kolejności liczb oraz pobierania danych wejściowych.

Testowanie pozwoliło sprawdzić podstawowe funkcjonalności aplikacji i potwierdzić ich poprawne działanie.