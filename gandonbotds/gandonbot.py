import asyncio
import json
import logging
import random
from datetime import datetime
import os
import requests
from aiogram import Bot, Dispatcher, types

API_TOKEN = '6748213241:AAHTjrmijG5hrEp8U5DFPa4WesrL4In3zlM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

loh_history_month = "loh_history_month"
loh_history_year = "loh_history_year"
loh_history_decade = "loh_history_decade"
year_list = ['2025-01-01', '2026-01-01', '2027-01-01', '2028-01-01', '2029-01-01', '2030-01-01']
decade = ['2030-01-01']

def get_chat_history_file(filename, chat_id):
    return f"{filename}_{chat_id}.json"

def get_today():
    url = 'https://tools.aimylogic.com/api/now?tz=Russia/Moscow&format=dd/MM/yyyy'
    json_date = requests.get(url).json()
    date_str = json_date['formatted']
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    return date_obj.strftime('%Y-%m-%d')

def fill_json(source, target):
    with open(source, 'r') as source, open(target, 'a') as target:
        for line in source:
            target.write(line)

def clear_json(filename):
    with open(filename, "w") as f:
        f.truncate(0)

def backup_file(filename):
    current_datetime = datetime.now()
    datetime_str = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f"{filename}_{datetime_str}"
    try:
        with open(filename, 'rb') as original_file:
            data = original_file.read()
        with open(backup_filename, 'wb') as backup_file:
            backup_file.write(data)
    except Exception:
        print('Не получилось чет')

def ensure_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write('')

@dp.message_handler(commands=['gandon'])
async def bot_start(message: types.Message):
    stickers = [
        ("CAACAgIAAxkBAAELDF9ljAiMnv8y7qNh6QkOQf-sDAtDcAACCiYAArkQaEksYoQTtEf5LTME", 0.8),
        ("CAACAgIAAxkBAAEJ81FnMiPfN7cuIrX-HB034R-H7bqzhQAC0DoAAmUBEUjsMn7wln8kVjYE", 0.2)
    ]
    chosen_sticker = random.choices([s[0] for s in stickers], weights=[s[1] for s in stickers], k=1)[0]
    await bot.send_sticker(chat_id=message.chat.id, sticker=chosen_sticker)

@dp.message_handler(commands=['pid'])
async def bot_start(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=r'CAACAgQAAxkBAAEJ83FnMiXdhaEpd2UHyK_rNUbNcEEBsAACfAADTqDDMI8bQNwH2de3NgQ')


@dp.message_handler(commands=['gay'])
async def bot_start(message: types.message):
    random_number = random.randint(1,100)
    response_text = f'Ты гей на: {random_number}%🌈😄'
    await bot.send_message(chat_id=message.chat.id, text=response_text, reply_to_message_id=message.message_id)
    if random_number >= 90:
        await bot.send_sticker(chat_id=message.chat.id, sticker=r'CAACAgQAAxkBAAEJ83FnMiXdhaEpd2UHyK_rNUbNcEEBsAACfAADTqDDMI8bQNwH2de3NgQ',
                               reply_to_message_id=message.message_id)


@dp.message_handler(commands=['egor'])
async def bot_start(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=r"CAACAgIAAxkBAAELD9Zljoxnm_c_kbMeDXbnjKM7Bs3UjQAC5DMAAtAr0UvRtsrwWiqPnTQE")

@dp.message_handler(commands=['idinax'])
async def bot_start(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=r"CAACAgIAAxkBAAELHvNlnPd1pNA-LkabUX_ymdlZKEMyWAACRxgAAm8kYUvWOStTKuDSkzQE")

@dp.message_handler(commands=['alo'])
async def bot_start(message: types.Message):
    await bot.send_animation(message.chat.id, animation=random.choice(
        ['https://media.tenor.com/JgdIUEUnVHwAAAAM/dog-alo.gif', 'https://media.tenor.com/9to_c_qFJtgAAAAM/alo-dog.gif',
         'https://media.tenor.com/Rxv1zg0HTiEAAAAM/alo-phona.gif']))


