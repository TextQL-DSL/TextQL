import string

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