# Rock, Paper, Scissors 🎮

This is a simple Python game where you can play **Rock, Paper, Scissors** against the computer.  

## 🎯 Rules
- Rock (0) beats Scissors (2)  
- Scissors (2) beat Paper (1)  
- Paper (1) beats Rock (0)  
- If both choices are the same → it's a **tie**

## 🔢 Choices
We represent the moves using numbers:
- `0` → Rock 🪨  
- `1` → Paper 📄  
- `2` → Scissors ✂️  

## 🏆 Possible Outcomes
| User Choice | Computer Choice | Winner   |
|-------------|-----------------|----------|
| 0 (Rock)    | 0 (Rock)        | Tie      |
| 0 (Rock)    | 1 (Paper)       | Computer |
| 0 (Rock)    | 2 (Scissors)    | User     |
| 1 (Paper)   | 0 (Rock)        | User     |
| 1 (Paper)   | 1 (Paper)       | Tie      |
| 1 (Paper)   | 2 (Scissors)    | Computer |
| 2 (Scissors)| 0 (Rock)        | Computer |
| 2 (Scissors)| 1 (Paper)       | User     |
| 2 (Scissors)| 2 (Scissors)    | Tie      |

## ▶️ How to Play
1. Run the program.  
2. Enter your choice (`0`, `1`, or `2`).  
3. The computer will randomly select its choice.  
4. The winner will be displayed.  
