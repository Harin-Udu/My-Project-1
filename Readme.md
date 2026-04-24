This Readme will provide the below clarifications,

   - Guide on how to properly open the folder locally  
   - Detailed description of all the key components and features of the project

1. Guidence to open the project locally

There are two main ways to open it locally 

1.1. Using git clone

Steps: 
  1. Open your IDE (vs code, pycharm) and get the terminal of where you want to save the project 

  2. Then run, (This will save the folder in the location you want)
      
    git clone https://github.com/Harin-Udu/My-Project-1.git
  
  3. Then run, (this leads the terminal to that specific location)
      
    cd My-Project-1 
  
  4. Then run, (this will open the folder where the project is)

    code .

  5. Once the folder is open then go to the terminal of that specfic folder and run the below code,

    python manage.py runserver 

  6. Then run this code on the web to open the website,

    http://127.0.0.1:8000/

1.2. Zipping and extracting 

Steps:
  1. Zip the file from the codes section

  2. Extract the zipped folder 

  3. Inside the newly extracted folder there will be another folder called My-Project-1-main bring all the files inside this nested folder back to the initial folder

  4. Then delete the nested My-Project-1-main folder

  5. Then open the main folder in your IDE

  6. Once the folder is open then go to the terminal of that folder and run the below code,

    python manage.py runserver 

  7. Then run this code on the web to open the website,

    http://127.0.0.1:8000/

2. Details on the project

2.1. How to read the different folders and files 

2.1.1. config folder 

   This is the brain of the project where the files inside this are essential to run the website mainly settings.py which controls all the aspects of the projects and urls.py which handles all the routing 

2.1.2. salon folder

   This is where all the content shown in the webpage is created. Each page is seperately made using a html and css file which will be highlighted in section 2.2

2.2. Webpages and features 

2.2.1. Main Page

The main page of the app has the below features,

   - A small description of services
   - A gallary with pictures
   - A review section
   - A contact section with details

2.2.2. About page 

The about page of the app has the below features,

   - A detailed story about the saloon
   - A what we offer section
   - A why chooose us section

2.2.3. Our team page 

This page has pictures of all the members of valencia saloon 

2.2.4. Support page 

This support page of the app has the below features,

   - Frequently asked questions from various topics
   - A contact section with details

2.2.5. Booking page 

This page has all the details related to booking an appointment 
