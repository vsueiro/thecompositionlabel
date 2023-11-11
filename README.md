# fast-fashion-composition

Outlining basic repo structure:

```
scraper/
    links/
        2023-11-10-12:00:00.csv
        2023-11-09-12:00:00.csv
        2023-11-08-12:00:00.csv
        …
    items/
        123456789.csv
        987654321.csv
        123987621.csv
        …
    errors/
        missing-items.csv

    get-item-links.py
    get-items-details.py
    get-item-details.py
    build-item-list.py

data/
    women-top-rated.csv
```

## get-item-links.py

Pega links de todos os produtos da categoria atual, página por página, e salva como `links/{timestamp}.csv`
Por fim, roda get-items-details.py

## get-items-details.py

Pega os links mais recentes, aleatoriza a ordem, e roda o `get-item-details.py` para cada um deles. Por fim, roda `build-item-list.py`

## get-item-details.py

Pega detalhes de um item específico (a partir da URL) e salva em um CSV individual como `items/{ID}.csv`

## build-item-list.py

Pega os links mais recentes, para cada um, acessa os detalhes do produto e junta num CSV único. Se não achar os detalhes, lista o produto em `data/errors/missing-items.csv`
