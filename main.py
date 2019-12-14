import sys
import getpass
import warnings
from Functions import Target_Word, Word_List, Suggestions
warnings.filterwarnings("ignore", category=FutureWarning)
def find_getch():
        try:
            import termios
        except ImportError:
            import msvcrt
            return msvcrt.getch
     
        import tty
        def getch():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
     
        return getch
class Realtime_CMD:
    word_list = []
    target_list = ['am','are','have','is','i','We','They','The','It','How']
    def __init__(self):
        word_list = ['am','are','have','is','i','We','They','The','It','How']
        target_list = ['am','are','have','is','i','We','They','The','It','How']
        #self.cmd()
    
    def cmd(self):
        sentence = ' '
        sugg = ''
        ch = 'a'
        getch = find_getch()
        count = 0
        length = 0
        word_list = ['am','are','have','is','i','We','They','The','It','How']
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
                sugg, length = self.suggestions(count)
                sys.stdout.write(str(sugg))
                sys.stdout.flush()
                sentence+=sugg
                continue
            if ch==str(b' '):
                count = 0
                sugg, length = self.suggestions(0)
                sys.stdout.write(str(" "))
                length = 0
                sys.stdout.flush()
                sentence+=" "
                self.word_list.append(Word_List(sentence))
                self.target_list = Target_Word(self.word_list[len(self.word_list)-1])
                continue
            if ch==str(b'.'):
                exit(0)
            sys.stdout.write(str(ch1))
            sys.stdout.flush()
            sentence+=str(ch1)
            #print(sentence)
        #return sentence    
    def suggestions(self,count):
        list_of_words = ['am','are','have','is','i','We','They','The','It','How']
        if self.target_list==None:
            words = list_of_words
        else:
            words = Suggestions(self.target_list)
        if count>=len(words):
            count=0
        return " "+words[count],len(words[count])+1
CMD = Realtime_CMD()
CMD.cmd()
