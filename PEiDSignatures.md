# Introduction #

Since version 1.2.6 _pefile_ supports parsing PEiD's signatures. Comprehensive signature datbases can be found at:

http://www.PEiD.info/BobSoft/Downloads.html (Look for UserDB.TXT)

Thanks to [PEiD](http://www.PEiD.info/) and [BobSoft](http://www.PEiD.info/BobSoft/) for the signatures!


# Usage #

## Loading ##

First import the new module, _peutils_, included with _pefile_

```
import peutils
```

Then we need to load a signature database, we can do this in different ways.

  * Loading a database from a file in the local filesystem

```
signatures = peutils.SignatureDatabase('/path/to/signature.txt')
```

  * Loading a database directly from a URL

```
signatures = peutils.SignatureDatabase('http://url.to/signature/file.txt')
```

  * And finally, directly from data (for instance, if we have already read and loaded the contents of a database)

```
with file('/path/to/signature/file.txt', 'rt') as f: 
    sig_data = f.read()
signatures = peutils.SignatureDatabase(data=sig_data)
```

It's also possible to aggregate more signatures to an already created instance by just using the _load()_ method:

```
signatures.load('/Users/ero/Devel/pefile/userdb-extra.txt')
```


## Matching ##

Once we have a _SignatureDatabase_ instance, we can run PE instances through it in order to find matching packer signatures:

```
matches = signatures.match(pe, ep_only = True)
```


### Output ###

```
['Upack 0.24 - 0.27 beta / 0.28 alpha -> Dwing']
```


We can also get all possible matches found as the signature tree is walked. The last signature will always be the most precise (as more bytes will have been matched) and is the one returned by the _match()_ method.

```
matches = sig.match_all(pe, ep_only = True)
```

### Output ###
```
[['Upack v0.1x - v0.2x -> Dwing'], 
['Upack v0.24 ~ v0.28 Alpha -> Dwing'], 
['Upack 0.24 - 0.27 beta / 0.28 alpha -> Dwing']]
```


## Signature generation ##

Experimental and not specially intelligent when generating signatures, _peutils_ is able to generate a signature for a given PE file.

One can generate signatures for the entry point of a PE file as follows:

```
signatures.generate_ep_signature(pe, 'Name of the signature', length_of_the_signature)
```


Alternatively signatures for all section in a PE file can be generated as follows:


```
signatures.generate_section_signatures(pe, 'Name of the signature', length_of_the_signature)
```


Both of those methods will return a string following the same format as any other PEiD signature. For instance (straight out of UserDB.txt)

```
[!EP (ExE Pack) V1.0 -> Elite Coding Group]
signature = 60 68 ?? ?? ?? ?? B8 ?? ?? ?? ?? FF 10
ep_only = true


[$pirit v1.5]
signature = ?? ?? ?? 5B 24 55 50 44 FB 32 2E 31 5D
ep_only = true


[* PseudoSigner 0.1 [32Lite 0.03] --> Anorganix]
signature = 60 06 FC 1E 07 BE 90 90 90 90 6A 04 68 90 10 90 90 68 ?? ?? ?? ?? E9 ?? ?? ?? ??
ep_only = true
```