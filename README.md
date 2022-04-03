# s223527

## Analiza struktury opinii w serwisie [Ceneo.pl]

|Składowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product-review|Review|bs4.element.Tag|
|identyfikator_opinii|\["data-entry-id"]|review_id|str|
|autor|"span.user-post__author-name"|author|bs4.element.ResultSet|str|
|rekomendacja|"span.user-post__author-recomendation"> em|recommenadtion||
|liczba_gwiazdek|"span.user-post__score-count"|stars|float|
|tresc|"div.user-post__text"|content|str|
|data_wystawienia|div.user-post__published > time:nth-child(1)\[datetime\]|[publish_date|str|
|data_zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|str|
|dla_ilu_przydatna|span[id^=votes-yes]|useful|int|
|dla_ilu_nieprzydatna|span[id^=votes-no]|useless|int|
|lista_zalet|div.review-feature__title--positives > div.review-feature__item|Positives_list|str|
|lista_wad|div.review-feature__title--negatives > div.review-feature__item|Negatives_list|str|
||||
||||
## Etapy pracy nad projektem
- pobranie składowych pojedynczej opinii do niezaleznych zmiennych
- zapisanie składowych do pojedynczej opiinii do obiektu słownika (disctionary)
- pobranie wszystkich opinii z pojedynczej strony i zapisanie ich do listy słowników
- pobranie opinii o wszkazym produkcie i zapisanie ich do pliku