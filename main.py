import sys
import getpass
from Functions import Target_Word, Word_List 
def _find_getch():
    try:
        import termios
    except ImportError:
        import msvcrt
        return msvcrt.getch
 
    import tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
 
    return _getch
 
def cmd():
    sentence = ''
    sugg = ''
    ch = 'a'
    getch = _find_getch()
    count = 0
    length = 0
    while ch not in '\r\n':
        
        ch2 = getch()
        ch1 = ch2.decode('utf-8')
        count = count+1
        ch = str(ch2)
        if count>=5:
            count=0
        if ch==str(b'\r'):
            for i in range(length):
                sys.stdout.write('\b \b')
                sys.stdout.flush()
                sentence = sentence[:(len(sentence)-1)]
            sugg, length = suggestions(count)
            sys.stdout.write(str(sugg))
            sys.stdout.flush()
            sentence+=sugg
            continue
        if ch==str(b' '):
            count = 0
            sugg, length = suggestions(0)
            sys.stdout.write(str(sugg))
            length = 0
            sys.stdout.flush()
            sentence+=" "
            continue
        if ch==str(b'.'):
            break
        sys.stdout.write(str(ch1))
        sys.stdout.flush()
        sentence+=str(ch1)
    return sentence
def suggestions(count):
    words = ['','work','job','career','profession']
    return " "+words[count],len(words[count])+1
sequence = cmd()
word_list = Word_List(sequence)
