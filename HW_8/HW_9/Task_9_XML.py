import json
import datetime
import csv
import re
import Module_Task_4_Functions as Mod4
import xml.etree.ElementTree as ET

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


class ClassFileJSON(ClassFile):
    def __init__(self):
        super().__init__()
        self.pbl_js_body = None

    def get_json_file(self):
        self.ask_pbl_file()
        self.pbl_js_body = json.load(open(self.pbl_full_path_name))

    def publish(self):
        self.get_json_file()
        for __js_pbl in self.pbl_js_body["publish"]:
            # print(js_pbl["title"])

            if __js_pbl["title"] == 'Ad':
                __my_json_obj = ClassAd()
                __my_json_obj.pbl_text = __js_pbl["text"]
                __my_json_obj.pbl_expiration_date = datetime.datetime.strptime(__js_pbl["expiration_date"], __my_json_obj.date_format)
                __my_json_obj.get_pbl_left_days()
                __my_json_obj.upload_pbl(__my_json_obj.pbl_title, __my_json_obj.pbl_text,
                                  'Actual until: ' + __my_json_obj.pbl_expiration_date.strftime(__my_json_obj.date_format) + ', ' + (
                                      __my_json_obj.pbl_left_days) + ' days left', '------------------------------')

            if __js_pbl["title"] == 'News':
                __my_json_obj = ClassNews()
                __my_json_obj.pbl_city = __js_pbl["city"]
                __my_json_obj.pbl_text = __js_pbl["text"]
                __my_json_obj.get_pbl_date()
                __my_json_obj.upload_pbl(__my_json_obj.pbl_title, __my_json_obj.pbl_text, __my_json_obj.pbl_city + ', ' + __my_json_obj.pbl_date,
                                  '------------------------------')

            if __js_pbl["title"] == 'Weather':
                __my_json_obj = ClassWeather()
                __my_json_obj.pbl_city = __js_pbl["city"]
                __my_json_obj.pbl_temperature = __js_pbl["temperature"]
                __my_json_obj.get_pbl_final_mood()
                __my_json_obj.upload_pbl(__my_json_obj.pbl_title, __my_json_obj.pbl_city,
                                  'The temperature for today is ' + str(__my_json_obj.pbl_temperature) + ', ' + str(
                                      __my_json_obj.pbl_final_mood), '------------------------------')
        self.remove_file(self.pbl_full_path_name)


class ClassFileXML(ClassFile):
    def __init__(self):
        super().__init__()
        self.pbl_xml_body = None
        self.pbl_xml_root = None

    def get_json_file(self):
        self.ask_pbl_file()
        self.pbl_xml_body = ET.parse(self.pbl_full_path_name)
        self.pbl_xml_root = self.pbl_xml_body.getroot()

    def publish(self):
        self.get_json_file()
        for __xml_pbl in self.pbl_xml_root.findall('pb'):
            # print(__xml_pbl.get('title'))
            if __xml_pbl.get('title') == 'Ad':
                __my_xml_obj = ClassAd()
                __my_xml_obj.pbl_text = __xml_pbl.find('text').text
                __my_xml_obj.pbl_expiration_date = datetime.datetime.strptime(__xml_pbl.find('expiration_date').text, __my_xml_obj.date_format)
                __my_xml_obj.get_pbl_left_days()
                __my_xml_obj.upload_pbl(__my_xml_obj.pbl_title, __my_xml_obj.pbl_text,
                                  'Actual until: ' + __my_xml_obj.pbl_expiration_date.strftime(__my_xml_obj.date_format) + ', ' + (
                                      __my_xml_obj.pbl_left_days) + ' days left', '------------------------------')

            if __xml_pbl.get('title') == 'News':
                __my_xml_obj = ClassNews()
                __my_xml_obj.pbl_city = __xml_pbl.find('city').text
                __my_xml_obj.pbl_text = __xml_pbl.find('text').text
                __my_xml_obj.get_pbl_date()
                __my_xml_obj.upload_pbl(__my_xml_obj.pbl_title, __my_xml_obj.pbl_text, __my_xml_obj.pbl_city + ', ' + __my_xml_obj.pbl_date,
                                  '------------------------------')

            if __xml_pbl.get('title') == 'Weather':
                __my_xml_obj = ClassWeather()
                __my_xml_obj.pbl_city = __xml_pbl.find('city').text
                __my_xml_obj.pbl_temperature = __xml_pbl.find('temperature').text
                __my_xml_obj.get_pbl_final_mood()
                __my_xml_obj.upload_pbl(__my_xml_obj.pbl_title, __my_xml_obj.pbl_city,
                                  'The temperature for today is ' + str(__my_xml_obj.pbl_temperature) + ', ' + str(
                                      __my_xml_obj.pbl_final_mood), '------------------------------')
        self.remove_file(self.pbl_full_path_name)


