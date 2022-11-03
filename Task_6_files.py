import datetime
import Module_Task_4_Functions as Mod4

class ClassData():
    def __init__(self):
        self.pbl_text = ''
        self.pbl_file =  'newsfeed.txt'
        self.pbl_date = None

    def upload_pbl(self, *args):
        f = open(self.pbl_file, 'a', encoding = 'utf8')  # open for writing
        for line in args:
            print(line)
            f.write((line+'\n'))
        f.write('\n')
        f.write('\n')
        f.close()

    def get_pbl_date(self):
        self.pbl_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

    def ask_pbl_text(self,ask_text):
        print(ask_text)
        self.pbl_text = str(input())

    def ask_pbl_xxx(self,ask_text):
        print(ask_text)
        return str(input())

    def remove_file(self, fpath):
        import os
        ## If file exists, delete it ##
        if os.path.isfile(fpath):
            os.remove(fpath)

class ClassNews(ClassData):
    def __init__(self):
        super().__init__()
        self.pbl_title = 'News -------------------------'
        self.pbl_city = ''

    def publish(self):
        self.ask_pbl_city()
        self.ask_pbl_text('Type News:')
        self.get_pbl_date()
        self.upload_pbl(self.pbl_title, self.pbl_text, self.pbl_city+', '+self.pbl_date, '------------------------------')

    def ask_pbl_city(self):
        print('Type City:')
        self.pbl_city = str(input())


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


class ClassFile(ClassData):
    def __init__(self):
        super().__init__()
        self.pbl_title = 'Information from file -------------------------'
        self.pbl_file_name = ''
        self.pbl_file_path = ''
        self.pbl_full_path_name = ''
        self.pbl_info = ''
        self.pbl_file_content = ''

    def ask_pbl_file(self):
        self.pbl_file_path = self.ask_pbl_xxx('Type the file path (leave empty for default path):')
        self.pbl_file_name = self.ask_pbl_xxx('Type the file name:')
        self.pbl_full_path_name = self.pbl_file_path + self.pbl_file_name

    def get_file_content(self):
        with open(self.pbl_full_path_name, 'r', encoding='utf-8') as file:
            self.pbl_file_content = file.read()  #.replace('\n', '')
            self.pbl_file_content = Mod4.get_normal_text(self.pbl_file_content)
            self.pbl_info = 'Infromation was uploaded ' + self.pbl_date + ' from file: ' + self.pbl_full_path_name
            #print(self.pbl_file_content)

    def publish(self):
        self.ask_pbl_file()
        self.get_pbl_date()
        self.get_file_content()
        self.upload_pbl(self.pbl_title, self.pbl_file_content, self.pbl_info, '------------------------------')
        self.remove_file(self.pbl_full_path_name)


def my_prg():

    print('What kind of publication do you want to publish?\n(1 - News, 2 - Advertising, 3 - Weather, 4 - From file)\nType a number:')
    input_type_pbl = int(input())

    if input_type_pbl == 1:
        obj_pbl = ClassNews()

    elif input_type_pbl == 2:
        obj_pbl = ClassAd()

    elif input_type_pbl == 3:
        obj_pbl = ClassWeather()

    elif input_type_pbl == 4:
        obj_pbl = ClassFile()

    else:
        print('Wrong type. Please try again')
        exit()

    obj_pbl.publish()


if __name__ == '__main__':
    my_prg()

