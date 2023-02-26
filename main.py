import os
with open('result/final_file.txt', 'w') as full:
    q = {}
    for i in os.listdir():
        if i.endswith('.txt'):
            with open(i, encoding='utf-8') as f:
                lines = len(f.readlines())
                q[i] = lines
                q_sort = sorted(q.items(), key=lambda x : x[1])
                q = dict(q_sort)
    for k, v in q.items():
        qa = f'{k}\n{v}\n'
        count = 0
        full.write(f'{k}\n')
        full.write(f'{str(v)}\n')
        for m in range(v):
            count += 1
            za = f'Строка номер {count} файла номер {k}\n'
            full.write(za)
