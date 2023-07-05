import telebot
from telebot import types

# Создание бота
bot = telebot.TeleBot('6337776952:AAGLuPdsZ-L_fetxdPcRlSP5knjNMGLj9hI')

# Обработчик команды /start или /help
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    send_main_menu(message.chat.id)

def start(update, context):
    keyboard = [
        [types.InlineKeyboardButton("Подписка и аккаунт", callback_data='subscription')],
        [types.InlineKeyboardButton("Вопросы по оплате", callback_data='payment')],
        [types.InlineKeyboardButton("Импорт банковских операций", callback_data='import')],
        [types.InlineKeyboardButton("Синхронизация и данные", callback_data='sync')],
        [types.InlineKeyboardButton("Полезная информация", callback_data='info')],
        [types.InlineKeyboardButton("Написать оператору", callback_data='operator')]
    ]

    reply_markup = types.InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите категорию:', reply_markup=reply_markup)

# Обработчик нажатия на кнопку
def button_click(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'subscription':
        keyboard = [
            [types.InlineKeyboardButton("Войти в личный аккаунт", callback_data='login')],
            [types.InlineKeyboardButton("Перенести данные из бесплатной версии", callback_data='transfer')],
            [types.InlineKeyboardButton("Семейный аккаунт", callback_data='family')],
            [types.InlineKeyboardButton("Отображение подписки в профиле", callback_data='profile')],
            [types.InlineKeyboardButton("Ошибка \"Обратитесь в поддержку\"", callback_data='error')],
            [types.InlineKeyboardButton("Очистить аккаунт с сохранением подписки", callback_data='clear')]
        ]
    elif query.data == 'payment':
        keyboard = [
            [types.InlineKeyboardButton("Как приобрести подписку", callback_data='purchase')],
            [types.InlineKeyboardButton("Деньги списались, но нет письма", callback_data='no_email')],
            [types.InlineKeyboardButton("Квитанция об оплате", callback_data='receipt')]
        ]
    elif query.data == 'import':
        keyboard = [
            [types.InlineKeyboardButton("Загрузить новые операции", callback_data='load_operations')],
            [types.InlineKeyboardButton("Переподключить импорт", callback_data='reconnect')],
            [types.InlineKeyboardButton("Дубли операций", callback_data='duplicates')],
            [types.InlineKeyboardButton("Проблемы с импортом Сбербанк", callback_data='sberbank')],
            [types.InlineKeyboardButton("Проблемы с импортом Тинькофф банк", callback_data='tinkoff')],
            [types.InlineKeyboardButton("Проблемы с импортом Газпромбанк", callback_data='gazprombank')]
        ]
    elif query.data == 'sync':
        keyboard = [
            [types.InlineKeyboardButton("Что такое синхронизация данных", callback_data='data_sync')],
            [types.InlineKeyboardButton("Переустановка приложения", callback_data='reinstall')],
            [types.InlineKeyboardButton("Синхронизация старой и новой версий приложения", callback_data='old_new_sync')],
            [types.InlineKeyboardButton("Пропали данные (восстановить данные)", callback_data='data_recovery')],
            [types.InlineKeyboardButton("Очистить данные с сохранением подписки", callback_data='clear_data')]
        ]
    elif query.data == 'info':
        keyboard =[
            [types.InlineKeyboardButton("Как начать работать с приложением", callback_data='getting_started')],
            [types.InlineKeyboardButton("Можно ли переводить денежные средства в приложении?", callback_data='money_transfer')],
            [types.InlineKeyboardButton("Купил подписку - что дальше", callback_data='after_purchase')],
            [InlineKeyboardButton("Тарифы", callback_data='tariffs')],
            [InlineKeyboardButton("Курсы Правила денег", callback_data='money_rules')]
]
def sub_button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'login':
        text = 'После оплаты на ваш почтовый ящик должно прийти письмо о первом входе в приложение. Если письма нет, скорее всего оно попало в папку Спам. Попробуйте войти в личный аккаунт в приложении, используя как логин email, на который вы зарегистрировали подписку на приложение (по кнопке У меня есть профиль). Пароль запросите через Забыли пароль. Если не получается, то напишите обращение в службу поддержки.'  
if query.data == 'transfer':
        text = 'Если вы пользовались бесплатной версией приложения, и хотите далее пользоваться этими данными, перенести их в личный аккаунт (на сервер), то нужно приобрести подписку на приложение, а затем нажать в Профиле (значок человечка) на Привязать купленную подписку (используя личный логин и пароль). Данные будут перенесены в ваш аккаунт.' 
if query.data == 'family':
    text = 'Когда вы покупаете подписку, она привязывается к вашему аккаунту (логин - ваш email) и не ограничена в его пределах: открывает все перечисленные в ней функции. Вы можете использовать этот аккаунт на разных устройствах: Android, iOS, веб-версию - на ПК https://coinkeeper.me/introduce-yourself. Все данные, которые вы вносите в аккаунт с любого устройства, будут отображаться на других, то есть синхронизироваться между собой. При ведении совместного бюджета на одном аккаунте каждому, кто им пользуется, будут видны все доходы, счета и категории. Чтобы использовать аккаунт как семейный, нужно каждому члену семьи на своем устройстве  войти в приложение с одинаковым логином и паролем (от аккаунта).' 
if query.data == 'profile':
    text = 'Если у вас есть подписка Премиум, и также подписка Платинум, то в Профиле вашего аккаунта будет отображаться подписка Платинум, так как она обладает большим функционалом. Когда истечет срок действия Платинум подписки, то будет отображаться подписка Премиум. Здесь информация по тарифам https://about.coinkeeper.me/alltariffs' 
if query.data == 'error':
    text = 'Такое сообщение появляется, если вы вносили какие-либо данные в приложение. Если эти данные вам не нужны, переустановите приложение и выполните вход с существующим профилем (через "У меня есть аккаунт") [ссылка](https://ck3help.me/page6298290.html). Если данные нужны и вы хотите продолжить ими пользоваться, то напишите обращение в службу поддержки.'
if query.data == 'clear':
    text = 'Можно очистить аккаунт самостоятельно, вручную удалив все данные по операциям. Также мы можем очистить аккаунт на своей стороне, при этом удалится всё - история, категории, метки и счета, импорт банковских операций, если он был подключен (если подключена карта CoinKeeper от АкБарс банка, то обнулять аккаунт нельзя). Подписка на приложение останется. Для обнуления аккаунта напишите обращение в службу поддержки.'
if query.data == 'purchase':
    text = 'Вы можете приобрести подписку на нашем сайте - [ссылка](https://about.coinkeeper.me/). Подробнее о возможностях наших тарифов можно почитать [здесь](https://about.coinkeeper.me/alltariffs).'
if query.data == 'no_email':
    text = 'Подписка на приложение привязывается к вашему email, который вы вводите как логин при регистрации. После оплаты подписка начисляется автоматически в соответствии с тем тарифом, который был приобретен. Попробуйте войти  в личный аккаунт в приложении, используя как логин ваш емейл, пароль запросите через "Забыли пароль". Вот [инструкция для входа в приложение](https://ck3help.me/page6298290.html). Если не получается войти в аккаунт, напишите обращение в службу поддержки.'
if query.data == 'receipt':
    text = 'После оплаты квитанция должна была прийти к вам на почту. Если там ее нет, можно проверить папку спам. Также вы можете поискать квитанцию по нашей инструкции. Вот [инструкция о том, как найти квитанцию о покупке с GooglePlay](https://support.google.com/googleplay/answer/2850369?hl=ru). Здесь квитанции о покупках, сделанных на iTunes: [ссылка](https://support.apple.com/ru-ru/HT204088).'
if query.data == 'load_operations':
    text = 'Чтобы загрузить новые операции нужно нажать на кнопку "Обновить" под карточкой счета в приложении. Если после совершения операции в банке прошло более суток, но операция не загрузилась в приложение, попробуйте переподключить импорт. Если новые операции не загружаются, напишите обращение в службу поддержки.'
if query.data == 'reconnect':
    text = 'Чтобы решить какую-либо проблему в работе приложения можно попробовать переустановить приложение (если у вас был подключен импорт банковских операций, после переустановки приложения, нужно будет подключить его заново, если подключена карта CoinKeeper АкБарс банка, то не переустанавливайте приложение). Перед переустановкой ОБЯЗАТЕЛЬНО:Синхронизируйте принудительно данные в мобильном приложении (нажмите на Обновить в строке Синхронизация в Профиле (знак человечка)); Войдите в веб-версию приложения (через ПК https://coinkeeper.me/introduce-yourself ) либо в свой аккаунт через другой телефон и проверьте все ли данные (суммы и статистика) отображаются таким же образом, как и в мобильном приложении; Если все данные верны, то попробуйте переустановить приложение (удалить и скачать заново, на Android устройствах, удалить, очистив кэш приложения); Войдите в личный аккаунт (с логином и паролем) и проверьте, сохраняется ли проблема; Если данные в веб-версии или на другом телефоне отличаются от данных в мобильном приложении, не переустанавливайте приложение и напишите обращение в поддержку. Если после переустановки приложения проблема сохраняется, напишите, пожалуйста, обращение в службу поддержки.'
if query.data == 'duplicates':
  text = "Появление дублей операций при загрузке импорта связано с механизмом обработки операций на стороне банков. Один из способов уменьшения количества дублей - это обновление импорта (загрузка новых операций) не чаще, чем 1 раз в сутки. Возможные дубли операций помечены красной карточкой. Дубли операций можно удалить."
if query.data == 'sberbank':
        text = '1. Проверьте, все ли данные вы вносите верно при подключении импорта. 2. Попробуйте переподключить импорт для счета (отключить импорт через режим редактирования счета - карандашик в правом верхнем углу карточки счета, подключить импорт обратно по шагам). 3. Если вы подключаете данные за большой период, попробуйте использовать текущую дату при подключении. 4. Если предыдущие варианты не сработали, то перейдите в самый низ раздела Профиль. Нажмите и удерживайте строку Версия приложения. Измените настройку для Сбербанка: Js, Native, NativWithJSParams, NativWebView. Попробуйте подключить импорт через все предлагаемые настройки. 5. Если ни один способ не помог корректно подключить импорт, то напишите обращение в службу поддержки.' 
        text = ''
if query.data == 'tinkoff':
    text = '1. Проверьте, все ли данные вы вносите верно при подключении импорта. Нужно использовать пароль от интернет банка Тинькофф. Для проверки можно использовать вход в личный кабинет на сайте банка. 2. Попробуйте переподключить импорт для счета (отключить импорт через режим редактирования счета - карандашик в правом верхнем углу карточки счета, подключить импорт обратно по шагам). Попробуйте оба варианта подключения импорта - как через логин (логин от интернет банка с сайта Тинькофф), так и через номер телефона. Логин можно получить через восстановление пароля на сайте банка, вам нужно заменить и логин, и пароль: https://www.tinkoff.ru/registration/?recovery=. 3. Если вы подключаете данные за большой период, попробуйте использовать текущую дату при подключении. 4. Если предыдущие варианты не сработали, то перейдите в самый низ раздела Профиль. Нажмите и удерживайте строку Версия приложения. Измените настройку для Тинькофф банк: Js или Native (в зависимости от исходного установленного параметра). Попробуйте подключить импорт. 5. Если ни один способ не помог корректно подключить импорт, то напишите обращение в службу поддержки.' 
if query.data == 'data_sync':
    text = 'После внесения транзакций на устройство (через платный аккаунт), они автоматически переносятся на сервер. При смене или переустановке устройства, данные автоматически загрузятся в аккаунт на устройство. Если вы вносите большое количество данных или не уверены в стабильности сети, можно принудительно нажать на кнопку Обновить в Профиле вашего аккаунта (перейти в Профиль нужно через значок человечка), чтобы установить связь с сервером и перенести данные. Если в Профиле в строке Синхронизация отображается ошибка (красный или желтый кружок) в течение какого-то времени, то напишите обращение в службу поддержки.'
elif query.data == 'reinstall':
    text = 'Чтобы решить какую-либо проблему в работе приложения можно попробовать переустановить приложение (если у вас был подключен импорт банковских операций, после переустановки приложения, нужно будет подключить его заново, если подключена карта CoinKeeper АкБарс банка, то не переустанавливайте приложение). Перед переустановкой ОБЯЗАТЕЛЬНО:\n- Синхронизируйте принудительно данные в мобильном приложении (нажмите на Обновить в строке Синхронизация в Профиле (знак человечка));\n- Войдите в веб-версию приложения (через ПК https://coinkeeper.me/introduce-yourself ) либо в свой аккаунт через другой телефон и проверьте все ли данные (суммы и статистика) отображаются таким же образом, как и в мобильном приложении;\n- Если все данные верны, то попробуйте переустановить приложение (удалить и скачать заново, на Android устройствах, удалить, очистив кэш приложения);\n- Войдите в личный аккаунт (с логином и паролем) и проверьте, сохраняется ли проблема;\n- Если данные в веб-версии или на другом телефоне отличаются от данных в мобильном приложении, не переустанавливайте приложение и напишите обращение в поддержку. Если после переустановки приложения проблема сохраняется, напишите, пожалуйста, обращение в службу поддержки.'
elif query.data == 'old_new_sync':
    text = 'Старая и новая версии приложения синхронизированы между собой (чтобы была возможность без проблем перейти к использованию новой версии приложения). Для получения доступа к своим данным в новой версии приложения нужно войти в новую версию с использованием своего старого логина и пароля (при наличии оплаченной подписки).'
elif query.data == 'data_recovery':
    text = 'Сейчас функции восстановления данных в приложении нет. Проверьте, пожалуйста, возможно, на каком-то из устройств или в веб-версии https://coinkeeper.me/introduce-yourself данные не успели синхронизироваться. На данный момент существует только возможность Проверьте, пожалуйста, возможно, на каком-то из устройств или в веб-версии https://coinkeeper.me/introduce-yourself данные не успели синхронизироваться. На данный момент существует только возможность восстановить счет, удаленный с сохранением истории по нему. Восстановить счет можно следующим образом: 1. На ПК зайдите в свой аккаунт на coinkeeper.me (с личным логином и паролем). 2. Откройте ссылку https://coinkeeper.me/restore/ обязательно в новом окне. 3. Отобразится список удаленных счетов. 4. Выберите нужный для восстановления счет и нажмите на него.5. Перейдите в свой аккаунт, там вы увидите восстановленный счет.' 
elif query.data == 'clear_data':
    text = 'Можно очистить аккаунт самостоятельно, вручную удалив все данные по операциям. Также мы можем очистить аккаунт на своей стороне, при этом удалится всё - история, категории, метки и счета, импорт банковских операций, если он был подключен (если подключена карта CoinKeeper от АкБарс банка, то обнулять аккаунт нельзя). Подписка на приложение останется. Для обнуления аккаунта напишите обращение в службу поддержки.'
elif query.data == 'money_transfer':
    text = 'Сейчас в приложении нельзя фактически осуществлять операции - только отображать операции, совершенные через банк. Приложение активно развивается, еще будет много нового функционала и в будущем мы планируем реализовать возможность совершать операции непосредственно через приложение. Приобрести подписку на приложение по супер выгодной цене можно по ссылке https://about.coinkeeper.me/special_sale_offer'
elif query.data == 'after_purchase':
    text = 'Вы можете посмотреть нашу инструкцию, как начать пользоваться приложением - https://about.coinkeeper.me/faq#rec342408969.'
elif query.data == 'tariffs':
    text = 'С тарифами и их возможностями можно ознакомиться здесь - https://about.coinkeeper.me/alltariffs.'
elif query.data == 'money_rules':
    text = 'С курсом "Правила денег" можно ознакомиться по ссылке - https://pd.coinkeeper.me/courses.'
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Написать оператору", callback_data='operator')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите действие:', reply_markup=reply_markup)

# Обработчик нажатия на кнопку
def button_callback(update, context):
    query = update.callback_query
    if query.data == 'operator':
        query.answer()
        query.edit_message_text(
            text="Опишите вашу ситуацию максимально подробно.\nНаш оператор ответит вам в течение 24-х часов."
        )
        # Отправляем пользователю поле для ввода текста
        context.bot.send_message(chat_id=query.message.chat_id, text="Введите ваше сообщение:")

# Создаем экземпляр Updater и регистрируем обработчики
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CallbackQueryHandler(button_callback))
dispatcher.add_handler(CommandHandler('start', start))


