; Write a program in the assembly language that computes the following arithmetic expression, considering the following data types for the variables:
; -> a - byte, b - doubleword; c-qword, where: a=2, b=1, c=20=14 (in hexadecimal) - Signed representation
; Expression: c+(a*a-b+7)/(2+a)=20+(2*2-1+7)/(2+2)=20+(10)/(4)=22=16 (in hexadecimal)
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
    b DD 1   
    c DQ 20   
    aux DD 0    
; our code starts here
segment code use32 class=code
    start:
        mov AL, byte[a]      ; AL=a=2
        add AL,2             ; AL=AL+2=4
        cbw                  ; signed conversion form AL to AX
        cwd                  ; signed conversion from AX to DX:AX
        push DX
        push AX
        pop EAX              ; EAX=DX:AX=4
        mov EBX,EAX          ; EBX=EAX=4
        mov EAX,0            ; EAX=0
        mov AL,byte[a]       ; AL=a=2
        imul byte[a]         ; AX=AL*a=2*2=4
        cwd                  ; signed conversion from AX to DX:AX
        push DX
        push AX
        pop EAX              ; EAX=DX:AX
        sub EAX,dword[b]     ; EAX=EAX-b=4-1=3
        mov ECX,7            ; EBX=7
        add EAX,ECX          ; EAX=EAX+EBX=3+7=10=A (in hexadecimal)
        cdq                  ; signed conversion from EAX to EDX:EAX
        idiv EBX             ; EAX= EDX:EAX/EBX=10/4=2  || EDX=2
        cdq
        add EAX,dword[c]
        adc EDX,dword[c+4]   ; EDX:EAX=EDX:EAX+c=20+2=22=16 (in hexadecimal)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
