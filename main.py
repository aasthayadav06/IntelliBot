
import re

# ==========================================
# IntelliBot: Intelligent Rule-Based Chatbot
# ==========================================

rules = [
    {
        "id": "R1",
        "pattern": r"\b(hi|hello|hey|hii|hiii|good morning|good afternoon|good evening)\b",
        "intent": "Greeting",
        "response": "Hello! I am IntelliBot. How can I help you?"
    },
    {
        "id": "R2",
        "pattern": r"\b(what is your name|who are you|your name)\b",
        "intent": "Bot Identity",
        "response": "My name is IntelliBot, a rule-based conversational agent."
    },
    {
        "id": "R3",
        "pattern": r"\b(how are you|how r you|how are u)\b",
        "intent": "Bot Status",
        "response": "I am functioning properly and ready to help you!"
    },
    {
        "id": "R4",
        "pattern": r"\b(what can you do|your features|help|your capabilities)\b",
        "intent": "Help",
        "response": "I can answer basic questions about AI, machine learning, Python, and neural networks."
    },
    {
        "id": "R5",
        "pattern": r"\b(what is ai|define ai|artificial intelligence meaning|meaning of ai)\b",
        "intent": "Artificial Intelligence",
        "response": "Artificial Intelligence (AI) enables computers to perform tasks like learning, reasoning, and problem-solving."
    },
    {
        "id": "R6",
        "pattern": r"\b(what is machine learning|define machine learning|meaning of machine learning)\b",
        "intent": "Machine Learning",
        "response": "Machine Learning is a branch of AI that allows computers to learn patterns from data."
    },
    {
        "id": "R7",
        "pattern": r"\b(what is python|define python|python programming)\b",
        "intent": "Python",
        "response": "Python is a high-level programming language known for its simple syntax and readability."
    },
    {
        "id": "R8",
        "pattern": r"\b(thank you|thanks|thx|thank u)\b",
        "intent": "Thanks",
        "response": "You're welcome! Feel free to ask me another question."
    },
    {
        "id": "R9",
        "pattern": r"\b(bye|goodbye|see you|exit|quit)\b",
        "intent": "Goodbye",
        "response": "Goodbye! It was nice helping you. Have a great day!"
    },
    {
        "id": "R10",
        "pattern": r"\b(applications of ai|uses of ai|ai applications|where is ai used|use of artificial intelligence)\b",
        "intent": "AI Applications",
        "response": "AI is used in healthcare, education, banking, transportation, cybersecurity, robotics, and virtual assistants."
    },
    {
        "id": "R11",
        "pattern": r"\b(what is deep learning|define deep learning)\b",
        "intent": "Deep Learning",
        "response": "Deep Learning is a branch of machine learning that uses multi-layered neural networks to learn complex patterns."
    },
    {
        "id": "R12",
        "pattern": r"\b(what is an algorithm|define algorithm|algorithm meaning)\b",
        "intent": "Algorithm",
        "response": "An algorithm is a step-by-step procedure used to solve a problem or complete a task."
    },
    {
        "id": "R13",
        "pattern": r"\b(what is a chatbot|what is chatbot|define chatbot)\b",
        "intent": "Chatbot",
        "response": "A chatbot is a computer program designed to communicate with users through text or voice."
    },
    {
        "id": "R14",
        "pattern": r"\b(what is an intelligent agent|what is intelligent agent|define intelligent agent)\b",
        "intent": "Intelligent Agent",
        "response": "An intelligent agent perceives its environment and takes actions to achieve its goals."
    },
    {
        "id": "R15",
        "pattern": r"\b(what is search algorithm|search algorithms|define search algorithm)\b",
        "intent": "Search Algorithms",
        "response": "Search algorithms explore possible states to find a solution. Examples include BFS, DFS, and A*."
    },
    {
        "id": "R16",
        "pattern": r"\b(what is bfs|breadth first search|explain bfs)\b",
        "intent": "Breadth-First Search",
        "response": "BFS explores nodes level by level, usually using a queue."
    },
    {
        "id": "R17",
        "pattern": r"\b(what is minimax|what is the minimax algorithm|minimax algorithm|explain minimax|minimax)\b",
        "intent": "Minimax Algorithm",
        "response": "Minimax is a decision-making algorithm used in games. It chooses moves by considering the best possible outcomes for both players."
    },
    {
        "id": "R18",
        "pattern": r"\b(what is dfs|depth first search|explain dfs)\b",
        "intent": "Depth-First Search",
        "response": "DFS explores one branch as deeply as possible before backtracking. It commonly uses a stack or recursion."
    },
    {
        "id": "R19",
        "pattern": r"\b(what is a constraint satisfaction problem|constraint satisfaction problem|what is csp)\b",
        "intent": "Constraint Satisfaction Problem",
        "response": "A Constraint Satisfaction Problem (CSP) involves variables, domains, and constraints that a solution must satisfy."
    },
    {
        "id": "R20",
        "pattern": r"\b(what is a neural network|what is neural network|what are neural networks|explain neural networks|neural network meaning)\b",
        "intent": "Neural Networks",
        "response": "Neural networks are computing systems inspired by the human brain that learn patterns from data."
    }
]


