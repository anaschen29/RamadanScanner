# RamadanScanner


Assalamu Alaykom! This is how we are running the tap access system for Ramadan 2024. Here is a general overview of how to run this for a day's iftar on a mac/linux. 
1) Grab the reader from the closet in Lobdell. We also have a USB-C to USB adapter in it case you need it. 
2) `cd` into the directory you want to use and clone the git repo by running `git clone https://github.com/anaschen29/RamadanScanner.git`

    Once inside the repo, make sure to run `pip install -r requirements.txt`. This should install the dependencies required for the app. If there is a dependency you don't have installed, you can always run `pip install <dependency>`. 

    

3) Run the create_files.py script (you can do this using the command `python3 create_files.py` or `python create_files.py`). This creates a .txt file for the day's taps, and should display something like _Empty file 'taps/taps(03-25).txt' created._ **ONLY DO THIS ONCE PER DAY.**
4) Run the app.py script (again, you can do `python3 app.py` or `python app.py`). This will run on your local device a flask app which you will use to tap people in, and will give you a link you can open in your browser. 
5) Make sure the affiliate taps when the cursor in the top right. When this happens, this should increment the counter by one. If this didn't happen, then the cursor was not in the right field, so please double check and ask them to tap again. 
6) For guests, the guest list should at the bottom of your browser screen. Each entry should look like this. 
![Screen Shot 2024-03-27 at 8 40 46 AM](https://github.com/anaschen29/RamadanScanner/assets/37285929/03cbcc76-54d7-4873-88b7-3ff2295ef257)

If the entry is there, then just ask the host to tap for every guest. The host **has to** tap for their guests.

7) This means that the counter you see there should count exactly the number of people in Lobdell, including MIT affiliates, hosts, guests, children etc... (Parents can tap for their kids).
   
8) When done, make sure to end the script on your terminal by running `^C`. Next, commit, add, and push the changes to the repo if you are a collaborator. Otherwise, contact me and I'll let you know what to do. Return the reader to the closet in Lobdell (or to me). 



رمضان كريم. 
