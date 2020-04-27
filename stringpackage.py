def Stringpackage():
    x=str(input("Enter The string to perform 1st five builtin function:"))
    #give input This is 1st string
    
    #Return a capitalized version of the string.
    #More specifically, make the first character have upper case and the rest lower case.
    print(x.capitalize())
    
    #Return a version of the string suitable for caseless comparisons.
    print(x.casefold())
    
    #Return a centered string of length width.
    #Padding is done using the specified fill character (default is a space).
    print(x.center(10,'z'))
    
    #Return the number of non-overlapping occurrences of substring sub in
    #string S[start:end].  Optional arguments start and end are
    #interpreted as in slice notation.
    sub='i'
    print(x.count(sub,1,10))
    
    sub='lol'
    print(x.count(sub))
    
    #encode(self, /, encoding='utf-8', errors='strict')
    #Encode the string using the codec registered for encoding.
    #The encoding in which to encode the string.
    #errors
    #The error handling scheme to use for encoding errors.
    #The default is 'strict' meaning that encoding errors raise a
    #UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
    #'xmlcharrefreplace' as well as any other name registered with
    #codecs.register_error that can handle UnicodeEncodeErrors.
    print(x.encode('utf-8','strict'))
    
    0
    
    y=str(input("Enter string to perform next 5 function:"))
    #give input this is 2nd string
    
    z='ing'
    
    #Return True if S ends with the specified suffix, False otherwise.
    #With optional start, test S beginning at that position.
    #With optional end, stop comparing S at that position.
    #suffix can also be a tuple of strings to try.
    
    print(y.endswith(z))
    print(y.endswith(z,10))
    z='s'
    print(y.endswith(z, 1, 4))
    print(y.endswith(z, 2, 6))
    
    #Return a copy where all tab characters are expanded using spaces.
    #If tabsize is not given, a tab size of 8 characters is assumed.
    
    print("\noriginal string:",y)
    print(y.expandtabs())
    print(y.expandtabs(16))
    
    #Return the lowest index in S where substring sub is found,
    # that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #Return -1 on failure.
    
    k='tr'
    print(y.find(k))
    print(y.find(k, 10))
    print(y.find(k, 40))
    
    #Return a formatted version of S, using substitutions from args and kwargs.
    #The substitutions are identified by braces ('{' and '}').
    
    l="Hi i'm {age:.2f} year old!"
    print(l.format(age = 200))
    
    #Return a formatted version of S, using substitutions from mapping.
    #The substitutions are identified by braces ('{' and '}').
    #print(l.format_map())
    
    #Return the lowest index in S where substring sub is found, 
    #such that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #Raises ValueError when the substring is not found.
    print(l.index("old"))
     
    #Return True if the string is an alpha-numeric string, False otherwise.
    #string is alpha-numeric if all characters in the string are alpha-numeric and
    #there is at least one character in the string.
    print(y.isalnum())
    
    #Return True if the string is an alphabetic string, False otherwise.
    #A string is alphabetic if all characters in the string are alphabetic and there
    #is at least one character in the string.
    print(y.isalpha()) 
    
    
    
    #Return True if all characters in the string are ASCII, False otherwise.
    #ASCII characters have code points in the range U+0000-U+007F.
    #Empty string is ASCII too.
    print(y.isascii())
    
    
    #Return True if the string is a decimal string, False otherwise.
    #A string is a decimal string if all characters in the string are decimal and
    #there is at least one character in the string.
    print(y.isdecimal())
    
    #Return True if the string is a digit string, False otherwise.
    #A string is a digit string if all characters in the string are digits and there
    #is at least one character in the string.
    print(y.isdigit())
    
    #Return True if the string is a valid Python identifier, False otherwise.
    #Use keyword.iskeyword() to test for reserved identifiers such as "def" and
    #"class".
    print(y.isidentifier())
        
    
    #Return True if the string is a lowercase string, False otherwise.
    #A string is lowercase if all cased characters in the string are lowercase and
    #there is at least one cased character in the string.    
    print(y.islower())    
        
    
    #Return True if the string is a numeric string, False otherwise.
    #A string is numeric if all characters in the string are numeric and there is at
    #least one character in the string.
    print(y.isnumeric())
    
    #Return True if the string is printable, False otherwise.
    #A string is printable if all of its characters are considered printable in
    #repr() or if it is empty.
    print(y.isprintable()) 
     
    #Return True if the string is a whitespace string, False otherwise.
    #A string is whitespace if all characters in the string are whitespace and there
    #is at least one character in the string.
    print(y.isspace())    
        
    #Return True if the string is a title-cased string, False otherwise.
    #In a title-cased string, upper- and title-case characters may only
    #follow uncased characters and lowercase characters only cased ones.
    print(y.istitle())    
        
        
    #Return True if the string is an uppercase string, False otherwise.
    #A string is uppercase if all cased characters in the string are uppercase and
    #there is at least one cased character in the string.    
    print(y.isupper())
    
    
    #Concatenate any number of strings.
    #The string whose method is called is inserted in between each given string.
    #The result is returned as a new string.
    j='  Wipro Sarjapur  '
    print("#".join(j)) 
    
    #Return a left-justified string of length width.
    #Padding is done using the specified fill character (default is a space).
    print(j.ljust(20))
    
    #Return a copy of the string converted to lowercase.
    print(j.lower())
    
    #Return a copy of the string with leading whitespace removed.
    #If chars is given and not None, remove characters in chars instead.
    print(j.lstrip())
    
    #Partition the string into three parts using the given separator.
    #
    #This will search for the separator in the string.  If the separator is found,
    #returns a 3-tuple containing the part before the separator, the separator
    #itself, and the part after it.
    #
    #If the separator is not found, returns a 3-tuple containing the original string
    #and two empty strings.
    print(j.partition(" "))
      
    #replace(self, old, new, count=-1, /)
    #Return a copy with all occurrences of substring old replaced by new.
    #
    #  count
    #    Maximum number of occurrences to replace.
    #    -1 (the default value) means replace all occurrences.
    #
    #If the optional argument count is given, only the first count occurrences are
    #replaced.
    print(j.replace("a","b"))
        
        
    #rfind(...)
    #S.rfind(sub[, start[, end]]) -> int
    #
    #Return the highest index in S where substring sub is found,
    #such that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #
    #Return -1 on failure.
    print(j.rfind('Wipro'))
    
    
    #rindex(...)
    #S.rindex(sub[, start[, end]]) -> int
    #
    #Return the highest index in S where substring sub is found,
    #such that sub is contained within S[start:end].  Optional
    #arguments start and end are interpreted as in slice notation.
    #
    #Raises ValueError when the substring is not found.
    print(j.rindex('Wipro'))
    
    
    #rjust(self, width, fillchar=' ', /)
    #Return a right-justified string of length width.
    #
    #Padding is done using the specified fill character (default is a space).
    print(j.rjust(20))
    
    
    #rpartition(self, sep, /)
    #Partition the string into three parts using the given separator.
    #
    #This will search for the separator in the string, starting at the end. If
    #the separator is found, returns a 3-tuple containing the part before the
    #separator, the separator itself, and the part after it.
    #
    #If the separator is not found, returns a 3-tuple containing two empty strings
    #and the original string.
    #print(j.rpartinion("a"))
    
    
    
    #rsplit(self, /, sep=None, maxsplit=-1)
    #Return a list of the words in the string, using sep as the delimiter string.
    #
    #  sep
    #    The delimiter according which to split the string.
    #    None (the default value) means split according to any whitespace,
    #    and discard empty strings from the result.
    #  maxsplit
    #    Maximum number of splits to do.
    #    -1 (the default value) means no limit.
    #
    #Splits are done starting at the end of the string and working to the front.
    print(j.rsplit(' '))
    
    
    #rstrip(self, chars=None, /)
    #Return a copy of the string with trailing whitespace removed.
    #
    #If chars is given and not None, remove characters in chars instead.
    print(j.rstrip())
    
    #split(self, /, sep=None, maxsplit=-1)
    #Return a list of the words in the string, using sep as the delimiter string.
    #  sep
    #  The delimiter according which to split the string.
    #  None (the default value) means split according to any whitespace,
    #  and discard empty strings from the result.
    #  maxsplit
    #  Maximum number of splits to do.
    #  -1 (the default value) means no limit.
    print(j.split(' '))
    
    #splitlines(self, /, keepends=False)
    #Return a list of the lines in the string, breaking at line boundaries.
    #
    #Line breaks are not included in the resulting list unless keepends is given and
    #true.
    #print(j.splitlines(' '))
    
    
    #startswith(...)
    #S.startswith(prefix[, start[, end]]) -> bool
    #
    #Return True if S starts with the specified prefix, False otherwise.
    #With optional start, test S beginning at that position.
    #With optional end, stop comparing S at that position.
    #prefix can also be a tuple of strings to try.
    print(j.startswith('Sarjapur'))
    
    
    #strip(self, chars=None, /)
    #Return a copy of the string with leading and trailing whitespace remove.
    #
    #If chars is given and not None, remove characters in chars instead.
    print(j.strip())
    
    #swapcase(self, /)
    #Convert uppercase characters to lowercase and lowercase characters to uppercase.
    print(j.swapcase())
    
    #title(self, /)
    #Return a version of the string where each word is titlecased.
    #
    #More specifically, words start with uppercased characters and all remaining
    #cased characters have lower case.
    print(j.title())
    
    
    #translate(self, table, /)
    #    Replace each character in the string using the given translation table.
    #    
    #      table
    #        Translation table, which must be a mapping of Unicode ordinals to
    #        Unicode ordinals, strings, or None.
    #    
    #    The table must implement lookup/indexing via __getitem__, for instance a
    #    dictionary or list.  If this operation raises LookupError, the character is
    #    left untouched.  Characters mapped to None are deleted.
    #print(j.translate())
    
    #upper(self, /)
    #    Return a copy of the string converted to uppercase.
    print(j.upper())
    
    
    #zfill(self, width, /)
    #    Pad a numeric string with zeros on the left, to fill a field of the given width.
    #    
    #    The string is never truncated.
    #print(j.zfill())