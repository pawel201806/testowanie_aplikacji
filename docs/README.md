# Aplikacja do sortowania liczb – Git/GitHub

## 1. Opis projektu

Projekt przedstawia prostą aplikację napisaną w języku Python, która umożliwia wprowadzanie liczb przez użytkownika, sortowanie ich oraz wykonywanie podstawowych operacji na listach.

Aplikacja została przygotowana w celu poznania systemu kontroli wersji Git, korzystania z GitHuba oraz testowania oprogramowania przy użyciu biblioteki PyTest.

## 2. Funkcjonalności aplikacji

Program umożliwia:
- sortowanie liczb rosnąco,
- sortowanie liczb malejąco,
- usuwanie duplikatów z listy,
- sprawdzanie, czy lista jest posortowana,
- pobieranie liczb od użytkownika,
- obsługę liczb całkowitych i zmiennoprzecinkowych,
- obsługę nieprawidłowych danych wejściowych.

## 3. Struktura projektu

```text
testowanie_aplikacji/
├── src/
│   ├── app.py
│   └── test_app.py
├── docs/
│   ├── README.md
│   └── TEST_PLAN.md
├── .github/
│   └── workflows/
│       └── tests.yml
└── .gitignore
```

## 4. Wymagania

- Python 3.10 lub nowszy
- PyTest

## 5. Instalacja

W terminalu należy zainstalować bibliotekę PyTest:

```bash
python -m pip install pytest
```

## 6. Uruchamianie aplikacji

Z głównego folderu projektu należy wykonać polecenie:

```bash
python src/app.py
```

Program umożliwia wpisywanie liczb jedna po drugiej. Aby zakończyć wprowadzanie danych, należy wpisać `stop`.

## 7. Uruchamianie testów

Testy można uruchomić poleceniem:

```bash
python -m pytest src/ -v
```

Testy sprawdzają poprawność sortowania, usuwania duplikatów, sprawdzania kolejności liczb oraz pobierania danych wejściowych.

## 8. Automatyzacja testów

Projekt zawiera konfigurację GitHub Actions w pliku `.github/workflows/tests.yml`.

Jej zadaniem jest automatyczne uruchamianie testów po przesłaniu zmian do repozytorium GitHub.

## 9. Podsumowanie

Projekt pozwala poznać podstawowe możliwości języka Python, tworzenie testów jednostkowych przy użyciu PyTest oraz wykorzystanie Git i GitHuba do przechowywania kodu, dokumentacji i historii zmian.