code = '''// Online C++ compiler to run C++ program online
#include <iostream>
int z { 5 + 10 } ;
int main ( ) {
    
    int x ;
    int y = 10 ;
    float h = z + y ;
    return 0;
}'''

code_list=code.split()
print(code_list)

print(f'"main" appears {code_list.count("main")} time(s)')

# ====================================================================================
from keyword import iskeyword
main_index= code_list.index("main")
StdTypes=('int', 'float', 'double', 'char', 'bool', 'void', 'wchar_t')
LocalVar=[]
LocalTyp=[]
GlobalVar=[]
GlobalTyp=[]
ErrorMsg=[]
FunctionNames=[]
Line=1
Operators= ['+', '-', '*', '/', '%', '&', '|', '^' ]
for Index in range (0, len(code_list)):

    if code_list[Index] not in StdTypes:
        continue
    elif Index == '\n':
        Line+=1
    else:
        Index+=1
        if code_list[Index+1]== '(':
            continue
        elif not code_list[Index].isidentifier():
            ErrorMsg.append(code_list[Index]+" is a Wrong Variable Name in Line "+ str(Line))
            continue
        elif iskeyword(code_list[Index]):
            ErrorMsg.append(code_list[Index]+" is a Wrong Variable Name in Line "+ str(Line))
            continue
        elif code_list[Index] == 'main':
            ErrorMsg.append(code_list[Index]+" is a Wrong Variable Name in Line "+ str(Line))
            continue
        elif code_list[Index] in FunctionNames:
            ErrorMsg.append(code_list[Index]+" is a Wrong Variable Name in Line "+ str(Line))
            continue
        elif code_list[Index+1] != ';' and code_list[Index+1] != '{' and code_list[Index+1] != '=':
            ErrorMsg.append(code_list[Index]+" missing ; in line "+ str(Line))
            continue 
        elif code_list[Index+1]== ';':
            if Index < main_index:
                GlobalVar.append(code_list[Index])
                GlobalTyp.append(code_list[Index-1])
            elif Index > main_index:
                LocalVar.append(code_list[Index])
                LocalTyp.append(code_list[Index-1])
        elif code_list[Index+1]== '=':
            i=Index
            while 1:
                i+=2
                if (code_list[i].isdigit() or code_list[i] in LocalVar or code_list[i] in GlobalVar) and code_list[i+1]==';':
                    if Index < main_index:
                        GlobalVar.append(code_list[Index])
                        GlobalTyp.append(code_list[Index-1])
                    elif Index > main_index:
                        LocalVar.append(code_list[Index])
                        LocalTyp.append(code_list[Index-1])
                    break
                elif not ((code_list[i].isdigit() or code_list[i] in LocalVar or code_list[i] in GlobalVar) and code_list[i+1] in Operators):
                    ErrorMsg.append("Wrong declaration in Line "+ str(Line))
                    break
        elif code_list[Index+1]== '{':
            i=Index
            while 1:
                if code_list[Index+2]=='}' and code_list[Index+3]==';':
                    if Index < main_index:
                        GlobalVar.append(code_list[Index])
                        GlobalTyp.append(code_list[Index-1])
                    elif Index > main_index:
                        LocalVar.append(code_list[Index])
                        LocalTyp.append(code_list[Index-1])
                    break
                i+=2
                if (code_list[i].isdigit() or code_list[i] in LocalVar or code_list[i] in GlobalVar) and code_list[i+1]=='}' and code_list[i+2]==';':
                    if Index < main_index:
                        GlobalVar.append(code_list[Index])
                        GlobalTyp.append(code_list[Index-1])
                    elif Index > main_index:
                        LocalVar.append(code_list[Index])
                        LocalTyp.append(code_list[Index-1])
                    break
                elif (code_list[i].isdigit() or code_list[i] in LocalVar or code_list[i] in GlobalVar) and code_list[i+1]=='}' and code_list[i+2]!=';':
                    ErrorMsg.append("; is missing in Line "+ str(Line))
                    break
                elif not ((code_list[i].isdigit() or code_list[i] in LocalVar or code_list[i] in GlobalVar) and code_list[i+1] in Operators):
                    ErrorMsg.append("Wrong declaration in Line "+ str(Line))
                    break
print(ErrorMsg)
print(LocalVar)
print(LocalTyp)
print(GlobalVar)
print(GlobalTyp)
