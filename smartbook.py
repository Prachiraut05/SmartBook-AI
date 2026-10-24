
import tkinter as tk
from tkinter import scrolledtext

# =====================================================
# SMARTBOOK AI - BOOK RECOMMENDATION CHATBOT
# =====================================================

BOOKS = [
    {
        "title": "Mrityunjay",
        "author": "Shivaji Sawant",
        "genre": "Historical",
        "language": "Marathi",
        "length": "Long",
        "level": "Intermediate",
        "description": "A powerful historical novel based on the life of Karna from the Mahabharata."
    },
    {
        "title": "Shamchi Aai",
        "author": "Sane Guruji",
        "genre": "Inspirational",
        "language": "Marathi",
        "length": "Medium",
        "level": "Beginner",
        "description": "A heartwarming story about a mother's love, values, and life lessons."
    },
    {
        "title": "Kosala",
        "author": "Bhalchandra Nemade",
        "genre": "Fiction",
        "language": "Marathi",
        "length": "Long",
        "level": "Advanced",
        "description": "A novel exploring life through the experiences of Pandurang Sangvikar."
    },
    {
        "title": "Vyakti Ani Valli",
        "author": "P. L. Deshpande",
        "genre": "Comedy",
        "language": "Marathi",
        "length": "Medium",
        "level": "Beginner",
        "description": "A humorous and engaging portrayal of memorable characters."
    },
    {
        "title": "Shriman Yogi",
        "author": "Ranjit Desai",
        "genre": "Historical",
        "language": "Marathi",
        "length": "Long",
        "level": "Intermediate",
        "description": "A historical novel based on Chhatrapati Shivaji Maharaj."
    },
    {
        "title": "Natsamrat",
        "author": "V. V. Shirwadkar (Kusumagraj)",
        "genre": "Drama",
        "language": "Marathi",
        "length": "Medium",
        "level": "Intermediate",
        "description": "A dramatic portrayal of the struggles of a celebrated stage actor."
    },
    {
        "title": "Yayati",
        "author": "V. S. Khandekar",
        "genre": "Historical",
        "language": "Marathi",
        "length": "Long",
        "level": "Advanced",
        "description": "A mythological novel exploring desire, sacrifice, and responsibility."
    },
    {
        "title": "Ravan",
        "author": "Sharad Tandale",
        "genre": "Historical",
        "language": "Marathi",
        "length": "Medium",
        "level": "Intermediate",
        "description": "A book that examines the character of Ravan from a different perspective."
    },
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "genre": "Fantasy",
        "language": "English",
        "length": "Long",
        "level": "Beginner",
        "description": "A young wizard discovers a magical world."
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Inspirational",
        "language": "English",
        "length": "Medium",
        "level": "Beginner",
        "description": "A young shepherd follows his dreams."
    },
    {
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "genre": "Fantasy",
        "language": "English",
        "length": "Long",
        "level": "Intermediate",
        "description": "A hobbit begins an adventurous journey."
    }
]

# =====================================================
# PREFERENCE OPTIONS
# =====================================================

GENRES = [
    "Fantasy", "Fiction", "Mystery", "Romance",
    "Historical", "Comedy", "Drama", "Inspirational", "Any"
]

LANGUAGES = ["English", "Marathi", "Hindi", "Any"]
LENGTHS = ["Short", "Medium", "Long", "Any"]
LEVELS = ["Beginner", "Intermediate", "Advanced", "Any"]

# =====================================================
# DARK THEME COLOURS
# =====================================================

BG = "#121826"
PANEL = "#1b2435"
CHAT_BG = "#0d1320"
TEXT = "#e5e7eb"
MUTED = "#aab4c5"
ACCENT = "#38bdf8"
BUTTON_BG = "#26364f"
BUTTON_ACTIVE = "#334b6b"
USER_COLOR = "#86efac"
BOT_COLOR = "#7dd3fc"


# =====================================================
# SMARTBOOK CHATBOT CLASS
# =====================================================

