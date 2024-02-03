from bs4 import BeautifulSoup

names_list = []
landmark_location_list = []
info_list = []
lowest_price_site_list = []
rating_review_list = []
visual_list = []

for i in range(1,10):

    with open(f'trivago{i}.html', 'r', encoding='utf-8') as file:
        data = file.read()

    soup = BeautifulSoup(data, 'lxml')

    # map_location = soup.find_all('ul', class_='flex flex-wrap leading-normal')
    # print(len(map_location))
    # print(i)
    # for i in range(len(map_location)):
    #     print(map_location[i].text)
    #     if i == 5:
    #         break


    # SCRAPING NAMES OF THE HOTELS
    name = soup.find_all('button' , class_="ItemNameSection_itemNameButton__sWjFo")
    # PRINT RELATED TO HOTEL NAMES
    # print(len(name))
    # for i in range(len(name)):
    #     print(name[i].text)
    #     if i==5:
    #         break

    # MAKING LIST OF THE SCRAPED HOTEL NAMES

    for i in range(len(name)):
        names_list.append(name[i].text)
    # PRINT RELATED TO names_list
    # print(len(names_list))
    # print("")



    # SCRAPING LANDMARK LOCATION OF THE HOTELS
    landmark_location = soup.find_all('span' , class_="block text-left w-11/12 text-m")
    # PRINT RELATED TO HOTEL NAMES
    # print(len(landmark_location))
    # for i in range(len(landmark_location)):
    #     print(landmark_location[i].text)
    #     if i==5:
    #         break

    # MAKING LIST OF THE SCRAPED HOTEL LANDMARK LOCATION

    for i in range(len(landmark_location)):
        landmark_location_list.append(landmark_location[i].text)
    # PRINT RELATED TO landmark_location_list
    # print(len(landmark_location_list))
    # print("")

        # # INFO LOCATION (LOCATION UNDER INFO TAB OF EACH HOTEL)
        # info_location = soup.find_all('span' , class_="inline-block mb-1")
        # print(len(info_location))
        # info_location_list = []
        # j = 0
        # s = ''
        # for i in range(len(info_location)):
        #     if j != 4 :
        #         s = s + info_location[i].text
        #         j = j + 1
        #     else:
        #         info_location_list.append(s)
        #         s = info_location[i].text
        #         j = 1
        # print(len(info_location_list))
        # for i in range(len(info_location_list)):
        #     print(info_location_list[i])
        #     if i == 5:
        #         break
        # print("")



    # SCRAPING INFO (i.e. LOCATION , TELEPHONE , FAX , ONLINE_SITE) OF THE HOTELS
    info = soup.find_all('div' , class_="text-m")
    # # PRINT RELATED TO INFO
    # print(len(info))

    # MAKING LIST OF THE ABOVE MENTIONED DATA
    # ... SEEMS LIKE THERE ARE SOME OTHER DATA WITH THE SAME TAG AS THIS
    # ... SO WE FILTER ONLY THE ABOVE MENTIONED DATA THAT WE NEED
    # ... WE DO IT BY CHECKING IF ", United Kingdom" IS IN THE DATA WE GOT

        #c = 0
    for i in range(len(info)):
        if ", United Kingdom" in info[i].text:
            info_list.append(info[i].text)
            #c = c + 1

            # PRINT RELATED TO INFO
            # if i < 16:
            #     print(info[i].text)

        #print(c)
    # PRINT RELATED TO info_list
    # print(len(info_list))
    # print("")


        # INTENDED TO TAKE THE PRICE THAT IS SHOWING IN BIG SIZE
        # ... BUT THAT IS NOT LOWEST PRICE . THE SMALL SIZE PRICE IS THE LOWEST PRICE
        # ... SO WE COMMENTED-IT-OUT
        # prices = soup.find_all('p' , class_="font-bold text-xl text-grey-900")
        # print(len(prices))
        # # print(prices[0].text)
        # for i in range(len(prices)):
        #     print(prices[i].text)
        #     if i==5:
        #         break
        # print("")
        # prices_list = []
        # for i in range(len(prices)):
        #     prices_list.append(prices[i].text)

        # rating = soup.find_all('span' , itemprop="ratingValue")
        # print(len(rating))
        # for i in range(len(rating)):
        #     print(rating[i].text)
        #     if i==5:
        #         break


        # INTENDED TO TAKE THE SITE THAT IS SHOWING IN BIG SIZE ALONG WITH BIG SIZE PRICE
        # ... BUT THAT IS NOT LOWEST PRICE . THE SMALL SIZE WEBSITE IS THE LOWEST PRICE
        # ... SO WE COMMENTED-IT-OUT
        # lowest = soup.find_all('strong' , class_="advertiser-name-placeholder text-m")
        # print(len(lowest))
        # for i in range(len(lowest)):
        #     print(lowest[i].text)
        #     if i==5:
        #         break
        # lowest_list = []
        # for i in range(len(lowest)):
        #     lowest_list.append(lowest[i].text)




    # SCRAPING THE LOWEST PRICE AND THE RESPECTIVE WEBSITE ITS OFFERED ON , TOGETHER
    lowest_price_site = soup.find_all('span' , class_="flex items-center gap-x-1")
    # PRINT RELATED TO LOWEST PRICE-SITE
    # print(len(lowest_price_site))
    # for i in range(len(lowest_price_site)):
    #     print(lowest_price_site[i].text)
        # if i==5:
        #     break

    # MAKING LIST OF THE ABOVE MENTIONED DATA

    for i in range(len(lowest_price_site)):
        lowest_price_site_list.append(lowest_price_site[i].text)
    # PRINT RELATED TO lowest_price_site_list
    # print(len(lowest_price_site_list))
    # print("")



    # SCRAPING THE RATING , REVIEW , REVIEW_COUNT OF THE HOTEL ALTOGETHER
    # ... COZ FOR SOME HOTELS RATINGS WAS MISSING
    # ... SO IF WE TAKE EACH OF THE 3 INDIVIDUALLY , IF AT ONE PLACE THE RATING MISSES , THE RATING OF THE NEXT HOTEL WILL SHIFTED TO THE MISSING HOTEL WHEN ALL THE FEATURES ARE JOINED TOGETHER
    # ... HENCE WE TRY TO TAKE THE 3 AS ONE UNIT , AND CHECK IF RATING IS NOT THERE, IF NOT ... WE INSERT NULL INTO IT
    # ... THEREBY PREVENTING THE NEXT HOTELS RATING BE SHIFTED UPWARDS TO THE HOTEL WHERE RATING IS MISSED
        #rating_review = soup.find_all('strong' , class_="leading-none")
    rating_review = soup.find_all('span' , class_="mt-px truncate")
    # PRINT RELATED TO RATING REVIEW
    # print(len(rating_review))
    # for i in range(len(rating_review)):
    #     print(rating_review[i].text)
    #
    #     if i== 5:
    #         break

    # MAKING LIST OF THE ABOVE MENTIONED DATA

    for i in range(len(rating_review)):
        rating_review_list.append(rating_review[i].text)
    # PRINT RELATED TO rating_review_list
    # print(len(rating_review_list))
    # print("")

        # rating_review_list = []
        # c = 0
        # for i in range(len(rating_review)):
        #     if 'reviews)' in rating_review[i].text:
        #         rating_review_list.append(rating_review[i].text)
        #         c = c + 1
        #
        #         if i < 12:
        #             print(rating_review[i].text)
        # print(c)
        #print("")

        # rating_review_list = []
        # for i in rating_review:
        #     if i.text[0] != '£':
        #         rating_review_list.append(i.text)



    # SCRAPING IMAGES OF THE HOTELS
    visual = soup.find_all('img' , class_="select-none bg-grey-500 ItemImage_placeholder__9n0hj object-cover")
    # PRINT RELATED TO IMAGES
    # print(len(visual))
    # for i in range(len(visual)):
    #     print(visual[i]['src'])
    #     if i==5:
    #         break

    # MAKING LIST OF THE ABOVE MENTIONED DATA

    for i in range(len(visual)):
        visual_list.append(visual[i]['src'])
    # PRINT RELATED TO visual_list
    # print(len(visual_list))
    # print("")



