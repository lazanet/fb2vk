# fb2vk
Bot for FB -> VK page cloning

## Requirements 
```bash
    sudo pip3 install requests
    sudo pip3 install requests-html
    sudo pip3 install html2text
```


## Creating vKontakte API key
1. Create a standalone app
2. Go to [this url](http://vk.com/apps?act=manage), click `manage` on app that you just created. Get Application's ID number on settings page.
3. Now you will need the user's token and id. This is the url that your user will paste to his/her browser. Then you will need the page url that user got redirected to (or find a way to do it all by your app).
    ``` 
    https://oauth.vk.com/authorize?client_id=YOUR-APP-ID&scope=pages,wall,offline&redirect_uri=http://oauth.vk.com/blank.html&response_type=token 
    ```
    More scopes can be found here: https://vk.com/dev/permissions 

    ### Snippet which generates url for user

    ``` python
    print("https://oauth.vk.com/authorize?client_id="+appID+"&scope=pages,wall,offline,photos&redirect_uri=http://oauth.vk.com/blank.html&response_type=token") 
    ```


4. Redirected url will look like this:
    ```
    https://oauth.vk.com/blank.html#access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&expires_in=0&user_id=xxxxxxxx
    ```
    from where you can fetch user's token.


<hr>

## Creating permanent facebook access token
http://www.awasthiashish.com/2017/03/generate-permanent-facebook-page-access.html
