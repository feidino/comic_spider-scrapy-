import requests,json,random

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
url = 'https://www.shanbay.com/api/v1/vocabtest/category/?_=1589184801513'
res = requests.get(url,headers = header)
print(res.status_code)
res_json = json.loads(res.text)
choice_dict = {}
n = 0
print('出题范围：\n')
for name_id,name in res_json['data']:
    n += 1
    print('%d、 %s'%(n,name))
    choice_dict[str(n)] = name_id
choice = input('请你输入以上出题范围的数字选择你的考核类型：')

if choice == '10':
    num = random.randint(1,9)
    choice_id = choice_id = choice_dict[str(num)]
else:
    choice_id = choice_dict[choice]

real_url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=%s&_=1589184801513'%(choice_id)
word_res = requests.get(real_url ,headers = header)
word_res_json = json.loads(word_res.text)
word_dict = {}
word_answer = {}
for word in word_res_json['data']:
    word_key = word['content']
    choice_0 = word['definition_choices'][0]['definition']
    choice_0_pk= word['definition_choices'][0]['pk']
    choice_0_rank= word['definition_choices'][0]['rank']
    choice_1 = word['definition_choices'][1]['definition']
    choice_1_pk= word['definition_choices'][1]['pk']
    choice_1_rank= word['definition_choices'][1]['rank']
    choice_2 = word['definition_choices'][2]['definition']
    choice_2_pk= word['definition_choices'][2]['pk']
    choice_2_rank= word['definition_choices'][2]['rank']
    choice_3 = word['definition_choices'][3]['definition']
    choice_3_pk= word['definition_choices'][3]['pk']
    choice_3_rank= word['definition_choices'][3]['rank']
    word_rank = word['rank']
    word_pk = word['pk']
    word_dict[word_key] = [[choice_0,choice_0_pk,choice_0_rank],[choice_1,choice_1_pk,choice_1_rank],
                            [choice_2,choice_2_pk,choice_2_rank],[choice_3,choice_3_pk,choice_3_rank]]
    word_answer[word_key] = [word_pk,word_rank]
word_knows = []
word_n0tknows = []
word_list = word_dict.values()
for word_name in word_dict.keys():
    print('—'*30)
    print(word_name)
    print('—'*30)
    user_choice = input('请问认识这个单词吗？\n认识请输入按enter,不认识请输入0：')
    if user_choice == '0':
        word_n0tknows.append(word_name)
    else:
        word_knows.append(word_name)
print('您一共认识%d个单词,分别是：%s'%(len(word_knows),','.join(word_knows)))

right_answer = []
rank_score = 0
pk_score = 0
for word_know in word_knows:
    print(word_know)
    for i in range(4):
        print('%d、 %s'%(i+1,word_dict[word_know][i][0]))
    print('\n')
    user_c = int(input('单词测试，选择正确的词义，请输入你认为正确的答案前面的数字：\n'))
    c_num = user_c - 1
    if word_answer[word_know][0] == word_dict[word_know][c_num][1]:
        right_answer.append(word_know)
        pk_score += word_dict[word_know][c_num][1]
        rank_score += word_dict[word_know][c_num][2]
    else:
        word_n0tknows.append(word_know)
print('\n50个单词，您一共认识%d个单词,不认识%d,掌握%d个单词，错了%d个单词'%(len(word_knows),50-len(word_knows),len(right_answer),len(word_knows)-len(right_answer)))

# print(real_url)
# print(word_res_json)
# print(word_dict)
# print(word_answer)
