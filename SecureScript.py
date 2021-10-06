# coding: utf-8
import base64
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import argparse
import sys
import colored
from colored import stylize

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encode", help="Give the file that you want to encode")
parser.add_argument("-d", "--decode", help="Give the file that you want to decode")
parser.add_argument("-p", "--password", required=True, help="Give your password for encode or decode the script")
parser.add_argument("-s", "--save",  help="use this if want to save the output")
parser.add_argument("-r", "--run", action='store_true', help="use this if you to run the script after decoding")
parser.set_defaults(run=False)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'

print(bcolors.OKCYAN+"""
\│/  ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐  \│/      
─ ─  ╚═╗├┤ │  │ │├┬┘├┤   ─ ─      
/│\  ╚═╝└─┘└─┘└─┘┴└─└─┘  /│\      
        \│/  ╔═╗┌─┐┬─┐┬┌─┐┌┬┐  \│/
        ─ ─  ╚═╗│  ├┬┘│├─┘ │   ─ ─
        /│\  ╚═╝└─┘┴└─┴┴   ┴   /│\
        
=========== Cod3d By Md Rasel =============
Github: https://github.com/Mdrasel1230/SecureScript
        """)

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args=parser.parse_args()

def cipherAES(password, iv):
    key = SHA256.new(password).digest()
    return AES.new(key, AES.MODE_CFB, iv)

def encodeX(plaintext, password):
    iv = Random.new().read(AES.block_size)
    return base64.b64encode(iv + cipherAES(password, iv).encrypt(plaintext))

def decodeX(ciphertext, password):
    d = base64.b64decode(ciphertext)
    iv, ciphertext = d[:AES.block_size], d[AES.block_size:]
    return cipherAES(password, iv).decrypt(ciphertext)

if args.encode !=None and args.decode == None and args.save == None and args.run == False: # -e -p
    enc = open(args.encode, "r").read()
    secret = base64.b64encode(enc)
    encX = encodeX(secret, args.password)
    print(encX+"\n")
    print("Save this in txt file with any name!")

elif args.encode !=None and args.decode == None and args.save !=None and args.run == False: # -e -p -s
    enc = open(args.encode, "r").read()
    secret = base64.b64encode(enc)
    encX = encodeX(secret, args.password)
    Template = """
# coding: utf-8
import base64
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import argparse
import sys
import colored
from colored import stylize

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--password", required=True, help="Give your password for decode and run the script")

print(stylize('''
                  ,,__
        ..  ..   / o._)                   .---.
       /--'/--\  \-'||        .----.    .'     '.
      /        \_/ / |      .'      '..'         '-.
    .'\  \__\  __.'.'     .'          i-._
      )\ |  )\ |      _.'
     // \\ // \\
    ||_  \\|_  \\_
    '--' '--'' '--'
=========== Cod3d By Md Rasel =============
Github: https://github.com/Mdrasel1230/SecureScript''', colored.fg("green"))+"\n")

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args=parser.parse_args()

def cipherAES(password, iv):
    key = SHA256.new(password).digest()
    return AES.new(key, AES.MODE_CFB, iv)

def decodeX(ciphertext, password):
    d = base64.b64decode(ciphertext)
    iv, ciphertext = d[:AES.block_size], d[AES.block_size:]
    return cipherAES(password, iv).decrypt(ciphertext)

pd = args.password.encode('utf-8')

decX = decodeX(b'{0}', pd)
decY = base64.b64decode(decX)
eval(compile(decY,'<string>','exec'))
print("\n"+stylize("Execution Done! [+]--(^_^)--[-]", colored.fg("green")))
""".format(encX)
    with open(args.save, 'w') as s:
        s.write(Template)
    print("Saved Done!")

elif args.encode !=None and args.decode != None and args.save !=None and args.run == False: # -e -d -s -p
    print("Please select encode or decode any one option!")

elif args.encode == None and args.decode != None and args.save !=None and args.run == False: # -d -s -p
    dec = open(args.decode, "r").read()
    decX = decodeX(dec, args.password)
    decY = base64.b64decode(decX)
    print(decY+"\n")
    with open(args.save, 'w') as d:
        d.write(decY)
    print("Successfully Decoded By Your Password, Saved Done!")

elif args.encode == None and args.decode != None and args.save !=None and args.run == True: # -d -s -p -r
    dec = open(args.decode, "r").read()
    decX = decodeX(dec, args.password)
    decY = base64.b64decode(decX)
    print(decY+"\n")
    with open(args.save, 'w') as d:
        d.write(decY)
    print("Successfully Decoded By Your Password, Saved Done!"+"\n")
    print("Now it will running..")
    eval(compile(decY,'<string>','exec'))
    print(stylize("Execution Done! [+]--(^_^)--[-]", colored.fg("green")))

elif args.encode == None and args.decode != None and args.save == None and args.run == True: # -d -p -r 
    dec = open(args.decode, "r").read()
    decX = decodeX(dec, args.password)
    decY = base64.b64decode(decX)
    print(decY+"\n")
    print("Save this file with any name end with .py extension!")
    print("Now it will running..")
    eval(compile(decY,'<string>','exec'))
    print(stylize("Execution Done! [+]--(^_^)--[-]", colored.fg("green")))

elif args.encode == None and args.decode != None and args.save == None and args.run == False: # -d -p
    dec = open(args.decode, "r").read()
    decX = decodeX(dec, args.password)
    decY = base64.b64decode(decX)
    print(decY+"\n")
    print("Save this file with any name end with .py extension!")

else:
    print("Something is wrong!")
