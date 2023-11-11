// Dados globais
let globalData = [];

// Função para ler o arquivo CSV e criar a lista
d3.csv("data/women-top-rated.csv").then(function(data) {
    globalData = data;
    createList(data);
});

// Função para filtrar e criar a lista de cards
function filterAndCreateList() {
    const selectedMaterials = Array.from(document.querySelectorAll('.filter:checked')).map(checkbox => checkbox.value);
    const filteredData = globalData.filter(item => {
        // Se nenhum filtro estiver selecionado, mostra todos os itens
        if (selectedMaterials.length === 0) return true;

        // Conta quantos materiais selecionados estão presentes no item
        const countMaterialsInItem = selectedMaterials.reduce((count, material) => {
            return count + (item[material] ? 1 : 0);
        }, 0);

        // O item deve conter todos os materiais selecionados e somente eles
        return countMaterialsInItem === selectedMaterials.length && countMaterialsInItem === Object.keys(item).filter(key => key.match(/Polyester|Elastane|Viscose|Cotton|Polyamide/) && item[key]).length;
    });

    createList(filteredData);
}

// Adiciona event listener ao botão de aplicar filtros
document.getElementById('applyFilters').addEventListener('click', filterAndCreateList);

// Função createList
function createList(data) {
    const container = document.getElementById('list');
    container.innerHTML = ''; // Limpa a lista atual

    data.forEach(item => {
        const cardMarkup = createCardMarkup(item);
        container.insertAdjacentHTML('beforeend', cardMarkup);
    });
}

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


