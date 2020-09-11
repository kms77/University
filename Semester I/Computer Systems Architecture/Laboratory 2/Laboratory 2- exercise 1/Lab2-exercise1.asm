; Write a program in the assembly language that computes the following arithmetic expression, considering the following data types for the variables:
; a - byte, b - word, c - double word, d - qword - Unsigned representation where: a=2, b=5, d=1, c=10
; Expression : c-(a+d)+(b+d)=10-(2+1)+(5+1)=10-3+6=7+6=13=D (in hexadecimal)
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DB 2
    b DW 5
    c DD 10 
    d DQ 1    
; our code starts here
segment code use32 class=code
    start:
        mov EBX,dword[d]     
        mov ECX,dword[d+4]   ; ECX:EBX=1
        mov AL,byte [a]      ; AL=a=2 
        mov AH,0             ; unsigned conversion from AL to AX
        mov DX,0             ; unsigned conversion from AX to DX:AX
        push DX
        push AX
        pop EAX              ; unsigned conversion from DX:AX to EAX
        mov EDX,0            ; convert EAX to EDX:EAX
        add EAX,EBX
        adc EDX,ECX          ; EDX:EAX=EDX:EAX+ECX:EBX=1+2=3
        mov EBX,EAX          ; EBX=EAX=3
        mov EAX,dword[c]     ; EAX=c=10=A (in hexadecimal)
        sub EAX,EBX           
        sbb EDX,ECX          ; EDX:EAX=EDX:EAX-ECX:EBX=10-3=7
        mov EBX,EAX          ; EBX=EAX=7
        mov ECX,EDX          ; ECX=EDX=0
        mov AX, word[b]      ; AX=b=5
        mov DX,0             ; unsigned conversion from AX to DX:AX
        push DX
        push AX
        pop EAX              ; unsigned conversion from DX:AX to EAX
        mov EDX,0            ; unsigned conversion from EAX to EDX:EAX
        add EAX,dword[d]      
        adc EDX,dword[d+4]   ; EDX:EAX=EDX:EAX+d=5+1=6
        add EAX,EBX          
        adc EDX,ECX          ; EDX:EAX=EDX:EAX+ECX:EBX=6+7=13=D (in hexadecimal)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
