import tkinter as tk
from sentence_generator import SentenceGenerator
import time
from difflib import SequenceMatcher


class TypingSpeed:

    def __init__(self, sentence_generator: SentenceGenerator()):
        self.generator = sentence_generator

        self.target_sentence = ""
        self.start_time = 0
        self.end_time = 0

        self.root = tk.Tk()
        self.root.title("Typing Speed App")
        self.root.geometry("740x360")

        self.text_intro = "This test will generate a sentence with random words for you to copy." \
                          " The timer starts as soon as you start typing. When you finish the " \
                          "sentence press 'ENTER' to submit it and see your result. Click 'Start' " \
                          "to begin."

        # Intro screen showing instructions
        self.frame_intro = tk.Frame(self.root)
        self.frame_intro.pack(expand=True)

        self.label_title = tk.Label(self.frame_intro, text="Typing Speed Test", font=("Helvetica", 24, "bold"))
        self.label_title.grid(row=0, column=0, padx=10, pady=10)

        self.message_intro = tk.Message(self.frame_intro, text=self.text_intro, font=("Helvetica", 16, "normal"), width=400)
        self.message_intro.grid(row=1, column=0, padx=10, pady=10)

        self.button_start = tk.Button(self.frame_intro,
                                      text="Start",
                                      font=("Helvetica", 16, "normal"),
                                      command=self.start_button)
        self.button_start.grid(row=2, column=0, padx=10, pady=10)

        # Typing test screen, only shows after user clicks start.
        self.frame_main = tk.Frame(self.root)

        # Frame to set same width of random text and user input.
        self.frame_text_boxes = tk.Frame(self.frame_main, bg="black")
        self.frame_text_boxes.grid(row=0, column=0, padx=10, pady=10)

        self.label_display_text = tk.Label(self.frame_text_boxes, bg="black", font=("Helvetica", 18, "normal"))
        self.label_display_text.grid(row=0, column=0, padx=20, pady=(20, 5))

        self.entry_user = tk.Entry(self.frame_text_boxes, justify="left", font=("Helvetica", 18, "normal"))
        self.entry_user.grid(row=1, column=0, padx=18, pady=(5, 20), sticky=tk.E+tk.W)
        self.entry_user.bind("<KeyPress>", self.start_timer)

        # Results displayed and reset button.
        self.label_speed = tk.Label(self.frame_main, text=f"Speed: __.__ WPM", font=("Helvetica", 18, "normal"))
        self.label_speed.grid(row=1, column=0, padx=10, pady=(20, 10))

        self.label_accuracy = tk.Label(self.frame_main, text="Accuracy: __._ %", font=("Helvetica", 18, "normal"))
        self.label_accuracy.grid(row=2, column=0, padx=10, pady=(10, 20))

        self.button_reset = tk.Button(self.frame_main, text="Reset", font=("Helvetica", 16, "normal"), command=self.reset_button)
        self.button_reset.grid(row=3, column=0, padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def start_button(self):
        """Hides intro frame and sets main frame."""
        self.frame_intro.pack_forget()
        self.frame_main.pack(expand=True)
        self.reset_button()
        self.entry_user.focus()

    def start_timer(self, key):
        """On first key press record system time in seconds as start_time, disable keypress binding
        and enable binding keypress of return button."""
        self.entry_user.unbind("<KeyPress>")
        self.start_time = time.time()
        self.entry_user.bind("<Return>", self.enter_button)

    def enter_button(self, enter):
        """On keypress of return button record system time in seconds as end_time, disable keypress of
        return button. Calculate time passes between key presses, calculate WPS and accuracy."""
        self.end_time = time.time()
        self.entry_user.unbind("<Return>")
        # Total time.
        typing_time_s = self.end_time - self.start_time
        user_sentence = self.entry_user.get()
        # Number of words typed.
        num_words = len(user_sentence.split())
        # WPM and Accuracy:
        wpm = num_words / (typing_time_s / 60)
        accuracy = SequenceMatcher(None, self.target_sentence, user_sentence).ratio() * 100
        # Show Accuracy in green if value is 100 % and red if not.
        if accuracy == 100:
            self.label_accuracy.config(fg="green")
        else:
            self.label_accuracy.config(fg="red")
        # Show WPM and Accuracy values.
        self.label_speed.config(text=f"Speed: {wpm:.1f} WPM")
        self.label_accuracy.config(text=f"Accuracy: {accuracy:.1f} %")

    def reset_button(self):
        """Show new sentence from SentenceGenerator and clear user entry.
        Reset key binding for the timer function."""
        self.entry_user.delete(0, "end")
        self.target_sentence = self.generator.build_random_sentence()
        self.label_display_text.config(text=self.target_sentence)
        self.entry_user.bind("<KeyPress>", self.start_timer)

    def on_closing(self):
        """End program when closing gui window."""
        self.root.destroy()
