This Readme will provide the below clarifications,
  1. Guide on how to properly open the folder locally 
  2. Detailed description of all the key components and features of the project 

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

  6. Once the folder is open then go to the terminal of that specfic folder and run the below code,

    python manage.py runserver 

  8. Then run this code on the web to open the website,

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

  8. Then run this code on the web to open the website,

    http://127.0.0.1:8000/

