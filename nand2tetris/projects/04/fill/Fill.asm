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
//�ڽ��б��֮ǰ��Ҫ�������A��MҪ�ֱ����Aһ��洢�ڴ��ַMһ��洢�ڴ��ַ�е�����
//a b�洢��Ļ��С��ַ����Ļ����ַ
@SCREEN
D=A
@a
M=D
@24575
D=A
@b
M=D
//��ѭ��
(LOOP)  
@KBD  //����ֵ����һ
D=M
@LOOP1
D;JGT
@LOOP2  //����ֵΪ0
D;JEQ

(LOOP1)
//�ж��Ƿ�Ϊȫ�ڣ�����Ǿͻص�ѭ��ͷ��
@a	
D=M
@b
D=D-M
@LOOP
D;JEQ
// �洢��ǰ��ֵַ�����ҽ���ǰ��ַ���ڴ�ֵ��Ϊ1
@a
D=M
A=M
M=1
@a  //��ֵַ+1
M=D+1
@LOOP
0;JMP

(LOOP2)
//�ж���Ļ�Ƿ�Ϊȫ��
@a	
D=A
@SCREEN
D=D-A
@LOOP
D;JEQ
//����ͬ��LOOP1
@a
D=M
A=M
M=0
@a
M=D-1
@LOOP
0;JMP