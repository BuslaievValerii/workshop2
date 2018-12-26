def getBrand(smth):

	'''
	This function returns brand of the car which had more owners than others
	Args: smth
	Returns: String
	example: Ford
	'''

	if len(smth)==1:
		return smth[0]['brand']

	if(len(smth[0]['owners'])<len(smth[1]['owners'])):
		smth.pop(0)
	else:
		smth.pop(1)

	return getBrand(smth)

def addOwner(smth_new, smth, name):

	'''
	This function adds name of the new owner to the set of other owners
	Args: smth, smth_new, name
	Returns: Set
	example: {'Bob', 'Boba', 'Biba'}
	'''

	name_add={name}
	brand_needed=getBrand(smth)

	for i in smth_new:
		if(i['brand']==brand_needed):
			owner_list=i['owners']
			owner_list.update(name_add)

	return owner_list

def getNames(smth_new):

	'''
	This function returns set of all the owners of all the cars
	Args: smth_new
	Returns: Set
	example: {'Bob', 'Boba', 'Biba'}
	'''

	names=set({})
	for j in smth_new:
		names.update(j['owners'])
	return names

smth=[
      {
       'brand': 'Ford',
       'model': 'Mustang',
       'year': 1964,
       'owners': {
                  'Bob', 
                  'Boba'
                 }
      },
      {
       'brand': 'Mers',
       'model': 'C500',
       'year': 2000, 
       'owners': {
                  'Bob'
                 }
      },
      {
       'brand': 'Wolksvagen', 
       'model': 'Polo', 
       'year': 2002, 
       'owners': {}
      }
     ]

smth_new=smth[:]

print(getBrand(smth))

name='Biba'
print(addOwner(smth_new, smth, name))

print(getNames(smth_new))