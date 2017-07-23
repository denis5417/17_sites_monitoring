# Утилита для проверки сайтов

Утилита для проверки состояния сайтов. На входе - текстовый файл с URL адресами для проверки. На выходе - статус каждого сайта по результатам следующих проверок:

1. Сервер отвечает на запрос статусом HTTP 200;
2. Доменное имя сайта проплачено как минимум на 1 месяц вперед.

# Установка и использование

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и библиотек [python-whois](https://bitbucket.org/richardpenman/pywhois) и 
[requests](https://bitbucket.org/richardpenman/pywhois).

Установка библиотек:

```#!bash
pip install -r requirements.txt
```

Запуск на Linux:

```#!bash
$ python3 check_sites_health.py <path_to_file_with_urls>
http://www.koob.ru/philosophy/ | Good. Server is responding 200. | Domain extended enough.
http://www.e-puzzle.ru | Good. Server is responding 200. | Domain extended enough.
http://www.lib.ru/FILOSOF/ | Good. Server is responding 200. | Domain extended enough.
http://www.imwerden.de | Good. Server is responding 200. | !DOMAIN DOESN'T EXTENDED ENOUGH!
http://www.vehi.net | Good. Server is responding 200. | Domain extended enough.
http://www.lib.com.ua/9/0.html | Good. Server is responding 200. | !DOMAIN DOESN'T EXTENDED ENOUGH!
http://www.litportal.ru/index.html | Good. Server is responding 200. | Domain extended enough.
http://ihtik.lib.ru | !SOMETHING WRONG! | Domain extended enough.
http://imwerden.de/cat/modules.php | Good. Server is responding 200. | !DOMAIN DOESN'T EXTENDED ENOUGH!
http://www.litportal.ru/index.html | Good. Server is responding 200. | Domain extended enough.
http://koapp.narod.ru/hudlit/phylos/catalog.htm | Good. Server is responding 200. | Domain extended enough.
http://kulichki.com/inkwell/noframes/filosofy.htm | Good. Server is responding 200. | Domain extended enough.
http://psylib.kiev.ua | !SOMETHING WRONG! | !DOMAIN DOESN'T EXTENDED ENOUGH!
http://www.magister.msk.ru/library/philos/philos.htm | Good. Server is responding 200. | Domain extended enough.
http://abuss.narod.ru/Biblio/philo | !SOMETHING WRONG! | Domain extended enough.
http://filosof.historic.ru/books.shtml | Good. Server is responding 200. | Domain extended enough.
http://philosophy.ru | Good. Server is responding 200. | Domain extended enough.
http://elenakosilova.narod.ru/uhref.html | !SOMETHING WRONG! | Domain extended enough.
http://humanities.edu.ru/db/sect/222 | !SOMETHING WRONG! | !DOMAIN DOESN'T EXTENDED ENOUGH!
http://sovphil.narod.ru/catalog.html | Good. Server is responding 200. | Domain extended enough.
```
[Пример файла](https://pastebin.com/raw/fNs0Appd)

Вывод в файл:

```#!bash
$ python3 check_sites_health.py <path_to_file_with_urls> > <path_to_output_file>
```
Справка:
```#!bash
$ python3 check_sites_health.py -h
usage: check_sites_health.py [-h] filepath

positional arguments:
  filepath    Path to file with URLs

optional arguments:
  -h, --help  show this help message and exit
```

Запуск на Windows происходит аналогично.

# Цель проекта

Этот код написан в образовательных целях. Тренировачный курс для веб девелоперов - [DEVMAN.org](https://devman.org)
