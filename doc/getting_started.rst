===============
Getting Started
===============

The core of the library is the `BurnerEmail` object. Here are some
examples on how to use it::

    from slippery.burner_email import BurnerEmail

    email = BurnerEmail.generate()              # create a new email address
    print email.getmailto()                     # send emails here!
    email.setinbox('aaaaa', 'aaaaaaaaaaaaaaaa') # use this instead of generate if you
                                                # already have an email
    msgs = email.fetch_emails()                 # see what's in the inbox
    print email.fetch_email('12345')            # get the contents of an email
    email.delete_email('12345')                 # delete an email

When you use the method `fetch_emails()` it returns an array of dictionaries with
the following form::

    {'id':int, 'sender':str, 'subject':str, 'date':str}

`id` is what should be passed to `fetch_email()` and `delete_email()`.

The library also includes a useful method for setting a SOCKS5 proxy::

    from slippery import proxy
    proxy.set_proxy('localhost', '9050')

And that's it! Super simple. There's also an example of a very simple console
program in the examples directory of the repo.
