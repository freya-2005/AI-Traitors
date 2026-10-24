import random
from collections import Counter


class GameEngine:
    """Core game logic for AI Traitors."""

    def __init__(self):
        self.players = []
        self.traitor = None
        self.roles = {}
        self.eliminated = []
        self.votes = {}
        self.history = []
        self.round_number = 1
        self.started = False
        self.winner = None

    def start_game(self, player_names):
        """Start a new game and assign secret roles."""
        names = [
            name.strip()
            for name in player_names
            if name.strip()
        ]

        # Prevent duplicate player names.
        if len(names) != len(set(names)):
            raise ValueError("Every player must have a unique name.")

        if not 4 <= len(names) <= 10:
            raise ValueError("Enter between 4 and 10 players.")

        self.players = names
        self.traitor = random.choice(names)
        self.roles = {
            player: (
                "TRAITOR" if player == self.traitor
                else "FAITHFUL"
            )
            for player in names
        }

        self.eliminated = []
        self.votes = {}
        self.history = []
        self.round_number = 1
        self.started = True
        self.winner = None

        self.history.append(
            f"Round {self.round_number} has started."
        )

        return self.get_game_status()

    def get_alive_players(self):
        """Return players who are still in the game."""
        return [
            player for player in self.players
            if player not in self.eliminated
        ]

    def get_role(self, player_name):
        """Return one player's secret role."""
        if player_name not in self.roles:
            raise ValueError("Player not found.")

        return self.roles[player_name]

    def eliminate_player(self, player_name, reason="elimination"):
        """Eliminate a living player."""
        if not self.started:
            raise ValueError("Start a game first.")

        if player_name not in self.players:
            raise ValueError("Player not found.")

        if player_name in self.eliminated:
            raise ValueError("This player is already eliminated.")

        self.eliminated.append(player_name)
        self.history.append(
            f"{player_name} was eliminated by {reason}."
        )

        self.check_winner()
        return self.get_game_status()

    def cast_vote(self, voter, target):
        """Record a player's vote against another living player."""
        alive = self.get_alive_players()

        if not self.started:
            raise ValueError("Start a game first.")

        if voter not in alive:
            raise ValueError("The voter must be alive.")

        if target not in alive:
            raise ValueError("The target must be alive.")

        if voter == target:
            raise ValueError("Players cannot vote for themselves.")

        self.votes[voter] = target
        self.history.append(f"{voter} cast a vote.")

        return dict(self.votes)

    def finish_voting(self):
        """Eliminate the player with the most votes."""
        if not self.votes:
            raise ValueError("No votes have been cast.")

        counts = Counter(self.votes.values())
        highest = max(counts.values())

        candidates = [
            player for player, count in counts.items()
            if count == highest
        ]

        if len(candidates) > 1:
            self.history.append(
                "Voting ended in a tie. No player was eliminated."
            )
            eliminated_player = None
        else:
            eliminated_player = candidates[0]
            self.eliminate_player(
                eliminated_player,
                reason="voting"
            )

        self.votes = {}
        self.round_number += 1

        return {
            "eliminated_player": eliminated_player,
            "vote_counts": dict(counts),
            "game_status": self.get_game_status()
        }

    def check_winner(self):
        """Check whether the Traitor or Faithful team has won."""
        if not self.started:
            return None

        alive = self.get_alive_players()

        if self.traitor not in alive:
            self.winner = "FAITHFUL"
        elif len(alive) <= 2:
            self.winner = "TRAITOR"
        else:
            self.winner = None

        if self.winner:
            self.history.append(
                f"The {self.winner} team has won!"
            )

        return self.winner

    def get_game_status(self):
        """Return public game information."""
        return {
            "players": self.players.copy(),
            "alive_players": self.get_alive_players(),
            "eliminated": self.eliminated.copy(),
            "round_number": self.round_number,
            "history": self.history.copy(),
            "started": self.started,
            "winner": self.winner
        }

    def reset_game(self):
        """Reset the engine for a new game."""
        self.__init__()


# Create one game engine for use by the application.
game_engine = GameEngine()


# Helper functions for easier use in Flask routes.

def start_game(player_names):
    return game_engine.start_game(player_names)


def get_alive_players():
    return game_engine.get_alive_players()


def get_role(player_name):
    return game_engine.get_role(player_name)


def eliminate_player(player_name, reason="elimination"):
    return game_engine.eliminate_player(player_name, reason)


def cast_vote(voter, target):
    return game_engine.cast_vote(voter, target)


def finish_voting():
    return game_engine.finish_voting()


def check_winner():
    return game_engine.check_winner()


def get_game_status():
    return game_engine.get_game_status()


def reset_game():
    game_engine.reset_game()