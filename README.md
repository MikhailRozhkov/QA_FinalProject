#Автотест на проверку API приложения яндекс.самокат, а также SQL-запрос для работы с БД

-Для запуска теста должны быть установлены пакеты pytest  requests 

-Запуск теста выполняется командой ytest в терминале Pycharm

-Также запуск теста может быть осуществлен по нажатию на зеленую стрелку возле теста

##Содержимое проекта включает в себя 5 основных файлов:
-Файл data.py содержит в себе тело запроса создания заказа

-Файл configuration.py содержит в себе все необходимые URL  пути запросов

-Файл send_requests.py содержит в себе запрос создания заказа и получения его трек-номера с его сохранением

-Файл order_tracking.py содержит в себе запрос на получение заказа по сохраненному треку и проверку кода ответа

-Файл SQL_Requests содержит в себе SQL-запросы для получения  списка логинов курьеров с количеством их заказов в статусе «В доставке» и тестирование статусов заказов

-Скриншот-подтверждение работы автотеста
