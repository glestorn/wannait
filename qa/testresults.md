# Результаты тестирования (функциональные аспекты)
| ID | Название | Сценарий | Ожидаемый результат | Фактический результат | Оценка |
|---|---|---|---|---|---|
| ф1а  | Просмотр пользователем доступных станций (Интернет есть) | Зайти в приложение | Приложение отображает список станций | Данные не получены | Тест не пройден |  
| ф1б  | Просмотр пользователем доступных станций (Интернета нет)  | Зайти в приложение | Приложение сообщает об отсутствиии подлючения | Уведомление получено | Тест пройден |  
| ф2а  | Поиск нужных станций (интернета нет)  | Попытаться начать поиск (нажать на элемент интерфейса) | Выводится сообщение об отсутствии подключения | Уведомление получено | Тест пройден |  
| ф2б  | Поиск нужных станций (интернет есть)  | Перебрать все варианты из плана тестирования в окне поиска и нажать кнопку для отправки запроса | При любых выриантах выводятся станции, подходящие под запрос  | Данные не получены | Тест не пройден |  
| ф3а  | Приостановление воспроизведения  | Запустить воспроизведение, Приостановить воспроизведение | Воспроизведение будет приостановлено  | Невозможножно проверить из-за пункта ф3б  | Тест не пройден |  
| ф3б  | Продолжение воспроизведения | При приостановленом воспроизведения попытаться продолжить | Воспроизведение продолжится  | Данные не получены  | Тест не пройден |  
| ф3в  | Быстро переключать приостановить / продолжить | 1. Нажать приостановить<br>   2. Нажать продолжить<br>  3. Вернуться к шагу 1, пока не надоест<br> | Будет происходить вопроизведение фрагментов |Данные не получены | Тест не пройден |  
| ф4а  | Запись небольшого фрагмента (10 cек.) | 1. Нажать запись<br>  2. Подождать нужное время<br>  3. Закончить запись<br>  | В памяти будет успешно сохранён записываемый фрагмент  | Из-за ф3б невозможно проверить | Тест не пройден |  
| ф4б  | -//- (20, 40, 60, 120, 240 сек.)  | -//- | -//- |  Из-за ф3б невозможно проверить | Тест не пройден |  
| ф4в  | -//- (16 минут) | -//-  | -//- | Из-за ф3б невозможно проверить | Тест не пройден |  
| ф4г  | Быстро переключать запись / конец записи  | Повторять 1. 3. из предыдущего пункта много раз | В памяти будут успешно сохранены все записанные фрагменты | Из-за ф3б невозможно проверить | Тест не пройден |   
| ф4д  | Запрос на запись при отсутствии аудиопотока  | Нажать на запись при отсутствии аудиопотока | Получено уведомление об отсутствии аудиопотока | Уведомление получено | Тест пройден |   
| ф5а  | Прослушивание желаемой станции (подлючение есть) | прослушать хотя бы 5 минут станцию | Успешное прослушивание (без вылетов и так далее) | Аудипоток не воспроизводится | Тест не пройден |  
| ф5б  | Прослушивание желаемой станции (подлючения нет) | во время прослушивания станции отключить интернет | Уведомление об ошибке | Получено уведомление об ошибке | Тест пройден |  

# Результаты тестирования (нефункциональные аспекты)
## Удобство использования  
Как пользователь ios я имею проблемы при работе с приложением:
* не понятно, зачем нужна боковая панель  
* без прочтения всей документации не понятно поведение некоторых функций, например, почему поиск почему-то выдаёт историю поиска, а не помогает сформировать запрос, для того чтобы начать запись нужно открыть боковую панель, нажать на запись (никто не уведомляет сколько я могу ещё записывать).  
Для меня идеал выглядит примерно вот так.  
![идеал](https://www.sketchappsources.com/resources/source-image/apple-music-app-template.png)
## Время отклика  
Если подключение к интернету медленное, то это чувствуется при каждом нажатии на элементы GUI, которые этого подключения требуют.

