'''
   CS5001
   Lab 6
   Spring 2025
   Sia Xuan, Dayu Wang
'''


def create_emoji_dictionary():
    '''
    '''
    emoji_dictionary = {
                        "happy": '\U0001F60A',
                        "sad": 	'\U0001F622',
                        "Worried": '\U0001F61F',
                        "Loudly Crying": '\U0001F62D',
                        "love": '\U00002764', 
                        "fall in love" : '\U0001F498', 
                        "dog": '\U0001F436', 
                        "cat": '\U0001F431', 
                        "angry": '\U0001F621'    
                       }
    return emoji_dictionary


def translate_sentence(sentence: str, emoji_dictionary: dict[str, str]):
    '''
    '''
    sentence_lower = sentence.lower()
    positions = []
    for key in emoji_dictionary:
        index = sentence_lower.lower().find(key)
        while index != -1:  
            positions.append((index, key))
            index = sentence_lower.find(key, index + len(key)+1)        
    for position, key in sorted(positions, reverse=True):
        sentence = sentence[:position] + emoji_dictionary[key] + sentence[position + len(key):]
        
    return sentence


def main():
    emoji_dictionary = create_emoji_dictionary()
    sentence = input("please enter your sentence")
    print(translate_sentence(sentence, emoji_dictionary))

main()
