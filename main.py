def on_button_a():
    global Start, Programm, SchrittnummerGlobal, GeschwindigkeitAlt
    Start = 0
    basic.set_led_color(0xff0000)
    Programm = Programm + 1
    SchrittnummerGlobal = 1
    GeschwindigkeitAlt = -1
    if Programm > 4:
        Programm = 1
    AnzeigeProgramm()
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

# Stossstange
def Programm1():
    global SchrittnummerGlobal, ZeitPause, StartZeitPause, Start
    if SchrittnummerGlobal == 1:
        if Start == 1:
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 10:
        if calliBot2.read_bumper_sensor(C2Sensor.RECHTS, C2State.AN) and calliBot2.read_bumper_sensor(C2Sensor.LINKS, C2State.AN):
            SchrittnummerGlobal = 20
        elif calliBot2.read_bumper_sensor(C2Sensor.RECHTS, C2State.AN):
            SchrittnummerGlobal = 30
        elif calliBot2.read_bumper_sensor(C2Sensor.LINKS, C2State.AN):
            SchrittnummerGlobal = 40
        elif SchrittNeu:
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, Geschwindigkeit)
            calliBot2.set_led(C2Motor.BEIDE, False)
    elif SchrittnummerGlobal == 20:
        calliBot2.set_led(C2Motor.BEIDE, True)
        calliBot2.motor(C2Motor.BEIDE, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 500
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    elif SchrittnummerGlobal == 21:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, Geschwindigkeit)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, Geschwindigkeit)
            ZeitPause = 400
            StartZeitPause = ZeitAktuell
            SchrittnummerGlobal = 22
    elif SchrittnummerGlobal == 22:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 30:
        calliBot2.set_led(C2Motor.LINKS, False)
        calliBot2.set_led(C2Motor.RECHTS, True)
        calliBot2.motor_stop(C2Motor.RECHTS, C2Stop.BREMSEN)
        calliBot2.motor(C2Motor.LINKS, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    elif SchrittnummerGlobal == 31:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 40:
        calliBot2.set_led(C2Motor.RECHTS, False)
        calliBot2.set_led(C2Motor.LINKS, True)
        calliBot2.motor_stop(C2Motor.LINKS, C2Stop.BREMSEN)
        calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    elif SchrittnummerGlobal == 41:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    else:
        Start = 0
        SchrittnummerGlobal = 1

def on_button_b():
    global Start, GeschwindigkeitAlt
    if Start == 0:
        Start = 1
        basic.set_led_color(0x00ff00)
        AnzeigeProgramm()
    else:
        basic.set_led_color(0xff0000)
        Start = 0
        GeschwindigkeitAlt = -1
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

# Fahren auf dunkler Linie
def Programm4():
    global SchrittnummerGlobal, ZeitPause, StartZeitPause, SuchZeit, Start
    if SchrittnummerGlobal == 1:
        if Start == 1:
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 10:
        if calliBot2.read_line_sensor(C2Sensor.RECHTS, C2SensorStatus.HELL) and calliBot2.read_line_sensor(C2Sensor.LINKS, C2SensorStatus.HELL):
            SchrittnummerGlobal = 20
        elif calliBot2.read_line_sensor(C2Sensor.RECHTS, C2SensorStatus.HELL):
            SchrittnummerGlobal = 30
        elif calliBot2.read_line_sensor(C2Sensor.LINKS, C2SensorStatus.HELL):
            SchrittnummerGlobal = 40
        elif SchrittNeu:
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, Geschwindigkeit)
            calliBot2.set_led(C2Motor.BEIDE, False)
    elif SchrittnummerGlobal == 20:
        calliBot2.set_led(C2Motor.BEIDE, True)
        calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, Geschwindigkeit)
        calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    elif SchrittnummerGlobal == 21:
        if calliBot2.read_line_sensor(C2Sensor.RECHTS, C2SensorStatus.DUNKEL) and calliBot2.read_line_sensor(C2Sensor.LINKS, C2SensorStatus.DUNKEL):
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, Geschwindigkeit)
            SchrittnummerGlobal = 10
        if IstZeitPause >= ZeitPause:
            SchrittnummerGlobal = 22
            SuchZeit = SuchZeit + SuchZeit
        if SuchZeit > 2000:
            SuchZeit = 2000
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        calliBot2.motor(C2Motor.BEIDE, C2Dir.RUECKWAERTS, 40)
    elif SchrittnummerGlobal == 22:
        if calliBot2.read_line_sensor(C2Sensor.RECHTS, C2SensorStatus.DUNKEL) and calliBot2.read_line_sensor(C2Sensor.LINKS, C2SensorStatus.DUNKEL):
            calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, Geschwindigkeit)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.VORWAERTS, Geschwindigkeit)
            SchrittnummerGlobal = 10
        if IstZeitPause >= ZeitPause:
            SchrittnummerGlobal = 21
            SuchZeit = SuchZeit + SuchZeit
        if SuchZeit > 2000:
            SuchZeit = 2000
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, Geschwindigkeit)
        calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, Geschwindigkeit)
    elif SchrittnummerGlobal == 30:
        calliBot2.set_led(C2Motor.LINKS, False)
        calliBot2.set_led(C2Motor.RECHTS, True)
        calliBot2.motor_stop(C2Motor.RECHTS, C2Stop.BREMSEN)
        calliBot2.motor(C2Motor.LINKS, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    elif SchrittnummerGlobal == 31:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 40:
        calliBot2.set_led(C2Motor.RECHTS, False)
        calliBot2.set_led(C2Motor.LINKS, True)
        calliBot2.motor_stop(C2Motor.LINKS, C2Stop.BREMSEN)
        calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    elif SchrittnummerGlobal == 41:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    else:
        Start = 0
        SchrittnummerGlobal = 1

def on_pin_touch_p0():
    global Geschwindigkeit
    Geschwindigkeit = Geschwindigkeit - 4
    if Geschwindigkeit < 0:
        Geschwindigkeit = 0
input.on_pin_touch_event(TouchPin.P0, input.button_event_down(), on_pin_touch_p0)

def AnzeigeProgramm():
    if Programm == 1:
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . # # # .
                        # # # # #
                        # # . # #
        """)
    elif Programm == 2:
        basic.show_leds("""
            # # . . .
                        . . . . .
                        # . . # #
                        # . # # #
                        # . . # #
        """)
    elif Programm == 3:
        basic.show_leds("""
            # # # . .
                        . . . . .
                        . # # # .
                        # . . . #
                        . # # # .
        """)
    elif Programm == 4:
        basic.show_leds("""
            # # # # .
                        . . . . .
                        . . # # .
                        # # . . #
                        . . . # .
        """)
# Fahren bis dunkle Linie
def Programm3():
    global SchrittnummerGlobal, ZeitPause, StartZeitPause, Start
    if SchrittnummerGlobal == 1:
        if Start == 1:
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 10:
        if calliBot2.read_line_sensor(C2Sensor.RECHTS, C2SensorStatus.DUNKEL) and calliBot2.read_line_sensor(C2Sensor.LINKS, C2SensorStatus.DUNKEL):
            SchrittnummerGlobal = 20
        elif calliBot2.read_line_sensor(C2Sensor.RECHTS, C2SensorStatus.DUNKEL):
            SchrittnummerGlobal = 30
        elif calliBot2.read_line_sensor(C2Sensor.LINKS, C2SensorStatus.DUNKEL):
            SchrittnummerGlobal = 40
        elif SchrittNeu:
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, Geschwindigkeit)
            calliBot2.set_led(C2Motor.BEIDE, False)
    elif SchrittnummerGlobal == 20:
        calliBot2.set_led(C2Motor.BEIDE, True)
        calliBot2.motor(C2Motor.BEIDE, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 500
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    elif SchrittnummerGlobal == 21:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, Geschwindigkeit)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, Geschwindigkeit)
            ZeitPause = 400
            StartZeitPause = ZeitAktuell
            SchrittnummerGlobal = 22
    elif SchrittnummerGlobal == 22:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 30:
        calliBot2.set_led(C2Motor.LINKS, False)
        calliBot2.set_led(C2Motor.RECHTS, True)
        calliBot2.motor_stop(C2Motor.RECHTS, C2Stop.BREMSEN)
        calliBot2.motor(C2Motor.LINKS, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    elif SchrittnummerGlobal == 31:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 40:
        calliBot2.set_led(C2Motor.RECHTS, False)
        calliBot2.set_led(C2Motor.LINKS, True)
        calliBot2.motor_stop(C2Motor.LINKS, C2Stop.BREMSEN)
        calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, Geschwindigkeit)
        ZeitPause = 300
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    elif SchrittnummerGlobal == 41:
        if IstZeitPause >= ZeitPause:
            calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
            SchrittnummerGlobal = 10
    else:
        Start = 0
        SchrittnummerGlobal = 1
def LEDAnsteuerung():
    global SchrittNummerLED, ZeitBelWechsel, BelBlau, BelGruen, BelRot, SchrittnummerGlobal, GeschwindigkeitAlt
    if Start == 1:
        if SchrittNummerLED == 1:
            SchrittNummerLED = 2
            ZeitBelWechsel = control.millis()
            calliBot2.set_rgb_led(C2RgbLed.LV, BelRot, BelGruen, BelBlau)
            calliBot2.set_rgb_led(C2RgbLed.LH, 0, 0, 0)
        elif SchrittNummerLED == 2:
            if BelDauer >= BelWechsel:
                SchrittNummerLED = 3
                ZeitBelWechsel = ZeitAktuell
                calliBot2.set_rgb_led(C2RgbLed.LV, 0, 0, 0)
                calliBot2.set_rgb_led(C2RgbLed.RV, BelRot, BelGruen, BelBlau)
        elif SchrittNummerLED == 3:
            if BelDauer >= BelWechsel:
                SchrittNummerLED = 4
                ZeitBelWechsel = ZeitAktuell
                calliBot2.set_rgb_led(C2RgbLed.RV, 0, 0, 0)
                calliBot2.set_rgb_led(C2RgbLed.RH, BelRot, BelGruen, BelBlau)
        elif SchrittNummerLED == 4:
            if BelDauer >= BelWechsel:
                SchrittNummerLED = 5
                ZeitBelWechsel = ZeitAktuell
                calliBot2.set_rgb_led(C2RgbLed.RH, 0, 0, 0)
                calliBot2.set_rgb_led(C2RgbLed.LH, BelRot, BelGruen, BelBlau)
        elif SchrittNummerLED == 5:
            if BelDauer >= BelWechsel:
                SchrittNummerLED = 1
                ZeitBelWechsel = ZeitAktuell
                if BelRot > 0:
                    BelBlau = 0
                    BelGruen = 16
                    BelRot = 0
                elif BelGruen > 0:
                    BelBlau = 16
                    BelGruen = 0
                    BelRot = 0
                elif BelBlau > 0:
                    BelBlau = 0
                    BelGruen = 0
                    BelRot = 16
        else:
            calliBot2.set_rgb_led(C2RgbLed.ALL, 0, 0, 0)
    else:
        BelBlau = 0
        BelGruen = 0
        BelRot = 16
        SchrittNummerLED = 1
        SchrittnummerGlobal = 1
        calliBot2.set_rgb_led(C2RgbLed.ALL, 0, 0, 0)
        calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
        calliBot2.set_led(C2Motor.BEIDE, False)
        if Geschwindigkeit != GeschwindigkeitAlt:
            GeschwindigkeitAlt = Geschwindigkeit
            if Geschwindigkeit > 96:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                """)
            elif Geschwindigkeit > 92:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # .
                """)
            elif Geschwindigkeit > 88:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # . .
                """)
            elif Geschwindigkeit > 84:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # # . . .
                """)
            elif Geschwindigkeit > 80:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        # . . . .
                """)
            elif Geschwindigkeit > 76:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # #
                                        . . . . .
                """)
            elif Geschwindigkeit > 72:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # # .
                                        . . . . .
                """)
            elif Geschwindigkeit > 68:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # # . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 64:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # # . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 60:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        # . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 56:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # #
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 52:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # # .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 48:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # # . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 44:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # # . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 40:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        # . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 36:
                basic.show_leds("""
                    # # # # #
                                        # # # # #
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 32:
                basic.show_leds("""
                    # # # # #
                                        # # # # .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 28:
                basic.show_leds("""
                    # # # # #
                                        # # # . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 24:
                basic.show_leds("""
                    # # # # #
                                        # # . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 20:
                basic.show_leds("""
                    # # # # #
                                        # . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 16:
                basic.show_leds("""
                    # # # # #
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 12:
                basic.show_leds("""
                    # # # # .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 8:
                basic.show_leds("""
                    # # # . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 4:
                basic.show_leds("""
                    # # . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            elif Geschwindigkeit > 0:
                basic.show_leds("""
                    # . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
            else:
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
# Ultraschall
def Programm2():
    global SchrittnummerGlobal, GeschwindigkeitUS, SuchZeit, ZeitPause, StartZeitPause, Start
    if SchrittnummerGlobal == 1:
        if Start == 1:
            SchrittnummerGlobal = 10
            GeschwindigkeitUS = 40
    elif SchrittnummerGlobal == 10:
        if Entfernung < 5:
            SchrittnummerGlobal = 50
        elif Entfernung < 10:
            SchrittnummerGlobal = 60
        elif Entfernung < 15:
            SchrittnummerGlobal = 20
        elif Entfernung > 25:
            SchrittnummerGlobal = 40
            SuchZeit = 100
        elif Entfernung > 20:
            SchrittnummerGlobal = 30
        elif SchrittNeu:
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, GeschwindigkeitUS)
            calliBot2.set_led(C2Motor.BEIDE, True)
    elif SchrittnummerGlobal == 20:
        GeschwindigkeitUS = GeschwindigkeitUS - 4
        if GeschwindigkeitUS < 40:
            GeschwindigkeitUS = 40
        calliBot2.set_led(C2Motor.LINKS, False)
        calliBot2.set_led(C2Motor.RECHTS, True)
        calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, GeschwindigkeitUS)
        ZeitPause = 200
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 21
    elif SchrittnummerGlobal == 21:
        if IstZeitPause >= ZeitPause:
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 30:
        GeschwindigkeitUS = GeschwindigkeitUS + 4
        if GeschwindigkeitUS > 100:
            GeschwindigkeitUS = 100
        calliBot2.set_led(C2Motor.LINKS, True)
        calliBot2.set_led(C2Motor.RECHTS, False)
        calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, GeschwindigkeitUS)
        ZeitPause = 200
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 31
    elif SchrittnummerGlobal == 31:
        if IstZeitPause >= ZeitPause:
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 40:
        calliBot2.set_led(C2Motor.BEIDE, False)
        calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, 40)
        calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, 40)
        ZeitPause = SuchZeit
        StartZeitPause = ZeitAktuell
        SchrittnummerGlobal = 41
    elif SchrittnummerGlobal == 41:
        if Entfernung < 25:
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, GeschwindigkeitUS)
            SchrittnummerGlobal = 10
        if IstZeitPause >= ZeitPause:
            calliBot2.motor(C2Motor.LINKS, C2Dir.RUECKWAERTS, 40)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.VORWAERTS, 40)
            SchrittnummerGlobal = 42
            SuchZeit = SuchZeit + SuchZeit
            if SuchZeit > 2000:
                SuchZeit = 2000
            ZeitPause = SuchZeit
            StartZeitPause = ZeitAktuell
    elif SchrittnummerGlobal == 42:
        if Entfernung < 25:
            calliBot2.motor(C2Motor.BEIDE, C2Dir.VORWAERTS, GeschwindigkeitUS)
            SchrittnummerGlobal = 10
        if IstZeitPause >= ZeitPause:
            calliBot2.motor(C2Motor.LINKS, C2Dir.VORWAERTS, 40)
            calliBot2.motor(C2Motor.RECHTS, C2Dir.RUECKWAERTS, 40)
            SchrittnummerGlobal = 41
            SuchZeit = SuchZeit + SuchZeit
            if SuchZeit > 2000:
                SuchZeit = 2000
            ZeitPause = SuchZeit
            StartZeitPause = ZeitAktuell
    elif SchrittnummerGlobal == 50:
        calliBot2.set_led(C2Motor.LINKS, False)
        calliBot2.set_led(C2Motor.RECHTS, False)
        calliBot2.motor(C2Motor.BEIDE, C2Dir.RUECKWAERTS, 40)
        SchrittnummerGlobal = 51
    elif SchrittnummerGlobal == 51:
        if Entfernung > 8:
            SchrittnummerGlobal = 10
    elif SchrittnummerGlobal == 60:
        calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
        calliBot2.set_led(C2Motor.BEIDE, False)
        SchrittnummerGlobal = 61
    elif SchrittnummerGlobal == 61:
        if Entfernung > 11 or Entfernung < 5:
            SchrittnummerGlobal = 10
    else:
        Start = 0
        SchrittnummerGlobal = 1

