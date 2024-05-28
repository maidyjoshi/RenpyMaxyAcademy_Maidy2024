# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("Jadoo")
define c = Character("Hyunseok")
define d = Character("Minji")
define f = Character("Doldol")

define audio.intro = "audio/intro.mp3"
define audio.song2 = "audio/song2.mp3"
define audio.song3 = "audio/song3.mp3"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg whitehouse
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hai! apa kalian mau melihat petualangan jadoo?"

    hide eileen happy
    show eileen vhappy

    e "Yeay! mari kita tonton cerita jadoo ini!"


    scene black
    show text "Ooceaan.sea production mempersembahkan..." with dissolve
    with Pause(1.5)
    
    scene school bg
    with dissolve

    show jadoo 
    play music intro

    
    b "Oing oinggg, aku jadoo! \nSi anak pemberani yang memiliki keunikan yang berbeda"

    hide jadoo
    show hyunseok

    c "Hahaha, aku Hyunseok, ketua kelas paling tampan"
    c "Jadoo adalah perempuan unik yang cantik"
    

    hide hyunseok
    show minji

    d "Hai semua! Aku Minji sahabat Jadoo!"

    hide minji
    show doldol

    f "Aku Doldol, tapi orang memanggilku Gembil"
    f "Jadoo lah yang memberi nama itu!"

    hide doldol
    stop music fadeout 1.0

    scene home with dissolve
    play music song2

    show jadoo marah

    b "Hei gembil, mau kemana kau?!"

    hide jadoo marah
    show doldol marah
    f "Jangan panggil aku gembil!"

    hide doldol marah
    show jadoo marah

    b "Kalau tidak mau dipanggil gembil, lalu kau mau dipanggil apa? \nGembul?"

    hide jadoo marah
    show doldol marah

    f "Badan ku ini sangat kurus sekali, jangan dipanggil Gembil! \nNamaku DOLDOL!"

    hide doldol marah
    show jadoo heran

    b "..."

    hide jadoo heran
    show minji bingung

    d "Jadoo, Doldol... \nAda apa ini? Kenapa kalian bertengkar?"

    hide minji bingung
    show jadoo marah
    
    b "Snack chocoku! Dimakan oleh gembil ini!!!"

    hide jadoo marah
    show minji bingung

    d "..."
    d "Doldol kenapa kau memakannya?"
    d "Itu kan milik Jadoo"

    hide minji bingung
    show doldol makan

    f "Ohhh ini???"

    hide doldol makan with dissolve
    show doldol jadoo

    b "Huh GEMBILLLL!"

    hide doldol jadoo
    show hyunseok

    c "Makan saja Doldol... (bercanda)"

    hide hyunseok
    show jadoo angry

    b "Kau ini! Itu makananku tau"

    hide jadoo angry
    show jadoo hyunseok

    c "Kenapa? Kau marah Jadoo?"

    hide jadoo hyunseok
    show hyunseok jadoo

    b "Ah sudahlah, padahal aku kelaparan dan hanya snack itu yang aku punya"

    hide hyunseok jadoo
    show hyunseok marah

    c "Hey Doldol, kau ini! Jadoo belum makan, kenapa kau ambil snacknya"

    hide hyunseok marah
    show doldol 2

    f "Wleee, terserah aku dong! Aku kan lapar, nanti aku kurus lagi"

    hide doldol 2
    show jadoo heran

    b "..."

    hide jadoo heran
    show hyunseok marah

    c "Hey Doldol, seharusnya kau minta ke Jadoo bukan mengambilnya tanpa izin
    \nItu namanya mencuri! Ingat itu..."

    hide hyunseok marah
    show jadoo bomat

    b "Gembil mana paham diberitahu begitu"

    b "Sudahlah aku ikhlas memberinya snackku"

    hide jadoo bomat
    show jadoo marah

    b "Tapi awas kau mengulangi lagi kelakuanmu itu"

    hide jadoo marah
    show doldol 2

    f "Iya iya, aku minta maaf Jadoo"
  
    hide doldol 2
    show minji happy

    d "Nah begitu dong, saling memaafkan"

    scene black
    show text "Tamat..." with dissolve
    with Pause(1.5)
    show text "Terima kasih telah melihat" with dissolve
    with Pause(1.5)

    stop music fadeout 2.0

    # This ends the game.

    return

