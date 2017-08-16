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
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/16640621_1407871549237242_8731785688204173502_n.jpg?oh=5525a02bd34ac7f65d6bb0a54ac4e4f4&oe=59F033FA',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/14708219_1233740213334125_731178637874495198_n.jpg?oh=52105b2e075589444e0c6cfca755d975&oe=59EFCEB2',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/14291921_1252052744819124_8336105302969309541_n.jpg?oh=459016e414efc7806f3bf0fa13383688&oe=5A306660',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/14141903_1236184579739274_7991324806780006796_n.jpg?oh=1780f0e08ca0dd27d84c7ee297a6018e&oe=5A1D73E2',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/14051795_1236184316405967_2865724824847652055_n.jpg?oh=3873b418d711a461c92d9aaf85bfb6a4&oe=5A2A87EF',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/13886902_1817843611783778_1673974955086866955_n.jpg?oh=fecc4646295949d404e935b25e40e9a1&oe=5A2D8460',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-1/17201271_10210800547482891_3681294658914218944_n.jpg?oh=78e33837e1e26035e699ec0c5f8ee29e&oe=5A32CBF5',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/16729009_10210573665530984_7145416717855968866_n.jpg?oh=b407f448138211fbdcc6ac7e25f864df&oe=5A1D7F86',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/20729639_10212344408958463_6202965616116237856_n.jpg?oh=069a8070fac76c9a04d27192506f4cfb&oe=5A336D1E',
		'https://scontent.fdet1-1.fna.fbcdn.net/v/t1.0-9/14184459_10209001400505341_4583114924133526486_n.jpg?oh=936b6e0dc37033968630bb3831e53b73&oe=5A1F79F1',
	]
concepts = ['Neil']
modelName = 'Friends'
trainModel(urls, concepts, modelName)