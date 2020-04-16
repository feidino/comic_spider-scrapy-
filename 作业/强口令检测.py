# 写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的
# 定义是：长度不少于8 个字符，同时包含大写和小写字符，至少有一位数字。你可
# 能需要用多个正则表达式来测试该字符串，以保证它的强度。
import re
password = input('请输入密码：')
def psw(string):
    res0 = re.compile(r'[0-9]+')
    pwdRegex0 = res0.findall(string)
    pwdstr0 = ''.join(pwdRegex0)
    if pwdstr0.isdigit():
        res1 = re.compile(r'[a-z]+')
        pwdRegex1 = res1.findall(string)
        pwdstr1 = ''.join(pwdRegex1)
        if pwdstr1.islower():
            res2 = re.compile(r'[A-Z]+')
            pwdRegex2 = res2.findall(string)
            pwdstr2 = ''.join(pwdRegex2)
            if pwdstr2.isupper():
                if len(string) >= 8:
                    res = re.compile(r'.{8,}')
                    pwdRegex = res.findall(string)
                    pwdstr = ''.join(pwdRegex)
                    if pwdstr == password:
                        print('输入的密码是强口令')    
                    else:
                        print('输入的密码不是强口令')
                else:
                    print('密码强度不够，密码必须包含8个字符以上')
            else:
                print('密码强度不够，密码必须包含大写字母')
        else:
            print('密码强度不够，密码必须包含小写字母')
    else:
        print('密码强度不够，密码必须包含1个数字')    

psw(password)