import pandas as pd

# READYING THE COLUMNS FOR THE DATAFRAME WHERE ALL THE ABOVE FEATURE LISTS ARE GONNA BE INSERTED INTO
# ... SO WE FIRST MAKE A DICTIONARY WITH KEYS AS COLUMN NAMES & ITEMS AS THE ABOVE FEATURE LISTS
trivago_raw = {
    'Name' : names_list ,
    'Landmark_Location' : landmark_location_list ,
    'Contact_Info' : info_list ,
    'Lowest_Price-Site' : lowest_price_site_list ,
    'Rating-Review-Num' : rating_review_list ,
    'Visual' : visual_list
}

trivago_raw_list = list(trivago_raw.values())

# PRINT EACH FEATURE LIST
# for i in trivago_raw_list[0]:
#     print(i)
# print(len(trivago_raw_list[0]))


# CREATING THE DATAFRAME USING THE ABOVE DICTIONARY
trivago_raw_df = pd.DataFrame(trivago_raw)

# PRINT RELATED TO RAW DATAFRAME
# print("Trivago Raw Dataframe")
# for i in trivago_raw_df.columns:
#     print(trivago_raw_df[i].head())
#
# print(str(trivago_raw_df))
# print("")



# CREATING A CSV FILE OF THE RAW DATA WITHOUT CLEANING
#trivago_raw_df.to_csv('trivago_sample_before_cleaning.csv', index=False)



