def decode_from_morse(code):
    dicti = {}
    morse = '''A,.-
    B,-...
    W,.--
    G,--.
    D,-..
    E,.
    V,...-
    Z,--..
    I,..
    J,.---
    K,-.-
    L,.-..
    M,--
    N,-.
    O,---
    P,.--.
    R,.-.
    S,...
    T,-
    U,..-
    F,..-.
    H,....
    C,-.-.
    ö,---.
    ch,----
    Q,--.-
    X,-..-
    Y,-.--
    é,..-..
    ü,..--
    ä,.-.-
    1,.----
    2,..---
    3,...--
    4,....-
    5,.....
    6,-....
    7,--...
    8,---..
    9,----.
    0,-----
    .,......
    comma,.-.-.-
    /,-..-.
    ?,..--..
    !,--..--
    space,-...-
    error,........
    @,.--.-.'''
    morse = morse.split('\n')
    morse = [i.strip() for i in morse]
    for i in range(len(morse)):
        dicti[morse[i][morse[i].find(',') + 1:]] = morse[i][0]
    message = code.split()
    message = [dicti[i] for i in message]
    return message