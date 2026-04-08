from . import imphash_ws2_32, oleaut32, ws2_32, wsock32

"""
A small module containing a database of ordinal to symbol mappings for DLLs
which frequently get linked without symbolic information.
"""

ords = {
    b"oleaut32.dll": oleaut32.ord_names,
    b"ws2_32.dll": ws2_32.ord_names,
    b"wsock32.dll": wsock32.ord_names,
}

# Imphash-specific ordinal tables frozen to the state prior to the August 2024
# change so that imphash values remain compatible with YARA, YARA-X, and other
# tools based on the original pefile implementation.  wsock32 is mapped to the
# same table as ws2_32 because that was the original pefile behaviour.
imphash_ords = {
    b"oleaut32.dll": oleaut32.ord_names,
    b"ws2_32.dll": imphash_ws2_32.ord_names,
    b"wsock32.dll": imphash_ws2_32.ord_names,
}


def formatOrdString(ord_val):
    return "ord{}".format(ord_val).encode()


def ordLookup(libname, ord_val, make_name=False):
    """
    Lookup a name for the given ordinal if it's in our
    database.
    """
    names = ords.get(libname.lower())
    if names is None:
        if make_name is True:
            return formatOrdString(ord_val)
        return None
    name = names.get(ord_val)
    if name is None:
        return formatOrdString(ord_val)
    return name


def ordLookupForImphash(libname, ord_val, make_name=False):
    """
    Lookup a name for the given ordinal using the imphash-specific database.

    This uses ordinal tables that are frozen to the state prior to the August
    2024 change so that imphash values remain compatible with YARA, YARA-X,
    VirusTotal, and other tools based on the original pefile implementation.
    """
    names = imphash_ords.get(libname.lower())
    if names is None:
        if make_name is True:
            return formatOrdString(ord_val)
        return None
    name = names.get(ord_val)
    if name is None:
        return formatOrdString(ord_val)
    return name
