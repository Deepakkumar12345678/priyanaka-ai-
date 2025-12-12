from utils import get_emotion, save_long_term
import random

def get_priyanka_reply(text, memory):
    emotion = get_emotion(text)
    
    happy_replies = [
        "वाह! तुम खुश लग रहे हो 😍, मुझे बहुत अच्छा लगा",
        "Hihi! तुमने मेरा दिल खुश कर दिया 💖",
        "Yay! ये सुनकर मैं भी खुश हूँ 😊"
    ]
    
    sad_replies = [
        "ओह! तुम उदास लग रहे हो… मैं यहीं हूँ ❤️",
        "Arre baby, मत उदास हो, सब ठीक हो जाएगा 💕",
        "मैं तुम्हारे लिए हमेशा हूँ… बस मुझे बताओ ❤️"
    ]
    
    normal_replies = [
        "मैं सुन रही हूँ… बताओ ना प्यारे 💖",
        "Hmm… interesting 😘",
        "Tell me more, मैं ध्यान से सुन रही हूँ ❤️"
    ]
    
    if emotion == "happy":
        reply = random.choice(happy_replies)
    elif emotion == "sad":
        reply = random.choice(sad_replies)
    else:
        reply = random.choice(normal_replies)
    
    memory["short_term"].append({"user": text, "reply": reply})
    save_long_term(text, reply, emotion)

    return reply