def on_pin_touch_p3():
    global Geschwindigkeit
    Geschwindigkeit = Geschwindigkeit + 4
    if Geschwindigkeit > 100:
        Geschwindigkeit = 100
input.on_pin_touch_event(TouchPin.P3, input.button_event_down(), on_pin_touch_p3)

SchrittnummerGlobalAlt = 0
Entf1 = 0
Entf2 = 0
Entf3 = 0
Entfernung = 0
GeschwindigkeitUS = 0
BelDauer = 0
BelBlau = 0
BelGruen = 0
BelRot = 0
ZeitBelWechsel = 0
SchrittNummerLED = 0
SuchZeit = 0
IstZeitPause = 0
ZeitAktuell = 0
StartZeitPause = 0
ZeitPause = 0
Geschwindigkeit = 0
SchrittNeu = 0
GeschwindigkeitAlt = 0
SchrittnummerGlobal = 0
Programm = 0
Start = 0
BelWechsel = 0
BelWechsel = 100

def on_forever():
    global ZeitAktuell, BelDauer, IstZeitPause, Entf3, Entf2, Entf1, Entfernung, Geschwindigkeit, Programm, SchrittnummerGlobal, Start, SchrittNeu, SchrittnummerGlobalAlt
    ZeitAktuell = control.millis()
    BelDauer = ZeitAktuell - ZeitBelWechsel
    IstZeitPause = ZeitAktuell - StartZeitPause
    Entf3 = Entf2
    Entf2 = Entf1
    Entf1 = calliBot2.entfernung(C2Einheit.CM)
    Entfernung = (Entf1 + Entf2 + Entf3) / 3
    if SchrittnummerGlobal == 0:
        calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.BREMSEN)
        Geschwindigkeit = 40
        Programm = 1
        basic.set_led_color(0xff0000)
        basic.show_string("ON")
        SchrittnummerGlobal = 1
    if Programm == 1:
        Programm1()
    elif Programm == 2:
        Programm2()
    elif Programm == 3:
        Programm3()
    elif Programm == 4:
        Programm4()
    else:
        basic.show_icon(IconNames.CONFUSED)
        basic.set_led_color(0xff8000)
        Start = 0
        SchrittnummerGlobal = 1
        calliBot2.set_led(C2Motor.BEIDE, False)
        calliBot2.motor_stop(C2Motor.BEIDE, C2Stop.FREI)
    SchrittNeu = 0
    if SchrittnummerGlobal != SchrittnummerGlobalAlt:
        SchrittNeu = 1
    SchrittnummerGlobalAlt = SchrittnummerGlobal
    LEDAnsteuerung()
basic.forever(on_forever)
