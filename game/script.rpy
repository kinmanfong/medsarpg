# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Pharmacist Aina")

# The game starts here.

label start:
    define stage = "start"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hsj:
        size (1920, 1080)

    play sound "bird.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lady:
        size (1280, 720)
        xalign 0.6
        yalign 0.6

    # These display lines of dialogue.

    e "Welcome to Pharmacy Department of Seberang Jaya Hospital!"
    e "I am Pharmacist Aina, and I will be guiding you through this Medication Safety module."

    show lady:
        size (1280, 720)
        xalign 1.23
        yalign 0.7
    with move

    e "Before we start, let us get to know each other first."


    python:
        name = renpy.input("How shall I address you?")
        name = name.strip()

    define char = Character("[name]")

    e "Nice to meet you, [name]!"
    e "Before we begin, here are a few tips for you for this e-Learning module."
    e "At any time during the course, you can access the {b}Menu{/b} option below, or using the {b}Esc{/b} key if you are on desktop."
    e "In the {b}Menu{/b}, you can {b}Save{/b} your progress at any point during the module..."
    e "...then you can {b}Load{/b} directly to that point anytime in the future."
    e "You can even change the speed of my text under {b}Preferences{/b}. Do explore around!"
    e "Are you ready to learn about Medication Safety? If yes, let's start!"

    play sound farmasiopd

    hide lady
    with moveoutright       


    scene bg farmasi1:
        size (1920, 1080)
    with fade

    show lady:
       size (1280, 720)
       xalign 1.23
       yalign 0.7
    with moveinright


    e "Welcome to our pharmacy department."
    e "Everyday, a lot of our tasks as healthcare professionals revolves around medication and its uses."
    e  "So, knowing about Medication Safety is one of our core responsibility." 

    hide lady
    with moveoutright       

    show lady2:
       size (1280, 720)
       xalign -0.5
       yalign 0.7
    with moveinleft

    show p1:
       size (700, 800)
       xalign 0.7
       yalign 0.0
    with moveinright

    e "According to Malaysian Patient Safety Goals (MPSG) 2.0..."
    
    hide p1
    with moveoutright       
  
    show p2:
       size (1177, 858)
       xalign 0.8
       yalign 0.0
    with moveinright

    e "...one of the goals is to have ZERO cases of medication error leading to severe harm or death."
    
    show arrow:
       size (400, 400)
       xalign 0.75    
       yalign 0.2
    with moveinright
    e "...one of the goals is to have ZERO cases of medication error leading to severe harm or death.{fast}"    

    hide p2
    hide arrow
    with moveoutright

    e "So, what is a Medication Error?"
    e "Medication Error can be defined into two types, {b}'Actual Medication Error'{/b}, and {b}'Near Miss Medication Error'{/b}."
    
    show p3:
       size (1450, 350)
       xalign 0.85
       yalign 0.3
    with moveinright

    e "An {b}Actual Medication Error{/b} is when an error reached the patient."
    e "Similarly, if the patient detected the error, it is also considered an {b}Actual Medication Error{/b}."

    hide p3
    with moveoutright

    show p4:
        size(1450, 350)
        xalign 0.85
        yalign 0.3
    with moveinright

    e "On the other hand, a {b}Near Miss Medication Error{/b} are errors which did NOT reach the patient."
    e "Even if it was detected by healthcare personnel, as long as BEFORE it reaches the patient, it is a {b}'Near Miss'{/b}."

    hide p4
    with moveoutright
    hide lady2
    with moveoutleft

    show lady3:
       size (850, 850)
       xalign 1.0
       yalign 0.7
    with moveinright

    e "Let's have a short quiz."   
    e "According to Malaysian Patient Safety Goals (MPSG) 2.0, one of the goals is to have ZERO cases of medication error leading to severe harm or death."

    menu:
        with dissolve
        e "TRUE or FALSE?"
        "True":
            jump choice1_yes

        "False":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        play sound "correct.mp3"
        e "Correct! Seems like you are paying attention."

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        play sound "wrong.mp3"
        e "Well, it's okay to be wrong, but the correct answer is True."

        jump choice1_done

    label choice1_done:

    e "Let us continue our module."
    
    play sound "step.mp3"
    hide lady3
    with moveoutright       

    scene bg farmasi2:
        size (1920, 1080)
    with fade

    show lady2:
       size (1280, 720)
       xalign -0.5
       yalign 0.8
    with moveinleft

    show p5:
        size(1300,800)
        xalign 0.8
        yalign 0.025
    with moveinright

    e "Medication Error can happen at any stage."
    e "Thus, Medication Safety is everyone's responsibility."
    e "So, what are the strategies that we, as healthcare professionals can use to prevent Medication Error?"
    e "One simple method is by practicing the 5R of Medication Safety."

    hide p5
    with moveoutright

    show p6:
        size(529,839)
        xalign 0.65
        yalign 0.025
    with moveinright

    e "In pharmacy, we call this the 5R, or 5B."

    show p6:
        xalign 1.0
        yalign 0.025
    with move

    label menu2:
        menu:
            with dissolve
            e "Which would you like to know more about?"
            "Right Patient":
                jump op1

            "Right Drug":
                jump op2
            
            "Right Dose":
                jump op3

            "Right Route":
                jump op4
            
            "Right Time":
                jump op5

            "{i}{b}(Skip){/b}{/i}":
                jump done1

        label op1:
            show rightptn:
                size (564,573)
                xalign 0.5
                yalign 0.3
            with moveintop

            e "Right Patient"
            
            hide rightptn
            jump menu2


        label op2:
            show rightdrug:
                size (564,573)
                xalign 0.5
                yalign 0.3
            with moveintop

            e "Right Drug"
                
            hide rightdrug
            jump menu2

        label op3:
            show rightdose:
                size (564,573)
                xalign 0.5
                yalign 0.3
            with moveintop

            e "Right Dose"
            
            hide rightdose
            jump menu2

        label op4:
            show rightroute:
                size (564,573)
                xalign 0.5
                yalign 0.3
            with moveintop

            e "Right Route"
                    
            hide rightroute
            jump menu2

        label op5:
            show righttime:
                size (564,573)
                xalign 0.5
                yalign 0.3
            with moveintop

            e "Right Time"
                    
            hide righttime
            jump menu2   

    label done1:

    hide p6
    with moveoutright
    hide lady2
    with moveoutleft

    show lady3:
       size (850, 850)
       xalign 1.0
       yalign 0.7
    with moveinright

    e "Let's have a short quiz."   


    label menu3:
        menu:
            with dissolve
            e "Which of this is NOT part of the 5R in Medication Safety?"
            "Right Time":
                jump c2

            "Right Patient":
                jump c2

            "Right Dose":
                jump c2    

            "Right Route":
                jump c2

            "Right Quantity":
                jump c1

            "Right Drug":
                jump c2
    
        label c1:
            play sound "correct.mp3"
            e "Correct! Seems like you are paying attention."

            jump done2

        label c2:

            play sound "wrong.mp3"
            e "Incorrect, do try again."
            jump menu3

    label done2:


    e "Let us continue our module."
    e "For our next part, we shall have a visit to our medical ward."

    play sound "step.mp3"
    hide lady3
    with moveoutright

    scene bg wad11:
         size (1920, 1080)
    with fade

    e "This is one of our medical ward."
    e "Let's enter."

    scene bg wad2:
         size (1920, 1080)
    with fade    

    show lady2:
       size (1280, 720)
       xalign -0.5
       yalign 0.8
    with moveinleft

    e "As pharmacist, not only do we handle medications at {b}Outpatient{/b}, but also in {b}Inpatient{/b} and this involves patients in the ward."
    e "In this case, it is our responsibility to collaborate with doctors and nurses to ensure Medication Safety is practiced for our patients."
    e "The next topic I would like to introduce is known as High-Alert Medication."
    
    show p9:
         size (1100,625)
         xalign 0.7
         yalign 0.15
    with moveinright
    
    e "What are HAMs?"

    hide p9
    with moveoutright

    show p10:
         size (1200,725)
         xalign 0.8
         yalign 0.1
    with moveinright

    e "Though medications listed under HAMs may differ from facilities depending on the drug availability..."
    e "...certain high risk drugs has been identified and listed based on reported cases of errors."

    hide p10
    with moveoutright

    show p11:
         size (556,677)
         xalign 0.6
         yalign 0.1
    with moveinright

    e "This is a very useful and informative guide on the safe use of HAMs, from our Ministry of Health."
    e "Not only that, it also lists down risk prevention strategies for the management of HAMs, which we will also go through later."
    e "I would highly recommend you to read it!"

    show qr:
         size (300,373)
         xalign 0.9
         yalign 0.25
    with moveinright

    e "Do scan the QR code to download the guide, or you can search it over on the internet."
 
    hide lady2
    with moveoutleft

    show p11:
        xalign 0.1
        yalign 0.1
    with move

    show qr:
        xalign 0.5
        yalign 0.25
    with move

    play sound "announce.mp3"
    show lady3:
       size (850, 850)
       xalign 1.0
       yalign 0.7
    with moveinright

    e "It's visiting hours in the ward. Let's head back to the pharmacy."

    play sound "step.mp3"

    hide lady3
    with moveoutright

    scene bg farmasi3:
        size (1920, 1080)
    with fade

    show lady2:
       size (1280, 720)
       xalign -0.5
       yalign 0.8
    with moveinleft

    e "Before we go through the risk prevention strategies for HAMs..."
    e "...let us go through some common risk factors associated with HAMs, to know what might cause errors in the first place."

    label menu4:
            menu:
                with dissolve
                e "There are 6 common risk factors. Choose one to learn more about it."
                "Different route of administration":
                    jump o1

                "Wrong infusion rate":
                    jump o2
                
                "Incorrect preparation of drug":
                    jump o3

                "Look Alike, Sound Alike (LASA)":
                    jump o4
                
                "Misinterpretation of medication order":
                    jump o5

                "Availability of products variation":
                    jump o6

                "{i}{b}(Skip){/b}{/i}":
                    jump done3

            label o1:
                show r1:
                    size (900,350)
                    xalign 0.5
                    yalign 0.2
                with moveintop

                e "Different route of administration"
                
                hide r1
                jump menu4


            label o2:
                show r2:
                    size (900,350)
                    xalign 0.5
                    yalign 0.2
                with moveintop

                e "Wrong infusion rate"
                    
                hide r2
                jump menu4

            label o3:
                show r3:
                    size (900,350)
                    xalign 0.5
                    yalign 0.2
                with moveintop

                e "Incorrect preparation of drug"
                
                hide r3
                jump menu4

            label o4:
                show r4:
                    size (900,350)
                    xalign 0.5
                    yalign 0.2
                with moveintop

                e "Look Alike, Sound Alike (LASA)"
                        
                hide r4
                jump menu4

            label o5:
                show r5:
                    size (900,350)
                    xalign 0.5
                    yalign 0.2
                with moveintop

                e "Misinterpretation of medication order"
                        
                hide r5
                jump menu4

            label o6:
                show r6:
                    size (900,350)
                    xalign 0.5
                    yalign 0.2
                with moveintop

                e "Availability of products variation"
                        
                hide r6
                jump menu4  

    label done3:

    hide lady2
    with moveoutleft

    scene bg farmasi1:
        size (1920, 1080)
    with fade

    show lady2:
       size (1280, 720)
       xalign -0.5
       yalign 0.8
    with moveinleft

    e "After learning about the risk factors, I am going to show you some examples from our pharmacy."
    
    hide lady2
    with moveoutleft

    play sound "search.mp3"
    scene black
    e "Hold on, give me a moment to search for examples...{p=5}{nw}"

    scene bg farmasi1:
        size (1920, 1080)
    with fade

    show lady2:
       size (1280, 720)
       xalign -0.5
       yalign 0.8
    with moveinleft

    e "Thanks for waiting, I got some samples to show you from around the pharmacy."

    show lasa1:
         size (820,720)
         xalign 0.65
         yalign 0.1
    with moveinright

    e "Take a look at these two bottles. I chose the same drug..."
    e "...or are they??"

    hide lasa1

    show lasa11:
         size (800,250)
         xalign 0.65
         yalign 0.3
    with irisout

    e "Look closer, they contain the same drug, but of different strength combination!"
    e "This falls under the risk factor of '{b}Availability of products variation{/b}'."
    e "Another possible risk factor is LASA, or known as '{b}Look Alike, Sound Alike{/b}.'"

    hide lasa11
    with moveoutright

    show lasa2:
         size (1000,520)
         xalign 0.7
         yalign 0.3
    with moveinright

    e "Here is another similar example."

    e "So what can we do to reduce the risk of errors?"
    e "Other than practicing the 5R's that I mentioned earlier..."
    e "...there are other risk reduction strategies that we can practice."
    
    hide lasa2
    with moveoutright

    show lasa3:
         size (600,750)
         xalign 0.65
         yalign 0.1
    with moveinright

    e "One of it is to have tagging like these for {b}LASA{/b} drugs."

    hide lasa3
    with moveoutright

    show ham1:
         size (700,400)
         xalign 0.3
         yalign 0.05
    with moveinright

    show ham2:
         size (700,400)
         xalign 0.9
         yalign 0.05
    with moveinright

    show ham3:
         size (700,400)
         xalign 0.6
         yalign 0.65
    with moveinright

    e "What does all these have in common?"
    e "Yes, they all have the {b}HAMs{/b}, or {b}High Alert Medications{/b} tag to alert its users."

    hide ham3
    with moveoutright
    hide ham2
    with moveoutright
    hide ham1
    with moveoutright

    show ham4:
         size (600,800)
         xalign 0.6
         yalign 0.05
    with moveinright
    
    e "{b}HAMs{/b} tagging can also be placed on product packages, containers, envelopes, and loose ampoules."

    hide ham4
    with moveoutright

    show tall1:
         size (600,800)
         xalign 0.4
         yalign 0.1
    with moveinright

    show tall3:
         size (600,800)
         xalign 0.9
         yalign 0.1
    with moveinright

    e "Did you notice anything special about the drug name?"
    e "Hint: Chlorpro{b}MAZINE{/b}....{b}CLOZ{/b}apine....{b}FLU{/b}oxetine....Fluvoxa{b}MINE{/b}...."
    e "This special method of naming is known as {b}TALL-man lettering{/b}."
    e "It is used to emphasize differences in medications with similar sounding names."

    hide tall3
    with moveoutright

    hide tall1
    with moveoutright

    hide lady2
    with moveoutleft

    scene bg farmasi3:
        size (1920, 1080)
    with fade

    show lady2:
       size (1280, 720)
       xalign -0.5
       yalign 0.8
    with moveinleft

    e "Oh no! An error has happened at the pharmacy."
    e "Should we report it? And how should we report it?" 
    e "Wait, before that, we should assess and see whether the error should be reported or not."
    e "Not all errors should be reported via MERS, or Medication Error Reporting System." 
    e "For this example, I am going to use a real case scenario of an actual error that has happened."
   
    show error:
         size (1280,400)
         xalign 0.9
         yalign 0.3
    with moveinright

    e "You received this STAT medication chit from the ward during your night shift."

    show error:
         size (1280,400)
         xalign 0.9
         yalign 0.02
    with move

    e "Which medication would you supply?"

    show venofer:
         size (200,400)
         xalign 0.5
         yalign 0.6
    with moveinright

    e "Option 1: Iron sucrose"

    show cosmofer:
         size (200,400)
         xalign 0.8
         yalign 0.6
    with moveinright

    e "or Option 2: Iron dextran"

    label menu5:
            menu:
                with dissolve
                e "Which is the correct drug?"
                "1: Iron sucrose":
                    jump d1

                "2: Iron dextran":
                    jump d2
        
            label d1:

                play sound "wrong.mp3"
                e "Unfortunately, this option is incorrect. This is the same medication error that happened in this real case scenario."
                jump done5

            label d2:

                play sound "correct.mp3"
                e "This option is correct. Unfortunately in this real case scenario, the wrong medication was supplied instead."
                jump done5

    label done5:
    
    e "In this case scenario, the staff nurse detected the error and returned the wrong medication to the pharmacy."
    e "Though the error didn't reach the patient, but a Medication Error reporting still need to be done with root cause analysis to prevent such further errors from happening."

    hide cosmofer
    with moveoutright

    hide venofer
    with moveoutright

    hide error
    with moveouttop

    show error2:
         size (700,700)
         xalign 0.4
         yalign 0.1
    with moveinright

    show error3:
         size (700,700)
         xalign 0.95
         yalign 0.1
    with moveinright

    e "From the RCA, remedial action include TALL-man lettering, and also to remind staff on differences between the two drugs."

    hide error3
    with moveoutright

    hide error2
    with moveoutright

    show p7:
         size (606,597)
         xalign 0.65
         yalign 0.1
    with moveinright

    e "What to report?"

    hide p7
    with moveoutright

    show p8:
         size (614,563)
         xalign 0.65
         yalign 0.1
    with moveinright

    e "What NOT to report?"

    hide p8
    with moveoutright

    show mers1:
         size (1300,700)
         xalign 0.9
         yalign 0.1
    with moveinright

    e "MERs online platform was launched in 2013 to facilitate the reporting of medication errors for both government and private health sectors."

    hide mers1
    with moveoutright
    
    show mers2:
         size (480,700)
         xalign 0.6
         yalign 0.1
    with moveinright

    e "There is a guideline on MERs available as reference if you wish to know more."
    
    hide mers2
    with moveoutright

    show mers3:
         size (1300,600)
         xalign 0.9
         yalign 0.15
    with moveinright

    e "The purpose of reporting ME is not to penalise, but to gather data for analysis..."
    e "...and to {b}LEARN{/b}, {b}SHARE{/b} and eventually minimize occurences of errors, which ultimately lead to improving {b}PATIENT SAFETY{/b}."

    hide mers3
    with moveoutright
    hide lady2
    with moveoutleft

    show lady:
        size (1280, 720)
        xalign 1.23
        yalign 0.7
    with moveinright

    e "This brings us to the end of our Medication Safety module."   
    e "Hopefully this course will be helpful in your daily work as healthcare professionals."
    e "As again, patient safety is our main priority."

    show qr2:
        size (600, 600)
        xalign 0.5
        yalign 0.1
    with moveinleft

    e "Before we end, do scan this QR for your feedback and to access the Medication Safety quiz."

    label menu6:
            e "In order for me to prepare your certificate of completion, please key in these details."

            python:
                        fullName = renpy.input("Your full name:")
                        ic = renpy.input("Your ic number (without -):")
                        email = renpy.input("Your email address:")

            menu:
                with dissolve
                e "Just to confirm your details: [fullName], [ic], [email]. Correct?"
                "Yes":
                    python:
                        stage = "finished"

                    jump done6
                     
                     
                "No":
                    jump menu6

    label done6:

    e "Remember, you still can access any parts of this module again with the {b}Load{/b} option {i}(If you have Saved before){/i}."
    e "I thank you for your time, [name] and see you again!"

    # This ends the game.

return
