#coding:utf-8
import random
from janome.tokenizer import Tokenizer

def create_base_data(filename, outfile, add_line, limit):
	file = open(filename,'r', encoding="utf-8")
	data = file.readlines()
	file.close()
	data = random.sample(data, limit)  # ランダムに何行か抜く
	# ファイルに書き出し
	file = open(outfile, 'w', encoding='utf-8')
	for line in data:
		file.write(line)
	file.write(add_line)
	file.close()

def wakati(text):
	text = text.replace('\n','') #改行を削除
	text = text.replace('\r','') #スペースを削除
	t = Tokenizer()
	result =t.tokenize(text, wakati=True)
	return result

#デフォルトの文の数は5
def generate_text(num_sentence=10):
	filename = "messages_759750762262691871.txt"
	src = open(filename, "r").read()
	wordlist = wakati(src)
	print(wordlist)

	#マルコフ連鎖用のテーブルを作成
	markov = {}
	w1 = ""
	w2 = ""
	for word in wordlist:
		if w1 and w2:
			if (w1, w2) not in markov:
				markov[(w1, w2)] = []
			markov[(w1, w2)].append(word)
		w1, w2 = w2, word

	#文章の自動生成
	count_kuten = 0 #句点「。」の数
	num_sentence= num_sentence
	sentence = ""
	w1, w2  = random.choice(list(markov.keys()))

	while count_kuten < num_sentence:
		print(w1,w2)
		tmp = random.choice(markov[(w1, w2)])
		sentence += tmp
		if(tmp=='。'):
			count_kuten += 1
			sentence += ''
		elif('だろ' in tmp):
			count_kuten += 1
			sentence += ''
		elif('だよ' in tmp):
			count_kuten += 1
			sentence += ''
		elif('した' in tmp):
			count_kuten += 1
			sentence += ''
		w1, w2 = w2, tmp
		count_kuten += 1

	print(sentence)
	return sentence