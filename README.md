# FAQ
Русскоязычный краудсорсинговый проект помощи начинающим разработчикам Telegram ботов
## Telegram client API(он же MTProto, он же tgcli)
Клиентское API телеграма - это API позволяющее вам выполнять автоматизированные действия от лица клиента.
Иными словами, всё, что может делать юзер в телеграме, можно запрограммировать на tgcli(получить всю историю группы,
получить всех пользователей группы, сделать поиск в группе по словам, взаимодействовать с ботом и [т.д и т.п](http://stek29.rocks/tl-schema/latest/)).
Так как Telegram client api предполагает написание скриптов на tl(поверьте, вы не хотите на нём [писать](https://tlgrm.ru/docs/mtproto/TL)), то получили распространение обёртки над tgcli для разных языков.
Их список можно увидеть ниже.
### Список популярных библиотек:
+ Python:
  - [Telethon](https://github.com/LonamiWebs/Telethon)
  - [pyrogram](https://github.com/pyrogram/pyrogram)  
+ Rust: 
  - [Vail](https://github.com/JuanPotato/Vail)
  - [mtproto-rs](https://github.com/Connicpu/mtproto-rs)  
+ PHP: 
  - [MadelineProto](https://github.com/danog/MadelineProto)  
+ Kotlin: 
  - [kotlogram](https://github.com/badoualy/kotlogram)  
+ JavaScript: 
  - [telegraf](https://github.com/telegraf/telegraf)
  - [telegram-mtproto](https://github.com/zerobias/telegram-mtproto)  
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

## Telegram Bot API
### Список популярных библиотек:
+ Python
  - [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
  - [twx.botapi](https://github.com/datamachine/twx.botapi)
  - [Telepot](https://github.com/nickoala/telepot)
  - [Telegram Bot Service](https://github.com/sourcesimian/txTelegramBot)
  - [telebot](https://github.com/yukuku/telebot)
  - [aiogram](https://github.com/aiogram/aiogram)
+ Java
  - [TelegramBots](https://github.com/rubenlagus/TelegramBots)
+ C#
  - [Telegram.bot](https://github.com/TelegramBots/Telegram.Bot)
+ Ruby
  - [TelegramBot](https://github.com/eljojo/telegram_bot)
+ Go
  - [TBotAPI](https://github.com/mrd0ll4r/tbotapi)
+ Lua
  - [lua-telegram-bot](https://github.com/cosmonawt/lua-telegram-bot)
+ Haskell
  - [haskell-telegram-api](https://github.com/klappvisor/haskell-telegram-api)
+ JavaScript
  - [node-telegram-bot-api](https://github.com/yagop/node-telegram-bot-api)

### Лимиты Telegram Bot API

+ Сообщения:
  - При отправке сообщений внутри определенного чата избегайте отправки более одного сообщения в секунду. Telegram может разрешить короткие всплески, которые превышают этот предел, но в итоге вы начнете получать 429 ошибку.

  - Если вы отправляете массовые уведомления нескольким пользователям, API не будет разрешать более 30 сообщений в секунду или около того. Рассмотрите возможность распространения уведомлений на большие интервалы в 8-12 часов для достижения наилучших результатов.

  - Также обратите внимание, что ваш бот не сможет отправлять более 20 сообщений в минуту в одну группу.
+ Файлы:
	- Максимальный размер файла для скачивания 20 MB.
  - Максимальный размер файла для загрузки (отправки) 50 MB.

FAQ дополняется...  
