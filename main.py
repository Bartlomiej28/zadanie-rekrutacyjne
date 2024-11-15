from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv('.env')
api_key: str = os.getenv('API_KEY')

client = OpenAI(
    api_key = api_key
)

def read_article(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Plik artykułu nie został znaleziony.")
        return None
    except Exception as e:
        print(f"Błąd podczas odczytu pliku: {e}")
        return None


def create_prompt(article_text):
    return (
        "Ustrukturyzuj poniższy tekst za pomocą tagów HTML. Korzystaj tylko z istniejących nagłówków - nie wyodębniaj nowych z tekstu."
        "Przeanalizuj, w które miejsca warto wstawić grafiki i dodaj w te miejsca tag <img> z z atrybutem src='image_placeholder.jpg'."
        "Do każdego obrazka dodaj atrybut alt, który posłuży jako prompt i będzie w stanie wygenerować precyzyjny obrazek w kontekście artykułu i nagłówka, twórz bardzo szczegółowe treści w atrybucie alt."
        "Pod grafikami umieść podpis dla każdego obrazu używając tagów <figure> i <figcaption>"
        "Zwrócony kod nie powinien zawierać kodu CSS ani JavaScript i nie powinien zawierać tagów <html></html> <head></head> <body></body>. Zwróć sam kod bez opisu stworzonego przez ciebie kodu i bez ```html na początku i ``` na końcu kodu \n\n"
        "Treść artykułu:\n\n" + article_text
    )

def generate_html_from_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant skilled in HTML and prompt engineering."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


def save_html(html_content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML został wygenerowany i zapisany w pliku {file_path}")
    except Exception as e:
        print(f"Błąd podczas zapisu pliku: {e}")


def main():
    article_text = read_article('article.txt')
    prompt = create_prompt(article_text)
    html_content = generate_html_from_openai(prompt)
    save_html(html_content, 'artykul.html')

    html_code = generate_html_from_openai("Wygeneruj szablon HTML do podglądu stworzonego wcześniej artykułu. Szablon ten powinien zawierać strukturę HTML z pustą sekcją <body>, gotową do wklejenia treści artykułu. Stwórz style CSS dla atrybutów strukturyzujących treść, wyśrodkuj artykuł, pokoloruj nagłówki. Artyukł ma być atrakcyjny wizualnie. Zwróć sam kod bez opisu stworzonego przez ciebie kodu i bez ```html na początku i ``` na końcu kodu")
    save_html(html_code, 'szablon.html')

if __name__ == "__main__":
    main()