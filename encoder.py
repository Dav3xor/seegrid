
def file_available(stream):
    """
    returns true if there is a complete file available in <stream>
    """
    if len(stream):
        try:
            end_of_length = stream.index('|')
        except ValueError:
            return False 
        
        try:
            file_len = int(len(stream[:end_of_length]))
        except ValueError:
            return False
         
        return True if file_len <= len(stream)-end_of_length-1 else False


def encode(filename, stream):
    """
    encode <filename> into a bytearray <stream>
    """
    try:
        with open(filename, 'rb') as infile:
            input_file = infile.read()
    except IOError:
        print "Could not open file."
        return      
    stream += str(len(input_file)) + '|' + input_file



# files larger than memory could be supported, but will currently
# not work.  More than happy to add that feature if it comes up.
def decode(stream, filename):
    """
    decode the first file found in <stream>
    and write it to <filename>.
    """

    if file_available(stream):
        # wire protocol is in the form of <length>|file<length>|file....<length>|file

        # get a file length and remainder.  return if
        # we haven't recieved a length/contents separator
        try:
            file_len, contents = stream.split('|',1)
        except TypeError:
            return
        
        if int(file_len) > contents:
            return 
        try:
            with open(filename, 'wb') as output:
                output.write(contents[:int(file_len)])
            # haha, tricky...
            del stream[:len(file_len)+1+int(file_len)]
        except IOError:
            print "Could not open file."
            return 
