import telebot
from telebot import TeleBot, types
from schedules import *

bot = TeleBot("7637278497:AAGOP7ntdnoCfDuKLPAnNNiUmbUd_BIrb0c")  # Замените на свой токен

# Списки групп для ПТИ:
# для курсов, кроме 2-го
valid_groups = [
    "4093", "4092", "4711", "4541", "4413", "4411", "4406", "4405",
    "4371", "4312", "4311", "4091", "4075", "4071", "4061", "4042",
    "4035", "4031", "4026", "4025", "4022", "4016", "4015", "4012"
]
# для 2-го курса (пример, заполните своими данными)
second_year_groups = ["2031", "2032", "2041", "2042", "2051", "2052"]

@bot.message_handler(commands=["start"])
def start(message):
    show_courses(message)

def show_courses(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    courses = ["1 курс", "2 курс", "3 курс", "4 курс", "5 курс"]
    # Располагаем кнопки по 3 в ряд
    for i in range(0, len(courses), 3):
        markup.row(*[types.KeyboardButton(course) for course in courses[i:i + 3]])
    bot.send_message(message.chat.id, "Выберите курс:", reply_markup=markup)
    bot.register_next_step_handler(message, handle_course_selection)


def handle_course_selection(message):
    if message.text not in ["1 курс", "2 курс", "3 курс", "4 курс", "5 курс"]:
        bot.send_message(message.chat.id, "Некорректный выбор. Попробуйте снова.")
        show_courses(message)
        return
    selected_course = message.text
    show_groups(message, selected_course)

def show_groups(message, course):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Если выбран 2 курс, используем второй список групп
    groups = second_year_groups if course == "2 курс" else valid_groups
    # Формируем клавиатуру с группами (3 кнопки в ряду)
    for i in range(0, len(groups), 3):
        markup.row(*[types.KeyboardButton(g) for g in groups[i:i + 3]])
    markup.add(types.KeyboardButton("Назад"))
    bot.send_message(message.chat.id, f"Выберите группу для {course}:", reply_markup=markup)
    bot.register_next_step_handler(message, handle_group_selection, course)

def handle_group_selection(message, course):
    if message.text == "Назад":
        show_courses(message)
        return

    groups = second_year_groups if course == "2 курс" else valid_groups
    if message.text in groups:
        show_schedule(message, message.text, course)
    else:
        bot.send_message(message.chat.id, "Такой группы нет. Попробуйте снова.")
        show_groups(message, course)

def show_schedule(message, group, course):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Назад"]
    # Располагаем дни по 2 кнопки в ряду
    for i in range(0, len(days), 2):
        markup.row(*[types.KeyboardButton(day) for day in days[i:i + 2]])
    bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=markup)
    bot.register_next_step_handler(message, choose_day, group, course)

def choose_day(message, group, course):
    if message.text == "Назад":
        show_groups(message, course)
        return

    schedule_text = get_schedule(message.text, group)
    bot.send_message(message.chat.id, schedule_text)
    # После показа расписания снова предлагаем выбрать день
    show_schedule(message, group, course)

