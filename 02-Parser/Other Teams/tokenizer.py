
import re
	
def tokenizer(data):
    current=0
    tokens=[]
    keywords=['main','int','void','for','while','do','if','else','break','char']
    alphabet=re.compile(r"[a-z|A-Z]|_|\d")
    numbers=re.compile(r"\.|\d")
    whitespace=re.compile(r"\s")
    operators=re.compile(r"[+,\-,*,/,&,^,|,%,^,>,<,~,!,=]")
    special_char=re.compile(r"[#,(,),{,},?,:,;,\\,\[,\],\,]")
    string=re.compile(r".")
    print (data)
    data=re.sub(r"//.*","",data)
    data=re.sub(r'\/\*.*\*\/',"",data)
    print (data)

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
            else:
                tokens.append({
                    'identifier':value,
                    })
            continue
        if re.match(string, char):
            value=''
            while re.match(string, char):
                value+= char
                current = current + 1
                char=data[current]
            tokens.append({
                "string" : value})
        current=current+1
    print(tokens)




main=''' (while While (num!=0))
    {
        _j_20 300 = num % 10.000;
        for (i = 0; i < 16; i++)
        {
            if (arr[i] == j)    //hello
            {
                if (i < 10)
                {
                    hexa[n] = (char)(i + 48);
                }
                else
                {
                /* remove that 8239741$%^*@#$@$ */
                    hexa[n] = (char)((i - 10) + 65);
                }
                break;
            }
       }
        num /= 10000;
        n++;
        printf("hello it %d is me");
    }'''
tokenizer(main)

