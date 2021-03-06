## Описание скриптов:
###  `script.sh`
- *Что делает* : Парсит лог файл и сохраняет информацию в `.csv` файлы в `results/bash`
- *Опции* : Можно указать путь к файлу с логами в качестве первого агрумента (`./script.sh <FILEPATH>`). По умолчанию берется файл `access.log` из корня репозитория.

###  `script.py`
- *Что делает* : Парсит лог файл и сохраняет информацию в `.csv` файлы в `results/python`. Имеет опцию конвертировать `.csv` файлы `.json` формат.
- *Флаги запуска* : 
    - `--json` - конвертирует файлы csv в json формат в директорию `results/python/json`
    - `--log_path <FILEPATH>` - можно указать свой лог файл. По умолчанию берется файл access.log из корня репозитория.

## Быстрый запуск:
### python
1. Положить файл лога в корень репозитория и назвать его `access.log`.
2. Зайти в директорию `src`
3. Выполнить команду `python3 script.py --json`. Файлы с результатами в папке `results/python`

### bash
1. Положить файл лога в корень репозитория и назвать его `access.log`.
2. Зайти в директорию `src`
3. Выполнить команду `./script.sh`. Файлы с результатами в папке `results/bash`

## Имена файлов c результатами по заданиям:
1. Задание 1 - `task_1.csv` - Общее количество запросов.
2. Задание 2 - `task_2.csv` - Общее количество запросов по типу.
3. Задание 3 - `task_3.csv` - Топ 10 самых частых запросов.
4. Задание 4 - `task_4.csv` - Топ 5 самых больших по размеру запросов c (4ХХ) ошибкой.
5. Задание 5 - `task_5.csv` - Топ 5 пользователей по количеству запросов c (5ХХ) ошибкой.
