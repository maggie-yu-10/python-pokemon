![](https://github.com/maggie-yu-10/python-pokemon/blob/master/pokemon1.png?raw=true | width=100)
![](https://github.com/[username]/python-pokemon/blob/master/pokemon2.png?raw=true | width=100)

Name: Tianhe Xie and Maggie Yu
Pennkey: tianhex maggieyu
Hours Spent: 40


UPenn version of Pokemon battle

NOTE: In the CIS192 project demo, we said that we would be using Flask and Pillow to create a Pokemon battle simulator. After further consideration, we decided that the Tkinter GUI would be more effective and overall a better experience for the player. In addition, since this game does not have “Pokemon types” like the original Pokemon games (rather, we use original characters with no types), we decided to omit type effectiveness. Additional Pokemon statistics, such as Attack, Defense and Speed, were also omitted (If we were to implement all the characteristics of a Pokemon battle, this project would have taken 80+ hours to complete).



OVERVIEW: This game is a battle simulator adapted from the classic Pokemon games. 

In Pokemon battles, your party and your opponent’s party battle each other. The battle is 1 vs 1, and one member of your party will face off against a member of the opponent’s party. When a party member runs out of health and is no longer able to battle, the remaining available party members replace them. The game ends when one team is unable to battle (no available Pokemon).



HOW THE GAME WORKS:
Your party includes: CIS student, Tia, Maggie
Your opponent’s party includes: Amy Gutmann, Angry Squirrel, Goldman Sachs
You start with CIS student. PLEASE BE PATIENT when the program displays the attacks (There is a one second delay between your move and your opponent’s move). Make sure that the text “it’s your turn now” displays before clicking anything. Clicking randomly when the attack is still taking in place may cause the program to fail.

Your party and your opponent’s party take turns making moves, with your party going first. There are four types of moves to choose from: Attack, Bag, Party, and Flee. When performing an action, make sure to click to first click one of the four types of moves, then the sub-buttons (if any)!

Attack: There are four attacks for each fighter. Clicking on one of these attacks will deal damage to the opponent. Each move has different dmg (damage level).

Bag: Your bag has three items (Canada Goose Jacket, iPhone, and Wawa burrito). These items can be reused.

Party: You have the option to switch between available party members. Clicking on the “Party” button, will display all available party members (in other words, “fainted” members will not be displayed).

Flee: Attempting to flee from battle takes one turn.



RUNNING THE PROGRAM: This project uses Tkinter and Pillow. Tkinter comes pre-installed with the Python installer binaries for Mac OS X and the Windows platform. If you install Python from the official binaries for Mac OS X or Windows platform, you are good to go with Tkinter. To install Pillow, run 
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
In your terminal. 
To play, run game.py. Make sure you are in the correct directory!

Make sure all python and image files are in their correct locations.
When you unzip CIS192Pokemon.zip, you should have:

Python files 
game.py, helper.py, pokemon.py, move.py
Images
Intro.png, toobad.png, congrats.png, attackimagetemplate.png, party.png, flee.png, bag.png, attack.png
Folders
tia: internshipflex.png, aiattackpng, slytherinsnake.png, tiktok.png, tia.png, tiablvl.png, tiaw.png, tiab.png
party: tiaprofile.png, maggieprofile.png, cis studentprofile.png, partytemplate.png
squirrel: squirrel.png, squirrelb.png, squirrelblvl.png, squirrel
gs: gs.png, gsb.png, gsblvl.png
maggie: splurge.png, chillyphilly.png, teado.png, nintendoswitch.png, maggie.png, maggiew.png, maggieb.png, maggieblvl.png
amyg: amygblvl.png, amygw.png, amygb.png, amyg.png
bag: wawap.png, phonep.png, cgoosep.png, bagtemplate.png
you: cry.png, code.png, officehours.png, soylent.png, youblvl.png, youb.png, youw.png, you.png
backgrounds: plocust.png, pvanpelt.png, plove.png, phuntsman.png, bartemp1.png, ptampons.png
