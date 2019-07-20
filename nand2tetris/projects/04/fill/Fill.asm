// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
           //a b存储屏幕最小地址和屏幕最大地址
@SCREEN
D=A
@a
M=D
@24575
D=A
@b
M=D

(LOOP)  
@KBD
D=M
@LOOP1
D;JGT
@LOOP2
D;JEQ

(LOOP1)
@a	
D=M
@b
D=D-M
@LOOP
D;JEQ

@a
D=M
A=M
M=1
@a
M=D+1
@LOOP
0;JMP

(LOOP2)
@a	
D=A
@SCREEN
D=D-A
@LOOP
D;JEQ

@a
D=M
A=M
M=0
@a
M=D-1
@LOOP
0;JMP