"""
Zadanie 9.2: obsługa API
W ramach zadania pobierzesz dane z API Narodowego Banku Polskiego, które dostarczane są w formacie JSON. 
Wybierzesz z nich listę kursów walut i utworzysz plik CSV, w którym je zapiszesz.

Zapisz je do pliku. Można też pobrać je bezpośrednio z poziomu Pythona, np. przy pomocy biblioteki requests:

import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
To, co mamy w data jest już pythonowym obiektem. Nawet nie musimy bawić się w operacje przy pomocy json. 
Piękna sprawa. 
Swoją drogą – biblioteka requests często jest wskazywana jako przykład znakomitego projektu – przyjazne API i wzorcowo napisany kod.

Dane wyglądają mniej więcej w ten sposób:

[{"table":"C","no":"071/C/NBP/2020","tradingDate":"2020-04-09","effectiveDate":"2020-04-10","rates":[{"currency":"dolar amerykański","code":"USD","bid":4.1117,"ask":4.1947},{"currency":"dolar australijski","code":"AUD","bid":2.5907,"ask":2.6431},{"currency":"dolar kanadyjski","code":"CAD","bid":2.9388,"ask":2.9982},{"currency":"euro","code":"EUR","bid":4.4945,"ask":4.5853},{"currency":"forint (Węgry)","code":"HUF","bid":0.012725,"ask":0.012983},{"currency":"frank szwajcarski","code":"CHF","bid":4.2487,"ask":4.3345},{"currency":"funt szterling","code":"GBP","bid":5.1287,"ask":5.2323},{"currency":"jen (Japonia)","code":"JPY","bid":0.037844,"ask":0.038608},{"currency":"korona czeska","code":"CZK","bid":0.1671,"ask":0.1705},{"currency":"korona duńska","code":"DKK","bid":0.6020,"ask":0.6142},{"currency":"korona norweska","code":"NOK","bid":0.4045,"ask":0.4127},{"currency":"korona szwedzka","code":"SEK","bid":0.4115,"ask":0.4199},{"currency":"SDR (MFW)","code":"XDR","bid":5.6318,"ask":5.7456}]}]
Trzeba z nich wybrać listę rates i na jej podstawie stworzyć plik csv. Plik ten powinien mieć następujące kolumny:

currency;code;bid;ask
Jako separator ustaw znak średnika, czyli ;.

To jedna część ćwiczenia. Drugą będzie prosty kalkulator walut. Postaraj się stworzyć formularz, w którym umieścisz pole typu select. 
Powinno ono zawierać kody walut, np. na podstawie poprzedniego zapytania do banku. Jak działa taki select możesz sprawdzić np. tutaj: 
https://www.w3schools.com/tags/tag_select.asp
Powinno być jeszcze drugie pole, w którym wpiszemy, ile danej waluty chcemy kupić.
Po kliknięciu w przycisk “Przelicz”, powinien nam się wyświetlić koszt takiej operacji w złotówkach (PLN).
Postaraj się o estetyczny wygląd aplikacji.

Kod umieść w serwisie GitHub i prześlij link Mentorowi, niech sprawdzi, czy już rwać włosy z głowy z powodu kursu franka szwajcarskiego.

Dla chętnych
Stwórz różne pythonowe obiekty i postaraj się, używając pickle, zapisać je do pliku. Poeksperymentuj, a jeśli trzeba, poszukaj odpowiedzi w sieci na następujące pytania:

Czy można "zapiklować" więcej niż jeden obiekt na raz bez opakowywania ich w jakiś kontener? Pamiętaj, że lista tasks w poprzednim przypadku to jeden obiekt.
Czy mogę "zapiklować" instancję klasy?
Czy używanie pickle jest zawsze bezpieczne?
"""
import json

import requests
from flask import Flask, request, render_template

from utils import pick, export_rates_to_csv




app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
curr = response.json()[0]['rates']



#http://localhost:5000/rates
@app.route("/rates", methods=["GET"])
def get_rates():
    #zamieniłem tutaj kod waluty na opis waluty - jest czytelniejsze jak na moje
    """
    Fill-in select field.
    """
    items = []

    for i in curr:
        item = i['currency']
        items.append(item)
        
    return render_template("rates.html", items=items)



@app.route("/rates", methods=["GET", "POST"])
def get_value():
    """
    Fill in select field by selected currency as selected option.
    Calculate rate based on given amout of choosen currency.
    """
    items = []
    choose = str(request.form.get("choosen"))
    amo = float(request.form.get("amount"))

    for i in curr:
        item = i['currency']
        items.append(item)
        if choose == i["currency"]:
            rate = round(amo * i["ask"], 4)
    return render_template("rates.html", items=items, amount=amo, rate=rate, choose=choose)





if __name__ == "__main__":
    export_rates_to_csv(curr)

    """
    # pickle :)

    def ogorki(val):
        bla = []
        for i in val:
            bla.append(i)
        return bla

    ogor = curr
    ogorki(ogor)

    with open("todo.pickle", 'wb') as f:
        pickle.dump(ogorki(ogor), f)

    with open("todo.pickle", "rb") as f:
        ogor = pickle.load(f)
    """

    app.run(debug=True)