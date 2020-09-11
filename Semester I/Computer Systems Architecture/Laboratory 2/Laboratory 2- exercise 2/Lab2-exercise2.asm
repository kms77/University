; Write a program in the assembly language that computes the following arithmetic expression, considering the following data types for the variables:
; a - byte, b - word, c - double word, d - qword - Signed representation where: a=3, b=2, d=6, c=12
; Expression: (c+b+a)-(d+d)=(12+2+3)-(6+6)=17-12=5
bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a DB 3    
    b DW 2    
    c DD 12   
    d DQ 6  
    aux DD 0    
; our code starts here
segment code use32 class=code
    start:
        mov AL,byte [a]      ; AL=a=3
        cbw                  ; signed conversion from AL to AX
        add AX,word[b]       ; AX=AX+b=3+2=5
        cwd                  ; signed conversion from AX to EAX
        push DX
        push AX
        pop EAX              ; EAX=DX:AX
        add EAX,dword[c]     ; EAX=EAX+c=5+12=17=11 (in hexadecimal)
        mov dword [aux],EAX  ; aux=EAX=17=11 (in hexadecimal)        
        mov EAX,dword[d]     
        mov EDX,dword[d+4]   ; EDX:EAX=d=6
        add EAX,dword[d]
        adc EAX,dword[d+4]   ; EDX:EAX=EDX:EAX+d=6+6=12=C (in hexadecimal)
        mov EBX,EAX          
        mov ECX,EDX          ; ECX:EBX=EDX:EAX=12=C (in hexadecimal)
        mov EAX,dword[aux]   ; EAX=aux=17=11 (in hexadecimal)
        cdq                  ; signed conversion from EAX to EDX:EAX
        mov EDX,0         
        sub EAX,EBX          ; 
        sbb EDX,ECX          ; EDX:EAX=EDX:EAX-ECX:EBX=17-12=5
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
