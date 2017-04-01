def read(filename):
	'''it should read the file with 'filename'
	and return it's content.
	'''
	f = open(filename, 'r')
	data = f.read()
	f.close()

	return data 
