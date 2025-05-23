# purga-radio-processor

## Чукотское радио
Основная задача — получить данные с чукотской речью. Шаги примерно такие:
1. написать для сисадмина радио скрипт, который будет брать из записанных эфиров фиксированные куски

    Внутри передачи бывает, что играет музыка в секунды, когда диктор молчит, переводит дух. Речь без музыки - может, изредка бывает, но скорее редко.

    Запись дня начинается с 00:00. Новости на чукотском языке выходят ежедневно по будним дням, в 13:00 и 18:00.
    Длительность ориентировочно 5-7 минут. Когда не было программ не вспомнят.

    Что сейчас делать с этими кусками: можно вытащить первые 15 минут из этих файлов (13 и 18) и потом уже у себя экспериментировать с более точным вырезанием.

    Куски - mp3, 10минутные отрывки с 13:00 и с 18:00 из всех будних дней, которые есть. Окна времени, когда выходят передачи на чукотском - это всегда фиксированное время (бывало, что эфира не было, но они не записывали эту информацию, они не знают, когда не было). И просим это загрузить на яндексдиск. Стоит сделать пробный прогон, чтоб всё быстро порезалось и загрузилось. Они увидят, что это не страшно, что работает. И можно будет обкачивать всё, что есть. Важно, чтоб там всё необходимое само инсталлировалось. И инструкцию написать короткую, понятную. Это задача ещё на одного.

    Логировать ли процесс - да, можно не подбробный, но да, давайте знать, что обработалось, а что нет.

2. убрать фоновую музыку с полученных файлов + обработать куски, оставив только чукотскую речь

    Output - Аудиофайлы только с чукотским без фоновой музыки. И метаинформация (в какой день, в какое время сказано).

    А потом, чтоб у них лишнего не запускать, будем чистить. Начало можно ловить по фразе "Новости на радио Пурга". Конец можно ловить по музыке после чукотской речи (когда получим кусочки, посмотрим, разная она или одинаковая). Ещё может упростить дело то, что у них всего около 3х дикторов, то есть по спикеру чукотский (в теории) может ловиться. И от фоновой музыки чистить. Начать решать эту задачу можно будет после того, как мы запустим пробный вариант и возьмём у них чуть-чуть аудио. Это ещё один человек.

    В названии новых вырезанных кусков нужны день и время.

3. составить датасет вида (аудио + мета)
    Крайне желательна дополнительная информация в имени файла или отдельном текстовом файле (ведущий, тема выпуска и подобное), но вы её не вытащите быстро. Вы вытаскиваете у них новости. Тема одна - новости, подробнее не объявляют.

    Если в итоге получим датасет с "грязными" аудио чукотского — уже хорошо, уже потянет.


4. обучить генеративную модель на полученных данных (чтобы просто генерила что-то чукотоподобное) (**со звездочкой**)
    
    Если не получится, есть альтернатива: есть корпус зашумленных размеченных аудио так же на чукотском, обучить asr на нем

### Информация об устройстве и людях:

Компьютер OC  Windows 10 Pro, файлы на отдельном жестком диске объемом 3,5 Тб. У них есть знакомый, который очень хорошо знаком с питоном, но он может быть в разъездах. Мы общаемся с сисадмином - мистер N. Считает, что способен сам запустить, если дать инструкцию.
Готовые вырезанные кусочки загрузить на яндексдиск.

### О данных
У них есть отдельный компьютер, на котором отдельный диск с папками, т.н. логи эфира в хорошем качестве и с FM. В хорошем качестве пишутся в *.wav, c FM в *mp3. Скрин структуры папок имеется. Название папок по датам, название файлов по часам.
![alt text](/pics/struct1.jpg)
![alt text](/pics/struct2.jpg)
`В этой папке только до 12 дня, потому что он отправил это как раз в тот день, другое ещё не было записано)`


Есть ощущение, что данных может быть достаточно, чтоб обучить нейросеть говорению. Без этапа распознавания. Учимся по кусочку аудио предсказывать следующий.

Или можно побаловаться с распознаванием речи без эталонной расшифровки. Так делают, статьи есть про это.

#### На случай, если коммуникация с Пургой не сложится.
Есть корпус чукотский https://chuklang.ru/corpus. Вытащить из него пары аудио-предложение. Обучить на этих очень шумных данных ASR, расшифровать этой моделью кусочки по фин.грамотности. И либо вздохнуть, либо удивиться.

## Side quest (as i understood)
Вот записи нескольких передач по фин.грамотности (всё, что у меня есть) - (за архивом с файлами -> @heritagejazztime / @@bnnnch / @tbkazak)

Да, они на фоне музыки (кажется, она редко меняется). Нужно убрать музыку, не повредив слова. (Надо будет ещё мне дать послушать, а то чукотская речь может быть непривычной и вы можете с музыкой стереть что-нибудь нужное.) Нужно убрать русский текст в начале и в конце (ну и заголовок, который всегда один и тот же).


А. Этих выпусков всего 20. Больше не существует (то есть аналогичные из эфиров вырезать не будем). Только из этих чукотскую речь надо вытащить.
На самом деле 1-2 записи я готова с коллегами расшифровать, чтоб всё же не zero-shot был.

Это выглядит как задача для одного.
