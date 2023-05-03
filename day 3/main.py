print('''               /\____/\    __
             .'  """"  `,-'  `--.__
        __,- :   -  -  ;  " ::     `-. -.__
     ,-sssss `._  `' _,'"     ,'~~~::`.sssss-.
    |ssssss ,' ,_`--'_    __,' ::  `  `.ssssss|
   |sssssss `-._____~ `,,'_______,---_;; ssssss|
    |ssssssssss     `--'~{__   ____   ,'ssssss|
     `-ssssssssssssssssss ~~~~~~~~~~~~ ssss.-'
          `---.sssssssssssssssssssss.---' 
''')

print("welcome to mr kitten house")
wake_up =input("do you wanna wake up mister kitten? (yes or no)\n")
wake_up.lower()
if wake_up == 'no':
    print('''               /\____/\    __
             .'  """"  `,-'  `--.__
        __,- :   -  -  ;  " ::     `-. -.__
     ,-sssss `._  `' _,'"     ,'~~~::`.sssss-.
    |ssssss ,' ,_`--'_    __,' ::  `  `.ssssss|
   |sssssss `-._____~ `,,'_______,---_;; ssssss|
    |ssssssssss     `--'~{__   ____   ,'ssssss|
     `-ssssssssssssssssss ~~~~~~~~~~~~ ssss.-'
          `---.sssssssssssssssssssss.---' 
mr kitten continues his nap peacefully(game over bud)''')
if wake_up =='yes':
    print('''
                               |        |
                               |\      /|
                               | \____/ |
                               |  /\/\  |
                              .'___  ___`.
                             /  \|/  \|/  )    (erm wtfrick dude, do u at least have food)
            _.--------------( ____ __ _____)
         .-' \  -. | | | | | \ ----\/---- /
       .'\  | | / \` | | | |  `.  -'`-  .'
      /`  ` ` '/ / \ | | | | \  `------'
     /-  `-------.' `-----.       -----. `---.
    (  / | | | |  )/ | | | )/ | | | | | ) | | )
     `._________.'_____,,,/\_______,,,,/_,,,,/  
     mr kitten wakes up and stares at u in disgust and asks u where the food is at\n''')
    food_location = input("where is the food?(box, kitchen, outside)").lower()
    if food_location == 'kitchen':
        print('''
                                _.---.
           meow       |\---/|  / ) ca|
          ------------;     |-/ /|foo|---
                      )     (' / `---'
          ===========(       ,'==========
          ||   _     |      |
          || o/ )    |      | o
          || ( (    /       ;
          ||  \ `._/       /
          ||   `._        /|
          ||      |\    _/||
        __||_____.' )  |__||____________
         ________\  |  |_________________
                  \ \  `-.
                   `-`---'  mr kitten finds the food yum yum(succses!)''')
    if food_location == 'box':
        print('''                                  ,
              ,-.       _,---._ __  / )
             /  )    .-'       `./ /   )
            (  (   ,'            `/    /|
             \  `-"             \'\   / |
              `.              ,  \ \ /  |
               /`.          ,'-`----Y   |
              (            ;        |   '
              |  ,-.    ,-'         |  /
              |  | (   |            | /
              )  |  \  `.___________|/
              `--'   `--'
              mr kitten opens the box and falls into what turns out to be an endless void, u check the box only to find it completly empty(game over bud)''')
    if food_location == 'outside':
        print('''
              

         *                  *
             __                *
          ,db'    *     *
         ,d8/       *        *    *
         888
         `db\       *     *
           `o`_                    **
      *               *   *    _      *
            *                 / )
         *    (\__/) *       ( (  *
       ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.
      | @|  ={      }= | @|  / / | @|o |
     _j__j__j_)     `-------/ /__j__j__j_
     ________(               /___________
      |  | @| \              || o|O | @|
      |o |  |,'\       ,   ,'"|  |  |  |  
     vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v
                _) )    `. \ /
               (__/       ) )
                         (_/ mr kitten stares into the night sky and realizes that he shouldve never have come here,
                         he walks toward the moon and never comes back(game over bud)
''')
