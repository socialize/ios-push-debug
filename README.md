
#Push Debugging Scripts


This is a set of scripts that can be used for testing push functionality in an app,
independent of Socialize.

Using the scripts:

 - Run p12_to_pem.sh <p12> (Remember to specify the location of your p12 file.)
    ./p12_to_pem ~/Desktop/my.p12

2) Run push.py <TOKEN>
    ./push.py FE66489F304DC75B8D6E8200DFF8A456E8DAEACEC428B427E9518741C92C6660

3) run feedback.py to check for any errors from apple
    ./feedback.py
