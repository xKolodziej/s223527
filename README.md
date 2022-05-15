# s223527

## Analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product-review|review|
|identyfikator opinii|\[data-entry-id\]|review_id|
|autor|span.user-post__author-name|author|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|
|liczba gwiazdek|span.user-post__score-count|stars|
|treść|div.user-post__text|content|
|data wystawienia|span.user-post__published > time:nth-child(1)\[datetime\]|publish_date|
|data zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes[data-total-vote]<br>button.vote-yes > span<br>span[id^=votes-yes]|useful|
|dla ilu nieprzydatna|button.vote-no[data-total-vote]<br>button.vote-no > span<br>span[id^=votes-no]|useless|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--positives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--positives)|pros|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item <br>div.review-feature__col:has( > div.review-feature__title--negatives) > div.review-feature__item<br>div.review-feature__item:has( ~ div.review-feature__title--negatives)|cons|
## Etapy pracy nad projektem
1) pobranie składowych pojedynczej opinii do niezaleznych zmiennych
2) zapisanie składowych do pojedynczej opiinii do obiektu słownika (disctionary)
3) pobranie wszystkich opinii z pojedynczej strony i zapisanie ich do listy słowników
4) pobranie opinii o wszkazym produkcie i zapisanie ich do pliku
5) optymalizacja kodu:
  - zdefiniowanie funkcji do ekstrakcji elementów strony Html
  - utorzenie słownika selektorów opisującego pojedynczą opinię
  - zastąpienie ekstrakcji składowych pojedynczej opinii do niezależnych zmiennych ekstrakcją tych składowych w dictionary        comperhension w oparciu o słownik selektorów 
6) analiza opinii o wskazanym produkcie:
  1) wyliczenie podstawowych statystyk
    1) liczba wzystkich opinii w produkcie
    2) liczba opinii z podaną liczbą zalet
    3) liczba opinii z podaną liczbą wad
    4) średnia ocena produktu
  2)narysowanie wykresów
    1) udział poszcególnych rekomendacji w liczbie opinii
    2) histogram czestotliwości wystąpień poszczególnych ocen (liczba gwiazdek)
 
