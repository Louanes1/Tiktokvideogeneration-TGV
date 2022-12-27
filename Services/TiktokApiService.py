import requests

class TiktokApiService:
    Endpoints = {"Upload":"https://open-api.tiktok.com/share/video/upload/"
    ,"AccessToken":"https://open-api.tiktok.com/share/video/upload/"
    } 


    def __init__(self,Endpoints,profile,):
        self.Endpoints= Endpoints
        self.profile=profile
        self.CLIENT_KEY= "CLIENT_KEY" #retrieve from git.ignore file ?
        self.CLIENT_SECRET="CLIENT_SECRET"
        self.code="" #Authorization code from Web/iOS/Android authorization callback"
        self.grant_type="authorization_code" #grant_type value should always be set as authorization_code.
    
    
    def IsConnected():
        
        result = requests.get("url","params","data", "headers")
        if(result.status == 200):
            return True

        else:
            return False
        


    def UploadVideo(self,video,id,token):

        ''' api references : https://developers.tiktok.com/doc/web-video-kit-with-web/'''

        request_body = {"Content-Type":"multipart/form-data"}
        parameters = {"open_id":id,"access_token":token}        

        response = requests.post(self.Endpoints["Upload"],video,request_body,parameters)

        return response


    def GetToken(self):
        
        self.profile="louwi"
        parameterss = {"client_key":self.CLIENT_KEY,"client_secret":self.CLIENT_SECRET,"code":self.code,"grant_type":self.grant_type} 
        response = requests.post(url = self.Endpoints["AccessToken"],params = parameterss)
        return response




