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
	Confirms that the API is active, and returns the current version number
	@return - the data from the api
	'''
	def getStatus(self):
		params = {}
		return self.doCurl("GET","/status",params)
  


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
	Search for matching entities
	@param what
	@param entity_name
	@param where
	@param per_page
	@param page
	@param longitude
	@param latitude
	@param country
	@param language
	@return - the data from the api
	'''
	def getEntitySearch(self,what='',entity_name='',where='',per_page='',page='',longitude='',latitude='',country='',language=''):
		params = {}
		if(what != ''): 
			params['what'] = what
		if(entity_name != ''): 
			params['entity_name'] = entity_name
		if(where != ''): 
			params['where'] = where
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(longitude != ''): 
			params['longitude'] = longitude
		if(latitude != ''): 
			params['latitude'] = latitude
		if(country != ''): 
			params['country'] = country
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/search",params)
  


	'''
	Search for matching entities
	@param what - What to get results for. E.g. Plumber e.g. plumber
	@param where - The location to get results for. E.g. Dublin e.g. Dublin
	@param per_page - Number of results returned per page
	@param page - Which page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getEntitySearchWhatBylocation(self,what='',where='',per_page='',page='',country='',language=''):
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
		return self.doCurl("GET","/entity/search/what/bylocation",params)
  


	'''
	Search for matching entities
	@param what
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
	@param who
	@param latitude_1
	@param longitude_1
	@param latitude_2
	@param longitude_2
	@param per_page
	@param page
	@param country
	@return - the data from the api
	'''
	def getEntitySearchWhoByboundingbox(self,who='',latitude_1='',longitude_1='',latitude_2='',longitude_2='',per_page='',page='',country=''):
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
		return self.doCurl("GET","/entity/search/who/byboundingbox",params)
  


	'''
	Search for matching entities
	@param who - Company Name e.g. Starbucks
	@param where - The location to get results for. E.g. Dublin e.g. Dublin
	@param per_page - Number of results returned per page
	@param page - Which page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@return - the data from the api
	'''
	def getEntitySearchWhoBylocation(self,who='',where='',per_page='',page='',country=''):
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
		return self.doCurl("GET","/entity/search/who/bylocation",params)
  


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
	@param who - Company name e.g. Starbucks
	@param per_page - How many results per page
	@param page - What page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@return - the data from the api
	'''
	def getEntitySearchWho(self,who='',per_page='',page='',country=''):
		params = {}
		if(who != ''): 
			params['who'] = who
		if(per_page != ''): 
			params['per_page'] = per_page
		if(page != ''): 
			params['page'] = page
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/entity/search/who",params)
  


	'''
	Search for matching entities
	@param where - Location to search for results. E.g. Dublin e.g. Dublin
	@param per_page - How many results per page
	@param page - What page number to retrieve
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie
	@param language - An ISO compatible language code, E.g. en
	@return - the data from the api
	'''
	def getEntitySearchBylocation(self,where='',per_page='',page='',country='',language=''):
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
		return self.doCurl("GET","/entity/search/bylocation",params)
  


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
	Merge two entities into one
	@param from
	@param to
	@return - the data from the api
	'''
	def postEntityMerge(self,from2='',to=''):
		params = {}
		if(from2 != ''): 
			params['from2'] = from2
		if(to != ''): 
			params['to'] = to
		return self.doCurl("POST","/entity/merge",params)
  


	'''
	Force refresh of search indexes
	@return - the data from the api
	'''
	def getToolsReindex(self):
		params = {}
		return self.doCurl("GET","/tools/reindex",params)
  


	'''
	Supply an entity and an object within it (e.g. a phone number), and retrieve a URL that allows the user to report an issue with that object
	@param entity_id - The unique Entity ID e.g. 379236608286720
	@param gen_id - A Unique ID for the object you wish to report, E.g. Phone number e.g. 379236608299008
	@param language
	@return - the data from the api
	'''
	def getEntityReport(self,entity_id='',gen_id='',language=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(gen_id != ''): 
			params['gen_id'] = gen_id
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/report",params)
  


	'''
	Allows us to identify the user, entity and element from an encoded endpoint URL's token
	@param token
	@return - the data from the api
	'''
	def getToolsDecodereport(self,token=''):
		params = {}
		if(token != ''): 
			params['token'] = token
		return self.doCurl("GET","/tools/decodereport",params)
  


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
	Create a new business entity with all it's objects
	@param name
	@param address1
	@param address2
	@param address3
	@param district
	@param town
	@param county
	@param postcode
	@param country
	@param latitude
	@param longitude
	@param timezone
	@param telephone_number
	@param telephone_type
	@param email
	@param website
	@param category_id
	@param category_name
	@return - the data from the api
	'''
	def putBusiness(self,name='',address1='',address2='',address3='',district='',town='',county='',postcode='',country='',latitude='',longitude='',timezone='',telephone_number='',telephone_type='',email='',website='',category_id='',category_name=''):
		params = {}
		if(name != ''): 
			params['name'] = name
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
		if(telephone_type != ''): 
			params['telephone_type'] = telephone_type
		if(email != ''): 
			params['email'] = email
		if(website != ''): 
			params['website'] = website
		if(category_id != ''): 
			params['category_id'] = category_id
		if(category_name != ''): 
			params['category_name'] = category_name
		return self.doCurl("PUT","/business",params)
  


	'''
	Provides a personalised URL to redirect a user to add an entity to Central Index
	@param language - The language to use to render the add path
	@return - the data from the api
	'''
	def getEntityAdd(self,language=''):
		params = {}
		if(language != ''): 
			params['language'] = language
		return self.doCurl("GET","/entity/add",params)
  


	'''
	Find a location from cache or cloudant depending if it is in the cache
	@param string
	@param country
	@return - the data from the api
	'''
	def getLookupLocation(self,string='',country=''):
		params = {}
		if(string != ''): 
			params['string'] = string
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/lookup/location",params)
  


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
	Allows a new phone object to be added to a specified entity. A new object id will be calculated and returned to you if successful.
	@param entity_id
	@param number
	@param description
	@param premium_rate
	@param telephone_type
	@param tps
	@param ctps
	@return - the data from the api
	'''
	def postEntityPhone(self,entity_id='',number='',description='',premium_rate='',telephone_type='',tps='',ctps=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(number != ''): 
			params['number'] = number
		if(description != ''): 
			params['description'] = description
		if(premium_rate != ''): 
			params['premium_rate'] = premium_rate
		if(telephone_type != ''): 
			params['telephone_type'] = telephone_type
		if(tps != ''): 
			params['tps'] = tps
		if(ctps != ''): 
			params['ctps'] = ctps
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
	With a known entity id, an fax object can be added.
	@param entity_id
	@param number
	@param description
	@param premium_rate
	@return - the data from the api
	'''
	def postEntityFax(self,entity_id='',number='',description='',premium_rate=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(number != ''): 
			params['number'] = number
		if(description != ''): 
			params['description'] = description
		if(premium_rate != ''): 
			params['premium_rate'] = premium_rate
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
	With a known entity id, an category object can be added.
	@param entity_id
	@param category_id
	@param category_name
	@return - the data from the api
	'''
	def postEntityCategory(self,entity_id='',category_id='',category_name=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(category_id != ''): 
			params['category_id'] = category_id
		if(category_name != ''): 
			params['category_name'] = category_name
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
	Find all matches by phone number and then return all matches that also match company name and location. Default location_strictness is defined in Km and the default is set to 0.2 (200m)
	@param phone
	@param company_name
	@param latitude
	@param longitude
	@param name_strictness
	@param location_strictness
	@return - the data from the api
	'''
	def getMatchByphone(self,phone='',company_name='',latitude='',longitude='',name_strictness='',location_strictness=''):
		params = {}
		if(phone != ''): 
			params['phone'] = phone
		if(company_name != ''): 
			params['company_name'] = company_name
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		if(name_strictness != ''): 
			params['name_strictness'] = name_strictness
		if(location_strictness != ''): 
			params['location_strictness'] = location_strictness
		return self.doCurl("GET","/match/byphone",params)
  


	'''
	Find all matches by location and then return all matches that also match company name. Default location_strictness is set to 7, which equates to +/- 20m
	@param company_name
	@param latitude
	@param longitude
	@param name_strictness
	@param location_strictness
	@return - the data from the api
	'''
	def getMatchBylocation(self,company_name='',latitude='',longitude='',name_strictness='',location_strictness=''):
		params = {}
		if(company_name != ''): 
			params['company_name'] = company_name
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		if(name_strictness != ''): 
			params['name_strictness'] = name_strictness
		if(location_strictness != ''): 
			params['location_strictness'] = location_strictness
		return self.doCurl("GET","/match/bylocation",params)
  


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
	Spider a single url looking for key facts
	@param url
	@return - the data from the api
	'''
	def getToolsSpider(self,url=''):
		params = {}
		if(url != ''): 
			params['url'] = url
		return self.doCurl("GET","/tools/spider",params)
  


	'''
	Supply an address to geocode - returns lat/lon and accuracy
	@param address
	@return - the data from the api
	'''
	def getToolsGeocode(self,address=''):
		params = {}
		if(address != ''): 
			params['address'] = address
		return self.doCurl("GET","/tools/geocode",params)
  


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
	With a known entity id, an invoice_address object can be updated.
	@param entity_id
	@param address1
	@param address2
	@param address3
	@param district
	@param town
	@param county
	@param postcode
	@param address_type
	@return - the data from the api
	'''
	def postEntityInvoice_address(self,entity_id='',address1='',address2='',address3='',district='',town='',county='',postcode='',address_type=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
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
	Create/Update a postal address
	@param entity_id
	@param address1
	@param address2
	@param address3
	@param district
	@param town
	@param county
	@param postcode
	@param address_type
	@return - the data from the api
	'''
	def postEntityPostal_address(self,entity_id='',address1='',address2='',address3='',district='',town='',county='',postcode='',address_type=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
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
		if(postcode != ''): 
			params['postcode'] = postcode
		if(address_type != ''): 
			params['address_type'] = address_type
		return self.doCurl("POST","/entity/postal_address",params)
  


	'''
	With a known entity id, a advertiser is added
	@param entity_id
	@param tags
	@param locations
	@param expiry
	@param is_national
	@param language
	@return - the data from the api
	'''
	def postEntityAdvertiser(self,entity_id='',tags='',locations='',expiry='',is_national='',language=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(tags != ''): 
			params['tags'] = tags
		if(locations != ''): 
			params['locations'] = locations
		if(expiry != ''): 
			params['expiry'] = expiry
		if(is_national != ''): 
			params['is_national'] = is_national
		if(language != ''): 
			params['language'] = language
		return self.doCurl("POST","/entity/advertiser",params)
  


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
	Create/update a new location entity with the supplied ID in the locations reference database.
	@param location_id
	@param name
	@param formal_name
	@param latitude
	@param longitude
	@param resolution
	@param country
	@param population
	@param description
	@param timezone
	@param is_duplicate
	@param is_default
	@return - the data from the api
	'''
	def postLocation(self,location_id='',name='',formal_name='',latitude='',longitude='',resolution='',country='',population='',description='',timezone='',is_duplicate='',is_default=''):
		params = {}
		if(location_id != ''): 
			params['location_id'] = location_id
		if(name != ''): 
			params['name'] = name
		if(formal_name != ''): 
			params['formal_name'] = formal_name
		if(latitude != ''): 
			params['latitude'] = latitude
		if(longitude != ''): 
			params['longitude'] = longitude
		if(resolution != ''): 
			params['resolution'] = resolution
		if(country != ''): 
			params['country'] = country
		if(population != ''): 
			params['population'] = population
		if(description != ''): 
			params['description'] = description
		if(timezone != ''): 
			params['timezone'] = timezone
		if(is_duplicate != ''): 
			params['is_duplicate'] = is_duplicate
		if(is_default != ''): 
			params['is_default'] = is_default
		return self.doCurl("POST","/location",params)
  


	'''
	Add a new synonym to a known location
	@param location_id
	@param synonym
	@param language
	@return - the data from the api
	'''
	def postLocationSynonym(self,location_id='',synonym='',language=''):
		params = {}
		if(location_id != ''): 
			params['location_id'] = location_id
		if(synonym != ''): 
			params['synonym'] = synonym
		if(language != ''): 
			params['language'] = language
		return self.doCurl("POST","/location/synonym",params)
  


	'''
	Remove a new synonym from a known location
	@param location_id
	@param synonym
	@param language
	@return - the data from the api
	'''
	def deleteLocationSynonym(self,location_id='',synonym='',language=''):
		params = {}
		if(location_id != ''): 
			params['location_id'] = location_id
		if(synonym != ''): 
			params['synonym'] = synonym
		if(language != ''): 
			params['language'] = language
		return self.doCurl("DELETE","/location/synonym",params)
  


	'''
	Add a new source to a known location
	@param location_id
	@param type
	@param url
	@param ref
	@return - the data from the api
	'''
	def postLocationSource(self,location_id='',type='',url='',ref=''):
		params = {}
		if(location_id != ''): 
			params['location_id'] = location_id
		if(type != ''): 
			params['type'] = type
		if(url != ''): 
			params['url'] = url
		if(ref != ''): 
			params['ref'] = ref
		return self.doCurl("POST","/location/source",params)
  


	'''
	With a known entity id, a status object can be updated.
	@param entity_id
	@param status
	@return - the data from the api
	'''
	def postEntityStatus(self,entity_id='',status=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(status != ''): 
			params['status'] = status
		return self.doCurl("POST","/entity/status",params)
  


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
	With a known entity id, avideo object can be added.
	@param entity_id
	@param title
	@param description
	@param thumbnail
	@param embed_code
	@return - the data from the api
	'''
	def postEntityVideo(self,entity_id='',title='',description='',thumbnail='',embed_code=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(title != ''): 
			params['title'] = title
		if(description != ''): 
			params['description'] = description
		if(thumbnail != ''): 
			params['thumbnail'] = thumbnail
		if(embed_code != ''): 
			params['embed_code'] = embed_code
		return self.doCurl("POST","/entity/video",params)
  


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
	Update user based on email address or social_network/social_network_id
	@param email
	@param first_name
	@param last_name
	@param active
	@param trust
	@param creation_date
	@param user_type
	@param social_network
	@param social_network_id
	@return - the data from the api
	'''
	def postUser(self,email='',first_name='',last_name='',active='',trust='',creation_date='',user_type='',social_network='',social_network_id=''):
		params = {}
		if(email != ''): 
			params['email'] = email
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
		return self.doCurl("POST","/user",params)
  


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
	The search matches a category name or synonym on a given string and language.
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
	The search matches a location name or synonym on a given string and language.
	@param str - A string to search against, E.g. Dub e.g. dub
	@param country - Which country to return results for. An ISO compatible country code, E.g. ie e.g. ie
	@return - the data from the api
	'''
	def getAutocompleteLocation(self,str='',country=''):
		params = {}
		if(str != ''): 
			params['str'] = str
		if(country != ''): 
			params['country'] = country
		return self.doCurl("GET","/autocomplete/location",params)
  


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
	Allow an entity to be claimed by a valid user
	@param entity_id
	@param claimed_user_id
	@param claimed_date
	@return - the data from the api
	'''
	def postEntityClaim(self,entity_id='',claimed_user_id='',claimed_date=''):
		params = {}
		if(entity_id != ''): 
			params['entity_id'] = entity_id
		if(claimed_user_id != ''): 
			params['claimed_user_id'] = claimed_user_id
		if(claimed_date != ''): 
			params['claimed_date'] = claimed_date
		return self.doCurl("POST","/entity/claim",params)
  





