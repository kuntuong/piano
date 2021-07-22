import play
import pygame

# Set the backdrop to a color
play.set_backdrop("light green")

# The home music when logged on
pygame.mixer_music.load("hello.ogg")
pygame.mixer_music.play()

# The list for keys
keys = []

# The lists for sounds
sounds_1 = []
sounds_2 = []
sounds_3 = []

# The list for the melody
melody = []

chosen_instrument = 0

# The keys on piano in a for loop
@play.when_program_starts
def start():
        instrument_keys[0].color = "green"
        
for i in range(8):
        key = play.new_box(
                color = "white",
                border_color = "black",
                border_width = 3,
                x = -180 + (50 * i), y = 0,
                width = 40,
                height = 100
        )
        keys.append(key)

        # The sounds for the keys
        sound_1 = pygame.mixer.Sound("c" + str(i + 1) + ".ogg")
        sounds_1.append(sound_1)

        sound_2 = pygame.mixer.Sound("f" + str(i + 1) + ".ogg")
        sounds_2.append(sound_2)
        
        sound_3 = pygame.mixer.Sound("g" + str(i + 1) + ".ogg")
        sounds_3.append(sound_3)

instrument_1_sounds = []
instrument_2_sounds = []
instrument_3_sounds = []

instrument_keys = []
instrument_keys_text = []

for i in range(3):
        box_instrument = play.new_box(
                color="white",
                border_color="black",
                border_width = 1,
                x = -185 + (i * 180), y = -250,
                width=160,
                height=50
        )

        ki = play.new_text(
                words="Instrument " + str(i + 1),
                x = -185 + (i * 180), y = -250,
                font_size= 20,
                color="blue"
        )
        instrument_keys.append(box_instrument)
        instrument_keys_text.append(ki)

text_1 = play.new_text(
        words="Piano for Fun!",
        x=0,
        y=200,
        font=None,
        font_size=55,
        color="black"
)

text_2 = play.new_text(
        words="Create your melody by pressing the keys",
        x=0,
        y=150,
        font=None,
        font_size=55,
        color="black"
)

play_box = play.new_box(
        color = "light blue",
        border_color = "black",
        border_width = 1,
        x = -100,
        y = -140,
        width = 170,
        height = 55
)

clear_box = play.new_box(
        color = "light yellow",
        border_color = "black",
        border_width = 1,
        x = 100,
        y = -140,
        width = 170,
        height = 55
)

play_text = play.new_text(
        words="play melody",
        x= -100,
        y= -140,
        font=None,
        font_size=20,
        color="black"
)

clear_text = play.new_text(
        words="clear melody",
        x= 100,
        y= -140,
        font=None,
        font_size=20,
        color="black"
)

@play.repeat_forever
def repeat():
        for i in range(len(keys)):
                if keys[i].is_clicked:
                        if instrument_keys[0].color == "green":
                                sounds_1[i].play()
                        elif instrument_keys[1].color == "green":
                                sounds_2[i].play()
                        elif instrument_keys[2].color == "green":
                                sounds_3[i].play()

                        melody.append(i)

        for i in range(len(instrument_keys)):
                if instrument_keys[i].is_clicked:
                        chosen_instrument = i

                        instrument_keys[i].color = "green"
                        
                        for j in range(len(instrument_keys)):
                                if j == i :
                                        instrument_keys[j].color="green"
                                else:
                                        instrument_keys[j].color="white"

@play_box.when_clicked
async def play_clicked():
        for i in melody:
                await play.timer(seconds=0.5)
                if instrument_keys[0].color == "green":
                        sounds_1[i].play()
                elif instrument_keys[1].color == "green":
                        sounds_2[i].play()
                elif instrument_keys[2].color == "green":
                        sounds_3[i].play()

@clear_box.when_clicked
def clear_clicked():
        melody.clear()
        
play.start_program()

