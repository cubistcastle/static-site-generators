from datetime import date

#
#  Return the current date.
#
#  Used in pages like so:
#
#   <p>I was updated at {{ today() }}.</p>
#
def today():
        return date.today().strftime("%B %d, %Y")
