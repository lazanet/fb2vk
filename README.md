# fb2vk
Bot for FB -> VK page cloning

##TODO
- Write normal readme.


## Uputstvo za podesavanje vk API-ja
- first create a standalone(Jay didnt create a standalone application) app,phone code etc...
- then go to this url ` http://vk.com/apps?act=manage ` click manage the app you just created. on settings page get the application id number.
- now you need the users token and id. this is the url that your user will paste to his/her browser. than you will need the page url that user redirected.(or find a way to do it all by your app) 
- ` https://oauth.vk.com/authorize?client_id=YOUR-APP-ID&scope=pages,wall,offline&redirect_uri=http://oauth.vk.com/blank.html&response_type=token `
- more scopes can be found here https://vk.com/dev/permissions the url example is for wall posting,page posting etc... user will give permissions and thats it. 
- now you have token and users id.(if he/she gave you the redirected page url just after giving your app the permissions)
- token url example
- https://oauth.vk.com/blank.html#access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&expires_in=0&user_id=xxxxxxxx
- now to post to users wall this is the code

## Autentifikacija vk aplikacije!!	

` print "https://oauth.vk.com/authorize?client_id="+appID+"&scope=pages,wall,offline,photos&redirect_uri=http://oauth.vk.com/blank.html&response_type=token" `

#################################################################################

## Pravljenje permanentnog FB access tokena
http://www.awasthiashish.com/2017/03/generate-permanent-facebook-page-access.html
