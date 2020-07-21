import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26
        
    Returns: a dictionary mapping a letter (string) to another letter (string). 
    '''
    lowerLetters = list(string.ascii_lowercase)
    upperLetters = list(string.ascii_uppercase)
    
    lowerShift = list(string.ascii_lowercase)
    upperShift = list(string.ascii_uppercase)
    
    shiftedLower = lowerShift[shift:] + lowerShift[:shift]
    shiftedUpper = upperShift[shift:] + upperShift[:shift]
        
    allLettersOrig = lowerLetters + upperLetters
    allLettersShift = shiftedLower + shiftedUpper
    
    shiftDict = {k:v for k,v in zip(allLettersOrig,allLettersShift)}
    
    print(shiftDict)
build_shift_dict(2)

