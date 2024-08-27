---
layout: post
title: x86 assembly code basics for reverse engineers
date: 2024-08-25 21:32 -0400
description: Learn the basics of x86 assembly code for use in dissemblers like
  Ghidra, IDA, and Binary Ninja, and debuggers like x64dbg.
image:
  path: /assets/images/asm.webp
  description: A screenshot of Locky locale checks in Ghidra
categories:
  - Malware Reverse Engineering
---

Assembly language is the lowest-level set of instructions for a CPU. You need
to know the basics of assembly to use dissemblers like Ghidra, IDA, and
Binary Ninja, and debuggers like x64dbg. x86 is the CPU architecture that
most Windows systems use. Although the ARM CPU architecture is making some gains
in marketshare, Windows on ARM an emulate x86 applications, and 64 bit CPUs can
run 32 bit applications. Malware authors are likely to continue to target 32 bit
x86 CPUs for some time for maximum compatibility, so this guide will focus on
32 bit x86 assembly.

## Registers

Registers are super-fast temporary memory on a CPU. On x86 CPUs the registers
store 32 bits each. The general purpose registers `EAX`, `EBX`, `ECX`, and `EDX`
can each be divided into 16 or 8 bits as shown in the diagram below.

![A diagram of x86 registers by David Evans at the University of Virginia](/assets/images/x86-registers.webp)
_Diagram by David Evans at the University of Virginia_

Some registers are used for specific tasks.

**Register**|**Purpose**
EAX|Used for addition, multiplication, and return value
EBP|Base pointer. Often used to reference arguments passed into a function, as well as the local variables within a function.
ECX|Used as a counter
ESP|Points to the last item on the stack - the stack pointer
ESI/EDI|Used by memory transfer instructions
EIP|Points to the next instruction to execute

### Condition Codes (CC)

Condition code registers are used to flag when conditions are met.

**Register**|**Purpose**
CF|Carry flag
ZF|Zero Flag
SF|Sign Flag
OF|Overflow flag

## The stack

The stack is a last-in-first-out (LIFO) data structure that is stored in system
memory (i.e., RAM). Like a stack of plates, the last item `pushed` onto the
stack will be the first item `popped` off of the stack.

![A representation of the stack with push and pop operations](/assets/images/lifo-stack.webp)

32 bit applications use the stack to store the values of local variables and
function arguments.  The first parameter will be the bottom `PUSH` instruction,
and the last argument will be the top `PUSH` instruction. Each item on the stack
has 4 bytes. Addressing on the stack goes from larger to smaller values as more
items are added to the stack, which might seem counterintuitive.

The `ESP` register points to the address of the next item on the stack. Its
value is automatically updated as the stack changes.

The `EBP` register stores the base pointer (also known as the frame pointer),
which is an unchanging value that is as a reference point for accessing items on
the stack. For example:

Parameter: `EBP` + value<br>
Local variables: `EBP` - value

## Assembly notation

Ghidra and other tools use the Intel notation for assembly code, which follows
this format when moving data in and out of registers.

```nasm
MOV DESTINATION, SOURCE
```

Comments start with `;`.

In Ghidra, parameters that reference memory locations instead of a direct value
are enclosed in square brackets. For example:

```nasm
MOV EAX, [0x410230]
```

**Example**|**Description**
-----------|---------------
[EAX]|Access dynamically allocated memory (base)
[EBP + 0x10]|Access data on the stack (base + displacement)
[EAX + EBX * 8]|Access an array with 8-byte structures (base + index * scale)
[EAX + EBX + 0xC]|Access a two-dimensional array of structures (base + index + displacement)

## Common patterns

### Setting a register to 0

Compilers will XOR a register by itself as the most efficient way of setting
that register to `0`.

```nasm
XOR EDI, EDI
```

### Testing if a register is set to 0

```nasm
TEST EAX, EAX ; Implied AND, but does NOT modify the destination register
```

### Testing if a register is set to a value

```nasm
CMP ECX, 8 ; Implied SUB, but does NOT modify the destination register
```

