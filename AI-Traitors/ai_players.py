# ==========================================
# AI PLAYERS + MEMORY
# ==========================================

AI_PLAYERS = {

    "Rahul": {
        "personality": "aggressive",
        "description": "Aggressive and confident."
    },

    "Neha": {
        "personality": "logical",
        "description": "Logical and analytical."
    },

    "Jay": {
        "personality": "quiet",
        "description": "Quiet and observant."
    },

    "Priya": {
        "personality": "social",
        "description": "Social and persuasive."
    }
}


# ==========================================
# AI MEMORY
# ==========================================

AI_MEMORY = {}


def reset_memory(players):

    global AI_MEMORY

    AI_MEMORY = {}

    for player in players:

        if player in AI_PLAYERS:

            AI_MEMORY[player] = []


def remember(player, event):

    if player not in AI_MEMORY:
        AI_MEMORY[player] = []

    AI_MEMORY[player].append(event)


def get_memory(player):

    return AI_MEMORY.get(player, [])


# ==========================================
# GET AI PLAYERS
# ==========================================

def get_ai_players(all_players):

    return [
        player
        for player in all_players
        if player in AI_PLAYERS
    ]


# ==========================================
# STARTING MESSAGE
# ==========================================

def generate_message(player, alive_players):

    if player not in AI_PLAYERS:

        return f"🤖 {player}: I am watching everyone carefully."

    personality = AI_PLAYERS[player]["personality"]

    if personality == "aggressive":

        return (
            f"🤖 {player}: "
            "I don't trust someone here. "
            "We need to stop wasting time."
        )

    elif personality == "logical":

        return (
            f"🤖 {player}: "
            "Let's look at everyone's behaviour "
            "and voting patterns before deciding."
        )

    elif personality == "quiet":

        return (
            f"🤖 {player}: "
            "I've been observing everyone. "
            "Something doesn't feel right."
        )

    elif personality == "social":

        return (
            f"🤖 {player}: "
            "We should hear everyone out "
            "before accusing someone."
        )

    return f"🤖 {player}: I am watching everyone."


# ==========================================
# AI DISCUSSION WITH MEMORY
# ==========================================

def generate_discussion(ai_players, traitor):

    messages = []

    # --------------------------------------
    # Rahul
    # --------------------------------------

    if "Rahul" in ai_players:

        memory = get_memory("Rahul")

        if len(memory) > 0:

            messages.append(
                "🤖 Rahul: "
                "I remember what happened earlier. "
                "I'm not changing my mind easily."
            )

        elif traitor == "Rahul":

            messages.append(
                "🤖 Rahul: "
                "I think Jay has been acting strangely. "
                "We should investigate him."
            )

        else:

            messages.append(
                "🤖 Rahul: "
                "I think Neha is suspicious. "
                "She's watching everyone too carefully."
            )


    # --------------------------------------
    # Neha
    # --------------------------------------

    if "Neha" in ai_players:

        memory = get_memory("Neha")

        if len(memory) > 0:

            messages.append(
                "🤖 Neha: "
                "I remember Rahul's earlier accusation. "
                "We should consider the previous votes."
            )

        elif traitor == "Neha":

            messages.append(
                "🤖 Neha: "
                "Rahul is being far too aggressive. "
                "I think we should focus on him."
            )

        else:

            messages.append(
                "🤖 Neha: "
                "Rahul, that's a strong accusation. "
                "What evidence do you have?"
            )


    # --------------------------------------
    # Priya
    # --------------------------------------

    if "Priya" in ai_players:

        memory = get_memory("Priya")

        if len(memory) > 0:

            messages.append(
                "🤖 Priya: "
                "We need to remember what everyone said "
                "in the previous round."
            )

        elif traitor == "Priya":

            messages.append(
                "🤖 Priya: "
                "Let's not accuse each other without evidence. "
                "I think Jay might be hiding something."
            )

        else:

            messages.append(
                "🤖 Priya: "
                "Rahul is pushing this accusation too quickly. "
                "We should hear everyone first."
            )


    # --------------------------------------
    # Jay
    # --------------------------------------

    if "Jay" in ai_players:

        memory = get_memory("Jay")

        if len(memory) > 0:

            messages.append(
                "🤖 Jay: "
                "I've been keeping track of everyone's behaviour. "
                "Some things don't add up."
            )

        elif traitor == "Jay":

            messages.append(
                "🤖 Jay: "
                "I agree with Priya. "
                "Maybe Rahul is trying to distract us."
            )

        else:

            messages.append(
                "🤖 Jay: "
                "I'm not convinced either way. "
                "I'm watching Rahul carefully."
            )


    # --------------------------------------
    # SAVE MESSAGES TO MEMORY
    # --------------------------------------

    for message in messages:

        for player in ai_players:

            remember(player, message)


    return messages