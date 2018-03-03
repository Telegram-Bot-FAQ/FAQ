# FAQ
Русскоязычный краудсорсинговый проект помощи начинающим разработчикам Telegram ботов
## tgcli(он же MTProto, он же клиентское api)
Клиентское API телеграма - это API позволяющее вам выполнять автоматизированные действия от лица клиента.
Иными словами, всё, что может делать юзер в телеграме, можно запрограммировать на tgcli(получить всю историю группы,
получить всех пользователей группы, сделать поиск в группе по словам, взаимодействовать с ботом и [т.д и т.п](http://stek29.rocks/tl-schema/latest/)).
Так как Telegram client api предполагает написание скриптов на tl(поверьте, вы не хотите на нём [писать](https://tlgrm.ru/docs/mtproto/TL)), то получили распространение обёртки над tgcli для разных языков.
Их список можно увидеть ниже.
### список tgcli библиотек:
Python: [Telethon](https://github.com/LonamiWebs/Telethon) and [pyrogram](https://github.com/pyrogram/pyrogram);  
Rust: [Vail](https://github.com/JuanPotato/Vail) and [mtproto-rs](https://github.com/Connicpu/mtproto-rs);  
PHP: [MadelineProto](https://github.com/danog/MadelineProto);  
Kotlin: [kotlogram](https://github.com/badoualy/kotlogram);  
JavaScript: [telegram-mtproto](https://github.com/zerobias/telegram-mtproto);  
C: [tg](https://github.com/vysheng/tg) and [tdcli](https://bitbucket.org/vysheng/tdcli);  
Elixir: [1664390](https://gitlab.com/snippets/1664390) and [telegram-mt-elixir](https://github.com/Fnux/telegram-mt-elixir) and  [telegram-tl-elixir](https://github.com/Fnux/telegram-tl-elixir);  
C#: [unigram](https://github.com/unigramdev/unigram);  
Go : [mtproto](https://github.com/sdidyk/mtproto);  
Список дополняется...  
