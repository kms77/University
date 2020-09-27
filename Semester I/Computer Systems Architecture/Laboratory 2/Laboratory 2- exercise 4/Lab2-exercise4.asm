; Write a program in the assembly language that computes the following arithmetic expression, considering the following data types for the variables:
; a,b,c-byte; d-doubleword; e-qword- where a=3, b=2, c=4, d=10=A (in hexadecimal), e=20=14 (in hexadecimal) 
; Expression: 2/(a+b*c-9)+e-d = 2/(3+2*4-9)+20-10=2/(3+8-9)+10=(2/2)+10=11=B (in hexadecimal) -Sign representation

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
    b DB 2
    c DB 4
    d DD 10
    e DQ 20
; our code starts here
segment code use32 class=code
    start:
        mov AL, byte[b]      ; AL=b=2
        imul byte[c]         ; AX=AL*c=2*4=8
        mov BX,AX            ; BX=AX=8
        mov AL, byte[a]      ; AL=a=3
        cbw
        add AX,BX            ; AX=AX+BX=3+8=11=B (in hexadecimal)
        mov BX,AX            ; BX=AX=11=B (in hexadecimal)
        mov AL,9             ; AL=9
        cbw                  ; signed conversion from AL to AX
        sub BX,AX            ; BX=BX-AX=11-9=2
        mov AL,2             ; AL=2
        cbw                  ; signed conversion from AL to AX
        cwd                  ; signed conversion from AX to DX:AX
        push DX
        push AX
        pop EAX              ; EAX=DX:AX=2
        idiv BX              ; AX=EAX/BX=2/2=1  | Dx=EAX%BX=2%2=0
        cbw                  ; signed conversion from AL to AX
        cwd                  ; signed conversion from AX to DX:AX
        push DX
        push AX
        pop EAX              ; EAX=DX:AX=1
        cdq                  ; signed conversion from EAX to EDX:EAX
        add EAX, dword[e]  
        adc EDX, dword[e+4]  ; EDX:EAX=EDX:EAX+d=1+20=21=15 (in hexadecimal)
        sub EAX, dword[d]    ; EAX=EAX-d=21-10=11=B (in hexadecimal)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
