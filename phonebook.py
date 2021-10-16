import re
import csv

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
temp_list = []
cnt = 0
for contact in contacts_list:
  temp_list.append([])
  for i in contact[0:3]:
    if i != '':
      for j in i.split(' '):
        temp_list[cnt].append(j)
  if len(temp_list[cnt]) < 3:
    temp_list[cnt].append('')
  cnt += 1

cnt = 0
for organization in contacts_list:
  for i in organization[3:5]:
    temp_list[cnt].append(i)
  cnt += 1

regex_pattern = r'(\+7|8)?\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s*\(?(\w*.)?\s*(\d{4})?\)?'
subst = r'+7(\2)\3-\4-\5 \6\7'

cnt = 0
for contact in contacts_list:
  correct_phone_number = re.sub(regex_pattern, subst, contact[5])
  temp_list[cnt].append(correct_phone_number)
  temp_list[cnt].append(contact[6])
  cnt += 1

correct_list = []
correct_list.append(temp_list[0])
for contact in temp_list[1:]:
    flag = 0
    for correct_contact in correct_list:
        if contact[0] == correct_contact[0] and contact[1] == correct_contact[1]:
            for i in range(2, len(correct_contact)):
                if correct_contact[i] == '':
                    correct_contact[i] = contact[i]
            flag += 1
    if flag == 0:
        correct_list.append(contact)

# TODO 2: сохраните получившиеся данные в другой файл
with open("correct_phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(correct_list)