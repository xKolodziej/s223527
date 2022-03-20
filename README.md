# s223527

## Analiza struktury opinii w serwisie [Ceneo.pl]

|Składowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product-review|Review|
|identyfikator_opinii|\[data-entry-id]|review_id|
|autor|span.user-post__author-name|author|
|rekomendacja|span.user-post__author-recomendation > em|recommenadtion|
|liczba_gwiazdek|span.user-post__score-count|stars|
|tresc|div.user-post__text|content|
|data_wystawienia|div.user-post__published > time:nth-child(1)\[datetime\]|[ublish_date|
|data_zakupu|div.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|
|dla_ilu_przydatna||useful|
|dla_ilu_nieprzydatna||useless|
|lista_zalet|review-feature__title--positives > review-feature__item|Positives_list|
|lista_wad|review-feature__title--negatives > review-feature__item|Negatives_list|
||||
||||