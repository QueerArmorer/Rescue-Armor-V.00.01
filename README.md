# Rescue-Armor-V.00.01

 , __                              ___,                              
/|/  \                            /   |                              
 |___/  _   ,   __          _    |    |   ,_    _  _  _    __   ,_   
 | \   |/  / \_/    |   |  |/    |    |  /  |  / |/ |/ |  /  \_/  |  
 |  \_/|__/ \/ \___/ \_/|_/|__/   \__/\_/   |_/  |  |  |_/\__/    |_/
                                                                                  

Welcome to Rescue Armor! The name is a geeky reference to the original intention of this project:

The "Rescue Armor" in Iron Man is a suit of armor made for Pepper Potts. In the MCU, the Rescue Armor set was specifically designed to have a lot of the fighting capabilities of the iron man suit but it was designed (and redesigned) so that someone who didn't know or do a lot of advanced technical things could operate it.
That's our goal here. We want to make a suite of tools that, when set up and implemented at the end, could be installed by someone with minimal information security experience and be used to spot bad actors.
Our short term goal is thinking this is for someone who will be monitoring a team and setting up a team's computers for them, with teams and friendgroups being interchangable in this instance.
Our long term goal is this should be plug and play on any Windows system and it just works, with variants for Mac and Linux coming.

It is VERY MUCH still early and coming together. At the moment you have to run the USB set up first, then the setup python script which will run the entire folder of setup scripts. Then there's a python script to run the individual modules all as a group. EVENTUALLY this is going to be an executable but we are running down the problems as scripts first before compiling.

Concept behind what this is supposed to be doing:

The "hash check" is designed to check and see if core files have been modified without permission by creating hashes of their known good counterparts and looking for changes. The "set up" should be run AFTER you have the software suites you want ready to go and installed. At the moment, there is a script to run for Windows updates. In the near future we'll write an additional script that allows for the hashes to be checked and frozen while updates and new software is installed before generating a new set of hashes.

The CPU check is relatively simple. It runs a blender reference in CPU only, stores the value, then runs it again when the user is away and checks for performance degredation. We're planning on adding a long term tracker that can see if there is a gradual decline indicating hardware heat death and reduce false positives. Largely checking for hidden mining software, although it'll also flag Meltdown and Spectre attacks that leave permanent ghosts.

The keylogger checking module makes a big set of words and then simulates pressing the keys for each one. It then makes a list that includes what it typed, every simple encryption method for what it typed, and checks the computer for what was typed. This way we don't have to look for specific installs or programs, we can just look for the logs themselves. The long term goal is to add an additional version that runs less often but is far more thorough in checking other file types.

The DNS checker is fairly simple, it's the kind of thing you would do if checking for DNS spoofing on your own machine but automated. It calls a couple "known" websites and checks the IP addresses they return against their fixed IPs.

The Hard Drive check is a simple performance check that creates a 200mb text file of War and Peace repeating over and over, cuts and pastes it, and records the time the action took before deleting the war and peace file. It then does this as a test against itself over and over.

We are not reinventing the wheel. Antivirus software, password managers, VPNs, ARP poison detection, and Root Kit Checkers exist, they're effective, we're going to automate installing and updating those rather than making new ones.

Long term goals:

Add additional modules based on development and feedback.
Refine all modules.
Create automated scripts for every piece of this so that none of it need to be dicussed
Create scripts that include education about best practice for how to use Recue Armor
Compile it as an executable
Refine and test based on feedback
Variant MacOS and Chrome, as well as a Linux Distro with Rescue Armor set up during install ... eventually.
