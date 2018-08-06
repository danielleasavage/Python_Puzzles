class HashTable:
    """
    A hashtable represented as a list of lists with open hashing.
    Each bucket is a list of (key,value) tuples
    """
    
    def __init__(self, nbuckets):
        self.nbuckets = nbuckets
        self.table = [[] for i in range(nbuckets)]
        
    def buckets_str(self):
        """
        Return a string representing the various buckets of this table. The output looks like:
          0000->
          0001->
          0002->
          0003->parrt:99
          0004->
        where parrt:99 indicates an association of (parrt,99) in bucket 3.
        """ 
        bucket_string = ''
        for b_index, bucket in enumerate(self.table):
            bucket_string += str(b_index).zfill(4) + '->'
            for tup in self.table[b_index]:
                key = tup[0]
                values = tup[1]
                bucket_string += '{}:{}, '.format(key,values)
            bucket_string = bucket_string.rstrip(', ')
            bucket_string += '\n'
        return bucket_string
    
    
    def __str__(self):
        """
        Return what str(table) would return for a regular Python dict such as {parrt:99}.
        The order should be bucket order and then insertion order in the bucket.
        The insertion order is guaranteed when you append to the buckets in put.
        """
        dict_string = '{'
        for b_index, bucket in enumerate(self.table):
            for tup in self.table[b_index]:
                key = tup[0]
                values = tup[1]
                dict_string += '{}:{}, '.format(key,values)
        dict_string = dict_string.rstrip(', ')
        dict_string += '}'
        return dict_string
    
    
    def hashcode(self,o):
        """
        Return a hashcode for strings and integers; all others return None
        For integers, just return the integer value.
        For strings, perform operation h = h*31 + ord(c) for all characters in the string
        """
        if isinstance(o, int):
            return o
        else:
            h = 0
            for c in o:
                h = h*31 + ord(c)
            return h
    
    
    def get(self, key):
        """
        Return table[key].
        Find the appropriate bucket indicated by the key and look for the association with the key. Return the value (not the key and not the association!)
        Return None if key not found.
        """
        bucket = self.hashcode(key) % self.nbuckets
        for k,tup in enumerate(self.table[bucket]):
            if tup[0] == key:
                return tup[1]
            elif k==len(self.table[bucket]):
                return None
            
    def __getitem__(self, key):
        """
        Return table[key].
        Find the appropriate bucket indicated by the key and look for the association with the key. Return the value (not the key and not the association!)
        Return None if key not found.
        """
        return self.get(key)

    
    def put(self, key, value):
        """
        Perform table[key] = value
        Find the appropriate bucket indicated by key and then append a value to the bucket.
        If the bucket for key already has a key, value pair with that key then replace it.
        Make sure that you are only adding (key, value) associations to the buckets.
        """
        bucket = self.hashcode(key) % self.nbuckets
        if len(self.table[bucket]) == 0:
            self.table[bucket].append((key, value))
        else:
            for k, tup in enumerate(self.table[bucket]):
                if tup[0] == key:
                    self.table[bucket][k] = (key, value)
                    break
                elif k == len(self.table[bucket]) - 1:
                    self.table[bucket].append((key, value))
                    break
        #return table
        
    def __setitem__(self, key, value):
        """
        Perform table[key] = value
        Find the appropriate bucket indicated by key and then append a value to the bucket.
        If the bucket for key already has a key, value pair with that key then replace it.
        Make sure that you are only adding (key, value) associations to the buckets.
        """
        self.put(key, value)
        
    
    def bucket_indexof(self, key):
        """
        Return the element within a specific bucket; the bucket is table[key].
        You have to search the bucket linearly.
        """
        bucket = self.hashcode(key) % len(self.table)
        for t, tup in enumerate(self.table[bucket]):
            if tup[0] == key:
                return bucket, t

        return None