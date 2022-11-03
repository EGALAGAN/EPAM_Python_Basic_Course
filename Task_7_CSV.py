import Task_6_files
import csv
import re


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
        'What kind of publication do you want to publish?\n(1 - News, 2 - Advertising, 3 - Weather, 4 - From file, 5 - Refresh statistic)\nType a number:')
    input_type_pbl = int(input())

    if input_type_pbl == 1:
        obj_pbl = Task_6_files.ClassNews()

    elif input_type_pbl == 2:
        obj_pbl = Task_6_files.ClassAd()

    elif input_type_pbl == 3:
        obj_pbl = Task_6_files.ClassWeather()

    elif input_type_pbl == 4:
        obj_pbl = Task_6_files.ClassFile()

    elif input_type_pbl == 5:
        refresh_statistic()
        exit()

    else:
        print('Wrong type. Please try again')
        exit()

    obj_pbl.publish()
    write_statistic(p_source_file=obj_pbl.pbl_file)


if __name__ == '__main__':
    my_prg_and_statistic()
