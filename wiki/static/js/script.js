$(document).ready(function(){

  
//    // Обработчик клика на изображения в карусели
//    $('.carousel-item img').click(function() {
//     // Проверяем, увеличено ли уже изображение
//     if ($(this).hasClass('enlarged')) {
//         // Если увеличено, возвращаем к исходному размеру
//         $(this).removeClass('enlarged');
//         $(this).css({
//             'transform': 'scale(1)',
//             'cursor': 'zoom-in',
//             'z-index': 'auto',
//             'position': 'static'
//         });
//     } else {
//         // Если не увеличено, увеличиваем и показываем поверх всего
//         $(this).addClass('enlarged');
//         $(this).css({
//             'cursor': 'zoom-out',
//             'position': 'fixed', // Фиксированное позиционирование
//             'top': '50%', // Центрируем по вертикали
//             'left': '50%', // Центрируем по горизонтали
//             'transform': 'translate(-50%, -50%) scale(1.5)', // Центрируем и масштабируем
//             'z-index': '1000', // Устанавливаем высокий z-index
//             'max-width': '90%', // Ограничиваем максимальную ширину
//             'max-height': '90%', // Ограничиваем максимальную высоту
//             'box-shadow': '0 0 20px rgba(0, 0, 0, 0.5)' // Добавляем тень для эффекта
//         });
//     }
// });




   // Добавляем оверлей в конец body
   $('body').append('<div id="img-overlay"></div>');

   $('.carousel-item img').click(function() {
       let imgSrc = $(this).attr('src'); // Получаем src изображения

       if ($('#img-overlay').is(':visible')) {
           // Если уже открыто — скрываем
           $('#img-overlay').fadeOut();
       } else {
           // Показываем оверлей с увеличенным изображением
           $('#img-overlay').html('<img src="' + imgSrc + '">').fadeIn();
       }
   });

   // Закрытие при клике на оверлей
   $(document).on('click', '#img-overlay', function() {
       $(this).fadeOut();
   });






});

