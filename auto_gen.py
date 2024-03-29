from os import listdir, getcwd, path
from operator import itemgetter


mypath = getcwd()

def gen_detail():
    files = listdir(mypath + "/Solution")
    all = []
    for f in files:
        id_slice = f.split(']')
        Id = id_slice[0].replace("[","")
        
        pro_slice = id_slice[1].split('.')
        Problem = pro_slice[0]
        if pro_slice[1] == 'py':
            Lang = "Python"
        elif pro_slice[1] == 'js':
            Lang = "JavaScript"
        elif pro_slice[1] == 'cpp':
            Lang = "C++"
        elif pro_slice[1] == 'sql':
            Lang = "MySQL"
        elif pro_slice[1] == 'c':
            Lang = "C"

        detail = {
            'id': int(Id),
            'problem': Problem,
            'language': Lang
        }
        all.append(detail)
    return all

def write_to_markdown():
    detail = gen_detail()
    detail_sorted = sorted(detail, key=itemgetter('id')) 

    markdown = open("README.md", "w")

    title = "# MyLeetCode\n" + "LeetCode Practice</br>\n" + "Program Language: Python C++ JavaScript\n"
    total_solved = "Total Sovled: " + str(len(detail_sorted))
    table_header = "\n\n\n No.   | Question  | Solution   \n" + "-------| ----------| --------- \n"
    data = ''
    for d in detail_sorted:
        number = str(d['id']) + ((7 - len(str(d['id']))) * ' ') + "|"
        question = '[' + d['problem'] + '](https://leetcode.com/problems/' + d['problem'].lower().replace(' ','-') + '/)|'
        lang_and_link = '[' + d['language'] + ']' + '(https://github.com/dsmsfans/My_LeetCode/tree/master/Solution)'
        data = data + number + question + lang_and_link + '\n'
    
    output = title + total_solved + table_header + data
    markdown.write(output)
    markdown.close

if __name__ == "__main__":
    write_to_markdown()