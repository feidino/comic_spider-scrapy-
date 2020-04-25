# 1．创建Regex 对象的函数是什么？
re.compile()
# 2．在创建Regex 对象时，为什么常用原始字符串？
使用原始字符串是为了让反斜杠不必转义
# 3．search()方法返回什么？
match的一个对象
# 4．通过Match 对象，如何得到匹配该模式的实际字符串？
使用match的group()方法匹配
# 5．用r'(\d\d\d)-(\d\d\d-\d\d\d\d)'创建的正则表达式中，分组0 表示什么？分组1呢？分组2 呢？
分组0 匹配整个正则表达式，分组1表示(\d\d\d)，分组2表示(\d\d\d-\d\d\d\d)
分组0 是整个匹配，分组1 包含第一组括号，分组2 包含第二组括号
# 6．括号和句点在正则表达式语法中有特殊的含义。如何指定正则表达式匹配真正的括号和句点字符？
句号和括号可以用反斜杠转义：\.、\（和\）。
# 7．findall()方法返回一个字符串的列表，或字符串元组的列表。是什么决定它提供哪种返回？
正则表达式的分组
# 8．在正则表达式中，|字符表示什么意思？
|字符表示匹配两个组中的“任何一个”。
# 9．在正则表达式中，?字符有哪两种含义？
第一种：正则表达式分组进行0次或者1次的匹配，第二种：非贪心匹配，当分组出现匹配次数范围时，表示首先返回以最小匹配次数字符串
# 10．在正则表达式中，+和*字符之间的区别是什么？
+是1次至无数次匹配，*是0次至无数次匹配
# 11．在正则表达式中，{3}和{3,5}之间的区别是什么？
{3}是进行3次匹配，{3,5}是进行至少3次，最多5次的匹配
# 12．在正则表达式中，\d、\w 和\s 缩写字符类是什么意思？
\d表示表示匹配任意一个数字，\w匹配字母或数字或下划线，\s匹配任意的空白符
# 13．在正则表达式中，\D、\W 和\S 缩写字符类是什么意思？
\D表示表示匹配非数字字符，\W匹配非字母或数字或下划线字符，\S匹配非空白符字符
# 14．如何让正则表达式不区分大小写？
在re.compile()函数第二个参数输入re.IGNORECASE或者re.I
# 15．字符.通常匹配什么？如果re.DOTALL 作为第二个参数传递给re.compile()，它会匹配什么？
.它匹配除了换行之外的所有字符，作为第二个参数传递给re.compile()，让句点字符匹配所有字符，包括换行字符。
# 16．.*和.*?之间的区别是什么？
.*执行贪心匹配，.*?执行非贪心匹配
# 17．匹配所有数字和小写字母的字符分类语法是什么？
[0-9a-z]
# 18．如果numRegex = re.compile(r'\d+')，那么numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')返回什么？
X drummers, X pipers, five rings, X hens
# 19．将re.VERBOSE 作为第二个参数传递给re.compile()，让你能做什么？
re.VERBOSE 参数允许为传入 re.compile() 的字符串添加空格和注释
# 20．如何写一个正则表达式，匹配每3 位就有一个逗号的数字？它必须匹配以下数字：
#  '42'
#  '1,234'
#  '6,368,745'
# 但不会匹配：
#  '12,34,567' （逗号之间只有两位数字）
#  '1234' （缺少逗号）
re.compile（r'^\d{1,3}(,{3})*$'）将创建这个正则表达式，但其他正则表达
式字符串可以生成类似的正则表达式。
# 21．如何写一个正则表达式，匹配姓Nakamoto 的完整姓名？你可以假定名字
# 总是出现在姓前面，是一个大写字母开头的单词。该正则表达式必须匹配：
#  'Satoshi Nakamoto'
#  'Alice Nakamoto'
#  'RoboCop Nakamoto'
# 但不匹配：
#  'satoshi Nakamoto'（名字没有大写首字母）
#  'Mr. Nakamoto'（前面的单词包含非字母字符）
#  'Nakamoto' （没有名字）
#  'Satoshi nakamoto'（姓没有首字母大写）
re.compile(r'[A-Z][a-z]*\sNakamoto')
# 22．如何编写一个正则表达式匹配一个句子，它的第一个词是Alice、Bob 或
# Python 编程快速上手——让繁琐工作自动化
# Carol，第二个词是eats、pets 或throws，第三个词是apples、cats 或baseballs。该句
# 子以句点结束。这个正则表达式应该不区分大小写。它必须匹配：
#  'Alice eats apples.'
#  'Bob pets cats.'
#  'Carol throws baseballs.'
#  'Alice throws Apples.'
#  'BOB EATS CATS.'
# 但不匹配：
#  'RoboCop eats apples.'
#  'ALICE THROWS FOOTBALLS.'
#  'Carol eats 7 cats.'
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\ s(apples|cats|baseballs)\.',re.IGNORECASE)