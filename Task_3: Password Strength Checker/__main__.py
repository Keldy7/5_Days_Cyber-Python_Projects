# ========= Password Strength Checker =========
# Author: Aude Marie K.
# Creation date: 03rd October 2024

import re
import tkinter as tk
from tkinter import messagebox

class PasswordStrengthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.password_visible = False
        self.create_widgets()

        # Parametres de config
        self.size = 10

    def create_widgets(self):
        tk.Label(self.root, text = "Enter your password: ").pack(pady = self.size)

        # Combiner le champ de mot de passe et le bouton œil
        self.password_frame = tk.Frame(self.root)
        self.password_frame.pack(pady = 5)

        # Zone de saisie du mot de passe
        self.password_entry = tk.Entry(self.password_frame, width = self.size * 4, show="*")
        self.password_entry.pack(side = tk.LEFT)

        # Bouton pour afficher/masquer le mot de passe (œil)
        self.toggle_button = tk.Button(self.password_frame, text = "👁️", command = self.toggle_password_visibility)
        self.toggle_button.pack(side = tk.LEFT, padx=5)

        # Bouton pour soumettre le mot de passe
        tk.Button(self.root, text = "Check Strength", command = self.check_password_strength).pack(pady = self.size * 2)

        # Zone de résultats
        self.result_label = tk.Label(self.root, text = "")
        self.result_label.pack(pady = self.size)

    
    def toggle_password_visibility(self):
        # Si le mot de passe est actuellement masqué, l'afficher
        if self.password_visible:
            self.password_entry.config(show = "*")
            self.password_visible = False
        else:
            self.password_entry.config(show = "")
            self.password_visible = True

    def check_password_strength(self):
        password = self.password_entry.get()
        score, feedback = self.evaluate_password(password)
        self.result_label.config(text = f"Password strength: {feedback}")

    def evaluate_password(self, password):
        score = 0
        feedback = ""

        # Critère 1: Longueur
        if len(password) >= 8:
            score += 1
        else:
            feedback += "Password should be at least 8 characters long.\n"

        # Critère 2: Lettres minuscules
        if re.search("[a-z]", password):
            score += 1
        else:
            feedback += "Password should contain lowercase letters.\n"

        # Critère 3: Lettres majuscules
        if re.search("[A-Z]", password):
            score += 1
        else:
            feedback += "Password should contain uppercase letters.\n"

        # Critère 4: Chiffres
        if re.search("[0-9]", password):
            score += 1
        else:
            feedback += "Password should contain digits.\n"

        # Critère 5: Caractères spéciaux
        if re.search("[@#$%^&*()_+!]", password):
            score += 1
        else:
            feedback += "Password should contain special characters (e.g., @, #, $, etc.).\n"

        # Score de force du mot de passe
        if score == 5:
            feedback = "Very Strong"
        elif score == 4:
            feedback = "Strong"
        elif score == 3:
            feedback = "Moderate"
        elif score == 2:
            feedback = "Weak"
        else:
            feedback = "Very Weak"

        return score, feedback

def main():
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
