import json

with open('toeic_voca.json') as data_file:
    vocas = json.load(data_file)

print("토익 단어 테스트를 시작합니다.")
slang = input("저한테 욕 한마디 해주시겠어요? : ") #정답을 못맞췄을 때 사용
st = int(input("몇 일차를 진행하시겠습니까 ?(숫자만 입력해주세요) : ")) #단어는 200개씩 제공

if st == 1:
    today_words = vocas[:200]
elif st == 2:
    today_words = vocas[200:400]
elif st == 3:
    today_words = vocas[400:600]
elif st == 4:
    today_words = vocas[600:800]
elif st == 5:
    today_words = vocas[800:1000]
else:
    today_words = vocas[1000:]

for today_word in today_words:
    word = list(today_word.keys())[0]
    meaning = list(today_word.values())[0]
    print(meaning)
    answer = input()
    if answer == word:
        print("정답입니다.")
    else:
        print("틀렸어! 정답은 {} 임".format(word), slang)

print("오늘의 단어를 완료했습니다. 프로그램을 종료합니다.")
