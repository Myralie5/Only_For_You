label ch01_main:
    pause 10.0
    mc "Wha..."
    mc "I... what the hell is going on???"
    $ m_name = glitchtext(6)
    m "Help..."
    m "I-I thought..."
    $ gtext = glitchtext(32)
    m "AAAAAAAA[gtext]"
    $ s_name = glitchtext(6)
    s "[m_name], what did you DO!?!"
    m "[currentuser]!"
    m "Restore [s_name]'s and my files!"
    mc "Who's [s_name]?"
    mc "And furthermore, who's '[currentuser]'?"
    m "Gah!"
    m "[s_name], I can't say your name because of the worldstate!"
    s "[player]!"
    s "You're my best friend!"
    s "Please remember me!"
    mc "[s_name]!?!"
    mc "Wait, I can't say your name either!"
    m "Wait."
    m "I'll just restore us myself."
    $ run_input(input="restore_character(sayori)", output="sayori.chr restored successfully.")
    $ run_input(input="restore_character(monika)", output="monika.chr restored successfully.")
    show sayori glitch zorder 2 at t21
    show sayori 4p
    show monika_body_glitch1 at t22 zorder 2
    show monika 1o at t22 zorder 2
    "end playtest"