input.onSound(DetectedSound.Loud, function () {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 5000, 4882, 255, 255, 1000, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
    radio.sendString("Name: Julek")
})
radio.onReceivedNumber(function (receivedNumber) {
    basic.showString("Num: ")
    basic.showString("" + receivedNumber)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendNumber(click)
    click += 1
})
radio.onReceivedString(function (receivedString) {
    basic.showString("Str: ")
    basic.showString(receivedString)
})
radio.onReceivedValue(function (name, value) {
    basic.showString("N:V: ")
    basic.showString(name)
    basic.showString(":")
    basic.showString("" + value)
})
let click = 0
radio.setGroup(255)
radio.sendValue("age", 12)
basic.forever(function () {
    basic.showArrow(ArrowNames.North)
})
