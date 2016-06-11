


def encode(filename, stream):
    """
    encode <filename into a bytearray <stream>
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
    if len(stream):
        # wire protocol is in the form of <length>|file<length>|file....<length>|file
        file_len, contents = stream.split('|',1)
        try:
            with open(filename, 'wb') as output:
                output.write(contents[:int(file_len)])
            # haha, tricky...
            del stream[:len(file_len)+1+int(file_len)]
        except IOError:
            print "Could not open file."
            return 
