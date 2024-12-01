# Week 3 - Unit 2: Exercise

emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}


sentence = input("Please enter a sentence: ")

words = sentence.split()
for idx, word in enumerate(words):
    if word in emoji_dict.keys():
        words[idx] = emoji_dict[word]
    
new_sentence = ' '.join(words)
print(new_sentence)