# CLEANING STARTS

# MAKING A COPY OF THE ORIGINAL RAW DATA
# ... JUST IN CASE IF WE CHANGE THINGS AND WE WANNA GO BACK AGAIN TO THE ORIGINAL RAW DATA
trivago_cleaned = trivago_raw_df


# CLEANING INFO COLUMN
# ... THAT HAS LOCATION , TELEPHONE , FAX , ONLINE_SITE OF THE HOTELS

# CLEANING LOCATION
def extract_loc(info):

    uk_index_start = info.find("United Kingdom")
    uk_index_end = uk_index_start + len("United Kingdom")

    loct = info[:uk_index_end]

    return loct

loct = map(extract_loc , trivago_cleaned['Contact_Info'])
loct_list = list(loct)
# for i in range(len(loct_list)):
#     print(loct_list[i])
#
#     if i== 10:
#         break
#print(len(loct_list))

# ADDING LOCATION COLUMN
trivago_cleaned['Location'] = loct_list


# CLEANING TELEPHONE
def extract_tele(info):

    if "Telephone:" in info:

        telephone_start_index = info.find("Telephone:")
        telephone_end_index = telephone_start_index + len("Telephone:")

        number_start_index = telephone_end_index+1

        if "|" in info:
            number_end_index = info.find("|")
            number_end_index = number_end_index -1
        else :
            number_end_index = len(info)


        return info[number_start_index : number_end_index]

    else:
        return None

tele = map(extract_tele , trivago_cleaned['Contact_Info'])
tele_list = list(tele)
# for i in range(len(tele_list)):
#     print(tele_list[i])
#
#     if i== 10:
#         break
#print(len(tele_list))

# ADDING TELEPHONE COLUMN
trivago_cleaned['Telephone'] = tele_list



