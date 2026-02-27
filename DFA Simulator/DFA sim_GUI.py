import tkinter as tk
from tkinter import messagebox, scrolledtext


class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def simulate(self, input_string, output_box):
        current_state = self.start_state
        output_box.delete("1.0", tk.END)

        output_box.insert(tk.END, f"Start State: {current_state}\n\n")

        step = 1
        for symbol in input_string:
            output_box.insert(tk.END, f"Step {step}:\n")
            output_box.insert(tk.END, f"  Current State: {current_state}\n")
            output_box.insert(tk.END, f"  Input Symbol: {symbol}\n")

            if symbol not in self.alphabet:
                output_box.insert(tk.END, "  Symbol not in alphabet\n")
                output_box.insert(tk.END, "\nResult: REJECTED")
                return

            if (current_state, symbol) not in self.transitions:
                output_box.insert(tk.END, "  No transition defined\n")
                output_box.insert(tk.END, "\nResult: REJECTED")
                return

            next_state = self.transitions[(current_state, symbol)]
            output_box.insert(
                tk.END, f"  Transition: ({current_state}, {symbol}) → {next_state}\n\n"
            )

            current_state = next_state
            step += 1

        output_box.insert(tk.END, f"Final State: {current_state}\n")

        if current_state in self.accept_states:
            output_box.insert(tk.END, "Result: ACCEPTED")
        else:
            output_box.insert(tk.END, "Result: REJECTED")

### Core Funtion ###

def simulate_dfa():
    try:
        states = set(states_entry.get().split(","))
        alphabet = set(alphabet_entry.get().split(","))
        start_state = start_entry.get()
        accept_states = set(accept_entry.get().split(","))

        transitions = {}
        lines = transitions_text.get("1.0", tk.END).strip().split("\n")

        for line in lines:
            if line:
                left, right = line.split("->")
                state, symbol = left.split(",")
                transitions[(state, symbol)] = right

        input_string = string_entry.get()

        dfa = DFA(states, alphabet, transitions, start_state, accept_states)
        dfa.simulate(input_string, output_text)

    except Exception as e:
        messagebox.showerror("Error", "Invalid DFA input format")


### GUI ###

root = tk.Tk()
root.title("Finite Automata Simulator (DFA)")
root.geometry("700x700")

tk.Label(root, text="States (comma-separated):").pack()
states_entry = tk.Entry(root, width=50)
states_entry.pack()

tk.Label(root, text="Alphabet (comma-separated):").pack()
alphabet_entry = tk.Entry(root, width=50)
alphabet_entry.pack()

tk.Label(root, text="Start State:").pack()
start_entry = tk.Entry(root, width=50)
start_entry.pack()

tk.Label(root, text="Accept States (comma-separated):").pack()
accept_entry = tk.Entry(root, width=50)
accept_entry.pack()

tk.Label(root, text="Transitions (one per line: q0,0->q1):").pack()
transitions_text = scrolledtext.ScrolledText(root, width=60, height=8)
transitions_text.pack()

tk.Label(root, text="Input String:").pack()
string_entry = tk.Entry(root, width=50)
string_entry.pack()

tk.Button(root, text="Simulate DFA", command=simulate_dfa).pack(pady=10)

tk.Label(root, text="Simulation Output:").pack()
output_text = scrolledtext.ScrolledText(root, width=80, height=25)
output_text.pack()

root.mainloop()
