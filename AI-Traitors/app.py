@app.route("/start", methods=["GET", "POST"])
def start():
    game = create_game()
    session["game"] = game

    player_role = (
        "TRAITOR"
        if game["traitor"] == "You"
        else "FAITHFUL"
    )

    return render_template("role.html", role=player_role)