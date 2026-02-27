# Deterministic Finite Automata (DFA) Simulator

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def simulate(self, input_string):
        current_state = self.start_state
        print(f"Start State: {current_state}\n")

        step = 1
        for symbol in input_string:
            print(f"Step {step}:")
            print(f"  Current State: {current_state}")
            print(f"  Input Symbol: {symbol}")

            if (current_state, symbol) not in self.transitions:
                print("No transition found!")
                print("\nResult: REJECTED")
                return

            next_state = self.transitions[(current_state, symbol)]
            print(f"  Transition: ({current_state}, {symbol}) → {next_state}\n")

            current_state = next_state
            step += 1

        print(f"Final State: {current_state}")

        if current_state in self.accept_states:
            print("Result: ACCEPTED")
        else:
            print("Result: REJECTED")


# Accepts strings ending with '01'

states = {"q0", "q1", "q2"}
alphabet = {"0", "1"}

transitions = {
    ("q0", "0"): "q1",
    ("q0", "1"): "q0",
    ("q1", "0"): "q1",
    ("q1", "1"): "q2",
    ("q2", "0"): "q1",
    ("q2", "1"): "q0",
}

start_state = "q0"
accept_states = {"q2"}

dfa = DFA(states, alphabet, transitions, start_state, accept_states)

# Input string
input_string = input("Enter input string (0s and 1s): ")

dfa.simulate(input_string)
