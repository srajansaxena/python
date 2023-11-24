player = input("Enter Your Name\n")

print(f"Welcome to India {player}\n")

mark1 = input("Where do you want to go?\n\nDelhi or Chennai\n")
if mark1 == "Delhi":
    print("\nYou are in Delhi !!! ,stay alert O.o, even indians are not safe here.\n")
    mark2 = input("Now Where do you want to go next?\nJaipur or Aligarh?\n")

    if mark2 == "Jaipur":
        print("\nYou are in Jaipur, visit Hawa Mahal, City Palace and proceed to next destination.\n")
        markJ = input("Hope you had a good rest here.\nWhere do you want to go next?\nAhmedabad or Mathura?\n")

        if markJ == "Ahmedabad":
            print("\nSince you are here, visit Sabarmati Riverfront, Gandhi Ashram.\n However you took the wrong turn. Game Over for you.\n Calibrate your compass and may be try again. Thanks for playing this game.\n" )
        elif markJ == "Mathura":
            print("\nYou are in Mathura. Take a break and visit Temples and Hills around here.\n")
            markMat = input("Where do you want to go next?\nAgra or Firozabad?\n")

            if markMat == "Agra":
                taj=('''Congratulations! You are in the city of Taj Mahal, one of the seven wonders of the world. Enjoy!
                                				
                                                                                         :
                                                                                         :
                                                                                        / \
                                                                                     _;;;;;;;_
                                                                                  .-'         '-.                               .
                                                  .                              /               \\                              m
                                                  m                             /                 \\                            | |
                                                 | |                           |                   |                           |M|
                                                 |M|                           |    ___--'--___    |                           ---+
                                                 ---+       .               .:.\\__--  _______  --__/.:.               .        |  |
                                                 |  |       m              /   \\ -----       ----- /   \\              m        |  |
                                                 |  |      | |      :     /_____ __________________ ____\\     :      | |       |  |                            (
                                                 |  |      |n|      __:  | n n n|  ______________  |n n n|  ;__      |n|       |  |                          (::
                                                 ___|      | |      |n\\__|_M_M_M| | ____________ | |M_M_M|__/nn|     | |      |---|                      (:(::::
                                                 |   |     | |      |    |      | ||      _     || |     |     |     | |      |   |                     (:::::::
                                                 |   |     | |      | /\\ |  .-. | ||   .-" "-.  || | .-. |  /\\ |     |-|      |   |     ..  ...        (::::::::
                                                 |   |     |-|      ||  || /   \\| ||  '  -"-  ' || |/   \\| |  ||     | |      |   | ..............    (:::::::::
                                                 |   |     | |      |    | |   || || |  |   |  ||| ||   ||     |     | |      ----|.................(:::::::::::
                 ()                              ____|     | |      |    | +---+| || |  -----  ||| |+---+|     |     | |     |    | .................(::::::::::
                 :::)():(:)                      |    |    |_|      |    |  .-. | || |         ||| | .-. |     |     |-|     |    |..................(::::::::::
                 ::::):(:::)                     |    |    | |      | /\\ | /   \\| || |   ||    ||| |/   \\|  /\\ |     | |     |    | .................(::::::::::
                 :::::)::::::)   .  .            | (:():)()  |      ||  || |   || || |  ||||   ||| ||   || |  ||     | |     |    |  .................(:::::::::
                 ::::::):::::::)      . ::        (:(:))(:):)| -----============================================---- | | ----|    |   .................(::::::::
                 :::::):::::::::)      ::::::    (:(:):((:():)                                                      m            .,.   ...m
                 ::::::::::::::::)    ::::m:m   |     000          m m  m  M     ;;;                       M M  M   MMM          ...MM   MM    m
                 ::mmm::::::::mm:::). .::MM:MM  ------000---------MM MM MM MM--::::::-------------------M-MMMMMMMM--MMMm-M-MM------MMMM MMM   MMm        mm
                 MMMMMM::::::MMMM:). . . MMMMMMM      0 MM   .    MM MM MM MM             ==            M MMMMMMMM  MMMM M MMM    MMMMM MMMM  MMM       MMM
                 MMMMMMM:::::MMMMM      MMMMMMMM  MM .  MMM       MM MM MM       i i i  :F_P: i i.i         MMMMMM  MMMM M MMM    MMMMM MMMM  MMM       MMMM
                 MMMMMMM::::MMMMMMM     MMMMMMMMM MM    MMMM      MM M        .    //             \\    .         M  MMMM M MMM    MMMMM MMMM  MMM       MMMM
                 MMMMMMM:::MMMMMMMMM .  MMMMMMMMM MM  M  MMM      M               /                \\.      .          MM M MM  .  MMMMM MMMM  MMM       MMMM
                 MMMMMMMM::MMMMMMMMM    MMMMMMMMM MM  M MMMM              .'    ./                  '\\                     MM    'MMMMM MMMM  MMMM     MMMMM
                 MMMMMMMM::MMMMMMMMM   MMMMMMMMMM MM  M MMMM           .       //                     \\.         .                MMMMM MMMM .MMMM      MMMM
                 MMMMMMMM::MMMMMMMMM   MMMMMMMMM  MM                         ./'                       '\\                          MMM MMMM  MMMM' .   MMMM
                 MMMMMMMM:::MMMMMMMM   MMMMMMMM                    .        //                           '\\.           .                      MMMM    ' MMM
                 MMMMMMMMM::MMMMMMMM    MMMMMM                             //                              \\.                                MMMM       MMM ' .
                 MMMMMMMMM:: MMMMMMM   MMMMM                  .          //'                                '\\.            .                            MM
                 MMMMMMM:   MMMMMMM                                    .//                                    '\\
                 MMMMMMM    MMMMMM                       .            ///                                       '\\              .
                 MMMMMM                                              //'                                          \\.                 .
                 MMMMMMM                             .             .//                                             \\\.
                 MMMMMM                                           ///                                                \\\.                                                                                                                                         
                ''')
                print(taj)
            elif markMat == "Firozabad":
                print("\nYou were too close but took a wrong turn. Go to Nepal now you dumb person.\n")
            else:
                print("\nYou have mentioned the wrong city. GTFO of India.")
        else:
            print("\nYou have mentioned the wrong city. GTFO of India.")

    elif mark2 == "Aligarh":
        print("\nYou are in Aligarh.\nThe creator only knows AMU from here so may be visit that on the way to next place.\n")
        markAl = input("Where do you want to go next?\nLucknow or Mathura?\n")

        if markAl == "Lucknow":
            print("\nSince you are here, visit Imambara,Rumi Darwaza and other spots.\n However you took the wrong turn. Game Over for you.\n Calibrate your compass and may be try again. Thanks for playing this game\n")
        elif markAl == "Mathura":
            print("\nYou are in Mathura. Take a break and visit Temples and Hills around here.\n")
            markMat = input("Where do you want to go next?\nAgra or Firozabad?\n")

            if markMat == "Agra":
                taj=('''Congratulations! You are in the city of Taj Mahal, one of the seven wonders of the world. Enjoy!
                				
                                                                                         :
                                                                                         :
                                                                                        / \
                                                                                     _;;;;;;;_
                                                                                  .-'         '-.                               .
                                                  .                              /               \\                              m
                                                  m                             /                 \\                            | |
                                                 | |                           |                   |                           |M|
                                                 |M|                           |    ___--'--___    |                           ---+
                                                 ---+       .               .:.\\__--  _______  --__/.:.               .        |  |
                                                 |  |       m              /   \\ -----       ----- /   \\              m        |  |
                                                 |  |      | |      :     /_____ __________________ ____\\     :      | |       |  |                            (
                                                 |  |      |n|      __:  | n n n|  ______________  |n n n|  ;__      |n|       |  |                          (::
                                                 ___|      | |      |n\\__|_M_M_M| | ____________ | |M_M_M|__/nn|     | |      |---|                      (:(::::
                                                 |   |     | |      |    |      | ||      _     || |     |     |     | |      |   |                     (:::::::
                                                 |   |     | |      | /\\ |  .-. | ||   .-" "-.  || | .-. |  /\\ |     |-|      |   |     ..  ...        (::::::::
                                                 |   |     |-|      ||  || /   \\| ||  '  -"-  ' || |/   \\| |  ||     | |      |   | ..............    (:::::::::
                                                 |   |     | |      |    | |   || || |  |   |  ||| ||   ||     |     | |      ----|.................(:::::::::::
                 ()                              ____|     | |      |    | +---+| || |  -----  ||| |+---+|     |     | |     |    | .................(::::::::::
                 :::)():(:)                      |    |    |_|      |    |  .-. | || |         ||| | .-. |     |     |-|     |    |..................(::::::::::
                 ::::):(:::)                     |    |    | |      | /\\ | /   \\| || |   ||    ||| |/   \\|  /\\ |     | |     |    | .................(::::::::::
                 :::::)::::::)   .  .            | (:():)()  |      ||  || |   || || |  ||||   ||| ||   || |  ||     | |     |    |  .................(:::::::::
                 ::::::):::::::)      . ::        (:(:))(:):)| -----============================================---- | | ----|    |   .................(::::::::
                 :::::):::::::::)      ::::::    (:(:):((:():)                                                      m            .,.   ...m
                 ::::::::::::::::)    ::::m:m   |     000          m m  m  M     ;;;                       M M  M   MMM          ...MM   MM    m
                 ::mmm::::::::mm:::). .::MM:MM  ------000---------MM MM MM MM--::::::-------------------M-MMMMMMMM--MMMm-M-MM------MMMM MMM   MMm        mm
                 MMMMMM::::::MMMM:). . . MMMMMMM      0 MM   .    MM MM MM MM             ==            M MMMMMMMM  MMMM M MMM    MMMMM MMMM  MMM       MMM
                 MMMMMMM:::::MMMMM      MMMMMMMM  MM .  MMM       MM MM MM       i i i  :F_P: i i.i         MMMMMM  MMMM M MMM    MMMMM MMMM  MMM       MMMM
                 MMMMMMM::::MMMMMMM     MMMMMMMMM MM    MMMM      MM M        .    //             \\    .         M  MMMM M MMM    MMMMM MMMM  MMM       MMMM
                 MMMMMMM:::MMMMMMMMM .  MMMMMMMMM MM  M  MMM      M               /                \\.      .          MM M MM  .  MMMMM MMMM  MMM       MMMM
                 MMMMMMMM::MMMMMMMMM    MMMMMMMMM MM  M MMMM              .'    ./                  '\\                     MM    'MMMMM MMMM  MMMM     MMMMM
                 MMMMMMMM::MMMMMMMMM   MMMMMMMMMM MM  M MMMM           .       //                     \\.         .                MMMMM MMMM .MMMM      MMMM
                 MMMMMMMM::MMMMMMMMM   MMMMMMMMM  MM                         ./'                       '\\                          MMM MMMM  MMMM' .   MMMM
                 MMMMMMMM:::MMMMMMMM   MMMMMMMM                    .        //                           '\\.           .                      MMMM    ' MMM
                 MMMMMMMMM::MMMMMMMM    MMMMMM                             //                              \\.                                MMMM       MMM ' .
                 MMMMMMMMM:: MMMMMMM   MMMMM                  .          //'                                '\\.            .                            MM
                 MMMMMMM:   MMMMMMM                                    .//                                    '\\
                 MMMMMMM    MMMMMM                       .            ///                                       '\\              .
                 MMMMMM                                              //'                                          \\.                 .
                 MMMMMMM                             .             .//                                             \\\.
                 MMMMMM                                           ///                                                \\\.                                                                                                                                             
                ''')
                print(taj)

            elif markMat == "Firozabad":
                print("\nYou were too close but took a wrong turn. Go to Nepal.\n")
            else:
                print("\nYou have mentioned the wrong city. GTFO of India.\n")
        else:
            print("\nYou have mentioned the wrong city. GTFO of India.\n")

    else:
        print("\nYou have mentioned the wrong city. GTFO of India.\n")

elif mark1 == "Chennai":
    print(f"\nHi {player}! You went to South India. You should have booked through a better tour operator; the marble wonder is in the North. Try again.\n")
else:
    print("\nYou have mentioned the wrong city. GTFO of India.\n")
