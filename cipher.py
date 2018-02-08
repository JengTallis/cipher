'''
cipher.py

A collection of classic ciphers

'''
import argparse
import math


# =============  Define English Alphabets =============
alphabet = ""
for i in range (ord('A'), ord('Z')+1):
	alphabet += chr(i)
alpha_len = len(alphabet)

# ==================== Argument Parser ====================
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", required=True, help="c for caeser, k for keyword, v for virgenere, t for columnar_transposition")
ap.add_argument("-m", "--mode", required=True, help="c for cipher, d for decipher")
ap.add_argument("-k", "--key", required=True, help="cipher key")
ap.add_argument("-s", "--str", required=True, help="string to cipher/decipher")
args = vars(ap.parse_args())


'''
# =============  Keyword Cipher  =============
'''

def key_alpha(key):
	alpha = ""
	for a in alphabet:
		if a not in key:
			alpha += a
	key_alpha = key + alpha
	return key_alpha

def key_cipher(key, string):
	key_a = key_alpha(key)
	cipher = ""
	for s in string:
		cipher += key_a[alphabet.index(s)]
	print(cipher)
	return cipher

def key_decipher(key, cipher):
	key_a= key_alpha(key)
	decipher = ""
	for c in cipher:
		decipher += alphabet[key_a.index(c)]
	print(decipher)
	return decipher


'''
# =============  Caeser Cipher  =============
'''
def caeser_cipher(amt, string):
	cipher = ""
	for s in string:
		shift = (ord(s) + amt) - alpha_len if (ord(s) + amt) > ord('Z') else (ord(s) + amt)
		cipher += chr(shift)
	print(cipher)
	return cipher

def caeser_decipher(amt, string):
	cipher = ""
	for s in string:
		shift =  (ord(s) - amt) + alpha_len if (ord(s) - amt) < ord('A') else (ord(s) - amt)
		cipher += chr(shift)
	print(cipher)
	return cipher

'''
# =============  Virgenere Cipher  =============
'''	
def virg_k(key, p):
	k = ""
	for i in range(len(p)):
		k += key[(i) % len(key)]
	return k

def virgenere_cipher(key, p):		# Ci = (Pi + Ki) % 26
	k = virg_k(key, p)
	cipher = ""
	for i in range(len(p)):
		cipher += alphabet[(alphabet.index(p[i]) + alphabet.index(k[i])) % alpha_len]
	print(cipher)
	return cipher

def virgenere_decipher(key, c):		# Pi = (Ci - Ki) % 26
	k = virg_k(key, c)
	p = ""
	for i in range(len(c)):
		p += alphabet[(alphabet.index(c[i]) - alphabet.index(k[i])) % alpha_len]
	print(p)
	return p

'''
# =============  columnar_transposition Cipher  =============
'''	
def cipher_matrix(key, p):
	w = len(key)
	h = math.ceil(len(p)/len(key))
	mat = [['' for i in range(w)] for j in range(h)]
	for x in range(len(p)):
		j = math.floor(x/len(key))
		i = x % len(key)
		mat[j][i] = p[x]
	return mat

def decipher_matrix(key_ord, c):
	w = len(key_ord)
	h = math.ceil(len(c)/len(key_ord))
	ls = [math.floor(len(c)/len(key_ord))] * w
	r = len(c) % w
	if r > 0:
		for i in range(r):
			ls[i] += 1
	mat = [['' for i in range(w)] for j in range(h)]
	x = 0
	for i in range(len(key_ord)):
		for j in range(ls[key_ord.index(i)]):
			mat[j][key_ord.index(i)] = c[x]
			x += 1
	return mat

def sort_str(s):
	ss = []
	for c in s:
		ss.append(c)
	ss.sort()
	idx = []
	for c in ss:
		idx.append(s.index(c))
	return idx

def columnar_transposition_cipher(key, p):
	mat = cipher_matrix(key, p)
	key_ord = sort_str(key)
	cipher = ""
	for i in range(len(key)):
		for j in range(len(mat)):
			cipher += mat[j][key_ord.index(i)]
	print(cipher)
	return cipher

def columnar_transposition_decipher(key, c):
	key_ord = sort_str(key)
	mat = decipher_matrix(key_ord, c)
	p = ""
	for x in range(len(c)):
		j = math.floor(x/len(key))
		i = x % len(key)
		p += mat[j][i]
	print(p)
	return p
'''
# ==================== Cipher Worker ====================
t: c for caeser, k for keyword, v for virgenere, t for columnar_transposition
m: c for cipher, d for decipher 
'''
def cipher_worker(t,m,k,s):
	if t == 'c':	# caeser
		if m == 'c':
			caeser_cipher(int(k),s)
		elif m == 'd':
			caeser_decipher(int(k),s)
		else:
			print("Invalid mode")
	elif t == 'k':
		if m == 'c':
			key_cipher(k,s)
		elif m == 'd':
			key_decipher(k,s)
		else:
			print("Invalid mode")
	elif t == 'v':
		if m == 'c':
			virgenere_cipher(k,s)
		elif m == 'd':
			virgenere_decipher(k,s)
		else:
			print("Invalid mode")
	elif t == 't':
		if m == 'c':
			columnar_transposition_cipher(k,s)
		elif m == 'd':
			columnar_transposition_decipher(k,s)
		else:
			print("Invalid mode")
	else:
		print("Invalid cipher type")


t = args["type"]
m = args["mode"]
k = args["key"]
s = args["str"]
cipher_worker(t,m,k,s)


#columnar_transposition_cipher("CAT", "ILOVECHICKENANDSOUP")
#columnar_transposition_decipher("CAT", "LEIENOIVHKASPOCCNDU")

#decipher_matrix([1,0,2], "LEIENOIVHKASPOCCNDU")

#virgenere_cipher("LEMON", "ATTACKATDAWN")
#virgenere_decipher("LEMON", "LXFOPVEFRNHR")

#key_cipher("PEIHONG", "HHN")
#caeser_cipher(3, "HELLO")


