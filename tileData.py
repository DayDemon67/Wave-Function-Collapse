from pygame.image import load
images = {
    "bridge": load("tiles/bridge.png"),
    "component": load("tiles/component.png"),
    "connection": load("tiles/connection.png"),
    "corner": load("tiles/corner.png"),
    "dskew": load("tiles/dskew.png"),
    "skew": load("tiles/skew.png"),
    "substrate": load("tiles/substrate.png"),
    "t": load("tiles/t.png"),
    "track": load("tiles/track.png"),
    "transition": load("tiles/transition.png"),
    "turn": load("tiles/turn.png"),
    "viad": load("tiles/viad.png"),
    "vias": load("tiles/vias.png"),
    "wire": load("tiles/wire.png")
}
edges = {
    "bridge": [1, 2, 1, 2],
    "component": [3, 3, 3, 3],
    "connection": [1, 4, 3, 5],
    "corner": [0, 0, 4, 5],
    "dskew": [1, 1, 1, 1],
    "skew": [1, 1, 0, 0],
    "substrate": [0, 0, 0, 0],
    "t": [0, 1, 1, 1],
    "track": [1, 0, 1, 0],
    "transition": [2, 0, 1, 0],
    "turn": [1, 1, 0, 0],
    "viad": [0, 1, 0, 1],
    "vias": [1, 0, 0, 0],
    "wire": [0, 2, 0, 2]
}
connections = {
    0: [0],
    1: [1],
    2: [2],
    3: [3],
    4: [5],
    5: [4]
}
dim = (14, 14)
tile_representations = {
    "bridge": "═╪═",
    "component": "▓▓▓",
    "connection": "▄█▄",
    "corner": "▄  ",
    "dskew": "\ \\",
    "skew": " \ ",
    "substrate": "░░░",
    "t": "─╤─",  #
    "track": " │ ",
    "transition": " ■ ",
    "turn": " └─",
    "viad": "─●─",
    "vias": " ● ",
    "wire": "═══"
}