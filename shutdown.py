# ========================================= # Makers! Add your own voice commands here. # =========================================
actor.add_keyword(_('shut down'), SpeakShellCommandOutput(say, "sudo shutdown -h now",_('Shutdown failed')))
actor.add_keyword(_('reboot'), SpeakShellCommandOutput(say,"sudo shutdown -r now",_('Reboot failed')))