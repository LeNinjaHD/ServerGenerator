import urllib.request 
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

print("ServerGenerator v1.0 made by LeNinjaHD")
print("")

print("Welcome! Select a action:")
print("1: Generate A New Server")
print("2: Purge Server Directory")
print("3: Quit")
selection = input("> ")
match selection:
    case "2":
        os.remove("server/paper.jar")
        os.remove("server/server.properties")
        os.remove("server/start.sh")
        print("Purge Complete.")
        cls()
        quit()
    case "3":
        cls()
        quit()
    case "1":
        print("What Server Version do you want to use? do you want to use? (Possible Answers: latest, 1.16.5, 1.12.2, 1.8.8)")
        version = input("> ")
        print("")

        match version:
            case "latest":
                file = "https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/388/downloads/paper-1.17.1-388.jar"
            case "1.16.5":
                file = "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/790/downloads/paper-1.16.5-790.jar"
            case "1.12.2":
                file = "https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar"
            case "1.8.8":
                file = "https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar"

        print("How do you want to name the Server?")
        name = input("> ")
        print("")

        print("On What port should your server run on?")
        port = input("> ")
        print("")

        print("What do you want the MOTD to be?")
        motd = input("> ")
        print("")

        print("How much RAM do you want your sever to use? (In GB, example input: 2)")
        ram = input("> ")
        print("")

        print("Creating Start Script...")
        startscript = "screen -S {} java -Xmx{}G -Xms{}G -jar paper.jar -nogui".format(name, ram, ram)
        f = open("server/start.sh", "w")
        f.write(startscript)
        f.close()
        print("Created!")
        print("")

        print("Creating Server Properties")
        f = open("server/server.properties", "w")
        f.write("server-port={}\n".format(port))
        f.write("motd={}".format(motd))
        f.close()
        print("Created!")
        print("")

        print("Downloading server jar")
        urllib.request.urlretrieve(file, "./server/paper.jar")
        print("Done! Your server is in the server/ Directory")
        time.sleep(1)
        cls()
        quit()