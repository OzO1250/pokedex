#This function compare the Pokemon in both the API call and the GSheet file, then create a new array merging both Pokemon but removing the duplicates
def compare_poke(api_list, gsheet_list):
    a = api_list

    b = gsheet_list

    c = b

    for d in a:
        #print("%s - %s" % (x,d[1]))
        for e in b:
            if (d[1] == e[1]):
                #print("%s AND %s are the same" % (e,d))
                #print(b.index(e))
                c.pop(b.index(e))

    c=a+c

    d = sorted(c,key=lambda x:int(x[0]))
    #print("Cuarto arreglo %s" % d)

    return d