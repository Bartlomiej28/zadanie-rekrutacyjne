# Projekt Rekrutacyjny

## Opis
 Projekt napisany w Pythonie wymaga dodania klucza API oraz zainstalowania odpowiednich zależności.

## Wymagania
- Python 3
- Plik `.env` z kluczem API (wzór dostępny w `.env.example`)

## Instalacja i uruchomienie

1. Sklonuj repozytorium:
   ```
   git clone <URL_repozytorium>
   cd <nazwa_katalogu>
   ```

2. Zainstaluj wymagane pakiety:
   ```
   pip install -r requirements.txt
   ```

3. Skonfiguruj zmienne środowiskowe:
   - Skopiuj plik `.env.example` do `.env`:
     ```
     cp .env.example .env
     ```
   - Wypełnij klucz `API_KEY` w pliku `.env`.

4. Uruchom aplikację:
   ```
   python main.py
   ```

## Uwagi
Upewnij się, że masz zainstalowaną odpowiednią wersję Pythona oraz wszystkie wymagane pakiety przed uruchomieniem projektu.