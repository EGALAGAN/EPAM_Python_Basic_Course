
import random
import string


# 1. create a list of random number of dicts (from 2 to 10)
def func_create_list_of_dict(n_list_start=2, n_list_end=10, dict_size=5, n_dict_val=100):
    return_dict_list = []
    for i in range(random.randint(n_list_start, n_list_end)): # random number of dictionaries (from 2 to 10)
        size = random.randint(1, dict_size)    # random dictionary size (for example, 1-5)
        keys = random.sample(string.ascii_lowercase, size)  # random letters
        values = (random.randint(0, n_dict_val) for i in range(size))  # random number for values
        # create dictionary from tuples, that generated by iterator zip
        one_dict = dict(zip(keys, values))
        # add it to the list
        return_dict_list.append(one_dict)
    return return_dict_list


# 2 get previously generated list of dicts and create one common dict
def get_common_dict_from_list(param_dict_list):
    return_final_dict = {}
    checked_list = []  # list for already checked keys
    # loop for each dictionary
    for i in range(len(param_dict_list)):
        current_list = param_dict_list[i]
        # loop for each key
        for current_key, current_value in current_list.items():
            final_key = current_key
            final_value = current_value
            checked_key = current_key
            # loop for comparing value of current key with other values of the rest dictionaries
            for i_nextList in range(i+1, len(param_dict_list)):
                try:
                    # if dicts have same key, we will take max value, and rename key with dict number with max value
                    tmp_value = param_dict_list[i_nextList][current_key]
                    if tmp_value > current_value:
                        final_key = current_key + '_' + str(i_nextList+1)
                        final_value = tmp_value
                except:
                    pass
            # avoiding double-check already checked keys
            if checked_key not in checked_list:
                return_final_dict[final_key] = final_value
            checked_list.append(checked_key)

    return return_final_dict


def get_common_dict_from_random_list(n_list_start=2, n_list_end=10, dict_size=5, n_dict_val=100):
    dict_list = func_create_list_of_dict(n_list_start, n_list_end, dict_size, n_dict_val)
    print(dict_list)

    return_final_dict = get_common_dict_from_list(dict_list)
    print(return_final_dict)

    return return_final_dict


final_dict = get_common_dict_from_random_list()

################################

import re


# normalize it from letter cases point of view
def get_normal_text(param_initial_text):
    # split the text by two end-line characters
    list1 = param_initial_text.split('\n\n  ')
    list2 = []
    # print(list1)
    for i in range(len(list1)):
        # split on the sentences by dots
        list11 = list1[i].capitalize().split('. ')
        list22 = []
        for j in range(len(list11)):
            # Capitalize the first words of the sentences
            list22.append(list11[j].capitalize())
        # join sentences
        edited_text2 = '. '.join(list22)
        list2.append(edited_text2)
    # join parts back
    return_final_text1 = '\n\n  '.join(list2)
    return return_final_text1


# create one more sentence with last words of each existing sentence
def get_sentence_from_last_words(param_final_text1, param_place_for_new_sentence='paragraph.'):
    new_sentence = ' '.join(re.findall('([a-zA-Z]+)\.', param_final_text1)).capitalize() + '.'
    # print(re.findall('([a-zA-Z]+)\.', final_text1))
    # print(new_sentence)

    # and add it to the end of this paragraph
    list3 = []
    for a in param_final_text1.split('\n'):
        # find the appropriate place for new sentence
        if a.endswith(param_place_for_new_sentence):
            list3.append(a + ' ' + new_sentence)
            # print(a+' '+new_sentence)
        else:
            list3.append(a)
            # print(a)
    return_final_text2 = '\n'.join(list3)
    return return_final_text2


# correct mistakes
def get_corrected_text(param_final_text2):
    return_final_text3 = param_final_text2.replace(' iz ', ' is ').replace(' tex.', ' text.').replace('Fix“iz”', 'Fix “iz”')
    return return_final_text3


# calculate number of whitespace characters
def qet_num_whitespaces(param_initial_text):
    return_cnt_whitespaces = 0
    for i in param_initial_text:
        if i.isspace():
            return_cnt_whitespaces += 1
    return return_cnt_whitespaces



initial_text = """homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

print(initial_text)

final_text1 = get_normal_text(initial_text)
print('------')
print(final_text1)

final_text2 = get_sentence_from_last_words(param_final_text1=final_text1, param_place_for_new_sentence='paragraph.')
print('----')
print(final_text2)

final_text3 = get_corrected_text(final_text2)
print('----')
print(final_text3)

cnt_whitespaces = qet_num_whitespaces(initial_text)
print('cnt_whitespaces = ', cnt_whitespaces)
print('----')