# Normalize user input
def normalize_input(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Match user input against predefined rules
def match_rule(user_input):
    text = normalize_input(user_input)

    for rule in rules:
        if re.search(rule["pattern"], text, re.IGNORECASE):
            return rule, 100

    return None, 0


# Display environment classification
def show_environment():
    print("\n--- Intelligent Agent Environment ---")
    print("Observability: Partially Observable")
    print("Nature: Deterministic")
    print("Task: Sequential")
    print("Changes: Static")
    print("-------------------------------------\n")


# Main chatbot
def main():
    last_question = None

    print("=" * 50)
    print("       Welcome to IntelliBot!")
    print(" Intelligent Rule-Based Conversational Agent")
    print("=" * 50)

    print("\nType 'help' to see available topics.")
    print("Type 'context' to view your last question.")
    print("Type 'environment' to view environment classification.")
    print("Type 'exit' to stop the chatbot.")

    show_environment()

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nIntelliBot: Goodbye!")
            break

        if not user_input:
            print("IntelliBot: Please type a message.")
            continue

        normalized = normalize_input(user_input)

        if normalized in ("exit", "quit", "goodbye", "bye"):
            rule, confidence = match_rule(user_input)
            print("\nMatched Rule: R9")
            print("Intent: Goodbye")
            print("Current State: Conversation ending")
            print("Selected Action: Display goodbye response")
            print("Match Confidence: 100%")
            print("IntelliBot:", rules[8]["response"])
            break

        if normalized == "context":
            print("\nMatched Rule: CONTEXT")
            print("Intent: Conversation Context")
            print("Current State:", last_question if last_question else "No previous question")
            print("Selected Action: Display last question")
            print("Match Confidence: 100%")
            print("IntelliBot:", f"Your last question was: {last_question}" if last_question else "You haven't asked a question yet.")
            continue

        if normalized == "environment":
            show_environment()
            continue

        if normalized == "help":
            print("\nMatched Rule: R4")
            print("Intent: Help")
            print("Current State: Help requested")
            print("Selected Action: Display available topics")
            print("Match Confidence: 100%")
            print("IntelliBot: You can ask about AI, machine learning, Python, deep learning,")
            print("chatbots, intelligent agents, BFS, DFS, minimax, CSP, and neural networks.")
            continue

        matched_rule, confidence = match_rule(user_input)
        last_question = user_input

        if matched_rule:
            print("\nMatched Rule:", matched_rule["id"])
            print("Intent:", matched_rule["intent"])
            print("Current State:", user_input)
            print("Selected Action: Display response for", matched_rule["intent"])
            print("Match Confidence:", str(confidence) + "%")
            print("IntelliBot:", matched_rule["response"])
        else:
            print("\nMatched Rule: NONE")
            print("Intent: Unknown")
            print("Current State:", user_input)
            print("Selected Action: Display fallback response")
            print("Match Confidence: 0%")
            print("IntelliBot: I don't know that one yet. Type 'help' to see available topics.")


if __name__ == "__main__":
    main()

