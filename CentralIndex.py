#!/usr/bin/python

'''
Central Index

The Central Index Python Library

@package 	CentralIndex
@author  	Daniel Ord
@link    	http://centralindex.com
@since   	Version 1.0
'''

class CentralIndex:

	'''
	Constructor - store the api key in the class
	
	@param apikey - the user's API key
	@param debugMode - whether to output debugging or not
	@return - the data from the api
	'''
	
	def __init__(self, apikey):
		global apiKey 
		apiKey = apikey

	'''
	Perform curl request
	
	@param method - the HTTP method to do
	@param path - the relative path to visit
	@param data - an array of parameters to pass
	@return - the data from the api
	'''

	def doCurl(self, method, path, data):

		debugMode = False
		
		api_url = "http://api.centralindex.com/v1"
		
		data['api_key'] = apiKey

		import requests
		url = api_url + path
		
		if method == "GET":
			
			r = requests.get(url, params=data)
			
		else:
			
			if(method == "PUT"):
				r = requests.put(url, data=data)
			if(method == "POST"):
				r = requests.post(url, data=data)
			if(method == "DELETE"):
				r = requests.delete(url, data=data)
						
		if(debugMode):
			print "METHOD = %s\n" % method
			print "URL = %s\n" % url
			print ("Data:\n")
			print data
			print "Output:\n"        
			print r.text
		
		return r.text
		
		
	'''
	Get the activity from the collection
	@param type - The activity type: add, claim, special offer, image, video, description, testimonial
	@param country - The country to filter by
	@param latitude_1 - The latitude_1 to filter by
	@param longitude_1 - The longitude_1 to filter by
	@param latitude_2 - The latitude_2 to filter by
	@param longitude_2 - The longitude_2 to filter by
	@param number_results - The number_results to filter by
	@param unique_action - Return only the most recent instance of this action?
	@return - the data from the api
	'''
	def getActivity_stream(self,type='',country='',latitude_1='',longitude_1='',latitude_2='',longitude_2='',number_results='',unique_action=''):
		params = {}
		if(type != ''): 
			params['type'] = type
		if(country != ''): 
			params['country'] = country
		if(latitude_1 != ''): 
			params['latitude_1'] = latitude_1
		if(longitude_1 != ''): 
			params['longitude_1'] = longitude_1
		if(latitude_2 != ''): 
			params['latitude_2'] = latitude_2
		if(longitude_2 != ''): 
			params['longitude_2'] = longitude_2
		if(number_results != ''): 
			params['number_results'] = number_results
		if(unique_action != ''): 
			params['unique_action'] = unique_action
		return self.doCurl("GET","/activity_stream",params)
  


	'''
	When we get some activity make a record of it
	@param entity_id - The entity to pull
	@param entity_name - The entity name this entry refers to
	@param type - The activity type.
	@param country - The country for the activity
	@param longitude - The longitude for teh activity
	@param latitude - The latitude for teh activity
	@return - the data from the api
	'''
	def postActivity_stream(self,entity_id='',entity_name='',type='',country='',longitude='',latitude=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(entity_name != ''): 
			params['entity_name'] = entity_name
		if(type != ''): 
			params['type'] = type
		if(country != ''): 
			params['country'] = country
		if(longitude != ''): 
			params['longitude'] = longitude
		if(latitude != ''): 
			params['latitude'] = latitude
		return self.doCurl("POST","/activity_stream",params)
  


	'''
	Get all advertisers that have been updated from a give date for a given reseller
	@param from_date
	@param country
	@return - the data from the api
	'''
	def getAdvertiserUpdated(self,from_date='',country=''):
		params = {}
		if(from_date != ''): 
			params['from_date'] = from_date
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/advertiser/updated",params)
  


	'''
	Get all advertisers that have been updated from a give date for a given publisher
	@param publisher_id
	@param from_date
	@param country
	@return - the data from the api
	'''
	def getAdvertiserUpdatedBy_publisher(self,publisher_id='',from_date='',country=''):
		params = {}
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(from_date != ''): 
			params['from_date'] = from_date
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/advertiser/updated/by_publisher",params)
  


	'''
	The search matches a category name on a given string and language.
	@param str - A string to search against, E.g. Plumbers e.g. but
	@param language - An ISO compatible language code, E.g. en e.g. en
	@return - the data from the api
	'''
	def getAutocompleteCategory(self,str='',language=''):
		params = {}
		if(str != ''): 
			params['str'] = str
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/autocomplete/category",params)
  


	'''
	The search matches a category name or synonym on a given string and language.
	@param str - A string to search against, E.g. Plumbers e.g. but
	@param language - An ISO compatible language code, E.g. en e.g. en
	@return - the data from the api
	'''
	def getAutocompleteKeyword(self,str='',language=''):
		params = {}
		if(str != ''): 
			params['str'] = str
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/autocomplete/keyword",params)
  


	'''
	The search matches a location name or synonym on a given string and language.
	@param str - A string to search against, E.g. Dub e.g. dub
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param language - An ISO compatible language code, E.g. en e.g. en
	@return - the data from the api
	'''
	def getAutocompleteLocation(self,str='',country='',language=''):
		params = {}
		if(str != ''): 
			params['str'] = str
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/autocomplete/location",params)
  


	'''
	The search matches a location name or synonym on a given string and language.
	@param str - A string to search against, E.g. Middle e.g. dub
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param resolution
	@return - the data from the api
	'''
	def getAutocompleteLocationBy_resolution(self,str='',country='',resolution=''):
		params = {}
		if(str != ''): 
			params['str'] = str
		if(country != ''): 
			params['country'] = country
		if(resolution != ''): 
			params['resolution'] = resolution
		return self.doCurl("GET","/autocomplete/location/by_resolution",params)
  


	'''
	Create a new business entity with all it's objects
	@param name
	@param building_number
	@param address1
	@param address2
	@param address3
	@param district
	@param town
	@param county
	@param province
	@param postcode
	@param country
	@param latitude
	@param longitude
	@param timezone
	@param telephone_number
	@param additional_telephone_number
	@param email
	@param website
	@param category_id
	@param category_type
	@param do_not_display
	@param referrer_url
	@param referrer_name
	@return - the data from the api
	'''
	def putBusiness(self,name='',building_number='',address1='',address2='',address3='',district='',town='',county='',province='',postcode='',country='',latitude='',longitude='',timezone='',telephone_number='',additional_telephone_number='',email='',website='',category_id='',category_type='',do_not_display='',referrer_url='',referrer_name=''):
		params = {}
		if(name != ''): 
			params['name'] = name
		if(building_number != ''): 
			params['building_number'] = building_number
		if(address1 != ''): 
			params['address1'] = address1
		if(address2 != ''): 
			params['address2'] = address2
		if(address3 != ''): 
			params['address3'] = address3
		if(district != ''): 
			params['district'] = district
		if(town != ''): 
			params['town'] = town
		if(county != ''): 
			params['county'] = county
		if(province != ''): 
			params['province'] = province
		if(postcode != ''): 
			params['postcode'] = postcode
		if(country != ''): 
			params['country'] = country
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		if(timezone != ''): 
			params['timezone'] = timezone
		if(telephone_number != ''): 
			params['telephone_number'] = telephone_number
		if(additional_telephone_number != ''): 
			params['additional_telephone_number'] = additional_telephone_number
		if(email != ''): 
			params['email'] = email
		if(website != ''): 
			params['website'] = website
		if(category_id != ''): 
			params['category_id'] = category_id
		if(category_type != ''): 
			params['category_type'] = category_type
		if(do_not_display != ''): 
			params['do_not_display'] = do_not_display
		if(referrer_url != ''): 
			params['referrer_url'] = referrer_url
		if(referrer_name != ''): 
			params['referrer_name'] = referrer_name
		return self.doCurl("PUT","/business",params)
  


	'''
	Returns business tool that matches a given tool id
	@param tool_id
	@return - the data from the api
	'''
	def getBusiness_tool(self,tool_id=''):
		params = {}
		if(tool_id != ''): 
			params['tool_id'] = tool_id
		return self.doCurl("GET","/business_tool",params)
  


	'''
	Delete a business tool with a specified tool_id
	@param tool_id
	@return - the data from the api
	'''
	def deleteBusiness_tool(self,tool_id=''):
		params = {}
		if(tool_id != ''): 
			params['tool_id'] = tool_id
		return self.doCurl("DELETE","/business_tool",params)
  


	'''
	Update/Add a Business Tool
	@param tool_id
	@param country
	@param headline
	@param description
	@param link_url
	@param active
	@return - the data from the api
	'''
	def postBusiness_tool(self,tool_id='',country='',headline='',description='',link_url='',active=''):
		params = {}
		if(tool_id != ''): 
			params['tool_id'] = tool_id
		if(country != ''): 
			params['country'] = country
		if(headline != ''): 
			params['headline'] = headline
		if(description != ''): 
			params['description'] = description
		if(link_url != ''): 
			params['link_url'] = link_url
		if(active != ''): 
			params['active'] = active
		return self.doCurl("POST","/business_tool",params)
  


	'''
	Returns active business tools for a specific masheryid in a given country
	@param country
	@return - the data from the api
	'''
	def getBusiness_toolBy_masheryid(self,country=''):
		params = {}
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/business_tool/by_masheryid",params)
  


	'''
	Assigns a Business Tool image
	@param tool_id
	@param filedata
	@return - the data from the api
	'''
	def postBusiness_toolImage(self,tool_id='',filedata=''):
		params = {}
		if(tool_id != ''): 
			params['tool_id'] = tool_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/business_tool/image",params)
  


	'''
	With a known category id, an category object can be added.
	@param category_id
	@param language
	@param name
	@return - the data from the api
	'''
	def putCategory(self,category_id='',language='',name=''):
		params = {}
		if(category_id != ''): 
			params['category_id'] = category_id
		if(language != ''): 
			params['language'] = language
		if(name != ''): 
			params['name'] = name
		return self.doCurl("PUT","/category",params)
  


	'''
	Returns the supplied wolf category object by fetching the supplied category_id from our categories object.
	@param category_id
	@return - the data from the api
	'''
	def getCategory(self,category_id=''):
		params = {}
		if(category_id != ''): 
			params['category_id'] = category_id
		return self.doCurl("GET","/category",params)
  


	'''
	Returns all Central Index categories and associated data
	@return - the data from the api
	'''
	def getCategoryAll(self):
		params = {}
		return self.doCurl("GET","/category/all",params)
  


	'''
	With a known category id, a mapping object can be added.
	@param category_id
	@param type
	@param id
	@param name
	@return - the data from the api
	'''
	def postCategoryMappings(self,category_id='',type='',id='',name=''):
		params = {}
		if(category_id != ''): 
			params['category_id'] = category_id
		if(type != ''): 
			params['type'] = type
		if(id != ''): 
			params['id'] = id
		if(name != ''): 
			params['name'] = name
		return self.doCurl("POST","/category/mappings",params)
  


	'''
	With a known category id, a mapping object can be deleted.
	@param category_id
	@param category_type
	@param mapped_id
	@return - the data from the api
	'''
	def deleteCategoryMappings(self,category_id='',category_type='',mapped_id=''):
		params = {}
		if(category_id != ''): 
			params['category_id'] = category_id
		if(category_type != ''): 
			params['category_type'] = category_type
		if(mapped_id != ''): 
			params['mapped_id'] = mapped_id
		return self.doCurl("DELETE","/category/mappings",params)
  


	'''
	Allows a category object to merged with another
	@param from
	@param to
	@return - the data from the api
	'''
	def postCategoryMerge(self,from2='',to=''):
		params = {}
		if(from2 != ''): 
			params['from2'] = from2
		if(to != ''): 
			params['to'] = to
		return self.doCurl("POST","/category/merge",params)
  


	'''
	With a known category id, a synonyms object can be removed.
	@param category_id
	@param synonym
	@param language
	@return - the data from the api
	'''
	def deleteCategorySynonym(self,category_id='',synonym='',language=''):
		params = {}
		if(category_id != ''): 
			params['category_id'] = category_id
		if(synonym != ''): 
			params['synonym'] = synonym
		if(language != ''): 
			params['language'] = language
		return self.doCurl("DELETE","/category/synonym",params)
  


	'''
	With a known category id, an synonym object can be added.
	@param category_id
	@param synonym
	@param language
	@return - the data from the api
	'''
	def postCategorySynonym(self,category_id='',synonym='',language=''):
		params = {}
		if(category_id != ''): 
			params['category_id'] = category_id
		if(synonym != ''): 
			params['synonym'] = synonym
		if(language != ''): 
			params['language'] = language
		return self.doCurl("POST","/category/synonym",params)
  


	'''
	Update/Add a country
	@param country_id
	@param name
	@param synonyms
	@param continentName
	@param continent
	@param geonameId
	@param dbpediaURL
	@param freebaseURL
	@param population
	@param currencyCode
	@param languages
	@param areaInSqKm
	@param capital
	@param east
	@param west
	@param north
	@param south
	@param claimPrice
	@param claimMethods
	@param twilio_sms
	@param twilio_phone
	@param twilio_voice
	@param currency_symbol - the symbol of this country's currency
	@param currency_symbol_html - the html version of the symbol of this country's currency
	@param postcodeLookupActive - Whether the lookup is activated for this country
	@param addressFields - Whether fields are activated for this country
	@param addressMatching - The configurable matching algorithm
	@param dateFormat - The format of the date for this country
	@param iso_3166_alpha_3
	@param iso_3166_numeric
	@return - the data from the api
	'''
	def postCountry(self,country_id='',name='',synonyms='',continentName='',continent='',geonameId='',dbpediaURL='',freebaseURL='',population='',currencyCode='',languages='',areaInSqKm='',capital='',east='',west='',north='',south='',claimPrice='',claimMethods='',twilio_sms='',twilio_phone='',twilio_voice='',currency_symbol='',currency_symbol_html='',postcodeLookupActive='',addressFields='',addressMatching='',dateFormat='',iso_3166_alpha_3='',iso_3166_numeric=''):
		params = {}
		if(country_id != ''): 
			params['country_id'] = country_id
		if(name != ''): 
			params['name'] = name
		if(synonyms != ''): 
			params['synonyms'] = synonyms
		if(continentName != ''): 
			params['continentName'] = continentName
		if(continent != ''): 
			params['continent'] = continent
		if(geonameId != ''): 
			params['geonameId'] = geonameId
		if(dbpediaURL != ''): 
			params['dbpediaURL'] = dbpediaURL
		if(freebaseURL != ''): 
			params['freebaseURL'] = freebaseURL
		if(population != ''): 
			params['population'] = population
		if(currencyCode != ''): 
			params['currencyCode'] = currencyCode
		if(languages != ''): 
			params['languages'] = languages
		if(areaInSqKm != ''): 
			params['areaInSqKm'] = areaInSqKm
		if(capital != ''): 
			params['capital'] = capital
		if(east != ''): 
			params['east'] = east
		if(west != ''): 
			params['west'] = west
		if(north != ''): 
			params['north'] = north
		if(south != ''): 
			params['south'] = south
		if(claimPrice != ''): 
			params['claimPrice'] = claimPrice
		if(claimMethods != ''): 
			params['claimMethods'] = claimMethods
		if(twilio_sms != ''): 
			params['twilio_sms'] = twilio_sms
		if(twilio_phone != ''): 
			params['twilio_phone'] = twilio_phone
		if(twilio_voice != ''): 
			params['twilio_voice'] = twilio_voice
		if(currency_symbol != ''): 
			params['currency_symbol'] = currency_symbol
		if(currency_symbol_html != ''): 
			params['currency_symbol_html'] = currency_symbol_html
		if(postcodeLookupActive != ''): 
			params['postcodeLookupActive'] = postcodeLookupActive
		if(addressFields != ''): 
			params['addressFields'] = addressFields
		if(addressMatching != ''): 
			params['addressMatching'] = addressMatching
		if(dateFormat != ''): 
			params['dateFormat'] = dateFormat
		if(iso_3166_alpha_3 != ''): 
			params['iso_3166_alpha_3'] = iso_3166_alpha_3
		if(iso_3166_numeric != ''): 
			params['iso_3166_numeric'] = iso_3166_numeric
		return self.doCurl("POST","/country",params)
  


	'''
	Fetching a country
	@param country_id
	@return - the data from the api
	'''
	def getCountry(self,country_id=''):
		params = {}
		if(country_id != ''): 
			params['country_id'] = country_id
		return self.doCurl("GET","/country",params)
  


	'''
	For a given country add/update a background image to show in the add/edit path
	@param country_id
	@param filedata
	@param backgroundImageAttr
	@return - the data from the api
	'''
	def postCountryBackgroundImage(self,country_id='',filedata='',backgroundImageAttr=''):
		params = {}
		if(country_id != ''): 
			params['country_id'] = country_id
		if(filedata != ''): 
			params['filedata'] = filedata
		if(backgroundImageAttr != ''): 
			params['backgroundImageAttr'] = backgroundImageAttr
		return self.doCurl("POST","/country/backgroundImage",params)
  


	'''
	For a given country add/update a social login background image to show in the add/edit path
	@param country_id
	@param filedata
	@return - the data from the api
	'''
	def postCountrySocialLoginImage(self,country_id='',filedata=''):
		params = {}
		if(country_id != ''): 
			params['country_id'] = country_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/country/socialLoginImage",params)
  


	'''
	Send an email via amazon
	@param to_email_address - The email address to send the email too
	@param reply_email_address - The email address to add in the reply to field
	@param source_account - The source account to send the email from
	@param subject - The subject for the email
	@param body - The body for the email
	@param html_body - If the body of the email is html
	@return - the data from the api
	'''
	def postEmail(self,to_email_address='',reply_email_address='',source_account='',subject='',body='',html_body=''):
		params = {}
		if(to_email_address != ''): 
			params['to_email_address'] = to_email_address
		if(reply_email_address != ''): 
			params['reply_email_address'] = reply_email_address
		if(source_account != ''): 
			params['source_account'] = source_account
		if(subject != ''): 
			params['subject'] = subject
		if(body != ''): 
			params['body'] = body
		if(html_body != ''): 
			params['html_body'] = html_body
		return self.doCurl("POST","/email",params)
  


	'''
	This entity isn't really supported anymore. You probably want PUT /business. Only to be used for testing.
	@param type
	@param scope
	@param country
	@param trust
	@param our_data
	@return - the data from the api
	'''
	def putEntity(self,type='',scope='',country='',trust='',our_data=''):
		params = {}
		if(type != ''): 
			params['type'] = type
		if(scope != ''): 
			params['scope'] = scope
		if(country != ''): 
			params['country'] = country
		if(trust != ''): 
			params['trust'] = trust
		if(our_data != ''): 
			params['our_data'] = our_data
		return self.doCurl("PUT","/entity",params)
  


	'''
	Allows a whole entity to be pulled from the datastore by its unique id
	@param entity_id - The unique entity ID e.g. 379236608286720
	@return - the data from the api
	'''
	def getEntity(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/entity",params)
  


	'''
	With a known entity id, an add can be updated.
	@param entity_id
	@param add_referrer_url
	@param add_referrer_name
	@return - the data from the api
	'''
	def postEntityAdd(self,entity_id='',add_referrer_url='',add_referrer_name=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(add_referrer_url != ''): 
			params['add_referrer_url'] = add_referrer_url
		if(add_referrer_name != ''): 
			params['add_referrer_name'] = add_referrer_name
		return self.doCurl("POST","/entity/add",params)
  


	'''
	Allows an advertiser object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityAdvertiser(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/advertiser",params)
  


	'''
	Expires an advertiser from and entity
	@param entity_id
	@param publisher_id
	@param reseller_ref
	@param reseller_agent_id
	@return - the data from the api
	'''
	def postEntityAdvertiserCancel(self,entity_id='',publisher_id='',reseller_ref='',reseller_agent_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(reseller_ref != ''): 
			params['reseller_ref'] = reseller_ref
		if(reseller_agent_id != ''): 
			params['reseller_agent_id'] = reseller_agent_id
		return self.doCurl("POST","/entity/advertiser/cancel",params)
  


	'''
	With a known entity id, a advertiser is added
	@param entity_id
	@param tags
	@param locations
	@param max_tags
	@param max_locations
	@param expiry_date
	@param is_national
	@param language
	@param reseller_ref
	@param reseller_agent_id
	@param publisher_id
	@return - the data from the api
	'''
	def postEntityAdvertiserCreate(self,entity_id='',tags='',locations='',max_tags='',max_locations='',expiry_date='',is_national='',language='',reseller_ref='',reseller_agent_id='',publisher_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(tags != ''): 
			params['tags'] = tags
		if(locations != ''): 
			params['locations'] = locations
		if(max_tags != ''): 
			params['max_tags'] = max_tags
		if(max_locations != ''): 
			params['max_locations'] = max_locations
		if(expiry_date != ''): 
			params['expiry_date'] = expiry_date
		if(is_national != ''): 
			params['is_national'] = is_national
		if(language != ''): 
			params['language'] = language
		if(reseller_ref != ''): 
			params['reseller_ref'] = reseller_ref
		if(reseller_agent_id != ''): 
			params['reseller_agent_id'] = reseller_agent_id
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		return self.doCurl("POST","/entity/advertiser/create",params)
  


	'''
	Adds/removes locations
	@param entity_id
	@param gen_id
	@param locations_to_add
	@param locations_to_remove
	@return - the data from the api
	'''
	def postEntityAdvertiserLocation(self,entity_id='',gen_id='',locations_to_add='',locations_to_remove=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		if(locations_to_add != ''): 
			params['locations_to_add'] = locations_to_add
		if(locations_to_remove != ''): 
			params['locations_to_remove'] = locations_to_remove
		return self.doCurl("POST","/entity/advertiser/location",params)
  


	'''
	Renews an advertiser from an entity
	@param entity_id
	@param expiry_date
	@param publisher_id
	@param reseller_ref
	@param reseller_agent_id
	@return - the data from the api
	'''
	def postEntityAdvertiserRenew(self,entity_id='',expiry_date='',publisher_id='',reseller_ref='',reseller_agent_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(expiry_date != ''): 
			params['expiry_date'] = expiry_date
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(reseller_ref != ''): 
			params['reseller_ref'] = reseller_ref
		if(reseller_agent_id != ''): 
			params['reseller_agent_id'] = reseller_agent_id
		return self.doCurl("POST","/entity/advertiser/renew",params)
  


	'''
	Allows the removal or insertion of tags into an advertiser object
	@param gen_id - The gen_id of this advertiser
	@param entity_id - The entity_id of the advertiser
	@param language - The tag language to alter
	@param tags_to_add - The tags to add
	@param tags_to_remove - The tags to remove
	@return - the data from the api
	'''
	def postEntityAdvertiserTag(self,gen_id='',entity_id='',language='',tags_to_add='',tags_to_remove=''):
		params = {}
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(language != ''): 
			params['language'] = language
		if(tags_to_add != ''): 
			params['tags_to_add'] = tags_to_add
		if(tags_to_remove != ''): 
			params['tags_to_remove'] = tags_to_remove
		return self.doCurl("POST","/entity/advertiser/tag",params)
  


	'''
	With a known entity id, an advertiser is updated
	@param entity_id
	@param tags
	@param locations
	@param extra_tags
	@param extra_locations
	@param is_national
	@param language
	@param reseller_ref
	@param reseller_agent_id
	@param publisher_id
	@return - the data from the api
	'''
	def postEntityAdvertiserUpsell(self,entity_id='',tags='',locations='',extra_tags='',extra_locations='',is_national='',language='',reseller_ref='',reseller_agent_id='',publisher_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(tags != ''): 
			params['tags'] = tags
		if(locations != ''): 
			params['locations'] = locations
		if(extra_tags != ''): 
			params['extra_tags'] = extra_tags
		if(extra_locations != ''): 
			params['extra_locations'] = extra_locations
		if(is_national != ''): 
			params['is_national'] = is_national
		if(language != ''): 
			params['language'] = language
		if(reseller_ref != ''): 
			params['reseller_ref'] = reseller_ref
		if(reseller_agent_id != ''): 
			params['reseller_agent_id'] = reseller_agent_id
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		return self.doCurl("POST","/entity/advertiser/upsell",params)
  


	'''
	Search for matching entities that are advertisers and return a random selection upto the limit requested
	@param tag - The word or words the advertiser is to appear for in searches
	@param where - The location to get results for. E.g. Dublin
	@param limit - The number of advertisers that are to be returned
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getEntityAdvertisers(self,tag='',where='',limit='',country='',language=''):
		params = {}
		if(tag != ''): 
			params['tag'] = tag
		if(where != ''): 
			params['where'] = where
		if(limit != ''): 
			params['limit'] = limit
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/advertisers",params)
  


	'''
	With a known entity id, an affiliate link object can be added.
	@param entity_id
	@param affiliate_name
	@param affiliate_link
	@param affiliate_message
	@param affiliate_logo
	@return - the data from the api
	'''
	def postEntityAffiliate_link(self,entity_id='',affiliate_name='',affiliate_link='',affiliate_message='',affiliate_logo=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(affiliate_name != ''): 
			params['affiliate_name'] = affiliate_name
		if(affiliate_link != ''): 
			params['affiliate_link'] = affiliate_link
		if(affiliate_message != ''): 
			params['affiliate_message'] = affiliate_message
		if(affiliate_logo != ''): 
			params['affiliate_logo'] = affiliate_logo
		return self.doCurl("POST","/entity/affiliate_link",params)
  


	'''
	Allows an affiliate link object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityAffiliate_link(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/affiliate_link",params)
  


	'''
	With a known entity id, an background object can be added. There can however only be one background object.
	@param entity_id
	@param number_of_employees
	@param turnover
	@param net_profit
	@param vat_number
	@param duns_number
	@param registered_company_number
	@return - the data from the api
	'''
	def postEntityBackground(self,entity_id='',number_of_employees='',turnover='',net_profit='',vat_number='',duns_number='',registered_company_number=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(number_of_employees != ''): 
			params['number_of_employees'] = number_of_employees
		if(turnover != ''): 
			params['turnover'] = turnover
		if(net_profit != ''): 
			params['net_profit'] = net_profit
		if(vat_number != ''): 
			params['vat_number'] = vat_number
		if(duns_number != ''): 
			params['duns_number'] = duns_number
		if(registered_company_number != ''): 
			params['registered_company_number'] = registered_company_number
		return self.doCurl("POST","/entity/background",params)
  


	'''
	Uploads a CSV file of known format and bulk inserts into DB
	@param filedata
	@return - the data from the api
	'''
	def postEntityBulkCsv(self,filedata=''):
		params = {}
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/entity/bulk/csv",params)
  


	'''
	Shows the current status of a bulk upload
	@param upload_id
	@return - the data from the api
	'''
	def getEntityBulkCsvStatus(self,upload_id=''):
		params = {}
		if(upload_id != ''): 
			params['upload_id'] = upload_id
		return self.doCurl("GET","/entity/bulk/csv/status",params)
  


	'''
	Uploads a JSON file of known format and bulk inserts into DB
	@param data
	@return - the data from the api
	'''
	def postEntityBulkJson(self,data=''):
		params = {}
		if(data != ''): 
			params['data'] = data
		return self.doCurl("POST","/entity/bulk/json",params)
  


	'''
	Shows the current status of a bulk JSON upload
	@param upload_id
	@return - the data from the api
	'''
	def getEntityBulkJsonStatus(self,upload_id=''):
		params = {}
		if(upload_id != ''): 
			params['upload_id'] = upload_id
		return self.doCurl("GET","/entity/bulk/json/status",params)
  


	'''
	Get all entities within a specified group
	@param group_id
	@return - the data from the api
	'''
	def getEntityBy_groupid(self,group_id=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		return self.doCurl("GET","/entity/by_groupid",params)
  


	'''
	uncontributes a given entities supplier content and makes the entity inactive if the entity is un-usable
	@param entity_id - The entity to pull
	@param supplier_masheryid - The suppliers masheryid to match
	@param supplier_id - The supplier id to match
	@param supplier_user_id - The user id to match
	@return - the data from the api
	'''
	def deleteEntityBy_supplier(self,entity_id='',supplier_masheryid='',supplier_id='',supplier_user_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(supplier_masheryid != ''): 
			params['supplier_masheryid'] = supplier_masheryid
		if(supplier_id != ''): 
			params['supplier_id'] = supplier_id
		if(supplier_user_id != ''): 
			params['supplier_user_id'] = supplier_user_id
		return self.doCurl("DELETE","/entity/by_supplier",params)
  


	'''
	Fetches the documents that match the given masheryid and supplier_id
	@param supplier_id - The Supplier ID
	@return - the data from the api
	'''
	def getEntityBy_supplier_id(self,supplier_id=''):
		params = {}
		if(supplier_id != ''): 
			params['supplier_id'] = supplier_id
		return self.doCurl("GET","/entity/by_supplier_id",params)
  


	'''
	Get all entiies claimed by a specific user
	@param user_id - The unique user ID of the user with claimed entities e.g. 379236608286720
	@return - the data from the api
	'''
	def getEntityBy_user_id(self,user_id=''):
		params = {}
		if(user_id != ''): 
			params['user_id'] = user_id
		return self.doCurl("GET","/entity/by_user_id",params)
  


	'''
	With a known entity id, an category object can be added.
	@param entity_id
	@param category_id
	@param category_type
	@return - the data from the api
	'''
	def postEntityCategory(self,entity_id='',category_id='',category_type=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(category_id != ''): 
			params['category_id'] = category_id
		if(category_type != ''): 
			params['category_type'] = category_type
		return self.doCurl("POST","/entity/category",params)
  


	'''
	Allows a category object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityCategory(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/category",params)
  


	'''
	Fetches the changelog documents that match the given entity_id
	@param entity_id
	@return - the data from the api
	'''
	def getEntityChangelog(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/entity/changelog",params)
  


	'''
	Allow an entity to be claimed by a valid user
	@param entity_id
	@param claimed_user_id
	@param claimed_date
	@param claim_method
	@param phone_number
	@param referrer_url
	@param referrer_name
	@return - the data from the api
	'''
	def postEntityClaim(self,entity_id='',claimed_user_id='',claimed_date='',claim_method='',phone_number='',referrer_url='',referrer_name=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(claimed_user_id != ''): 
			params['claimed_user_id'] = claimed_user_id
		if(claimed_date != ''): 
			params['claimed_date'] = claimed_date
		if(claim_method != ''): 
			params['claim_method'] = claim_method
		if(phone_number != ''): 
			params['phone_number'] = phone_number
		if(referrer_url != ''): 
			params['referrer_url'] = referrer_url
		if(referrer_name != ''): 
			params['referrer_name'] = referrer_name
		return self.doCurl("POST","/entity/claim",params)
  


	'''
	Allows a description object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityDescription(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/description",params)
  


	'''
	With a known entity id, a description object can be added.
	@param entity_id
	@param headline
	@param body
	@return - the data from the api
	'''
	def postEntityDescription(self,entity_id='',headline='',body=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(headline != ''): 
			params['headline'] = headline
		if(body != ''): 
			params['body'] = body
		return self.doCurl("POST","/entity/description",params)
  


	'''
	Allows a phone object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityDocument(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/document",params)
  


	'''
	With a known entity id, an document object can be added.
	@param entity_id
	@param name
	@param filedata
	@return - the data from the api
	'''
	def postEntityDocument(self,entity_id='',name='',filedata=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(name != ''): 
			params['name'] = name
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/entity/document",params)
  


	'''
	With a known entity id, an email address object can be added.
	@param entity_id
	@param email_address
	@param email_description
	@return - the data from the api
	'''
	def postEntityEmail(self,entity_id='',email_address='',email_description=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(email_address != ''): 
			params['email_address'] = email_address
		if(email_description != ''): 
			params['email_description'] = email_description
		return self.doCurl("POST","/entity/email",params)
  


	'''
	Allows a email object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityEmail(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/email",params)
  


	'''
	With a known entity id, an employee object can be added.
	@param entity_id
	@param title
	@param forename
	@param surname
	@param job_title
	@param description
	@param email
	@param phone_number
	@return - the data from the api
	'''
	def postEntityEmployee(self,entity_id='',title='',forename='',surname='',job_title='',description='',email='',phone_number=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(title != ''): 
			params['title'] = title
		if(forename != ''): 
			params['forename'] = forename
		if(surname != ''): 
			params['surname'] = surname
		if(job_title != ''): 
			params['job_title'] = job_title
		if(description != ''): 
			params['description'] = description
		if(email != ''): 
			params['email'] = email
		if(phone_number != ''): 
			params['phone_number'] = phone_number
		return self.doCurl("POST","/entity/employee",params)
  


	'''
	Allows an employee object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityEmployee(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/employee",params)
  


	'''
	With a known entity id, an fax object can be added.
	@param entity_id
	@param number
	@param description
	@return - the data from the api
	'''
	def postEntityFax(self,entity_id='',number='',description=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(number != ''): 
			params['number'] = number
		if(description != ''): 
			params['description'] = description
		return self.doCurl("POST","/entity/fax",params)
  


	'''
	Allows a fax object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityFax(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/fax",params)
  


	'''
	With a known entity id, a geopoint can be updated.
	@param entity_id
	@param longitude
	@param latitude
	@param accuracy
	@return - the data from the api
	'''
	def postEntityGeopoint(self,entity_id='',longitude='',latitude='',accuracy=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(longitude != ''): 
			params['longitude'] = longitude
		if(latitude != ''): 
			params['latitude'] = latitude
		if(accuracy != ''): 
			params['accuracy'] = accuracy
		return self.doCurl("POST","/entity/geopoint",params)
  


	'''
	With a known entity id, a group  can be added to group members.
	@param entity_id
	@param group_id
	@return - the data from the api
	'''
	def postEntityGroup(self,entity_id='',group_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(group_id != ''): 
			params['group_id'] = group_id
		return self.doCurl("POST","/entity/group",params)
  


	'''
	Allows a group object to be removed from an entities group members
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityGroup(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/group",params)
  


	'''
	With a known entity id, a image object can be added.
	@param entity_id
	@param filedata
	@param image_name
	@return - the data from the api
	'''
	def postEntityImage(self,entity_id='',filedata='',image_name=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(filedata != ''): 
			params['filedata'] = filedata
		if(image_name != ''): 
			params['image_name'] = image_name
		return self.doCurl("POST","/entity/image",params)
  


	'''
	Allows a image object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityImage(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/image",params)
  


	'''
	With a known entity id, an invoice_address object can be updated.
	@param entity_id
	@param building_number
	@param address1
	@param address2
	@param address3
	@param district
	@param town
	@param county
	@param province
	@param postcode
	@param address_type
	@return - the data from the api
	'''
	def postEntityInvoice_address(self,entity_id='',building_number='',address1='',address2='',address3='',district='',town='',county='',province='',postcode='',address_type=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(building_number != ''): 
			params['building_number'] = building_number
		if(address1 != ''): 
			params['address1'] = address1
		if(address2 != ''): 
			params['address2'] = address2
		if(address3 != ''): 
			params['address3'] = address3
		if(district != ''): 
			params['district'] = district
		if(town != ''): 
			params['town'] = town
		if(county != ''): 
			params['county'] = county
		if(province != ''): 
			params['province'] = province
		if(postcode != ''): 
			params['postcode'] = postcode
		if(address_type != ''): 
			params['address_type'] = address_type
		return self.doCurl("POST","/entity/invoice_address",params)
  


	'''
	With a known entity id and a known invoice_address ID, we can delete a specific invoice_address object from an enitity.
	@param entity_id
	@return - the data from the api
	'''
	def deleteEntityInvoice_address(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("DELETE","/entity/invoice_address",params)
  


	'''
	With a known entity id, a list description object can be added.
	@param entity_id
	@param headline
	@param body
	@return - the data from the api
	'''
	def postEntityList(self,entity_id='',headline='',body=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(headline != ''): 
			params['headline'] = headline
		if(body != ''): 
			params['body'] = body
		return self.doCurl("POST","/entity/list",params)
  


	'''
	Allows a list description object to be reduced in confidence
	@param gen_id
	@param entity_id
	@return - the data from the api
	'''
	def deleteEntityList(self,gen_id='',entity_id=''):
		params = {}
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("DELETE","/entity/list",params)
  


	'''
	With a known entity id, a logo object can be added.
	@param entity_id
	@param filedata
	@param logo_name
	@return - the data from the api
	'''
	def postEntityLogo(self,entity_id='',filedata='',logo_name=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(filedata != ''): 
			params['filedata'] = filedata
		if(logo_name != ''): 
			params['logo_name'] = logo_name
		return self.doCurl("POST","/entity/logo",params)
  


	'''
	Allows a phone object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityLogo(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/logo",params)
  


	'''
	Merge two entities into one
	@param from
	@param to
	@param override_trust - Do you want to override the trust of the 'from' entity
	@param uncontribute_masheryid - Do we want to uncontribute any data for a masheryid?
	@param uncontribute_userid - Do we want to uncontribute any data for a user_id?
	@param uncontribute_supplierid - Do we want to uncontribute any data for a supplier_id?
	@return - the data from the api
	'''
	def postEntityMerge(self,from2='',to='',override_trust='',uncontribute_masheryid='',uncontribute_userid='',uncontribute_supplierid=''):
		params = {}
		if(from2 != ''): 
			params['from2'] = from2
		if(to != ''): 
			params['to'] = to
		if(override_trust != ''): 
			params['override_trust'] = override_trust
		if(uncontribute_masheryid != ''): 
			params['uncontribute_masheryid'] = uncontribute_masheryid
		if(uncontribute_userid != ''): 
			params['uncontribute_userid'] = uncontribute_userid
		if(uncontribute_supplierid != ''): 
			params['uncontribute_supplierid'] = uncontribute_supplierid
		return self.doCurl("POST","/entity/merge",params)
  


	'''
	Update entities that use an old category ID to a new one
	@param from
	@param to
	@param limit
	@return - the data from the api
	'''
	def postEntityMigrate_category(self,from2='',to='',limit=''):
		params = {}
		if(from2 != ''): 
			params['from2'] = from2
		if(to != ''): 
			params['to'] = to
		if(limit != ''): 
			params['limit'] = limit
		return self.doCurl("POST","/entity/migrate_category",params)
  


	'''
	With a known entity id, a name can be updated.
	@param entity_id
	@param name
	@param formal_name
	@return - the data from the api
	'''
	def postEntityName(self,entity_id='',name='',formal_name=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(name != ''): 
			params['name'] = name
		if(formal_name != ''): 
			params['formal_name'] = formal_name
		return self.doCurl("POST","/entity/name",params)
  


	'''
	With a known entity id, a opening times object can be added. Each day can be either 'closed' to indicate that the entity is closed that day, '24hour' to indicate that the entity is open all day or single/split time ranges can be supplied in 4-digit 24-hour format, such as '09001730' or '09001200,13001700' to indicate hours of opening.
	@param entity_id - The id of the entity to edit
	@param monday - e.g. 'closed', '24hour' , '09001730' , '09001200,13001700'
	@param tuesday - e.g. 'closed', '24hour' , '09001730' , '09001200,13001700'
	@param wednesday - e.g. 'closed', '24hour' , '09001730' , '09001200,13001700'
	@param thursday - e.g. 'closed', '24hour' , '09001730' , '09001200,13001700'
	@param friday - e.g. 'closed', '24hour' , '09001730' , '09001200,13001700'
	@param saturday - e.g. 'closed', '24hour' , '09001730' , '09001200,13001700'
	@param sunday - e.g. 'closed', '24hour' , '09001730' , '09001200,13001700'
	@param closed - a comma-separated list of dates that the entity is closed e.g. '2013-04-29,2013-05-02'
	@param closed_public_holidays - whether the entity is closed on public holidays
	@return - the data from the api
	'''
	def postEntityOpening_times(self,entity_id='',monday='',tuesday='',wednesday='',thursday='',friday='',saturday='',sunday='',closed='',closed_public_holidays=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(monday != ''): 
			params['monday'] = monday
		if(tuesday != ''): 
			params['tuesday'] = tuesday
		if(wednesday != ''): 
			params['wednesday'] = wednesday
		if(thursday != ''): 
			params['thursday'] = thursday
		if(friday != ''): 
			params['friday'] = friday
		if(saturday != ''): 
			params['saturday'] = saturday
		if(sunday != ''): 
			params['sunday'] = sunday
		if(closed != ''): 
			params['closed'] = closed
		if(closed_public_holidays != ''): 
			params['closed_public_holidays'] = closed_public_holidays
		return self.doCurl("POST","/entity/opening_times",params)
  


	'''
	With a known entity id, a opening times object can be removed.
	@param entity_id - The id of the entity to edit
	@return - the data from the api
	'''
	def deleteEntityOpening_times(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("DELETE","/entity/opening_times",params)
  


	'''
	Allows a new phone object to be added to a specified entity. A new object id will be calculated and returned to you if successful.
	@param entity_id
	@param number
	@param trackable
	@return - the data from the api
	'''
	def postEntityPhone(self,entity_id='',number='',trackable=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(number != ''): 
			params['number'] = number
		if(trackable != ''): 
			params['trackable'] = trackable
		return self.doCurl("POST","/entity/phone",params)
  


	'''
	Allows a phone object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityPhone(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/phone",params)
  


	'''
	Create/Update a postal address
	@param entity_id
	@param building_number
	@param address1
	@param address2
	@param address3
	@param district
	@param town
	@param county
	@param province
	@param postcode
	@param address_type
	@param do_not_display
	@return - the data from the api
	'''
	def postEntityPostal_address(self,entity_id='',building_number='',address1='',address2='',address3='',district='',town='',county='',province='',postcode='',address_type='',do_not_display=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(building_number != ''): 
			params['building_number'] = building_number
		if(address1 != ''): 
			params['address1'] = address1
		if(address2 != ''): 
			params['address2'] = address2
		if(address3 != ''): 
			params['address3'] = address3
		if(district != ''): 
			params['district'] = district
		if(town != ''): 
			params['town'] = town
		if(county != ''): 
			params['county'] = county
		if(province != ''): 
			params['province'] = province
		if(postcode != ''): 
			params['postcode'] = postcode
		if(address_type != ''): 
			params['address_type'] = address_type
		if(do_not_display != ''): 
			params['do_not_display'] = do_not_display
		return self.doCurl("POST","/entity/postal_address",params)
  


	'''
	Fetches the documents that match the given masheryid and supplier_id
	@param supplier_id - The Supplier ID
	@return - the data from the api
	'''
	def getEntityProvisionalBy_supplier_id(self,supplier_id=''):
		params = {}
		if(supplier_id != ''): 
			params['supplier_id'] = supplier_id
		return self.doCurl("GET","/entity/provisional/by_supplier_id",params)
  


	'''
	Allows a list of available revisions to be returned by its entity id
	@param entity_id
	@return - the data from the api
	'''
	def getEntityRevisions(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/entity/revisions",params)
  


	'''
	Allows a specific revision of an entity to be returned by entity id and a revision number
	@param entity_id
	@param revision_id
	@return - the data from the api
	'''
	def getEntityRevisionsByRevisionID(self,entity_id='',revision_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(revision_id != ''): 
			params['revision_id'] = revision_id
		return self.doCurl("GET","/entity/revisions/byRevisionID",params)
  


	'''
	Search for matching entities
	@param latitude_1
	@param longitude_1
	@param latitude_2
	@param longitude_2
	@param per_page
	@param page
	@param country
	@param language
	@return - the data from the api
	'''
	def getEntitySearchByboundingbox(self,latitude_1='',longitude_1='',latitude_2='',longitude_2='',per_page='',page='',country='',language=''):
		params = {}
		if(latitude_1 != ''): 
			params['latitude_1'] = latitude_1
		if(longitude_1 != ''): 
			params['longitude_1'] = longitude_1
		if(latitude_2 != ''): 
			params['latitude_2'] = latitude_2
		if(longitude_2 != ''): 
			params['longitude_2'] = longitude_2
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/search/byboundingbox",params)
  


	'''
	Search for matching entities
	@param where - Location to search for results. E.g. Dublin e.g. Dublin
	@param per_page - How many results per page
	@param page - What page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie
	@param language - An ISO compatible language code, E.g. en
	@param latitude - The decimal latitude of the search context (optional)
	@param longitude - The decimal longitude of the search context (optional)
	@return - the data from the api
	'''
	def getEntitySearchBylocation(self,where='',per_page='',page='',country='',language='',latitude='',longitude=''):
		params = {}
		if(where != ''): 
			params['where'] = where
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		return self.doCurl("GET","/entity/search/bylocation",params)
  


	'''
	Search for matching entities
	@param what - What to get results for. E.g. Plumber e.g. plumber
	@param per_page - Number of results returned per page
	@param page - The page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getEntitySearchWhat(self,what='',per_page='',page='',country='',language=''):
		params = {}
		if(what != ''): 
			params['what'] = what
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/search/what",params)
  


	'''
	Search for matching entities
	@param what - What to get results for. E.g. Plumber e.g. plumber
	@param latitude_1 - Latitude of first point in bounding box e.g. 53.396842
	@param longitude_1 - Longitude of first point in bounding box e.g. -6.37619
	@param latitude_2 - Latitude of second point in bounding box e.g. 53.290463
	@param longitude_2 - Longitude of second point in bounding box e.g. -6.207275
	@param per_page
	@param page
	@param country - A valid ISO 3166 country code e.g. ie
	@param language
	@return - the data from the api
	'''
	def getEntitySearchWhatByboundingbox(self,what='',latitude_1='',longitude_1='',latitude_2='',longitude_2='',per_page='',page='',country='',language=''):
		params = {}
		if(what != ''): 
			params['what'] = what
		if(latitude_1 != ''): 
			params['latitude_1'] = latitude_1
		if(longitude_1 != ''): 
			params['longitude_1'] = longitude_1
		if(latitude_2 != ''): 
			params['latitude_2'] = latitude_2
		if(longitude_2 != ''): 
			params['longitude_2'] = longitude_2
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/search/what/byboundingbox",params)
  


	'''
	Search for matching entities
	@param what - What to get results for. E.g. Plumber e.g. plumber
	@param where - The location to get results for. E.g. Dublin e.g. Dublin
	@param per_page - Number of results returned per page
	@param page - Which page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param language - An ISO compatible language code, E.g. en
	@param latitude - The decimal latitude of the search context (optional)
	@param longitude - The decimal longitude of the search context (optional)
	@return - the data from the api
	'''
	def getEntitySearchWhatBylocation(self,what='',where='',per_page='',page='',country='',language='',latitude='',longitude=''):
		params = {}
		if(what != ''): 
			params['what'] = what
		if(where != ''): 
			params['where'] = where
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		return self.doCurl("GET","/entity/search/what/bylocation",params)
  


	'''
	Search for matching entities, ordered by nearness
	@param what - What to get results for. E.g. Plumber e.g. plumber
	@param per_page - Number of results returned per page
	@param page - Which page number to retrieve
	@param language - An ISO compatible language code, E.g. en
	@param latitude - The decimal latitude of the centre point of the search
	@param longitude - The decimal longitude of the centre point of the search
	@return - the data from the api
	'''
	def getEntitySearchWhatBynearest(self,what='',per_page='',page='',language='',latitude='',longitude=''):
		params = {}
		if(what != ''): 
			params['what'] = what
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(language != ''): 
			params['language'] = language
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		return self.doCurl("GET","/entity/search/what/bynearest",params)
  


	'''
	Search for matching entities
	@param who - Company name e.g. Starbucks
	@param per_page - How many results per page
	@param page - What page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getEntitySearchWho(self,who='',per_page='',page='',country='',language=''):
		params = {}
		if(who != ''): 
			params['who'] = who
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/search/who",params)
  


	'''
	Search for matching entities
	@param who
	@param latitude_1
	@param longitude_1
	@param latitude_2
	@param longitude_2
	@param per_page
	@param page
	@param country
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getEntitySearchWhoByboundingbox(self,who='',latitude_1='',longitude_1='',latitude_2='',longitude_2='',per_page='',page='',country='',language=''):
		params = {}
		if(who != ''): 
			params['who'] = who
		if(latitude_1 != ''): 
			params['latitude_1'] = latitude_1
		if(longitude_1 != ''): 
			params['longitude_1'] = longitude_1
		if(latitude_2 != ''): 
			params['latitude_2'] = latitude_2
		if(longitude_2 != ''): 
			params['longitude_2'] = longitude_2
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/search/who/byboundingbox",params)
  


	'''
	Search for matching entities
	@param who - Company Name e.g. Starbucks
	@param where - The location to get results for. E.g. Dublin e.g. Dublin
	@param per_page - Number of results returned per page
	@param page - Which page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param latitude - The decimal latitude of the search context (optional)
	@param longitude - The decimal longitude of the search context (optional)
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getEntitySearchWhoBylocation(self,who='',where='',per_page='',page='',country='',latitude='',longitude='',language=''):
		params = {}
		if(who != ''): 
			params['who'] = who
		if(where != ''): 
			params['where'] = where
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/search/who/bylocation",params)
  


	'''
	Send an email to an email address specified in an entity
	@param entity_id - The entity id of the entity you wish to contact
	@param gen_id - The gen_id of the email address you wish to send the message to
	@param from_email - The email of the person sending the message 
	@param subject - The subject for the email
	@param content - The content of the email
	@return - the data from the api
	'''
	def postEntitySend_email(self,entity_id='',gen_id='',from_email='',subject='',content=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		if(from_email != ''): 
			params['from_email'] = from_email
		if(subject != ''): 
			params['subject'] = subject
		if(content != ''): 
			params['content'] = content
		return self.doCurl("POST","/entity/send_email",params)
  


	'''
	Allows a social media object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntitySocialmedia(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/socialmedia",params)
  


	'''
	With a known entity id, a social media object can be added.
	@param entity_id
	@param type
	@param website_url
	@return - the data from the api
	'''
	def postEntitySocialmedia(self,entity_id='',type='',website_url=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(type != ''): 
			params['type'] = type
		if(website_url != ''): 
			params['website_url'] = website_url
		return self.doCurl("POST","/entity/socialmedia",params)
  


	'''
	Allows a special offer object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntitySpecial_offer(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/special_offer",params)
  


	'''
	With a known entity id, a website object can be added.
	@param entity_id
	@param title
	@param description
	@param terms
	@param start_date
	@param expiry_date
	@param url
	@param image_url
	@return - the data from the api
	'''
	def postEntitySpecial_offer(self,entity_id='',title='',description='',terms='',start_date='',expiry_date='',url='',image_url=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(title != ''): 
			params['title'] = title
		if(description != ''): 
			params['description'] = description
		if(terms != ''): 
			params['terms'] = terms
		if(start_date != ''): 
			params['start_date'] = start_date
		if(expiry_date != ''): 
			params['expiry_date'] = expiry_date
		if(url != ''): 
			params['url'] = url
		if(image_url != ''): 
			params['image_url'] = image_url
		return self.doCurl("POST","/entity/special_offer",params)
  


	'''
	With a known entity id, a status object can be updated.
	@param entity_id
	@param status
	@param inactive_reason
	@param inactive_description
	@return - the data from the api
	'''
	def postEntityStatus(self,entity_id='',status='',inactive_reason='',inactive_description=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(status != ''): 
			params['status'] = status
		if(inactive_reason != ''): 
			params['inactive_reason'] = inactive_reason
		if(inactive_description != ''): 
			params['inactive_description'] = inactive_description
		return self.doCurl("POST","/entity/status",params)
  


	'''
	With a known entity id, an tag object can be added.
	@param entity_id
	@param tag
	@param language
	@return - the data from the api
	'''
	def postEntityTag(self,entity_id='',tag='',language=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(tag != ''): 
			params['tag'] = tag
		if(language != ''): 
			params['language'] = language
		return self.doCurl("POST","/entity/tag",params)
  


	'''
	Allows a tag object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityTag(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/tag",params)
  


	'''
	With a known entity id, a testimonial object can be added.
	@param entity_id
	@param title
	@param text
	@param date
	@param testifier_name
	@return - the data from the api
	'''
	def postEntityTestimonial(self,entity_id='',title='',text='',date='',testifier_name=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(title != ''): 
			params['title'] = title
		if(text != ''): 
			params['text'] = text
		if(date != ''): 
			params['date'] = date
		if(testifier_name != ''): 
			params['testifier_name'] = testifier_name
		return self.doCurl("POST","/entity/testimonial",params)
  


	'''
	Allows a testimonial object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityTestimonial(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/testimonial",params)
  


	'''
	Get the updates a uncontribute would perform
	@param entity_id - The entity to pull
	@param object_name - The entity object to update
	@param supplier_id - The supplier_id to remove
	@param user_id - The user_id to remove
	@return - the data from the api
	'''
	def getEntityUncontribute(self,entity_id='',object_name='',supplier_id='',user_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(object_name != ''): 
			params['object_name'] = object_name
		if(supplier_id != ''): 
			params['supplier_id'] = supplier_id
		if(user_id != ''): 
			params['user_id'] = user_id
		return self.doCurl("GET","/entity/uncontribute",params)
  


	'''
	Separates an entity into two distinct entities 
	@param entity_id
	@param supplier_masheryid
	@param supplier_id
	@return - the data from the api
	'''
	def postEntityUnmerge(self,entity_id='',supplier_masheryid='',supplier_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(supplier_masheryid != ''): 
			params['supplier_masheryid'] = supplier_masheryid
		if(supplier_id != ''): 
			params['supplier_id'] = supplier_id
		return self.doCurl("POST","/entity/unmerge",params)
  


	'''
	Allows a video object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityVideo(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/video",params)
  


	'''
	With a known entity id, a YouTube video object can be added.
	@param entity_id
	@param embed_code
	@return - the data from the api
	'''
	def postEntityVideoYoutube(self,entity_id='',embed_code=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(embed_code != ''): 
			params['embed_code'] = embed_code
		return self.doCurl("POST","/entity/video/youtube",params)
  


	'''
	Allows a website object to be reduced in confidence
	@param entity_id
	@param gen_id
	@return - the data from the api
	'''
	def deleteEntityWebsite(self,entity_id='',gen_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/entity/website",params)
  


	'''
	With a known entity id, a website object can be added.
	@param entity_id
	@param website_url
	@param display_url
	@param website_description
	@return - the data from the api
	'''
	def postEntityWebsite(self,entity_id='',website_url='',display_url='',website_description=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(website_url != ''): 
			params['website_url'] = website_url
		if(display_url != ''): 
			params['display_url'] = display_url
		if(website_description != ''): 
			params['website_description'] = website_description
		return self.doCurl("POST","/entity/website",params)
  


	'''
	Add an entityserve document
	@param entity_id - The id of the entity to create the entityserve event for
	@param country - the ISO code of the country
	@param event_type - The event type being recorded
	@return - the data from the api
	'''
	def putEntityserve(self,entity_id='',country='',event_type=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(country != ''): 
			params['country'] = country
		if(event_type != ''): 
			params['event_type'] = event_type
		return self.doCurl("PUT","/entityserve",params)
  


	'''
	Remove a flatpack using a supplied flatpack_id
	@param flatpack_id - the id of the flatpack to delete
	@return - the data from the api
	'''
	def deleteFlatpack(self,flatpack_id=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("DELETE","/flatpack",params)
  


	'''
	Update/Add a flatpack
	@param flatpack_id - this record's unique, auto-generated id - if supplied, then this is an edit, otherwise it's an add
	@param domainName - the domain name to serve this flatpack site on (no leading http:// or anything please)
	@param stub - the stub that is appended to the flatpack's url e.g. http://dev.localhost/stub
	@param flatpackName - the name of the Flat pack instance
	@param less - the LESS configuration to use to overrides the Bootstrap CSS
	@param language - the language in which to render the flatpack site
	@param country - the country to use for searches etc
	@param mapsType - the type of maps to use
	@param mapKey - the nokia map key to use to render maps
	@param searchFormShowOn - list of pages to show the search form
	@param searchFormShowKeywordsBox - whether to display the keywords box on the search form
	@param searchFormShowLocationBox - whether to display the location box on search forms - not required
	@param searchFormKeywordsAutoComplete - whether to do auto-completion on the keywords box on the search form
	@param searchFormLocationsAutoComplete - whether to do auto-completion on the locations box on the search form
	@param searchFormDefaultLocation - the string to use as the default location for searches if no location is supplied
	@param searchFormPlaceholderKeywords - the string to show in the keyword box as placeholder text e.g. e.g. cafe
	@param searchFormPlaceholderLocation - the string to show in the location box as placeholder text e.g. e.g. Dublin
	@param searchFormKeywordsLabel - the string to show next to the keywords control e.g. I'm looking for
	@param searchFormLocationLabel - the string to show next to the location control e.g. Located in
	@param cannedLinksHeader - the string to show above canned searches
	@param homepageTitle - the page title of site's home page
	@param homepageDescription - the meta description of the home page
	@param homepageIntroTitle - the introductory title for the homepage
	@param homepageIntroText - the introductory text for the homepage
	@param head - payload to put in the head of the flatpack
	@param adblock - payload to put in the adblock of the flatpack
	@param bodyTop - the payload to put in the top of the body of a flatpack
	@param bodyBottom - the payload to put in the bottom of the body of a flatpack
	@param header_menu - the JSON that describes a navigation at the top of the page
	@param header_menu_bottom - the JSON that describes a navigation below the masthead
	@param footer_menu - the JSON that describes a navigation at the bottom of the page
	@param bdpTitle - The page title of the entity business profile pages
	@param bdpDescription - The meta description of entity business profile pages
	@param bdpAds - The block of HTML/JS that renders Ads on BDPs
	@param serpTitle - The page title of the serps
	@param serpDescription - The meta description of serps
	@param serpNumberResults - The number of results per search page
	@param serpNumberAdverts - The number of adverts to show on the first search page
	@param serpAds - The block of HTML/JS that renders Ads on Serps
	@param serpTitleNoWhat - The text to display in the title for where only searches
	@param serpDescriptionNoWhat - The text to display in the description for where only searches
	@param cookiePolicyUrl - The cookie policy url of the flatpack
	@param cookiePolicyNotice - Whether to show the cookie policy on this flatpack
	@param addBusinessButtonText - The text used in the 'Add your business' button
	@param twitterUrl - Twitter link
	@param facebookUrl - Facebook link
	@param copyright - Copyright message
	@param advertUpgradeActive - whether upgrade message is displayed on this Flatpack
	@param advertUpgradePrice - the cost of upgrading
	@param advertUpgradeMaxTags - the number of tags upgrading gives you
	@param advertUpgradeMaxLocations - the number of locations upgrading gives you
	@param advertUpgradeContractLength - the length of the contract (days)
	@param advertUpgradeRefId - a unique reference for the upgrade
	@param phoneReveal - record phone number reveal
	@param loginLinkText - the link text for the Login link
	@param contextLocationId - The location ID to use as the context for searches on this flatpack
	@param addBusinessButtonPosition - The location ID to use as the context for searches on this flatpack
	@param denyIndexing - Whether to noindex a flatpack
	@param contextRadius - allows you to set a catchment area around the contextLocationId in miles for use when displaying the activity stream module
	@param activityStream - allows you to set the activity to be displayed in the activity stream
	@param activityStreamSize - Sets the number of items to show within the activity stream.
	@return - the data from the api
	'''
	def postFlatpack(self,flatpack_id='',domainName='',stub='',flatpackName='',less='',language='',country='',mapsType='',mapKey='',searchFormShowOn='',searchFormShowKeywordsBox='',searchFormShowLocationBox='',searchFormKeywordsAutoComplete='',searchFormLocationsAutoComplete='',searchFormDefaultLocation='',searchFormPlaceholderKeywords='',searchFormPlaceholderLocation='',searchFormKeywordsLabel='',searchFormLocationLabel='',cannedLinksHeader='',homepageTitle='',homepageDescription='',homepageIntroTitle='',homepageIntroText='',head='',adblock='',bodyTop='',bodyBottom='',header_menu='',header_menu_bottom='',footer_menu='',bdpTitle='',bdpDescription='',bdpAds='',serpTitle='',serpDescription='',serpNumberResults='',serpNumberAdverts='',serpAds='',serpTitleNoWhat='',serpDescriptionNoWhat='',cookiePolicyUrl='',cookiePolicyNotice='',addBusinessButtonText='',twitterUrl='',facebookUrl='',copyright='',advertUpgradeActive='',advertUpgradePrice='',advertUpgradeMaxTags='',advertUpgradeMaxLocations='',advertUpgradeContractLength='',advertUpgradeRefId='',phoneReveal='',loginLinkText='',contextLocationId='',addBusinessButtonPosition='',denyIndexing='',contextRadius='',activityStream='',activityStreamSize=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(domainName != ''): 
			params['domainName'] = domainName
		if(stub != ''): 
			params['stub'] = stub
		if(flatpackName != ''): 
			params['flatpackName'] = flatpackName
		if(less != ''): 
			params['less'] = less
		if(language != ''): 
			params['language'] = language
		if(country != ''): 
			params['country'] = country
		if(mapsType != ''): 
			params['mapsType'] = mapsType
		if(mapKey != ''): 
			params['mapKey'] = mapKey
		if(searchFormShowOn != ''): 
			params['searchFormShowOn'] = searchFormShowOn
		if(searchFormShowKeywordsBox != ''): 
			params['searchFormShowKeywordsBox'] = searchFormShowKeywordsBox
		if(searchFormShowLocationBox != ''): 
			params['searchFormShowLocationBox'] = searchFormShowLocationBox
		if(searchFormKeywordsAutoComplete != ''): 
			params['searchFormKeywordsAutoComplete'] = searchFormKeywordsAutoComplete
		if(searchFormLocationsAutoComplete != ''): 
			params['searchFormLocationsAutoComplete'] = searchFormLocationsAutoComplete
		if(searchFormDefaultLocation != ''): 
			params['searchFormDefaultLocation'] = searchFormDefaultLocation
		if(searchFormPlaceholderKeywords != ''): 
			params['searchFormPlaceholderKeywords'] = searchFormPlaceholderKeywords
		if(searchFormPlaceholderLocation != ''): 
			params['searchFormPlaceholderLocation'] = searchFormPlaceholderLocation
		if(searchFormKeywordsLabel != ''): 
			params['searchFormKeywordsLabel'] = searchFormKeywordsLabel
		if(searchFormLocationLabel != ''): 
			params['searchFormLocationLabel'] = searchFormLocationLabel
		if(cannedLinksHeader != ''): 
			params['cannedLinksHeader'] = cannedLinksHeader
		if(homepageTitle != ''): 
			params['homepageTitle'] = homepageTitle
		if(homepageDescription != ''): 
			params['homepageDescription'] = homepageDescription
		if(homepageIntroTitle != ''): 
			params['homepageIntroTitle'] = homepageIntroTitle
		if(homepageIntroText != ''): 
			params['homepageIntroText'] = homepageIntroText
		if(head != ''): 
			params['head'] = head
		if(adblock != ''): 
			params['adblock'] = adblock
		if(bodyTop != ''): 
			params['bodyTop'] = bodyTop
		if(bodyBottom != ''): 
			params['bodyBottom'] = bodyBottom
		if(header_menu != ''): 
			params['header_menu'] = header_menu
		if(header_menu_bottom != ''): 
			params['header_menu_bottom'] = header_menu_bottom
		if(footer_menu != ''): 
			params['footer_menu'] = footer_menu
		if(bdpTitle != ''): 
			params['bdpTitle'] = bdpTitle
		if(bdpDescription != ''): 
			params['bdpDescription'] = bdpDescription
		if(bdpAds != ''): 
			params['bdpAds'] = bdpAds
		if(serpTitle != ''): 
			params['serpTitle'] = serpTitle
		if(serpDescription != ''): 
			params['serpDescription'] = serpDescription
		if(serpNumberResults != ''): 
			params['serpNumberResults'] = serpNumberResults
		if(serpNumberAdverts != ''): 
			params['serpNumberAdverts'] = serpNumberAdverts
		if(serpAds != ''): 
			params['serpAds'] = serpAds
		if(serpTitleNoWhat != ''): 
			params['serpTitleNoWhat'] = serpTitleNoWhat
		if(serpDescriptionNoWhat != ''): 
			params['serpDescriptionNoWhat'] = serpDescriptionNoWhat
		if(cookiePolicyUrl != ''): 
			params['cookiePolicyUrl'] = cookiePolicyUrl
		if(cookiePolicyNotice != ''): 
			params['cookiePolicyNotice'] = cookiePolicyNotice
		if(addBusinessButtonText != ''): 
			params['addBusinessButtonText'] = addBusinessButtonText
		if(twitterUrl != ''): 
			params['twitterUrl'] = twitterUrl
		if(facebookUrl != ''): 
			params['facebookUrl'] = facebookUrl
		if(copyright != ''): 
			params['copyright'] = copyright
		if(advertUpgradeActive != ''): 
			params['advertUpgradeActive'] = advertUpgradeActive
		if(advertUpgradePrice != ''): 
			params['advertUpgradePrice'] = advertUpgradePrice
		if(advertUpgradeMaxTags != ''): 
			params['advertUpgradeMaxTags'] = advertUpgradeMaxTags
		if(advertUpgradeMaxLocations != ''): 
			params['advertUpgradeMaxLocations'] = advertUpgradeMaxLocations
		if(advertUpgradeContractLength != ''): 
			params['advertUpgradeContractLength'] = advertUpgradeContractLength
		if(advertUpgradeRefId != ''): 
			params['advertUpgradeRefId'] = advertUpgradeRefId
		if(phoneReveal != ''): 
			params['phoneReveal'] = phoneReveal
		if(loginLinkText != ''): 
			params['loginLinkText'] = loginLinkText
		if(contextLocationId != ''): 
			params['contextLocationId'] = contextLocationId
		if(addBusinessButtonPosition != ''): 
			params['addBusinessButtonPosition'] = addBusinessButtonPosition
		if(denyIndexing != ''): 
			params['denyIndexing'] = denyIndexing
		if(contextRadius != ''): 
			params['contextRadius'] = contextRadius
		if(activityStream != ''): 
			params['activityStream'] = activityStream
		if(activityStreamSize != ''): 
			params['activityStreamSize'] = activityStreamSize
		return self.doCurl("POST","/flatpack",params)
  


	'''
	Get a flatpack
	@param flatpack_id - the unique id to search for
	@return - the data from the api
	'''
	def getFlatpack(self,flatpack_id=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("GET","/flatpack",params)
  


	'''
	Upload a CSS file for the Admin for this flatpack
	@param flatpack_id - the id of the flatpack to update
	@param filedata
	@return - the data from the api
	'''
	def postFlatpackAdminCSS(self,flatpack_id='',filedata=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/flatpack/adminCSS",params)
  


	'''
	Upload an image to serve out as the large logo in the Admin for this flatpack
	@param flatpack_id - the id of the flatpack to update
	@param filedata
	@return - the data from the api
	'''
	def postFlatpackAdminLargeLogo(self,flatpack_id='',filedata=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/flatpack/adminLargeLogo",params)
  


	'''
	Upload an image to serve out as the small logo in the Admin for this flatpack
	@param flatpack_id - the id of the flatpack to update
	@param filedata
	@return - the data from the api
	'''
	def postFlatpackAdminSmallLogo(self,flatpack_id='',filedata=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/flatpack/adminSmallLogo",params)
  


	'''
	Get a flatpack using a domain name
	@param domainName - the domain name to search for
	@return - the data from the api
	'''
	def getFlatpackBy_domain_name(self,domainName=''):
		params = {}
		if(domainName != ''): 
			params['domainName'] = domainName
		return self.doCurl("GET","/flatpack/by_domain_name",params)
  


	'''
	Get flatpacks that match the supplied masheryid
	@return - the data from the api
	'''
	def getFlatpackBy_masheryid(self):
		params = {}
		return self.doCurl("GET","/flatpack/by_masheryid",params)
  


	'''
	Clone an existing flatpack
	@param flatpack_id - the flatpack_id to clone
	@param domainName - the domain of the new flatpack site (no leading http:// or anything please)
	@return - the data from the api
	'''
	def getFlatpackClone(self,flatpack_id='',domainName=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(domainName != ''): 
			params['domainName'] = domainName
		return self.doCurl("GET","/flatpack/clone",params)
  


	'''
	Upload an icon to serve out with this flatpack
	@param flatpack_id - the id of the flatpack to update
	@param filedata
	@return - the data from the api
	'''
	def postFlatpackIcon(self,flatpack_id='',filedata=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/flatpack/icon",params)
  


	'''
	Remove a canned link to an existing flatpack site.
	@param flatpack_id - the id of the flatpack to delete
	@param gen_id - the id of the canned link to remove
	@return - the data from the api
	'''
	def deleteFlatpackLink(self,flatpack_id='',gen_id=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		return self.doCurl("DELETE","/flatpack/link",params)
  


	'''
	Add a canned link to an existing flatpack site.
	@param flatpack_id - the id of the flatpack to delete
	@param keywords - the keywords to use in the canned search
	@param location - the location to use in the canned search
	@param linkText - the link text to be used to in the canned search link
	@return - the data from the api
	'''
	def postFlatpackLink(self,flatpack_id='',keywords='',location='',linkText=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(keywords != ''): 
			params['keywords'] = keywords
		if(location != ''): 
			params['location'] = location
		if(linkText != ''): 
			params['linkText'] = linkText
		return self.doCurl("POST","/flatpack/link",params)
  


	'''
	Upload a logo to serve out with this flatpack
	@param flatpack_id - the id of the flatpack to update
	@param filedata
	@return - the data from the api
	'''
	def postFlatpackLogo(self,flatpack_id='',filedata=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/flatpack/logo",params)
  


	'''
	Upload a TXT file to act as the sitemap for this flatpack
	@param flatpack_id - the id of the flatpack to update
	@param filedata
	@return - the data from the api
	'''
	def postFlatpackSitemap(self,flatpack_id='',filedata=''):
		params = {}
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/flatpack/sitemap",params)
  


	'''
	Upload a file to our asset server and return the url
	@param filedata
	@return - the data from the api
	'''
	def postFlatpackUpload(self,filedata=''):
		params = {}
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/flatpack/upload",params)
  


	'''
	Returns group that matches a given group id
	@param group_id
	@return - the data from the api
	'''
	def getGroup(self,group_id=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		return self.doCurl("GET","/group",params)
  


	'''
	Update/Add a Group
	@param group_id
	@param name
	@param description
	@param url
	@return - the data from the api
	'''
	def postGroup(self,group_id='',name='',description='',url=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		if(name != ''): 
			params['name'] = name
		if(description != ''): 
			params['description'] = description
		if(url != ''): 
			params['url'] = url
		return self.doCurl("POST","/group",params)
  


	'''
	Delete a group with a specified group_id
	@param group_id
	@return - the data from the api
	'''
	def deleteGroup(self,group_id=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		return self.doCurl("DELETE","/group",params)
  


	'''
	Returns all groups
	@return - the data from the api
	'''
	def getGroupAll(self):
		params = {}
		return self.doCurl("GET","/group/all",params)
  


	'''
	Bulk delete entities from a specified group
	@param group_id
	@param filedata
	@return - the data from the api
	'''
	def postGroupBulk_delete(self,group_id='',filedata=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/group/bulk_delete",params)
  


	'''
	Bulk ingest entities into a specified group
	@param group_id
	@param filedata
	@param category_type
	@return - the data from the api
	'''
	def postGroupBulk_ingest(self,group_id='',filedata='',category_type=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		if(filedata != ''): 
			params['filedata'] = filedata
		if(category_type != ''): 
			params['category_type'] = category_type
		return self.doCurl("POST","/group/bulk_ingest",params)
  


	'''
	Bulk update entities with a specified group
	@param group_id
	@param data
	@return - the data from the api
	'''
	def postGroupBulk_update(self,group_id='',data=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		if(data != ''): 
			params['data'] = data
		return self.doCurl("POST","/group/bulk_update",params)
  


	'''
	Get number of claims today
	@param from_date
	@param to_date
	@param country_id
	@return - the data from the api
	'''
	def getHeartbeatBy_date(self,from_date='',to_date='',country_id=''):
		params = {}
		if(from_date != ''): 
			params['from_date'] = from_date
		if(to_date != ''): 
			params['to_date'] = to_date
		if(country_id != ''): 
			params['country_id'] = country_id
		return self.doCurl("GET","/heartbeat/by_date",params)
  


	'''
	Get number of claims today
	@param country
	@param claim_type
	@return - the data from the api
	'''
	def getHeartbeatTodayClaims(self,country='',claim_type=''):
		params = {}
		if(country != ''): 
			params['country'] = country
		if(claim_type != ''): 
			params['claim_type'] = claim_type
		return self.doCurl("GET","/heartbeat/today/claims",params)
  


	'''
	Process a bulk file
	@param job_id
	@param filedata - A tab separated file for ingest
	@return - the data from the api
	'''
	def postIngest_file(self,job_id='',filedata=''):
		params = {}
		if(job_id != ''): 
			params['job_id'] = job_id
		if(filedata != ''): 
			params['filedata'] = filedata
		return self.doCurl("POST","/ingest_file",params)
  


	'''
	Add a ingest job to the collection
	@param description
	@param category_type
	@return - the data from the api
	'''
	def postIngest_job(self,description='',category_type=''):
		params = {}
		if(description != ''): 
			params['description'] = description
		if(category_type != ''): 
			params['category_type'] = category_type
		return self.doCurl("POST","/ingest_job",params)
  


	'''
	Get an ingest job from the collection
	@param job_id
	@return - the data from the api
	'''
	def getIngest_job(self,job_id=''):
		params = {}
		if(job_id != ''): 
			params['job_id'] = job_id
		return self.doCurl("GET","/ingest_job",params)
  


	'''
	Get an ingest log from the collection
	@param job_id
	@param success
	@param errors
	@param limit
	@param skip
	@return - the data from the api
	'''
	def getIngest_logBy_job_id(self,job_id='',success='',errors='',limit='',skip=''):
		params = {}
		if(job_id != ''): 
			params['job_id'] = job_id
		if(success != ''): 
			params['success'] = success
		if(errors != ''): 
			params['errors'] = errors
		if(limit != ''): 
			params['limit'] = limit
		if(skip != ''): 
			params['skip'] = skip
		return self.doCurl("GET","/ingest_log/by_job_id",params)
  


	'''
	Check the status of the Ingest queue, and potentially flush it
	@param flush
	@return - the data from the api
	'''
	def getIngest_queue(self,flush=''):
		params = {}
		if(flush != ''): 
			params['flush'] = flush
		return self.doCurl("GET","/ingest_queue",params)
  


	'''
	Read a location with the supplied ID in the locations reference database.
	@param location_id
	@return - the data from the api
	'''
	def getLocation(self,location_id=''):
		params = {}
		if(location_id != ''): 
			params['location_id'] = location_id
		return self.doCurl("GET","/location",params)
  


	'''
	Create/update a new locz document with the supplied ID in the locations reference database.
	@param location_id
	@param type
	@param country
	@param language
	@param name
	@param formal_name
	@param resolution
	@param population
	@param description
	@param timezone
	@param latitude
	@param longitude
	@param parent_town
	@param parent_county
	@param parent_province
	@param parent_region
	@param parent_neighbourhood
	@param parent_district
	@param postalcode
	@param searchable_id
	@param searchable_ids
	@return - the data from the api
	'''
	def postLocation(self,location_id='',type='',country='',language='',name='',formal_name='',resolution='',population='',description='',timezone='',latitude='',longitude='',parent_town='',parent_county='',parent_province='',parent_region='',parent_neighbourhood='',parent_district='',postalcode='',searchable_id='',searchable_ids=''):
		params = {}
		if(location_id != ''): 
			params['location_id'] = location_id
		if(type != ''): 
			params['type'] = type
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		if(name != ''): 
			params['name'] = name
		if(formal_name != ''): 
			params['formal_name'] = formal_name
		if(resolution != ''): 
			params['resolution'] = resolution
		if(population != ''): 
			params['population'] = population
		if(description != ''): 
			params['description'] = description
		if(timezone != ''): 
			params['timezone'] = timezone
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		if(parent_town != ''): 
			params['parent_town'] = parent_town
		if(parent_county != ''): 
			params['parent_county'] = parent_county
		if(parent_province != ''): 
			params['parent_province'] = parent_province
		if(parent_region != ''): 
			params['parent_region'] = parent_region
		if(parent_neighbourhood != ''): 
			params['parent_neighbourhood'] = parent_neighbourhood
		if(parent_district != ''): 
			params['parent_district'] = parent_district
		if(postalcode != ''): 
			params['postalcode'] = postalcode
		if(searchable_id != ''): 
			params['searchable_id'] = searchable_id
		if(searchable_ids != ''): 
			params['searchable_ids'] = searchable_ids
		return self.doCurl("POST","/location",params)
  


	'''
	Read multiple locations with the supplied ID in the locations reference database.
	@param location_ids
	@return - the data from the api
	'''
	def getLocationMultiple(self,location_ids=''):
		params = {}
		if(location_ids != ''): 
			params['location_ids'] = location_ids
		return self.doCurl("GET","/location/multiple",params)
  


	'''
	Fetch the project logo, the symbol of the Wolf
	@param a
	@param b
	@param c
	@param d
	@return - the data from the api
	'''
	def getLogo(self,a='',b='',c='',d=''):
		params = {}
		if(a != ''): 
			params['a'] = a
		if(b != ''): 
			params['b'] = b
		if(c != ''): 
			params['c'] = c
		if(d != ''): 
			params['d'] = d
		return self.doCurl("GET","/logo",params)
  


	'''
	Fetch the project logo, the symbol of the Wolf
	@param a
	@return - the data from the api
	'''
	def putLogo(self,a=''):
		params = {}
		if(a != ''): 
			params['a'] = a
		return self.doCurl("PUT","/logo",params)
  


	'''
	Find a category from cache or cloudant depending if it is in the cache
	@param string - A string to search against, E.g. Plumbers
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getLookupCategory(self,string='',language=''):
		params = {}
		if(string != ''): 
			params['string'] = string
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/lookup/category",params)
  


	'''
	Find a category from a legacy ID or supplier (e.g. bill_moss)
	@param id
	@param type
	@return - the data from the api
	'''
	def getLookupLegacyCategory(self,id='',type=''):
		params = {}
		if(id != ''): 
			params['id'] = id
		if(type != ''): 
			params['type'] = type
		return self.doCurl("GET","/lookup/legacy/category",params)
  


	'''
	Find a location from cache or cloudant depending if it is in the cache (locz)
	@param string
	@param language
	@param country
	@param latitude
	@param longitude
	@return - the data from the api
	'''
	def getLookupLocation(self,string='',language='',country='',latitude='',longitude=''):
		params = {}
		if(string != ''): 
			params['string'] = string
		if(language != ''): 
			params['language'] = language
		if(country != ''): 
			params['country'] = country
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		return self.doCurl("GET","/lookup/location",params)
  


	'''
	Find all matches by phone number and then return all matches that also match company name and location. Default location_strictness is defined in Km and the default is set to 0.2 (200m)
	@param phone
	@param company_name
	@param latitude
	@param longitude
	@param postcode
	@param country
	@param name_strictness
	@param location_strictness
	@return - the data from the api
	'''
	def getMatchByphone(self,phone='',company_name='',latitude='',longitude='',postcode='',country='',name_strictness='',location_strictness=''):
		params = {}
		if(phone != ''): 
			params['phone'] = phone
		if(company_name != ''): 
			params['company_name'] = company_name
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		if(postcode != ''): 
			params['postcode'] = postcode
		if(country != ''): 
			params['country'] = country
		if(name_strictness != ''): 
			params['name_strictness'] = name_strictness
		if(location_strictness != ''): 
			params['location_strictness'] = location_strictness
		return self.doCurl("GET","/match/byphone",params)
  


	'''
	Find all matches by phone number, returning up to 10 matches
	@param phone
	@param country
	@param exclude - Entity ID to exclude from the results
	@return - the data from the api
	'''
	def getMatchByphone2(self,phone='',country='',exclude=''):
		params = {}
		if(phone != ''): 
			params['phone'] = phone
		if(country != ''): 
			params['country'] = country
		if(exclude != ''): 
			params['exclude'] = exclude
		return self.doCurl("GET","/match/byphone2",params)
  


	'''
	Perform a match on the two supplied entities, returning the outcome and showing our working
	@param primary_entity_id
	@param secondary_entity_id
	@param return_entities - Should we return the entity documents
	@return - the data from the api
	'''
	def getMatchOftheday(self,primary_entity_id='',secondary_entity_id='',return_entities=''):
		params = {}
		if(primary_entity_id != ''): 
			params['primary_entity_id'] = primary_entity_id
		if(secondary_entity_id != ''): 
			params['secondary_entity_id'] = secondary_entity_id
		if(return_entities != ''): 
			params['return_entities'] = return_entities
		return self.doCurl("GET","/match/oftheday",params)
  


	'''
	Update/Add a message
	@param message_id - Message id to pull
	@param ses_id - Aamazon email id
	@param from_user_id - User sending the message
	@param from_email - Sent from email address
	@param to_entity_id - The id of the entity being sent the message
	@param to_email - Sent from email address
	@param subject - Subject for the message
	@param body - Body for the message
	@param bounced - If the message bounced
	@return - the data from the api
	'''
	def postMessage(self,message_id='',ses_id='',from_user_id='',from_email='',to_entity_id='',to_email='',subject='',body='',bounced=''):
		params = {}
		if(message_id != ''): 
			params['message_id'] = message_id
		if(ses_id != ''): 
			params['ses_id'] = ses_id
		if(from_user_id != ''): 
			params['from_user_id'] = from_user_id
		if(from_email != ''): 
			params['from_email'] = from_email
		if(to_entity_id != ''): 
			params['to_entity_id'] = to_entity_id
		if(to_email != ''): 
			params['to_email'] = to_email
		if(subject != ''): 
			params['subject'] = subject
		if(body != ''): 
			params['body'] = body
		if(bounced != ''): 
			params['bounced'] = bounced
		return self.doCurl("POST","/message",params)
  


	'''
	Fetching a message
	@param message_id - The message id to pull the message for
	@return - the data from the api
	'''
	def getMessage(self,message_id=''):
		params = {}
		if(message_id != ''): 
			params['message_id'] = message_id
		return self.doCurl("GET","/message",params)
  


	'''
	Fetching messages by ses_id
	@param ses_id - The amazon id to pull the message for
	@return - the data from the api
	'''
	def getMessageBy_ses_id(self,ses_id=''):
		params = {}
		if(ses_id != ''): 
			params['ses_id'] = ses_id
		return self.doCurl("GET","/message/by_ses_id",params)
  


	'''
	With a known entity id, a private object can be added.
	@param entity_id - The entity to associate the private object with
	@param data - The data to store
	@return - the data from the api
	'''
	def putPrivate_object(self,entity_id='',data=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(data != ''): 
			params['data'] = data
		return self.doCurl("PUT","/private_object",params)
  


	'''
	Allows a private object to be removed
	@param private_object_id - The id of the private object to remove
	@return - the data from the api
	'''
	def deletePrivate_object(self,private_object_id=''):
		params = {}
		if(private_object_id != ''): 
			params['private_object_id'] = private_object_id
		return self.doCurl("DELETE","/private_object",params)
  


	'''
	Allows a private object to be returned based on the entity_id and masheryid
	@param entity_id - The entity associated with the private object
	@return - the data from the api
	'''
	def getPrivate_objectAll(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/private_object/all",params)
  


	'''
	Perform the whole PTB process on the supplied entity
	@param entity_id
	@param destructive
	@return - the data from the api
	'''
	def getPtbAll(self,entity_id='',destructive=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(destructive != ''): 
			params['destructive'] = destructive
		return self.doCurl("GET","/ptb/all",params)
  


	'''
	Report on what happened to specific entity_id
	@param year - the year to examine
	@param month - the month to examine
	@param entity_id - the entity to research
	@return - the data from the api
	'''
	def getPtbLog(self,year='',month='',entity_id=''):
		params = {}
		if(year != ''): 
			params['year'] = year
		if(month != ''): 
			params['month'] = month
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/ptb/log",params)
  


	'''
	Process an entity with a specific PTB module
	@param entity_id
	@param module
	@param destructive
	@return - the data from the api
	'''
	def getPtbModule(self,entity_id='',module='',destructive=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(module != ''): 
			params['module'] = module
		if(destructive != ''): 
			params['destructive'] = destructive
		return self.doCurl("GET","/ptb/module",params)
  


	'''
	Report on the run-rate of the Paint the Bridge System
	@param country - the country to get the runrate for
	@param year - the year to examine
	@param month - the month to examine
	@param day - the day to examine
	@return - the data from the api
	'''
	def getPtbRunrate(self,country='',year='',month='',day=''):
		params = {}
		if(country != ''): 
			params['country'] = country
		if(year != ''): 
			params['year'] = year
		if(month != ''): 
			params['month'] = month
		if(day != ''): 
			params['day'] = day
		return self.doCurl("GET","/ptb/runrate",params)
  


	'''
	Report on the value being added by Paint The Bridge
	@param country - the country to get the runrate for
	@param year - the year to examine
	@param month - the month to examine
	@param day - the day to examine
	@return - the data from the api
	'''
	def getPtbValueadded(self,country='',year='',month='',day=''):
		params = {}
		if(country != ''): 
			params['country'] = country
		if(year != ''): 
			params['year'] = year
		if(month != ''): 
			params['month'] = month
		if(day != ''): 
			params['day'] = day
		return self.doCurl("GET","/ptb/valueadded",params)
  


	'''
	Returns publisher that matches a given publisher id
	@param publisher_id
	@return - the data from the api
	'''
	def getPublisher(self,publisher_id=''):
		params = {}
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		return self.doCurl("GET","/publisher",params)
  


	'''
	Delete a publisher with a specified publisher_id
	@param publisher_id
	@return - the data from the api
	'''
	def deletePublisher(self,publisher_id=''):
		params = {}
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		return self.doCurl("DELETE","/publisher",params)
  


	'''
	Update/Add a publisher
	@param publisher_id
	@param country
	@param name
	@param description
	@param active
	@return - the data from the api
	'''
	def postPublisher(self,publisher_id='',country='',name='',description='',active=''):
		params = {}
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(country != ''): 
			params['country'] = country
		if(name != ''): 
			params['name'] = name
		if(description != ''): 
			params['description'] = description
		if(active != ''): 
			params['active'] = active
		return self.doCurl("POST","/publisher",params)
  


	'''
	Returns publisher that matches a given publisher id
	@param country
	@return - the data from the api
	'''
	def getPublisherByCountry(self,country=''):
		params = {}
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/publisher/byCountry",params)
  


	'''
	Returns publishers that are available for a given entity_id.
	@param entity_id
	@return - the data from the api
	'''
	def getPublisherByEntityId(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/publisher/byEntityId",params)
  


	'''
	Create a queue item
	@param queue_name
	@param data
	@return - the data from the api
	'''
	def putQueue(self,queue_name='',data=''):
		params = {}
		if(queue_name != ''): 
			params['queue_name'] = queue_name
		if(data != ''): 
			params['data'] = data
		return self.doCurl("PUT","/queue",params)
  


	'''
	With a known queue id, a queue item can be removed.
	@param queue_id
	@return - the data from the api
	'''
	def deleteQueue(self,queue_id=''):
		params = {}
		if(queue_id != ''): 
			params['queue_id'] = queue_id
		return self.doCurl("DELETE","/queue",params)
  


	'''
	Retrieve queue items.
	@param limit
	@param queue_name
	@return - the data from the api
	'''
	def getQueue(self,limit='',queue_name=''):
		params = {}
		if(limit != ''): 
			params['limit'] = limit
		if(queue_name != ''): 
			params['queue_name'] = queue_name
		return self.doCurl("GET","/queue",params)
  


	'''
	Add an error to a queue item
	@param queue_id
	@param error
	@return - the data from the api
	'''
	def postQueueError(self,queue_id='',error=''):
		params = {}
		if(queue_id != ''): 
			params['queue_id'] = queue_id
		if(error != ''): 
			params['error'] = error
		return self.doCurl("POST","/queue/error",params)
  


	'''
	Find a queue item by its type and id
	@param type
	@param id
	@return - the data from the api
	'''
	def getQueueSearch(self,type='',id=''):
		params = {}
		if(type != ''): 
			params['type'] = type
		if(id != ''): 
			params['id'] = id
		return self.doCurl("GET","/queue/search",params)
  


	'''
	Unlock queue items.
	@param queue_name
	@param seconds
	@return - the data from the api
	'''
	def postQueueUnlock(self,queue_name='',seconds=''):
		params = {}
		if(queue_name != ''): 
			params['queue_name'] = queue_name
		if(seconds != ''): 
			params['seconds'] = seconds
		return self.doCurl("POST","/queue/unlock",params)
  


	'''
	Return a sales log by id
	@param sales_log_id - The sales log id to pull
	@return - the data from the api
	'''
	def getSales_log(self,sales_log_id=''):
		params = {}
		if(sales_log_id != ''): 
			params['sales_log_id'] = sales_log_id
		return self.doCurl("GET","/sales_log",params)
  


	'''
	Return a sales log by id
	@param from_date
	@param country
	@param action_type
	@return - the data from the api
	'''
	def getSales_logBy_countryBy_date(self,from_date='',country='',action_type=''):
		params = {}
		if(from_date != ''): 
			params['from_date'] = from_date
		if(country != ''): 
			params['country'] = country
		if(action_type != ''): 
			params['action_type'] = action_type
		return self.doCurl("GET","/sales_log/by_country/by_date",params)
  


	'''
	Return a sales log by id
	@param from_date
	@param to_date
	@return - the data from the api
	'''
	def getSales_logBy_date(self,from_date='',to_date=''):
		params = {}
		if(from_date != ''): 
			params['from_date'] = from_date
		if(to_date != ''): 
			params['to_date'] = to_date
		return self.doCurl("GET","/sales_log/by_date",params)
  


	'''
	Log a sale
	@param entity_id - The entity the sale was made against
	@param country - The country code the sales log orginated
	@param action_type - The type of action we are performing
	@param publisher_id - The publisher id that has made the sale
	@param mashery_id - The mashery id
	@param reseller_ref - The reference of the sale made by the seller
	@param reseller_agent_id - The id of the agent selling the product
	@param max_tags - The number of tags available to the entity
	@param max_locations - The number of locations available to the entity
	@param extra_tags - The extra number of tags
	@param extra_locations - The extra number of locations
	@param expiry_date - The date the product expires
	@return - the data from the api
	'''
	def postSales_logEntity(self,entity_id='',country='',action_type='',publisher_id='',mashery_id='',reseller_ref='',reseller_agent_id='',max_tags='',max_locations='',extra_tags='',extra_locations='',expiry_date=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(country != ''): 
			params['country'] = country
		if(action_type != ''): 
			params['action_type'] = action_type
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(mashery_id != ''): 
			params['mashery_id'] = mashery_id
		if(reseller_ref != ''): 
			params['reseller_ref'] = reseller_ref
		if(reseller_agent_id != ''): 
			params['reseller_agent_id'] = reseller_agent_id
		if(max_tags != ''): 
			params['max_tags'] = max_tags
		if(max_locations != ''): 
			params['max_locations'] = max_locations
		if(extra_tags != ''): 
			params['extra_tags'] = extra_tags
		if(extra_locations != ''): 
			params['extra_locations'] = extra_locations
		if(expiry_date != ''): 
			params['expiry_date'] = expiry_date
		return self.doCurl("POST","/sales_log/entity",params)
  


	'''
	Add a Sales Log document for a syndication action
	@param action_type
	@param syndication_type
	@param publisher_id
	@param expiry_date
	@param entity_id
	@param group_id
	@param seed_masheryid
	@param supplier_masheryid
	@param country
	@param reseller_masheryid
	@return - the data from the api
	'''
	def postSales_logSyndication(self,action_type='',syndication_type='',publisher_id='',expiry_date='',entity_id='',group_id='',seed_masheryid='',supplier_masheryid='',country='',reseller_masheryid=''):
		params = {}
		if(action_type != ''): 
			params['action_type'] = action_type
		if(syndication_type != ''): 
			params['syndication_type'] = syndication_type
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(expiry_date != ''): 
			params['expiry_date'] = expiry_date
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(group_id != ''): 
			params['group_id'] = group_id
		if(seed_masheryid != ''): 
			params['seed_masheryid'] = seed_masheryid
		if(supplier_masheryid != ''): 
			params['supplier_masheryid'] = supplier_masheryid
		if(country != ''): 
			params['country'] = country
		if(reseller_masheryid != ''): 
			params['reseller_masheryid'] = reseller_masheryid
		return self.doCurl("POST","/sales_log/syndication",params)
  


	'''
	For insance, reporting a phone number as wrong
	@param entity_id - A valid entity_id e.g. 379236608286720
	@param country - The country code from where the signal originated e.g. ie
	@param gen_id - The gen_id for the item being reported
	@param signal_type - The signal that is to be reported e.g. wrong
	@param data_type - The type of data being reported
	@param inactive_reason - The reason for making the entity inactive
	@param inactive_description - A description to accompany the inactive reasoning
	@return - the data from the api
	'''
	def postSignal(self,entity_id='',country='',gen_id='',signal_type='',data_type='',inactive_reason='',inactive_description=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(country != ''): 
			params['country'] = country
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		if(signal_type != ''): 
			params['signal_type'] = signal_type
		if(data_type != ''): 
			params['data_type'] = data_type
		if(inactive_reason != ''): 
			params['inactive_reason'] = inactive_reason
		if(inactive_description != ''): 
			params['inactive_description'] = inactive_description
		return self.doCurl("POST","/signal",params)
  


	'''
	Get the number of times an entity has been served out as an advert or on serps/bdp pages
	@param entity_id - A valid entity_id e.g. 379236608286720
	@param year - The year to report on
	@param month - The month to report on
	@return - the data from the api
	'''
	def getStatsEntityBy_date(self,entity_id='',year='',month=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(year != ''): 
			params['year'] = year
		if(month != ''): 
			params['month'] = month
		return self.doCurl("GET","/stats/entity/by_date",params)
  


	'''
	Get the stats on an entity in a given year
	@param entity_id - A valid entity_id e.g. 379236608286720
	@param year - The year to report on
	@return - the data from the api
	'''
	def getStatsEntityBy_year(self,entity_id='',year=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(year != ''): 
			params['year'] = year
		return self.doCurl("GET","/stats/entity/by_year",params)
  


	'''
	Confirms that the API is active, and returns the current version number
	@return - the data from the api
	'''
	def getStatus(self):
		params = {}
		return self.doCurl("GET","/status",params)
  


	'''
	Add a Syndicate
	@param syndication_type
	@param publisher_id
	@param expiry_date
	@param entity_id
	@param group_id
	@param seed_masheryid
	@param supplier_masheryid
	@param country
	@return - the data from the api
	'''
	def postSyndicationCreate(self,syndication_type='',publisher_id='',expiry_date='',entity_id='',group_id='',seed_masheryid='',supplier_masheryid='',country=''):
		params = {}
		if(syndication_type != ''): 
			params['syndication_type'] = syndication_type
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(expiry_date != ''): 
			params['expiry_date'] = expiry_date
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(group_id != ''): 
			params['group_id'] = group_id
		if(seed_masheryid != ''): 
			params['seed_masheryid'] = seed_masheryid
		if(supplier_masheryid != ''): 
			params['supplier_masheryid'] = supplier_masheryid
		if(country != ''): 
			params['country'] = country
		return self.doCurl("POST","/syndication/create",params)
  


	'''
	When we get a syndication update make a record of it
	@param entity_id - The entity to pull
	@param publisher_id - The publisher this log entry refers to
	@param action - The log type
	@param success - If the syndication was successful
	@param message - An optional message e.g. submitted to the syndication partner
	@param syndicated_id - The entity as known to the publisher
	@return - the data from the api
	'''
	def postSyndication_log(self,entity_id='',publisher_id='',action='',success='',message='',syndicated_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(publisher_id != ''): 
			params['publisher_id'] = publisher_id
		if(action != ''): 
			params['action'] = action
		if(success != ''): 
			params['success'] = success
		if(message != ''): 
			params['message'] = message
		if(syndicated_id != ''): 
			params['syndicated_id'] = syndicated_id
		return self.doCurl("POST","/syndication_log",params)
  


	'''
	Get all syndication log entries for a given entity id
	@param entity_id
	@return - the data from the api
	'''
	def getSyndication_logBy_entity_id(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/syndication_log/by_entity_id",params)
  


	'''
	Provides a tokenised URL to redirect a user so they can add an entity to Central Index
	@param language - The language to use to render the add path e.g. en
	@param portal_name - The name of the website that data is to be added on e.g. YourLocal
	@param country - The country of the entity to be added e.g. gb
	@param flatpack_id - The id of the flatpack site where the request originated
	@return - the data from the api
	'''
	def getTokenAdd(self,language='',portal_name='',country='',flatpack_id=''):
		params = {}
		if(language != ''): 
			params['language'] = language
		if(portal_name != ''): 
			params['portal_name'] = portal_name
		if(country != ''): 
			params['country'] = country
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("GET","/token/add",params)
  


	'''
	Provides a tokenised URL to redirect a user to claim an entity on Central Index
	@param entity_id - Entity ID to be claimed e.g. 380348266819584
	@param language - The language to use to render the claim path e.g. en
	@param portal_name - The name of the website that entity is being claimed on e.g. YourLocal
	@param flatpack_id - The id of the flatpack site where the request originated
	@return - the data from the api
	'''
	def getTokenClaim(self,entity_id='',language='',portal_name='',flatpack_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(language != ''): 
			params['language'] = language
		if(portal_name != ''): 
			params['portal_name'] = portal_name
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("GET","/token/claim",params)
  


	'''
	Allows us to identify the user, entity and element from an encoded endpoint URL's token
	@param token
	@return - the data from the api
	'''
	def getTokenDecode(self,token=''):
		params = {}
		if(token != ''): 
			params['token'] = token
		return self.doCurl("GET","/token/decode",params)
  


	'''
	Fetch token for edit path
	@param entity_id - The id of the entity being upgraded
	@param language - The language for the app
	@param flatpack_id - The id of the flatpack site where the request originated
	@param edit_page - the page in the edit path that the user should land on
	@return - the data from the api
	'''
	def getTokenEdit(self,entity_id='',language='',flatpack_id='',edit_page=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(language != ''): 
			params['language'] = language
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		if(edit_page != ''): 
			params['edit_page'] = edit_page
		return self.doCurl("GET","/token/edit",params)
  


	'''
	Fetch token for login path
	@param portal_name - The name of the application that has initiated the login process, example: 'Your Local'
	@param language - The language for the app
	@param flatpack_id - The id of the flatpack site where the request originated
	@return - the data from the api
	'''
	def getTokenLogin(self,portal_name='',language='',flatpack_id=''):
		params = {}
		if(portal_name != ''): 
			params['portal_name'] = portal_name
		if(language != ''): 
			params['language'] = language
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("GET","/token/login",params)
  


	'''
	Fetch token for messaging path
	@param entity_id - The id of the entity being messaged
	@param portal_name - The name of the application that has initiated the email process, example: 'Your Local'
	@param language - The language for the app
	@param flatpack_id - The id of the flatpack site where the request originated
	@return - the data from the api
	'''
	def getTokenMessage(self,entity_id='',portal_name='',language='',flatpack_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(portal_name != ''): 
			params['portal_name'] = portal_name
		if(language != ''): 
			params['language'] = language
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("GET","/token/message",params)
  


	'''
	Provides a tokenised URL that allows a user to report incorrect entity information
	@param entity_id - The unique Entity ID e.g. 379236608286720
	@param portal_name - The name of the portal that the user is coming from e.g. YourLocal
	@param language - The language to use to render the report path
	@param flatpack_id - The id of the flatpack site where the request originated
	@return - the data from the api
	'''
	def getTokenReport(self,entity_id='',portal_name='',language='',flatpack_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(portal_name != ''): 
			params['portal_name'] = portal_name
		if(language != ''): 
			params['language'] = language
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("GET","/token/report",params)
  


	'''
	Fetch token for update path
	@param entity_id - The id of the entity being upgraded
	@param portal_name - The name of the application that has initiated the login process, example: 'Your Local'
	@param language - The language for the app
	@param price - The price of the advert in the entities native currency
	@param max_tags - The number of tags attached to the advert
	@param max_locations - The number of locations attached to the advert
	@param contract_length - The number of days from the initial sale date that the contract is valid for
	@param ref_id - The campaign or reference id
	@param flatpack_id - The id of the flatpack site where the request originated
	@return - the data from the api
	'''
	def getTokenUpgrade(self,entity_id='',portal_name='',language='',price='',max_tags='',max_locations='',contract_length='',ref_id='',flatpack_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(portal_name != ''): 
			params['portal_name'] = portal_name
		if(language != ''): 
			params['language'] = language
		if(price != ''): 
			params['price'] = price
		if(max_tags != ''): 
			params['max_tags'] = max_tags
		if(max_locations != ''): 
			params['max_locations'] = max_locations
		if(contract_length != ''): 
			params['contract_length'] = contract_length
		if(ref_id != ''): 
			params['ref_id'] = ref_id
		if(flatpack_id != ''): 
			params['flatpack_id'] = flatpack_id
		return self.doCurl("GET","/token/upgrade",params)
  


	'''
	The JaroWinklerDistance between two entities postal address objects
	@param first_entity_id - The entity id of the first entity to be used in the postal address difference
	@param second_entity_id - The entity id of the second entity to be used in the postal address difference
	@return - the data from the api
	'''
	def getToolsAddressdiff(self,first_entity_id='',second_entity_id=''):
		params = {}
		if(first_entity_id != ''): 
			params['first_entity_id'] = first_entity_id
		if(second_entity_id != ''): 
			params['second_entity_id'] = second_entity_id
		return self.doCurl("GET","/tools/addressdiff",params)
  


	'''
	Use this call to get information (in HTML or JSON) about the data structure of given entity object (e.g. a phone number or an address)
	@param object - The API call documentation is required for
	@param format - The format of the returned data eg. JSON or HTML
	@return - the data from the api
	'''
	def getToolsDocs(self,object='',format=''):
		params = {}
		if(object != ''): 
			params['object'] = object
		if(format != ''): 
			params['format'] = format
		return self.doCurl("GET","/tools/docs",params)
  


	'''
	Format an address according to the rules of the country supplied
	@param address - The address to format
	@param country - The country where the address is based
	@return - the data from the api
	'''
	def getToolsFormatAddress(self,address='',country=''):
		params = {}
		if(address != ''): 
			params['address'] = address
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/tools/format/address",params)
  


	'''
	Format a phone number according to the rules of the country supplied
	@param number - The telephone number to format
	@param country - The country where the telephone number is based
	@return - the data from the api
	'''
	def getToolsFormatPhone(self,number='',country=''):
		params = {}
		if(number != ''): 
			params['number'] = number
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/tools/format/phone",params)
  


	'''
	Supply an address to geocode - returns lat/lon and accuracy
	@param building_number
	@param address1
	@param address2
	@param address3
	@param district
	@param town
	@param county
	@param province
	@param postcode
	@param country
	@return - the data from the api
	'''
	def getToolsGeocode(self,building_number='',address1='',address2='',address3='',district='',town='',county='',province='',postcode='',country=''):
		params = {}
		if(building_number != ''): 
			params['building_number'] = building_number
		if(address1 != ''): 
			params['address1'] = address1
		if(address2 != ''): 
			params['address2'] = address2
		if(address3 != ''): 
			params['address3'] = address3
		if(district != ''): 
			params['district'] = district
		if(town != ''): 
			params['town'] = town
		if(county != ''): 
			params['county'] = county
		if(province != ''): 
			params['province'] = province
		if(postcode != ''): 
			params['postcode'] = postcode
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/tools/geocode",params)
  


	'''
	Given a spreadsheet id add a row
	@param spreadsheet_key - The key of the spreadsheet to edit
	@param data - A comma separated list to add as cells
	@return - the data from the api
	'''
	def postToolsGooglesheetAdd_row(self,spreadsheet_key='',data=''):
		params = {}
		if(spreadsheet_key != ''): 
			params['spreadsheet_key'] = spreadsheet_key
		if(data != ''): 
			params['data'] = data
		return self.doCurl("POST","/tools/googlesheet/add_row",params)
  


	'''
	Given some image data we can resize and upload the images
	@param filedata - The image data to upload and resize
	@param type - The type of image to upload and resize
	@return - the data from the api
	'''
	def postToolsImage(self,filedata='',type=''):
		params = {}
		if(filedata != ''): 
			params['filedata'] = filedata
		if(type != ''): 
			params['type'] = type
		return self.doCurl("POST","/tools/image",params)
  


	'''
	Generate JSON in the format to generate Mashery's IODocs
	@param mode - The HTTP method of the API call to document. e.g. GET
	@param path - The path of the API call to document e.g, /entity
	@param endpoint - The Mashery 'endpoint' to prefix to our API paths e.g. v1
	@param doctype - Mashery has two forms of JSON to describe API methods; one on github, the other on its customer dashboard
	@return - the data from the api
	'''
	def getToolsIodocs(self,mode='',path='',endpoint='',doctype=''):
		params = {}
		if(mode != ''): 
			params['mode'] = mode
		if(path != ''): 
			params['path'] = path
		if(endpoint != ''): 
			params['endpoint'] = endpoint
		if(doctype != ''): 
			params['doctype'] = doctype
		return self.doCurl("GET","/tools/iodocs",params)
  


	'''
	compile the supplied less with the standard Bootstrap less into a CSS file
	@param less - The LESS code to compile
	@return - the data from the api
	'''
	def getToolsLess(self,less=''):
		params = {}
		if(less != ''): 
			params['less'] = less
		return self.doCurl("GET","/tools/less",params)
  


	'''
	Ring the person and verify their account
	@param to - The phone number to verify
	@param from - The phone number to call from
	@param pin - The pin to verify the phone number with
	@param twilio_voice - The language to read the verification in
	@return - the data from the api
	'''
	def getToolsPhonecallVerify(self,to='',from2='',pin='',twilio_voice=''):
		params = {}
		if(to != ''): 
			params['to'] = to
		if(from2 != ''): 
			params['from2'] = from2
		if(pin != ''): 
			params['pin'] = pin
		if(twilio_voice != ''): 
			params['twilio_voice'] = twilio_voice
		return self.doCurl("GET","/tools/phonecall/verify",params)
  


	'''
	Return the phonetic representation of a string
	@param text
	@return - the data from the api
	'''
	def getToolsPhonetic(self,text=''):
		params = {}
		if(text != ''): 
			params['text'] = text
		return self.doCurl("GET","/tools/phonetic",params)
  


	'''
	Attempt to process a phone number, removing anything which is not a digit
	@param number
	@return - the data from the api
	'''
	def getToolsProcess_phone(self,number=''):
		params = {}
		if(number != ''): 
			params['number'] = number
		return self.doCurl("GET","/tools/process_phone",params)
  


	'''
	Fully process a string. This includes removing punctuation, stops words and stemming a string. Also returns the phonetic representation of this string.
	@param text
	@return - the data from the api
	'''
	def getToolsProcess_string(self,text=''):
		params = {}
		if(text != ''): 
			params['text'] = text
		return self.doCurl("GET","/tools/process_string",params)
  


	'''
	Force refresh of search indexes
	@return - the data from the api
	'''
	def getToolsReindex(self):
		params = {}
		return self.doCurl("GET","/tools/reindex",params)
  


	'''
	replace some text parameters with some entity details
	@param entity_id - The entity to pull for replacements
	@param string - The string full of parameters
	@return - the data from the api
	'''
	def getToolsReplace(self,entity_id='',string=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(string != ''): 
			params['string'] = string
		return self.doCurl("GET","/tools/replace",params)
  


	'''
	Check to see if a supplied email address is valid
	@param from - The phone number from which the SMS orginates
	@param to - The phone number to which the SMS is to be sent
	@param message - The message to be sent in the SMS
	@return - the data from the api
	'''
	def getToolsSendsms(self,from2='',to='',message=''):
		params = {}
		if(from2 != ''): 
			params['from2'] = from2
		if(to != ''): 
			params['to'] = to
		if(message != ''): 
			params['message'] = message
		return self.doCurl("GET","/tools/sendsms",params)
  


	'''
	Spider a single url looking for key facts
	@param url
	@param pages
	@param country
	@return - the data from the api
	'''
	def getToolsSpider(self,url='',pages='',country=''):
		params = {}
		if(url != ''): 
			params['url'] = url
		if(pages != ''): 
			params['pages'] = pages
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/tools/spider",params)
  


	'''
	Returns a stemmed version of a string
	@param text
	@return - the data from the api
	'''
	def getToolsStem(self,text=''):
		params = {}
		if(text != ''): 
			params['text'] = text
		return self.doCurl("GET","/tools/stem",params)
  


	'''
	Removes stopwords from a string
	@param text
	@return - the data from the api
	'''
	def getToolsStopwords(self,text=''):
		params = {}
		if(text != ''): 
			params['text'] = text
		return self.doCurl("GET","/tools/stopwords",params)
  


	'''
	Fetch the entity and convert it to DnB TSV format
	@param entity_id - The entity_id to fetch
	@return - the data from the api
	'''
	def getToolsSyndicateDnb(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/tools/syndicate/dnb",params)
  


	'''
	Fetch the entity and convert it to TomTom XML format
	@param entity_id - The entity_id to fetch
	@return - the data from the api
	'''
	def getToolsSyndicateGoogle(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/tools/syndicate/google",params)
  


	'''
	Fetch the entity and convert it to Google KML format
	@param entity_id - The entity_id to fetch
	@return - the data from the api
	'''
	def getToolsSyndicateKml(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/tools/syndicate/kml",params)
  


	'''
	Fetch the entity and convert it to Nokia CSV format
	@param entity_id - The entity_id to fetch
	@return - the data from the api
	'''
	def getToolsSyndicateNokia(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/tools/syndicate/nokia",params)
  


	'''
	Fetch the entity and convert it to TomTom XML format
	@param entity_id - The entity_id to fetch
	@return - the data from the api
	'''
	def getToolsSyndicateTomtom(self,entity_id=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("GET","/tools/syndicate/tomtom",params)
  


	'''
	Check to see if a supplied email address is valid
	@param email_address - The email address to validate
	@return - the data from the api
	'''
	def getToolsValidate_email(self,email_address=''):
		params = {}
		if(email_address != ''): 
			params['email_address'] = email_address
		return self.doCurl("GET","/tools/validate_email",params)
  


	'''
	Calls a number to make sure it is active
	@param phone_number - The phone number to validate
	@param country - The country code of the phone number to be validated
	@return - the data from the api
	'''
	def getToolsValidate_phone(self,phone_number='',country=''):
		params = {}
		if(phone_number != ''): 
			params['phone_number'] = phone_number
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/tools/validate_phone",params)
  


	'''
	Deleting a traction
	@param traction_id
	@return - the data from the api
	'''
	def deleteTraction(self,traction_id=''):
		params = {}
		if(traction_id != ''): 
			params['traction_id'] = traction_id
		return self.doCurl("DELETE","/traction",params)
  


	'''
	Fetching a traction
	@param traction_id
	@return - the data from the api
	'''
	def getTraction(self,traction_id=''):
		params = {}
		if(traction_id != ''): 
			params['traction_id'] = traction_id
		return self.doCurl("GET","/traction",params)
  


	'''
	Update/Add a traction
	@param traction_id
	@param trigger_type
	@param action_type
	@param country
	@param email_addresses
	@param title
	@param body
	@param api_method
	@param api_url
	@param api_params
	@param active
	@param reseller_masheryid
	@param publisher_masheryid
	@param description
	@return - the data from the api
	'''
	def postTraction(self,traction_id='',trigger_type='',action_type='',country='',email_addresses='',title='',body='',api_method='',api_url='',api_params='',active='',reseller_masheryid='',publisher_masheryid='',description=''):
		params = {}
		if(traction_id != ''): 
			params['traction_id'] = traction_id
		if(trigger_type != ''): 
			params['trigger_type'] = trigger_type
		if(action_type != ''): 
			params['action_type'] = action_type
		if(country != ''): 
			params['country'] = country
		if(email_addresses != ''): 
			params['email_addresses'] = email_addresses
		if(title != ''): 
			params['title'] = title
		if(body != ''): 
			params['body'] = body
		if(api_method != ''): 
			params['api_method'] = api_method
		if(api_url != ''): 
			params['api_url'] = api_url
		if(api_params != ''): 
			params['api_params'] = api_params
		if(active != ''): 
			params['active'] = active
		if(reseller_masheryid != ''): 
			params['reseller_masheryid'] = reseller_masheryid
		if(publisher_masheryid != ''): 
			params['publisher_masheryid'] = publisher_masheryid
		if(description != ''): 
			params['description'] = description
		return self.doCurl("POST","/traction",params)
  


	'''
	Fetching active tractions
	@return - the data from the api
	'''
	def getTractionActive(self):
		params = {}
		return self.doCurl("GET","/traction/active",params)
  


	'''
	Create a new transaction
	@param entity_id
	@param user_id
	@param basket_total
	@param basket
	@param currency
	@param notes
	@return - the data from the api
	'''
	def putTransaction(self,entity_id='',user_id='',basket_total='',basket='',currency='',notes=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(user_id != ''): 
			params['user_id'] = user_id
		if(basket_total != ''): 
			params['basket_total'] = basket_total
		if(basket != ''): 
			params['basket'] = basket
		if(currency != ''): 
			params['currency'] = currency
		if(notes != ''): 
			params['notes'] = notes
		return self.doCurl("PUT","/transaction",params)
  


	'''
	Given a transaction_id retrieve information on it
	@param transaction_id
	@return - the data from the api
	'''
	def getTransaction(self,transaction_id=''):
		params = {}
		if(transaction_id != ''): 
			params['transaction_id'] = transaction_id
		return self.doCurl("GET","/transaction",params)
  


	'''
	Set a transactions status to authorised
	@param transaction_id
	@param paypal_getexpresscheckoutdetails
	@return - the data from the api
	'''
	def postTransactionAuthorised(self,transaction_id='',paypal_getexpresscheckoutdetails=''):
		params = {}
		if(transaction_id != ''): 
			params['transaction_id'] = transaction_id
		if(paypal_getexpresscheckoutdetails != ''): 
			params['paypal_getexpresscheckoutdetails'] = paypal_getexpresscheckoutdetails
		return self.doCurl("POST","/transaction/authorised",params)
  


	'''
	Given a transaction_id retrieve information on it
	@param paypal_transaction_id
	@return - the data from the api
	'''
	def getTransactionBy_paypal_transaction_id(self,paypal_transaction_id=''):
		params = {}
		if(paypal_transaction_id != ''): 
			params['paypal_transaction_id'] = paypal_transaction_id
		return self.doCurl("GET","/transaction/by_paypal_transaction_id",params)
  


	'''
	Set a transactions status to cancelled
	@param transaction_id
	@return - the data from the api
	'''
	def postTransactionCancelled(self,transaction_id=''):
		params = {}
		if(transaction_id != ''): 
			params['transaction_id'] = transaction_id
		return self.doCurl("POST","/transaction/cancelled",params)
  


	'''
	Set a transactions status to complete
	@param transaction_id
	@param paypal_doexpresscheckoutpayment
	@param user_id
	@param entity_id
	@return - the data from the api
	'''
	def postTransactionComplete(self,transaction_id='',paypal_doexpresscheckoutpayment='',user_id='',entity_id=''):
		params = {}
		if(transaction_id != ''): 
			params['transaction_id'] = transaction_id
		if(paypal_doexpresscheckoutpayment != ''): 
			params['paypal_doexpresscheckoutpayment'] = paypal_doexpresscheckoutpayment
		if(user_id != ''): 
			params['user_id'] = user_id
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		return self.doCurl("POST","/transaction/complete",params)
  


	'''
	Set a transactions status to inprogess
	@param transaction_id
	@param paypal_setexpresscheckout
	@return - the data from the api
	'''
	def postTransactionInprogress(self,transaction_id='',paypal_setexpresscheckout=''):
		params = {}
		if(transaction_id != ''): 
			params['transaction_id'] = transaction_id
		if(paypal_setexpresscheckout != ''): 
			params['paypal_setexpresscheckout'] = paypal_setexpresscheckout
		return self.doCurl("POST","/transaction/inprogress",params)
  


	'''
	Update user based on email address or social_network/social_network_id
	@param email
	@param user_id
	@param first_name
	@param last_name
	@param active
	@param trust
	@param creation_date
	@param user_type
	@param social_network
	@param social_network_id
	@param reseller_admin_masheryid
	@param group_id
	@param admin_upgrader
	@return - the data from the api
	'''
	def postUser(self,email='',user_id='',first_name='',last_name='',active='',trust='',creation_date='',user_type='',social_network='',social_network_id='',reseller_admin_masheryid='',group_id='',admin_upgrader=''):
		params = {}
		if(email != ''): 
			params['email'] = email
		if(user_id != ''): 
			params['user_id'] = user_id
		if(first_name != ''): 
			params['first_name'] = first_name
		if(last_name != ''): 
			params['last_name'] = last_name
		if(active != ''): 
			params['active'] = active
		if(trust != ''): 
			params['trust'] = trust
		if(creation_date != ''): 
			params['creation_date'] = creation_date
		if(user_type != ''): 
			params['user_type'] = user_type
		if(social_network != ''): 
			params['social_network'] = social_network
		if(social_network_id != ''): 
			params['social_network_id'] = social_network_id
		if(reseller_admin_masheryid != ''): 
			params['reseller_admin_masheryid'] = reseller_admin_masheryid
		if(group_id != ''): 
			params['group_id'] = group_id
		if(admin_upgrader != ''): 
			params['admin_upgrader'] = admin_upgrader
		return self.doCurl("POST","/user",params)
  


	'''
	With a unique ID address an user can be retrieved
	@param user_id
	@return - the data from the api
	'''
	def getUser(self,user_id=''):
		params = {}
		if(user_id != ''): 
			params['user_id'] = user_id
		return self.doCurl("GET","/user",params)
  


	'''
	With a unique email address an user can be retrieved
	@param email
	@return - the data from the api
	'''
	def getUserBy_email(self,email=''):
		params = {}
		if(email != ''): 
			params['email'] = email
		return self.doCurl("GET","/user/by_email",params)
  


	'''
	Returns all the users that match the supplied group_id
	@param group_id
	@return - the data from the api
	'''
	def getUserBy_groupid(self,group_id=''):
		params = {}
		if(group_id != ''): 
			params['group_id'] = group_id
		return self.doCurl("GET","/user/by_groupid",params)
  


	'''
	Returns all the users that match the supplied reseller_admin_masheryid
	@param reseller_admin_masheryid
	@return - the data from the api
	'''
	def getUserBy_reseller_admin_masheryid(self,reseller_admin_masheryid=''):
		params = {}
		if(reseller_admin_masheryid != ''): 
			params['reseller_admin_masheryid'] = reseller_admin_masheryid
		return self.doCurl("GET","/user/by_reseller_admin_masheryid",params)
  


	'''
	With a unique ID address an user can be retrieved
	@param name
	@param id
	@return - the data from the api
	'''
	def getUserBy_social_media(self,name='',id=''):
		params = {}
		if(name != ''): 
			params['name'] = name
		if(id != ''): 
			params['id'] = id
		return self.doCurl("GET","/user/by_social_media",params)
  


	'''
	Removes group_admin privileges from a specified user
	@param user_id
	@return - the data from the api
	'''
	def postUserGroup_admin_remove(self,user_id=''):
		params = {}
		if(user_id != ''): 
			params['user_id'] = user_id
		return self.doCurl("POST","/user/group_admin_remove",params)
  


	'''
	Removes reseller privileges from a specified user
	@param user_id
	@return - the data from the api
	'''
	def postUserReseller_remove(self,user_id=''):
		params = {}
		if(user_id != ''): 
			params['user_id'] = user_id
		return self.doCurl("POST","/user/reseller_remove",params)
  


	'''
	Deletes a specific social network from a user
	@param user_id
	@param social_network
	@return - the data from the api
	'''
	def deleteUserSocial_network(self,user_id='',social_network=''):
		params = {}
		if(user_id != ''): 
			params['user_id'] = user_id
		if(social_network != ''): 
			params['social_network'] = social_network
		return self.doCurl("DELETE","/user/social_network",params)
  


	'''
	Shows what would be emitted by a view, given a document
	@param database - the database being worked on e.g. entities
	@param designdoc - the design document containing the view e.g. _design/report
	@param view - the name of the view to be tested e.g. bydate
	@param doc - the JSON document to be analysed e.g. {}
	@return - the data from the api
	'''
	def getViewhelper(self,database='',designdoc='',view='',doc=''):
		params = {}
		if(database != ''): 
			params['database'] = database
		if(designdoc != ''): 
			params['designdoc'] = designdoc
		if(view != ''): 
			params['view'] = view
		if(doc != ''): 
			params['doc'] = doc
		return self.doCurl("GET","/viewhelper",params)
  