def write_statistic(p_source_file = 'newsfeed.txt', p_word_cnt_file='word_cnt.csv', p_letters_cnt_file='letters_cnt.csv'):
    # f_csv1 = 'word_cnt.csv'
    # f_csv2 = 'letters_cnt.csv'
    f_csv1 = p_word_cnt_file
    f_csv2 = p_letters_cnt_file
    my_headers = ['letter','count_all','count_uppercase','percentage']

    # with open('newsfeed.txt', 'r', encoding='utf-8') as f:
    with open(p_source_file, 'r', encoding='utf-8') as f:
        f_body = f.read()
        str_body = ' '.join(f_body.split('\n'))
        list_body = str_body.replace(',', '').replace(';', '').lower().split(' ')
        # print(list_body)

        checkedlist = []  # list for already checked words

        with open(f_csv1, 'w', encoding='utf8', newline='') as f1:  # open for writing
            fwriter = csv.writer(f1, delimiter='-')

            # loop for each word
            for i in range(len(list_body)):
                current_word = list_body[i]
                cnt = 0
                # avoiding double-check already checked words
                if current_word not in checkedlist:
                    for k in range(i, len(list_body)):
                        if current_word == list_body[k]:
                            cnt += 1
                    # print(f'{current_word} - {cnt}')
                    fwriter.writerow([current_word, cnt])
                    checkedlist.append(current_word)
        ##########

        with open(f_csv2, 'w', encoding='utf8', newline='') as f2:  # open for writing
            fwriter2 = csv.DictWriter(f2, fieldnames=my_headers)
            fwriter2.writeheader()

            checkedListLetter = []  # list for already checked letters
            letters_body = re.findall('([a-zA-Z])', f_body)
            # print(len(letters_body),letters_body)

            for i in range(len(letters_body)):
                current_letter = letters_body[i]
                cnt_letter = 0
                cnt_letter_upper = 0

                # avoiding double-check already checked words
                if current_letter not in checkedListLetter:
                    for k in range(i, len(letters_body)):
                        if current_letter.upper() == letters_body[k].upper():
                            cnt_letter += 1
                        if current_letter.upper() == letters_body[k]:
                            cnt_letter_upper += 1
                    checkedListLetter.append(current_letter.upper())
                    checkedListLetter.append(current_letter.lower())

                    # print(current_letter,cnt_letter,cnt_letter_upper, round((cnt_letter/len(letters_body))*100,2))
                    fwriter2.writerow({'letter':current_letter, 'count_all':cnt_letter, 'count_uppercase':cnt_letter_upper,'percentage':round((cnt_letter/len(letters_body))*100,2)})
    # print(checkedListLetter)

    # print(finalDict)
    # print(checkedList)


def refresh_statistic():
    write_statistic()


def my_prg_and_statistic():

    print(
        'What kind of publication do you want to publish?\n(1 - News, 2 - Advertising, 3 - Weather, 4 - From file, 5 - Refresh statistic, 6 - From JSON file, 7 - From XML file)\nType a number:')
    input_type_pbl = int(input())

    if input_type_pbl == 1:
        obj_pbl = ClassNews()

    elif input_type_pbl == 2:
        obj_pbl = ClassAd()

    elif input_type_pbl == 3:
        obj_pbl = ClassWeather()

    elif input_type_pbl == 4:
        obj_pbl = ClassFile()

    elif input_type_pbl == 5:
        refresh_statistic()
        exit()

    elif input_type_pbl == 6:
        obj_pbl = ClassFileJSON()

    elif input_type_pbl == 7:
        obj_pbl = ClassFileXML()

    else:
        print('Wrong type. Please try again')
        exit()

    obj_pbl.publish()
    write_statistic(p_source_file=obj_pbl.pbl_file)


if __name__ == '__main__':
    # can be used for a test:
    # my_xml_file = ET.parse('my_xml.xml')
    # my_xml_file.write('x.xml')

    my_prg_and_statistic()



# XML example:
# <publish>
#     <pb title="News">
#         <city>London</city>
#         <text>New Karol</text>
#     </pb>
#     <pb title="Ad">
#         <text>sale BIG BEN $1</text>
#         <expiration_date>01/12/2022</expiration_date>
#     </pb>
#     <pb title="Weather">
#         <city>London</city>
#         <temperature>50</temperature>
#     </pb>
# </publish>
