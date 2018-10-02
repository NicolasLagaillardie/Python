def secToymwdhms(nb_sec):
    """Converts a periode in secondes to years, months, weeks, days, hours, minutes and secondes"""
    q,s=divmod(nb_sec,60)
    h,m=divmod(q,60)
    j,h=divmod(h,24)
    mo,j=divmod(j,30)
    se,j=divmod(j,7)
    a,mo=divmod(mo,12)
    return "%d:%d:%d:%d:%d:%d:%d" %(a,mo,se,j,h,m,s)
