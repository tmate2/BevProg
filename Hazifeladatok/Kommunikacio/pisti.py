def main():
    f = open("chatroom.txt","r")
    s = f.readline()
    
    while(s):
        print(s)
        s = f.readline()

    f.close
    f = open("chatroom.txt","a")
    message = input("pisti> ")
    print(f"<pisti> {message}", file=f)
    f.close

if __name__ == "__main__":
    main()