@dp.message_handler(commands=['salam'])
async def bot_start(message: types.Message):
    await bot.send_animation(message.chat.id, animation='https://tenor.googleapis.com/v2/media?id=15374560520306509995&format=optimizedgif&client_key=tenor_web&appversion=browser-r20241030-1&access_token=ya29.a0AeDClZD4ksRXU-iexB7D7duCvCNcXAWAbgpj0x3YVAxdreIdeYbawbkh5CTz0nP_cWXNZYDcr5t4ysgSHvlGF69dIxkbvdZgjMMy63FQ5jPMBJIcnmu1bAxU-rfaEWiK_XFVOyoAMw3A3dnun--AQX1eCW2ytliiZgaCgYKAXgSARMSFQHGX2MipuoUynvw3Nqj98ohvlVqLA0169&key=AIzaSyC-P6_qz3FzCoXGLk6tgitZo4jEJ5mLzD8')

@dp.message_handler(commands=['new'])
async def bot_start(message: types.Message):
    await bot.send_animation(message.chat.id, animation='https://media1.tenor.com/m/odH89hBnjhIAAAAd/%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%B9.gif')

@dp.message_handler(commands=['reznya'])
async def bot_start(message: types.Message):
    await bot.send_sticker(message.chat.id, sticker=r'CAACAgIAAxkBAAEJ-L1nMw2TsRidNLimPP2o7eeJoh01EAAC22IAAvy1mEk-HNRKJzgXajYE')


@dp.message_handler(commands=['pizdec'])
async def bot_start(message: types.Message):
    await bot.send_sticker(message.chat.id, sticker=r'CAACAgIAAxkBAAEJ-MdnMw81EY12mMbEqB7zh0Ijvq1yewACn08AAuAOmUkYs4M3F32wCTYE')


@dp.message_handler(commands=['bug'])
async def bot_start(message: types.Message):
    await bot.send_sticker(message.chat.id, sticker=r'CAACAgIAAxkBAAEJ-MlnMxAPluzcRAukWihkusHahHFIMgAC8VYAAoI3-EhSsnkAAYk7O_w2BA')


@dp.message_handler(commands=['zv'])
async def bot_start(message: types.message):
    await bot.send_sticker(message.chat.id, sticker=r'CAACAgIAAxkBAAEJ-L9nMw3nJcTzgJ13SE8hB6s4sfKSCgACtFcAAnkEmEk-xcu3Y34lTDYE')


