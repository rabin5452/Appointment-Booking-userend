from databasecon import cnx,cursor
import time
def get_token(email):
        query="Select tokenid,arrivaltime,waitingtime from tokendata where email=%s"
        values=email
        cursor.execute(query,(values,))
        access_pass=cursor.fetchall()
        cnx.commit()
        print(access_pass)
        tokeninfo=access_pass[0]
        return tokeninfo


# system will indicate                                  
def check_avalailability():
        return 0

#system will indicate on cashier manual input
def check_notification():
        return 1

## to check that wheather user have already taken token or not
def check_onetimetokenrequest(email):
        ac_tokenid=None
        query="SELECT tokenid from tokendata where email=%s"
        values=email
        access_pass=tuple()
        cursor.execute(query,(values,))
        access_pass=cursor.fetchall()
        for i in access_pass:
                ac_tokenid=i[0]
        cnx.commit()
        if ac_tokenid==None:
                ## not taken
                return 0
        else:   
                ## alredy taken
                return 1

def absentusercheck(email):
        query="Select tokenid from absenttable where email=%s"
        values=email
        cursor.execute(query,(values,))
        try:
                data=cursor.fetchone()
                print(data)
                if data[0]>0:
                        return 1
                else:
                        return 0
        except TypeError:
                return 0
        
def absentdetail(email):
        query="Select tokenid from absenttable where email=%s"
        values=email
        cursor.execute(query,(values,))
        try:
                data=cursor.fetchall()
                if data is not None:
                        return data[0]
                else:
                        return 0
        except TypeError:
                return 0
