function openModal() {
  // Reset values of input fields and textarea

  // Show the modal
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
}

function openModal2() {
  // Reset values of input fields and textarea
  document.getElementById("booking-date2").value = "2023-12-21";  // Set the default value or an empty string
  document.getElementById("booking-time2").value = "11:00";  // Set the default value or an empty string
  document.getElementById("booking-guests2").value = "1";  // Set the default value or an empty string
  document.getElementById("booking-comments2").value = "";  // Clear the textarea

  // Show the modal
  var modal = document.getElementById("myModal2");
  modal.style.display = "block";
}

  // Show the modal
  var modal = document.getElementById("myModal");
  modal.style.display = "block";


  function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
  }
    function closeModal2() {
    var modal = document.getElementById("myModal2");
    modal.style.display = "none";
  }

  function confirmReservation() {
    closeModal();
}

  window.onclick = function(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };





document.addEventListener('DOMContentLoaded', function() {
    // Создаем объект для отслеживания нажатых кнопок
    let clickedPreferences = {};

    document.getElementById('text-container').addEventListener('click', function(event) {
        // Проверяем, что клик был совершен на элементе с классом 'preference-btn'
        if (event.target.classList.contains('preference-btn')) {
            const preference = event.target.getAttribute('data-preference');
            // Проверяем, была ли кнопка уже нажата
            if (!clickedPreferences[preference]) {
                // Если не нажата, то логируем и делаем ее активной
                console.log(preference);
                clickedPreferences[preference] = true; // Отмечаем кнопку как нажатую

                // Обновляем значение скрытого поля (если оно уже есть в DOM)
                const preferencesInput = document.getElementById('preferences-input');
                if (preferencesInput) {
                    preferencesInput.value = preference;
                }
                // Добавляем класс для визуального отображения активной кнопки
                event.target.classList.add('active');
            } else {
                // Если кнопка уже была нажата, выводим сообщение
                console.log(preference + ' уже было выбрано');
                // Опционально: убираем класс активности с кнопки
                event.target.classList.remove('active');
                // Удаляем выбор из объекта отслеживания
                delete clickedPreferences[preference];
            }
        }
    });
});



function like() {
  // Измените содержимое элемента с информацией
  document.getElementById('info').textContent = 'Вам понравилась эта статья.';
}

function dislike() {
  // Измените содержимое элемента с информацией
  document.getElementById('info').textContent = 'Вам не понравилась эта статья.';
}
document.getElementById('show-positive').addEventListener('click', function() {
    var retings = document.querySelectorAll('.grid-item');
    retings.forEach(function(reting) {
        if (reting.getAttribute('data-is-good') === 'true') {
            reting.style.display = ''; // Показываем положительный отзыв
        } else {
            reting.style.display = 'none'; // Скрываем отрицательный отзыв
        }
    });
});

document.getElementById('show-negative').addEventListener('click', function() {
    var retings = document.querySelectorAll('.grid-item');
    retings.forEach(function(reting) {
        if (reting.getAttribute('data-is-good') === 'false') {
            reting.style.display = ''; // Показываем отрицательный отзыв
        } else {
            reting.style.display = 'none'; // Скрываем положительный отзыв
        }
    });
});




function shareContent() {
  if (navigator.share) {
    navigator.share({
      title: 'Заголовок вашего контента',
      text: 'Описание вашего контента',
      url: window.location.href
    })
    .then(() => console.log('Успешно поделились'))
    .catch((error) => console.log('Ошибка при попытке поделиться', error));
  } else {
    // Здесь вы можете добавить фоллбэк для браузеров, не поддерживающих Web Share API
    alert('Ваш браузер не поддерживает функцию обмена');
  }
}