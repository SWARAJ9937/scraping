from flask import Flask , request , json

app = Flask(__name__)

list = [{
    "cin":"96942801G",
    "mbi":"",
    "medsId":"None",
    "memeCk":104954600,
    "grgrCk":33,
    "sbsbCk":104954600,
    "firstName":"JOSEPH",
    "middleInitial":"M",
    "lastName":"PHAM",
    "dateOfBirth":"08/22/2016",
    "dateOfBirthDisplay":"None",
    "gender":"M",
    "genderDisplay":"None",
    "lineOfBusiness":"Medi-Cal",
    "healthNetworkPlanCode":"HMO83MC",
    "healthNetworkPlanDesc":"Family Choice Health Services",
    "pcpInfo":{
       "pcpId":"00A684500",
       "pcpName":"Vu, Peter H.",
       "pcpEffDate":"11/01/2022",
       "pcpTermDate":"12/31/9999",
       "pcpDetail":{
          "providerInfo":{
             "providerEntityType":"None",
             "providerNPI":"None",
             "providerTaxId":"None",
             "providerFirstName":"None",
             "providerMiddleInitial":"None",
             "providerLastName":"None",
             "providerGender":"None",
             "providerTypeCode":"None",
             "providerTypeDesc":"None",
             "providerSpecialtyCode":"None",
             "providerSpecialtyDesc":"None",
             "providerId":"00A684500",
             "providerName":"Vu, Peter H.",
             "prpR_ID":"00A684500"
          },
          "providerAddressList":"None",
          "providerNetworkAffiliationList":"None"
       },
       "memE_CK":104954600,
       "mepR_PCP_TYPE":"None",
       "mepR_EFF_DT":"11/01/2022",
       "prpR_ID":"00A684500"
    },
    "healthNetworkPlanEffectiveDate":"11/01/2022",
    "healthNetworkPlanTermDate":"12/31/2199",
    "eligibilityStatus":1,
    "writtenLanguage":"Vietnamese",
    "spokenLanguage":"Vietnamese",
    "phone":"**********",
    "email":"**********",
    "address":{
       "address1":"**********",
       "address2":"",
       "city":"GARDEN GROVE",
       "state":"CA",
       "zipCode":"928443139"
    },
    "isUserAssocToMemberPcp":False,
    "pcpNPI":"None",
    "aidCode":"None",
    "aidCodeDesc":"None",
    "ihaDueDate":"None"
 }]

@app.route('/list')    # methods=['GET', 'POST'])
def appbook():
   #  if request.method == 'GET':
   #      if len(list) > 0:
   #          return jsonify(list)
   #      else:
   #          'Nothing found' , 404
   return 

   #  if request.method == 'POST':
   #      new_author = request.form['author']
   #      new_land = request.form['language']
   #      new_list = request.form['']

