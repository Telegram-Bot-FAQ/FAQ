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

### Список популярных библиотек:
 + Python
   - [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - отлично подходит для начинающих, желающих понять основы работы с Bot API. Имеет подробную документацию (на английском языке) и обширную аудиторию.
   - [aiogram](https://github.com/aiogram/aiogram) - продвинутая библиотека для создания высокопроизводительных ботов. Библиотека постоянно обновляется и имеет крутые фишки, например [FSM](https://ru.wikipedia.org/wiki/Конечный_автомат), установку стандартного типа разметки и прочие полезные мелочи, полезные при разработке. Аудитория пользователей библиотеки на данный момент небольшая.
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
Самый дешевый вариант - Aruba, просят 1 евро в месяц, есть 2 бесплатных месяца: https://www.arubacloud.com/free-trial.aspx

_

**Q:** Как сделать, чтобы бот _ждал_ от пользователя следующее сообщение?

**A:** Используйте FSM (машины состояний). В некоторых библиотеках эта возможность уже встроена: [пример aiogram](https://github.com/aiogram/aiogram/blob/dfcc59d349e5387ff59ead32bd8f20d4ae064568/examples/finite_state_machine_example.py)

_

**Q:** Как хранить данные от пользователей?

**A:** Для долгосрочного хранения есть базы данных. Скорее всего, вашему небольшому проекту хватит мощностей SQLite. Если же проект подразумевает подключение к БД с разных ресурсов - взгляните на MySQL и PostgreSQL.


---


### Особенности работы с Bot API

##### В этом разделе описаны различные хитрости и неочевидные способы работы с Bot API, которые помогут вам упростить разработку или восполнить какое-либо ограничение в API.

#### Отправка Фото с большой подписью

Технически Bot API не позволяет отправлять фото с подписью более 200 символов. Но мы можем воспользоваться тем, что ссылки на изображения образуют _предпросмотр_. Этим можно воспользоваться оставив в скрытом HTML символе ссылку на картинку \(главное не забыть указать разметку HTML в параметре `parse_mode`\)
```HTML
"​​<a href="ссылка_на_картинку">&#8203;</a>
Lorem ipsum dolor sit amet..."
```
![](http://telegra.ph/file/ef107beda6880867f0348.png)

#### Бесплатный хостинг картинок
POST HTTP запрос `http://telegra.ph/upload`

Поддерживаемые типы медиафайлов:
`image/gif, image/jpeg, image/jpg, image/png, video/mp4`

**Примеры:**
- Python

```python
import requests


with open('/Users/python273/Desktop/123345.jpeg', 'rb') as f:
    print(
        requests.post(
            'http://telegra.ph/upload',
            files={'file': ('file', f, 'image/jpeg')}
        ).json()
    )
```

#### Убираем часики на inline-кнопках
![](http://telegra.ph/file/b61e25a0a3f81f157eecf.png)

Причина возникновения этих _часиков_ - ожидание Телеграмом ответа от бота после нажатия пользователем на кнопку. Чтобы эти часики не зависали, после обработки нажатия нужно вызвать метод [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery)


---


### Лимиты Telegram Bot API

 + Сообщения:
   - При отправке сообщений внутри определенного чата избегайте отправки более одного сообщения в секунду. Telegram может разрешить короткие всплески, которые превышают этот предел, но в итоге вы начнете получать 429 ошибку.

   - Если вы отправляете массовые уведомления нескольким пользователям, API не будет разрешать более 30 сообщений в секунду или около того. Рассмотрите возможность распространения уведомлений на большие интервалы в 8-12 часов для достижения наилучших результатов.

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
  - [unigram](https://github.com/unigramdev/unigram)
+ Go:
  - [mtproto](https://github.com/sdidyk/mtproto)
