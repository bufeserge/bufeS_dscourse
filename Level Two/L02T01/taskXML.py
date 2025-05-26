# L02T01 : Data Structures


# INSTRUCTIONS : Create a python program called taskXML.py. Write the code to:
#                           -Read in the movie.xml file.
#                           -Read about the iter() and itertext() function here. Use the iter() function to list all the child tags of the movie element.
#                           -Use the itertext() function to print out the movie descriptions.
#                           -Find the number of movies that are favourites and the number of movies that are not.
#
#
#
# i'll start by parsing the movie.xml file with ElementTree
# i'll go through each <movie> tag under any genre and decade using nested loops or findall
# i'll use iter() to list all the child tags inside each movie (like format, year, etc)
# i'll use itertext() to extract and print the text inside description tags
# i'll also look at the 'favorite' attribute (case-insensitive) to count how many are true or false


import xml.etree.ElementTree as ET  # import the ElementTree module to parse XML data

tree = ET.parse("movie.xml")  # parse the XML file and store it as an ElementTree object
root = tree.getroot()  # get the root element, which is <collection>

favourite_count = 0  # counter to track how many movies are marked as favourites
non_favourite_count = 0  # counter to track how many are not favourites

print(
    "\nAll child tags inside <movie> elements:\n"
)  # label for clarity before listing tags

# loop through all genres inside the collection
for genre in root.findall("genre"):  # loop over each <genre> element
    for decade in genre.findall("decade"):  # loop over each <decade> within the genre
        for movie in decade.findall(
            "movie"
        ):  # loop over each <movie> within the decade
            print(
                f"Movie Title: {movie.attrib.get('title')}"
            )  # print the movie title from the attributes

            for (
                child
            ) in movie.iter():  # use .iter() to go through all tags under each <movie>
                if child.tag != "movie":  # skip the outer <movie> tag itself
                    print(
                        f"  Tag: {child.tag}"
                    )  # print the tag name of each child element

print("\nMovie Descriptions:\n")  # label before printing descriptions

# loop again through all movies to print their descriptions
for genre in root.findall("genre"):  # loop over each genre
    for decade in genre.findall("decade"):  # loop over each decade
        for movie in decade.findall("movie"):  # loop over each movie
            for description in movie.findall(
                "description"
            ):  # find the <description> tag inside each movie
                print(
                    description.text.strip()
                )  # print the text inside <description>, stripped of whitespace

print("\nCounting favourites:\n")  # label before showing counts

# final loop to count favourites vs non-favourites
for genre in root.findall("genre"):  # go through each genre
    for decade in genre.findall("decade"):  # go through each decade
        for movie in decade.findall("movie"):  # go through each movie
            fav = movie.attrib.get(
                "favorite", "False"
            ).lower()  # get the favorite attribute (default to False), lowercased
            if fav == "true":  # check if it's marked as favourite
                favourite_count += 1  # add to favourites count
            else:  # anything not explicitly marked true is treated as not favourite
                non_favourite_count += 1  # add to non-favourites count

print(
    f"Number of favourite movies: {favourite_count}"
)  # print total favourite movie count
print(
    f"Number of non-favourite movies: {non_favourite_count}"
)  # print total non-favourite movie count
