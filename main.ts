input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Start = 0
    basic.setLedColor(0xff0000)
    Programm = Programm + 1
    SchrittnummerGlobal = 1
    GeschwindigkeitAlt = -1
    if (Programm > 4) {
        Programm = 1
    }
    AnzeigeProgramm()
})
// Stossstange
function Programm1 () {
    if (SchrittnummerGlobal == 1) {
        if (Start == 1) {
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 10) {
        if (calliBot2.readBumperSensor(C2Sensor.rechts, C2State.an) && calliBot2.readBumperSensor(C2Sensor.links, C2State.an)) {
            SchrittnummerGlobal = 20
        } else if (calliBot2.readBumperSensor(C2Sensor.rechts, C2State.an)) {
            SchrittnummerGlobal = 30
        } else if (calliBot2.readBumperSensor(C2Sensor.links, C2State.an)) {
            SchrittnummerGlobal = 40
        } else if (SchrittNeu) {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, Geschwindigkeit)
            calliBot2.setLed(C2Motor.beide, false)
        }
    } else if (SchrittnummerGlobal == 20) {
        calliBot2.setLed(C2Motor.beide, true)
        calliBot2.motor(C2Motor.beide, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 500
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    } else if (SchrittnummerGlobal == 21) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, Geschwindigkeit)
            calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, Geschwindigkeit)
            ZeitPause = 400
            StartZeitPause = ZeitAktuell
            SchrittnummerGlobal = 22
        }
    } else if (SchrittnummerGlobal == 22) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 30) {
        calliBot2.setLed(C2Motor.links, false)
        calliBot2.setLed(C2Motor.rechts, true)
        calliBot2.motorStop(C2Motor.rechts, C2Stop.Bremsen)
        calliBot2.motor(C2Motor.links, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    } else if (SchrittnummerGlobal == 31) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 40) {
        calliBot2.setLed(C2Motor.rechts, false)
        calliBot2.setLed(C2Motor.links, true)
        calliBot2.motorStop(C2Motor.links, C2Stop.Bremsen)
        calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    } else if (SchrittnummerGlobal == 41) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else {
        Start = 0
        SchrittnummerGlobal = 1
    }
}
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    if (Start == 0) {
        Start = 1
        basic.setLedColor(0x00ff00)
        AnzeigeProgramm()
    } else {
        basic.setLedColor(0xff0000)
        Start = 0
        GeschwindigkeitAlt = -1
    }
})
// Fahren auf dunkler Linie
function Programm4 () {
    if (SchrittnummerGlobal == 1) {
        if (Start == 1) {
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 10) {
        if (calliBot2.readLineSensor(C2Sensor.rechts, C2SensorStatus.hell) && calliBot2.readLineSensor(C2Sensor.links, C2SensorStatus.hell)) {
            SchrittnummerGlobal = 20
        } else if (calliBot2.readLineSensor(C2Sensor.rechts, C2SensorStatus.hell)) {
            SchrittnummerGlobal = 30
        } else if (calliBot2.readLineSensor(C2Sensor.links, C2SensorStatus.hell)) {
            SchrittnummerGlobal = 40
        } else if (SchrittNeu) {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, Geschwindigkeit)
            calliBot2.setLed(C2Motor.beide, false)
        }
    } else if (SchrittnummerGlobal == 20) {
        calliBot2.setLed(C2Motor.beide, true)
        calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, Geschwindigkeit)
        calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    } else if (SchrittnummerGlobal == 21) {
        if (calliBot2.readLineSensor(C2Sensor.rechts, C2SensorStatus.dunkel) && calliBot2.readLineSensor(C2Sensor.links, C2SensorStatus.dunkel)) {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, Geschwindigkeit)
            SchrittnummerGlobal = 10
        }
        if (IstZeitPause >= ZeitPause) {
            SchrittnummerGlobal = 22
            SuchZeit = SuchZeit + SuchZeit
        }
        if (SuchZeit > 2000) {
            SuchZeit = 2000
        }
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        calliBot2.motor(C2Motor.beide, C2Dir.rueckwaerts, 40)
    } else if (SchrittnummerGlobal == 22) {
        if (calliBot2.readLineSensor(C2Sensor.rechts, C2SensorStatus.dunkel) && calliBot2.readLineSensor(C2Sensor.links, C2SensorStatus.dunkel)) {
            calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, Geschwindigkeit)
            calliBot2.motor(C2Motor.rechts, C2Dir.vorwaerts, Geschwindigkeit)
            SchrittnummerGlobal = 10
        }
        if (IstZeitPause >= ZeitPause) {
            SchrittnummerGlobal = 21
            SuchZeit = SuchZeit + SuchZeit
        }
        if (SuchZeit > 2000) {
            SuchZeit = 2000
        }
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, Geschwindigkeit)
        calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, Geschwindigkeit)
    } else if (SchrittnummerGlobal == 30) {
        calliBot2.setLed(C2Motor.links, false)
        calliBot2.setLed(C2Motor.rechts, true)
        calliBot2.motorStop(C2Motor.rechts, C2Stop.Bremsen)
        calliBot2.motor(C2Motor.links, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    } else if (SchrittnummerGlobal == 31) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 40) {
        calliBot2.setLed(C2Motor.rechts, false)
        calliBot2.setLed(C2Motor.links, true)
        calliBot2.motorStop(C2Motor.links, C2Stop.Bremsen)
        calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    } else if (SchrittnummerGlobal == 41) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else {
        Start = 0
        SchrittnummerGlobal = 1
    }
}
input.onPinTouchEvent(TouchPin.P0, input.buttonEventDown(), function () {
    Geschwindigkeit = Geschwindigkeit - 4
    if (Geschwindigkeit < 0) {
        Geschwindigkeit = 0
    }
})
function AnzeigeProgramm () {
    if (Programm == 1) {
        basic.showLeds(`
            # . . . .
            . . . . .
            . # # # .
            # # # # #
            # # . # #
            `)
    } else if (Programm == 2) {
        basic.showLeds(`
            # # . . .
            . . . . .
            # . . # #
            # . # # #
            # . . # #
            `)
    } else if (Programm == 3) {
        basic.showLeds(`
            # # # . .
            . . . . .
            . # # # .
            # . . . #
            . # # # .
            `)
    } else if (Programm == 4) {
        basic.showLeds(`
            # # # # .
            . . . . .
            . . # # .
            # # . . #
            . . . # .
            `)
    }
}
// Fahren bis dunkle Linie
function Programm3 () {
    if (SchrittnummerGlobal == 1) {
        if (Start == 1) {
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 10) {
        if (calliBot2.readLineSensor(C2Sensor.rechts, C2SensorStatus.dunkel) && calliBot2.readLineSensor(C2Sensor.links, C2SensorStatus.dunkel)) {
            SchrittnummerGlobal = 20
        } else if (calliBot2.readLineSensor(C2Sensor.rechts, C2SensorStatus.dunkel)) {
            SchrittnummerGlobal = 30
        } else if (calliBot2.readLineSensor(C2Sensor.links, C2SensorStatus.dunkel)) {
            SchrittnummerGlobal = 40
        } else if (SchrittNeu) {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, Geschwindigkeit)
            calliBot2.setLed(C2Motor.beide, false)
        }
    } else if (SchrittnummerGlobal == 20) {
        calliBot2.setLed(C2Motor.beide, true)
        calliBot2.motor(C2Motor.beide, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 500
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    } else if (SchrittnummerGlobal == 21) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, Geschwindigkeit)
            calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, Geschwindigkeit)
            ZeitPause = 400
            StartZeitPause = ZeitAktuell
            SchrittnummerGlobal = 22
        }
    } else if (SchrittnummerGlobal == 22) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 30) {
        calliBot2.setLed(C2Motor.links, false)
        calliBot2.setLed(C2Motor.rechts, true)
        calliBot2.motorStop(C2Motor.rechts, C2Stop.Bremsen)
        calliBot2.motor(C2Motor.links, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    } else if (SchrittnummerGlobal == 31) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 40) {
        calliBot2.setLed(C2Motor.rechts, false)
        calliBot2.setLed(C2Motor.links, true)
        calliBot2.motorStop(C2Motor.links, C2Stop.Bremsen)
        calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    } else if (SchrittnummerGlobal == 41) {
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
            SchrittnummerGlobal = 10
        }
    } else {
        Start = 0
        SchrittnummerGlobal = 1
    }
}
function LEDAnsteuerung () {
    if (Start == 1) {
        if (SchrittNummerLED == 1) {
            SchrittNummerLED = 2
            ZeitBelWechsel = control.millis()
            calliBot2.setRgbLed(C2RgbLed.LV, BelRot, BelGruen, BelBlau)
            calliBot2.setRgbLed(C2RgbLed.LH, 0, 0, 0)
        } else if (SchrittNummerLED == 2) {
            if (BelDauer >= BelWechsel) {
                SchrittNummerLED = 3
                ZeitBelWechsel = ZeitAktuell
                calliBot2.setRgbLed(C2RgbLed.LV, 0, 0, 0)
                calliBot2.setRgbLed(C2RgbLed.RV, BelRot, BelGruen, BelBlau)
            }
        } else if (SchrittNummerLED == 3) {
            if (BelDauer >= BelWechsel) {
                SchrittNummerLED = 4
                ZeitBelWechsel = ZeitAktuell
                calliBot2.setRgbLed(C2RgbLed.RV, 0, 0, 0)
                calliBot2.setRgbLed(C2RgbLed.RH, BelRot, BelGruen, BelBlau)
            }
        } else if (SchrittNummerLED == 4) {
            if (BelDauer >= BelWechsel) {
                SchrittNummerLED = 5
                ZeitBelWechsel = ZeitAktuell
                calliBot2.setRgbLed(C2RgbLed.RH, 0, 0, 0)
                calliBot2.setRgbLed(C2RgbLed.LH, BelRot, BelGruen, BelBlau)
            }
        } else if (SchrittNummerLED == 5) {
            if (BelDauer >= BelWechsel) {
                SchrittNummerLED = 1
                ZeitBelWechsel = ZeitAktuell
                if (BelRot > 0) {
                    BelBlau = 0
                    BelGruen = 16
                    BelRot = 0
                } else if (BelGruen > 0) {
                    BelBlau = 16
                    BelGruen = 0
                    BelRot = 0
                } else if (BelBlau > 0) {
                    BelBlau = 0
                    BelGruen = 0
                    BelRot = 16
                }
            }
        } else {
            calliBot2.setRgbLed(C2RgbLed.All, 0, 0, 0)
        }
    } else {
        BelBlau = 0
        BelGruen = 0
        BelRot = 16
        SchrittNummerLED = 1
        SchrittnummerGlobal = 1
        calliBot2.setRgbLed(C2RgbLed.All, 0, 0, 0)
        calliBot2.motorStop(C2Motor.beide, C2Stop.Bremsen)
        calliBot2.setLed(C2Motor.beide, false)
        if (Geschwindigkeit != GeschwindigkeitAlt) {
            GeschwindigkeitAlt = Geschwindigkeit
            if (Geschwindigkeit > 96) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    `)
            } else if (Geschwindigkeit > 92) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # .
                    `)
            } else if (Geschwindigkeit > 88) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # . .
                    `)
            } else if (Geschwindigkeit > 84) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    # # . . .
                    `)
            } else if (Geschwindigkeit > 80) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    # . . . .
                    `)
            } else if (Geschwindigkeit > 76) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # #
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 72) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # # .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 68) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # # . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 64) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # # . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 60) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    # . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 56) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # #
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 52) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # # .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 48) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # # . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 44) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # # . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 40) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    # . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 36) {
                basic.showLeds(`
                    # # # # #
                    # # # # #
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 32) {
                basic.showLeds(`
                    # # # # #
                    # # # # .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 28) {
                basic.showLeds(`
                    # # # # #
                    # # # . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 24) {
                basic.showLeds(`
                    # # # # #
                    # # . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 20) {
                basic.showLeds(`
                    # # # # #
                    # . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 16) {
                basic.showLeds(`
                    # # # # #
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 12) {
                basic.showLeds(`
                    # # # # .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 8) {
                basic.showLeds(`
                    # # # . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 4) {
                basic.showLeds(`
                    # # . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else if (Geschwindigkeit > 0) {
                basic.showLeds(`
                    # . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            } else {
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            }
        }
    }
}
// Ultraschall
function Programm2 () {
    if (SchrittnummerGlobal == 1) {
        if (Start == 1) {
            SchrittnummerGlobal = 10
            GeschwindigkeitUS = 40
        }
    } else if (SchrittnummerGlobal == 10) {
        if (Entfernung < 5) {
            SchrittnummerGlobal = 50
        } else if (Entfernung < 10) {
            SchrittnummerGlobal = 60
        } else if (Entfernung < 15) {
            SchrittnummerGlobal = 20
        } else if (Entfernung > 25) {
            SchrittnummerGlobal = 40
            SuchZeit = 100
        } else if (Entfernung > 20) {
            SchrittnummerGlobal = 30
        } else if (SchrittNeu) {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, GeschwindigkeitUS)
            calliBot2.setLed(C2Motor.beide, true)
        }
    } else if (SchrittnummerGlobal == 20) {
        GeschwindigkeitUS = GeschwindigkeitUS - 4
        if (GeschwindigkeitUS < 40) {
            GeschwindigkeitUS = 40
        }
        calliBot2.setLed(C2Motor.links, false)
        calliBot2.setLed(C2Motor.rechts, true)
        calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, GeschwindigkeitUS)
        ZeitPause = 200
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    } else if (SchrittnummerGlobal == 21) {
        if (IstZeitPause >= ZeitPause) {
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 30) {
        GeschwindigkeitUS = GeschwindigkeitUS + 4
        if (GeschwindigkeitUS > 100) {
            GeschwindigkeitUS = 100
        }
        calliBot2.setLed(C2Motor.links, true)
        calliBot2.setLed(C2Motor.rechts, false)
        calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, GeschwindigkeitUS)
        ZeitPause = 200
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    } else if (SchrittnummerGlobal == 31) {
        if (IstZeitPause >= ZeitPause) {
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 40) {
        calliBot2.setLed(C2Motor.beide, false)
        calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, 40)
        calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, 40)
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    } else if (SchrittnummerGlobal == 41) {
        if (Entfernung < 25) {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, GeschwindigkeitUS)
            SchrittnummerGlobal = 10
        }
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motor(C2Motor.links, C2Dir.rueckwaerts, 40)
            calliBot2.motor(C2Motor.rechts, C2Dir.vorwaerts, 40)
            SchrittnummerGlobal = 42
            SuchZeit = SuchZeit + SuchZeit
            if (SuchZeit > 2000) {
                SuchZeit = 2000
            }
            ZeitPause = SuchZeit
            StartZeitPause = ZeitAktuell
        }
    } else if (SchrittnummerGlobal == 42) {
        if (Entfernung < 25) {
            calliBot2.motor(C2Motor.beide, C2Dir.vorwaerts, GeschwindigkeitUS)
            SchrittnummerGlobal = 10
        }
        if (IstZeitPause >= ZeitPause) {
            calliBot2.motor(C2Motor.links, C2Dir.vorwaerts, 40)
            calliBot2.motor(C2Motor.rechts, C2Dir.rueckwaerts, 40)
            SchrittnummerGlobal = 41
            SuchZeit = SuchZeit + SuchZeit
            if (SuchZeit > 2000) {
                SuchZeit = 2000
            }
            ZeitPause = SuchZeit
            StartZeitPause = ZeitAktuell
        }
    } else if (SchrittnummerGlobal == 50) {
        calliBot2.setLed(C2Motor.links, false)
        calliBot2.setLed(C2Motor.rechts, false)
        calliBot2.motor(C2Motor.beide, C2Dir.rueckwaerts, 40)
        SchrittnummerGlobal = 51
    } else if (SchrittnummerGlobal == 51) {
        if (Entfernung > 8) {
            SchrittnummerGlobal = 10
        }
    } else if (SchrittnummerGlobal == 60) {
        calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
        calliBot2.setLed(C2Motor.beide, false)
        SchrittnummerGlobal = 61
    } else if (SchrittnummerGlobal == 61) {
        if (Entfernung > 11 || Entfernung < 5) {
            SchrittnummerGlobal = 10
        }
    } else {
        Start = 0
        SchrittnummerGlobal = 1
    }
}
input.onPinTouchEvent(TouchPin.P3, input.buttonEventDown(), function () {
    Geschwindigkeit = Geschwindigkeit + 4
    if (Geschwindigkeit > 100) {
        Geschwindigkeit = 100
    }
})
let SchrittnummerGlobalAlt = 0
let Entf1 = 0
let Entf2 = 0
let Entf3 = 0
let Entfernung = 0
let GeschwindigkeitUS = 0
let BelDauer = 0
let BelBlau = 0
let BelGruen = 0
let BelRot = 0
let ZeitBelWechsel = 0
let SchrittNummerLED = 0
let SuchZeit = 0
let IstZeitPause = 0
let ZeitAktuell = 0
let StartZeitPause = 0
let ZeitPause = 0
let Geschwindigkeit = 0
let SchrittNeu = 0
let GeschwindigkeitAlt = 0
let SchrittnummerGlobal = 0
let Programm = 0
let Start = 0
let BelWechsel = 0
BelWechsel = 100
basic.forever(function () {
    ZeitAktuell = control.millis()
    BelDauer = ZeitAktuell - ZeitBelWechsel
    IstZeitPause = ZeitAktuell - StartZeitPause
    Entf3 = Entf2
    Entf2 = Entf1
    Entf1 = calliBot2.entfernung(C2Einheit.cm)
    Entfernung = (Entf1 + Entf2 + Entf3) / 3
    if (SchrittnummerGlobal == 0) {
        calliBot2.motorStop(C2Motor.beide, C2Stop.Bremsen)
        Geschwindigkeit = 40
        Programm = 1
        basic.setLedColor(0xff0000)
        basic.showString("ON")
        SchrittnummerGlobal = 1
    }
    if (Programm == 1) {
        Programm1()
    } else if (Programm == 2) {
        Programm2()
    } else if (Programm == 3) {
        Programm3()
    } else if (Programm == 4) {
        Programm4()
    } else {
        basic.showIcon(IconNames.Confused)
        basic.setLedColor(0xff8000)
        Start = 0
        SchrittnummerGlobal = 1
        calliBot2.setLed(C2Motor.beide, false)
        calliBot2.motorStop(C2Motor.beide, C2Stop.Frei)
    }
    SchrittNeu = 0
    if (SchrittnummerGlobal != SchrittnummerGlobalAlt) {
        SchrittNeu = 1
    }
    SchrittnummerGlobalAlt = SchrittnummerGlobal
    LEDAnsteuerung()
})
