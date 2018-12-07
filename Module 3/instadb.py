import cx_Oracle
import pprint
import datetime

con = cx_Oracle.connect("ARPIT/arpit123@localhost/xe")
cur = con.cursor()

def __max_likes__():
    # maximum likes
    cur.execute("select PictureID, count(likedby) from Likes group by (PictureID)")
    op = cur.fetchall()
    max = 0
    id = 0
    for o in op:
        if (o[1] > max):
            max = o[1]
            id = o[0]
        else:
            continue

    print("Maximum likes are to picture: ", id, " No. of maximum likes is: ", max)

def __min_likes__():    
    # minimum likes
    cur.execute("select PictureID, count(likedby) from Likes group by (PictureID)")
    op = cur.fetchall()
    min = 999
    id = 0
    for o in op:
        if (o[1] < min):
            min = o[1]
            id = o[0]
        else:
            continue

    print("Minimum likes are to picture: ", id, " No. of minimum likes is: ", min)


def __who_liked_most__():
    # who liked most
    cur.execute("select likedby, count(pictureid) from Likes group by (likedby)")
    op = cur.fetchall()

    max = 0
    id = 0
    for i in op:
        if (i[1] > max):
            max = i[1]
            id = i[0]
        else:
            continue
    print("Maximum likes are by user: ", id, " No. of maximum likes is: ", max)


def __music_pictures__():
    # music pictures
    cur.execute("select pictureID from pics where music=1")
    op = cur.fetchall()
    print("The pictures with music tags are with picture ID: ")
    for i in op:
        print(i[0])


def __most_popular_tag__():
    # most popular tag
    cur.execute(
        """select sum(arts)"Arts",sum(science) "Science",sum(music)"Music",sum(history)"History",sum(engineering)"Engineering" from Pics""")
    op = cur.fetchall()
    sumop = {}
    i = 0
    for x in cur.description:
        sumop.update({x[0]: op[0][i]})
        i += 1

    maxval = 0
    maxkey = ""
    for key, value in sumop.items():
        if value > maxval:
            maxval = value
            maxkey = key

    print("Most popular tag is ", maxkey, " with ", maxval, " likes")


def __oldie__():
    # tag pictures older than 1 year
    old = cur.execute("select pictureid from pics where extract(year from dateofpost)<2017 order by dateofpost").fetchall()
    print("Old post")
    for oldie in old:
        print(oldie[0])



def __most_liked_user__():
    # most liked user
    raw_likes = cur.execute(
        """select count(likedby) as "max likes", pictureid from Likes group by (pictureid)""").fetchall()
    likes_list = []
    for raw in raw_likes:
        likes_dict = {}
        likes_dict["picid"] = raw[1]
        likes_dict["likedby"] = raw[0]
        likes_dict["userid"] = int(raw[1] / 100)
        likes_list.append(likes_dict.copy())
    # pp=pprint.PrettyPrinter(indent=4)
    # pp.pprint(likes_list)

    max_likes = 0
    max_liked_user = 0
    for i in range(1, 6):
        likes = 0
        for row in likes_list:
            if row['userid'] == i:
                likes += row['likedby']
        print("Total likes for", i, "is", likes)
        if likes > max_likes:
            max_likes = likes
            max_liked_user = i

    print("Max liked user is", max_liked_user, "with", max_likes, "likes")



def __delete_inactive_users__():
    # delete inactive users
    raw_raw_inactive = cur.execute("""select userid,dateofpost from Pics order by userid asc, dateofpost desc""").fetchall()
    raw_inactive = []
    for i in range(1, 6):
        for raw_raw in raw_raw_inactive:
            if raw_raw[0] == i:
                raw_inactive.append((raw_raw[0], raw_raw[1]))
                break

    # print("Raw Inactive",raw_inactive)
    date = datetime.datetime.today()
    i = 1
    for raw in raw_inactive:
        if raw[0] != i:
            print("User", i, "is inactive")
            i += 1
        else:
            difference = date - raw[1]
            # print(difference)
            if difference.days > 365:
                print("User", raw[0], "is inactive for ", difference.days, "days")
            i += 1

choice=1
while(choice in range(1,9)):
    choice=int(input("""
    1.Max Likes
    2.Min Likes
    3.Who liked most
    4.Music pictures
    5.Popular Tag
    6.Most liked User
    7.Old Tagging
    8.Delete Inactive Users 
    9.Exit\n"""))

    if choice==1:
        __max_likes__()
    elif choice==2:
        __min_likes__()
    elif choice==3:
        __who_liked_most__()
    elif choice==4:
        __music_pictures__()
    elif choice==5:
        __most_popular_tag__()
    elif choice==6:
        __most_liked_user__()
    elif choice==7:
        __oldie__()
    elif choice==8:
        __delete_inactive_users__()
    elif choice==9:
        print("Bye")
    else:
        print("Exit")


