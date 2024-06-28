import os
import telebot
from telebot import types
from dotenv import load_dotenv

tg_token1 = os.environ["TG_TOKEN1"]
bot1 = telebot.TeleBot(tg_token1)


@bot1.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📋Информация о компании")
    item2 = types.KeyboardButton("💲Как производится оплата")
    item3 = types.KeyboardButton("🏫Как происходит обучение")
    item4 = types.KeyboardButton("🧍Кураторская поддержка")
    item5 = types.KeyboardButton("⚙️Помощь администратора")
    markup.add(item1, item2, item3, item4, item5)
    bot1.send_message(
        message.chat.id,
        "Здравствуйте, {0.first_name}! Я чат бот🤖 школы. С моей помощью вы можете узнать интересующую вас информацию о нашей школе. Для этого выберите интересующий вас пункт в меню клавиатуры."
        .format(message.from_user),
        reply_markup=markup)


@bot1.message_handler(content_types=["text"])
def send_message(message):
    if message.text == "📋Информация о компании":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Вводное интервью")
        item2 = types.KeyboardButton("Задачи")
        back = types.KeyboardButton("⬅️назад")
        markup.add(item1, item2, back)
        bot1.send_message(message.chat.id,
                          "📋Информация о компании",
                          reply_markup=markup)

    elif message.text == "Вводное интервью":
        bot1.send_message(message.chat.id,
                          "https://www.youtube.com/watch?v=uRGFiM0Dzf8")

    elif message.text == "Задачи":
        bot1.send_message(
            message.chat.id, """Какие задачи родителей мы решаем?

Мотивационные:
Помочь ребенку через проекты поверить в свои силы;
Восстановить потерянную мотивацию к занятиям;
Отвлечь от компьютерных игр, чтобы воспринимал ПК как инструмент для работы;
Привить желание заниматься хоть чем-то, кроме игр;
Привить желание учиться именно в IT-сфере;
Заинтересовать, чтобы загорелся и начал заниматься перспективным направлением.

Поиск хобби:
У вашего ребёнка появится хобби;
Ваш ребенок узнает, что такое программирование и дизайн;
Научится мыслить системно и приобретет способность к упрощению и систематизации информации.

Получение навыка:
Вы хотите, чтобы ребенок умел программировать и получил монетизируемый навык;
Вы хотите удовлетворить желание ребенка программировать и ищите сильный, проработанный курс;
Вы ищите самый лучший курс по цены/результата для изучения программирования ребенком;
Поможем разобраться родителям в IT и дать самую подходящую траекторию для ребёнка.

Создание крепкого фундамента:
У ребёнка появится сильный фундамент и конкурентное преимущество;
Ребенок будет иметь представление о профессиях и специальностях в ВУЗах;
Ваш ребенок получит одну из траекторий дальнейшего профессионального развития.

Введение в профессию:
Получит звание «программист», аналогично с «боксером»;
Найдет единомышленников, «движуху»;
Ребенок будет уметь самостоятельно делать проекты, т.к. уже знаком с программированием;
Научится «эксплуатировать» полученные навыки. Привить «менеджерские» навыки в работе."""
        )

    elif message.text == "💲Как производится оплата":
        bot1.send_message(
            message.chat.id, """Как производится оплата

Вы оплачиваете каждый период/абонемент (8 занятий
по утвержденному расписанию), каждые 28 дней, в
последний день предыдущего оплаченного периода.
Мы будем об этом напоминать. Если нет возможности
оплатить в срок — предупредите, мы подождем, занятия
при этом не приостанавливаем.

Новогодние, майские и летние каникулы — исключение,
когда абонемент можно заморозить. В остальное
время оплата идет каждые 8 занятий по расписанию.

Пропущенные основные занятия по любым причинам у
вас не сгорают, а отрабатываются, вне расписания, по
договоренности с педагогом, без привязки к оплате
периодов. По запросу мы пришлем вам варианты, когда
можно подключиться на отработку. Отработки
проводятся в другой группе при наличии свободного
места, либо индивидуально, но длительностью 45
минут. Если нет возможности отработать в учебное
время, то копим пропуски и отрабатываем во время
школьных каникул.

При покупке нескольких периодов — предоставляем
скидки. Когда по вашей рекомендации к нам придет
новый ученик — фиксированная скидка 2500 рублей на
один период.

При решении сделать паузу в занятиях более трех
недель без оплаты будущих уроков место в группе
открепляется, и по возвращению если место занято -
подбирается новая группа или педагог.""")

    elif message.text == "🏫Как происходит обучение":
        bot1.send_message(
            message.chat.id, """Как происходит обучение

Ребята обучаются в мини-группах до 4-х человек. С
ними наставник-педагог.

Программа состоит из модулей, в модулях лежат
проекты, проекты поделены на шаги, в шаги вложена
необходимая информация (статьи, ссылки,
документация), необходимая к изучению для
выполнения шага.

По завершению проект отправляется на проверку.
Проверяют действующие программисты и пишут
ревью-код. После принятия открывается следующий
проект модуля. Если пришли правки, то нужно
доработать проект. Время проверки - от 3 до 24 часов.
Пока проверяется проект одного модуля, выполняем
проект другого модуля программы.

Педагог будет помогать с возникшими вопросами,
следить за происходящим, комментировать, объяснять
при трудностях, курировать задачи.

Материалы на платформе в доступе и вне занятий.
Домашнее задание обычно - несколько шагов
самостоятельно. От самостоятельной работы напрямую
зависит скорость прогресса. Больше уделяет времени
программированию - быстрее проходит программу. На
урок можно подключаться уже с возникшими
вопросами по задачам.""")

    elif message.text == "🧍Кураторская поддержка":
        bot1.send_message(
            message.chat.id, """Кураторская поддержка

Спасибо Вам, что выбрали нашу школу и доверили
своего ребенка на обучение. Мы будем прикладывать
все усилия, чтобы дать максимальный результат и
добиться поставленных Вами целей.

Что дальше?

Дальше у нас наступает первый месяц адаптации.
Месяц, когда ученик знакомится ближе с педагогом,
правилами группы, форматом обучения, своими
обязанностями, и самое главное - начинает
сталкиваться с первыми трудностями.

Наша совместная задача, родителя и куратора - держать
руку на пульсе и сразу реагировать на все замечания и
комментарии ребенка на любые моменты
образовательного процесса. Это позволит понимать
ситуацию и вносить изменения в работу, что снизит
стресс у ребенка и поможет быстрее влиться в процесс.

Пишите пожалуйста, обратную связь и не бойтесь
критиковать.

По всем вопросам - обращайтесь, с удовольствием
ответим.

Мы здесь на связи с Вами с 9 до 20 по Москве в будни и
с 10 до 19 в выходные дни. Куратор при необходимости
будет Вам звонить, обсуждать процесс обучения.""")

    elif message.text == ("⚙️Помощь администратора"):
        bot1.send_message(
            message.chat.id,
            "Нажмите на ссылку, чтобы получить помощь администратора:",
            disable_notification=True)
        bot1.send_message(message.chat.id,
                          "https://t.me/+oGuakMoeX71jZGMy",
                          disable_web_page_preview=False)

    elif message.text == "⬅️назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("📋Информация о компании")
        item2 = types.KeyboardButton("💲Как производится оплата")
        item3 = types.KeyboardButton("🏫Как происходит обучение")
        item4 = types.KeyboardButton("🧍Кураторская поддержка")
        item5 = types.KeyboardButton("⚙️Помощь администратора")
        markup.add(item1, item2, item3, item4, item5)
        bot1.send_message(message.chat.id, "⬅️назад", reply_markup=markup)


def main():
    load_dotenv()
    bot1.infinity_polling()


if __name__ == "__main__":
    main()
