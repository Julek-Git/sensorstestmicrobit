def on_sound_loud():
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            5000,
            4882,
            255,
            255,
            1000,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    radio.send_string("Name: Julek")
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_received_number(receivedNumber):
    basic.show_string("Num: ")
    basic.show_string("" + str((receivedNumber)))
radio.on_received_number(on_received_number)

def on_logo_pressed():
    global click
    radio.send_number(click)
    click += 1
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_received_string(receivedString):
    basic.show_string("Str: ")
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    basic.show_string("N:V: ")
    basic.show_string(name)
    basic.show_string(":")
    basic.show_string("" + str((value)))
radio.on_received_value(on_received_value)

click = 0
radio.set_group(255)
radio.send_value("age", 12)

def on_forever():
    basic.show_arrow(ArrowNames.NORTH)
basic.forever(on_forever)
