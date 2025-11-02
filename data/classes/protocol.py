protocol = {
    0:"",       # client exit
    1:"s",      # player name/session id | Player sends name and server answers with a session id
    11:"sssii", # id scene name hat body | Register a new player in a scene
    12:"s",     # id | Unregister a new player in a scene (Only to client)
    13:"siisb", # id x y animation flipped | Update player attributes
    14:"sii",   # id hat body | Player change cosmetic
    15:"si",    # id emoji | Player emoji
}