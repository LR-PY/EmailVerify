import dns.resolver
import smtplib
import tldextract


def EmailVerify(email):

    domain = tldextract.extract(email)
    domain = domain.domain + "." + domain.suffix

    try:
        # MX record lookup
        records = dns.resolver.resolve(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # This email will be used to "send" an email to the server
        fromAddress = 'just_a_place_holder@domain.com'

        # This email address will be used to check if the server is accept all
        # If this obviously invalid email is accepted, the server is accept all
        acceptall = "invalid.email.9238381" + "@" + domain

        # Connect to the server and verify the email address
        server = smtplib.SMTP()
        server.connect(mxRecord)
        server.helo(server.local_hostname)
        server.mail(fromAddress)
        

    except:
        emailfound = True
        message = "Invalid Domain"

        return str(message)

    code, message = server.rcpt(str(acceptall))
    emailfound = False

    if code == 250:
        emailfound = True
        server.quit()
        return "Accept All"

    code, message = server.rcpt(str(email))
    if code == 250:
        emailfound = True
        server.quit()
        return "Valid Email"

    if emailfound == False:
        server.quit()
        return "No Valid Email Found"