class SmartBook:

    def __init__(self, root):
        self.root = root
        self.root.title("SmartBook AI - Book Recommendation")
        self.root.geometry("850x700")
        self.root.minsize(650, 560)
        self.root.configure(bg=BG)

        self.name = ""
        self.step = "name"
        self.preferences = {}
        self.results = []
        self.seen_titles = set()

        # ---------------- HEADER ----------------

        header = tk.Frame(root, bg="#172554", pady=16)
        header.pack(fill=tk.X)

        tk.Label(
            header,
            text="📚 SmartBook AI",
            font=("Arial", 23, "bold"),
            bg="#172554",
            fg="#f8fafc"
        ).pack()

        tk.Label(
            header,
            text="Discover your next favourite book",
            font=("Arial", 11),
            bg="#172554",
            fg="#bfdbfe"
        ).pack(pady=(4, 0))

        # ---------------- CHAT DISPLAY ----------------

        self.chat = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg=CHAT_BG,
            fg=TEXT,
            insertbackground=TEXT,
            selectbackground="#334155",
            height=20,
            padx=14,
            pady=12,
            relief=tk.FLAT,
            state=tk.DISABLED
        )

        self.chat.pack(
            fill=tk.BOTH,
            expand=True,
            padx=14,
            pady=(14, 8)
        )

        self.chat.tag_config(
            "bot",
            foreground=BOT_COLOR,
            font=("Arial", 11, "bold")
        )

        self.chat.tag_config(
            "user",
            foreground=USER_COLOR,
            font=("Arial", 11, "bold")
        )

        self.chat.tag_config("body", foreground=TEXT)

        # ---------------- DYNAMIC BUTTONS ----------------

        self.options = tk.Frame(root, bg=BG)
        self.options.pack(fill=tk.X, padx=14, pady=4)

        # ---------------- INPUT AREA ----------------

        input_frame = tk.Frame(
            root,
            bg=PANEL,
            padx=10,
            pady=10
        )

        input_frame.pack(
            fill=tk.X,
            padx=14,
            pady=(4, 14)
        )

        self.entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="#263247",
            fg=TEXT,
            insertbackground=TEXT,
            relief=tk.FLAT,
            bd=0
        )

        self.entry.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            ipady=10,
            padx=(0, 10)
        )

        self.entry.bind("<Return>", self.submit)

        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.submit,
            bg="#0284c7",
            fg="white",
            activebackground="#0369a1",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )

        self.send_button.pack(side=tk.LEFT, padx=(0, 8))

        tk.Button(
            input_frame,
            text="Restart",
            command=self.restart,
            bg="#475569",
            fg="white",
            activebackground="#64748b",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=8,
            cursor="hand2"
        ).pack(side=tk.LEFT)

        # ---------------- START CHAT ----------------

        self.add_message(
            "Hello! Welcome to SmartBook AI.\n"
            "I will recommend books based on your preferences."
        )

        self.add_message("First, what is your name?")

        self.entry.focus_set()

    # =================================================
    # DISPLAY CHAT MESSAGES
    # =================================================

    def add_message(self, message, sender="SmartBook"):
        self.chat.configure(state=tk.NORMAL)

        if sender == "You":
            self.chat.insert(tk.END, "You: ", "user")
        else:
            self.chat.insert(tk.END, "SmartBook: ", "bot")

        self.chat.insert(tk.END, message + "\n\n", "body")

        self.chat.configure(state=tk.DISABLED)
        self.chat.see(tk.END)

    # =================================================
    # CLEAR OLD BUTTONS
    # =================================================

    def clear_options(self):
        for widget in self.options.winfo_children():
            widget.destroy()

    # =================================================
    # SHOW OPTION BUTTONS
    # =================================================

    def show_buttons(self, choices, callback):
        self.clear_options()

        for index, choice in enumerate(choices):
            button = tk.Button(
                self.options,
                text=choice,
                command=lambda value=choice: callback(value),
                bg=BUTTON_BG,
                fg=TEXT,
                activebackground=BUTTON_ACTIVE,
                activeforeground="white",
                font=("Arial", 10, "bold"),
                relief=tk.FLAT,
                padx=12,
                pady=7,
                cursor="hand2"
            )

            button.grid(
                row=index // 4,
                column=index % 4,
                padx=4,
                pady=4,
                sticky="ew"
            )

        for col in range(4):
            self.options.grid_columnconfigure(col, weight=1)

    # =================================================
    # HANDLE TYPED INPUT
    # =================================================

    def submit(self, event=None):
        value = self.entry.get().strip()

        if not value:
            return

        self.entry.delete(0, tk.END)
        self.add_message(value, sender="You")

        # NAME
        if self.step == "name":
            self.name = value
            self.add_message(f"Nice to meet you, {self.name}!")
            self.ask_genre()

        # LANGUAGE
        elif self.step == "language":
            mapping = {
                "english": "English",
                "marathi": "Marathi",
                "मराठी": "Marathi",
                "hindi": "Hindi",
                "हिंदी": "Hindi",
                "any": "Any"
            }

            answer = value.strip().lower()

            if answer not in mapping:
                self.add_message(
                    "Please type English, Marathi, Hindi, or Any."
                )
                return

            self.preferences["language"] = mapping[answer]
            self.ask_length()

        # BOOK LENGTH
        elif self.step == "length":
            answer = value.title()

            if answer not in LENGTHS:
                self.add_message(
                    "Please type Short, Medium, Long, or Any."
                )
                return

            self.preferences["length"] = answer
            self.ask_level()

        # READING LEVEL
        elif self.step == "level":
            answer = value.title()

            if answer not in LEVELS:
                self.add_message(
                    "Please type Beginner, Intermediate, Advanced, or Any."
                )
                return

            self.preferences["level"] = answer
            self.recommend()

        elif self.step == "finished":
            self.add_message(
                "Please use Recommend Again or Restart below."
            )

    # =================================================
    # ASK GENRE
    # =================================================

    def ask_genre(self):
        self.step = "genre"

        self.add_message(
            "Which book genre do you prefer? Select a button below."
        )

        self.show_buttons(GENRES, self.select_genre)

    def select_genre(self, genre):
        if self.step != "genre":
            return

        self.preferences["genre"] = genre

        self.add_message("You selected: " + genre, sender="You")

        self.ask_language()

    # =================================================
    # ASK LANGUAGE
    # =================================================

    def ask_language(self):
        self.step = "language"

        self.add_message(
            "Which language do you prefer? "
            "You can type your answer or select a button."
        )

        self.show_buttons(LANGUAGES, self.select_language)

    def select_language(self, language):
        if self.step != "language":
            return

        self.preferences["language"] = language

        self.add_message("You selected: " + language, sender="You")

        self.ask_length()

    # =================================================
    # ASK BOOK LENGTH
    # =================================================

    def ask_length(self):
        self.step = "length"

        self.add_message("How long a book would you like?")

        self.show_buttons(LENGTHS, self.select_length)

    def select_length(self, length):
        if self.step != "length":
            return

        self.preferences["length"] = length

        self.add_message("You selected: " + length, sender="You")

        self.ask_level()

    # =================================================
    # ASK READING LEVEL
    # =================================================

    def ask_level(self):
        self.step = "level"

        self.add_message("What is your reading level?")

        self.show_buttons(LEVELS, self.select_level)

    def select_level(self, level):
        if self.step != "level":
            return

        self.preferences["level"] = level

        self.add_message("You selected: " + level, sender="You")

        self.recommend()

    # =================================================
    # RULE-BASED BOOK RECOMMENDATION
    # =================================================

    def recommend(self):
        self.clear_options()
        self.step = "finished"

        genre = self.preferences.get("genre", "Any")
        language = self.preferences.get("language", "Any")
        length = self.preferences.get("length", "Any")
        level = self.preferences.get("level", "Any")

        # Filter by language first
        available = [
            book for book in BOOKS
            if language == "Any"
            or book["language"].lower() == language.lower()
        ]

        # Weighted scoring
        scored = []

        for book in available:
            if book["title"] in self.seen_titles:
                continue

            score = 0

            if genre != "Any" and book["genre"].lower() == genre.lower():
                score += 4

            if language != "Any" and book["language"].lower() == language.lower():
                score += 5

            if length != "Any" and book["length"].lower() == length.lower():
                score += 2

            if level != "Any" and book["level"].lower() == level.lower():
                score += 2

            scored.append((score, book))

        # Highest scoring books first
        scored.sort(key=lambda item: item[0], reverse=True)

        self.results = scored[:3]

        self.add_message(
            f"Thank you, {self.name}! Here are your book recommendations."
        )

        if not self.results:
            self.add_message(
                "No more books are available in the current dataset "
                "for your selected language and preferences."
            )

            self.show_buttons(
                ["Recommend Again", "Restart", "Exit"],
                self.handle_action
            )

            return

        # Display recommendations
        for rank, (score, book) in enumerate(self.results, start=1):
            self.seen_titles.add(book["title"])

            self.add_message(
                f"📘 Recommendation {rank}\n"
                f"Title: {book['title']}\n"
                f"Author: {book['author']}\n"
                f"Genre: {book['genre']}\n"
                f"Language: {book['language']}\n"
                f"Length: {book['length']}\n"
                f"Reading level: {book['level']}\n"
                f"Match score: {score}/13\n\n"
                f"{book['description']}"
            )

        self.add_message(
            "Would you like new recommendations or start again?"
        )

        self.show_buttons(
            ["Recommend Again", "Restart", "Exit"],
            self.handle_action
        )

    # =================================================
    # HANDLE RECOMMEND AGAIN, RESTART, EXIT
    # =================================================

    def handle_action(self, action):
        self.clear_options()

        if action == "Exit":
            self.root.destroy()

        elif action == "Restart":
            self.restart()

        elif action == "Recommend Again":
            # FIX: Ask all preference questions again.
            # Keep the name and previously seen books.
            self.preferences = {}
            self.results = []

            self.add_message(
                f"Let's find more books for you, {self.name}!"
            )

            self.ask_genre()

    # =================================================
    # RESTART ENTIRE CHATBOT
    # =================================================

    def restart(self):
        self.clear_options()

        self.chat.configure(state=tk.NORMAL)
        self.chat.delete("1.0", tk.END)
        self.chat.configure(state=tk.DISABLED)

        self.name = ""
        self.step = "name"
        self.preferences = {}
        self.results = []
        self.seen_titles = set()

        self.entry.delete(0, tk.END)

        self.add_message(
            "Hello! Welcome to SmartBook AI.\n"
            "I will recommend books based on your preferences."
        )

        self.add_message("First, what is your name?")

        self.entry.focus_set()


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartBook(root)
    root.mainloop()
