// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@2 
M=0  //初始化结果的位
(LOOP)  // 循环
@1
D=M
@END
D;JEQ      //当1 的值为0的时候跳到end
@0
D=M
@2
M=D+M   //内部是加法3*2变成 3+3
@1
M=M-1   //1是次数每次循环结束-1
@LOOP
0;JMP
@END
0;JMP

