// static/js/map.js

ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map('map', {
        center: [55.751574, 37.573856], // Координаты центра карты
        zoom: 10 // Уровень масштабирования
    });

    // Добавление метки
    var myPlacemark = new ymaps.Placemark([55.751574, 37.573856], {
        hintContent: 'Москва!',
        balloonContent: 'Столица России'
    });

    myMap.geoObjects.add(myPlacemark);
}
