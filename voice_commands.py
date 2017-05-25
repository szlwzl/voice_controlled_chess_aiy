# ========================================= # Makers! Add your own voice commands here. # =========================================
actor.add_keyword('light on', GpioWrite(26, True)) actor.add_keyword('lights on', GpioWrite(26, True))
actor.add_keyword('light off', GpioWrite(26, False)) actor.add_keyword('lights off', GpioWrite(26, False))