@dp.message_handler(commands=['vibor'])
async def bot_start(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEKCS1nNZ5IWgwpTbrXLRNAi00haHopEQACeAIAAtzyqwchI2WJ2IRufjYE")
    thinking_message = await bot.send_message(chat_id=message.chat.id, text="Думаю...")
    await asyncio.sleep(3)
    await bot.delete_message(chat_id=message.chat.id, message_id=thinking_message.message_id)
    result = random.choice(['красное', 'синее'])
    await bot.send_message(chat_id=message.chat.id, text=f"Я выбираю: {result}")


@dp.message_handler(commands=['charles'])
async def bot_start(message: types.Message):
    response_text = f'Вот пошагавая инструкция как настроить Charles на пк и мобильном ус-ве - <a href="https://wiki.yandex.ru/napravlenija-kompanii/qa/qa-manual/spravochnik-manual/pogruzhenie-v-mir-charles/">Инструкция</a>'
    await bot.send_message(message.chat.id, text=response_text, reply_to_message_id=message.message_id, parse_mode="HTML")


def get_value(file_name, day):
    with open(file_name, 'r') as file:
        for line in file:
            data = json.loads(line)
            if data['date'] == day:
                return data['username']
    return False

@dp.message_handler(commands=['day_gandon'])
async def get_gandon_tg(message: types.Message):
    chat_id = message.chat.id
    month_history = get_chat_history_file(loh_history_month, chat_id)
    year_history = get_chat_history_file(loh_history_year, chat_id)
    ensure_file_exists(month_history)

    today = get_today()
    today_month = today[:7]

    current_month_present = False
    with open(month_history, 'r') as file:
        for line in file:
            data = json.loads(line)
            if data['date'].startswith(today_month):
                current_month_present = True
                break

    if not current_month_present:
        fill_json(month_history, year_history)
        backup_file(month_history)
        clear_json(month_history)

    elif today in year_list:
        fill_json(year_history, get_chat_history_file(loh_history_decade, chat_id))
        backup_file(year_history)
        clear_json(year_history)

    if get_value(month_history, today):
        await message.answer(f"ОТЪЕБИСЬ ГАНДОН УЖЕ ВЫБРАН, ЭТО @{get_value(month_history, today)}")
    else:
        members = await bot.get_chat_administrators(chat_id)
        logins = [member.user.username for member in members if member.user.username]
        logins.remove('Rabotyaga_bedniy_bot')
        loh = random.choice(logins)
        loh_entry = {"date": today, "username": loh}
        with open(month_history, "a") as f:
            json.dump(loh_entry, f)
            f.write('\n')
        await message.answer(f"ГАНДОН ДНЯ: @{loh}")
        await bot.send_sticker(chat_id=chat_id,
                               sticker=r"CAACAgIAAxkBAAELDF9ljAiMnv8y7qNh6QkOQf-sDAtDcAACCiYAArkQaEksYoQTtEf5LTME")

@dp.message_handler(commands=['month_gandon', 'year_gandon', 'decade_gandon'])
async def handle_gandon_command(message: types.Message):
    command = message.get_command()
    period_type = command.split('_')[0][1:]
    await get_gandon(message, period_type)


@dp.message_handler(commands=['month_gandons'])
async def month_gandons(message: types.Message):
    chat_id = message.chat.id
    loh_history_month = get_chat_history_file(chat_id, "loh_history_month")
    ensure_file_exists(loh_history_month)
    with open(loh_history_month, "r") as f:
        data = [json.loads(line) for line in f]
    if not data:
        await message.answer("За этот месяц еще не было выбрано ни одного гандона.")
        return
    user_counts = {}
    for entry in data:
        username = entry['username']
        user_counts[username] = user_counts.get(username, 0) + 1
    sorted_users = sorted(user_counts.items(), key=lambda x: x[1], reverse=True)
    grouped_users = {}
    for username, count in sorted_users:
        if count not in grouped_users:
            grouped_users[count] = []
        grouped_users[count].append(username)
    result = "Список гандонов по дням за месяц:\n"
    max_count = sorted_users[0][1]
    position = 1
    for count in sorted(grouped_users.keys(), reverse=True):
        users = grouped_users[count]
        if count == max_count:
            result += f"{position}. " + ', '.join([f"@{user}" for user in users]) + f" ({count} раз) 👑\n"
        else:
            result += f"{position}. " + ', '.join([f"@{user}" for user in users]) + f" ({count} раз)\n"
        position += 1
    await message.answer(result)


async def get_gandon(message: types.Message, period_type):
    chat_id = message.chat.id
    try:
        if period_type == 'month':
            history = get_chat_history_file(loh_history_month, chat_id)
            period_name = "МЕСЯЦА"
        elif period_type == 'year':
            history = get_chat_history_file(loh_history_year, chat_id)
            period_name = "ГОДА"
        elif period_type == 'decade':
            history = get_chat_history_file(loh_history_decade, chat_id)
            period_name = "ДЕСЯТИЛЕТИЯ"
        loh, count = await calculate_gandon(history)
        if not loh:
            await message.answer("ПОШЕЛ ТЫ")
        elif len(loh) == 1:
            msg = f'ГАНДОН {period_name}: @{loh[0]}, ЧИСЛО ДНЕЙ ГАНДОНСТВА - {count}'
        else:
            msg = f'ГАНДОНЫ {period_name}: {" ".join(f"@{i}" for i in loh)}, ЧИСЛО ДНЕЙ ГАНДОНСТВА - {count}'
        await message.answer(msg)
    except Exception:
        await message.answer("ТЫ ГАНДОН")


async def calculate_gandon(file):
    loh_counts = {}
    with open(file, "r") as f:
        for line in f:
            entry = json.loads(line)
            loh_username = entry["username"]
            if loh_username in loh_counts:
                loh_counts[loh_username] += 1
            else:
                loh_counts[loh_username] = 1
    loh_of_the_month = max(loh_counts, key=loh_counts.get)
    loh = [x for x in loh_counts.keys() if loh_counts[x] == loh_counts[loh_of_the_month]]
    return loh, loh_counts[loh_of_the_month]

@dp.message_handler(commands=['random'])
async def bot_random(message: types.Message):
    await message.answer(f"{random.choice(['Идем в бар', 'Идем в боулинг', 'Никуда нахуй'])}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
