euros, centims = map(int, input().split())

if centims >= 100:
    print("Import no vàlid")
else:
    t = euros*100 + centims

    b500 = t//50000; t%=50000
    b200 = t//20000; t%=20000
    b100 = t//10000; t%=10000
    b50  = t//5000;  t%=5000
    b20  = t//2000;  t%=2000
    b10  = t//1000;  t%=1000
    b5   = t//500;   t%=500

    m2e  = t//200;   t%=200
    m1e  = t//100;   t%=100

    m50  = t//50;    t%=50
    m20  = t//20;    t%=20
    m10  = t//10;    t%=10
    m5   = t//5;     t%=5
    m2   = t//2;     t%=2
    m1   = t//1

    print("Bitllets de 500 euros:", b500)
    print("Bitllets de 200 euros:", b200)
    print("Bitllets de 100 euros:", b100)
    print("Bitllets de 50 euros:", b50)
    print("Bitllets de 20 euros:", b20)
    print("Bitllets de 10 euros:", b10)
    print("Bitllets de 5 euros:", b5)
    print("Monedes de 2 euros:", m2e)
    print("Monedes de 1 euro:", m1e)
    print("Monedes de 50 centims:", m50)
    print("Monedes de 20 centims:", m20)
    print("Monedes de 10 centims:", m10)
    print("Monedes de 5 centims:", m5)
    print("Monedes de 2 centims:", m2)
    print("Monedes de 1 centim:", m1)


    
