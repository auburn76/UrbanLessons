import time

class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user: User = None

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(nickname)
            user = User(nickname, password, age)
            self.current_user = user

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == nickname.password:
                self.current_user = nickname
            else:
                print("Пароль не верный")
        else:
            print("Пользователь не найден. Зарегистрируйтесь.")

    def log_out(self):
        self.current_user = None

    def add(self, *video: Video):
        for i in len(video):
            if video[i].title not in self.videos:
                self.videos.append(video[i].title)

    def get_videos(self, video_name):
        search_video = []
        for i in self.videos:
            if video_name.lower() in self.videos[i].lower:
                search_video.append(self.videos[i].title)

    def watch_video(self, video_name):
        if self.current_user != None:
            if video_name in self.videos:
                if video.adult_mode and self.current_user.age <18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(video.time_now, video.duration):
                        print(i)
                        time.sleep(1)
                    print('Конец видео')
            else:
                print('Видео не существует')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')