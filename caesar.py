import sys
import language_check

class CaesarCipher:
    def __init__(self, mode, text, shiftOfText=0):
        self.mode = mode
        self.text = text
        self.text = text.upper()
        self.shift = shiftOfText
        self.spellChecker = SpellCheckerObject()

        self.alphabets = "abcdefghijklmnopqrstuvwxyz0123456789!@$#&*? "
        self.alphabets = self.alphabets.upper()
        self.letter_to_index = dict(zip(self.alphabets, range(len(self.alphabets))))
        self.index_to_letter = dict(zip(range(len(self.alphabets)), self.alphabets))
    
        if (mode == "ENCRYPT"): self.encryptModule(self.text, self.shift)
        if (mode == "DECRYPT"): self.decryptModule(self.text, self.shift)
    
    # Functions
    def encryptModule(self ,text, shift=3):
        outputIndex = []
        inputText = text
        cipher = ''
        for txt in inputText:
            index = (self.letter_to_index[txt] + shift)  
            index = index % len(self.alphabets)
            cipherLetter = self.index_to_letter[index]
            cipher += cipherLetter
        print("Encrypted Text: \"{}\"".format(cipher))

    def decryptModule(self, text, shift=3):
        # Take the text and convert this to a int value
        inputText = text
        plain_text = ''
        plain_texts = []
        if (shift > 0):
            for txt in inputText:
                index = (self.letter_to_index[txt] - shift)  
                index = index % len(self.alphabets)
                plainLetter = self.index_to_letter[index]
                plain_text += plainLetter
            print(plain_text)
        elif (shift == 0):
            id_ = 0
            for shift_ in range(1, len(self.alphabets) * 2):
                for txt in inputText:
                    index = (self.letter_to_index[txt] - shift_)  
                    index = index % len(self.alphabets)
                    plainLetter = self.index_to_letter[index]
                    plain_text += plainLetter
                
                plain_texts.clear()
                plain_texts.append(plain_text)
                plain_text = ''
                #matches = self.tool.check(text)
            
                for txt in plain_texts:
                    id_ += 1
                    print('[+] Attempt -- Shift: {} Text: {}'.format(id_, txt))
            print("[+] All Possible Combination Tried!")
            #print("[+] Most Probability: \"{}\"".format(english_checker.returnTruth()))

        else:
            print("Please Provide The Shift Value, If None Is Given It Will Try Bruteforce")
            
# TODO: Create A Simple Spell Checker! (Unfinished)
class SpellCheckerObject:
    def __init__(self):
        self.tool = language_check.LanguageTool('en-US')
    def checkSentence(self, sentence):
        sentence_ = "u{}".format(sentence)
        matches = self.tool.check(sentence_)
        if (len(matches) == 0) : print("MEH MAYBE WORKING!")


def main():
    runTimeArguments = sys.argv
    arguments_passed = len(runTimeArguments) 
    try:
        if arguments_passed > 1:

            mode = sys.argv[1]
            text = sys.argv[2]
            shiftOfText = int(sys.argv[3])
            CaesarCipher(mode, text, shiftOfText)
    except IndexError as e:
        mode = sys.argv[1]
        text = sys.argv[2]
        CaesarCipher(mode, text, 0)
    pass

if __name__ == "__main__":
    main()

#CaesarCipher("ENCRYPT", "jarif", 3)
