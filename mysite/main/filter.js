const godFilter = document.getElementById('god-filter');
godFilter.addEventListener('change', filterModels);

function filterModels() {
    const selectedValue = godFilter.value;
    const models = document.getElementsByClassName('Aplikacija');

    for (let i = 0; i < models.length; i++) {
        const model = models[i];
        const god = model.getAttribute('aplikacija_AkGod');

        if (selectedValue && god !== selectedValue) {
            model.style.display = 'none';
        } else {
            model.style.display = '';
        }
    }
}