from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game

class Time:
    def __init__(self, game:"Game"):
        self.game = game
        self.time = 0.0
        self.day = 0  # each season has 10 days
        self.season = 1  # 0 winter, 1 spring, 2 summer, 3 fall
        self.cycle_speed = 0.08
        self.daytimes = {
            0: "midnight",
            4: "dawn",
            6: "morning",
            12: "noon",
            16: "afternoon",
            19: "sunset",
            22: "night",
            24: "midnight"
        }

    def update(self):
        self.time += self.cycle_speed * self.game.delta_time

        if self.time >= 24.0:
            self.time -= 24.0
            self.day += 1

            if self.day >= 10:
                self.day = 0
                self.season = (self.season + 1) % 4

    def get_time(self):
        return self.time

    def day_state(self):
        hours = sorted(self.daytimes.keys())
        current_state = ""
        for hour in hours:
            if self.time >= hour:
                current_state = self.daytimes[hour]
            else:
                break
        return current_state