# CLEANING FAX
def extract_fax(info):

    if "Fax:" in info:

        fax_start_index = info.find("Fax:")
        fax_end_index = fax_start_index + len("Fax:")

        num_start_index = fax_end_index + 1


        if info.count("|") == 2:

            first_line_index = info.find("|")

            second_line_index = info.find("|" , first_line_index + 1)

            num_end_index = second_line_index - 1

        else :

            num_end_index = len(info)


        return info[num_start_index: num_end_index]

    else:

        return None



faxx = map(extract_fax , trivago_cleaned['Contact_Info'])
faxx_list = list(faxx)
# for i in range(len(faxx_list)):
#     print(faxx_list[i])
#
#     if i== 10:
#         break
# print(len(faxx_list))

##ADDING LOCATION COLUMN
trivago_cleaned['Fax'] = faxx_list




    # # SPLITTING THE INFO COLUMN INTO ...
    # # ... SEPERATE FAX & ONLINE SITE COLUMN COZ THEY HAVE THE SAME SEPERATION CHARACTER "|" BETWEEN THEM
    # # ... LOCATION & TELEPHONE ARE SEPERATED BY A DIFFERENT CHARACTER ":"
    # # ... SO FOR NOW THESE 2 ARE TOGETHER ... LATER WHE WILL SPLIT THESE 2 ALSO
    # trivago_cleaned[['Location-Telephone', 'Fax', 'Site']] = trivago_cleaned['Contact_Info'].str.split('|', expand=True)
    #
    #
    # # PRINT RELATED TO THE ABOVE FAX & SITE & LOCATION-TELEPHONE SEPERATED
    # # but Location & Telephone still together
    # # print("Trivago Fax & Site seperated")
    # # for i in trivago_cleaned.columns:
    # #     print(trivago_cleaned[i].head())
    # # print("")
    #
    #
    # # DROPPING THE ALL INFO COLUMN , SINCE WE WONT BE NEEDING IT , WE ALREADY MADE THE SPLIT
    # trivago_cleaned.drop('Contact_Info' , axis=1 , inplace=True)
    #
    #
    # # SPLITTING LOCATION & TELEPHONE ON ":" CHARACTER
    # trivago_cleaned[['Location','Telephone']] = trivago_cleaned['Location-Telephone'].str.split(':', expand=True)
    #
    # # PRINT RELATED TO THE ABOVE LOCATION & TELEPHONE SEPERATED
    # # But the word telephone is still attached with Location at the end
    # # print("Trivago Address and Telephone seperated")
    # # for i in trivago_cleaned.columns:
    # #     print(trivago_cleaned[i].head())
    # # print("")
    #
    #
    # # DROPPING THE 'Location-Telephone' COLUMN , SINCE WE WONT BE NEEDING IT , WE ALREADY MADE THE SPLIT
    # trivago_cleaned.drop('Location-Telephone' , axis=1 , inplace=True)
    # # DROPPING SITE COLUMN AS WE DONT NEED IT
    # trivago_cleaned.drop('Site' , axis=1 , inplace=True)
    #
    #
    #
    # # FAX CLEANING STARTS
    #
    # # None , FAX : NULL , Official Site , FAX : +the_number
    # # these are the different kinds of values in the Fax column
    # # ... we want to just extract the fax number i.e. the value after "+"
    # # ... and make all other values NULL i.e. None in dataframe case
    #
    #     # def fax_clean(fax_col):
    #     #     for fax in fax_col:
    #     #         if '+' not in fax:
    #     #             return None
    #     #         else:
    #     #             return fax[5:]
    #     # #fax_num = map(fax_clean , trivago_cleaned['Fax'])
    #     #original_string[original_string.index('W'):]
    #     #x[x.index('+'):]
    #
    #
    # # FUNCTION TO EXTRACT THE FAX NUMBER INCLUDING THE +
    # fax_num = map(lambda x: x[x.index('+'):] if x is not None and '+' in x else None, trivago_cleaned['Fax'])
    # #result_map = map(lambda x: x*2 if x is not None else None, original_list)
    # fax_num_list = list(fax_num)
    #     #print(fax_num_list)
    #
    # # PRINT RELATED TO FAX_NUM LIST
    # # for i in fax_num_list:
    # #     print(i)
    # # print(len(fax_num_list))
    # # print(fax_num_list[0])
    # # print(type(fax_num_list[0]))
    # # # PRINT LENGTH OF EACH FAX ITEM
    # # for i in fax_num_list:
    # #     try:
    # #         print(len(i))
    # #     except:
    # #         print("0")
    # # print("")
    # #     # fax_num = map(lambda x: x[1:-4] if x is not None else None, fax_num_list)
    # #     # fax_num_list = list(fax_num)
    # #     # print(fax_num_list)
    # #     # print(type(fax_num_list[0]))
    # #     # print("")
    #
    #
    # # ADDING THE FAX COLUMN TO THE DATAFRAME
    # trivago_cleaned['Fax'] = fax_num_list
    #
    #
    # # PRINT RELATED TO FAX COLUMN
    # # print(trivago_cleaned['Fax'])
    # # print(trivago_cleaned['Fax'][0])
    # # print(type(trivago_cleaned['Fax'][0]))
    #
    #
    #
    # # LOCATION CLEANING STARTS
    #
    # # FUNCTION TO REMOVE 'Telephone' IF PRESENT AT THE END OF 'Location'
    # loc = map(lambda x: x[:-9] if 'Telephone' in x else x , trivago_cleaned['Location'])
    # loc_list = list(loc)
    # # PRINT RELATED TO LOCATION
    # # for i in loc_list:
    # #     print(i)
    # # print(len(loc_list))
    # # print(type(loc_list[0]))
    # # print("")
    #
    # # ADDING THE LOCATION COLUMN TO THE DATAFRAME
    # trivago_cleaned['Location'] = loc_list
    #
    #
    # # PRINT RELATED TO TELEPHONE COLUMN
    # # for i in trivago_cleaned['Telephone']:
    # #     print(i)
    # # print(type(trivago_cleaned['Telephone'][0]))
    # # print(len(trivago_cleaned['Telephone']))
    # # print("")




