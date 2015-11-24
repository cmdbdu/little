#coding:utf8
import imaplib
import email

class ReadMail:
    ''' simple mail conn
    '''
    def __init__(self,server,port,username,passwd):
        self.server = server
        self.port = port
        self.username = username
        self.passwd = passwd

    def login(self):
        conn = imaplib.IMAP4(self.server,self.port)
        try:
            conn.login(self.username,self.passwd)
            self.conn = conn 
            return self.conn
        except Exception, e:
            print 'Error :%s' % e

    def logout(self):
        try:
            self.conn.logout()
        except Exception,e:
            print 'Error: object has no attr logout'

def test():
    server = 'imap.sina.com'
    port = 143
    username = 'cmd_du@sina.com'
    passwd = 'chaikenadashagua'

    a = ReadMail(server,port,username,passwd)
    a.login()
    a.logout()

if __name__ == "__main__":
    test()
