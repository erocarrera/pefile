from . import oleaut32, ws2_32, wsock32

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
