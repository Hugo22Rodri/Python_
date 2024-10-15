countries = {"MX", "COL", "ARG", "USA"}
northAm=  {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
suothAm = {"COL", "BZ", "ARG"}

new_set = countries.union (northAm | centralAm | suothAm)
print(new_set)