# PRICE CLEANING STARTS

    # PRINT RELATED TO THE INITIAL 'Lowest_Price-Site' Column
    # for i in trivago_cleaned['Lowest_Price-Site']:
    #     print(i)

import re
    # only_price = re.findall(r'\d+', trivago_cleaned['Lowest_Price-Site'][0])
    # print(only_price[0])
    # print(type(int(only_price[0])))


# FUNCTION TO EXTRACT JUST THE BEST PRICE FOR THAT HOTEL

def extract_price(Price_Site):
    only_price = re.findall(r'\d+', Price_Site)
    only_price = only_price[0]
    only_price = int(only_price)

    return only_price

price = map(extract_price , trivago_cleaned['Lowest_Price-Site'])
price_list = list(price)

# PRINT RELATED TO price_list
# for i in price_list:
#     print(i)
# print("")
# print(len(price_list))
# print(type(price_list[0]))
# print("")

# ADDING PRICE COLUMN TO THE DATAFRAME
trivago_cleaned['Room_Prices'] = price_list


# Best_Offer_Site CLEANING STARTS
    # only_site = re.findall(r'[a-zA-Z]+', trivago_cleaned['Lowest_Price-Site'][0])
    # print(only_site[0])
    # print(type(only_site[0]))
    # alphabets = re.findall(r'[a-zA-Z]+', my_string)


# FUNCTION TO EXTRACT JUST THE NAME OF THE SITE OFFERING THE BEST PRICE FOR THAT HOTEL
def extract_site(Price_Site):
    only_site_list = re.findall(r'[a-zA-Z]+', Price_Site)
    only_site_str = '.'.join(only_site_list)

    return only_site_str


site = map(extract_site , trivago_cleaned['Lowest_Price-Site'])
site_list = list(site)

