# Projetar uma calculadora de conversão de bases (para números reais) que efetue as
# operações de soma e produto das bases 2 a 16


def get_ponto_flutuante(base,precisao,e,number):
    a=list(str(number))
    try:
        ind =a.index('.')
        l2 = a[ind:len(a)]
        del(l2[l2.index('.')])
    except:
        ind = len(a)
        l2 = []
    l1 = a[0:ind]
    pv = list(reversed(l1))
    k = len(pv)
    
    if(e>0):
        while(k<e):
            pv.append('0')
            k=k+1
        pv.append('0,')
    
    f = list(reversed(pv))+l2
    fnew=f[0:precisao+1]
    e=converter_base(10,base,e)
    value = ''.join(fnew)
    
    print("por truncamento: "+ str(value)+"X"+str(base)+"^"+str(e)) 
    h1=f[precisao+1:precisao+2]
    h1=''.join(h1)
    h2=value.replace('0,', '')
    
    
    p = soma(base,h1,h2)
    print("por arredondamento: 0,"+ str(p)+"X"+str(base)+"^"+str(e)) 
def produto(base,value1 ,value2):
    x1=base_10(base,value1)
    x2=base_10(base,value2)
    result = x1*x2
    result=converter_base(10,base,result)
    return result       
def soma(base,value1 ,value2):
    x1=base_10(base,value1)
    x2=base_10(base,value2)
    result = x1+x2
    result=converter_base(10,base,result)
    return result
def converter_base( base_in, base_out,  number):
    num_b10=base_10(base_in,number)
    result =[]
    while (num_b10>0):
        x=num_b10%base_out
        num_b10=int(num_b10/base_out)
        result.append(str(x))
    result =list(reversed(result))
    
    return int(''.join(result))
def converter_base_f( base_in, base_out,  number):
    
    result =['0.']
    t =0 
    while (t<10):
        x=number*base_out
        if(x<1):
            y = 0
        else:
            y = int(x)
        number=x-y
        result.append(str(y))
        t=t+1;
    
    result =(''.join(result))
    return float(result)
def converter_base_f2( base_in, base_out,  number):
    
    result =['0.']
    t =0 
    while (t<10):
        x=number*base_out
        if(x<1):
            y = 0
        else:
            y = int(x)
        number=x-y
        result.append(str(y))
        t=t+1;
    
    result =(''.join(result))
    return float(result)
def base_10(base_in,number):
    number=str(number)
    if(base_in==10):
        return int(number);
    size =len(number)-1
    total =0;
    for i in number:
        total = total +(int(i)*base_in**size)
        size=size-1
    return total
def opcao_2(base_in,base_out,number):
    if (number==int(number)):
        number= int(number)
        result = converter_base(base_in,base_out,number)
    else :
        if(int(number)!=0):
            v1=converter_base(base_in,base_out,int(number))
            number=number-int(number);
            v2=converter_base_f(base_in,base_out,number)
            result =v1+v2
        else:
            result=converter_base_f(base_in,base_out,number)
            
    return result

def iniciar():
    
    print("----- CALCULADORA DE BASES -----")
    print("1 - calcular ponto flutuante do resultado")
    print("2 - converter base")
    print("3 - soma")
    print("4 - produto")
    print("0 - sair")
    v1=0
    v2=0
    resultado="init"
    base_in=0
    base_out=0
    x =-1 
    while(x!=0):
        x=int(input("Digite uma opção :"))
        
        if(x==0):
            break
        if(x==1):
            elevation = len(str(int(resultado)))
            precisao = int(input("Digite a precisão que você deseja:"))
            get_ponto_flutuante(base_out,precisao,elevation,resultado)
        if(x==2):
            if(resultado!="init"):
                r=input("Deseja usar o ultimo resultado para converter ? [s/n]")
                if(r=='s'):
                    base_out=int(input("Para qual base deseja converter ?"))
                    v1=resultado
                    resultado=opcao_2(base_in,base_out,resultado)
                else:
                    v1=float(input("Digite valor a ser convertido :"))
                    base_in=int(input("Digite a base do valor :"))
                    base_out=int(input("Digite a base desejada :"))
                    resultado=opcao_2(base_in,base_out,v1)
            else:
                v1=float(input("Digite valor a ser convertido :"))
                base_in=int(input("Digite a base do valor :"))
                base_out=int(input("Digite a base desejada :"))
                resultado=opcao_2(base_in,base_out,v1)
            if (v1==int(v1)):
                v1= int(v1)
            print(str(v1)+"[BASE "+str(base_in)+"] ->"+str(resultado)+"[BASE "+str(base_out)+"]")
        if(x==3):
            
            base_out = int(input("Qual a base?"))
            base_in=base_out
            v1 = int(input("digite valor 1:"))
            v2 = int(input("digite valor 1:"))
            resultado=soma(base_out,v1,v2)
            print(str(v1)+"*"+str(v2)+" = "+str(resultado))
        if(x==4):
            
            base_out = int(input("Qual a base?"))
            base_in=base_out
            v1 = int(input("digite valor 1:"))
            v2 = int(input("digite valor 2:"))
            resultado=produto(base_out,v1,v2)
            print(str(v1)+"*"+str(v2)+" = "+str(resultado))
            
iniciar()