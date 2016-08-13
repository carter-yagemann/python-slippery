#    Copyright 2016 Carter Yagemann
#
#    This file is part of python-slippery.
#
#    python-slippery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    python-slippery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with python-slippery.  If not, see <http://www.gnu.org/licenses/>.

"""Parsing methods for the slippery.email webpages"""

from lxml.html import document_fromstring

def parse_inbox(html_str):
    """Parses an inbox for messages.

    Args:
      html_str:
        The raw HTML to parse. This should be in string form and can be
        retreived from BurnerEmail.getinbox().

    Return:
      An array of emails. Each email is a dictionary in the form:
        {'id':int, 'sender':str, 'subject':str, 'date':str}
    """
    doc = document_fromstring(html_str)
    raw = doc.xpath("//div[@id='mailqueue']//a[@class='messageBox iframe']")
    dict_array = []
    for msg in raw:
        if len(msg) == 3:
            msg_contents = {}
            msg_contents['id'] = msg.get('data-mid')
            msg_contents['sender'] = msg[0].text
            msg_contents['subject'] = msg[1].text
            msg_contents['date'] = msg[2].text
            dict_array.append(msg_contents)
    return dict_array

def parse_message(html_str, msg_type):
    """Parses a message page.

    Args:
      html_str:
        The raw HTML page to parse. This should be in string form.
      msg_type:
        Either 'text' or 'html'. Depending on which view the web page is using,
        the page has to be parsed differently.

    Return:
      A string containing the message body as HTML or text.
    """
    if not msg_type in ['text', 'html']:
        raise ValueError("type must be 'text' or 'html'.")
    doc = document_fromstring(html_str)
    frame = doc.xpath("//div[@id='mbody']")
    if msg_type == 'text':
        body = frame[0][0].text
    elif msg_type == 'html':
        body = frame[0].text
    return body
