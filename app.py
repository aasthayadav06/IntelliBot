import streamlit as st
from main import rules, match_rule, normalize_input

# --------------------------------------------------

# PAGE CONFIGURATION

# --------------------------------------------------

st.set_page_config(
page_title="IntelliBot",
page_icon="IB",
layout="wide"
)

# --------------------------------------------------

# HEADER

# --------------------------------------------------

st.title("IntelliBot")
st.subheader("Intelligent Rule-Based Conversational Agent")

st.write(
"Welcome to IntelliBot! Ask questions about Artificial Intelligence, "
"Machine Learning, Python, Deep Learning, Search Algorithms, "
"Neural Networks, and more."
)

st.divider()

# --------------------------------------------------

# SESSION STATE

# --------------------------------------------------

if something:
    st.session_state.messages = []

if "last_question" not in st.session_state:
    st.session_state.last_question = None

if "last_decision" not in st.session_state:
    st.session_state.last_decision = {
        "rule_id": "NONE",
        "intent": "Waiting for input",
        "confidence": 0,
        "action": "Waiting for user message"
    }

# --------------------------------------------------

# HELPER: ENVIRONMENT CLASSIFICATION

# --------------------------------------------------

# --------------------------------------------------
# HELPER: ENVIRONMENT CLASSIFICATION
# --------------------------------------------------

def environment_response():
    return (
        "**Intelligent Agent Environment**\n\n"
        "- **Observability:** Partially Observable\n"
        "- **Nature:** Deterministic\n"
        "- **Task:** Sequential\n"
        "- **Changes:** Static\n"
    )

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.header("About IntelliBot")

st.write(
    "IntelliBot is a rule-based conversational agent. "
    "It matches user messages against predefined regular-expression "
    "patterns and returns the corresponding response."
)

st.metric("Total Rules", len(rules))

st.subheader("Available Commands")
st.markdown(
    "- `help` — Show available topics\n"
    "- `context` — Display the previous regular message\n"
    "- `environment` — Show environment classification\n"
    "- `clear` — Clear the conversation\n"
    "- `bye` — End the conversation"
)

st.divider()
st.subheader("Supported Topics")

for rule in rules:
    st.write(f'{rule["id"]}: {rule["intent"]}')

if st.button("Clear Conversation", use_container_width=True):
    st.session_state.messages = []
    st.session_state.last_question = None
    st.session_state.last_decision = {
        "rule_id": "NONE",
        "intent": "Conversation Reset",
        "confidence": 100,
        "action": "Clear conversation"
    }
    st.rerun()


# --------------------------------------------------

# DISPLAY CHAT HISTORY

# No emoji or image avatars are used.

# --------------------------------------------------


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])




# --------------------------------------------------

# CHAT INPUT

# --------------------------------------------------

user_input = st.chat_input("Type your message here...")

if user_input:
normalized = normalize_input(user_input)

```
# Display user message
st.session_state.messages.append({
    "role": "user",
    "content": user_input
})

response = ""
rule_id = "NONE"
intent = "Unknown"
confidence = 0
action = "Display fallback response"

# ----------------------------------------------
# CLEAR COMMAND
# ----------------------------------------------

if normalized in ("clear", "clear chat", "reset"):
    st.session_state.messages = []
    st.session_state.last_question = None

    st.session_state.last_decision = {
        "rule_id": "NONE",
        "intent": "Conversation Reset",
        "confidence": 100,
        "action": "Clear conversation"
    }

    st.rerun()

# ----------------------------------------------
# GOODBYE COMMAND
# ----------------------------------------------

elif normalized in ("exit", "quit", "goodbye", "bye"):
    matched_rule, confidence = match_rule(user_input)

    if matched_rule:
        response = matched_rule["response"]
        rule_id = matched_rule["id"]
        intent = matched_rule["intent"]
    else:
        response = "Goodbye! It was nice helping you. Have a great day!"
        rule_id = "R9"
        intent = "Goodbye"

    confidence = 100
    action = "Display goodbye response"

# ----------------------------------------------
# CONTEXT COMMAND
# ----------------------------------------------

elif normalized == "context":
    if st.session_state.last_question:
        response = (
            "Your last question was: "
            + st.session_state.last_question
        )
    else:
        response = "You haven't asked a question yet."

    rule_id = "CONTEXT"
    intent = "Conversation Context"
    confidence = 100
    action = "Display last regular message"

# ----------------------------------------------
# ENVIRONMENT COMMAND
# ----------------------------------------------

elif normalized == "environment":
    response = environment_response()
    rule_id = "ENVIRONMENT"
    intent = "Environment Classification"
    confidence = 100
    action = "Display environment classification"

# ----------------------------------------------
# HELP COMMAND
# ----------------------------------------------

elif normalized == "help":
    topics = ", ".join(rule["intent"] for rule in rules)

    response = (
        "**Available topics:**\n\n"
        + topics
        + "\n\nYou can also type `context`, `environment`, "
          "`clear`, or `bye`."
    )

    rule_id = "R4"
    intent = "Help"
    confidence = 100
    action = "Display available topics"

# ----------------------------------------------
# NORMAL RULE MATCHING
# ----------------------------------------------

else:
    # Store only regular messages as the previous message.
    st.session_state.last_question = user_input

    matched_rule, confidence = match_rule(user_input)

    if matched_rule:
        response = matched_rule["response"]
        rule_id = matched_rule["id"]
        intent = matched_rule["intent"]
        action = "Display response for " + intent
    else:
        response = (
            "I don't know that one yet. "
            "Type 'help' to see the available topics."
        )

        rule_id = "NONE"
        intent = "Unknown"
        confidence = 0
        action = "Display fallback response"

# ----------------------------------------------
# SAVE ASSISTANT RESPONSE
# ----------------------------------------------

st.session_state.messages.append({
    "role": "assistant",
    "content": response
})

# ----------------------------------------------
# SAVE DECISION DETAILS
# ----------------------------------------------

st.session_state.last_decision = {
    "rule_id": rule_id,
    "intent": intent,
    "confidence": confidence,
    "action": action
}

st.rerun()
```

# --------------------------------------------------

# DECISION DETAILS

# --------------------------------------------------

st.divider()
st.subheader("Decision Details")

decision = st.session_state.last_decision

col1, col2 = st.columns(2)

with col1:
st.write("**Matched Rule:**", decision["rule_id"])
st.write("**Intent:**", decision["intent"])

with col2:
st.write(
"**Match Confidence:**",
str(decision["confidence"]) + "%"
)
st.write("**Selected Action:**", decision["action"])

st.caption(
"IntelliBot uses predefined rules and regular expressions. "
"Its confidence score represents rule matching, not a trained "
"machine-learning probability."
)
