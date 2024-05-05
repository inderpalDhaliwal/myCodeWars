def difference_in_ages(ages):
    if not ages:
        return(0,0,0)
    youngest = min(ages)
    oldest = max(ages)
    age_diff = oldest - youngest 
    
    return (youngest, oldest, age_diff)