# PRINT RELATED TO site_list
# for i in site_list:
#     print(i)
# print("")
# print(len(site_list))
# print(type(site_list[0]))
# print("")

# ADDING 'Best_Offer_Site' COLUMN TO DATAFRAME
trivago_cleaned['Best_Offer_Site'] = site_list

# DROPPING 'Lowest_Price-Site' COLUMN AS WE CLEANED IT
trivago_cleaned.drop('Lowest_Price-Site' , axis=1 , inplace=True)



# 'Rating-Review-Num' CLEANING STARTS

    # PRINT RELATED TO THE INITIAL 'Lowest_Price-Site' Column
    # for i in trivago_cleaned['Rating-Review-Num']:
    #     print(i)
    # print(len(trivago_cleaned['Rating-Review-Num']))
    # print("")


# FUNCTION TO INSERT None WHEREVER Review IS MISSING
def insert_none(r):
    if '-' not in r:
        s = ''
        brac_index = r.index("(")
        s = r[:brac_index] + "- None " + r[brac_index:]

        return s

    else:
        return r

print("")

rrm = map(insert_none , trivago_cleaned['Rating-Review-Num'])
rrm_list = list(rrm)

# PRINT RELATED TO rmm_list
# for i in rrm_list:
#     print(i)
# print("")
# print(len(rrm_list))
# print(type(rrm_list[0]))
# print("")

# UPDATING THE COLUMN BY INSERTING None WHEREVER Review IS MISSING
trivago_cleaned['Rating-Review-Num'] = rrm_list



# RATING cleaning starts

#trivago_cleaned[['Rating_Review', 'Review_Count']] = trivago_cleaned['Rating-Review-Num'].str.split('-', expand=True)

# FUNCTION TO JUST EXTRACT THE FIRST 3 CHARACTERS WHICH IS RATING
# ... THE WHOLE NUMBER PART(1) , DECIMAL DOT .(2) , DECIAML NUMBER PART(3)
only_rating = map(lambda x: float(x[:3]) , trivago_cleaned['Rating-Review-Num'] )
only_rating_list = list(only_rating)

# PRINT RELATED TO only_rating_list
# print(len(only_rating_list))
# print(only_rating_list[0])
# print(type(only_rating_list[0]))
# print("")

# ADDING RATING COLUMN TO THE DATFRAME
trivago_cleaned['Rating'] = only_rating_list



# REVIEW COUNT CLEANING STARTS

# FUNCTION TO EXTRACT JUST THE NUMBER OF REVIEWS
def review_count_extract(r):
    brac_index = r.index('(')
    review_count_part = r[brac_index+1 : -9]
    review_count_part = int(review_count_part)

    return review_count_part

only_review_count = map(review_count_extract , trivago_cleaned['Rating-Review-Num'] )
only_review_count_list = list(only_review_count)

# PRINT RELATED TO only_review_count_list
# print(len(only_review_count_list))
# print(only_review_count_list[0])
# print(type(only_review_count_list[0]))
# print("")

# ADDING REVIEW COUNT TO THE DATAFRMAE
trivago_cleaned['Review_Count'] = only_review_count_list


# REVIEW CLEANING STARTS

# FUNCTION TO EXTRACT JUST THE REVIEW
def review_extract(r):
    if "None" not in r:
        hyphen_index = r.index('-')
        brac_index = r.index('(')
        review_part = r[hyphen_index+2 : brac_index-1]

        return review_part

    else:
        return None

only_review = map(review_extract, trivago_cleaned['Rating-Review-Num'])
only_review_list = list(only_review)

# PRINT RELATED TO only_review_list
# print(len(only_review_list))
# for i in only_review_list:
#     print(i)
# print(type(only_review_list[5]))
# print("")

# ADDING REVIEW COLUMN TO THE DATAFRMAE
trivago_cleaned['Review'] = only_review_list


