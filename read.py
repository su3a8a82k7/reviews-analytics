data = []
count = 0
with open('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))		
print('讀取完了, 總共有', len(data), '筆')

sum_len = 0
for d in data:
	sum_len +=  len(d)
	
print('留言平均字數為:', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('小於100字一共有', len(new), '筆')
print(new[0])
print(new[1])		