## fb part
fbToken = "FACEBOOK_PERMANENT_TOKEN"

fbEmail = None
fbPass = None

## vk part
appID = "VK_APP_ID"

reportLoc = -1 # vkPage id for sending error reports 
reportUserToken = "VK_REPORT_PAGE_USER_TOKEN" # userToken for error report publishing

#############################################################################################
# PAGES IN SCOPE
#############################################################################################

data = []
data.append(dict(name = "UNIQUE_PAGE_NAME", fbPage = "FACEBOOK_PAGE_URL_ID", vkPageId = "VK_PAGE_ID", userToken = "VK_USER_TOKEN"))
data.append(dict(name = "UNIQUE_PAGE2_NAME", fbPage = "FACEBOOK_PAGE2_URL_ID", vkPageId = "VK_PAGE2_ID", userToken = "VK_USER2_TOKEN"))
## copy lines from above if more pages are used ...
