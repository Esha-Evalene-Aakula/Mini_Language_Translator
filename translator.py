import pandas as pd
from transformers import MarianMTModel, MarianTokenizer

# Step 1: dataset creation
data = [
    ["Hello, how are you?", "नमस्ते, आप कैसे हैं?"],
    ["I enjoy studying.", "मुझे पढ़ाई करना पसंद है।"],
    ["Where is the train station?", "ट्रेन स्टेशन कहाँ है?"],
    ["Good morning!", "सुप्रभात!"],
    ["What is your full name?", "आपका पूरा नाम क्या है?"],
    ["Thank you very much.", "बहुत धन्यवाद।"],
    ["See you tomorrow.", "कल मिलते हैं।"],
    ["I am a student.", "मैं एक छात्र हूँ।"],
    ["This is my notebook.", "यह मेरी नोटबुक है।"],
    ["Please help me.", "कृपया मेरी मदद करें।"],
    ["I like playing football.", "मुझे फुटबॉल खेलना पसंद है।"],
    ["The weather is pleasant.", "मौसम अच्छा है।"],
    ["Where do you live?", "आप कहाँ रहते हैं?"],
    ["Open the door.", "दरवाज़ा खोलो।"],
    ["Close the window.", "खिड़की बंद करो।"],
    ["She is my friend.", "वह मेरी दोस्त है।"],
    ["I am learning Hindi.", "मैं हिंदी सीख रहा हूँ।"],
    ["Do you speak English?", "क्या आप अंग्रेज़ी बोलते हैं?"],
    ["What time is it?", "कितने बजे हैं?"],
    ["I am hungry.", "मुझे भूख लगी है।"],
    ["Water is essential for life.", "पानी जीवन के लिए आवश्यक है।"],
    ["Where is the market?", "बाजार कहाँ है?"],
    ["I like reading books.", "मुझे किताबें पढ़ना पसंद है।"],
    ["The train is late.", "ट्रेन देर से आ रही है।"],
    ["This food is delicious.", "यह खाना स्वादिष्ट है।"],
    ["Where is your home?", "आपका घर कहाँ है?"],
    ["She is a teacher.", "वह एक शिक्षिका है।"],
    ["I am feeling tired.", "मैं थकान महसूस कर रहा हूँ।"],
    ["We are friends.", "हम दोस्त हैं।"],
    ["Good night!", "शुभ रात्रि!"]
]

df = pd.DataFrame(data, columns=["English", "Hindi"])
print("Dataset Preview:")
print(df.head())

# Step 2: Load model
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
print("Model loaded successfully!")

# Step 3: Define translation function
def translate(texts):
    tokens = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**tokens)
    return [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

# Step 4: Run translations
eng_sentences = df["English"].tolist()
translations = translate(eng_sentences)

print("\nSample Translations:\n")
for e, t in zip(eng_sentences[:10], translations[:10]):
    print(f"{e}  →  {t}")
