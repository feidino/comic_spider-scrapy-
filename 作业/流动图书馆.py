class Books:
    def __init__(self,name,author,comment,state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.status = state
    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '书名：《%s》 作者：%s 评语：%s 状态：%s ' % (self.name, self.author, self.comment, status)     
                                        
class BookManager:
    def write_book(self,book_info):
        with open (r'e:\vscode 文件\books.txt','a',encoding='utf-8') as n_books:
            lines = n_books.writelines(book_info)
        n_books.close()
        
    def read_book(self):
        with open (r'e:\vscode 文件\books.txt','r',encoding='utf-8') as n_books:
            lines = n_books.readlines()
        n_books.close()
        return lines
        
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break
 
    def show_all_book(self):
        print('书籍信息如下：')
        lines = self.read_book()
        for i in lines:
            print(i)

    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author =  input('请输入作者名称：')
        new_comment = input('请输入书籍推荐语：')
        new_status = '未借出'
        #new_book = Books(new_name, new_author, new_comment)
        book_info = '书名：《%s》 作者：%s 评语：%s 状态：%s\n' % (new_name, new_author,new_comment, new_status)
        self.write_book(book_info)
        print('书籍录入成功！\n')

    def check_book(self,name):
        book_c = self.read_book()
        for book in book_c:
            data = book.split()
            a = data[1]
            b_name = a[4:-1]
            if b_name == name:
                 return book 
        else:
            return None
        
    def book_status(self,name):
        book_c = self.read_book()
        for book in book_c:
            data = book.split()
            a = data[0]
            b_name = a[4:-1]
            if b_name == name:
                b = data[3]
                status = b[3:]
                return status
        else:
            return None
        
    def write_status(self,name,status):
        book_c = self.read_book()
        for book_info in book_c:
            data = book_info.split()
            b_name = data[0][4:-1]
            if b_name == name:
                n = book_c.index(book_info)
                l = list(book_info)
                l[-4] = status
                n_l = ''.join(l)
                book_info = n_l
                book_c[n] = book_info
                break
        with open (r'e:\vscode 文件\books.txt','w',encoding='utf-8') as books:
            lines = books.writelines(book_c)
            books.close()
           
    def lend_book(self):
        name = input('\n请输入书籍的名称：')
        res = self.book_status(name)
        if res != None:
            if res == '已借出':
                print('\n你来晚了一步，这本书已经被借走了噢\n')
            else:
                print('\n借阅成功，借了不看会变胖噢～\n')
                self.write_status(name,'已')         
        else:
            print('\n这本书暂时没有收录在系统里呢\n')
    
    def return_book(self):
        name = input('\n请输入归还书籍的名称：\n')
        res = self.book_status(name)#将返回值赋值给变量res
        if res == None:
        # 如果返回的是空值，即这本书的书名不在系统里
            print('\n没有这本书噢，你恐怕输错了书名～\n')
        else:
        # 如果返回的是实例对象
            if res == '未借出':
             # 如果实例属性state等于0，即这本书的借阅状态为'未借出'
                print('\n这本书没有被借走，在等待有缘人的垂青呢！\n')
            else:
             # 如果实例属性state等于1，即状态为'已借出'
                print('\n归还成功！\n')
                self.write_status(name,'未')
                # 归还后书籍借阅状态为0，重置为'未借出'         
            
run_book = BookManager()
run_book.menu()