def get_schedule(day, group):
    # Словарь расписаний для каждой группы. Функции расписаний импортируются из schedules.
    schedules = {
        "4093": {
            "Понедельник": schedule_monday4093,
            "Вторник": schedule_tuesday4093,
            "Среда": schedule_Wednesday4093,
            "Четверг": schedule_thursday4093,
            "Пятница": schedule_friday4093,
            "Суббота": schedule_saturday4093
        },
        "4092": {
            "Понедельник": schedule_monday4092,
            "Вторник": schedule_tuesday4092,
            "Среда": schedule_Wednesday4092,
            "Четверг": schedule_thursday4092,
            "Пятница": schedule_friday4092,
            "Суббота": schedule_saturday4092
        },
        "4711": {
            "Понедельник": schedule_monday4711,
            "Вторник": schedule_tuesday4711,
            "Среда": schedule_Wednesday4711,
            "Четверг": schedule_thursday4711,
            "Пятница": schedule_friday4711,
            "Суббота": schedule_saturday4711
        },
        "4541": {
            "Понедельник": schedule_monday4541,
            "Вторник": schedule_tuesday4541,
            "Среда": schedule_Wednesday4541,
            "Четверг": schedule_thursday4541,
            "Пятница": schedule_friday4541,
            "Суббота": schedule_saturday4541
        },
        "4413": {
            "Понедельник": schedule_monday4413,
            "Вторник": schedule_tuesday4413,
            "Среда": schedule_Wednesday4413,
            "Четверг": schedule_thursday4413,
            "Пятница": schedule_friday4413,
            "Суббота": schedule_saturday4413
        },
        "4411": {
            "Понедельник": schedule_monday4411,
            "Вторник": schedule_tuesday4411,
            "Среда": schedule_Wednesday4411,
            "Четверг": schedule_thursday4411,
            "Пятница": schedule_friday4411,
            "Суббота": schedule_saturday4411
        },
        "4406": {
            "Понедельник": schedule_monday4406,
            "Вторник": schedule_tuesday4406,
            "Среда": schedule_Wednesday4406,
            "Четверг": schedule_thursday4406,
            "Пятница": schedule_friday4406,
            "Суббота": schedule_saturday4406
        },
        "4405": {
            "Понедельник": schedule_monday4405,
            "Вторник": schedule_tuesday4405,
            "Среда": schedule_Wednesday4405,
            "Четверг": schedule_thursday4405,
            "Пятница": schedule_friday4405,
            "Суббота": schedule_saturday4405
        },
        "4371": {
            "Понедельник": schedule_monday4371,
            "Вторник": schedule_tuesday4371,
            "Среда": schedule_Wednesday4371,
            "Четверг": schedule_thursday4371,
            "Пятница": schedule_friday4371,
            "Суббота": schedule_saturday4371
        },
        "4312": {
            "Понедельник": schedule_monday4312,
            "Вторник": schedule_tuesday4312,
            "Среда": schedule_Wednesday4312,
            "Четверг": schedule_thursday4312,
            "Пятница": schedule_friday4312,
            "Суббота": schedule_saturday4312
        },
        "4311": {
            "Понедельник": schedule_monday4311,
            "Вторник": schedule_tuesday4311,
            "Среда": schedule_Wednesday4311,
            "Четверг": schedule_thursday4311,
            "Пятница": schedule_friday4311,
            "Суббота": schedule_saturday4311
        },
        "4091": {
            "Понедельник": schedule_monday4091,
            "Вторник": schedule_tuesday4091,
            "Среда": schedule_wednesday4091,
            "Четверг": schedule_thursday4091,
            "Пятница": schedule_friday4091,
            "Суббота": schedule_saturday4091
        },
        "4075": {
            "Понедельник": schedule_monday4075,
            "Вторник": schedule_tuesday4075,
            "Среда": schedule_wednesday4075,
            "Четверг": schedule_thursday4075,
            "Пятница": schedule_friday4075,
            "Суббота": schedule_saturday4075
        },
        "4071": {
            "Понедельник": schedule_monday4071,
            "Вторник": schedule_tuesday4071,
            "Среда": schedule_wednesday4071,
            "Четверг": schedule_thursday4071,
            "Пятница": schedule_friday4071,
            "Суббота": schedule_saturday4071
        },
        "4042": {
            "Понедельник": schedule_monday4042,
            "Вторник": schedule_tuesday4042,
            "Среда": schedule_wednesday4042,
            "Четверг": schedule_thursday4042,
            "Пятница": schedule_friday4042,
            "Суббота": schedule_saturday4042
        },
        "4035": {
            "Понедельник": schedule_monday4035,
            "Вторник": schedule_tuesday4035,
            "Среда": schedule_wednesday4035,
            "Четверг": schedule_thursday4035,
            "Пятница": schedule_friday4035,
            "Суббота": schedule_saturday4035
        },
        "4031": {
            "Понедельник": schedule_monday4031,
            "Вторник": schedule_tuesday4031,
            "Среда": schedule_wednesday4031,
            "Четверг": schedule_thursday4031,
            "Пятница": schedule_friday4031,
            "Суббота": schedule_saturday4031
        },
        "4026": {
            "Понедельник": schedule_monday4026,
            "Вторник": schedule_tuesday4026,
            "Среда": schedule_wednesday4026,
            "Четверг": schedule_thursday4026,
            "Пятница": schedule_friday4026,
            "Суббота": schedule_saturday4026
        },
        "4025": {
            "Понедельник": schedule_monday4025,
            "Вторник": schedule_tuesday4025,
            "Среда": schedule_wednesday4025,
            "Четверг": schedule_thursday4025,
            "Пятница": schedule_friday4025,
            "Суббота": schedule_saturday4025
        },
        "4022": {
            "Понедельник": schedule_monday4022,
            "Вторник": schedule_tuesday4022,
            "Среда": schedule_wednesday4022,
            "Четверг": schedule_thursday4022,
            "Пятница": schedule_friday4022,
            "Суббота": schedule_saturday4022
        },
        "4016": {
            "Понедельник": schedule_monday4016,
            "Вторник": schedule_tuesday4016,
            "Среда": schedule_wednesday4016,
            "Четверг": schedule_thursday4016,
            "Пятница": schedule_friday4016,
            "Суббота": schedule_saturday4016
        },
        "4015": {
            "Понедельник": schedule_monday4015,
            "Вторник": schedule_tuesday4015,
            "Среда": schedule_wednesday4015,
            "Четверг": schedule_thursday4015,
            "Пятница": schedule_friday4015,
            "Суббота": schedule_saturday4015
        },
        "4012": {
            "Понедельник": schedule_monday4012,
            "Вторник": schedule_tuesday4012,
            "Среда": schedule_wednesday4012,
            "Четверг": schedule_thursday4012,
            "Пятница": schedule_friday4012,
            "Суббота": schedule_saturday4012
        }
    }
    group_schedule = schedules.get(group, {})
    return group_schedule.get(day, "Расписание не найдено.")

bot.polling(none_stop=True)
