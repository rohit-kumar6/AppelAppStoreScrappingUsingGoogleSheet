# AppelAppStoreScrappingUsingGoogleSheetAppelAppStoreScrappingUsingGoogleSheet

# Setup Virtual Environment Python
1. Cd into Respective folder
2. Install virtualenv (python3 -m pip install virtualenv)
3. Create virtualenv (python3 -m venv {name of your venv})
4. Activate virtualenv (source {name of your venv}/bin/activate)
5. pip install -r requirements.txt

# Setup Google sheet access
1. Create Cred.json File, Put in Respective folder where code is present
2. Replace google sheet key in main.py line no 8

# Create Cred.json
1. Create new project in https://console.cloud.google.com/apis/dashboard
2. Enable "Google Drive API", "Google Sheet API"
3. Go to Credentials <img width="266" alt="Screenshot 2021-08-19 at 8 15 58 PM" src="https://user-images.githubusercontent.com/22203782/130089625-20b75ce0-94b0-413f-a07f-eec4c24b9732.png">
4. Create Credentials
5. Select Service Account <img width="520" alt="Screenshot 2021-08-19 at 8 16 24 PM" src="https://user-images.githubusercontent.com/22203782/130089710-8dd76a94-5b9a-48eb-8cab-734dee8ab379.png">
6. Put name <img width="582" alt="Screenshot 2021-08-19 at 8 16 49 PM" src="https://user-images.githubusercontent.com/22203782/130089807-f2d89ec4-8000-4692-a20e-da765959704a.png">
7. Add Editor access <img width="524" alt="Screenshot 2021-08-19 at 8 17 14 PM" src="https://user-images.githubusercontent.com/22203782/130089879-90945ae5-3c39-4c58-9f44-f3676fb5d39b.png">
8. Click Done
9. Once create, go inside that service account
10. Clikck key and add key -> Create new key -> Json <img width="1175" alt="Screenshot 2021-08-19 at 8 18 16 PM" src="https://user-images.githubusercontent.com/22203782/130090057-ed18bf5f-6a64-47ab-b668-e70d5fb64189.png">
11. It will donwload json file. Rename and put in working directory


# Now Run the main.py now
