from datetime import datetime as dt # imports datetime module
import smtplib # Imports library to provide an interface to sned emails
import ssl # used to establish secure connections
from email.message import EmailMessage # module that is used to create email messages using code

host_path = "C:\Windows\System32\drivers\etc\hosts" # location of the hosts file which is used to block websites
redirect = "127.0.0.1" # Websites that are blocked will be redirected to this IP address (double check in hosts file with localhost )
website_list = ["www.website1.com", "website1.com"] # List of websites whose IP address will be changed to block them
email_sender = 'sender@gmail.com' #email of the sender (replace with sender email)
email_password = 'password123' # can be obtained through creating a new app password using "google app passwords" from the senders google account.
email_receiver = 'reciever@gmail.com' #email of the reciever  (replace with reciver  email)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17): # This checks if the current time is between 9am and 5pm.

        with open(host_path,"r+") as file:# opens the hosts file in read and write mode.

            content = file.read() # reads the content of the hosts file.

            for website in website_list:

                if website in content :
                    pass # If website is in hosts file, the code does nothing


                else: # If website is not in hosts file, the code adds the websites to the hosts file

                    file.write(redirect+"  "+website+"\n")  # writes the IP address of the local host to the website name in the hosts file
                    subject =  " Website has been blocked!" # Sets the subject of the email being sent
                    body = """
                     The website  """ + website + "  " + "has been blocked by your administrator "

                    # Types out " The website ______ has been blocked by your adminstrator " in the body of the email

                    em = EmailMessage() # creates the Emailmessages() class and sets it to an variable

                    em['From'] = email_sender #sets the sender of the email message.

                    em['To'] = email_receiver #sets the reciever of the email message.

                    em['Subject'] = subject #sets the subject of the email message.

                    em.set_content(body) # sets the body of the email message.

                    context = ssl.create_default_context() # creates a default SSL context.

                    # Log in and send the email
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                        smtp.login(email_sender, email_password)
                        smtp.sendmail(email_sender, email_receiver, em.as_string())
        break

    else: # unblocks websites in the hosts list if time is beyond 5pm

        with open(host_path, "r+") as file: #uses a context manager to open the hosts file in read and write mode,ensuring that file is closed properly after usage.

            content = file.readlines()  # read all the lines in the hosts file and store them in the list

            file.seek(0) # Used to overwrite old content

            for line in content: #iterates through each line in the content list.

                if not any(website in line for website in website_list ): # checks if any website in the website_list is present in the current line of the list.
                    file.write(line) # write the line back to the hosts file.

            file.truncate() #  truncate the hosts file to remove any content

            print("websites are unblocked")

            break # breaks the loop
