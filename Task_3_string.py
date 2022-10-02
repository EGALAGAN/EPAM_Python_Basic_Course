import re
initial_text = """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

print(initial_text)

# normalize it from letter cases point of view
# split the text by two end-line characters
list1 = initial_text.split('\n\n  ')
list2 = []
# print(list1)
for i in range(len(list1)):
    # split on the sentences by dots
    list11 = list1[i].capitalize().split('. ')
    list22 = []
    for j in range(len(list11)):
        #Capitalize the first words of the sentences
        list22.append(list11[j].capitalize())
    # join sentences
    edited_text2 = '. '.join(list22)
    list2.append(edited_text2)
# join parts back
final_text1 = '\n\n  '.join(list2)
print('------')
print(final_text1)

# create one more sentence with last words of each existing sentence
new_sentence = ' '.join(re.findall('([a-zA-Z]+)\.', final_text1)).capitalize()+'.'
# print(re.findall('([a-zA-Z]+)\.', final_text1))
# print(new_sentence)

# and add it to the end of this paragraph
list3 = []
for a in final_text1.split('\n'):
    # find the appropriate place for new sentence
    if a.endswith('paragraph.'):
        list3.append(a+' '+new_sentence)
        # print(a+' '+new_sentence)
    else:
        list3.append(a)
        # print(a)
final_text2 = '\n'.join(list3)
print('----')
print(final_text2)

# correct mistakes
print('----')
final_text3 = final_text2.replace(' iz ', ' is ').replace(' tex.', ' text.').replace('Fix“iz”', 'Fix “iz”')
print(final_text3)


print('----')
# calculate number of whitespace characters
cnt_whitespaces = 0
for i in initial_text:
    if i.isspace():
        cnt_whitespaces += 1
print('cnt_whitespaces = ', cnt_whitespaces)

