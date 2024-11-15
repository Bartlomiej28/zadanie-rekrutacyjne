# Projekt Rekrutacyjny

## Opis
 Projekt napisany w Pythonie wymaga dodania klucza API oraz zainstalowania odpowiednich zależności.

## Główne funkcjonalności

1. **Odczyt artykułu z pliku tekstowego**  
   Program odczytuje treść artykułu z pliku `article.txt` przy użyciu funkcji `read_article`.

2. **Tworzenie promptu dla API OpenAI**  
   Tworzę precyzyjny prompt, który przekazuje do modelu GPT-4o oczekiwania dotyczące strukturyzacji artykułu w HTML.

3. **Generowanie HTML dla artykułu**  
   OpenAI przekształca treść artykułu na strukturalny kod HTML:
   - Dodaje tagi HTML dla nagłówków, akapitów i obrazów.
   - Umieszcza obrazki `<img>` z atrybutami `alt` oraz `src`.
   - Dodaje opis obrazów w sekcji `<figcaption>` dla poprawy dostępności.

4. **Tworzenie szablonu HTML z CSS**  
   Dodatkowy kod generuje szablon HTML do wizualizacji artykułu, zawierający:
   - Nagłówki w atrakcyjnych kolorach.
   - Wyśrodkowanie treści.
   - Style CSS dla nagłówków, akapitów i obrazów.

5. **Zapis wyników do plików**  
   - Wygenerowany kod HTML artykułu jest zapisywany w pliku `artykul.html`.
   - Szablon z CSS jest zapisywany w pliku `szablon.html`.

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
