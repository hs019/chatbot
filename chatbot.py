import tkinter as tk
import threading
import time
import random


# ── BOT RESPONSES ────────────────────────────────────────
def get_bot_reply(text):
    text = text.lower()

    # Specific phrases first
    if "what happened at school" in text or "wanna know what happened" in text:
        return random.choice([
            "Yeah, go ahead. What happened?",
            "I'm listening. Tell me.",
            "What happened at school?"
        ])

    # General categories
    elif any(w in text for w in ["hi", "hello", "hey"]):
        return random.choice([
            "Hey.",
            "Hi there.",
            "Hello."
        ])

    elif any(w in text for w in ["how are you"]):
        return random.choice([
            "I'm doing fine. How about you?",
            "Pretty good. You?",
            "All good here."
        ])

    elif any(w in text for w in ["sad", "upset", "cry", "bad"]):
        return random.choice([
            "That sounds rough. Want to talk about it?",
            "I'm here. What happened?",
            "Yeah, that can be tough."
        ])

    elif any(w in text for w in ["happy", "great", "good", "amazing"]):
        return random.choice([
            "Nice, that's good to hear.",
            "Glad things are going well.",
            "Sounds like a good day."
        ])

    elif any(w in text for w in ["school", "exam", "study", "homework"]):
        return random.choice([
            "How was it?",
            "Anything interesting happen?",
            "School can be a lot sometimes."
        ])

    elif any(w in text for w in ["bored"]):
        return random.choice([
            "Want to talk about something?",
            "We can fix that. What's on your mind?",
            "Yeah, boredom happens."
        ])

    elif any(w in text for w in ["game", "gaming"]):
        return random.choice([
            "What do you play?",
            "Gaming's a good way to pass time.",
            "Which game are you into?"
        ])

    elif any(w in text for w in ["food", "eat", "hungry"]):
        return random.choice([
            "What are you planning to eat?",
            "Food always helps.",
            "Got anything good?"
        ])

    elif any(w in text for w in ["thanks", "thank you"]):
        return random.choice([
            "No problem.",
            "Anytime.",
            "You're welcome."
        ])

    elif "name" in text:
        return "I'm Luna, your chatbot."

    elif "age" in text:
        return "I don't really have an age."

    elif "bye" in text:
        return random.choice([
            "Alright, take care.",
            "See you later.",
            "Goodbye."
        ])

    else:
        return random.choice([
            "Can you explain that a bit more?",
            "I'm not sure I understood.",
            "Tell me more.",
            "Interesting. Go on."
        ])


# ── SEND MESSAGE ─────────────────────────────────────────
def send_message(event=None):
    user_text = user_input.get().strip()
    if not user_text:
        return

    add_message(user_text, "user")
    user_input.delete(0, tk.END)
    send_btn.config(state=tk.DISABLED)

    typing_label.set("Typing...")

    def fetch_reply():
        time.sleep(0.5)
        reply = get_bot_reply(user_text)

        typing_label.set("")
        add_message(reply, "bot")

        send_btn.config(state=tk.NORMAL)
        user_input.focus()

    threading.Thread(target=fetch_reply, daemon=True).start()


def add_message(text, sender):
    bubble = tk.Label(
        chat_frame,
        text=text,
        wraplength=260,
        justify="left",
        padx=10,
        pady=8,
        font=("Segoe UI", 10)
    )

    if sender == "user":
        bubble.config(bg="#2563eb", fg="white")  # blue
        bubble.pack(anchor="e", pady=4, padx=8)
    else:
        bubble.config(bg="#e5e7eb", fg="#111827")  # light gray
        bubble.pack(anchor="w", pady=4, padx=8)

    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1.0)


# ── WINDOW ───────────────────────────────────────────────
root = tk.Tk()
root.title("Luna")
root.geometry("420x650")
root.configure(bg="#f3f4f6")


# ── HEADER ───────────────────────────────────────────────
header = tk.Frame(root, bg="#111827", pady=10)
header.pack(fill=tk.X)

tk.Label(header, text="Luna",
         font=("Segoe UI", 16, "bold"),
         bg="#111827", fg="white").pack()

tk.Label(header, text="Chat assistant",
         font=("Segoe UI", 9),
         bg="#111827", fg="#9ca3af").pack()


# ── CHAT AREA ────────────────────────────────────────────
chat_canvas = tk.Canvas(root, bg="#f3f4f6", highlightthickness=0)
chat_canvas.pack(fill=tk.BOTH, expand=True)

chat_frame = tk.Frame(chat_canvas, bg="#f3f4f6")
chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")

def on_configure(event):
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

chat_frame.bind("<Configure>", on_configure)


# ── TYPING LABEL ─────────────────────────────────────────
typing_label = tk.StringVar()
tk.Label(root, textvariable=typing_label,
         bg="#f3f4f6", fg="#6b7280",
         font=("Segoe UI", 9, "italic")).pack(anchor="w", padx=10)


# ── INPUT AREA ───────────────────────────────────────────
input_frame = tk.Frame(root, bg="#ffffff", pady=8)
input_frame.pack(fill=tk.X)

user_input = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    bg="#ffffff",
    fg="#111827",
    insertbackground="#111827"
)
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 5), ipady=10)
user_input.bind("<Return>", send_message)

send_btn = tk.Button(
    input_frame,
    text="Send",
    font=("Segoe UI", 10, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    relief=tk.FLAT,
    command=send_message
)
send_btn.pack(side=tk.RIGHT, padx=(5, 10), ipady=10)


# ── START MESSAGES ───────────────────────────────────────
add_message("Hello. I'm Luna.", "bot")
add_message("You can start typing whenever you're ready.", "bot")

user_input.focus()
root.mainloop()