from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.update import Update
from telegram.callbackquery import CallbackQuery
from telegram.ext.callbackcontext import CallbackContext


def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Подписка и аккаунт", callback_data='subscription')],
        [InlineKeyboardButton("Вопросы по оплате", callback_data='payment')],
        [InlineKeyboardButton("Импорт банковских операций", callback_data='import')],
        [InlineKeyboardButton("Синхронизация и данные", callback_data='sync')],
        [InlineKeyboardButton("Полезная информация", callback_data='info')],
        [InlineKeyboardButton("Написать оператору", callback_data='operator')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите категорию:', reply_markup=reply_markup)


def button_click(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    query.answer()

    if query.data == 'subscription':
        text = 'Текст для подкатегории "Подписка и аккаунт"'
    elif query.data == 'payment':
        text = 'Текст для подкатегории "Вопросы по оплате"'
    elif query.data == 'import':
        text = 'Текст для подкатегории "Импорт банковских операций"'
    elif query.data == 'sync':
        text = 'Текст для подкатегории "Синхронизация и данные"'
    elif query.data == 'info':
        text = 'Текст для подкатегории "Полезная информация"'
    elif query.data == 'operator':
        text = 'Текст для подкатегории "Написать оператору"'
    else:
        text = ''

    back_button = [InlineKeyboardButton("Назад", callback_data='back')]
    keyboard = [[back_button]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text, reply_markup=reply_markup)


def sub_button_click(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Подписка и аккаунт", callback_data='subscription')],
        [InlineKeyboardButton("Вопросы по оплате", callback_data='payment')],
        [InlineKeyboardButton("Импорт банковских операций", callback_data='import')],
        [InlineKeyboardButton("Синхронизация и данные", callback_data='sync')],
        [InlineKeyboardButton("Полезная информация", callback_data='info')],
        [InlineKeyboardButton("Написать оператору", callback_data='operator')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('Выберите категорию:', reply_markup=reply_markup)


# Создание телеграм-бота и добавление обработчиков
updater = Updater(('6337776952:AAGLuPdsZ-L_fetxdPcRlSP5knjNMGLj9hI'), use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
button_handler = CallbackQueryHandler(button_click, pattern='^(subscription|payment|import|sync|info|operator)$')
sub_button_handler = CallbackQueryHandler(sub_button_click, pattern='^back$')

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(sub_button_handler)

updater.start_polling()
