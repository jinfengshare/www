# I want to auto write to header file
# the problem has been solved: diff from two buffer by the first address
# nice job!
# author: jinfeng

import time
import win32clipboard as w 
import win32con

def getText(): 
    w.OpenClipboard() 
    d = w.GetClipboardData(win32con.CF_TEXT) 
    w.CloseClipboard() 
    return d 

def setText(buf): 
    w.OpenClipboard() 
    w.EmptyClipboard() 
    w.SetClipboardData(win32con.CF_TEXT, buf) 
    w.CloseClipboard()

if __name__ == '__main__':
    a = 0
    outbuf = ''
    
    while True:
        outbuf = ''
        source = getText()
        src = source.split('\n')
        for line in src:
            a = 0
            if len(line)<30:
                continue
            for i in line:
                if i==' ' and line[a+1]=='0':
                    name=line[0:a-1]
                    value=line[a+1:a+11]
                    if len(name)<8:
                        tab='\t\t\t'
                    else:
                        tab='\t\t'
                    s='#define %s%s(*(volatile unsigned char *))%s\n'%(name,tab,value)
                    outbuf = outbuf + s
                    break
                a = a+1

        setText(outbuf)
        

        time.sleep(3) # after 2 seconds, the content will always the lastest!
