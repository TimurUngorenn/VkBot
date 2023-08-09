import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(
    token='')
session_api = session.get_api()
longpoll = VkLongPoll(session)
hello_list = ('Привет',
              'Здраствуйте',
              'Хэллоу',
              'И тебе привет',
              'Добброго времени суток')
goodby_list = ('пока',
               'до свидания',
               'досвидос',
               'гудбай')
mem_list = ('photo-155590431_457274896',
            'photo-61166138_457301534',
            'photo-173886253_457245980',
            'photo-173886253_457246004')
filmfantastik_list = ('Звездные войны',
                      'игра пристолов',
                      'последниму игроку приготовься')
filmmult_list = ('Ну погоди',
                 'лунтик',
                 'барбоскины',
                 'три кота')
daun_list = ('приятно познакомиться я искуственный интелект',
             'очень приятно познакомиться',
             'это ваше погоняло?')
filmpsih_list = ('остров проклятых',
                 'обитель проклятых')
ilmbiz_list = ('Основатель',
               'форд против ферари')

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            print('Сообщение пришло в: ' + str(event.datetime))
            print('Текст сообщения: ' + str(event.text))

            response = event.text.lower()
            if event.from_user and not event.from_me:
                if response.find("привет") >= 0 or response.find('здравствуй') >= 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': random.choice(hello_list), 'random_id': 0})


                elif response.find("пока") >= 0 or response.find('до свидания') >= 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': random.choice(goodby_list), 'random_id': 0})



                elif response.find("как дел") >= 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': 'отлично у тебя как?', 'random_id': 0})
                elif response.find("что делаешь") >= 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': 'сижу а ты ?', 'random_id': 0})
                elif response.find("скинь прикол") >= 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': 'https://www.youtube.com/shorts/smFtz_YEC8w',
                                                     'random_id': 0, 'sticker_id': 10223})

                elif response.find("мне грустно") >= 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': 'https://www.youtube.com/shorts/smFtz_YEC8w',
                                                     'random_id': 0, 'sticker_id': 9011})
                elif response.find("хочу kfc") >= 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'message': 'негр тоже хотел', 'random_id': 0})
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0,
                                                     'attachment': 'photo700422692_457239725%2Fphotos700422692'})
                elif response == "зеркало":
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'attachment': 'audio-2001138153_120138153'})
                elif response == "мирта":
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'attachment': 'photo700422692_457239726'})
                elif response == "мем":
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'attachment': random.choice(mem_list),
                                                     'random_id': 0})
                elif response == "фильм фантастика":
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'message': random.choice(filmfantastik_list),
                                                     'random_id': 0})
                elif response == "фильм мультик":
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'message': random.choice(filmmult_list),
                                                     'random_id': 0})
                elif response.find("мультик") > 0 and response.find("фильм") > 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'message': random.choice(filmmult_list),
                                                     'random_id': 0})
                elif response.find("фантастика") > 0 and response.find("фильм") > 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'message': random.choice(filmfantastik_list),
                                                     'random_id': 0})
                elif response.find("даун") > 0 :
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'message': random.choice("daun_list"),
                                                     'random_id': 0})
                elif response == 'справка':
                    session.method('messages.send', {"user_id": event.user_id,
                                                     'message': 'Привет! Я бот.Напиши мне мем,''что бы я отправил тебе мем,''\n Привет! Я бот.Напиши мне фильм\",''что бы я отправил тебе фидьм, \nПривет! Я бот.Напиши мне \"мультик\",что бы я отправил тебе мультик, \n Привет! Я бот.Напиши мне \"зеркало",что бы я отправил тебе песню зеркало, \n Привет! Я бот.Напиши мне "фантастика",что бы я отправил тебе фильм фантастика, \n Привет! Я бот.Напиши мне "мне грустно",что бы я отправил тебе смешное видео, \n Привет! Я бот.Напиши мне "скинь прикол",что бы я отправил тебе прикольное видео',
                                                     'random_id': 0})
                elif response.find("про психушку") > 0 and response.find("фильм") > 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'message': random.choice(filmpsih_list),
                                                     'random_id': 0})
                elif response.find("про созданния бизнеса") > 0 and response.find("фильм") > 0:
                    time.sleep(random.uniform(0.5, 2.0))
                    session.method('messages.send', {'user_id': event.user_id,
                                                     'random_id': 0, 'message': random.choice(filmbiz_list),
                                                     'random_id': 0})












