from pickle import NONE
import re
with open("text.txt","r",encoding="UTF-8") as txt:
    content = txt.read()

def get_teachers(content):
    teachers = list()
    rule= '<td class="jsxmzc" nowrap="">【<font color="blue"><a href="javascript:void\(0\);" onclick="showTeacherInfo\(\'\w+\'\)">(\w+)</a></font>】<br>无</td>'
    teachers_data = re.findall('<td class="jsxmzc" nowrap="">.*?</td>',content)
    for teacher_data in teachers_data:
        teacher = re.match(rule,teacher_data).group(1)
        teachers.append(teacher)
    return teachers

def get_status(content):
    selected_people = re.findall('<font class="jxbrs">(\d+)</font>',content)
    all_people = re.findall('<font class="jxbrl">(\d+)</font>',content)
    selected_people = list(map(int,selected_people))
    all_people = list(map(int,all_people))
    li = []
    for i in range(len(selected_people)):
        li.append(selected_people[i]/all_people[i])
    return li

def get_xk_button_id(content):
    selected = re.findall('<button id="btn-xk-(.*?)" type="button" class="btn btn-primary btn-sm" onclick="chooseCourseZzxk\(\'(.*?)\',\'(.*?)\',\'(.*?)\',\'1\'\)">选课</button>',content)
    li = list()
    for _ in selected:
        li.append(_[0])
    return li

def get_panel(content):
    rule = '<h3 class="panel-title"><span class="kcmc" id="(.*?)">\((.*?)\)<a href="javascript:void\(0\);" onclick="showCourseInfo\(\'(.*?)\'\)">(.*?)</a> - <i id="(.*?)">(.*?)</i> 学分</span><span>教学班个数：<font class="jxbgsxx">(.*?)</font></span><span id="(.*?)">状态：<b>(.*?)</b></span></h3>'
    panel_infos = re.findall(rule,content)
    li = list()
    for panel_info in panel_infos:
        panel = {
            "课程名称":panel_info[3],
            "课程学分":panel_info[5],
            "课程数量":panel_info[6],
            "课程状态":panel_info[8]
        }
        li.append(panel)
        return li

if __name__ == "__main__":
    # print(get_xk_button_id(content)[2])
    xpath = '//*[@id="btn-xk-%s"]'
    print(len(get_teachers(content)))
    print(len(get_status(content)))
    print(len(get_xk_button_id(content)))
    print(get_panel(content))
    # print(get_panel(content))

    # rule = '<h3 class="panel-title"><span class="kcmc" id="(.*?)">\((.*?)\)<a href="javascript:void\(0\);" onclick="showCourseInfo\(\'(.*?)\'\)">(.*?)</a> - <i id="(.*?)">(.*?)</i> 学分</span><span>教学班个数：<font class="jxbgsxx">(.*?)</font></span><span id="(.*?)">状态：<b>(.*?)</b></span></h3>'
    # panel_info = re.findall(rule,content)
    # panel_info[3] # 课程名称
    # panel_info[5] # 课程学分
    # panel_info[6] # 课程数量
    # panel_info[7] # 课程状态
    
# for info in contents:
#     m = re.match('<td class="jsxmzc" nowrap="">(.*?)</td>',info)
#     m = m.group(1)
#     print(m)


# text= "<font color=\"blue\"><a href=\"javascript:void(0);\" onclick=\"showTeacherInfo('20060068')\">谢晖</a></font><br>无"
# rule= "<font color=\"blue\"><a href=\"javascript:void\(0\);\" onclick=\"showTeacherInfo\('20060068'\)\">(\w+)</a></font><br>无"

# print(re.match(rule,text).group(1))


# for info in contents:
#     print(info[117:].strip("</a></font>】<br>无</td>"))





# contents = re.findall('Info(\'*\')\">*</a>',content)
# print(content)

# for _ in contents:
#     rule = "<td class=\"jsxmzc\" nowrap=\"\">【<font color=\"blue\"><a href=\"javascript:void(0);\" onclick=\"showTeacherInfo(\'\d+\')\">(\w+)</a></font>】<br>无</td>"
#     print(_)