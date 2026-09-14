from . import imphash_oleaut32, imphash_ws2_32, oleaut32, ws2_32, wsock32

"""
A small module containing a database of ordinal to symbol mappings for DLLs
which frequently get linked without symbolic information.
"""

ords = {
    b"oleaut32.dll": oleaut32.ord_names,
    b"ws2_32.dll": ws2_32.ord_names,
    b"wsock32.dll": wsock32.ord_names,
}


def format_ordinal(ord_val):
    return f"ord{ord_val}".encode()


def ordinal_lookup(libname, ord_val, make_name=False):
    """
    Lookup a name for the given ordinal if it's in our database.
    """
    names = ords.get(libname.lower())
    if names is None:
        if make_name is True:
            return format_ordinal(ord_val)
        return None
    name = names.get(ord_val)
    if name is None:
        return format_ordinal(ord_val)
    return name


# Imphash-specific ordinal tables must remain frozen to the state when the original
# implementation was written so that imphash values remain compatible with YARA,
# YARA-X, and other tools based on the original pefile implementation. wsock32 is
# mapped to the same table as ws2_32 because that was the original pefile behaviour.
imphash_ords = {
    b"oleaut32.dll": imphash_oleaut32.ord_names,
    b"ws2_32.dll": imphash_ws2_32.ord_names,
    b"wsock32.dll": imphash_ws2_32.ord_names,
}


def imphash_format_ordinal(ord_val):
    return f"ord{ord_val}".encode()


def imphash_ordinal_lookup(libname, ord_val, make_name=False):
    """
    Lookup a name for the given ordinal using the imphash-specific database.

    This uses ordinal tables that are frozen to the state when the original
    implementation was written so that imphash values remain compatible with
    YARA, YARA-X, VirusTotal, and other tools based on the original pefile
    implementation.
    """
    names = imphash_ords.get(libname.lower())
    if names is None:
        if make_name is True:
            return imphash_format_ordinal(ord_val)
        return None
    name = names.get(ord_val)
    if name is None:
        return imphash_format_ordinal(ord_val)
    return name
