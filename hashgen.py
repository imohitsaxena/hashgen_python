import os
import hashlib
import sys

print("Please select Hashing Method")
print("1. SHA 2")
print("2. SHA 3")
sha_type = input()

if not(sha_type == '1' or sha_type == '2'):
	print("Invalid Input. Exiting.")
	exit()

print("Select size")
print("1. 224")
print("2. 256")
print("3. 384")
print("4. 512")
sha_type=sha_type + input()

if sha_type == '11':
	hash_algo = "sha224"
elif sha_type == '12':
	hash_algo = "sha256"
elif sha_type == '13':
	hash_algo = "sha384"
elif sha_type == '14':
	hash_algo = "sha512"
elif sha_type == '21':
	hash_algo = "sha3_224"
elif sha_type == '22':
	hash_algo = "sha3_256"
elif sha_type == '23':
	hash_algo = "sha3_384"
elif sha_type == '24':
	hash_algo = "sha3_512"
else:
	print("Invalid Input. Exiting.")
	exit()

if not(hash_algo in hashlib.algorithms_guaranteed):
	print("Hashing method not supported by Python Version " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro) + ".")
	print("Please upgrade to Python 3.6.8 or above.")
	exit()

count = 0
while True:
	if os.path.exists('hashes.txt'):
		count = count + 1
		if not os.path.exists('hashes_' + str(count) + '.txt'):
			out_file_name = 'hashes_' + str(count) + '.txt'
			break
	else:
		out_file_name = 'hashes.txt'
		break

f_out = open(out_file_name, 'a')

f_out.write('File : ' + hash_algo + '\n')

for f in os.listdir():
	if os.path.isfile(f):
		a_file = open(f, 'rb')
		content = a_file.read()
		hash_val = hashlib.new(hash_algo,content)
		f_out.write('\n' + f + ' : ' + hash_val.hexdigest())
f_out.close()
print('Done')
