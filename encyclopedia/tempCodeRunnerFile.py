def related_pages(search):
    relatedPages = []
    
    for sent in list_entries():
       for term in sent.split():
             if entrySearch in term:
               yield term
    return related
    
