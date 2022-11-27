import string
#from textblob import TextBlob, Word

def list_to_str(s):
    empty_s = " "
    return(empty_s.join(s))

def str_to_list(s):
    l = list(s.split(" "))
    return l

def filter_just_word(input):
    my_list = input
    my_str = list_to_str(my_list)

    my_str = my_str.translate(str.maketrans('', '', string.punctuation))
    my_list = str_to_list(my_str)

    return my_list

def filter_length(input, length):
    return input[0:length]

def filter_stopwords(input):
    stopwords = ['a', 'ante', 'bajo', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 
                'mediante', 'para', 'por', 'según', 'sin', 'sobre', 'tras', 'aunque', 'y', 'e', 'ni', 'o', 'u', 
                'pero', 'sino', 'mas', 'porque', 'que']
    my_list = input
    my_list = [word for word in my_list if word not in stopwords]

    return my_list

def filter_lemmatize(input):
    my_list = input
    #my_list = [Word(word).lemmatize() for word in my_list]

    return my_list