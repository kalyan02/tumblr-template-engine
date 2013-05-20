import tumblr_engine as te
import json

jsonDataRaw = open("data/demoData.json",'r')
jsonData = json.load( jsonDataRaw )
output = None
try:
	# compile the template
	tpl = te.Template( te.content )
	tpl.compile()
	
	# This helps map data from Tumblr's json api response to template tags
	# Fetch the default template first
	contextTemplate = te.defaultContextMapperTemplate()
	# Update the template to match the data
	contextDataMap = te.ContextDataMapper( jsonData['response'], contextTemplate )
	# Render the template with the context map 
	output = tpl.render(contextDataMap)
except Exception, e:
	print 'Template Compile Error : ' + e.message


if output:
	print len(output)
	print output