# DROPPING 'Rating-Review-Num' COLUMN AS WE CLEANED IT
trivago_cleaned.drop('Rating-Review-Num' , axis=1 , inplace=True)


# CHECKING THE DATAFRAME AFTER CLEANING 'Rating-Review-Num' COLUMN
# BY NOW WE HAVE CLEANED ALL THE COLUMNS
# for i in trivago_cleaned.columns:
#     print(trivago_cleaned[i].head(12))
# print("")


# CHANGING THE ORDER OF THE COLUMNS
trivago_cleaned_order = (trivago_cleaned[
    ['Name','Location','Landmark_Location','Telephone','Fax','Room_Prices'
     ,'Best_Offer_Site','Rating', 'Review','Review_Count','Visual']]
)

# PRINT EACH COLUMN VALUES
# for i in trivago_cleaned_order['Name']:
#     print(i)
#
#     if i == 7:
#         break

# CHECKING THE DATAFRAME AFTER CHANGING THE ORDER OF THE CLEANED COLUMNS
print("Trivago Cleaned Ordered Dataframe")
for i in trivago_cleaned_order.columns:
    print(trivago_cleaned_order[i].head())
print(str(trivago_cleaned_order))
print("")


# WRITING THE FINAL DATAFRMAE TO CSV FILE
trivago_cleaned_order.to_csv('trivago_sample_after_cleaning.csv', index=False)


# CHOOSING ONLY THE 6 COLUMNS LIKE THE 2 PREVIOUS WEBSITES AND DOING THE SAME
trivago_like_bookings_cleaned_order = (trivago_cleaned[
    ['Name','Location','Room_Prices','Rating'
     ,'Review','Visual']]
)

# print("Trivago Like Bookings Cleaned Ordered Dataframe")
# for i in trivago_like_bookings_cleaned_order.columns:
#     print(trivago_like_bookings_cleaned_order[i].head())
#
# print(str(trivago_like_bookings_cleaned_order))
# print("")

# WRITING THE FINAL DATAFRMAE 6 COLUMNS TO CSV FILE
#trivago_like_bookings_cleaned_order.to_csv('trivago_like_bookings_sample_after_cleaning.csv', index=False)



    # # trivago_sample_cleaned[['Rating', 'Review']] = trivago_sample_cleaned['Rating-Review'].str.split('-', expand=True)
    # # for i in trivago_sample_cleaned.columns:
    # #     print(trivago_sample_cleaned[i].head())
    # # print("")
    # #
    # #
    # # trivago_sample_cleaned.drop('Rating-Review' , axis=1 , inplace=True)
    # # trivago_sample_cleaned = trivago_sample_cleaned[['Name','Location','Room_Prices','Rating','Review', 'Best_Offer_Site' ,'Visual']]
    # #
    # # for i in trivago_sample_cleaned.columns:
    # #     print(trivago_sample_cleaned[i].head())
    # #
    # # just_price = map(lambda x: int( x[1:].replace(",","") ) , trivago_sample_cleaned['Room_Prices'])
    # # just_price_list = list(just_price)
    # # print(just_price_list[:5])
    # # print(type(just_price_list[0]))
    # # print("")
    # # trivago_sample_cleaned['Room_Prices'] = just_price_list
    # #
    # # int_rating = map(lambda x: float(x), trivago_sample_cleaned['Rating'])
    # # int_rating_list = list(int_rating)
    # # print(int_rating_list[:5])
    # # print(type(int_rating_list[0]))
    # # print("")
    # # trivago_sample_cleaned['Rating'] = int_rating_list
    # # print("")
    # #
    # # for i in trivago_sample_cleaned.columns:
    # #     print(trivago_sample_cleaned[i].head())
    # #
    # # for i in trivago_sample_cleaned.columns:
    # #     print(type(trivago_sample_cleaned[i][0]))
    # #
    # # #trivago_sample_cleaned.to_csv('trivago_sample_after_cleaning.csv', index=False)
