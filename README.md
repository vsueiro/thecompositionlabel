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

    get-all-items-links.py
    get-items-details.py
    build-all-items-list.py

data/
    women-top-rated.csv
```

## get-all-items-links.py

Pega links de todos os produtos da categoria atual, página por página, e salva como `links/{timestamp}.csv`

## get-items-details.py

Pega os links mais recentes, aleatoriza a ordem, e pega detalhes de alguns deles, salvando em `items/{ID}.csv`

## build-all-items-list.py

Pega os links mais recentes, para cada um, acessa os detalhes do produto e junta num CSV único. Se não achar os detalhes, lista o produto em `data/errors/missing-items.csv`
