## Telegram Bot API
Боты — специальные аккаунты в Telegram, созданные для того, чтобы автоматически обрабатывать и отправлять сообщения. 
Пользователи могут взаимодействовать с ботами при помощи сообщений, отправляемых через обычные или групповые чаты. 
Логика бота контролируется при помощи HTTPS запросов к [API для ботов](https://api.telegram.org)

**НЕОФИЦИАЛЬНЫЙ** вольный перевод о том, что из себя представляют боты https://tlgrm.ru/docs/bots

### Полезные ссылки:

- Список интересных групп/каналов, а также список чатов для программистов: https://github.com/goq/telegram-list

- Заказать бота / стать исполнителем: https://t.me/tgram_jobs

- Официальная актуальная английская документация по методам API: https://core.telegram.org/bots/api

  (плохо с английским - идём за переводчиком http://translate.google.com)

- Текстовые уроки "Пишем бота для Telegram на языке Python" с использованием библиотеки [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI):

 https://groosha.gitbooks.io/telegram-bot-lessons/content/

- Текстовые уроки "Асинхронный Telegram бот на языке Python 3" с использованием библиотеки [aiogram](https://github.com/aiogram/aiogram):

 https://surik00.gitbooks.io/aiogram-lessons/content/
 
- [Реализация реферальной системы на Python с pyTelegramBotApi.](referral%20system%20example/)

- Деплой бота на различных бесплатных серверах: https://github.com/deploy-your-bot-everywhere/deploy-your-bot-everywhere

### Список популярных библиотек:
 + Python
   - [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - отлично подходит для начинающих, желающих понять основы работы с Bot API. Имеет подробную документацию (на английском языке) и обширное комьюнити.
   - [aiogram](https://github.com/aiogram/aiogram) - продвинутая библиотека для создания высокопроизводительных ботов. Библиотека постоянно обновляется и имеет крутые фишки, например [FSM](https://ru.wikipedia.org/wiki/Конечный_автомат), установку стандартного типа разметки и прочие полезные мелочи, полезные при разработке. Комьюнити библиотеки на данный момент небольшое.
   - [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
   - [twx.botapi](https://github.com/datamachine/twx.botapi)
   - [Telepot](https://github.com/nickoala/telepot)
   - [Telegram Bot Service](https://github.com/sourcesimian/txTelegramBot)
   - [telebot](https://github.com/yukuku/telebot)
 + JavaScript
   - [telegraf](https://github.com/telegraf/telegraf)
   - [node-telegram-bot-api](https://github.com/yagop/node-telegram-bot-api)
 + Java
   - [TelegramBots](https://github.com/rubenlagus/TelegramBots)
   - [Java Telegram Bot API](https://github.com/pengrad/java-telegram-bot-api)
 + Kotlin
   - [TelegramBotAPI](https://github.com/InsanusMokrassar/TelegramBotAPI) - не самая простая библиотека, использует объектно-ориентированный подход
 + PHP
   - [PHP Telegram Bot](https://github.com/php-telegram-bot/core)
 + C#
   - [Telegram.bot](https://github.com/TelegramBots/Telegram.Bot)
 + Ruby
   - [TelegramBot](https://github.com/eljojo/telegram_bot)
 + Go
   - [tgbotapi](https://github.com/go-telegram-bot-api/telegram-bot-api)
 + Lua
   - [lua-telegram-bot](https://github.com/cosmonawt/lua-telegram-bot)
 + Haskell
   - [haskell-telegram-api](https://github.com/klappvisor/haskell-telegram-api)


---

## ЧаВо

**Q:** Могу ли я посмотреть список всех пользователей канала?

**A:** Нет, если пользователей более 200

_

**Q:** Где захостить бота?

**A:** Бесплатно можно на Heroku, есть [инструкция](https://github.com/Kylmakalle/heroku-telegram-bot).
Более удобный способ - купить VPS \(Virtual Private Server\). Это виртуальная машина, на которой можно запустить бота ровно так же, как и на своём компьтере.

Список некоторых хостинг-провайдеров:
- [OVH](https://www.ovh.ie/)
- [DigitalOcean](https://www.digitalocean.com/)
- [Aruba](https://www.arubacloud.com/)
- [Vultr](https://www.vultr.com/)
- [Hetzner](https://www.hetzner.com/cloud)

**Q:** Как сделать, чтобы бот _ждал_ от пользователя следующее сообщение?

**A:** Используйте FSM (машины состояний). В некоторых библиотеках эта возможность уже встроена: [пример aiogram](https://github.com/aiogram/aiogram/blob/dfcc59d349e5387ff59ead32bd8f20d4ae064568/examples/finite_state_machine_example.py)

_

**Q:** Как хранить данные от пользователей?

**A:** Для долгосрочного хранения есть базы данных. Скорее всего, вашему небольшому проекту хватит мощностей SQLite. Если же проект подразумевает подключение к БД с разных ресурсов - взгляните на MySQL и PostgreSQL.


---


### Особенности работы с Bot API

##### В этом разделе описаны различные хитрости и неочевидные способы работы с Bot API, которые помогут вам упростить разработку или восполнить какое-либо ограничение в API.

#### Отправка Фото с большой подписью

Ранее этот способ использовался из-за ограничения подписи к фото в 200 символов, на данный момент лимит составляет 1024 символа. Если вам этого всё ещё мало или хотите разместить фото под текстом, то вы можете воспользоваться _предпросмотром_ ссылки. Делается это путем гиперссылки, где в качестве текста ссылки будет скрытый символ (`parse_mode=HTML`):
```HTML
"​​<a href="ссылка_на_картинку">&#8203;</a>
Lorem ipsum dolor sit amet..."
```
![](http://telegra.ph/file/ef107beda6880867f0348.png)

#### Бесплатный хостинг картинок
POST HTTP запрос `http://telegra.ph/upload`

Поддерживаемые типы медиафайлов:
`image/gif, image/jpeg, image/jpg, image/png, video/mp4, video/ogg, video/mpeg`

**Примеры:**
- Python

```python
import requests


with open('/Users/python273/Desktop/123345.jpeg', 'rb') as f:
    print(
        requests.post(
            'https://telegra.ph/upload',
            files={'file': ('file', f, 'image/jpeg')}
        ).json()
    )
```

#### Убираем часики на inline-кнопках
![](http://telegra.ph/file/b61e25a0a3f81f157eecf.png)

Причина возникновения этих _часиков_ - ожидание Телеграмом ответа от бота после нажатия пользователем на кнопку. Чтобы эти часики не зависали, после обработки нажатия нужно вызвать метод [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery)


---


## Валидация callback data

Telegram не привязывает данные в inline кнопках к чату и message_id, что позволяет клиентам не только подсматривать, 
но и подменять их.

Подмена данных может помешать корректной работе бота, поэтому разработчик должен озаботиться валидацией данных в кнопках.

Для наглядности рассмотрим пример с абстрактным ботом для проведения конкурсов

```
Пользователь создает конкурс, бот публикует сообщение с кнопкой "Участвовать" в канал.

В кнопках data представлена в незамысловатом виде: "id:{contest_id}:{action}". Таким образом, в кнопке "Участвовать" мы видим 
"id:5:participate".

Давайте отправим боту "id:6:participate", то есть увеличим id конкурса на 1. В ответ получаем всплывающее сообщение 
"Вы успешно зарегистрированы". Пока ничего критичного, но мы смогли зарегистрироваться в другом конкурсе.

Бот довольно молодой, в нем явно не больше 100 конкурсов. Отправим "id:1337:participate", в ответ получаем сообщение "Конкурс завершен или удален", а кнопка "Участвовать" удалена.

Дело в том, что при нажатии на кнопку "Участвовать" бот вычленяет id конкурса из data и пытается получить информацию о нем из БД, но
конкурса с id 1337 нет, потому мы получили такое сообщение. А чтобы отсечь остальные "бесполезные" запросы, бот удаляет клавиатуру. 
Вот мы испортили чей-то конкурс.

Давайте пойдем дальше и сами создадим конкурс. Бот публикует сообщение в наш канал, а также посылает мне сообщение с кнопками для управления конкурсом.
Одна из них "Удалить конкурс", data в ней "id:7:delete". Что если отправить боту "id:5:delete" ? Сегодня нам везет и мы получаем всплывающее сообщение "Конкурс успешно удален", а сообщение в первом канале исчезает.

Оказывается, бот не сверяет user_id отправителя и user_id создателя, поэтому все конкурсы оказались удалены :)
```

### Что делать?

#### Всегда проверяйте возможность пользователя совершать те или иные действия

В примере выше бот не проверял возможность пользователя удалить конкурс, что позволило удалить его любому желающему.
Не стоит надеяться на то, что сообщение отправлено лично.

#### Прячьте данные

Вы можете создавать рандомный ключ для каждой кнопки, по нему в БД класть необходимые данные, а сам ключ помещать в кнопку. 
Таким образом структура данных становится неизвестной для злоумышленника.

#### Привязывайте данные к чату и message_id

Сделайте невозможным выполнение логики определенной data в другом чате и сообщении

#### 

### Лимиты Telegram Bot API

 + Сообщения:
   - При отправке сообщений внутри определенного чата избегайте отправки более одного сообщения в секунду. Telegram может разрешить короткие всплески, которые превышают этот предел, но в итоге вы начнете получать 429 ошибку.

   - Если вы отправляете массовые уведомления нескольким пользователям, API не будет разрешать более 30 сообщений в секунду или около того. Рассмотрите возможность распространения уведомлений на большие интервалы в 8-12 часов для достижения наилучших результатов.
   
   - Ваш бот не сможет редактировать посты других пользователей на каналах старше 48 часов

   - Также обратите внимание, что ваш бот не сможет отправлять более 20 сообщений в минуту в одну группу.
 + Файлы:
 	- Максимальный размер файла для скачивания 20 MB.
  
   -  Максимальный размер файла для отправки 50 MB.

---


## Telegram client API (он же MTProto, он же tgcli)
Клиентское API телеграма - это API позволяющее вам выполнять автоматизированные действия от лица клиента.
Иными словами, всё, что может делать пользователь в телеграме, можно запрограммировать на tgcli \(получить всю историю сообщений в группе,
получить список всех пользователей группы, сделать поиск в группе по словам, взаимодействовать с ботами и [т.д и т.п](http://stek29.rocks/tl-schema/latest/)\).
Так как Telegram client api предполагает написание скриптов на tl \(поверьте, вы не хотите на нём [писать](https://tlgrm.ru/docs/mtproto/TL)\), то получили распространение обёртки над tgcli для разных языков.


### Список популярных клиентских библиотек:
+ Python:
  - [Telethon](https://github.com/LonamiWebs/Telethon)
  - [pyrogram](https://github.com/pyrogram/pyrogram)
+ JavaScript:
  - [telegram-mtproto](https://github.com/zerobias/telegram-mtproto)
+ Rust:
  - [Vail](https://github.com/JuanPotato/Vail)
  - [mtproto-rs](https://github.com/Connicpu/mtproto-rs)
+ PHP:
  - [MadelineProto](https://github.com/danog/MadelineProto)
+ Kotlin:
  - [kotlogram](https://github.com/badoualy/kotlogram)
+ C:
  - [tg](https://github.com/vysheng/tg)
  - [tdcli](https://bitbucket.org/vysheng/tdcli)  
+ Elixir:
  - [1664390](https://gitlab.com/snippets/1664390)
  - [telegram-mt-elixir](https://github.com/Fnux/telegram-mt-elixir)
  - [telegram-tl-elixir](https://github.com/Fnux/telegram-tl-elixir)
+ C#:
  - [TLSharp](https://github.com/sochix/TLSharp)
+ Go:
  - [mtproto](https://github.com/sdidyk/mtproto)
