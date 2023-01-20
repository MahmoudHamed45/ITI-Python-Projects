

import re
from itertools import chain	
def tokenizer(data):
    current=0
    tokens=[]
    datatypes=['int','void','float','double','char','int*']

    keywords=['main','for','while','do','if','else','break','return']
    alphabet=re.compile(r"[a-z|A-Z]|_|\d")
    numbers=re.compile(r"\.|\d")
    whitespace=re.compile(r"\s")
    operators=re.compile(r"[+,\-,*,/,&,^,|,%,^,>,<,~,!,=]")
    special_char=re.compile(r"[#,(,),{,},?,:,;,\',\",\\,\[,\],\,]")

    while current < len(data):
        char = data[current]
        if re.match(whitespace, char):
            current = current +1
            continue
        if re.match(special_char,char):
            tokens.append({
                'special char': char
                })
            current=current+1
            continue
        if re.match(operators, char):
            value=''
            while re.match(operators, char):
                value += char
                current = current +1
                char= data[current]
            tokens.append({
                'operator':value             
                })
            continue
        if re.match(numbers, char):
            value=''
            while re.match(numbers, char):
                value += char
                current = current +1
                char= data[current]
            tokens.append({
                'number':value             
                })
            continue
        if re.match(alphabet, char):
            value=''
            while re.match(alphabet, char):
                value += char
                current = current +1
                char= data[current]
            if value in keywords:
                tokens.append({
                 'keyword':value,
                 })
            elif value in datatypes:
                tokens.append({
                    'datatypes':value,
                    })
            
            else:
                tokens.append({
                    'identifier':value,
                    })
            continue
        current=current+1
    return(tokens)



Decleration="int fun(int a,int b);"
Calling="fun(3,5);"
Defenation='''int fun(int a,int b){
    int res=a*b;
    return res;
}
    '''


main='''
int x=4

void fun(void);



(while While (num!=0))
    {
        _j_20 300 = num % 10.000;
        for (i = 0; i < 16; i++)
        {
            if (arr[i] == j)
            {
                if (i < 10)
                {
                    hexa[n] = (char)(i + 48);
                }
                else
                {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                    hexa[n] = (char)((i - 10) + 65);
                }
                break;
            }
       }
        num /= 10000;
        n++;
#     }'''


Tokens =tokenizer(main)
# if(Tokens[0].keys()=='keyword'):
#     print("yes")
res = list(chain.from_iterable(sub.keys() for sub in Tokens))
print(Tokens)
#int fun(int a);
#int x=4

for i in range(len(Tokens)):
    #void fun(void);
    #void fun(void){}
    Functions=[]
    # Functions[0]={
    #     'Name': 'fun',
    #     'Return_type':'int',
    #     'Arguments':['int','char']
    # }

    if(res[i]=='identifier' and res[i+1]=='special char' and Tokens[i+1]['special char']=='('):
        print("It's Function")
        prev=Tokens.index(Tokens[i])-1
        if(res[prev]=='datatypes'):
            print(res[i])
            print("It's prototype or definenation")
            index_of_close_P=0
            # for j in range(i ,True):
            #     if(res[]==):

                    
            # if(res[i+2]=='datatypes' and res[i+2]['datatypes']=='('):
            #     print("It's Prototype")


        else:
            print(res[i])
            print("Error Undefined Defination")    





# test="E"
# res=re.match('E',test)
# print(res)

[{'special char': '('}, {'keyword': 'while'}, {'identifier': 'While'}, {'special char': '('}, {'identifier': 'num'}, {'operator': '!='}, {'number': '0'}, {'special char': ')'}, {'special char': ')'}, {'special char': '{'}, {'identifier': '_j_20'}, {'number': '300'}, {'operator': '='}, {'identifier': 'num'}, {'operator': '%'}, {'number': '10.000'}, {'special char': ';'}, {'keyword': 'for'}, {'special char': '('}, {'identifier': 'i'}, {'operator': '='}, {'number': '0'}, {'special char': ';'}, {'identifier': 'i'}, {'operator': '<'}, {'number': '16'}, {'special char': ';'}, {'identifier': 'i'}, {'operator': '++'}, {'special char': ')'}, {'special char': '{'}, {'keyword': 'if'}, {'special char': '('}, {'identifier': 'arr'}, {'special char': '['}, {'identifier': 'i'}, {'special char': ']'}, {'operator': '=='}, {'identifier': 'j'}, {'special char': ')'}, {'special char': '{'}, {'keyword': 'if'}, {'special char': '('}, {'identifier': 'i'}, {'operator': '<'}, {'number': '10'}, {'special char': ')'}, {'special char': '{'}, {'identifier': 'hexa'}, {'special char': '['}, {'identifier': 'n'}, {'special char': ']'}, {'operator': '='}, {'special char': '('}, {'keyword': 'char'}, {'special char': ')'}, {'special char': '('}, {'identifier': 'i'}, {'operator': '+'}, {'number': '48'}, {'special char': ')'}, {'special char': ';'}, {'special char': '}'}, {'keyword': 'else'}, {'special char': '{'}, {'identifier': 'hexa'}, {'special char': '['}, {'identifier': 'n'}, {'special char': ']'}, {'operator': '='}, {'special char': '('}, {'keyword': 'char'}, {'special char': ')'}, {'special char': '('}, {'special char': '('}, {'identifier': 
'i'}, {'operator': '-'}, {'number': '10'}, {'special char': ')'}, {'operator': '+'}, {'number': '65'}, {'special char': ')'}, 
{'special char': ';'}, {'special char': '}'}, {'keyword': 'break'}, {'special char': ';'}, {'special char': '}'}, {'special char': '}'}, {'identifier': 'num'}, {'operator': '/='}, {'number': '10000'}, {'special char': ';'}, {'identifier': 'n'}, {'operator': '++'}, {'special char': ';'}, {'special char': '}'}]

[{'keyword': 'int'}, {'identifier': 'fun'}, {'special char': '('}, {'keyword': 'int'}, {'identifier': 'a'}, {'special char': ','}, {'keyword': 'int'}, {'identifier': 'b'}, {'special char': ')'}, {'special char': ';'}]


'''
int fun(int a,);

{

if (){}

}
'''


