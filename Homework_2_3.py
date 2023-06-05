import os.path


with open('1.txt', 'r', encoding='utf-8') as file_1,\
        open('2.txt', 'r', encoding='utf-8') as file_2,\
        open('3.txt', 'r', encoding='utf-8') as file_3,\
        open('final.txt', 'w', encoding='utf-8') as final_file:
    res_1 = file_1.readlines()
    res_1.insert(0, os.path.basename(r'C:\Users\Hayk\Desktop\Study\Нomework_2\1.txt'))
    res_2 = file_2.readlines()
    res_2.insert(0, os.path.basename(r'C:\Users\Hayk\Desktop\Study\Нomework_2\2.txt'))
    res_3 = file_3.readlines()
    res_3.insert(0, os.path.basename(r'C:\Users\Hayk\Desktop\Study\Нomework_2\3.txt'))
    res_4 = [res_1, res_2, res_3]
    res_4.sort(key=len)
    for res in res_4:
        final_file.write(res[0])
        final_file.write('\n')
        final_file.write(str(len(res[1:])))
        final_file.write('\n')
        final_file.writelines(res[1:])

