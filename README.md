# Blog-App-API
A web app API that allow authenticated user to perform actions like GET & POST, and also allow the superuser to make changes via the admin dashboard


# API documentation
🔗https://bloggerapi.pythonanywhere.com/

ENDPOINTS
/admin

/get-all-post

It uses a GET method to fetch all the post from the database in the format below




{
    
        "id": 2,
        
        "category": "Polictics",
        
        "status": "draft",
        
        "title": "Tinubu na Werey",
        
        "content": ".KJWBEFLJHWBEj wfeWLE Fhwefa efbe aehj ash a.ubef weubfwi HJ WEF.A W.F .WKEJF /AWJKEN/FKASNDKjnbD  ASUC AWSBEIUB/wufe .uBWEBUF ;IUBSHC .AWSEU .EAUBS EJH FWEBF .EFUIB/BAREUAEBR . rg eurbgf d.d fu vjdfu vdf",
        
        "date_published": "2023-10-04T05:46:07.098028Z",
        
        "hashtag": "#programming",
        
        "shares": 0,
        
        "image": "/blog-post-media/01_MONTERO_Call_Me_By_Your_Name.mp3",
        
        "video": null,
        
        "audio": null,
        
        "views": 0,
        
        "author": 1,
        
        "likes": []
    },
    



/posts/<str:model_name>/<int:pk>/comments/ [name='post-comments']
This uses a GET AND POST method to get a specific post and allow  users to POST comments via the endpoint



/register [name='register']
This uses a GET & POST to collect registration details from user and register them

{
   
    "password": "user21",
    "username": "Password2023",
    "email": "user21@gmail.com"
}

/login [name='login']
this uses GET & POST method with django authentication system and django-rest-framewok Oauth to check if user is valid and then return the user details 

{
    
    "username": "example77",
    "password": "example123"
}


/admin
This uses a get request to ursher users with login details to admin dashboad where series of changes can made, plus it is user friendly


