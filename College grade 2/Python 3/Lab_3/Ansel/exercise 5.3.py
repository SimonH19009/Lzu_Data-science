import collections
import sys

ID,FORENAME,MIDDLENAME,SURNAME,DEPARTMENT=range(5)

User=collections.namedtuple("User","username forename middlename surname id")
s=0

def print_users(users):
    global s
    namewidth=17
    usernamewidth=9
    title1 = "{0:<{nw}}{1:^6}{2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth)
    title2 = "{0:-<{nw}}{0:-<6}{0:-<{uw}}".format("",nw=namewidth,uw=usernamewidth)
    title  =(title1+"  "+title1 + "\n" +title2 +"  " + title2)
    print(title)
    for key in sorted(users):
        s=s+1
        user=users[key]
        initial=""
        if user.middlename:
            initial=" "+user.middlename[0]
        name="{0.surname},{0.forename}{1}".format(user,initial)
        if s%2==1:
            print("{0:.<{nw}.{nw}}({1.id:4}){1.username:{uw}}".format(name,user,nw=namewidth,uw=usernamewidth),end="")
            print("  ",end="")
        if s%2==0 and (s+2)%64!=1:print("{0:.<{nw}.{nw}}({1.id:4}){1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))
        if (s+2)%64==1:
            print(title)
            print("{0:.<{nw}.{nw}}({1.id:4}){1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth),
                  end="")

def main():
    if len(sys.argv)==1 or sys.argv[1] in {"-h","--help"}:
        print("usage:{0} file1 [file2 [... fileN]]".format(sys.argv[0]))
        sys.exit()

    usernames=set()
    users={}
    for filename in sys.argv[1:]:
        for line in open(filename,encoding="utf8"):
            line=line.rstrip()
            if line:
                user=process_line(line,usernames)
                users[(user.surname.lower(),user.forename.lower(),user.id)]=user
    print_users(users)


def generate_username(fields, usernames):
    username=((fields[FORENAME][0]+fields[MIDDLENAME][:1]+fields[SURNAME]).replace("-","").replace("'",""))
    username=original_name=username[:8].lower()
    count=1
    while username in usernames:
        username ="{0}{1}".format(original_name,count)
        count+=1
    usernames.add(username)
    return username


def process_line(line,usernames):
    fields=line.split(":")
    username=generate_username(fields,usernames)
    user=User(username,fields[FORENAME],fields[MIDDLENAME],fields[SURNAME],fields[ID])
    return user

main()