## Stack cleanup

```nasm
LEAVE
RET
```

## Unconditional jumps

**Name**|**Description**
--------|---------------
JMP|Jump directly to a memory address
CALL|Call a function
RET|Return a value to the calling function

## Conditional jumps

jcc format

**Notation**|**Description**
a|Above (unsigned)
b|Below (unsigned)
e|Equal
n|Not equal
g|Greater (signed)
l|Less (signed)
z|Zero

### Conditional jump examples

**Notation**|**Description**
jz|jump if zero
jnz|Jump if not 0
ja|jump above
jnge|jump if not greater than or equal to

loopcc format

Follows the same notation as jcc

### Loop example

A loop that adds `1` to the control variable while it is less than `5`.

```text
Start:
  mov eax, 0 ; Initialize the control variable

CheckIfStop:
  cmp eax, 5 ; Compare the current state of the control variable with the end condition
  jnl End ; jnl ; jump if not less. je (jump if equal) would also work here

InsideLoop:
  ; Actions inside the loop go here
  add eax, 1 ; Increment the control variable
  jmp CheckIfStop

End:
  ; Code that continues here after the loop
```

## Code branching

To convert if/else and case statements from C/C++ to assembly, compilers will
use conditional jumps. For example, when evaluating an `OR` condition, both
conditional jumps will point to the same function. When evaluating an `AND`
condition, the first conditional jump will jump to code to evaluate the second
condition, which will then execute the code if the second condition passes.

## Error handling

Often, Windows API calls return `0` (also called `FALSE` or `NULL`) in the
event of a failure, but not always. When examining functions that make Windows
API calls, it is important to look up that API call in Microsoft's documentation
(simply by Googling for the function name), to see what the possible return
values are and their meanings.

A common pattern is for any Windows executable is to call the API function, then
use the `JNZ` operation to jump to another function if the API call returned
`0`. After the `JNZ` operation, there is usually a call to `GetLastError` that
is used if the jump did not take place (because API call did not return `0`),
in order to get the error code for the current thread. The Jump Zero (`JZ`)
operation is used as the reverse of `JNZ`.

## Calling conventions

The `cdecl` and `stdcall` calling conventions have a few things in common:

- Arguments are added to the stack from right to left
- The return value is stored in EAX

### cdecl

- Most common
- The caller cleans up the stack by removing the arguments

### stdcall

- Used in the WIN32 APIs
- The callee cleans up the stack by removing the arguments

### fastcall

- Arguments are stored in registers
- Both Microsoft and GNU compilers use ECX and EDX
- Additional arguments are stored on the stack
- The callee cleans up the stack by removing the arguments

### thiscall

- Used in C++ object member functions
- `this` is stored as a pointer
- Microsoft compilers store the `this` pointer in `ECX`, and the callee cleans up the stack
- GNU compilers store the `this` pointer as the last (i.e., top) item pushed to the stack

## 64 bit assembly

### 64 bit expanded general purpose registers

**32 bit register**|**64 bit register**|**Purpose**
EAX|RAX|Used for addition, multiplication, and return value
ECX|RCX|Used as a counter
ESP|RSP|Points to the last item on the stack
ESI/EDI|RSI/RDI|Used by memory transfer instructions

> `RSP` is often used to access parameters instead of `RBP`.
{: .prompt-info }

### New 64 bit general purpose registers

R8 through R15

These can be accessed as smaller registers by appending a character to the end
of a register, such as `R9`:

- R9D: Lower 32 bits (Double word - DWORD)
- R9W: Lower 16 bits (WORD)
- R9B: Lower 8 bits (byte)

### 64 bit calling convention

Because of the expanded and additional registers, compilers will pass parameters
via registers, instead of via the stack.

1. RCX
2. RDX
3. R8
4. R9

Any additional arguments are placed onto the stack.

> Ghidra is unable to propagate external parameters in 64 bit PE files, so it cannot annotate parameter data types for you.
{: .prompt-warning }

### 64 bit addressing

 `RIP` + Displacement
