import dash_core_components as dcc
import dash_bootstrap_components as dbc

welcome_message = dcc.Markdown(
    """
    Welcome! Thanks for hanging out at home and doing your part in reducing the spread of COVID-19.
    As you may know, the soul of New Orleans is fueled by our artistic community which fills the city with music, dance, visual art, and other forms of expression. 
    Our community of artists need us now more than ever! Most gigs have been cancelled across the city, but our artist still need to make a living.
    There are only so many Netflix shows you can watch before your brain turns into a goo. But hey, you can check out the schedule of streams below and enjoy some local artistry. 
    Most streaming platforms allow for tipping, however you can also check the event description to see how the artists would like to be supported (example: Venmo,paypal,etc...)
    """
)

event_instructions = dbc.Card(dbc.CardBody(dcc.Markdown(
    """
    # Instructions:
    Thank you for contributing to our event calendar and allowing people to enjoy your art. Use the form below to enter your performance info.
    - You can use the streaming service of your choice as long as it allows you to get a shareable link to your stream
        - Some streaming services: 
            - [Youtube Live](https://support.google.com/youtube/answer/2474026?hl=en)
            - [Twitch](https://medium.com/@charliedeets/beginners-guide-to-streaming-on-twitch-dc2a7108fbd7)
            - [Facebook Live](https://www.facebook.com/help/587160588142067)
    - Some streaming services allow people to tip. However, you can also mention how you would like to be supported on the event description (Venmo,Paypal,etc...)
    """
)))