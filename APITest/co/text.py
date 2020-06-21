# -*- coding: utf-8 -*-
import codecs

class Text:
    def text (self):
        f = open('cookie.txt', 'r+')
        cookie = "123456"
        csrf = "HkSkbwIAW9r/1Pc9p+P+3p7P3iXeb9VTVSz0qv8c2TyDcpd9hKAVDvQ/to6wj8OXq2it8U+HQPHJ6lQd6GGy7w=="
        a = str(cookie +'\n'+ csrf)
        # print u'read%s' %a
        # a = str(self.get_today_str()) + ': ' + print_content + " status_code is right " + str(real_code) + '  ' + str(
        #     expect_code)
        # a= str("12304")
        # print a
        # f.write(a)
        # f.close()
        f = open('D:\SVN\APITest0524\co\cookie.txt', 'a+')
        index = 0
        line0 = None
        line1 = None
        for line in f:
            if index == 0:
                line0 = line
            elif index == 1:
                line1 = line
            else:
                return
            index += 1
        print (line0)
        print (line1)
        # print f.readline
        # print f[1]
        # for line in f:
        #     print line
        # print u'read%s' %line
        f.close()




if __name__ == '__main__':
    a_text = Text()
    a_text.text()
