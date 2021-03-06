Встречайте Mailr
================
Мы будем говорить о новом webmail клиенте с открытыми исходниками.

Я уже лет семь использую gmail и в этот период несколько раз пытался уйти от него, но 
всегда возвращался. И что интересно, когда смотрел очередную альтернативу, то первое 
требование было -- цепочки писем по удобству сопоставимые с gmail.

Из примеров, которые зацепили:
 - Thunderbird__ и `Thunderbird Conversations`__;
 - Geary__ -- gmail-подобный десктопный клиент;
 - `fastmail.fm`__ -- платная почта, которая какое-то время была под Opera Software.

__ http://www.mozilla.org/thunderbird/
__ https://addons.mozilla.org/thunderbird/addon/gmail-conversation-view/
__ http://www.yorba.org/geary
__ https://fastmail.fm

И конечно смотрел на `mailpile.is`__, но они пошли странным путем.

__ https://www.mailpile.is/

После всех этих и других проб понял, что в gmail сделаны идеальные для меня цепочки писем 
(ну или почти идеальные). А пару-тройку месяцев назад мне нужна была идея для проекта и в 
итоге склонился, что нужен webmail клиент с gmail-подобными цепочками писем. Это то чего
мне не хватает и чем бы пользовался регулярно на ежедневной основе, а последнее очень 
важно для заинтересованности в разработке и улучшениии продукта.

Начало положено, **очень многое** предстоит сделать, но уже сделан большой кусок работы. 
Большая часть не очень видна, так как она связана с IMAP общением, отложенной 
синхронизацией, парсингом писем, а видимая часть -- немного рабочего интерфейса. Сейчас 
есть `публичное демо`__, назовем это демо концепта, которое довольно быстро работает 
(правда, еще нет возможности писать письма). Можно послать письмо на 
**mailr[at]pusto.org** и оно, скорее всего, появится в Inbox.

__ http://mail.pusto.org

Рабочее название проекта **Mailr**. Код на `github. <https://github.com/naspeh/mailr>`_


.. image:: /en/mailr/screenshot-s.png

Мое видение первой версии
-------------------------
Mailr будет иметь быстрый и удобный веб интерфейс, которым будет удобно пользоваться 
на небольшом экране ноутбука, на большим мониторе и на iPad Mini, все эти девайсы у меня 
есть и мне хочется иметь единый настраиваемый интерфейс для них.

Mailr будет иметь gmail-совместимый режим через IMAP, чтоб можно было вернуться в любое 
время на gmail. Так как пока версия под мобильные телефоны не планируется, то этот режим 
будет тоже полезен, можно будет параллельно коннектиться к gmail привычным мобильным 
клиентом, если нужно. Кроме прочего с gmail за спиной проще начинать разработку и 
сконцентрироваться на удобном интерфейсе.

Многие функции из gmail нужно реализовать: удобные цепочки писем, метки, быстрый поиск, 
фильтры для сортировки входящей почты, хороший механизм схлопывания цитируемых писем, 
горячие клавиши, поддержка SSL...

Также будут дополнительные функции.

**Объединение цепочек писем.** Google хорошо находит соответствие писем и цепочек, но 
иногда его алгоритмы не работают:

.. image:: /en/mailr/unmatched-thread.png

Возможность вручную объединить цепочки -- это выход в таких ситуациях.

**Markdown для написания писем.** Мне нравится Markdown__ и reStructuredText__ и мне бы 
хотелось писать письма используя эти текстовые языки разметки, после конвертации они 
выдают отличный для чтения HTML. Текущий редактор писем в gmail для меня очень неудобный.

__ http://en.wikipedia.org/wiki/Markdown
__ http://en.wikipedia.org/wiki/ReStructuredText

**Две панели.** Это моя любимая функция :), две панели видно на скриншоте. Давно уже 
использую двухпанельный режим в своем текстовом редакторе VIM и мне уже не комфортно в 
однопанельных редакторах. Вторая панель расширяет обычно контекст, когда работаешь в 
первой. В будущем будет возможность отключить этот режим.

**Настраеваемый интерфейс.** Как говорил выше мне нужен удобный интерфейс на разнообразных 
разрешениях экрана, темы и настройки интерфейса будут решать эту задачу.

**Вся почта в одном табе.** Я использую Chrome и мне нравится, что он открывает 
"Настройки", "Скаченные файлы", "Расширения" в новых вкладках, а не окнах (раньше 
использовал Firefox -- он многое открывает в новых окнах). У меня весь серфинг интернета 
живет в одном окне браузера, а вся почта, в идеале, хочется, чтоб жила в одной вкладке 
(это также подразумевает все аккаунты, хотя это возможно появится уже после первой 
версии).

**Простой backup.** Это важно для Open Source продукта, чтоб была возможность взять все 
данные (аккаунты, фильтры, цепочки) и перенести с одной инсталяции на свою локальную или 
на сервер своего проверенного друга-гика.

Следующие версии
----------------
Когда можно будет использовать Mailr c gmail в качестве IMAP сервера, то дальше мне 
хочется уйти все таки от gmail и использовать свой email адрес. И, скорее всего, следующим
шагом будет интеграция с Mailgun__. Поднять свой правильный IMAP сервер с 
антиспам-фильтром -- дело не самое легкое, с Mailgun будет проще, тем более они не хранят 
письма у себя.

__ http://www.mailgun.com/

Дальше много мыслей для продолжения: поддержка других IMAP серверов, множественные 
аккаунты в одном табе, PGP шифрование, списки рассылок для друзей...

Напоследок
-----------
Хочется в этом проекте использовать минимум зависимостей и непереусложнить с кодом, ведь 
потом все нужно будет поддерживать.

Стек технологий:
 - Python 3, werkzeug, jinja2, sqlalchemy, lxml;
 - PostgreSQL с его крутыми типами данных и не только;
 - lessjs, jquery на фронтенде.

Да, только jquery -- из-за архитектурного решения. Мне больше нравится писать Python код, 
а JavaScript хочется очень минимизировать, поэтому вместо модного REST и рендеринга на 
стороне клиента мне захотелось генерировать семантичный HTML на стороне сервера. Это 
полезно, например, для iPad Mini, в нем процессор слабее и памяти меньше, чем обычно на 
ноутбуках и десктопах. В будущем эта ситуация может изменится.

В этом проекте еще нужно многое придумать, многое реализовать, многое оптимизировать. В 
последнее время я занимался им очень интенсивно, но мой отпуск заканчивается и нужно 
возвращаться к работе, то есть времени на проект будет намного меньше. Очень хочется его 
довести до стадии, чтоб заменить наконец gmail :).

Open Source -- это круто и мне всегда хотелось отдать дань этому сообществу, и если 
задуманное мной в этом email клиенте удастся реализовать и получится хороший продукт, то 
это будет отличный вклад.
