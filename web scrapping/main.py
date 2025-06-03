from bs4 import BeautifulSoup


with open('phones.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')


phones = soup.find_all('div', class_='Phone')


for phone in phones:
    company = phone.find('h2', class_='Company').text.strip()
    model = phone.find('p', class_='Model').text.strip()
    price = phone.find('p', class_='Price').text.strip()

    print(f"Company: {company}")
    print(f"Model: {model}")
    print(f"Price: {price}")
    print('-' * 30)
