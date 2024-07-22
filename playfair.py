import string
def create_matrix(keyword):
    letter=list(string.ascii_lowercase)
    letter_keyword=[(i,"") for i in keyword]
    letter_keyword=list(dict(letter_keyword).keys())
    for i in letter_keyword:
        letter.remove(i)
        if i=="i":
            letter.remove('j')
    for i in letter:
        if i=="i":
            letter.remove('j')
    raw_matrix=[]
    for i in letter_keyword:
        if i == "i":
            raw_matrix.append(["i","j"])
        else:
            raw_matrix.append(i)
    for i in letter:
        if i == "i":
            raw_matrix.append(["i","j"])
        else:
            raw_matrix.append(i)
    final_list=[]
    length=0
    for i in range(0, len(raw_matrix), 5):
        sublist = raw_matrix[i:i+5]
        final_list.append(sublist)
    print("final matrix",final_list)
def after_spilt(text):
    text=list(text)
    bogus="x"
    final_text=[]
    for i in range(len(text)):
        if text[i+1]==text[i]:
            sublist=[text[i],'x']
            final_text.append(sublist)
        elif i==len(text)-1:
            sublist=[text[i],'x']
            final_text.append(sublist)
        else:
            sublist=[text[i],text[i+1]]
            final_text.append(sublist)
            
    print(final_text)
def encryption(keyword):
    pass
def main():
    # keyword=input("Enter the keyword:")
    # create_matrix(keyword)
    text=input("Enter the text:")
    after_spilt(text)
if __name__=="__main__":
    main()