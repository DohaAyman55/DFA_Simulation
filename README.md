# Finite Automata Simulator & CFG Parser

Implementation of two core concepts from **Formal Languages and Automata Theory**:

- Deterministic Finite Automata (DFA) Simulator  
- Context-Free Grammar (CFG) Parser with Abstract Syntax Tree (AST)

Developed in **Python** as part of an academic project.

---

# Part 1 — DFA Simulator

## Features

- Define states, alphabet, and transitions
- Specify start and accepting states
- Step-by-step input simulation
- Displays **ACCEPTED / REJECTED** result
- GUI built with Tkinter

## Concepts

- Deterministic Finite Automata
- State transition functions
- Regular languages

---

# Part 2 — CFG Parser

## Features

- Predictive (LL-style) parsing
- FIRST and FOLLOW set usage
- Stack-based parsing algorithm
- Abstract Syntax Tree (AST) generation
- Syntax error detection

## Grammar Supports

- Assignment statements  
- Increment / decrement  
- Block statements  
- `for` loops  
- Arithmetic expressions  
- Relational expressions  

---

## Technologies Used

- Python  
- Tkinter  
- Stack-based parsing  
- Tree data structures  

---

## How to Run

Run the DFA Simulator:

```bash
python DFA sim_GUI.py
```

Run the CFG Parser:

```bash
python Parser.py
```

---

## Limitations

- Supports only deterministic finite automata (no NFA/ε-NFA)
- Grammar is predefined and manually configured
- No graphical DFA diagram visualization

---

## Future Improvements

- Add NFA and ε-NFA support
- Implement DFA state diagram visualization
- Allow dynamic grammar input
- Improve AST visualization

---

## Academic Context

This project demonstrates practical implementation of:

- Regular Languages  
- Context-Free Grammars  
- Predictive Parsing  
- Compiler-style AST construction  

---

**License:** Academic project – for educational purposes.
