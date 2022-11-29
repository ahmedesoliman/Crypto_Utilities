# author: ahmedesoliman
# breif: a program to generate the public keys and display the secret given the premitive P and the alpha a. assuming that private key a and b is also provided. 
 
if __name__ == '__main__':
 
    # Both the persons will be agreed upon the
    # public keys G and P
    # A prime number P is taken
    P = 53
     
    # A primitive root for P, alpha is taken
    alpha = 2
      
    # Alice will choose the private key a
    a = 21    
    a_pub = alpha ** a % P 
    print('The public key a for Alice is :%d '% (a_pub))
     
    # Bob will choose the private key b
    b = 25
    b_pub = alpha ** b % P 
    print('The public key b for Bob is :%d '% (b_pub))
     
     
    # Secret for Alice
    ka = a_pub ** b % P
     
    # Secret for Bob
    kb = b_pub ** a % P
     
    print('Secret key for the Alice is : %d '%(ka))
    print('Secret Key for the Bob is : %d '%(kb))