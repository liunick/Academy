from clarifai.rest import ClarifaiApp

clarifaiApp = ClarifaiApp(api_key='d1df0d143a3a4e4b8ecb696c0ed9dde4')

'''
urls = ['url1', 'url2']
concepts = ['concept1', 'concept2']
'''
def trainModel(urls, concepts, modelName):
	for url in urls:
		try:
			clarifaiApp.inputs.create_image_from_url(url=url, concepts=concepts)
		except:
			continue	
	try:
		print 'Model %s already exists. New model not created' % modelName
		model = clarifaiApp.models.get(modelName)
	except:
		print 'Model does not exist. Creating model %s' % modelName
		model = clarifaiApp.models.create(modelName, concepts=concepts)
	try:
		model.train()
	except:
		print 'ERROR: Model did not train'

def showAllModels(): 
	for item in clarifaiApp.models.get_all():
		print item.get_info()


#list of all
urls = [
		'https://images.eatthismuch.com/site_media/img/4440_laurabedo_38887c39-cc1c-430d-bd4d-2562c09df8cc.png',
		'http://img-aws.ehowcdn.com/350x235p/photos.demandstudios.com/198/37/fotolia_8334344_XS.jpg',
		'http://s.eatthis-cdn.com/media/images/ext/846505625/rice-cakes.jpg',

	]
concepts = ['Neil']
modelName = 'Friends'
trainModel(urls, concepts, modelName)
showAllModels()