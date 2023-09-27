# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;
### Liftoff Part 1: The Countdown

The assignment was to create a countdown for a space mission that counts down from 10 to 0 and declares liftoff. This is all to be printed in the terminal.
### Evidence 
![Countdown video](images/liftoff.countdowngif.gif)

### Code
[Countdown Code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/liftoff_countdown.py) 

### Reflection

As this was the first real coding assignment this year, I experienced some difficulty when creating my coundown. Not only did I have to use a for loop, of which I had to remind myself, but I also had trouble with the range. The assignment asks for a countdown from 10 to 0 and when I was inputing the range for my countdown, I created a range from 10-0. However, that doesn't include 0 at the end of the countdown because it considers it a mission accomplished when it reaches 1. In the end, I decided to leave it this way because it seems silly to print 0 and then print liftoff because in reality, a rocket would liftoff ON 0 not AFTER 0.

&nbsp;

### Liftoff Part 2: The Lights

Next, we had to change our code to include 2 external LEDs: one red and one green. The red LED had to blink for each number in the countdown and the green LED had to turn on upon liftoff, all while still displaying the necesary information as outlined in the previous assignment in the terminal.

### Evidence 

![Lights video](images/liftoff.lights.gif) 

### Wiring

![Lights wiring](images/liftoff.lights.jpg)

### Code
[Lights Code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/liftoff_lights.py)

### Reflection

My code was working beautifully BUT shortly thereafter, it mysteriously quit working. After a long time looking at it but not actually changing anything, it started working again and I successfully achieved liftoff. I also had an issue putting my video into my README because my file was too big but I fixed that too. I had hesitation when I had to blink the red led because I had to put multiple sleep commands in that add up to one second but I figured that out.

&nbsp;
### Liftoff Part 3: The button

The assignment was to add a button that triggers the countdown that uses the correct LEDs and shows the correct display in the terminal as described in the previous assignments.

### Evidence 

![Button video](images/liftoff.buttongif.gif) 
### Wiring

![Button wiring](images/liftoff.buttonwiring.jpg)

### Code
[Button Code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/liftoff_button.py)

### Reflection

The main difficulty that I faced was wiring the button. I had a lot of trouble getting my code to respond to the button even though the code seemed like it should have been working. In the end, I had the power and the pin going into the same rail on the board which meant the button wasn't actually going to respond to my code. When I fixed that, it started working immediately and I now have a functinoal button triggered countdown.

&nbsp;

### Liftoff Part 4: The servo

The extension of the assignment was to have a servo move 180 degrees upon liftoff to simulate the actual process of liftoff.

### Evidence 

![Servo video](images/liftoff.servo.gif)

### Wiring
![Servo wiring](images/liftoff.servowiring.jpg)
### Code
[Servo code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/liftoff_servo.py)
### Reflection

Hazel wasn't there the first day I was on this assignment so I was forced to figure it out completely by myself. I was able to figure out all of the code by myself for the first time. However, I struggled with the wiring and in the end, what was stopping me from succeeding was the fact that the ground going to my servo was going through a resistor. Also, I discovered a fun new feature of VScode when it started showing me my recent changes by displaying a very scary red triangle on the left side of the code. It turned out that it was not an emergency, just recent edits.

&nbsp;


### Crash avoidance: Part 1

Using an accelerometer, print the x, y, and z acceleration and angular velosity.

### Evidence 

![Part 1 video](images/crashavoidance_part1gif.gif)

### Wiring
![Part 1 wiring](images/WIN_20230920_09_37_01_Pro.jpg)
### Code
[Part 1 code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance_part1.py) 

### Reflection

The directions were very clear for this assignment so there was little room for error prone interpretation. The part that I had the most trouble with was when I accidentally created a new code.py file in my VS code that was unrelated to my PICO. I did that because the original code.py wasn't showing up but it turns out, if your code.py doesn't have any relationship with your Circuitpy folder, the code won't run. Don't worry though, I recovered my other code.py by plugging my PICO into the computer which I probably should have done at the beginning.

&nbsp;
### Crash avoidance: Part 2

Using an accelerometer, print the x, y, and z acceleration and angular velosity.

### Evidence 

![Part 2 video](images/crashavoidance_part2gif.gif)

### Wiring
![Part 2 wiring](images/crash2wiring.jpg)
### Code
[Part 2 code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance_part2.py) 

### Reflection

The directions were very clear for this assignment so there was little room for error prone interpretation. The part that I had the most trouble with was when I accidentally created a new code.py file in my VS code that was unrelated to my PICO. I did that because the original code.py wasn't showing up but it turns out, if your code.py doesn't have any relationship with your Circuitpy folder, the code won't run. Don't worry though, I recovered my other code.py by plugging my PICO into the computer which I probably should have done at the beginning.

&nbsp;
### Crash avoidance: Part 3

Using an accelerometer, print the x, y, and z acceleration and angular velosity on the OLED screen.

### Evidence 

![Part 3 video](images/crashavoidance_part3gif.gif)
![Part 3 Picture](images/crashavoidance_part3.jpg)

### Wiring
![Part 3 wiring](images/crashavoidance_part3wiring.jpg)
### Code
[Part 3 code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance_part3.py) 

### Reflection

The most easily made mistake for me this time was releasing the i2c pin BEFORE you declare where the pin goes. Second, I struggled a little with getting the OLED to move the cursor because it doesn't work like LCD displays. The wiring of the SCL and the SCL and the SDA and the SDA was weird since it had to be wired to each other in a chain like fashion.

&nbsp;
### Crash avoidance: Part 4

Using an accelerometer, print the x, y, and z acceleration and angular velosity on the OLED screen. Using an altimeter, only turn the LED on if the altitude is less than 3 meters above launch point.

### Evidence 

![Part 4 video](images/crashavoidance_part4gif.gif)

### Wiring
![Part 4 wiring](images/WIN_20230927_13_52_36_Pro.jpg)
### Code
[Part 4 code](https://github.com/ABird2918/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance_part4.py) 

### Reflection

GUESS WHAT?!?! I successfully completed a spicy assignment without help from anyone else! I hadn't actually done a code assignment this year without significant assistance from Hazel Conklin but I completed this assignment all on my own for the first time this year, all in one day. There was a funny issue with my altimeter where it didn't know what a meter was so I had to go way farther than 3 meters for it to register as 3 meters but it worked anyway. Also - apparently i2c pins don't really work and it'll throw errors at you if you haven't wired it yet. So I learned that too--wire before you get upset because vscode is insulting you.

&nbsp;
## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test


Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[test.py](raspberry-pi/test.py)

### Test Image

![Humgry Hungry tortoise](images/tortoise-eating-meat-o.webp)

### Test GIF

![Smush](images/manatee-gif.gif)
