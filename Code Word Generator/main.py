
import pandas as pd

data=pd.read_csv("alpha.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)

def gen_phonetic():
    word=input("Enter a word:").upper()
    try:
        output_list=[phonetic_dict[letter] for letter in word]
        gen_phonetic()
    except KeyError:
        print("Invalid input! Please enter a valid word.")
    else:   
        print(output_list)
        
gen_phonetic()