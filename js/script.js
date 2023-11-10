// Função para ler o arquivo CSV e criar a lista
d3.csv("data/women-top-rated.csv").then(function(data) {
    // Aqui, 'data' é um array de objetos, onde cada objeto representa uma linha do CSV
    createList(data);
});

// Função para criar o markup de um card
function createCardMarkup(item) {
    let materialsInfo = '';
    if (item.Polyester) materialsInfo += `Polyester: ${item.Polyester}%, `;
    if (item.Elastane) materialsInfo += `Elastane: ${item.Elastane}%, `;
    if (item.Viscose) materialsInfo += `Viscose: ${item.Viscose}%, `;
    if (item.Cotton) materialsInfo += `Cotton: ${item.Cotton}%, `;
    if (item.Polyamide) materialsInfo += `Polyamide: ${item.Polyamide}%`;

    // Removendo a última vírgula e espaço, se houver
    materialsInfo = materialsInfo.replace(/, $/, '');

    return `
        <a href="${item.Link}" class="card-link" target="_blank">
            <div class="card">
                <img src="${item.Image}" class="card-img-top" alt="Image of ${item.Title}">
                <div class="card-body">
                    <h5 class="card-title">${item.Title}</h5>
                    <p class="card-text">Price: ${item.Price}</p>
                    <p class="card-text">${materialsInfo}</p>
                </div>
            </div>
        </a>
    `;
}

// Função para criar a lista de cards
function createList(data) {
    const container = document.getElementById('list'); // Seleciona o elemento container existente

    data.forEach(item => {
        // Gera o markup para o card e insere no container
        const cardMarkup = createCardMarkup(item);
        container.insertAdjacentHTML('beforeend', cardMarkup);
    });
}

