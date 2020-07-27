parallel = True

## fb part
fb_token = "FACEBOOK_PERMANENT_TOKEN"

fb_email = None
fb_pass = None

## vk part
app_id = "VK_APP_ID"

report_loc = -1 # vkPage id for sending error reports 
report_user_token = "VK_REPORT_PAGE_USER_TOKEN" # userToken for error report publishing

#############################################################################################
# PAGES IN SCOPE
#############################################################################################

data = []
data.append(dict(name = "UNIQUE_PAGE_NAME", fb_page = "FACEBOOK_PAGE_URL_ID", vk_page_id = "VK_PAGE_ID", user_token = "VK_USER_TOKEN"))
data.append(dict(name = "UNIQUE_PAGE2_NAME", fb_page = "FACEBOOK_PAGE2_URL_ID", vk_page_id = "VK_PAGE2_ID", user_token = "VK_USER2_TOKEN"))
## copy lines from above if more pages are used ...
