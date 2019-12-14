import sys
import getpass

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
        count = count+1
        ch2 = getch()#.decode()
        ch = str(ch2)
        if count>=5:
            count=0
        if ch==str(b'\r'):
            for i in range(length):
                sys.stdout.write('\b \b')
                sys.stdout.flush()
            
            sugg, length = suggestions(count)
            sys.stdout.write(str(sugg))
            sys.stdout.flush()
            continue
        if ch==str(b' '):
            count = 0
            sugg, length = suggestions(0)
            sys.stdout.write(str(sugg))
            sys.stdout.flush()
            continue
        sentence += sugg
        if ch==str(b'.'):
            break
        ch1 = ch2.decode('utf-8')
        sentence += ch1
        sys.stdout.write(str(ch1))
        sys.stdout.flush()
    return sentence
def suggestions(count):
    words = [' ',' work ',' job ',' career ',' profession ']
    return words[count],len(words[count])
cmd()
