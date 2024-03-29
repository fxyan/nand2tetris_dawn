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
//在进行编程之前主要问题就是A和M要分辨清楚A一般存储内存地址M一般存储内存地址中的数据
//a b存储屏幕最小地址和屏幕最大地址
@SCREEN
D=A
@a
M=D
@24575
D=A
@b
M=D
//主循环
(LOOP)  
@KBD  //键盘值大于一
D=M
@LOOP1
D;JGT
@LOOP2  //键盘值为0
D;JEQ

(LOOP1)
//判断是否为全黑，如果是就回到循环头部
@a	
D=M
@b
D=D-M
@LOOP
D;JEQ
// 存储当前地址值，并且将当前地址的内存值改为1
@a
D=M
A=M
M=1
@a  //地址值+1
M=D+1
@LOOP
0;JMP

(LOOP2)
//判断屏幕是否为全白
@a	
D=A
@SCREEN
D=D-A
@LOOP
D;JEQ
//几乎同上LOOP1
@a
D=M
A=M
M=0
@a
M=D-1
@LOOP
0;JMP