var adr = 'Иваново, ' + document.getElementById('address').innerHTML;

ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map('map', {
        center: [55.753994, 37.622093],
        zoom: 18
    });

    myMap.controls.remove('searchControl');
    myMap.controls.remove('trafficControl');
    myMap.controls.remove('typeSelector');
    myMap.controls.remove('fullscreenControl');
    // myMap.controls.remove('zoomControl');
    myMap.controls.remove('rulerControl');
    myMap.behaviors.disable(['scrollZoom']);

    // Поиск координат центра Нижнего Новгорода.
    ymaps.geocode(adr, {
        results: 1
    }).then(function (res) {
        // Выбираем первый результат геокодирования.
        var firstGeoObject = res.geoObjects.get(0),
            // Координаты геообъекта.
            coords = firstGeoObject.geometry.getCoordinates(),
            // Область видимости геообъекта.
            bounds = firstGeoObject.properties.get('boundedBy');

        firstGeoObject.options.set('preset', 'islands#darkBlueDotIconWithCaption');
        // Получаем строку с адресом и выводим в иконке геообъекта.
        firstGeoObject.properties.set('iconCaption', adr);

        // Добавляем первый найденный геообъект на карту.
        myMap.geoObjects.add(firstGeoObject);
        // Масштабируем карту на область видимости геообъекта.
        myMap.setBounds(bounds, {
            // Проверяем наличие тайлов на данном масштабе.
            checkZoomRange: true
        });
    });
}