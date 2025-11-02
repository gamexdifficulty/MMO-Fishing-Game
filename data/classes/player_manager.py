from data.classes.player import Player

class PlayerManager:
    def __init__(self, game):
        self.game = game
        self.player_list = {}
        self.network_queue = []

    def update(self):
        if len(self.network_queue) > 0:
            for player_data in self.network_queue:
                # Creating player object here, because sprite objects cant be created in threads
                player = Player(self.game)
                player.id = player_data[0]
                player.name = player_data[1]
                player.hat = player_data[2]
                player.body = player_data[3]
                self.register_player(player)

            self.network_queue.clear()

        for player in self.player_list:
            self.player_list[player].update()

    def draw(self):
        for player in self.player_list:
            self.player_list[player].draw()
    
    def get(self,session_id):
        if session_id in self.player_list:
            return self.player_list[session_id]
        else:
            return False

    def register_player(self,player):
        self.player_list[player.id] = player

    def create_network_player(self,session_id:str,name:str,hat:int,body:int):
        self.network_queue.append([session_id,name,hat,body])

    def unregister_player(self,player):
        if player.id in self.player_list:
            del self.player_list[player.id]