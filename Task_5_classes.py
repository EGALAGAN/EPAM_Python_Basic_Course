import datetime


class ClassData():
    def __init__(self):
        self.pbl_text = ''
        self.pbl_file = 'C:\\Users\\Ekaterina_Galagan\\PycharmProjects\\pythonProject\\newsfeed.txt'

    def upload_pbl(self, *args):
        f = open(self.pbl_file, 'a+b')  # open for writing
        for line in args:
            print(line)
            f.write((line+'\n').encode("utf8"))
        f.write('\n'.encode("utf8"))
        f.write('\n'.encode("utf8"))
        f.close()


    def ask_pbl_text(self,ask_text):
        print(ask_text)
        self.pbl_text = str(input())


class ClassNews(ClassData):
    def __init__(self):
        super().__init__()
        self.pbl_title = 'News -------------------------'
        self.pbl_city = ''
        self.pbl_date = None

    def publish(self):
        self.ask_pbl_city()
        self.ask_pbl_text('Type News:')
        self.get_pbl_date()
        self.upload_pbl(self.pbl_title, self.pbl_text, self.pbl_city+', '+self.pbl_date, '------------------------------')

    def ask_pbl_city(self):
        print('Type City:')
        self.pbl_city = str(input())

    def get_pbl_date(self):
        self.pbl_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')


class ClassAd(ClassData):
    def __init__(self):
        super().__init__()
        self.pbl_title = 'Ad -------------------------'
        self.pbl_expiration_date = None
        self.pbl_left_days = None
        self.date_format = '%d/%m/%Y'

    def publish(self):
        self.ask_pbl_text('Type Ad:')
        self.ask_pbl_expiration_date()
        self.get_pbl_left_days()
        self.upload_pbl(self.pbl_title, self.pbl_text, 'Actual until: '+self.pbl_expiration_date.strftime(self.date_format)+', '+(self.pbl_left_days)+' days left', '------------------------------')

    def ask_pbl_expiration_date(self):
        print('Type the Expiration Date in the dd/mm/yyyy format:')
        try:
            self.pbl_expiration_date = datetime.datetime.strptime(input(), self.date_format)
        except:
            print('Wrong format. Publication cancelled')
            exit()

    def get_pbl_left_days(self):
        self.pbl_left_days = str((self.pbl_expiration_date - datetime.datetime.now()).days)
        # print('left days are: '+str(self.pbl_left_days))


class ClassWeather(ClassData):
    def __init__(self):
        super().__init__()
        self.pbl_title = 'Weather -------------------------'
        self.pbl_city = ''
        self.pbl_temperature = ''
        self.pbl_smile = "\U0001F60E"
        self.pbl_sad = "\U0001F976"
        self.pbl_final_mood = None

    def publish(self):
        self.ask_pbl_city()
        self.ask_pbl_temperature()
        self.get_pbl_final_mood()
        self.upload_pbl(self.pbl_title, self.pbl_city, 'The temperature for today is ' + str(self.pbl_temperature)+', '+str(self.pbl_final_mood), '------------------------------')

    def ask_pbl_city(self):
        print('Type City:')
        self.pbl_city = str(input())

    def ask_pbl_temperature(self):
        print('Type the Temperature for today:')
        try:
            self.pbl_temperature = int(input())
        except:
            print('Wrong format. Publication cancelled')
            exit()

    def get_pbl_final_mood(self):
        if int(self.pbl_temperature) >= 10:
            self.pbl_final_mood = self.pbl_smile
        else:
            self.pbl_final_mood = self.pbl_sad


def my_prg():

    print('What kind of publication do you want to publish?\n(1 - News, 2 - Advertising, 3 - Weather)\nType a number:')
    input_type_pbl = int(input())

    if input_type_pbl == 1:
        obj_pbl = ClassNews()

    elif input_type_pbl == 2:
        obj_pbl = ClassAd()

    elif input_type_pbl == 3:
        obj_pbl = ClassWeather()

    else:
        print('Wrong type. Please try again')
        exit()

    obj_pbl.publish()


my_prg()
