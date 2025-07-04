# Проект "Пурга". Очистка аудио

Для того, чтобы имеющийся набор записей вещания радиостанции превратить в датасет, нужно проделать два шага:
1) обрезать записи так, чтобы осталась чукотская речь (на основе информации о времени начала и продолжительности программы на чукотском)
2) произвести очистку от шума, фоновой музыки и других неголосовых элементов

Ниже приведены подробные объяснения насчёт того, как осуществить каждый из двух пунктов, используя наш проект.

## 1) Обрезка записей

Для обрезки записей пошагово следуйте приведённой ниже инструкции.

### Установлен ли Python?

1. Откройте **Командную строку**:
   - Нажмите клавиши `Win + R`
   - Введите `cmd`
   - Нажмите Enter

2. В открывшемся окне запустите команду:
   ```
   python --version
   ```

- Если увидите в выводе `Python 3.9.22` (или с другими цифрами, но важно, чтобы была 3.<число больше 8>.<что-то>), Python необходимой версии установлен!
- Если видите ошибку или "не является внутренней командой", Python не установлен.
- Если после первой точки вывелась цифра меньше 9, то также необходимо установить Python более новой версии (но установка будет такая же, как приведено ниже).

### Установка Python

1. Перейдите по ссылке: https://www.python.org/downloads/
2. Нажмите желтую кнопку "Download Python 3.13.5" (позже могут появиться другие цифры, все равно нажимайте)
3. Запустите скачанный файл
4. Поставьте галочку "Add Python to PATH" внизу окна установщика
5. Нажмите "Install Now"
6. Дождитесь завершения установки

### Скачиваем проект

1. Откройте страницу проекта на GitHub
2. Нажмите зеленую кнопку **"Code"**
3. Выберите **"Download ZIP"**
4. Распакуйте скачанный архив в удобную папку

### Переходим в папку проекта

1. В командной строке введите `cd ` (с пробелом после cd)
2. Перетащите папку проекта в окно командной строки
3. Нажмите Enter

Пример:
```
cd C:\Users\имя\Desktop\purga-radio-processor
```

### Запуск программы

В командной строке запустите команду:
```
python -m src.news_cutter.main "\\RECORDER\Logger" "\\RECORDER\Logger_cutted"
```
Если для работы с вашими записями поменялась папка, замените `\\RECORDER\Logger` на путь к нужной папке с аудио. Также, если не подходит `\\RECORDER\Logger_cutted` как папка, в которую будут сохраняться результаты обработки аудио, вместо неё укажите подходящий путь.

Если оставить пути к папкам, как выше, то получится так:
- Программа обработает тестовые из папки `\\RECORDER\Logger`
- Результаты появятся в папке `\\RECORDER\Logger_cutted`
- В папке `logs` в папке проекта будут файлы с информацией о работе программы

После запуска команды зайдите в папку `logs` и откройте файл `app`. Если в файле написано "ffmpeg не найден", необходимо установить "ffmpeg":
1. Откройте ссылку: https://www.gyan.dev/ffmpeg/builds/
2. Найдите раздел **"release builds"**
3. Нажмите на ссылку **"ffmpeg-release-essentials.zip"**
4. Найдите скачанный файл
5. Щелкните правой кнопкой мыши на архиве и выберите **"Извлечь все..."**
7. Нажмите **"Извлечь"**
8. Откройте распакованную папку, зайдите в папку **"bin"**, там будет файл `ffmpeg.exe`
9. Выделите его, нажмите `Ctrl + C`, откройте папку скачанного проекта и нажмите `Ctrl + V`, таким образом положив файл ffmpeg.exe в корневую папку проекта (там же, где и LICENSE, delta.md и README.md)
```
purga-radio-processor
  dummy_data
  src
  LICENSE
  ffmpeg.exe <- тут должен быть файл
  ...
```
После этого можете возвращаться к пункту с запуском программы и запустить команду заново - для повторного запуска больше других действий не нужно.

Если столкнетесь с другими проблемами, не стесняйтесь писать нам!

## 2) Очистка аудио

### Скачивание ноутбука с кодом

Скачайте этот файл с расширением .ipynb: https://github.com/Octopupu5/purga-radio-processor/blob/main/src/preprocess/preprocess.ipynb.

### Настройка Google Colab

Пройдите по ссылке https://colab.research.google.com. Должно автоматически открыться окно "Открыть блокнот" (если нет, то откройте самостоятельно: Файл -> Открыть блокнот). Нажмите Загрузить -> Выберите файл -> выберите скачанный на предыдущем шаге файл с кодом.

В боковом меню слева нажмите на самый нижний значок папки (называется Файлы), кликните правой кнопкой мыши по открывшемуся пространству (нужно немного подождать) -> Создать папку -> введите название `content`.

Кликните правой кнопкой мыши по созданной папке `content` -> Создать папку -> введите название `input_folder`.

Кликните правой кнопкой мыши по созданной подпапке `content/input_folder` -> Загрузить -> загрузите туда все аудиофайлы, которые необходимо обрезать.

### Выполнение кода

Открытый файл состоит из четырёх ячеек с кодом. При наведении мышки на ячейку в левой части ячейки появляется круглая кнопка Play. Чтобы запустить ячейку, нужно нажать на неё.

Для обработки аудиофайлов, загруженных в папку `content/input_folder`, нужно запустить первые две ячейки и дождаться окончания их выполнения - когда появятся зелёные галочки слева от ячеек. (Можно нажать Play на первой, не ждать выполнения и сразу нажать Play на второй и только потом ждать.) После выполнения первых двух ячеек в папке `content/cleaned_audio` будут лежать обработанные аудиофайлы.

Последние две ячейки применимы для датасета с радиопередачами по финансовой грамотности. Если их запустить, то созданные файлы будут переименованы по формату `How_to_save_money_{file_num}.wav`, а также в файл `audio_metadata.csv` запишутся метаданные о названии файла, языке, поле говорящего, продолжительности, теме передачи и дате обработки.

Не забудьте скачать созданные файлы - после завершения сессии в Google Colab они удалятся! Чтобы скачать файл, нужно нажать на него правой кнопкой мыши -> Скачать.
