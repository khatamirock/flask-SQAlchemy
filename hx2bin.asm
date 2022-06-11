
org 100h

.data
ms db 'kire vai $'
nl dw 13,10, '$'
num dw 13h
.code
mov ax, @data
mov ds, ax

lea dx,ms
mov ah,9
int 21h

mov ax,num



prin proc near
mov ah,2
mov ds,ax
int 21h

ret

